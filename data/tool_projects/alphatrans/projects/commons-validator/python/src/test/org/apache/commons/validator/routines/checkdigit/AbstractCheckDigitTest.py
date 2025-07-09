from __future__ import annotations
import re
import os
import enum
from io import BytesIO
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class AbstractCheckDigitTest(unittest.TestCase, ABC):

    _missingMessage: str = "Code is missing"
    _zeroSum: str = "0000000000"
    _invalid: typing.List[str] = ["12345678A"]
    _valid: typing.List[typing.List[str]] = None

    _routine: CheckDigit = None

    _checkDigitLth: int = 1
    _log: logging.Logger = logging.getLogger(__name__)
    __POSSIBLE_CHECK_DIGITS: str = (
        "0123456789 ABCDEFHIJKLMNOPQRSTUVWXYZ\tabcdefghijklmnopqrstuvwxyz!@£$%^&*()_+"
    )

    def tearDown(self) -> None:
        super().tearDown()
        self._valid = None
        self._routine = None

    def _checkDigit(self, code: str) -> str:
        if code is None or len(code) <= self._checkDigitLth:
            return ""
        start = len(code) - self._checkDigitLth
        return code[start:]

    def _removeCheckDigit(self, code: str) -> str:
        if code is None or len(code) <= self._checkDigitLth:
            return None
        return code[: len(code) - self._checkDigitLth]

    def _createInvalidCodes(self, codes: List[str]) -> List[str]:
        invalid_codes = []

        for full_code in codes:
            code = self._removeCheckDigit(full_code)
            check = self._checkDigit(full_code)
            for curr in self.__POSSIBLE_CHECK_DIGITS:
                if curr != check:
                    invalid_codes.append(code + curr)

        return invalid_codes

    def testSerialization(self) -> None:
        baos = io.BytesIO()
        try:
            # Serialize the routine object
            oos = io.BufferedWriter(baos)
            import pickle

            pickle.dump(self._routine, oos)
            oos.flush()
            oos.close()
        except Exception as e:
            pytest.fail(
                f"{self._routine.__class__.__name__} error during serialization: {e}"
            )

        result = None
        try:
            # Deserialize the routine object
            bais = io.BytesIO(baos.getvalue())
            ois = io.BufferedReader(bais)
            result = pickle.load(ois)
            bais.close()
        except Exception as e:
            pytest.fail(
                f"{self._routine.__class__.__name__} error during deserialization: {e}"
            )

        self.assertIsNotNone(result)

    def testZeroSum(self) -> None:
        self.assertFalse(self._routine.isValid(self._zeroSum), "isValid() Zero Sum")

        with self.assertRaises(Exception) as context:
            self._routine.calculate(self._zeroSum)

        self.assertEqual(
            "Invalid code, sum is zero", str(context.exception), "isValid() Zero Sum"
        )

    def testMissingCode(self) -> None:
        self.assertFalse(self._routine.isValid(None), "isValid() Null")
        self.assertFalse(self._routine.isValid(""), "isValid() Zero Length")
        self.assertFalse(self._routine.isValid("9"), "isValid() Length 1")

        with self.assertRaises(Exception) as context:
            self._routine.calculate(None)
        self.assertEqual(
            self._missingMessage, str(context.exception), "calculate() Null"
        )

        with self.assertRaises(Exception) as context:
            self._routine.calculate("")
        self.assertEqual(
            self._missingMessage, str(context.exception), "calculate() Zero Length"
        )

    def testCalculateInvalid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                f"testCalculateInvalid() for {self._routine.__class__.__name__}"
            )

        for i, code in enumerate(self._invalid):
            try:
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(
                        f"   {i} Testing Invalid Check Digit, Code=[{code}]"
                    )

                expected = self._checkDigit(code)
                actual = self._routine.calculate(self._removeCheckDigit(code))

                if expected == actual:
                    pytest.fail(
                        f"Expected mismatch for {code} expected {expected} actual {actual}"
                    )
            except CheckDigitException as e:
                self.assertTrue(
                    e.args[0].startswith("Invalid "),
                    f"Invalid Character[{i}]={e.args[0]}",
                )

    def testCalculateValid(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                f"testCalculateValid() for {self._routine.__class__.__name__}"
            )

        for i, valid_code in enumerate(self._valid):
            code = self._removeCheckDigit(valid_code)
            expected = self._checkDigit(valid_code)
            try:
                if self._log.isEnabledFor(logging.DEBUG):
                    self._log.debug(
                        f"   {i} Testing Valid Check Digit, Code=[{code}] expected=[{expected}]"
                    )
                self.assertEqual(
                    expected, self._routine.calculate(code), f"valid[{i}]: {valid_code}"
                )
            except Exception as e:
                self.fail(f"valid[{i}]={valid_code} threw {e}")

    def testIsValidFalse(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(
                f"testIsValidFalse() for {self._routine.__class__.__name__}"
            )

        for i, invalid_code in enumerate(self._invalid):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"   {i} Testing Invalid Code=[{invalid_code}]")
            self.assertFalse(
                self._routine.isValid(invalid_code), f"invalid[{i}]: {invalid_code}"
            )

        invalid_check_digits = self._createInvalidCodes(self._valid)
        for i, invalid_check_digit in enumerate(invalid_check_digits):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(
                    f"   {i} Testing Invalid Check Digit, Code=[{invalid_check_digit}]"
                )
            self.assertFalse(
                self._routine.isValid(invalid_check_digit),
                f"invalid check digit[{i}]: {invalid_check_digit}",
            )

    def testIsValidTrue(self) -> None:
        if self._log.isEnabledFor(logging.DEBUG):
            self._log.debug(f"testIsValidTrue() for {self._routine.__class__.__name__}")

        for i, valid_code in enumerate(self._valid):
            if self._log.isEnabledFor(logging.DEBUG):
                self._log.debug(f"   {i} Testing Valid Code=[{valid_code}]")
            self.assertTrue(
                self._routine.isValid(valid_code), f"valid[{i}]: {valid_code}"
            )
