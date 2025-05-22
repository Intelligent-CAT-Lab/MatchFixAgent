from __future__ import annotations
import re
import numbers
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

    __ERROR_CARDS: List[str] = [
        "4417123456789112",  # ERROR_VISA
        "4222222222229",  # ERROR_SHORT_VISA
        "378282246310001",  # ERROR_AMEX
        "5105105105105105",  # ERROR_MASTERCARD
        "6011000990139421",  # ERROR_DISCOVER
        "6534567890123450",  # ERROR_DISCOVER65
        "30569309025901",  # ERROR_DINERS
        "4370000000000069",  # ERROR_VPAY
        "",
        "12345678901",  # too short (11)
        "12345678901234567890",  # too long (20)
        "4417123456789112",  # invalid check digit
    ]
    __VALID_CARDS: List[str] = [
        "4417123456789113",  # VALID_VISA
        "4222222222222",  # VALID_SHORT_VISA
        "378282246310005",  # VALID_AMEX
        "5105105105105100",  # VALID_MASTERCARD
        "6011000990139424",  # VALID_DISCOVER
        "6534567890123458",  # VALID_DISCOVER65
        "30569309025904",  # VALID_DINERS
        "4370000000000061",  # VALID_VPAY
        "4370000000000012",  # VALID_VPAY2
        "60115564485789458",  # VALIDATOR-403
    ]
    __ERROR_VPAY: str = "4370000000000069"
    __VALID_VPAY2: str = "4370000000000012"
    __VALID_VPAY: str = "4370000000000061"
    __ERROR_DINERS: str = "30569309025901"
    __VALID_DINERS: str = "30569309025904"
    __ERROR_DISCOVER65: str = (
        "6534567890123450"  # FIXME need verified test data for Discover with "65" prefix
    )
    __VALID_DISCOVER65: str = (
        "6534567890123458"  # FIXME need verified test data for Discover with "65" prefix
    )
    __ERROR_DISCOVER: str = "6011000990139421"
    __VALID_DISCOVER: str = "6011000990139424"
    __ERROR_MASTERCARD: str = "5105105105105105"
    __VALID_MASTERCARD: str = "5105105105105100"
    __ERROR_AMEX: str = "378282246310001"
    __VALID_AMEX: str = "378282246310005"
    __ERROR_SHORT_VISA: str = "4222222222229"
    __VALID_SHORT_VISA: str = "4222222222222"
    __ERROR_VISA: str = "4417123456789112"
    __VALID_VISA: str = "4417123456789113"

    def testDisjointRange_test5_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))
        self.assertEqual(14, len(self.__VALID_DINERS))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))

        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 14, 16]),
            ],
            None,
        )
        self.assertTrue(ccv.isValid(self.__VALID_DINERS))

    def testDisjointRange_test4_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))
        self.assertEqual(14, len(self.__VALID_DINERS))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))

        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 14, 16]),
            ],
            None,
        )

    def testDisjointRange_test3_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))
        self.assertEqual(14, len(self.__VALID_DINERS))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))

    def testDisjointRange_test2_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))
        self.assertEqual(14, len(self.__VALID_DINERS))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))

    def testDisjointRange_test1_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )
        self.assertEqual(13, len(self.__VALID_SHORT_VISA))
        self.assertEqual(16, len(self.__VALID_VISA))

    def testDisjointRange_test0_decomposed(self) -> None:
        ccv = CreditCardValidator(
            2,
            0,
            [
                CreditCardRange(1, "305", "4", 0, 0, [13, 16]),
            ],
            None,
        )

    def testValidLength_test12_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                16, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testValidLength_test11_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                16, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testValidLength_test10_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                16, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testValidLength_test9_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testValidLength_test8_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(1, "", "", 0, 0, [15, 17])
            )
        )

    def testValidLength_test7_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                18, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

    def testValidLength_test6_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                17, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

    def testValidLength_test5_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                16, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

    def testValidLength_test4_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )
        self.assertTrue(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

    def testValidLength_test3_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 15, 17, None)
            )
        )

    def testValidLength_test2_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                13, CreditCardRange(0, "", "", 14, 14, None)
            )
        )

    def testValidLength_test1_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )
        self.assertFalse(
            CreditCardValidator.validLength(
                15, CreditCardRange(0, "", "", 14, 14, None)
            )
        )

    def testValidLength_test0_decomposed(self) -> None:
        self.assertTrue(
            CreditCardValidator.validLength(
                14, CreditCardRange(0, "", "", 14, 14, None)
            )
        )

    def testRangeGenerator_test1_decomposed(self) -> None:
        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardRange(0, "300", "305", 14, 14, None),  # Diners
                CreditCardRange(0, "3095", None, 14, 14, None),  # Diners
                CreditCardRange(0, "36", None, 14, 14, None),  # Diners
                CreditCardRange(0, "38", "39", 14, 14, None),  # Diners
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR,
            ],
        )
        for card in self.__VALID_CARDS:
            self.assertTrue(ccv.isValid(card), card)
        for card in self.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(card), card)

    def testRangeGenerator_test0_decomposed(self) -> None:
        ccv = CreditCardValidator(
            3,
            0,
            [
                CreditCardRange(0, "300", "305", 14, 14, None),  # Diners
                CreditCardRange(0, "3095", None, 14, 14, None),  # Diners
                CreditCardRange(0, "36", None, 14, 14, None),  # Diners
                CreditCardRange(0, "38", "39", 14, 14, None),  # Diners
            ],
            [
                CreditCardValidator.AMEX_VALIDATOR,
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.MASTERCARD_VALIDATOR,
                CreditCardValidator.DISCOVER_VALIDATOR,
            ],
        )

    def testRangeGeneratorNoLuhn_test1_decomposed(self) -> None:
        cv = CreditCardValidator.createRangeValidator(
            [
                CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardRange(0, "644", "65", 8, 8, None),
            ],
            None,
        )
        self.assertTrue(cv.isValid("1990000"))
        self.assertTrue(cv.isValid("199000"))
        self.assertFalse(cv.isValid("000000"))
        self.assertFalse(cv.isValid("099999"))
        self.assertFalse(cv.isValid("200000"))
        self.assertFalse(cv.isValid("64399999"))
        self.assertTrue(cv.isValid("64400000"))
        self.assertTrue(cv.isValid("64900000"))
        self.assertTrue(cv.isValid("65000000"))
        self.assertTrue(cv.isValid("65999999"))
        self.assertFalse(cv.isValid("66000000"))

    def testRangeGeneratorNoLuhn_test0_decomposed(self) -> None:
        cv = CreditCardValidator.createRangeValidator(
            [
                CreditCardRange(0, "1", None, 6, 7, None),
                CreditCardRange(0, "644", "65", 8, 8, None),
            ],
            None,
        )

    def testGeneric_test1_decomposed(self) -> None:
        ccv = CreditCardValidator.genericCreditCardValidator2()
        for card in self.__VALID_CARDS:
            self.assertTrue(ccv.isValid(card), card)
        for card in self.__ERROR_CARDS:
            self.assertFalse(ccv.isValid(card), card)

    def testGeneric_test0_decomposed(self) -> None:
        ccv = CreditCardValidator.genericCreditCardValidator2()

    def testMastercardUsingSeparators_test4_decomposed(self) -> None:
        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(
            "5134567890123456", regex.validate("5134567890123456"), "Number"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678-9012-3456"), "Hyphen"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678 9012 3456"), "Space"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678 9012-3456"), "MixedA"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678-9012 3456"), "MixedB"
        )
        self.assertFalse(regex.isValid("5134.5678.9012.3456"), "Invalid Separator A")
        self.assertFalse(regex.isValid("5134_5678_9012_3456"), "Invalid Separator B")
        self.assertFalse(regex.isValid("513-45678-9012-3456"), "Invalid Grouping A")
        self.assertFalse(regex.isValid("5134-567-89012-3456"), "Invalid Grouping B")
        self.assertFalse(regex.isValid("5134-5678-901-23456"), "Invalid Grouping C")
        self.assertEqual(
            "5500000000000004", validator.validate("5500-0000-0000-0004"), "Valid-A"
        )
        self.assertEqual(
            "5424000000000015", validator.validate("5424 0000 0000 0015"), "Valid-B"
        )
        self.assertEqual(
            "5301250070000191", validator.validate("5301-250070000191"), "Valid-C"
        )
        self.assertEqual(
            "5123456789012346", validator.validate("5123456789012346"), "Valid-D"
        )

    def testMastercardUsingSeparators_test3_decomposed(self) -> None:
        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(
            "5134567890123456", regex.validate("5134567890123456"), "Number"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678-9012-3456"), "Hyphen"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678 9012 3456"), "Space"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678 9012-3456"), "MixedA"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678-9012 3456"), "MixedB"
        )

        self.assertFalse(regex.isValid("5134.5678.9012.3456"), "Invalid Separator A")
        self.assertFalse(regex.isValid("5134_5678_9012_3456"), "Invalid Separator B")
        self.assertFalse(regex.isValid("513-45678-9012-3456"), "Invalid Grouping A")
        self.assertFalse(regex.isValid("5134-567-89012-3456"), "Invalid Grouping B")
        self.assertFalse(regex.isValid("5134-5678-901-23456"), "Invalid Grouping C")

    def testMastercardUsingSeparators_test2_decomposed(self) -> None:
        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

        self.assertEqual(
            "5134567890123456", regex.validate("5134567890123456"), "Number"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678-9012-3456"), "Hyphen"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678 9012 3456"), "Space"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134-5678 9012-3456"), "MixedA"
        )
        self.assertEqual(
            "5134567890123456", regex.validate("5134 5678-9012 3456"), "MixedB"
        )

    def testMastercardUsingSeparators_test1_decomposed(self) -> None:
        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )
        regex = validator.getRegexValidator()

    def testMastercardUsingSeparators_test0_decomposed(self) -> None:
        MASTERCARD_REGEX_SEP = (
            r"^(5[1-5]\d{2})(?:[- ])?(\d{4})(?:[- ])?(\d{4})(?:[- ])?(\d{4})$"
        )
        validator = CodeValidator.CodeValidator5(
            MASTERCARD_REGEX_SEP, LuhnCheckDigit.LUHN_CHECK_DIGIT
        )

    def testVPayOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue(validator.isValid(self.__VALID_VPAY), "Valid")
        self.assertTrue(validator.isValid(self.__VALID_VPAY2), "Valid")
        self.assertFalse(validator.isValid(self.__ERROR_VPAY), "Invalid")
        self.assertEqual(self.__VALID_VPAY, validator.validate(self.__VALID_VPAY))
        self.assertEqual(self.__VALID_VPAY2, validator.validate(self.__VALID_VPAY2))
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertTrue(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertTrue(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testVPayOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue(validator.isValid(self.__VALID_VPAY), "Valid")
        self.assertTrue(validator.isValid(self.__VALID_VPAY2), "Valid")
        self.assertFalse(validator.isValid(self.__ERROR_VPAY), "Invalid")
        self.assertEqual(self.__VALID_VPAY, validator.validate(self.__VALID_VPAY))
        self.assertEqual(self.__VALID_VPAY2, validator.validate(self.__VALID_VPAY2))

    def testVPayOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)
        self.assertTrue(validator.isValid(self.__VALID_VPAY), "Valid")
        self.assertTrue(validator.isValid(self.__VALID_VPAY2), "Valid")
        self.assertFalse(validator.isValid(self.__ERROR_VPAY), "Invalid")

    def testVPayOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VPAY, None, None)

    def testVisaOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")
        self.assertIsNone(validator.validate(self.__ERROR_VISA), "validate()")
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertTrue(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertTrue(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testVisaOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")
        self.assertIsNone(validator.validate(self.__ERROR_VISA), "validate()")
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )

    def testVisaOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")

    def testVisaOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.VISA, None, None)

    def testVisaValidator_test3_decomposed(self) -> None:
        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("423456789012"), "Length 12")
        self.assertTrue(regex.isValid("4234567890123"), "Length 13")
        self.assertFalse(regex.isValid("42345678901234"), "Length 14")
        self.assertFalse(regex.isValid("423456789012345"), "Length 15")
        self.assertTrue(regex.isValid("4234567890123456"), "Length 16")
        self.assertFalse(regex.isValid("42345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("423456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("3234567890123"), "Invalid Pref-A")
        self.assertFalse(regex.isValid("3234567890123456"), "Invalid Pref-B")
        self.assertFalse(regex.isValid("4234567x90123"), "Invalid Char-A")
        self.assertFalse(regex.isValid("4234567x90123456"), "Invalid Char-B")
        self.assertTrue(regex.isValid(self.__ERROR_VISA), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_SHORT_VISA), "Valid regex-S")
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")
        self.assertIsNone(validator.validate(self.__ERROR_VISA), "validate()")
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertTrue(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertTrue(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")
        self.assertTrue(validator.isValid("4111111111111111"), "Valid-A")
        self.assertTrue(validator.isValid("4543059999999982"), "Valid-C")
        self.assertTrue(validator.isValid("4462000000000003"), "Valid-B")
        self.assertTrue(validator.isValid("4508750000000009"), "Valid-D")
        self.assertTrue(validator.isValid("4012888888881881"), "Valid-E")

    def testVisaValidator_test2_decomposed(self) -> None:
        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("423456789012"), "Length 12")
        self.assertTrue(regex.isValid("4234567890123"), "Length 13")
        self.assertFalse(regex.isValid("42345678901234"), "Length 14")
        self.assertFalse(regex.isValid("423456789012345"), "Length 15")
        self.assertTrue(regex.isValid("4234567890123456"), "Length 16")
        self.assertFalse(regex.isValid("42345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("423456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("3234567890123"), "Invalid Pref-A")
        self.assertFalse(regex.isValid("3234567890123456"), "Invalid Pref-B")
        self.assertFalse(regex.isValid("4234567x90123"), "Invalid Char-A")
        self.assertFalse(regex.isValid("4234567x90123456"), "Invalid Char-B")
        self.assertTrue(regex.isValid(self.__ERROR_VISA), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_SHORT_VISA), "Valid regex-S")
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")
        self.assertIsNone(validator.validate(self.__ERROR_VISA), "validate()")
        self.assertEqual(self.__VALID_VISA, validator.validate(self.__VALID_VISA))
        self.assertEqual(
            self.__VALID_SHORT_VISA, validator.validate(self.__VALID_SHORT_VISA)
        )

    def testVisaValidator_test1_decomposed(self) -> None:
        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("423456789012"), "Length 12")
        self.assertTrue(regex.isValid("4234567890123"), "Length 13")
        self.assertFalse(regex.isValid("42345678901234"), "Length 14")
        self.assertFalse(regex.isValid("423456789012345"), "Length 15")
        self.assertTrue(regex.isValid("4234567890123456"), "Length 16")
        self.assertFalse(regex.isValid("42345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("423456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("3234567890123"), "Invalid Pref-A")
        self.assertFalse(regex.isValid("3234567890123456"), "Invalid Pref-B")
        self.assertFalse(regex.isValid("4234567x90123"), "Invalid Char-A")
        self.assertFalse(regex.isValid("4234567x90123456"), "Invalid Char-B")
        self.assertTrue(regex.isValid(self.__ERROR_VISA), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_SHORT_VISA), "Valid regex-S")
        self.assertFalse(validator.isValid(self.__ERROR_VISA), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_SHORT_VISA), "Invalid-S")

    def testVisaValidator_test0_decomposed(self) -> None:
        validator = CreditCardValidator.VISA_VALIDATOR
        regex = validator.getRegexValidator()

    def testMastercardOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testMastercardOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

    def testMastercardOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")

    def testMastercardOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.MASTERCARD, None, None)

    def testMastercardValidator_test7_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")
        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")
        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

        rev = validator.getRegexValidator()
        PAD = "0000000000"
        self.assertFalse(rev.isValid("222099" + PAD), "222099")
        for i in range(222100, 272100):
            j = str(i) + PAD
            self.assertTrue(rev.isValid(j), j)
        self.assertFalse(rev.isValid("272100" + PAD), "272100")

    def testMastercardValidator_test6_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")
        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")

        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

        rev = validator.getRegexValidator()
        PAD = "0000000000"
        self.assertFalse(rev.isValid("222099" + PAD), "222099")

        for i in range(222100, 272100):
            j = str(i) + PAD
            self.assertTrue(rev.isValid(j), j)

    def testMastercardValidator_test5_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")

        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

        rev = validator.getRegexValidator()
        PAD = "0000000000"
        self.assertFalse(rev.isValid("222099" + PAD), "222099")

    def testMastercardValidator_test4_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")

        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

        rev = validator.getRegexValidator()

    def testMastercardValidator_test3_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")
        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")

        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

        self.assertTrue(validator.isValid("5500000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("5424000000000015"), "Valid-B")
        self.assertTrue(validator.isValid("5301250070000191"), "Valid-C")
        self.assertTrue(validator.isValid("5123456789012346"), "Valid-D")
        self.assertTrue(validator.isValid("5555555555554444"), "Valid-E")

    def testMastercardValidator_test2_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")

        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")

        self.assertIsNone(validator.validate(self.__ERROR_MASTERCARD), "validate()")
        self.assertEqual(
            self.__VALID_MASTERCARD, validator.validate(self.__VALID_MASTERCARD)
        )

    def testMastercardValidator_test1_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("513456789012"), "Length 12")
        self.assertFalse(regex.isValid("5134567890123"), "Length 13")
        self.assertFalse(regex.isValid("51345678901234"), "Length 14")
        self.assertFalse(regex.isValid("513456789012345"), "Length 15")
        self.assertTrue(regex.isValid("5134567890123456"), "Length 16")
        self.assertFalse(regex.isValid("51345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("513456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("4134567890123456"), "Prefix 41")
        self.assertFalse(regex.isValid("5034567890123456"), "Prefix 50")
        self.assertTrue(regex.isValid("5134567890123456"), "Prefix 51")
        self.assertTrue(regex.isValid("5234567890123456"), "Prefix 52")
        self.assertTrue(regex.isValid("5334567890123456"), "Prefix 53")
        self.assertTrue(regex.isValid("5434567890123456"), "Prefix 54")
        self.assertTrue(regex.isValid("5534567890123456"), "Prefix 55")
        self.assertFalse(regex.isValid("5634567890123456"), "Prefix 56")
        self.assertFalse(regex.isValid("6134567890123456"), "Prefix 61")
        self.assertFalse(regex.isValid("5134567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_MASTERCARD), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_MASTERCARD), "Invalid")

    def testMastercardValidator_test0_decomposed(self) -> None:
        validator = CreditCardValidator.MASTERCARD_VALIDATOR
        if validator is not None:
            regex = validator.getRegexValidator()

    def testDiscoverOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")
        self.assertIsNone(validator.validate(self.__ERROR_DISCOVER), "validate()")
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER65), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testDiscoverOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")
        self.assertIsNone(validator.validate(self.__ERROR_DISCOVER), "validate()")
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )

    def testDiscoverOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")

    def testDiscoverOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DISCOVER, None, None)

    def testDiscoverValidator_test3_decomposed(self) -> None:
        validator = CreditCardValidator.DISCOVER_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("601156789012"), "Length 12-6011")
        self.assertFalse(regex.isValid("653456789012"), "Length 12-65")
        self.assertFalse(regex.isValid("6011567890123"), "Length 13-6011")
        self.assertFalse(regex.isValid("6534567890123"), "Length 13-65")
        self.assertFalse(regex.isValid("60115678901234"), "Length 14-6011")
        self.assertFalse(regex.isValid("65345678901234"), "Length 14-65")
        self.assertFalse(regex.isValid("601156789012345"), "Length 15-6011")
        self.assertFalse(regex.isValid("653456789012345"), "Length 15-65")
        self.assertTrue(regex.isValid("6011567890123456"), "Length 16-6011")
        self.assertTrue(regex.isValid("6444567890123456"), "Length 16-644")
        self.assertTrue(regex.isValid("6484567890123456"), "Length 16-648")
        self.assertTrue(regex.isValid("6534567890123456"), "Length 16-65")
        self.assertFalse(regex.isValid("65345678901234567"), "Length 17-65")
        self.assertFalse(regex.isValid("601156789012345678"), "Length 18-6011")
        self.assertFalse(regex.isValid("653456789012345678"), "Length 18-65")
        self.assertFalse(regex.isValid("6404567890123456"), "Prefix 640")
        self.assertFalse(regex.isValid("6414567890123456"), "Prefix 641")
        self.assertFalse(regex.isValid("6424567890123456"), "Prefix 642")
        self.assertFalse(regex.isValid("6434567890123456"), "Prefix 643")
        self.assertFalse(regex.isValid("6010567890123456"), "Prefix 6010")
        self.assertFalse(regex.isValid("6012567890123456"), "Prefix 6012")
        self.assertFalse(regex.isValid("6011567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER65), "Valid regex65")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")
        self.assertIsNone(validator.validate(self.__ERROR_DISCOVER), "validate()")
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertTrue(validator.isValid(self.__VALID_DISCOVER65), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")
        self.assertTrue(validator.isValid("6011111111111117"), "Valid-A")
        self.assertTrue(validator.isValid("6011000000000004"), "Valid-B")
        self.assertTrue(validator.isValid("6011000000000012"), "Valid-C")

    def testDiscoverValidator_test2_decomposed(self) -> None:
        validator = CreditCardValidator.DISCOVER_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("601156789012"), "Length 12-6011")
        self.assertFalse(regex.isValid("653456789012"), "Length 12-65")
        self.assertFalse(regex.isValid("6011567890123"), "Length 13-6011")
        self.assertFalse(regex.isValid("6534567890123"), "Length 13-65")
        self.assertFalse(regex.isValid("60115678901234"), "Length 14-6011")
        self.assertFalse(regex.isValid("65345678901234"), "Length 14-65")
        self.assertFalse(regex.isValid("601156789012345"), "Length 15-6011")
        self.assertFalse(regex.isValid("653456789012345"), "Length 15-65")
        self.assertTrue(regex.isValid("6011567890123456"), "Length 16-6011")
        self.assertTrue(regex.isValid("6444567890123456"), "Length 16-644")
        self.assertTrue(regex.isValid("6484567890123456"), "Length 16-648")
        self.assertTrue(regex.isValid("6534567890123456"), "Length 16-65")
        self.assertFalse(regex.isValid("65345678901234567"), "Length 17-65")
        self.assertFalse(regex.isValid("601156789012345678"), "Length 18-6011")
        self.assertFalse(regex.isValid("653456789012345678"), "Length 18-65")
        self.assertFalse(regex.isValid("6404567890123456"), "Prefix 640")
        self.assertFalse(regex.isValid("6414567890123456"), "Prefix 641")
        self.assertFalse(regex.isValid("6424567890123456"), "Prefix 642")
        self.assertFalse(regex.isValid("6434567890123456"), "Prefix 643")
        self.assertFalse(regex.isValid("6010567890123456"), "Prefix 6010")
        self.assertFalse(regex.isValid("6012567890123456"), "Prefix 6012")
        self.assertFalse(regex.isValid("6011567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER65), "Valid regex65")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")
        self.assertIsNone(validator.validate(self.__ERROR_DISCOVER), "validate()")
        self.assertEqual(
            self.__VALID_DISCOVER, validator.validate(self.__VALID_DISCOVER)
        )
        self.assertEqual(
            self.__VALID_DISCOVER65, validator.validate(self.__VALID_DISCOVER65)
        )

    def testDiscoverValidator_test1_decomposed(self) -> None:
        validator = CreditCardValidator.DISCOVER_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("601156789012"), "Length 12-6011")
        self.assertFalse(regex.isValid("653456789012"), "Length 12-65")
        self.assertFalse(regex.isValid("6011567890123"), "Length 13-6011")
        self.assertFalse(regex.isValid("6534567890123"), "Length 13-65")
        self.assertFalse(regex.isValid("60115678901234"), "Length 14-6011")
        self.assertFalse(regex.isValid("65345678901234"), "Length 14-65")
        self.assertFalse(regex.isValid("601156789012345"), "Length 15-6011")
        self.assertFalse(regex.isValid("653456789012345"), "Length 15-65")
        self.assertTrue(regex.isValid("6011567890123456"), "Length 16-6011")
        self.assertTrue(regex.isValid("6444567890123456"), "Length 16-644")
        self.assertTrue(regex.isValid("6484567890123456"), "Length 16-648")
        self.assertTrue(regex.isValid("6534567890123456"), "Length 16-65")
        self.assertFalse(regex.isValid("65345678901234567"), "Length 17-65")
        self.assertFalse(regex.isValid("601156789012345678"), "Length 18-6011")
        self.assertFalse(regex.isValid("653456789012345678"), "Length 18-65")
        self.assertFalse(regex.isValid("6404567890123456"), "Prefix 640")
        self.assertFalse(regex.isValid("6414567890123456"), "Prefix 641")
        self.assertFalse(regex.isValid("6424567890123456"), "Prefix 642")
        self.assertFalse(regex.isValid("6434567890123456"), "Prefix 643")
        self.assertFalse(regex.isValid("6010567890123456"), "Prefix 6010")
        self.assertFalse(regex.isValid("6012567890123456"), "Prefix 6012")
        self.assertFalse(regex.isValid("6011567x90123456"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER), "Valid regex")
        self.assertTrue(regex.isValid(self.__ERROR_DISCOVER65), "Valid regex65")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER), "Invalid")
        self.assertFalse(validator.isValid(self.__ERROR_DISCOVER65), "Invalid65")

    def testDiscoverValidator_test0_decomposed(self) -> None:
        validator = CreditCardValidator.DISCOVER_VALIDATOR
        self.assertIsNotNone(validator, "Validator should not be None")
        regex = validator.getRegexValidator()
        self.assertIsNotNone(regex, "RegexValidator should not be None")

    def testDinersOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_DINERS), "validate()")
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))
        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertTrue(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testDinersOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_DINERS), "validate()")
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

    def testDinersOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")

    def testDinersOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.DINERS, None, None)

    def testDinersValidator_test3_decomposed(self) -> None:
        validator = CreditCardValidator.DINERS_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("300456789012"), "Length 12-300")
        self.assertFalse(regex.isValid("363456789012"), "Length 12-36")
        self.assertFalse(regex.isValid("3004567890123"), "Length 13-300")
        self.assertFalse(regex.isValid("3634567890123"), "Length 13-36")
        self.assertTrue(regex.isValid("30045678901234"), "Length 14-300")
        self.assertTrue(regex.isValid("36345678901234"), "Length 14-36")
        self.assertFalse(regex.isValid("300456789012345"), "Length 15-300")
        self.assertFalse(regex.isValid("363456789012345"), "Length 15-36")
        self.assertFalse(regex.isValid("3004567890123456"), "Length 16-300")
        self.assertFalse(regex.isValid("3634567890123456"), "Length 16-36")
        self.assertFalse(regex.isValid("30045678901234567"), "Length 17-300")
        self.assertFalse(regex.isValid("36345678901234567"), "Length 17-36")
        self.assertFalse(regex.isValid("300456789012345678"), "Length 18-300")
        self.assertFalse(regex.isValid("363456789012345678"), "Length 18-36")

        self.assertTrue(regex.isValid("30045678901234"), "Prefix 300")
        self.assertTrue(regex.isValid("30145678901234"), "Prefix 301")
        self.assertTrue(regex.isValid("30245678901234"), "Prefix 302")
        self.assertTrue(regex.isValid("30345678901234"), "Prefix 303")
        self.assertTrue(regex.isValid("30445678901234"), "Prefix 304")
        self.assertTrue(regex.isValid("30545678901234"), "Prefix 305")
        self.assertFalse(regex.isValid("30645678901234"), "Prefix 306")
        self.assertFalse(regex.isValid("30945678901234"), "Prefix 3094")
        self.assertTrue(regex.isValid("30955678901234"), "Prefix 3095")
        self.assertFalse(regex.isValid("30965678901234"), "Prefix 3096")
        self.assertFalse(regex.isValid("35345678901234"), "Prefix 35")
        self.assertTrue(regex.isValid("36345678901234"), "Prefix 36")
        self.assertFalse(regex.isValid("37345678901234"), "Prefix 37")
        self.assertTrue(regex.isValid("38345678901234"), "Prefix 38")
        self.assertTrue(regex.isValid("39345678901234"), "Prefix 39")

        self.assertFalse(regex.isValid("3004567x901234"), "Invalid Char-A")
        self.assertFalse(regex.isValid("3634567x901234"), "Invalid Char-B")

        self.assertTrue(regex.isValid(self.__ERROR_DINERS), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_DINERS), "validate()")
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

        self.assertFalse(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertTrue(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

        self.assertTrue(validator.isValid("30000000000004"), "Valid-A")
        self.assertTrue(validator.isValid("30123456789019"), "Valid-B")
        self.assertTrue(validator.isValid("36432685260294"), "Valid-C")

    def testDinersValidator_test2_decomposed(self) -> None:
        validator = CreditCardValidator.DINERS_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("300456789012"), "Length 12-300")
        self.assertFalse(regex.isValid("363456789012"), "Length 12-36")
        self.assertFalse(regex.isValid("3004567890123"), "Length 13-300")
        self.assertFalse(regex.isValid("3634567890123"), "Length 13-36")
        self.assertTrue(regex.isValid("30045678901234"), "Length 14-300")
        self.assertTrue(regex.isValid("36345678901234"), "Length 14-36")
        self.assertFalse(regex.isValid("300456789012345"), "Length 15-300")
        self.assertFalse(regex.isValid("363456789012345"), "Length 15-36")
        self.assertFalse(regex.isValid("3004567890123456"), "Length 16-300")
        self.assertFalse(regex.isValid("3634567890123456"), "Length 16-36")
        self.assertFalse(regex.isValid("30045678901234567"), "Length 17-300")
        self.assertFalse(regex.isValid("36345678901234567"), "Length 17-36")
        self.assertFalse(regex.isValid("300456789012345678"), "Length 18-300")
        self.assertFalse(regex.isValid("363456789012345678"), "Length 18-36")

        self.assertTrue(regex.isValid("30045678901234"), "Prefix 300")
        self.assertTrue(regex.isValid("30145678901234"), "Prefix 301")
        self.assertTrue(regex.isValid("30245678901234"), "Prefix 302")
        self.assertTrue(regex.isValid("30345678901234"), "Prefix 303")
        self.assertTrue(regex.isValid("30445678901234"), "Prefix 304")
        self.assertTrue(regex.isValid("30545678901234"), "Prefix 305")
        self.assertFalse(regex.isValid("30645678901234"), "Prefix 306")
        self.assertFalse(regex.isValid("30945678901234"), "Prefix 3094")
        self.assertTrue(regex.isValid("30955678901234"), "Prefix 3095")
        self.assertFalse(regex.isValid("30965678901234"), "Prefix 3096")
        self.assertFalse(regex.isValid("35345678901234"), "Prefix 35")
        self.assertTrue(regex.isValid("36345678901234"), "Prefix 36")
        self.assertFalse(regex.isValid("37345678901234"), "Prefix 37")
        self.assertTrue(regex.isValid("38345678901234"), "Prefix 38")
        self.assertTrue(regex.isValid("39345678901234"), "Prefix 39")

        self.assertFalse(regex.isValid("3004567x901234"), "Invalid Char-A")
        self.assertFalse(regex.isValid("3634567x901234"), "Invalid Char-B")

        self.assertTrue(regex.isValid(self.__ERROR_DINERS), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_DINERS), "validate()")
        self.assertEqual(self.__VALID_DINERS, validator.validate(self.__VALID_DINERS))

    def testDinersValidator_test1_decomposed(self) -> None:
        validator = CreditCardValidator.DINERS_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("300456789012"), "Length 12-300")
        self.assertFalse(regex.isValid("363456789012"), "Length 12-36")
        self.assertFalse(regex.isValid("3004567890123"), "Length 13-300")
        self.assertFalse(regex.isValid("3634567890123"), "Length 13-36")
        self.assertTrue(regex.isValid("30045678901234"), "Length 14-300")
        self.assertTrue(regex.isValid("36345678901234"), "Length 14-36")
        self.assertFalse(regex.isValid("300456789012345"), "Length 15-300")
        self.assertFalse(regex.isValid("363456789012345"), "Length 15-36")
        self.assertFalse(regex.isValid("3004567890123456"), "Length 16-300")
        self.assertFalse(regex.isValid("3634567890123456"), "Length 16-36")
        self.assertFalse(regex.isValid("30045678901234567"), "Length 17-300")
        self.assertFalse(regex.isValid("36345678901234567"), "Length 17-36")
        self.assertFalse(regex.isValid("300456789012345678"), "Length 18-300")
        self.assertFalse(regex.isValid("363456789012345678"), "Length 18-36")

        self.assertTrue(regex.isValid("30045678901234"), "Prefix 300")
        self.assertTrue(regex.isValid("30145678901234"), "Prefix 301")
        self.assertTrue(regex.isValid("30245678901234"), "Prefix 302")
        self.assertTrue(regex.isValid("30345678901234"), "Prefix 303")
        self.assertTrue(regex.isValid("30445678901234"), "Prefix 304")
        self.assertTrue(regex.isValid("30545678901234"), "Prefix 305")
        self.assertFalse(regex.isValid("30645678901234"), "Prefix 306")
        self.assertFalse(regex.isValid("30945678901234"), "Prefix 3094")
        self.assertTrue(regex.isValid("30955678901234"), "Prefix 3095")
        self.assertFalse(regex.isValid("30965678901234"), "Prefix 3096")
        self.assertFalse(regex.isValid("35345678901234"), "Prefix 35")
        self.assertTrue(regex.isValid("36345678901234"), "Prefix 36")
        self.assertFalse(regex.isValid("37345678901234"), "Prefix 37")
        self.assertTrue(regex.isValid("38345678901234"), "Prefix 38")
        self.assertTrue(regex.isValid("39345678901234"), "Prefix 39")

        self.assertFalse(regex.isValid("3004567x901234"), "Invalid Char-A")
        self.assertFalse(regex.isValid("3634567x901234"), "Invalid Char-B")
        self.assertTrue(regex.isValid(self.__ERROR_DINERS), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_DINERS), "Invalid")

    def testDinersValidator_test0_decomposed(self) -> None:
        validator = CreditCardValidator.DINERS_VALIDATOR
        if validator is not None:
            regex = validator.getRegexValidator()

    def testAmexOption_test3_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)

        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_AMEX), "validate()")
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))
        self.assertTrue(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")

    def testAmexOption_test2_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_AMEX), "validate()")
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

    def testAmexOption_test1_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")

    def testAmexOption_test0_decomposed(self) -> None:
        validator = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)

    def testAmexValidator_test3_decomposed(self) -> None:
        validator = CreditCardValidator.AMEX_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("343456789012"), "Length 12")
        self.assertFalse(regex.isValid("3434567890123"), "Length 13")
        self.assertFalse(regex.isValid("34345678901234"), "Length 14")
        self.assertTrue(regex.isValid("343456789012345"), "Length 15")
        self.assertFalse(regex.isValid("3434567890123456"), "Length 16")
        self.assertFalse(regex.isValid("34345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("343456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("333456789012345"), "Prefix 33")
        self.assertTrue(regex.isValid("343456789012345"), "Prefix 34")
        self.assertFalse(regex.isValid("353456789012345"), "Prefix 35")
        self.assertFalse(regex.isValid("363456789012345"), "Prefix 36")
        self.assertTrue(regex.isValid("373456789012345"), "Prefix 37")
        self.assertFalse(regex.isValid("383456789012345"), "Prefix 38")
        self.assertFalse(regex.isValid("413456789012345"), "Prefix 41")

        self.assertFalse(regex.isValid("3434567x9012345"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_AMEX), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")
        self.assertIsNone(validator.validate(self.__ERROR_AMEX), "validate()")
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))
        self.assertTrue(validator.isValid(self.__VALID_AMEX), "Amex")
        self.assertFalse(validator.isValid(self.__VALID_DINERS), "Diners")
        self.assertFalse(validator.isValid(self.__VALID_DISCOVER), "Discover")
        self.assertFalse(validator.isValid(self.__VALID_MASTERCARD), "Mastercard")
        self.assertFalse(validator.isValid(self.__VALID_VISA), "Visa")
        self.assertFalse(validator.isValid(self.__VALID_SHORT_VISA), "Visa Short")
        self.assertTrue(validator.isValid("371449635398431"), "Valid-A")
        self.assertTrue(validator.isValid("340000000000009"), "Valid-B")
        self.assertTrue(validator.isValid("370000000000002"), "Valid-C")
        self.assertTrue(validator.isValid("378734493671000"), "Valid-D")

    def testAmexValidator_test2_decomposed(self) -> None:
        validator = CreditCardValidator.AMEX_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("343456789012"), "Length 12")
        self.assertFalse(regex.isValid("3434567890123"), "Length 13")
        self.assertFalse(regex.isValid("34345678901234"), "Length 14")
        self.assertTrue(regex.isValid("343456789012345"), "Length 15")
        self.assertFalse(regex.isValid("3434567890123456"), "Length 16")
        self.assertFalse(regex.isValid("34345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("343456789012345678"), "Length 18")

        self.assertFalse(regex.isValid("333456789012345"), "Prefix 33")
        self.assertTrue(regex.isValid("343456789012345"), "Prefix 34")
        self.assertFalse(regex.isValid("353456789012345"), "Prefix 35")
        self.assertFalse(regex.isValid("363456789012345"), "Prefix 36")
        self.assertTrue(regex.isValid("373456789012345"), "Prefix 37")
        self.assertFalse(regex.isValid("383456789012345"), "Prefix 38")
        self.assertFalse(regex.isValid("413456789012345"), "Prefix 41")

        self.assertFalse(regex.isValid("3434567x9012345"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_AMEX), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")

        self.assertIsNone(validator.validate(self.__ERROR_AMEX), "validate()")
        self.assertEqual(self.__VALID_AMEX, validator.validate(self.__VALID_AMEX))

    def testAmexValidator_test1_decomposed(self) -> None:
        validator = CreditCardValidator.AMEX_VALIDATOR
        regex = validator.getRegexValidator()

        self.assertFalse(regex.isValid("343456789012"), "Length 12")
        self.assertFalse(regex.isValid("3434567890123"), "Length 13")
        self.assertFalse(regex.isValid("34345678901234"), "Length 14")
        self.assertTrue(regex.isValid("343456789012345"), "Length 15")
        self.assertFalse(regex.isValid("3434567890123456"), "Length 16")
        self.assertFalse(regex.isValid("34345678901234567"), "Length 17")
        self.assertFalse(regex.isValid("343456789012345678"), "Length 18")
        self.assertFalse(regex.isValid("333456789012345"), "Prefix 33")
        self.assertTrue(regex.isValid("343456789012345"), "Prefix 34")
        self.assertFalse(regex.isValid("353456789012345"), "Prefix 35")
        self.assertFalse(regex.isValid("363456789012345"), "Prefix 36")
        self.assertTrue(regex.isValid("373456789012345"), "Prefix 37")
        self.assertFalse(regex.isValid("383456789012345"), "Prefix 38")
        self.assertFalse(regex.isValid("413456789012345"), "Prefix 41")
        self.assertFalse(regex.isValid("3434567x9012345"), "Invalid Char")
        self.assertTrue(regex.isValid(self.__ERROR_AMEX), "Valid regex")
        self.assertFalse(validator.isValid(self.__ERROR_AMEX), "Invalid")

    def testAmexValidator_test0_decomposed(self) -> None:
        validator = CreditCardValidator.AMEX_VALIDATOR
        self.assertIsNotNone(validator, "Validator should not be None")
        regex = validator.getRegexValidator()
        self.assertIsNotNone(regex, "RegexValidator should not be None")

    def testArrayConstructor_test2_decomposed(self) -> None:
        ccv = CreditCardValidator(
            1,
            0,
            None,
            [
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.AMEX_VALIDATOR,
            ],
        )
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))

        with self.assertRaises(ValueError) as context:
            CreditCardValidator(1, 0, None, None)
        self.assertEqual(str(context.exception), "Card validators are missing")

    def testArrayConstructor_test1_decomposed(self) -> None:
        ccv = CreditCardValidator(
            constructorId=1,
            options=0,
            creditCardRanges=None,
            creditCardValidators=[
                CreditCardValidator.VISA_VALIDATOR,
                CreditCardValidator.AMEX_VALIDATOR,
            ],
        )
        self.assertTrue(ccv.isValid(self.__VALID_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_SHORT_VISA))
        self.assertTrue(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))

    def testArrayConstructor_test0_decomposed(self) -> None:
        ccv = CreditCardValidator(
            1,
            0,
            None,
            [CreditCardValidator.VISA_VALIDATOR, CreditCardValidator.AMEX_VALIDATOR],
        )

    def testAddAllowedCardType_test1_decomposed(self) -> None:
        ccv = CreditCardValidator(0, CreditCardValidator.NONE, None, None)
        self.assertFalse(ccv.isValid(self.__VALID_VISA))
        self.assertFalse(ccv.isValid(self.__VALID_AMEX))
        self.assertFalse(ccv.isValid(self.__VALID_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__VALID_DISCOVER))
        self.assertFalse(ccv.isValid(self.__VALID_DINERS))

    def testAddAllowedCardType_test0_decomposed(self) -> None:
        ccv = CreditCardValidator(0, CreditCardValidator.NONE, None, None)

    def testIsValid_test4_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()
        self.assertIsNone(ccv.validate(None))
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
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER65))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER65))
        ccv = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)
        self.assertFalse(ccv.isValid("4417123456789113"))

    def testIsValid_test3_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()
        self.assertIsNone(ccv.validate(None))
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
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER65))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER65))
        ccv = CreditCardValidator(0, CreditCardValidator.AMEX, None, None)

    def testIsValid_test2_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()
        self.assertIsNone(ccv.validate(None))
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
        self.assertTrue(ccv.isValid(self.__VALID_DISCOVER65))
        self.assertFalse(ccv.isValid(self.__ERROR_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_SHORT_VISA))
        self.assertFalse(ccv.isValid(self.__ERROR_AMEX))
        self.assertFalse(ccv.isValid(self.__ERROR_MASTERCARD))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER))
        self.assertFalse(ccv.isValid(self.__ERROR_DISCOVER65))

    def testIsValid_test1_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()
        self.assertIsNone(ccv.validate(None))

    def testIsValid_test0_decomposed(self) -> None:
        ccv = CreditCardValidator.CreditCardValidator0()
