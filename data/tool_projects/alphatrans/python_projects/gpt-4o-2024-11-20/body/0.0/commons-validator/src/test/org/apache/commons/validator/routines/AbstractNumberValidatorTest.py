from __future__ import annotations
import locale
import re
import pickle
import os
import enum
from io import BytesIO
import unittest
import pytest
from abc import ABC
import io
import numbers
import typing
from typing import *
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *


class AbstractNumberValidatorTest(unittest.TestCase, ABC):

    _localeExpected: typing.Union[int, float, numbers.Number] = None

    _testLocale: typing.Any = None

    _localePattern: str = ""

    _localeValue: str = ""

    _testStringDE: str = ""

    _testStringUS: str = ""

    _testZero: typing.Union[int, float, numbers.Number] = None

    _testNumber: typing.Union[int, float, numbers.Number] = None

    _testPattern: str = ""

    _validStrictCompare: typing.List[typing.Union[int, float, numbers.Number]] = None

    _validStrict: typing.List[typing.List[str]] = None

    _invalidStrict: typing.List[typing.List[str]] = None

    _validCompare: typing.List[typing.Union[int, float, numbers.Number]] = None

    _valid: typing.List[typing.List[str]] = None

    _invalid: typing.List[typing.List[str]] = None

    _minMinusOne: typing.Union[int, float, numbers.Number] = None

    _min: typing.Union[int, float, numbers.Number] = None

    _maxPlusOne: typing.Union[int, float, numbers.Number] = None

    _max: typing.Union[int, float, numbers.Number] = None

    _strictValidator: AbstractNumberValidator = None

    _validator: AbstractNumberValidator = None

    def tearDown(self) -> None:
        super().tearDown()
        self._validator = None
        self._strictValidator = None

    def setUp(self) -> None:
        super().setUp()
        locale.setlocale(locale.LC_ALL, "en_US")

    def testSerialization(self) -> None:
        baos = io.BytesIO()
        try:
            oos = pickle.Pickler(baos)
            oos.dump(self._validator)
            oos.clear_memo()
        except Exception as e:
            pytest.fail(
                f"{self._validator.__class__.__name__} error during serialization: {e}"
            )

        result = None
        try:
            bais = io.BytesIO(baos.getvalue())
            ois = pickle.Unpickler(bais)
            result = ois.load()
        except Exception as e:
            pytest.fail(
                f"{self._validator.__class__.__name__} error during deserialization: {e}"
            )

        self.assertIsNotNone(result)

    def testRangeMinMax(self) -> None:
        number9 = 9
        number10 = 10
        number11 = 11
        number19 = 19
        number20 = 20
        number21 = 21

        self.assertFalse(
            self._strictValidator.isInRange(number9, number10, number20),
            "isInRange() < min",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number10, number10, number20),
            "isInRange() = min",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number11, number10, number20),
            "isInRange() in range",
        )
        self.assertTrue(
            self._strictValidator.isInRange(number20, number10, number20),
            "isInRange() = max",
        )
        self.assertFalse(
            self._strictValidator.isInRange(number21, number10, number20),
            "isInRange() > max",
        )

        self.assertFalse(
            self._strictValidator.minValue(number9, number10), "minValue() < min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number10, number10), "minValue() = min"
        )
        self.assertTrue(
            self._strictValidator.minValue(number11, number10), "minValue() > min"
        )

        self.assertTrue(
            self._strictValidator.maxValue(number19, number20), "maxValue() < max"
        )
        self.assertTrue(
            self._strictValidator.maxValue(number20, number20), "maxValue() = max"
        )
        self.assertFalse(
            self._strictValidator.maxValue(number21, number20), "maxValue() > max"
        )

    def testFormat(self) -> None:
        number = Decimal("1234.5")
        self.assertEqual(
            "1,234.5",
            self._strictValidator.format2(number, Locale.US),
            "US Locale, US Format",
        )
        self.assertEqual(
            "1.234,5",
            self._strictValidator.format2(number, Locale.GERMAN),
            "DE Locale, DE Format",
        )
        self.assertEqual(
            "12,34.50",
            self._strictValidator.format1(number, "#,#0.00"),
            "Pattern #,#0.00",
        )

    def testValidateLocale(self) -> None:
        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, Locale.US),
            "US Locale, US Format",
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringDE, None, Locale.US),
            "US Locale, DE Format",
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringDE, None, Locale.GERMAN),
            "DE Locale, DE Format",
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringUS, None, Locale.GERMAN),
            "DE Locale, US Format",
        )

        self.assertEqual(
            self._testNumber,
            self._strictValidator.parse(self._testStringUS, None, None),
            "Default Locale, US Format",
        )
        self.assertIsNone(
            self._strictValidator.parse(self._testStringDE, None, None),
            "Default Locale, DE Format",
        )

    def testValidNotStrict(self) -> None:
        for i in range(len(self._valid)):
            text = f"idx=[{i}] value=[{self._validCompare[i]}]"
            self.assertEqual(
                self._validCompare[i],
                self._validator._parse(self._valid[i], None, Locale.US),
                f"(A) {text}",
            )
            self.assertTrue(
                self._validator.isValid3(self._valid[i], None, Locale.US), f"(B) {text}"
            )
            self.assertEqual(
                self._validCompare[i],
                self._validator._parse(self._valid[i], self._testPattern, None),
                f"(C) {text}",
            )
            self.assertTrue(
                self._validator.isValid3(self._valid[i], self._testPattern, None),
                f"(D) {text}",
            )

    def testValidStrict(self) -> None:
        for i in range(len(self._validStrict)):
            text = f"idx=[{i}] value=[{self._validStrictCompare[i]}]"
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator._parse(
                    self._validStrict[i], None, locale=Locale.US
                ),
                f"(A) {text}",
            )
            self.assertTrue(
                self._strictValidator.isValid3(
                    self._validStrict[i], None, locale=Locale.US
                ),
                f"(B) {text}",
            )
            self.assertEqual(
                self._validStrictCompare[i],
                self._strictValidator._parse(
                    self._validStrict[i], self._testPattern, None
                ),
                f"(C) {text}",
            )
            self.assertTrue(
                self._strictValidator.isValid3(
                    self._validStrict[i], self._testPattern, None
                ),
                f"(D) {text}",
            )

    def testInvalidNotStrict(self) -> None:
        for i, invalid_value in enumerate(self._invalid):
            text = f"idx=[{i}] value=[{invalid_value}]"
            self.assertIsNone(
                self._validator._parse(invalid_value, None, Locale.US), f"(A) {text}"
            )
            self.assertFalse(
                self._validator.isValid3(invalid_value, None, Locale.US), f"(B) {text}"
            )
            self.assertIsNone(
                self._validator._parse(invalid_value, self._testPattern, None),
                f"(C) {text}",
            )
            self.assertFalse(
                self._validator.isValid3(invalid_value, self._testPattern, None),
                f"(D) {text}",
            )

    def testInvalidStrict(self) -> None:
        for i, value in enumerate(self._invalidStrict):
            text = f"idx=[{i}] value=[{value}]"
            self.assertIsNone(
                self._strictValidator._parse(value, None, Locale.US), f"(A) {text}"
            )
            self.assertFalse(
                self._strictValidator.isValid3(value, None, Locale.US), f"(B) {text}"
            )
            self.assertIsNone(
                self._strictValidator._parse(value, self._testPattern, None),
                f"(C) {text}",
            )
            self.assertFalse(
                self._strictValidator.isValid3(value, self._testPattern, None),
                f"(D) {text}",
            )

    def testValidateMinMax(self) -> None:
        fmt = "{:.0f}"  # Equivalent to DecimalFormat("#") in Java
        if self._max is not None:
            # Test Max
            self.assertEqual(
                self._max,
                self._validator._parse(fmt.format(self._max), "#", None),
                "Test Max",
            )
            # Test Max + 1
            self.assertIsNone(
                self._validator._parse(fmt.format(self._maxPlusOne), "#", None),
                "Test Max + 1",
            )
            # Test Min
            self.assertEqual(
                self._min,
                self._validator._parse(fmt.format(self._min), "#", None),
                "Test Min",
            )
            # Test Min - 1
            self.assertIsNone(
                self._validator._parse(fmt.format(self._minMinusOne), "#", None),
                "Test min - 1",
            )

    def testFormatType(self) -> None:
        self.assertEqual(0, self._validator.getFormatType(), "Format Type A")
        self.assertEqual(
            AbstractNumberValidator.STANDARD_FORMAT,
            self._validator.getFormatType(),
            "Format Type B",
        )
