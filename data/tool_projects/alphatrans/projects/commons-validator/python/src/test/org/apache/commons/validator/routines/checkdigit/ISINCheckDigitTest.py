from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *


class ISINCheckDigitTest(AbstractCheckDigitTest, unittest.TestCase):

    __invalidCheckDigits: List[str] = [
        "US037833100O",  # proper check digit is '5', see above
        "BMG8571G109D",  # proper check digit is '6', see above
        "AU0000XVGZAD",  # proper check digit is '3', see above
        "GB000263494I",  # proper check digit is '6', see above
        "FR000402625C",  # proper check digit is '0', see above
        "DK000976334H",  # proper check digit is '4', see above
    ]

    def testVALIDATOR_345_test0_decomposed(self) -> None:
        for invalid_check_digit in self.__invalidCheckDigits:
            self.assertFalse(
                self._routine.isValid(invalid_check_digit),
                f"Should fail: {invalid_check_digit}",
            )

    def setUp(self) -> None:
        super().setUp()
        self.routine = ISINCheckDigit.ISIN_CHECK_DIGIT
        self.valid = [
            "US0378331005",
            "BMG8571G1096",
            "AU0000XVGZA3",
            "GB0002634946",
            "FR0004026250",
            "3133EHHF3",  # see VALIDATOR-422 Valid check-digit, but not valid ISIN
            "DK0009763344",
            "dk0009763344",  # TODO lowercase is currently accepted, but is this valid?
            "AU0000xvgza3",  # lowercase NSIN
            "EZ0000000003",  # Invented; for use in ISINValidatorTest
            "XS0000000009",  # ditto
            "AA0000000006",  # ditto
        ]
        self.invalid = ["0378#3100"]
