from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *


class CreditCardValidatorTest(unittest.TestCase):

    __VALID_DINERS: str = "30569309025904"
    __VALID_DISCOVER: str = "6011000990139424"
    __VALID_MASTERCARD: str = "5105105105105100"
    __VALID_AMEX: str = "378282246310005"
    __VALID_SHORT_VISA: str = "4222222222222"
    __VALID_VISA: str = "4417123456789113"

    def testAddAllowedCardType_test3_decomposed(self) -> None:
        ccv = CreditCardValidator(CreditCardValidator.NONE)
        self.assertFalse(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        ccv.addAllowedCardType(DinersClub())
        self.assertTrue(ccv.isValid(self.__VALID_DINERS))

    def testAddAllowedCardType_test2_decomposed(self) -> None:
        ccv = CreditCardValidator(CreditCardValidator.NONE)
        self.assertFalse(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        ccv.addAllowedCardType(DinersClub())

    def testAddAllowedCardType_test1_decomposed(self) -> None:
        ccv = CreditCardValidator(CreditCardValidator.NONE)
        self.assertFalse(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))

    def testAddAllowedCardType_test0_decomposed(self) -> None:
        ccv = CreditCardValidator(CreditCardValidator.NONE)

    def testIsValid_test3_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator1()
        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012"))
        self.assertFalse(ccv.isValid("12345678901234567890"))
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertTrue(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER))
        ccv = CreditCardValidator(CreditCardValidator.AMEX)
        self.assertFalse(ccv.isValid("4417123456789113"))

    def testIsValid_test2_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator1()
        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012"))
        self.assertFalse(ccv.isValid("12345678901234567890"))
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertTrue(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER))
        ccv = CreditCardValidator(CreditCardValidator.AMEX)

    def testIsValid_test1_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator1()
        self.assertFalse(ccv.isValid(None))
        self.assertFalse(ccv.isValid(""))
        self.assertFalse(ccv.isValid("123456789012"))
        self.assertFalse(ccv.isValid("12345678901234567890"))
        self.assertFalse(ccv.isValid("4417123456789112"))
        self.assertFalse(ccv.isValid("4417q23456w89113"))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertTrue(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER))

    def testIsValid_test0_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator1()


class DinersClub(CreditCardType):

    __PREFIX: str = "300,301,302,303,304,305,"

    def matches(self, card: str) -> bool:
        prefix = card[:3] + ","
        return (prefix in self.__PREFIX) and (len(card) == 14)
