from __future__ import annotations
import re
import enum
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.ISBNValidator import *
from src.main.org.apache.commons.validator.routines.ISBNValidator import *


class ISBNValidatorTest(unittest.TestCase):

    __invalidISBN13Format: typing.List[str] = [
        "",  # empty
        "   ",  # empty
        "1",  # too short
        "978123456789",  # too short
        "97812345678901",  # too long
        "978-123456-1234567-123456-1",  # Group too long
        "978-12345-12345678-123456-1",  # Publisher too long
        "978-12345-1234567-1234567-1",  # Title too long
        "978-12345-1234567-123456-12",  # Check Digit too long
        "--978 1 930110 99 1",  # format
        "978 1 930110 99 1--",  # format
        "978 1 930110-99 1-",  # format
        "123-4-567890-12-8",  # format
        "978.1.2.3.4",  # Invalid Separator
        "978=1=2=3=4",  # Invalid Separator
        "978_1_2_3_4",  # Invalid Separator
        "978123456789X",  # invalid character
        "978-0-201-63385-X",  # invalid character
        "dsasdsadsadsa",  # invalid characters
        "I love sparrows!",  # invalid characters
        "979-1-234-567-89-6",  # format
    ]
    __validISBN13Format: typing.List[str] = [
        "9781234567890",
        "9791234567890",
        "978-12345-1234567-123456-1",
        "979-12345-1234567-123456-1",
        "978 12345 1234567 123456 1",
        "979 12345 1234567 123456 1",
        "978-1-2-3-4",
        "979-1-2-3-4",
        "978 1 2 3 4",
        "979 1 2 3 4",
    ]
    __invalidISBN10Format: typing.List[str] = [
        "",  # empty
        "   ",  # empty
        "1",  # too short
        "123456789",  # too short
        "12345678901",  # too long
        "12345678X0",  # X not at end
        "123456-1234567-123456-X",  # Group too long
        "12345-12345678-123456-X",  # Publisher too long
        "12345-1234567-1234567-X",  # Title too long
        "12345-1234567-123456-X2",  # Check Digit too long
        "--1 930110 99 5",  # format
        "1 930110 99 5--",  # format
        "1 930110-99 5-",  # format
        "1.2.3.4",  # Invalid Separator
        "1=2=3=4",  # Invalid Separator
        "1_2_3_4",  # Invalid Separator
        "123456789Y",  # Other character at the end
        "dsasdsadsa",  # invalid characters
        "I love sparrows!",  # invalid characters
        "068-556-98-45",  # format
    ]
    __validISBN10Format: List[str] = [
        "1234567890",
        "123456789X",
        "12345-1234567-123456-X",
        "12345 1234567 123456 X",
        "1-2-3-4",
        "1 2 3 4",
    ]

    def testConversionErrors_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

        inputs = ["123456789 ", "12345678901", "", "X234567890"]

        for input in inputs:
            with self.assertRaises(
                ValueError, msg=f"Expected ValueError for '{input}'"
            ):
                validator.convertToISBN13(input)

    def testConversionErrors_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        input = None
        try:
            input = "123456789 "
            validator.convertToISBN13(input)
            pytest.fail(f"Expected ValueError for '{input}'")
        except ValueError:
            pass

    def testConversionErrors_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testInvalid_test4_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        base_code = "193011099"
        self.assertFalse(validator.isValid(base_code + "0"), "ISBN10-0")
        self.assertFalse(validator.isValid(base_code + "1"), "ISBN10-1")
        self.assertFalse(validator.isValid(base_code + "2"), "ISBN10-2")
        self.assertFalse(validator.isValid(base_code + "3"), "ISBN10-3")
        self.assertFalse(validator.isValid(base_code + "4"), "ISBN10-4")
        self.assertTrue(validator.isValid(base_code + "5"), "ISBN10-5")
        self.assertFalse(validator.isValid(base_code + "6"), "ISBN10-6")
        self.assertFalse(validator.isValid(base_code + "7"), "ISBN10-7")
        self.assertFalse(validator.isValid(base_code + "8"), "ISBN10-8")
        self.assertFalse(validator.isValid(base_code + "9"), "ISBN10-9")
        self.assertFalse(validator.isValid(base_code + "X"), "ISBN10-X")

        base_code = "978193011099"
        self.assertFalse(validator.isValid(base_code + "0"), "ISBN13-0")
        self.assertTrue(validator.isValid(base_code + "1"), "ISBN13-1")
        self.assertFalse(validator.isValid(base_code + "2"), "ISBN13-2")
        self.assertFalse(validator.isValid(base_code + "3"), "ISBN13-3")
        self.assertFalse(validator.isValid(base_code + "4"), "ISBN13-4")
        self.assertFalse(validator.isValid(base_code + "5"), "ISBN13-5")
        self.assertFalse(validator.isValid(base_code + "6"), "ISBN13-6")
        self.assertFalse(validator.isValid(base_code + "7"), "ISBN13-7")
        self.assertFalse(validator.isValid(base_code + "8"), "ISBN13-8")
        self.assertFalse(validator.isValid(base_code + "9"), "ISBN13-9")

    def testInvalid_test3_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        baseCode = "193011099"
        self.assertFalse(validator.isValid(baseCode + "0"), "ISBN10-0")
        self.assertFalse(validator.isValid(baseCode + "1"), "ISBN10-1")
        self.assertFalse(validator.isValid(baseCode + "2"), "ISBN10-2")
        self.assertFalse(validator.isValid(baseCode + "3"), "ISBN10-3")
        self.assertFalse(validator.isValid(baseCode + "4"), "ISBN10-4")
        self.assertTrue(validator.isValid(baseCode + "5"), "ISBN10-5")
        self.assertFalse(validator.isValid(baseCode + "6"), "ISBN10-6")
        self.assertFalse(validator.isValid(baseCode + "7"), "ISBN10-7")
        self.assertFalse(validator.isValid(baseCode + "8"), "ISBN10-8")
        self.assertFalse(validator.isValid(baseCode + "9"), "ISBN10-9")
        self.assertFalse(validator.isValid(baseCode + "X"), "ISBN10-X")
        baseCode = "978193011099"
        self.assertFalse(validator.isValid(baseCode + "0"), "ISBN13-0")

    def testInvalid_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        base_code = "193011099"
        self.assertFalse(validator.isValid(base_code + "0"), "ISBN10-0")
        self.assertFalse(validator.isValid(base_code + "1"), "ISBN10-1")
        self.assertFalse(validator.isValid(base_code + "2"), "ISBN10-2")
        self.assertFalse(validator.isValid(base_code + "3"), "ISBN10-3")
        self.assertFalse(validator.isValid(base_code + "4"), "ISBN10-4")
        self.assertTrue(validator.isValid(base_code + "5"), "ISBN10-5")
        self.assertFalse(validator.isValid(base_code + "6"), "ISBN10-6")
        self.assertFalse(validator.isValid(base_code + "7"), "ISBN10-7")
        self.assertFalse(validator.isValid(base_code + "8"), "ISBN10-8")
        self.assertFalse(validator.isValid(base_code + "9"), "ISBN10-9")
        self.assertFalse(validator.isValid(base_code + "X"), "ISBN10-X")

    def testInvalid_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        base_code = "193011099"
        self.assertFalse(validator.isValid(base_code + "0"), "ISBN10-0")

    def testInvalid_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testNull_test7_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")
        self.assertFalse(validator.isValidISBN13(None), "isValidISBN13")
        self.assertIsNone(validator.validate(None), "validate")
        self.assertIsNone(validator.validateISBN10(None), "validateISBN10")
        self.assertIsNone(validator.validateISBN13(None), "validateISBN13")
        self.assertIsNone(validator.convertToISBN13(None), "convertToISBN13")

    def testNull_test6_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")
        self.assertFalse(validator.isValidISBN13(None), "isValidISBN13")
        self.assertIsNone(validator.validate(None), "validate")
        self.assertIsNone(validator.validateISBN10(None), "validateISBN10")
        self.assertIsNone(validator.validateISBN13(None), "validateISBN13")

    def testNull_test5_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")
        self.assertFalse(validator.isValidISBN13(None), "isValidISBN13")
        self.assertIsNone(validator.validate(None), "validate")
        self.assertIsNone(validator.validateISBN10(None), "validateISBN10")

    def testNull_test4_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")
        self.assertFalse(validator.isValidISBN13(None), "isValidISBN13")
        self.assertIsNone(validator.validate(None), "validate")

    def testNull_test3_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")
        self.assertFalse(validator.isValidISBN13(None), "isValidISBN13")

    def testNull_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")
        self.assertFalse(validator.isValidISBN10(None), "isValidISBN10")

    def testNull_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(validator.isValid(None), "isValid")

    def testNull_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testValidateISBN13_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("9781930110991"),
            "validateISBN13-1",
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978-1-930110-99-1"),
            "validateISBN13-2",
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978 1 930110 99 1"),
            "validateISBN13-3",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("9780201633856"),
            "validateISBN13-4",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978-0-201-63385-6"),
            "validateISBN13-5",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978 0 201 63385 6"),
            "validateISBN13-6",
        )
        self.assertEqual(
            "9781930110991", validator.validate("9781930110991"), "validate-1"
        )
        self.assertEqual(
            "9781930110991", validator.validate("978-1-930110-99-1"), "validate-2"
        )
        self.assertEqual(
            "9781930110991", validator.validate("978 1 930110 99 1"), "validate-3"
        )
        self.assertEqual(
            "9780201633856", validator.validate("9780201633856"), "validate-4"
        )
        self.assertEqual(
            "9780201633856", validator.validate("978-0-201-63385-6"), "validate-5"
        )
        self.assertEqual(
            "9780201633856", validator.validate("978 0 201 63385 6"), "validate-6"
        )

    def testValidateISBN13_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("9781930110991"),
            "validateISBN13-1",
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978-1-930110-99-1"),
            "validateISBN13-2",
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978 1 930110 99 1"),
            "validateISBN13-3",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("9780201633856"),
            "validateISBN13-4",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978-0-201-63385-6"),
            "validateISBN13-5",
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978 0 201 63385 6"),
            "validateISBN13-6",
        )

    def testValidateISBN13_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testValidateISBN10Convert_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "9781930110991", validator.validate("1930110995"), "validate-1"
        )
        self.assertEqual(
            "9781930110991", validator.validate("1-930110-99-5"), "validate-2"
        )
        self.assertEqual(
            "9781930110991", validator.validate("1 930110 99 5"), "validate-3"
        )
        self.assertEqual(
            "9780201633856", validator.validate("020163385X"), "validate-4"
        )
        self.assertEqual(
            "9780201633856", validator.validate("0-201-63385-X"), "validate-5"
        )
        self.assertEqual(
            "9780201633856", validator.validate("0 201 63385 X"), "validate-6"
        )

    def testValidateISBN10Convert_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testValidateISBN10_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance1(False)
        self.assertEqual(
            "1930110995", validator.validateISBN10("1930110995"), "validateISBN10-1"
        )
        self.assertEqual(
            "1930110995", validator.validateISBN10("1-930110-99-5"), "validateISBN10-2"
        )
        self.assertEqual(
            "1930110995", validator.validateISBN10("1 930110 99 5"), "validateISBN10-3"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("020163385X"), "validateISBN10-4"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("0-201-63385-X"), "validateISBN10-5"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("0 201 63385 X"), "validateISBN10-6"
        )
        self.assertEqual("1930110995", validator.validate("1930110995"), "validate-1")
        self.assertEqual(
            "1930110995", validator.validate("1-930110-99-5"), "validate-2"
        )
        self.assertEqual(
            "1930110995", validator.validate("1 930110 99 5"), "validate-3"
        )
        self.assertEqual("020163385X", validator.validate("020163385X"), "validate-4")
        self.assertEqual(
            "020163385X", validator.validate("0-201-63385-X"), "validate-5"
        )
        self.assertEqual(
            "020163385X", validator.validate("0 201 63385 X"), "validate-6"
        )

    def testValidateISBN10_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance1(False)
        self.assertEqual(
            "1930110995", validator.validateISBN10("1930110995"), "validateISBN10-1"
        )
        self.assertEqual(
            "1930110995", validator.validateISBN10("1-930110-99-5"), "validateISBN10-2"
        )
        self.assertEqual(
            "1930110995", validator.validateISBN10("1 930110 99 5"), "validateISBN10-3"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("020163385X"), "validateISBN10-4"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("0-201-63385-X"), "validateISBN10-5"
        )
        self.assertEqual(
            "020163385X", validator.validateISBN10("0 201 63385 X"), "validateISBN10-6"
        )

    def testValidateISBN10_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance1(False)

    def testIsValidISBN13_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(validator.isValidISBN13("9781930110991"), "isValidISBN13-1")
        self.assertTrue(validator.isValidISBN13("978-1-930110-99-1"), "isValidISBN13-2")
        self.assertTrue(validator.isValidISBN13("978 1 930110 99 1"), "isValidISBN13-3")
        self.assertTrue(validator.isValidISBN13("9780201633856"), "isValidISBN13-4")
        self.assertTrue(validator.isValidISBN13("978-0-201-63385-6"), "isValidISBN13-5")
        self.assertTrue(validator.isValidISBN13("978 0 201 63385 6"), "isValidISBN13-6")
        self.assertTrue(validator.isValid("9781930110991"), "isValid-1")
        self.assertTrue(validator.isValid("978-1-930110-99-1"), "isValid-2")
        self.assertTrue(validator.isValid("978 1 930110 99 1"), "isValid-3")
        self.assertTrue(validator.isValid("9780201633856"), "isValid-4")
        self.assertTrue(validator.isValid("978-0-201-63385-6"), "isValid-5")
        self.assertTrue(validator.isValid("978 0 201 63385 6"), "isValid-6")

    def testIsValidISBN13_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(validator.isValidISBN13("9781930110991"), "isValidISBN13-1")
        self.assertTrue(validator.isValidISBN13("978-1-930110-99-1"), "isValidISBN13-2")
        self.assertTrue(validator.isValidISBN13("978 1 930110 99 1"), "isValidISBN13-3")
        self.assertTrue(validator.isValidISBN13("9780201633856"), "isValidISBN13-4")
        self.assertTrue(validator.isValidISBN13("978-0-201-63385-6"), "isValidISBN13-5")
        self.assertTrue(validator.isValidISBN13("978 0 201 63385 6"), "isValidISBN13-6")

    def testIsValidISBN13_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testIsValidISBN10_test2_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(validator.isValidISBN10("1930110995"), "isValidISBN10-1")
        self.assertTrue(validator.isValidISBN10("1-930110-99-5"), "isValidISBN10-2")
        self.assertTrue(validator.isValidISBN10("1 930110 99 5"), "isValidISBN10-3")
        self.assertTrue(validator.isValidISBN10("020163385X"), "isValidISBN10-4")
        self.assertTrue(validator.isValidISBN10("0-201-63385-X"), "isValidISBN10-5")
        self.assertTrue(validator.isValidISBN10("0 201 63385 X"), "isValidISBN10-6")
        self.assertTrue(validator.isValid("1930110995"), "isValid-1")
        self.assertTrue(validator.isValid("1-930110-99-5"), "isValid-2")
        self.assertTrue(validator.isValid("1 930110 99 5"), "isValid-3")
        self.assertTrue(validator.isValid("020163385X"), "isValid-4")
        self.assertTrue(validator.isValid("0-201-63385-X"), "isValid-5")
        self.assertTrue(validator.isValid("0 201 63385 X"), "isValid-6")

    def testIsValidISBN10_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(validator.isValidISBN10("1930110995"), "isValidISBN10-1")
        self.assertTrue(validator.isValidISBN10("1-930110-99-5"), "isValidISBN10-2")
        self.assertTrue(validator.isValidISBN10("1 930110 99 5"), "isValidISBN10-3")
        self.assertTrue(validator.isValidISBN10("020163385X"), "isValidISBN10-4")
        self.assertTrue(validator.isValidISBN10("0-201-63385-X"), "isValidISBN10-5")
        self.assertTrue(validator.isValidISBN10("0 201 63385 X"), "isValidISBN10-6")

    def testIsValidISBN10_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testInvalidISBN13Format_test1_decomposed(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        validator = ISBNValidator.getInstance0()

        for i, isbn in enumerate(self.__invalidISBN13Format):
            # Check if the pattern does not match
            self.assertFalse(pattern.match(isbn), f"Pattern[{i}]={isbn}")

            # Check if the ISBN is not valid
            self.assertFalse(
                validator.isValidISBN13(isbn), f"isValidISBN13[{i}]={isbn}"
            )

            # Check if the validation result is None
            self.assertIsNone(
                validator.validateISBN13(isbn), f"validateISBN13[{i}]={isbn}"
            )

    def testInvalidISBN13Format_test0_decomposed(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        validator = ISBNValidator.getInstance0()

    def testValidISBN13Format_test0_decomposed(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        for i, isbn in enumerate(self.__validISBN13Format):
            self.assertTrue(pattern.match(isbn), f"Pattern[{i}]={isbn}")

    def testInvalidISBN10Format_test1_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()
        pattern = re.compile(ISBNValidator.ISBN10_REGEX)

        for i, isbn in enumerate(self.__invalidISBN10Format):
            # Check if the pattern does not match
            self.assertFalse(pattern.match(isbn), f"Pattern[{i}]={isbn}")

            # Check if the ISBN is not valid
            self.assertFalse(
                validator.isValidISBN10(isbn), f"isValidISBN10[{i}]={isbn}"
            )

            # Check if the validation result is None
            self.assertIsNone(
                validator.validateISBN10(isbn), f"validateISBN10[{i}]={isbn}"
            )

    def testInvalidISBN10Format_test0_decomposed(self) -> None:
        validator = ISBNValidator.getInstance0()

    def testValidISBN10Format_test0_decomposed(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN10_REGEX)
        for i, isbn in enumerate(self.__validISBN10Format):
            self.assertTrue(pattern.match(isbn), f"Pattern[{i}]={isbn}")
