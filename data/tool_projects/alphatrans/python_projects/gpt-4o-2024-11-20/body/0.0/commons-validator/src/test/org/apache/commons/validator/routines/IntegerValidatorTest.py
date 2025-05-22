from __future__ import annotations
import locale
import re
import unittest
import pytest
import io
import numbers
import os
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.IntegerValidator import *


class IntegerValidatorTest(AbstractNumberValidatorTest, unittest.TestCase):

    __INT_MIN_1: str = "-2147483649"
    __INT_MIN_0: str = "-2147483648.99999999999999999999999"  # force double rounding
    __INT_MIN: str = "-2147483648"
    __INT_MAX_1: str = "2147483648"
    __INT_MAX_0: str = "2147483647.99999999999999999999999"
    __INT_MAX: str = "2147483647"
    __INT_MAX_VAL: int = 2147483647
    __INT_MIN_VAL: int = -2147483648

    def testMinMaxValues_test0_decomposed(self) -> None:
        self.assertTrue(
            self._validator.isValid0("2147483647"), "2147483647 is max integer"
        )
        self.assertFalse(
            self._validator.isValid0("2147483648"), "2147483648 > max integer"
        )
        self.assertTrue(
            self._validator.isValid0("-2147483648"), "-2147483648 is min integer"
        )
        self.assertFalse(
            self._validator.isValid0("-2147483649"), "-2147483649 < min integer"
        )

    def testIntegerRangeMinMax_test4_decomposed(self) -> None:
        validator: IntegerValidator = (
            self._strictValidator
        )  # Assuming _strictValidator is set up correctly
        number9: int = validator.validate1("9", "#")
        number10: int = validator.validate1("10", "#")
        number11: int = validator.validate1("11", "#")
        number19: int = validator.validate1("19", "#")
        number20: int = validator.validate1("20", "#")
        number21: int = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

        self.assertFalse(validator.minValue1(number9, 10), "minValue() < min")
        self.assertTrue(validator.minValue1(number10, 10), "minValue() = min")
        self.assertTrue(validator.minValue1(number11, 10), "minValue() > min")

        self.assertTrue(validator.maxValue1(number19, 20), "maxValue() < max")
        self.assertTrue(validator.maxValue1(number20, 20), "maxValue() = max")
        self.assertFalse(validator.maxValue1(number21, 20), "maxValue() > max")

    def testIntegerRangeMinMax_test3_decomposed(self) -> None:
        validator: IntegerValidator = (
            self._strictValidator
        )  # Assuming _strictValidator is an instance of IntegerValidator
        number9: int = validator.validate1("9", "#")
        number10: int = validator.validate1("10", "#")
        number11: int = validator.validate1("11", "#")
        number19: int = validator.validate1("19", "#")
        number20: int = validator.validate1("20", "#")
        number21: int = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

        self.assertFalse(validator.minValue1(number9, 10), "minValue() < min")
        self.assertTrue(validator.minValue1(number10, 10), "minValue() = min")
        self.assertTrue(validator.minValue1(number11, 10), "minValue() > min")

    def testIntegerRangeMinMax_test2_decomposed(self) -> None:
        validator: IntegerValidator = self._strictValidator  # Cast to IntegerValidator
        number9: int = validator.validate1("9", "#")
        number10: int = validator.validate1("10", "#")
        number11: int = validator.validate1("11", "#")
        number19: int = validator.validate1("19", "#")
        number20: int = validator.validate1("20", "#")
        number21: int = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

    def testIntegerRangeMinMax_test1_decomposed(self) -> None:
        validator: IntegerValidator = self._strictValidator  # Cast to IntegerValidator
        number9: int = validator.validate1("9", "#")
        number10: int = validator.validate1("10", "#")
        number11: int = validator.validate1("11", "#")
        number19: int = validator.validate1("19", "#")
        number20: int = validator.validate1("20", "#")
        number21: int = validator.validate1("21", "#")

    def testIntegerRangeMinMax_test0_decomposed(self) -> None:
        validator: IntegerValidator = (
            self._strictValidator
        )  # Cast _strictValidator to IntegerValidator
        if validator is not None:
            number9: int = validator.validate1("9", "#")
        else:
            raise AttributeError(
                "'_strictValidator' is None and cannot be cast to IntegerValidator"
            )

    def testIntegerValidatorMethods_test31_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # Validate methods
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid methods
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate methods with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid methods with invalid input
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")
        self.assertFalse(
            validator.isValid3(pattern_val, pattern, Locale.GERMAN), "isValid(B) both"
        )

    def testIntegerValidatorMethods_test30_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # Validate methods
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid methods
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate methods with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid methods with invalid input
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testIntegerValidatorMethods_test29_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # validate(A) tests
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) tests
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) tests
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid(B) tests
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testIntegerValidatorMethods_test28_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # validate(A) tests
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) tests
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) tests
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid(B) tests
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

    def testIntegerValidatorMethods_test27_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # Validate methods
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid methods
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate methods with invalid input
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid methods with invalid input
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

    def testIntegerValidatorMethods_test26_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

    def testIntegerValidatorMethods_test25_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # validate(A) pattern
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

        # isValid(B) default
        self.assertFalse(validator.isValid0(XXXX), "isValid(B) default")

    def testIntegerValidatorMethods_test24_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # validate(A) pattern
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

    def testIntegerValidatorMethods_test23_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # validate(A) pattern
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid(A) locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid(A) pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # isValid(A) both
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # validate(B) locale
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

        # validate(B) pattern
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

        # validate(B) both
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

    def testIntegerValidatorMethods_test22_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

    def testIntegerValidatorMethods_test21_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

    def testIntegerValidatorMethods_test20_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

    def testIntegerValidatorMethods_test19_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

    def testIntegerValidatorMethods_test18_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

    def testIntegerValidatorMethods_test17_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        # Validate using default
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default
        self.assertTrue(
            IntegerValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            IntegerValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            IntegerValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check validity using both pattern and locale
        self.assertTrue(
            IntegerValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input
        self.assertIsNone(
            IntegerValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

    def testIntegerValidatorMethods_test16_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

    def testIntegerValidatorMethods_test15_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

    def testIntegerValidatorMethods_test14_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) in Java translates to a plain integer in Python

        validator = IntegerValidator.getInstance()

        # validate0 (default)
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # validate2 (locale)
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # validate1 (pattern)
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # validate3 (pattern and locale)
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid0 (default)
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # isValid2 (locale)
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # isValid1 (pattern)
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

    def testIntegerValidatorMethods_test13_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) in Java translates to a plain integer in Python

        # Validate using default
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check validity using default
        self.assertTrue(
            IntegerValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check validity using locale
        self.assertTrue(
            IntegerValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check validity using pattern
        self.assertTrue(
            IntegerValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

    def testIntegerValidatorMethods_test12_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

    def testIntegerValidatorMethods_test11_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

    def testIntegerValidatorMethods_test10_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        validator = IntegerValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

    def testIntegerValidatorMethods_test9_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) in Java translates to a plain integer in Python

        validator = IntegerValidator.getInstance()

        # validate(A) default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # validate(A) locale
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # validate(A) pattern
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # validate(A) both
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

    def testIntegerValidatorMethods_test8_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        # Validate default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate with locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate with pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

    def testIntegerValidatorMethods_test7_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345

        # Validate using default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

    def testIntegerValidatorMethods_test6_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python

        # Validate using default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testIntegerValidatorMethods_test5_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python

        # Validate using default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testIntegerValidatorMethods_test4_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python

        # Validate using default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

    def testIntegerValidatorMethods_test3_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) in Java translates to a plain integer in Python

        # Validate using default value
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            IntegerValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

    def testIntegerValidatorMethods_test2_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python

        # Get the instance of IntegerValidator
        validator = IntegerValidator.getInstance()

        # Validate the default value
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testIntegerValidatorMethods_test1_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python

        # Get the instance of IntegerValidator
        validator = IntegerValidator.getInstance()

        # Assert that the validation works as expected
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testIntegerValidatorMethods_test0_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Integer.valueOf(12345) equivalent in Python
        IntegerValidator.getInstance()

    def setUp(self) -> None:
        super().setUp()

        self._validator = IntegerValidator(False, 0)
        self._strictValidator = IntegerValidator.IntegerValidator1()

        self._testPattern = "#,###"

        self._max = 2147483647  # 2147483647
        self._maxPlusOne = self._max + 1
        self._min = -2147483648  # -2147483648
        self._minMinusOne = self._min - 1

        self._invalidStrict = [
            None,
            "",
            "X",
            "X12",
            "12X",
            "1X2",
            "1.2",
            self.__INT_MAX_1,
            self.__INT_MIN_1,
        ]

        self._invalid = [None, "", "X", "X12", self.__INT_MAX_1, self.__INT_MIN_1]

        self._testNumber = 1234
        self._testZero = 0
        self._validStrict = ["0", "1234", "1,234", self.__INT_MAX, self.__INT_MIN]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
        ]
        self._valid = [
            "0",
            "1234",
            "1,234",
            "1,234.5",
            "1234X",
            self.__INT_MAX,
            self.__INT_MIN,
            self.__INT_MAX_0,
            self.__INT_MIN_0,
        ]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
            self.__INT_MAX_VAL,
            self.__INT_MIN_VAL,
        ]

        self._testStringUS = "1,234"
        self._testStringDE = "1.234"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###"
        self._testLocale = "de_DE"  # Locale.GERMANY
        self._localeExpected = self._testNumber
