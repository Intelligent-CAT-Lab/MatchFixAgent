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
from src.main.org.apache.commons.validator.routines.DoubleValidator import *


class DoubleValidatorTest(AbstractNumberValidatorTest, unittest.TestCase):

    def testDoubleRangeMinMax_test4_decomposed(self) -> None:
        validator: DoubleValidator = self._strictValidator  # Cast to DoubleValidator
        number9: float = validator.validate1("9", "#")
        number10: float = validator.validate1("10", "#")
        number11: float = validator.validate1("11", "#")
        number19: float = validator.validate1("19", "#")
        number20: float = validator.validate1("20", "#")
        number21: float = validator.validate1("21", "#")

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

    def testDoubleRangeMinMax_test3_decomposed(self) -> None:
        validator: DoubleValidator = self._strictValidator  # Cast to DoubleValidator
        number9: float = validator.validate1("9", "#")
        number10: float = validator.validate1("10", "#")
        number11: float = validator.validate1("11", "#")
        number19: float = validator.validate1("19", "#")
        number20: float = validator.validate1("20", "#")
        number21: float = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

        self.assertFalse(validator.minValue1(number9, 10), "minValue() < min")
        self.assertTrue(validator.minValue1(number10, 10), "minValue() = min")
        self.assertTrue(validator.minValue1(number11, 10), "minValue() > min")

    def testDoubleRangeMinMax_test2_decomposed(self) -> None:
        validator: DoubleValidator = (
            self._strictValidator
        )  # Assuming _strictValidator is an instance of DoubleValidator
        number9: float = validator.validate1("9", "#")
        number10: float = validator.validate1("10", "#")
        number11: float = validator.validate1("11", "#")
        number19: float = validator.validate1("19", "#")
        number20: float = validator.validate1("20", "#")
        number21: float = validator.validate1("21", "#")

        self.assertFalse(validator.isInRange1(number9, 10, 20), "isInRange() < min")
        self.assertTrue(validator.isInRange1(number10, 10, 20), "isInRange() = min")
        self.assertTrue(validator.isInRange1(number11, 10, 20), "isInRange() in range")
        self.assertTrue(validator.isInRange1(number20, 10, 20), "isInRange() = max")
        self.assertFalse(validator.isInRange1(number21, 10, 20), "isInRange() > max")

    def testDoubleRangeMinMax_test1_decomposed(self) -> None:
        validator: DoubleValidator = self._strictValidator  # Cast to DoubleValidator
        number9: float = validator.validate1("9", "#")
        number10: float = validator.validate1("10", "#")
        number11: float = validator.validate1("11", "#")
        number19: float = validator.validate1("19", "#")
        number20: float = validator.validate1("20", "#")
        number21: float = validator.validate1("21", "#")

    def testDoubleRangeMinMax_test0_decomposed(self) -> None:
        validator: DoubleValidator = (
            self._strictValidator
        )  # Cast _strictValidator to DoubleValidator
        if validator is not None:
            number9: float = validator.validate1("9", "#")
        else:
            raise AttributeError(
                "'_strictValidator' is None and cannot be used for validation"
            )

    def testDoubleValidatorMethods_test31_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        # Validate default
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate with locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate with pattern
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # isValid checks for valid inputs
        self.assertTrue(
            DoubleValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )
        self.assertTrue(
            DoubleValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input (XXXX)
        self.assertIsNone(
            DoubleValidator.getInstance().validate0(XXXX), "validate(B) default"
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate2(XXXX, locale), "validate(B) locale"
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern",
        )
        self.assertIsNone(
            DoubleValidator.getInstance().validate3(
                pattern_val, pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # isValid checks for invalid inputs
        self.assertFalse(
            DoubleValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid2(XXXX, locale), "isValid(B) locale"
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid1(XXXX, pattern), "isValid(B) pattern"
        )
        self.assertFalse(
            DoubleValidator.getInstance().isValid3(pattern_val, pattern, Locale.GERMAN),
            "isValid(B) both",
        )

    def testDoubleValidatorMethods_test30_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test29_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test28_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test27_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test26_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test25_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test24_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        validator = DoubleValidator.getInstance()

        # Validate with default
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Validate with locale
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

        # Validate with pattern
        self.assertEqual(
            expected, validator.validate1(pattern_val, pattern), "validate(A) pattern"
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            validator.validate3(german_pattern_val, pattern, Locale.GERMAN),
            "validate(A) both",
        )

        # Check validity with default
        self.assertTrue(validator.isValid0(default_val), "isValid(A) default")

        # Check validity with locale
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale")

        # Check validity with pattern
        self.assertTrue(validator.isValid1(pattern_val, pattern), "isValid(A) pattern")

        # Check validity with both pattern and locale
        self.assertTrue(
            validator.isValid3(german_pattern_val, pattern, Locale.GERMAN),
            "isValid(A) both",
        )

        # Validate invalid input with default
        self.assertIsNone(validator.validate0(XXXX), "validate(B) default")

        # Validate invalid input with locale
        self.assertIsNone(validator.validate2(XXXX, locale), "validate(B) locale")

        # Validate invalid input with pattern
        self.assertIsNone(validator.validate1(XXXX, pattern), "validate(B) pattern")

        # Validate invalid input with both pattern and locale
        self.assertIsNone(
            validator.validate3(pattern_val, pattern, Locale.GERMAN), "validate(B) both"
        )

    def testDoubleValidatorMethods_test23_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        # Validate default
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate with locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate with pattern
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate with both pattern and locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check isValid for default
        self.assertTrue(
            DoubleValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

        # Check isValid with locale
        self.assertTrue(
            DoubleValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # Check isValid with pattern
        self.assertTrue(
            DoubleValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # Check isValid with both pattern and locale
        self.assertTrue(
            DoubleValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # Validate invalid input (default)
        self.assertIsNone(
            DoubleValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # Validate invalid input (locale)
        self.assertIsNone(
            DoubleValidator.getInstance().validate2(XXXX, locale), "validate(B) locale"
        )

        # Validate invalid input (pattern)
        self.assertIsNone(
            DoubleValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern",
        )

        # Validate invalid input (both pattern and locale)
        self.assertIsNone(
            DoubleValidator.getInstance().validate3(
                pattern_val, pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

    def testDoubleValidatorMethods_test22_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test21_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test20_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test19_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test18_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test17_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test16_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test15_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test14_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test13_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Double in Java corresponds to float in Python

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test12_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale "
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
        self.assertTrue(validator.isValid2(locale_val, locale), "isValid(A) locale ")

    def testDoubleValidatorMethods_test11_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = (
            12345.0  # Double.valueOf(12345) in Java translates to a float in Python
        )

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test10_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = (
            12345.0  # Double.valueOf(12345) in Java translates to a float in Python
        )

        # Validate using default value
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check if the default value is valid
        self.assertTrue(
            DoubleValidator.getInstance().isValid0(default_val), "isValid(A) default"
        )

    def testDoubleValidatorMethods_test9_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test8_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test7_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0

        validator = DoubleValidator.getInstance()

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

    def testDoubleValidatorMethods_test6_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Double.valueOf(12345) equivalent in Python

        # Validate using default value
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testDoubleValidatorMethods_test5_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = (
            12345.0  # Double.valueOf(12345) in Java translates to a float in Python
        )

        # Validate using default value
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testDoubleValidatorMethods_test4_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Double in Java corresponds to float in Python

        # Validate using default value
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

    def testDoubleValidatorMethods_test3_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        # Validate using default value
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            DoubleValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

    def testDoubleValidatorMethods_test2_decomposed(self) -> None:
        locale = "de_DE"  # Representing Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        # Get an instance of DoubleValidator
        validator = DoubleValidator.getInstance()

        # Validate the default value and assert the result
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testDoubleValidatorMethods_test1_decomposed(self) -> None:
        locale = "de_DE"  # Representing Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Equivalent to Double.valueOf(12345) in Java

        # Get the instance of DoubleValidator
        validator = DoubleValidator.getInstance()

        # Ensure the validator instance is not None
        self.assertIsNotNone(validator, "DoubleValidator instance is None")

        # Perform the assertion
        result = validator.validate0(default_val)
        self.assertIsNotNone(result, "Validation result is None")

        # Perform the assertion
        self.assertEqual(expected, result, "validate(A) default")

    def testDoubleValidatorMethods_test0_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345.0  # Double.valueOf(12345) equivalent in Python
        DoubleValidator.getInstance()

    def setUp(self) -> None:
        super().setUp()

        self._validator = DoubleValidator(False, 0)
        self._strictValidator = DoubleValidator.DoubleValidator1()

        self._testPattern = "#,###.#"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = 1234.5
        self._testZero = 0.0
        self._validStrict = ["0", "1234.5", "1,234.5"]
        self._validStrictCompare = [self._testZero, self._testNumber, self._testNumber]
        self._valid = ["0", "1234.5", "1,234.5", "1,234.5", "1234.5X"]
        self._validCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            self._testNumber,
            self._testNumber,
        ]

        self._testStringUS = "1,234.5"
        self._testStringDE = "1.234,5"

        self._localeValue = self._testStringDE
        self._localePattern = "#.###,#"
        self._testLocale = Locale.GERMANY
        self._localeExpected = self._testNumber
