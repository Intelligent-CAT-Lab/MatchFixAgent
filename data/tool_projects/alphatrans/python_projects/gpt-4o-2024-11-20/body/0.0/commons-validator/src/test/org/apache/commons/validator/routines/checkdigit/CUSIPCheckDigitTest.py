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
from src.main.org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *


class CUSIPCheckDigitTest(AbstractCheckDigitTest, unittest.TestCase):

    __validCheckDigits: List[str] = ["DUS0421C5"]
    __invalidCheckDigits: List[str] = ["DUS0421CW", "DUS0421CN", "DUS0421CE"]

    def testVALIDATOR_336_ValidCheckDigits_test0_decomposed(self) -> None:
        for validCheckDigit in self.__validCheckDigits:
            self.assertTrue(
                self._routine.isValid(validCheckDigit),
                f"Should fail: {validCheckDigit}",
            )

    def testVALIDATOR_336_InvalidCheckDigits_test0_decomposed(self) -> None:
        for invalidCheckDigit in self.__invalidCheckDigits:
            self.assertFalse(
                self._routine.isValid(invalidCheckDigit),
                f"Should fail: {invalidCheckDigit}",
            )

    def setUp(self) -> None:
        super().setUp()
        self.routine = CUSIPCheckDigit.CUSIP_CHECK_DIGIT
        self.valid = [
            "037833100",
            "931142103",
            "837649128",
            "392690QT3",
            "594918104",
            "86770G101",
            "Y8295N109",
            "G8572F100",
        ]
        self.invalid = ["0378#3100"]
