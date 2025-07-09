from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.test.org.apache.commons.validator.routines.checkdigit.AbstractCheckDigitTest import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *


class ISBNCheckDigitTest(AbstractCheckDigitTest, unittest.TestCase):

    def testInvalidLength_test1_decomposed(self) -> None:
        self.assertFalse(self._routine.isValid("123456789"), "isValid() Lth 9")
        self.assertFalse(self._routine.isValid("12345678901"), "isValid() Lth 11")
        self.assertFalse(self._routine.isValid("123456789012"), "isValid() Lth 12")
        self.assertFalse(self._routine.isValid("12345678901234"), "isValid() Lth 14")

        with pytest.raises(Exception) as excinfo:
            self._routine.calculate("12345678")
        self.assertEqual(
            str(excinfo.value), "Invalid ISBN Length = 8", "calculate() Lth 8"
        )

        with pytest.raises(Exception) as excinfo:
            self._routine.calculate("1234567890")
        self.assertEqual(
            str(excinfo.value), "Invalid ISBN Length = 10", "calculate() Lth 10"
        )

        with pytest.raises(Exception) as excinfo:
            self._routine.calculate("12345678901")
        self.assertEqual(
            str(excinfo.value), "Invalid ISBN Length = 11", "calculate() Lth 11"
        )

        with pytest.raises(Exception) as excinfo:
            self._routine.calculate("1234567890123")
        self.assertEqual(
            str(excinfo.value), "Invalid ISBN Length = 13", "calculate() Lth 13"
        )

    def testInvalidLength_test0_decomposed(self) -> None:
        self.assertFalse(self._routine.isValid("123456789"), "isValid() Lth 9 ")
        self.assertFalse(self._routine.isValid("12345678901"), "isValid() Lth 11")
        self.assertFalse(self._routine.isValid("123456789012"), "isValid() Lth 12")
        self.assertFalse(self._routine.isValid("12345678901234"), "isValid() Lth 14")

    def setUp(self) -> None:
        super().setUp()
        self._routine = ISBNCheckDigit.ISBN_CHECK_DIGIT
        self._valid = [
            "9780072129519",
            "9780764558313",
            "1930110995",
            "020163385X",
            "1590596277",  # ISBN-10 Ubuntu Book
            "9781590596272",  # ISBN-13 Ubuntu Book
        ]
        self._missingMessage = "ISBN Code is missing"
        self._zeroSum = "000000000000"
