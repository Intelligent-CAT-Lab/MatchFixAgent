from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *


class CodeValidatorTest(unittest.TestCase):

    def testConstructors_test33_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 6 - regex",
        )
        self.assertEqual(10, validator.getMinLength(), "Constructor 6 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 6 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 6 - check digit",
        )

    def testConstructors_test32_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 6 - regex",
        )
        self.assertEqual(10, validator.getMinLength(), "Constructor 6 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 6 - max length")

    def testConstructors_test31_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 6 - regex",
        )
        self.assertEqual(10, validator.getMinLength(), "Constructor 6 - min length")

    def testConstructors_test30_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 6 - regex",
        )

    def testConstructors_test29_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        validator.getRegexValidator()

    def testConstructors_test28_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )

    def testConstructors_test27_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit",
        )

    def testConstructors_test26_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")

    def testConstructors_test25_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")

    def testConstructors_test24_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex",
        )

    def testConstructors_test23_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        validator.getRegexValidator()

    def testConstructors_test22_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

    def testConstructors_test21_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit",
        )

    def testConstructors_test20_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")

    def testConstructors_test19_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")

    def testConstructors_test18_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex",
        )

    def testConstructors_test17_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertIsNotNone(validator.getRegexValidator())

    def testConstructors_test16_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

    def testConstructors_test15_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit",
        )

    def testConstructors_test14_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")

    def testConstructors_test13_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")

    def testConstructors_test12_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")

    def testConstructors_test11_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )

    def testConstructors_test10_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit",
        )

    def testConstructors_test9_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )
        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")

    def testConstructors_test8_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")

    def testConstructors_test7_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")

    def testConstructors_test6_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

    def testConstructors_test5_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit",
        )

    def testConstructors_test4_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")

    def testConstructors_test3_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")

    def testConstructors_test2_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")

    def testConstructors_test1_decomposed(self) -> None:
        validator: CodeValidator = None
        regex: RegexValidator = RegexValidator.RegexValidator3("^[0-9]*$")
        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

    def testConstructors_test0_decomposed(self) -> None:
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")

    def testValidator294_2_test1_decomposed(self) -> None:
        validator = CodeValidator(0, None, 0, None, -1, None)
        self.assertEqual(None, validator.validate(None))

    def testValidator294_2_test0_decomposed(self) -> None:
        validator = CodeValidator(3, None, 0, None, -1, None)

    def testValidator294_1_test3_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual(None, validator.validate(None), "Null")

        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual(None, validator.validate(None), "Null")

    def testValidator294_1_test2_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual(None, validator.validate(None), "Null")
        validator = CodeValidator(3, None, 0, None, -1, None)

    def testValidator294_1_test1_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual(None, validator.validate(None), "Null")

    def testValidator294_1_test0_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, 0, None)

    def testNoInput_test1_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        self.assertEqual(None, validator.validate(None), "Null")
        self.assertEqual(None, validator.validate(""), "Zero Length")
        self.assertEqual(None, validator.validate("   "), "Spaces")
        self.assertEqual("A", validator.validate(" A  "), "Trimmed")

    def testNoInput_test0_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)

    def testRegex_test13_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

        regex = r"^(?:([0-9]{3})(?:[-\s])([0-9]{3}))|([0-9]{6})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual(
            f"RegexValidator{{{regex}}}",
            validator.getRegexValidator().toString(),
            "Reformat 2 Regex",
        )
        self.assertEqual("123456", validator.validate("123-456"), "Reformat 2 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 2 123 456")
        self.assertEqual("123456", validator.validate("123456"), "Reformat 2 123456")

    def testRegex_test12_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

        regex = r"^(?:([0-9]{3})(?:[-\s])([0-9]{3}))|([0-9]{6})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual(
            f"RegexValidator{{{regex}}}",
            validator.getRegexValidator().toString(),
            "Reformat 2 Regex",
        )

    def testRegex_test11_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(None, validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertEqual(None, validator.validate(value5), "Regex 5")
        self.assertEqual(None, validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertEqual(None, validator.validate("123456"), "Reformat 123456")
        self.assertEqual(None, validator.validate("123.456"), "Reformat 123.456")

        regex = r"^(?:([0-9]{3})(?:[-\s])([0-9]{3}))|([0-9]{6})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        validator.getRegexValidator()

    def testRegex_test10_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)
        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

        regex = r"^(?:([0-9]{3})(?:[-\s])([0-9]{3}))|([0-9]{6})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

    def testRegex_test9_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

        regex = r"^(?:([0-9]{3})(?:[-\s])([0-9]{3}))|([0-9]{6})$"
        RegexValidator.RegexValidator3(regex)

    def testRegex_test8_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

    def testRegex_test7_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        regex_validator = RegexValidator.RegexValidator3(regex)
        validator = CodeValidator.CodeValidator1(regex_validator, 6, None)

    def testRegex_test6_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        # Assertions for no regex
        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        # Setting regex and testing
        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        # Setting a new regex and testing
        regex = r"^([0-9]{3})(?:[-\s])([0-9]{3})$"
        RegexValidator.RegexValidator3(regex)

    def testRegex_test5_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        # Assertions for no regex
        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        # Setting regex
        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

        # Assertions for regex
        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

    def testRegex_test4_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")

    def testRegex_test3_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        # Assert that the regex validator is None
        self.assertIsNone(validator.getRegexValidator(), "No Regex")

        # Validate values and assert equality
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        # Set a regex and reinitialize the validator
        regex = r"^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)

    def testRegex_test2_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

    def testRegex_test1_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"
        self.assertIsNone(validator.getRegexValidator(), "No Regex")

    def testRegex_test0_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)

    def testLength_test19_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(
            length_11, validator.validate(length_11), "Min 11 / Max 21 - 11"
        )
        self.assertEqual(
            length_12, validator.validate(length_12), "Min 11 / Max 21 - 12"
        )
        self.assertEqual(
            length_20, validator.validate(length_20), "Min 11 / Max 21 - 20"
        )
        self.assertEqual(
            length_21, validator.validate(length_21), "Min 11 / Max 21 - 21"
        )
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Exact 11 - min")
        self.assertEqual(11, validator.getMaxLength(), "Exact 11 - max")
        self.assertIsNone(validator.validate(length_10), "Exact 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Exact 11 - 11")
        self.assertIsNone(validator.validate(length_12), "Exact 11 - 12")

    def testLength_test18_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(
            length_11, validator.validate(length_11), "Min 11 / Max 21 - 11"
        )
        self.assertEqual(
            length_12, validator.validate(length_12), "Min 11 / Max 21 - 12"
        )
        self.assertEqual(
            length_20, validator.validate(length_20), "Min 11 / Max 21 - 20"
        )
        self.assertEqual(
            length_21, validator.validate(length_21), "Min 11 / Max 21 - 21"
        )
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Exact 11 - min")
        self.assertEqual(11, validator.getMaxLength(), "Exact 11 - max")

    def testLength_test17_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(
            length_11, validator.validate(length_11), "Min 11 / Max 21 - 11"
        )
        self.assertEqual(
            length_12, validator.validate(length_12), "Min 11 / Max 21 - 12"
        )
        self.assertEqual(
            length_20, validator.validate(length_20), "Min 11 / Max 21 - 20"
        )
        self.assertEqual(
            length_21, validator.validate(length_21), "Min 11 / Max 21 - 21"
        )
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Exact 11 - min")

    def testLength_test16_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(
            length_11, validator.validate(length_11), "Min 11 / Max 21 - 11"
        )
        self.assertEqual(
            length_12, validator.validate(length_12), "Min 11 / Max 21 - 12"
        )
        self.assertEqual(
            length_20, validator.validate(length_20), "Min 11 / Max 21 - 20"
        )
        self.assertEqual(
            length_21, validator.validate(length_21), "Min 11 / Max 21 - 21"
        )
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

        validator = CodeValidator(3, None, 11, None, 11, None)

    def testLength_test15_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(
            length_11, validator.validate(length_11), "Min 11 / Max 21 - 11"
        )
        self.assertEqual(
            length_12, validator.validate(length_12), "Min 11 / Max 21 - 12"
        )
        self.assertEqual(
            length_20, validator.validate(length_20), "Min 11 / Max 21 - 20"
        )
        self.assertEqual(
            length_21, validator.validate(length_21), "Min 11 / Max 21 - 21"
        )
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

    def testLength_test14_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertEqual(None, validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertEqual(None, validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")

    def testLength_test13_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")

    def testLength_test12_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)

    def testLength_test11_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

    def testLength_test10_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")

    def testLength_test9_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")

    def testLength_test8_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)

    def testLength_test7_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

    def testLength_test6_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")

    def testLength_test5_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")

    def testLength_test4_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)

    def testLength_test3_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")
        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

    def testLength_test2_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"
        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")

    def testLength_test1_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"
        self.assertEqual(-1, validator.getMinLength(), "No min")

    def testLength_test0_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)

    def testCheckDigit_test8_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), True, "No CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validator.validate(validEAN), validEAN, "EAN CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), False, "EAN CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "EAN CheckDigit (is) valid")
        self.assertIsNone(validator.validate("978193011099X"), "EAN CheckDigit ex")

    def testCheckDigit_test7_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        # Assertions for the first validator
        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            invalidEAN, validator.validate(invalidEAN), "No CheckDigit invalid"
        )
        self.assertEqual(validEAN, validator.validate(validEAN), "No CheckDigit valid")
        self.assertTrue(validator.isValid(invalidEAN), "No CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "No CheckDigit (is) valid")

        # Create a new validator with EAN13CheckDigit
        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        # Assertions for the second validator
        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validEAN, validator.validate(validEAN), "EAN CheckDigit valid")
        self.assertFalse(validator.isValid(invalidEAN), "EAN CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "EAN CheckDigit (is) valid")

    def testCheckDigit_test6_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), True, "No CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validator.validate(validEAN), validEAN, "EAN CheckDigit valid")

    def testCheckDigit_test5_decomposed(self) -> None:
        validator = CodeValidator(0, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), True, "No CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")

    def testCheckDigit_test4_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), True, "No CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

    def testCheckDigit_test3_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertEqual(
            validator.isValid(invalidEAN), True, "No CheckDigit (is) invalid"
        )
        self.assertEqual(validator.isValid(validEAN), True, "No CheckDigit (is) valid")

    def testCheckDigit_test2_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            invalidEAN, validator.validate(invalidEAN), "No CheckDigit invalid"
        )
        self.assertEqual(validEAN, validator.validate(validEAN), "No CheckDigit valid")

    def testCheckDigit_test1_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"
        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")

    def testCheckDigit_test0_decomposed(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:
        super().setUp()
