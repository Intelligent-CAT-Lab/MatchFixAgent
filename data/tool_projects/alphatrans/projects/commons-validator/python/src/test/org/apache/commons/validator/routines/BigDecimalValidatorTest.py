from __future__ import annotations
import locale
import re
import decimal
import unittest
import pytest
import io
import numbers
import os
import unittest
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.test.org.apache.commons.validator.routines.AbstractNumberValidatorTest import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class BigDecimalValidatorTest(AbstractNumberValidatorTest, unittest.TestCase):

    def testBigDecimalRangeMinMax_test4_decomposed(self) -> None:
        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")
        min_ = 10
        max_ = 20

        self.assertFalse(validator.isInRange(number9, min_, max_), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, min_, max_), "isInRange(A) = min")
        self.assertTrue(
            validator.isInRange(number11, min_, max_), "isInRange(A) in range"
        )
        self.assertTrue(validator.isInRange(number20, min_, max_), "isInRange(A) = max")
        self.assertFalse(
            validator.isInRange(number21, min_, max_), "isInRange(A) > max"
        )
        self.assertFalse(validator.minValue(number9, min_), "minValue(A) < min")
        self.assertTrue(validator.minValue(number10, min_), "minValue(A) = min")
        self.assertTrue(validator.minValue(number11, min_), "minValue(A) > min")
        self.assertTrue(validator.maxValue(number19, max_), "maxValue(A) < max")
        self.assertTrue(validator.maxValue(number20, max_), "maxValue(A) = max")
        self.assertFalse(validator.maxValue(number21, max_), "maxValue(A) > max")

    def testBigDecimalRangeMinMax_test3_decomposed(self) -> None:
        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")
        min_ = 10
        max_ = 20

        self.assertFalse(validator.isInRange(number9, min_, max_), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, min_, max_), "isInRange(A) = min")
        self.assertTrue(
            validator.isInRange(number11, min_, max_), "isInRange(A) in range"
        )
        self.assertTrue(validator.isInRange(number20, min_, max_), "isInRange(A) = max")
        self.assertFalse(
            validator.isInRange(number21, min_, max_), "isInRange(A) > max"
        )
        self.assertFalse(validator.minValue(number9, min_), "minValue(A) < min")
        self.assertTrue(validator.minValue(number10, min_), "minValue(A) = min")
        self.assertTrue(validator.minValue(number11, min_), "minValue(A) > min")

    def testBigDecimalRangeMinMax_test2_decomposed(self) -> None:
        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")
        min_ = 10
        max_ = 20

        self.assertFalse(validator.isInRange(number9, min_, max_), "isInRange(A) < min")
        self.assertTrue(validator.isInRange(number10, min_, max_), "isInRange(A) = min")
        self.assertTrue(
            validator.isInRange(number11, min_, max_), "isInRange(A) in range"
        )
        self.assertTrue(validator.isInRange(number20, min_, max_), "isInRange(A) = max")
        self.assertFalse(
            validator.isInRange(number21, min_, max_), "isInRange(A) > max"
        )

    def testBigDecimalRangeMinMax_test1_decomposed(self) -> None:
        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )
        number9 = decimal.Decimal("9")
        number10 = decimal.Decimal("10")
        number11 = decimal.Decimal("11")
        number19 = decimal.Decimal("19")
        number20 = decimal.Decimal("20")
        number21 = decimal.Decimal("21")
        min_ = 10
        max_ = 20
        self.assertFalse(validator.isInRange(number9, min_, max_), "isInRange(A) < min")

    def testBigDecimalRangeMinMax_test0_decomposed(self) -> None:
        validator = BigDecimalValidator(
            True, AbstractNumberValidator.STANDARD_FORMAT, True
        )

    def testBigDecimalValidatorMethods_test31_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # isValid(B) pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

        # isValid(B) both
        self.assertFalse(
            validator.isValid3(pattern_val, pattern, Locale.GERMAN), "isValid(B) both"
        )

    def testBigDecimalValidatorMethods_test30_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # isValid(B) pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testBigDecimalValidatorMethods_test29_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)
        validator = BigDecimalValidator.getInstance()

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

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

        # isValid(B) pattern
        self.assertFalse(validator.isValid1(XXXX, pattern), "isValid(B) pattern")

    def testBigDecimalValidatorMethods_test28_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # validate(A) default
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid0(default_val),
            "isValid(A) default",
        )

        # isValid(A) locale
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # isValid(A) pattern
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # isValid(A) both
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # validate(B) locale
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale",
        )

        # validate(B) pattern
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern",
        )

        # validate(B) both
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate3(
                pattern_val, pattern, Locale.GERMAN
            ),
            "validate(B) both",
        )

        # isValid(B) default
        self.assertFalse(
            BigDecimalValidator.getInstance().isValid0(XXXX), "isValid(B) default"
        )

        # isValid(B) locale
        self.assertFalse(
            BigDecimalValidator.getInstance().isValid2(XXXX, locale),
            "isValid(B) locale",
        )

    def testBigDecimalValidatorMethods_test27_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

        # isValid(B) locale
        self.assertFalse(validator.isValid2(XXXX, locale), "isValid(B) locale")

    def testBigDecimalValidatorMethods_test26_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test25_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test24_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test23_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test22_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test21_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # validate(A) default
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # validate(A) locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # validate(A) pattern
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # validate(A) both
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # isValid(A) default
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid0(default_val),
            "isValid(A) default",
        )

        # isValid(A) locale
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid2(locale_val, locale),
            "isValid(A) locale",
        )

        # isValid(A) pattern
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid1(pattern_val, pattern),
            "isValid(A) pattern",
        )

        # isValid(A) both
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "isValid(A) both",
        )

        # validate(B) default
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate0(XXXX), "validate(B) default"
        )

        # validate(B) locale
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate2(XXXX, locale),
            "validate(B) locale",
        )

        # validate(B) pattern
        self.assertIsNone(
            BigDecimalValidator.getInstance().validate1(XXXX, pattern),
            "validate(B) pattern",
        )

    def testBigDecimalValidatorMethods_test20_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test19_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test18_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test17_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test16_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test15_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test14_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test13_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test12_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test11_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test10_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test9_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # Validate using default value
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

        # Validate using both pattern and locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate3(
                german_pattern_val, pattern, Locale.GERMAN
            ),
            "validate(A) both",
        )

        # Check if the default value is valid
        self.assertTrue(
            BigDecimalValidator.getInstance().isValid0(default_val),
            "isValid(A) default",
        )

    def testBigDecimalValidatorMethods_test8_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test7_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

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

    def testBigDecimalValidatorMethods_test6_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # Validate using default value
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testBigDecimalValidatorMethods_test5_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # Validate using default value
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

        # Validate using pattern
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate1(pattern_val, pattern),
            "validate(A) pattern",
        )

    def testBigDecimalValidatorMethods_test4_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        validator = BigDecimalValidator.getInstance()

        # Test validate0 with default value
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

        # Test validate2 with locale value
        self.assertEqual(
            expected, validator.validate2(locale_val, locale), "validate(A) locale"
        )

    def testBigDecimalValidatorMethods_test3_decomposed(self) -> None:
        locale = Locale.GERMAN
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # Validate using default value
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate0(default_val),
            "validate(A) default",
        )

        # Validate using locale
        self.assertEqual(
            expected,
            BigDecimalValidator.getInstance().validate2(locale_val, locale),
            "validate(A) locale",
        )

    def testBigDecimalValidatorMethods_test2_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent in Python
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)  # BigDecimal equivalent in Python

        # Get an instance of BigDecimalValidator
        validator = BigDecimalValidator.getInstance()

        # Validate using the default value
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testBigDecimalValidatorMethods_test1_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN equivalent
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = decimal.Decimal(12345)

        # Get an instance of BigDecimalValidator
        validator = BigDecimalValidator.getInstance()

        # Perform the validation and assert the result
        self.assertEqual(
            expected, validator.validate0(default_val), "validate(A) default"
        )

    def testBigDecimalValidatorMethods_test0_decomposed(self) -> None:
        locale = "de_DE"  # Locale.GERMAN in Java
        pattern = "0,00,00"
        pattern_val = "1,23,45"
        german_pattern_val = "1.23.45"
        locale_val = "12.345"
        default_val = "12,345"
        XXXX = "XXXX"
        expected = 12345  # Using a standard Python integer instead of BigDecimal
        BigDecimalValidator.getInstance()

    def setUp(self) -> None:
        super().setUp()

        self._validator = BigDecimalValidator.BigDecimalValidator1(False)
        self._strictValidator = BigDecimalValidator.BigDecimalValidator2()

        self._testPattern = "#,###.###"

        self._max = None
        self._maxPlusOne = None
        self._min = None
        self._minMinusOne = None

        self._invalidStrict = [None, "", "X", "X12", "12X", "1X2", "1.234X"]

        self._invalid = [None, "", "X", "X12"]

        self._testNumber = BigDecimal("1234.5")
        testNumber2 = BigDecimal(".1")
        testNumber3 = BigDecimal("12345.67899")
        self._testZero = BigDecimal("0")
        self._validStrict = ["0", "1234.5", "1,234.5", ".1", "12345.678990"]
        self._validStrictCompare = [
            self._testZero,
            self._testNumber,
            self._testNumber,
            testNumber2,
            testNumber3,
        ]
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
