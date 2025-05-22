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
from src.main.org.apache.commons.validator.routines.CurrencyValidator import *


class CurrencyValidatorTest(unittest.TestCase):

    __UK_POUND: str = ""

    __US_DOLLAR: str = ""

    __CURRENCY_SYMBOL: str = "\u00a4"

    def testPattern_test6_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basic_pattern + ";[" + basic_pattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")

        self.assertEqual(
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
            "negative",
        )
        self.assertEqual(
            expected, validator.validate1("1,234.567", pattern), "no symbol +ve"
        )
        self.assertEqual(
            negative, validator.validate1("[1,234.567]", pattern), "no symbol -ve"
        )
        self.assertEqual(
            expected,
            validator.validate3(self.__US_DOLLAR + "1,234.567", pattern, Locale.US),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate3(
                "[" + self.__US_DOLLAR + "1,234.567]", pattern, Locale.US
            ),
            "negative",
        )
        self.assertEqual(
            expected,
            validator.validate3("1,234.567", pattern, Locale.US),
            "no symbol +ve",
        )
        self.assertEqual(
            negative,
            validator.validate3("[1,234.567]", pattern, Locale.US),
            "no symbol -ve",
        )
        self.assertFalse(
            validator.isValid1(self.__US_DOLLAR + "1,234.567", pattern),
            "invalid symbol",
        )
        self.assertFalse(
            validator.isValid3(self.__UK_POUND + "1,234.567", pattern, Locale.US),
            "invalid symbol",
        )
        Locale.setDefault(orig_default)

    def testPattern_test5_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basic_pattern + ";[" + basic_pattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")

        self.assertEqual(
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
            "negative",
        )
        self.assertEqual(
            expected, validator.validate1("1,234.567", pattern), "no symbol +ve"
        )
        self.assertEqual(
            negative, validator.validate1("[1,234.567]", pattern), "no symbol -ve"
        )
        self.assertEqual(
            expected,
            validator.validate3(self.__US_DOLLAR + "1,234.567", pattern, Locale.US),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate3(
                "[" + self.__US_DOLLAR + "1,234.567]", pattern, Locale.US
            ),
            "negative",
        )
        self.assertEqual(
            expected,
            validator.validate3("1,234.567", pattern, Locale.US),
            "no symbol +ve",
        )
        self.assertEqual(
            negative,
            validator.validate3("[1,234.567]", pattern, Locale.US),
            "no symbol -ve",
        )
        self.assertFalse(
            validator.isValid1(self.__US_DOLLAR + "1,234.567", pattern),
            "invalid symbol",
        )
        self.assertFalse(
            validator.isValid3(self.__UK_POUND + "1,234.567", pattern, Locale.US),
            "invalid symbol",
        )

    def testPattern_test4_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basic_pattern + ";[" + basic_pattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")

        self.assertEqual(
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
            "negative",
        )
        self.assertEqual(
            expected, validator.validate1("1,234.567", pattern), "no symbol +ve"
        )
        self.assertEqual(
            negative, validator.validate1("[1,234.567]", pattern), "no symbol -ve"
        )
        self.assertEqual(
            expected,
            validator.validate3(self.__US_DOLLAR + "1,234.567", pattern, Locale.US),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate3(
                "[" + self.__US_DOLLAR + "1,234.567]", pattern, Locale.US
            ),
            "negative",
        )
        self.assertEqual(
            expected,
            validator.validate3("1,234.567", pattern, Locale.US),
            "no symbol +ve",
        )
        self.assertEqual(
            negative,
            validator.validate3("[1,234.567]", pattern, Locale.US),
            "no symbol -ve",
        )
        self.assertFalse(
            validator.isValid1(self.__US_DOLLAR + "1,234.567", pattern),
            "invalid symbol",
        )

    def testPattern_test3_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK
        validator = CurrencyValidator.getInstance()
        basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
        pattern = basic_pattern + ";[" + basic_pattern + "]"
        expected = decimal.Decimal("1234.567")
        negative = decimal.Decimal("-1234.567")

        # Test cases
        self.assertEqual(
            expected,
            validator.validate1(self.__UK_POUND + "1,234.567", pattern),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
            "negative",
        )
        self.assertEqual(
            expected, validator.validate1("1,234.567", pattern), "no symbol +ve"
        )
        self.assertEqual(
            negative, validator.validate1("[1,234.567]", pattern), "no symbol -ve"
        )
        self.assertEqual(
            expected,
            validator.validate3(
                self.__US_DOLLAR + "1,234.567", pattern, locale="en_US"
            ),
            "default",
        )
        self.assertEqual(
            negative,
            validator.validate3(
                "[" + self.__US_DOLLAR + "1,234.567]", pattern, locale="en_US"
            ),
            "negative",
        )
        self.assertEqual(
            expected,
            validator.validate3("1,234.567", pattern, locale="en_US"),
            "no symbol +ve",
        )
        self.assertEqual(
            negative,
            validator.validate3("[1,234.567]", pattern, locale="en_US"),
            "no symbol -ve",
        )

        # Restore original locale
        locale.setlocale(locale.LC_ALL, orig_default)

    def testPattern_test2_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Save the original locale
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK
        try:
            validator = CurrencyValidator.getInstance()
            basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
            pattern = basic_pattern + ";[" + basic_pattern + "]"
            expected = decimal.Decimal("1234.567")
            negative = decimal.Decimal("-1234.567")

            # Perform assertions
            self.assertEqual(
                expected,
                validator.validate1(self.__UK_POUND + "1,234.567", pattern),
                "default",
            )
            self.assertEqual(
                negative,
                validator.validate1("[" + self.__UK_POUND + "1,234.567]", pattern),
                "negative",
            )
            self.assertEqual(
                expected, validator.validate1("1,234.567", pattern), "no symbol +ve"
            )
            self.assertEqual(
                negative, validator.validate1("[1,234.567]", pattern), "no symbol -ve"
            )
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)  # Restore the original locale

    def testPattern_test1_decomposed(self) -> None:
        orig_default = locale.getlocale()  # Save the original locale
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")  # Set locale to UK
            validator = CurrencyValidator.getInstance()
            basic_pattern = self.__CURRENCY_SYMBOL + "#,##0.000"
            pattern = basic_pattern + ";[" + basic_pattern + "]"
            expected = decimal.Decimal("1234.567")
            self.assertEqual(
                expected,
                validator.validate1(self.__UK_POUND + "1,234.567", pattern),
                "default",
            )
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)  # Restore the original locale

    def testPattern_test0_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()

    def testIntegerInvalid_test1_decomposed(self) -> None:
        validator = CurrencyValidator(True, False)
        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", Locale.UK), "UK positive"
        )
        self.assertFalse(
            validator.isValid2("-" + self.__UK_POUND + "1,234.56", Locale.UK),
            "UK negative",
        )
        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", Locale.US), "US positive"
        )
        self.assertFalse(
            validator.isValid2("(" + self.__US_DOLLAR + "1,234.56)", Locale.US),
            "US negative",
        )

    def testIntegerInvalid_test0_decomposed(self) -> None:
        validator = CurrencyValidator(True, False)

    def testIntegerValid_test3_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB")  # Set locale to UK
        validator = CurrencyValidator.CurrencyValidator1()
        expected = decimal.Decimal("1234.00")
        negative = decimal.Decimal("-1234.00")

        # Default locale
        self.assertEqual(
            expected, validator.validate0(self.__UK_POUND + "1,234"), "Default locale"
        )

        # UK locale
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234", "en_GB"),
            "UK locale",
        )

        # UK negative
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234", "en_GB"),
            "UK negative",
        )

        # US locale
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234", "en_US"),
            "US locale",
        )

        # US negative
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234)", "en_US"),
            "US negative",
        )

        # Restore original locale
        locale.setlocale(locale.LC_ALL, orig_default)

    def testIntegerValid_test2_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.CurrencyValidator1()
        expected = decimal.Decimal("1234.00")
        negative = decimal.Decimal("-1234.00")

        self.assertEqual(
            expected, validator.validate0(self.__UK_POUND + "1,234"), "Default locale"
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234", Locale.UK),
            "UK locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234", Locale.UK),
            "UK negative",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234", Locale.US),
            "US locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234)", Locale.US),
            "US negative",
        )

    def testIntegerValid_test1_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Save the original locale
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")  # Set locale to UK
        try:
            validator = CurrencyValidator.CurrencyValidator1()
            expected = decimal.Decimal("1234.00")
            self.__UK_POUND = "£"  # Define the UK pound symbol
            self.assertEqual(
                expected,
                validator.validate0(self.__UK_POUND + "1,234"),
                "Default locale",
            )
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)  # Restore the original locale

    def testIntegerValid_test0_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()  # Get the original default locale
        try:
            locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")  # Set the locale to UK
            validator = (
                CurrencyValidator.CurrencyValidator1()
            )  # Create a CurrencyValidator instance
        finally:
            # Restore the original locale after the test
            locale.setlocale(locale.LC_ALL, orig_default)

    def testInvalid_test3_decomposed(self) -> None:
        validator = CurrencyValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")
        self.assertFalse(
            validator.isValid2(self.__US_DOLLAR + "1,234.56", Locale.UK),
            "UK wrong symbol",
        )
        self.assertFalse(
            validator.isValid2("(" + self.__UK_POUND + "1,234.56)", Locale.UK),
            "UK wrong negative",
        )
        self.assertFalse(
            validator.isValid2(self.__UK_POUND + "1,234.56", Locale.US),
            "US wrong symbol",
        )
        self.assertFalse(
            validator.isValid2("-" + self.__US_DOLLAR + "1,234.56", Locale.US),
            "US wrong negative",
        )

    def testInvalid_test2_decomposed(self) -> None:
        validator = CurrencyValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")
        self.assertIsNone(validator.validate0(None), "validate() Null Value")
        self.assertIsNone(validator.validate0(""), "validate() Empty Value")

    def testInvalid_test1_decomposed(self) -> None:
        validator = CurrencyValidator.getInstance()
        self.assertFalse(validator.isValid0(None), "isValid() Null Value")
        self.assertFalse(validator.isValid0(""), "isValid() Empty Value")

    def testInvalid_test0_decomposed(self) -> None:
        validator = CurrencyValidator.getInstance()

    def testValid_test3_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        expected = decimal.Decimal("1234.56")
        negative = decimal.Decimal("-1234.56")
        no_decimal = decimal.Decimal("1234.00")
        one_decimal = decimal.Decimal("1234.50")

        self.assertEqual(
            expected,
            validator.validate0(self.__UK_POUND + "1,234.56"),
            "Default locale",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.56", Locale.UK),
            "UK locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234.56", Locale.UK),
            "UK negative",
        )
        self.assertEqual(
            no_decimal,
            validator.validate2(self.__UK_POUND + "1,234", Locale.UK),
            "UK no decimal",
        )
        self.assertEqual(
            one_decimal,
            validator.validate2(self.__UK_POUND + "1,234.5", Locale.UK),
            "UK 1 decimal",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.567", Locale.UK),
            "UK 3 decimal",
        )
        self.assertEqual(
            expected, validator.validate2("1,234.56", Locale.UK), "UK no symbol"
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.56", Locale.US),
            "US locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234.56)", Locale.US),
            "US negative",
        )
        self.assertEqual(
            no_decimal,
            validator.validate2(self.__US_DOLLAR + "1,234", Locale.US),
            "US no decimal",
        )
        self.assertEqual(
            one_decimal,
            validator.validate2(self.__US_DOLLAR + "1,234.5", Locale.US),
            "US 1 decimal",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.567", Locale.US),
            "US 3 decimal",
        )
        self.assertEqual(
            expected, validator.validate2("1,234.56", Locale.US), "US no symbol"
        )
        Locale.setDefault(orig_default)

    def testValid_test2_decomposed(self) -> None:
        orig_default = Locale.getDefault()
        Locale.setDefault(Locale.UK)
        validator = CurrencyValidator.getInstance()
        expected = decimal.Decimal("1234.56")
        negative = decimal.Decimal("-1234.56")
        no_decimal = decimal.Decimal("1234.00")
        one_decimal = decimal.Decimal("1234.50")

        self.assertEqual(
            expected,
            validator.validate0(self.__UK_POUND + "1,234.56"),
            "Default locale",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.56", Locale.UK),
            "UK locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("-" + self.__UK_POUND + "1,234.56", Locale.UK),
            "UK negative",
        )
        self.assertEqual(
            no_decimal,
            validator.validate2(self.__UK_POUND + "1,234", Locale.UK),
            "UK no decimal",
        )
        self.assertEqual(
            one_decimal,
            validator.validate2(self.__UK_POUND + "1,234.5", Locale.UK),
            "UK 1 decimal",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__UK_POUND + "1,234.567", Locale.UK),
            "UK 3 decimal",
        )
        self.assertEqual(
            expected, validator.validate2("1,234.56", Locale.UK), "UK no symbol"
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.56", Locale.US),
            "US locale",
        )
        self.assertEqual(
            negative,
            validator.validate2("(" + self.__US_DOLLAR + "1,234.56)", Locale.US),
            "US negative",
        )
        self.assertEqual(
            no_decimal,
            validator.validate2(self.__US_DOLLAR + "1,234", Locale.US),
            "US no decimal",
        )
        self.assertEqual(
            one_decimal,
            validator.validate2(self.__US_DOLLAR + "1,234.5", Locale.US),
            "US 1 decimal",
        )
        self.assertEqual(
            expected,
            validator.validate2(self.__US_DOLLAR + "1,234.567", Locale.US),
            "US 3 decimal",
        )
        self.assertEqual(
            expected, validator.validate2("1,234.56", Locale.US), "US no symbol"
        )

    def testValid_test1_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        try:
            validator = CurrencyValidator.getInstance()
            expected = decimal.Decimal("1234.56")
            negative = decimal.Decimal("-1234.56")
            no_decimal = decimal.Decimal("1234.00")
            one_decimal = decimal.Decimal("1234.50")
            self.assertEqual(
                expected,
                validator.validate0(self.__UK_POUND + "1,234.56"),
                "Default locale",
            )
        finally:
            locale.setlocale(locale.LC_ALL, orig_default)

    def testValid_test0_decomposed(self) -> None:
        orig_default = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")
        validator = CurrencyValidator.getInstance()
        # Reset the locale to the original default after the test
        locale.setlocale(locale.LC_ALL, orig_default)

    def testFormatType_test3_decomposed(self) -> None:
        CurrencyValidator.getInstance()
        self.assertEqual(
            1, CurrencyValidator.getInstance().getFormatType(), "Format Type A"
        )
        CurrencyValidator.getInstance()
        self.assertEqual(
            AbstractNumberValidator.CURRENCY_FORMAT,
            CurrencyValidator.getInstance().getFormatType(),
            "Format Type B",
        )

    def testFormatType_test2_decomposed(self) -> None:
        CurrencyValidator.getInstance()
        self.assertEqual(
            1, CurrencyValidator.getInstance().getFormatType(), "Format Type A"
        )
        CurrencyValidator.getInstance()

    def testFormatType_test1_decomposed(self) -> None:
        CurrencyValidator.getInstance()
        self.assertEqual(
            1, CurrencyValidator.getInstance().getFormatType(), "Format Type A"
        )

    def testFormatType_test0_decomposed(self) -> None:
        CurrencyValidator.getInstance()

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:
        super().setUp()
        self.__US_DOLLAR = DecimalFormatSymbols(Locale.US).getCurrencySymbol()
        self.__UK_POUND = DecimalFormatSymbols(Locale.UK).getCurrencySymbol()
