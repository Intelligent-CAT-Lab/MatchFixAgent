from __future__ import annotations
import locale
import re
import decimal
import numbers
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.PercentValidator import *


class PercentValidatorTest(unittest.TestCase):

    _validator: PercentValidator = None

    def testInvalid_test3_decomposed(self) -> None:
        validator = PercentValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")
        self.assertFalse(validator.isValid2("12@", Locale.UK), "UK wrong symbol")
        self.assertFalse(validator.isValid2("(12%)", Locale.UK), "UK wrong negative")
        self.assertFalse(validator.isValid2("12@", Locale.US), "US wrong symbol")
        self.assertFalse(validator.isValid2("(12%)", Locale.US), "US wrong negative")

    def testInvalid_test2_decomposed(self) -> None:
        validator = PercentValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")

    def testInvalid_test1_decomposed(self) -> None:
        validator = PercentValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")

    def testInvalid_test0_decomposed(self) -> None:
        validator: BigDecimalValidator = PercentValidator.getInstance()

    def testValid_test5_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = PercentValidator.getInstance()
        expected = decimal.Decimal("0.12")
        negative = decimal.Decimal("-0.12")
        hundred = decimal.Decimal("1.00")

        self.assertEqual(expected, validator.validate0("12%"), "Default locale")
        self.assertEqual(negative, validator.validate0("-12%"), "Default negtve")
        self.assertEqual(expected, validator.validate2("12%", Locale.UK), "UK locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.UK), "UK negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.UK), "UK No symbol")
        self.assertEqual(expected, validator.validate2("12%", Locale.US), "US locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.US), "US negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.US), "US No symbol")
        self.assertEqual(hundred, validator.validate0("100%"), "100%")

        Locale.setDefault(orig_default)

    def testValid_test4_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = PercentValidator.getInstance()
        expected = decimal.Decimal("0.12")
        negative = decimal.Decimal("-0.12")
        hundred = decimal.Decimal("1.00")

        self.assertEqual(expected, validator.validate0("12%"), "Default locale")
        self.assertEqual(negative, validator.validate0("-12%"), "Default negtve")
        self.assertEqual(expected, validator.validate2("12%", Locale.UK), "UK locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.UK), "UK negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.UK), "UK No symbol")
        self.assertEqual(expected, validator.validate2("12%", Locale.US), "US locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.US), "US negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.US), "US No symbol")
        self.assertEqual(hundred, validator.validate0("100%"), "100%")

    def testValid_test3_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = PercentValidator.getInstance()
        expected = decimal.Decimal("0.12")
        negative = decimal.Decimal("-0.12")
        hundred = decimal.Decimal("1.00")

        self.assertEqual(expected, validator.validate0("12%"), "Default locale")
        self.assertEqual(negative, validator.validate0("-12%"), "Default negtve")
        self.assertEqual(expected, validator.validate2("12%", Locale.UK), "UK locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.UK), "UK negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.UK), "UK No symbol")
        self.assertEqual(expected, validator.validate2("12%", Locale.US), "US locale")
        self.assertEqual(
            negative, validator.validate2("-12%", Locale.US), "US negative"
        )
        self.assertEqual(expected, validator.validate2("12", Locale.US), "US No symbol")

    def testValid_test2_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Get the original default locale
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set the locale to UK
        try:
            validator = PercentValidator.getInstance()
            expected = decimal.Decimal("0.12")
            negative = decimal.Decimal("-0.12")
            hundred = decimal.Decimal("1.00")
            self.assertEqual(expected, validator.validate0("12%"), "Default locale")
            self.assertEqual(negative, validator.validate0("-12%"), "Default negtve")
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)  # Restore the original locale

    def testValid_test1_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Get the original default locale
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set the locale to UK
        try:
            validator = (
                PercentValidator.getInstance()
            )  # Get the PercentValidator instance
            expected = decimal.Decimal("0.12")  # Expected value
            negative = decimal.Decimal(
                "-0.12"
            )  # Negative value (not used in this test)
            hundred = decimal.Decimal(
                "1.00"
            )  # Hundred percent value (not used in this test)
            self.assertEqual(
                expected, validator.validate0("12%"), "Default locale"
            )  # Assert that the validation result matches the expected value
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)  # Restore the original locale

    def testValid_test0_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Get the original default locale
        try:
            locale.setlocale(
                locale.LC_ALL, "en_GB.UTF-8"
            )  # Set the locale to UK with UTF-8 encoding
            validator = (
                PercentValidator.getInstance()
            )  # Get an instance of PercentValidator
        finally:
            locale.setlocale(
                locale.LC_ALL, orig_default
            )  # Restore the original locale after the test

    def testFormatType_test3_decomposed(self) -> None:
        PercentValidator.getInstance()
        self.assertEqual(
            2, PercentValidator.getInstance().getFormatType(), "Format Type A"
        )
        PercentValidator.getInstance()
        self.assertEqual(
            AbstractNumberValidator.PERCENT_FORMAT,
            PercentValidator.getInstance().getFormatType(),
            "Format Type B",
        )

    def testFormatType_test2_decomposed(self) -> None:
        PercentValidator.getInstance()
        self.assertEqual(
            2, PercentValidator.getInstance().getFormatType(), "Format Type A"
        )
        PercentValidator.getInstance()

    def testFormatType_test1_decomposed(self) -> None:
        validator = PercentValidator.getInstance()
        self.assertEqual(2, validator.getFormatType(), "Format Type A")

    def testFormatType_test0_decomposed(self) -> None:
        PercentValidator.getInstance()

    def tearDown(self) -> None:
        super().tearDown()
        self._validator = None

    def setUp(self) -> None:
        super().setUp()
        self._validator = PercentValidator.PercentValidator1()
