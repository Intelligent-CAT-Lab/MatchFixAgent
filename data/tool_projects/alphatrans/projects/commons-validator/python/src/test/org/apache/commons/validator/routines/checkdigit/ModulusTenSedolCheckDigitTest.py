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
from src.main.org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit import *


class ModulusTenSedolCheckDigitTest(AbstractCheckDigitTest, unittest.TestCase):

    __invalidCheckDigits: List[str] = [
        "026349E",  # proper check digit is '4', see above
        "087061C",  # proper check digit is '2', see above
        "B06LQ9H",  # proper check digit is '7', see above
        "343757F",  # proper check digit is '5', see above
        "B07LF5F",  # proper check digit is '5', see above
    ]

    def testVALIDATOR_346_test0_decomposed(self) -> None:
        for invalidCheckDigit in self.__invalidCheckDigits:
            self.assertFalse(
                self._routine.isValid(invalidCheckDigit),
                f"Should fail: {invalidCheckDigit}",
            )

    def setUp(self) -> None:
        super().setUp()
        self._routine = ModulusTenCheckDigit.ModulusTenCheckDigit2(
            [1, 3, 1, 7, 3, 9, 1]
        )
        self._valid = [
            "0263494",
            "0870612",
            "B06LQ97",
            "3437575",
            "B07LF55",
        ]
        self._invalid = ["123#567"]
        self._zeroSum = "0000000"
