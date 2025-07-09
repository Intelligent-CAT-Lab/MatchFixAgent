from __future__ import annotations
import time
import re
import random
import uuid
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNCodecTest import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64Test(unittest.TestCase):

    BASE64_IMPOSSIBLE_CASES: List[str] = [
        "ZE==",
        "ZmC=",
        "Zm9vYE==",
        "Zm9vYmC=",
        "AB",
    ]
    __random: random.Random = random.Random()
    __STANDARD_ENCODE_TABLE: typing.List[int] = [
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
        ord("g"),
        ord("h"),
        ord("i"),
        ord("j"),
        ord("k"),
        ord("l"),
        ord("m"),
        ord("n"),
        ord("o"),
        ord("p"),
        ord("q"),
        ord("r"),
        ord("s"),
        ord("t"),
        ord("u"),
        ord("v"),
        ord("w"),
        ord("x"),
        ord("y"),
        ord("z"),
        ord("0"),
        ord("1"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
        ord("8"),
        ord("9"),
        ord("+"),
        ord("/"),
    ]
    __CHARSET_UTF8: str = "utf-8"

    def testCodec265_test2_decomposed(self) -> None:
        size1GiB = 1 << 30
        blocks = -(-size1GiB // 3)  # Equivalent to Math.ceil(size1GiB / 3.0)
        expectedLength = 4 * blocks
        presumableFreeMemory = BaseNCodecTest.getPresumableFreeMemory()
        estimatedMemory = size1GiB * 4 + expectedLength + 32 * 1024
        self.assertTrue(
            presumableFreeMemory > estimatedMemory,
            "Not enough free memory for the test",
        )
        bytes_data = bytearray(size1GiB)
        encoded = Base64.encodeBase640(bytes_data)
        self.assertEqual(expectedLength, len(encoded))

    def testCodec265_test1_decomposed(self) -> None:
        size1GiB = 1 << 30
        blocks = -(-size1GiB // 3)  # Equivalent to Math.ceil(size1GiB / 3.0)
        expected_length = 4 * blocks
        presumable_free_memory = BaseNCodecTest.getPresumableFreeMemory()
        estimated_memory = size1GiB * 4 + expected_length + 32 * 1024
        if presumable_free_memory <= estimated_memory:
            self.skipTest("Not enough free memory for the test")
        bytes_data = bytearray(size1GiB)
        encoded = Base64.encodeBase640(bytes_data)

    def testCodec265_test0_decomposed(self) -> None:
        size1GiB = 1 << 30
        blocks = int((size1GiB + 2) // 3)  # Equivalent to Math.ceil(size1GiB / 3.0)
        expectedLength = 4 * blocks
        presumableFreeMemory = BaseNCodecTest.getPresumableFreeMemory()

    def testBase64DecodingOfTrailing18Bits_test0_decomposed(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(18)

    def testBase64DecodingOfTrailing12Bits_test0_decomposed(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(12)

    def testBase64DecodingOfTrailing6Bits_test0_decomposed(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(6)

    def testBase64ImpossibleSamples_test1_decomposed(self) -> None:
        codec = Base64(0, None, False, CodecPolicy.STRICT)
        for s in self.BASE64_IMPOSSIBLE_CASES:
            with self.assertRaises(
                ValueError, msg=f"Expected ValueError for input: {s}"
            ):
                codec.decode3(s)

    def testBase64ImpossibleSamples_test0_decomposed(self) -> None:
        codec = Base64(0, None, False, CodecPolicy.STRICT)

    def testHugeLineSeparator_test4_decomposed(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        bytesOriginal = StringUtils.getBytesUtf8(strOriginal)
        encoded = b64.encode0(bytesOriginal)
        decoded = b64.decode0(encoded)
        strDecoded = bytes(decoded).decode("utf-8")
        self.assertEqual("testDEFAULT_BUFFER_SIZE", strOriginal, strDecoded)

    def testHugeLineSeparator_test3_decomposed(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        bytesOriginal = StringUtils.getBytesUtf8(strOriginal)
        encoded = b64.encode0(bytesOriginal)
        decoded = b64.decode0(encoded)
        strDecoded = bytes(decoded).decode("utf-8")

    def testHugeLineSeparator_test2_decomposed(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        byteArray = StringUtils.getBytesUtf8(strOriginal)
        b64.encode0(byteArray)

    def testHugeLineSeparator_test1_decomposed(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        StringUtils.getBytesUtf8(strOriginal)

    def testHugeLineSeparator_test0_decomposed(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)

    def testStringToByteVariations_test17_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )
        Base64.decodeBase641(s2)
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode and assert for s3 (None)
        base64.decode3(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(base64.decode3(s3)), "StringToByte null"
        )
        Base64.decodeBase641(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(Base64.decodeBase641(s3)),
            "StringToByte static null",
        )

        # Decode and assert for s4b and s4a
        self.assertEqual(b4, base64.decode3(s4b), "StringToByte UUID")
        self.assertEqual(b4, Base64.decodeBase641(s4a), "StringToByte static UUID")
        self.assertEqual(
            b4, Base64.decodeBase641(s4b), "StringToByte static-url-safe UUID"
        )

    def testStringToByteVariations_test16_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )
        Base64.decodeBase641(s2)
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode and assert for s3 (None)
        base64.decode3(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(base64.decode3(s3)), "StringToByte null"
        )
        Base64.decodeBase641(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(Base64.decodeBase641(s3)),
            "StringToByte static null",
        )

        # Decode and assert for s4b
        self.assertListEqual(b4, base64.decode3(s4b), "StringToByte UUID")

    def testStringToByteVariations_test15_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )
        Base64.decodeBase641(s2)
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode and assert for s3 (null/None)
        base64.decode3(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(base64.decode3(s3)), "StringToByte null"
        )
        Base64.decodeBase641(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(Base64.decodeBase641(s3)),
            "StringToByte static null",
        )

    def testStringToByteVariations_test14_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )

        Base64.decodeBase641(s2)
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode and assert for s3
        base64.decode3(s3)
        self.assertIsNone(
            StringUtils.newStringUtf8(base64.decode3(s3)), "StringToByte null"
        )

        Base64.decodeBase641(s3)

    def testStringToByteVariations_test13_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode and assert for s3
        self.assertIsNone(
            StringUtils.newStringUtf8(base64.decode3(s3)), "StringToByte null"
        )

    def testStringToByteVariations_test12_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        # Decode using decode2 and assert for s1
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        # Static decodeBase641 and assert for s1
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2 (empty string)
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )

        # Static decodeBase641 and assert for s2 (empty string)
        Base64.decodeBase641(s2)
        self.assertEqual(
            "",
            StringUtils.newStringUtf8(Base64.decodeBase641(s2)),
            'StringToByte static ""',
        )

        # Decode for s3 (None) - this will likely raise an exception
        with self.assertRaises(DecoderException):
            base64.decode3(s3)

    def testStringToByteVariations_test11_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode and assert for s1
        decoded_s1 = base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1),
            "StringToByte Hello World",
        )

        # Decode using decode2 and assert for s1
        decoded_s1_obj = base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1_obj),
            "StringToByte Hello World",
        )

        # Static decodeBase641 and assert for s1
        static_decoded_s1 = Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(static_decoded_s1),
            "StringToByte static Hello World",
        )

        # Decode and assert for s2 (empty string)
        decoded_s2 = base64.decode3(s2)
        self.assertEqual("", StringUtils.newStringUtf8(decoded_s2), 'StringToByte ""')

        # Static decodeBase641 and assert for s2 (empty string)
        static_decoded_s2 = Base64.decodeBase641(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(static_decoded_s2), 'StringToByte static ""'
        )

    def testStringToByteVariations_test10_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        # Static decodeBase641 and assert
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode s2 and assert
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )

        # Static decodeBase641 for s2
        Base64.decodeBase641(s2)

    def testStringToByteVariations_test9_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert the result
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        # Static decodeBase641 method and assert the result
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode s2 and assert the result
        base64.decode3(s2)
        self.assertEqual(
            "", StringUtils.newStringUtf8(base64.decode3(s2)), 'StringToByte ""'
        )

    def testStringToByteVariations_test8_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert the result
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        # Static decode of s1 and assert the result
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

        # Decode s2 (empty string)
        base64.decode3(s2)

    def testStringToByteVariations_test7_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode3(s1)),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert the result
        base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(base64.decode2(s1)),
            "StringToByte Hello World",
        )

        # Decode s1 using the static method and assert the result
        Base64.decodeBase641(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(Base64.decodeBase641(s1)),
            "StringToByte static Hello World",
        )

    def testStringToByteVariations_test6_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        decoded_s1 = base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert the result
        decoded_s1_object = base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1_object),
            "StringToByte Hello World",
        )

        # Decode s1 using the static method
        Base64.decodeBase641(s1)

    def testStringToByteVariations_test5_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        decoded_s1 = base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1),
            "StringToByte Hello World",
        )

        # Decode s1 as an object and assert the result
        decoded_s1_obj = base64.decode2(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1_obj),
            "StringToByte Hello World",
        )

    def testStringToByteVariations_test4_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        decoded_s1 = base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1),
            "StringToByte Hello World",
        )

        # Decode s1 as an object
        base64.decode2(s1)

    def testStringToByteVariations_test3_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        # Decode s1 and assert the result
        decoded_s1 = base64.decode3(s1)
        self.assertEqual(
            "Hello World",
            StringUtils.newStringUtf8(decoded_s1),
            "StringToByte Hello World",
        )

    def testStringToByteVariations_test2_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        base64.decode3(s1)

    def testStringToByteVariations_test1_decomposed(self) -> None:
        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

    def testStringToByteVariations_test0_decomposed(self) -> None:
        base64 = Base64.Base645()

    def testByteToStringVariations_test11_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')
        self.assertIsNone(base64.encodeToString(b3), "byteToString null")
        self.assertIsNone(Base64.encodeBase64String(b3), "byteToString static null")
        self.assertEqual(
            "K/fMJwH+Q5e0nr7tWsxwkA==", base64.encodeToString(b4), "byteToString UUID"
        )
        self.assertEqual(
            "K/fMJwH+Q5e0nr7tWsxwkA==",
            Base64.encodeBase64String(b4),
            "byteToString static UUID",
        )
        self.assertEqual(
            "K_fMJwH-Q5e0nr7tWsxwkA",
            Base64.encodeBase64URLSafeString(b4),
            "byteToString static-url-safe UUID",
        )

    def testByteToStringVariations_test10_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')
        self.assertIsNone(base64.encodeToString(b3), "byteToString null")
        self.assertIsNone(Base64.encodeBase64String(b3), "byteToString static null")
        self.assertEqual(
            "K/fMJwH+Q5e0nr7tWsxwkA==", base64.encodeToString(b4), "byteToString UUID"
        )
        self.assertEqual(
            "K/fMJwH+Q5e0nr7tWsxwkA==",
            Base64.encodeBase64String(b4),
            "byteToString static UUID",
        )

    def testByteToStringVariations_test9_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')
        self.assertIsNone(base64.encodeToString(b3), "byteToString null")
        self.assertIsNone(Base64.encodeBase64String(b3), "byteToString static null")
        self.assertEqual(
            "K/fMJwH+Q5e0nr7tWsxwkA==", base64.encodeToString(b4), "byteToString UUID"
        )

    def testByteToStringVariations_test8_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')
        self.assertIsNone(base64.encodeToString(b3), "byteToString null")
        self.assertIsNone(Base64.encodeBase64String(b3), "byteToString static null")

    def testByteToStringVariations_test7_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')
        self.assertIsNone(base64.encodeToString(b3), "byteToString null")

    def testByteToStringVariations_test6_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')
        self.assertEqual("", Base64.encodeBase64String(b2), 'byteToString static ""')

    def testByteToStringVariations_test5_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )
        self.assertEqual("", base64.encodeToString(b2), 'byteToString ""')

    def testByteToStringVariations_test4_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )
        self.assertEqual(
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
            "byteToString static Hello World",
        )

    def testByteToStringVariations_test3_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        self.assertEqual(
            "SGVsbG8gV29ybGQ=", base64.encodeToString(b1), "byteToString Hello World"
        )

    def testByteToStringVariations_test2_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

    def testByteToStringVariations_test1_decomposed(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")

    def testByteToStringVariations_test0_decomposed(self) -> None:
        base64 = Base64.Base643(0)

    def testUUID_test10_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        urlSafe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]
        urlSafe2 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A="),
        ]
        urlSafe3 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA"),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA"),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg"),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A"),
        ]

        for i in range(4):
            encodedStandard = Base64.encodeBase640(ids[i])
            encodedUrlSafe = Base64.encodeBase64URLSafe(ids[i])
            decodedStandard = Base64.decodeBase640(standard[i])
            decodedUrlSafe1 = Base64.decodeBase640(urlSafe1[i])
            decodedUrlSafe2 = Base64.decodeBase640(urlSafe2[i])
            decodedUrlSafe3 = Base64.decodeBase640(urlSafe3[i])

            self.assertEqual(encodedStandard, standard[i], "standard encode uuid")
            self.assertEqual(encodedUrlSafe, urlSafe3[i], "url-safe encode uuid")
            self.assertEqual(decodedStandard, ids[i], "standard decode uuid")
            self.assertEqual(decodedUrlSafe1, ids[i], "url-safe1 decode uuid")
            self.assertEqual(decodedUrlSafe2, ids[i], "url-safe2 decode uuid")
            self.assertEqual(decodedUrlSafe3, ids[i], "url-safe3 decode uuid")

    def testUUID_test9_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        url_safe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]
        url_safe2 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A="),
        ]
        url_safe3 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA"),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA"),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg"),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A"),
        ]

    def testUUID_test8_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        url_safe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]
        url_safe2 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A="),
        ]
        url_safe3 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA"),
        ]

    def testUUID_test7_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        url_safe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]
        url_safe2 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A="),
        ]

    def testUUID_test6_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        url_safe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]
        url_safe2 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA="),
        ]

    def testUUID_test5_decomposed(self) -> None:
        ids = [
            Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"),
            Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090"),
            Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca"),
            Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8"),
        ]
        standard = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA=="),
            StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A=="),
        ]
        url_safe1 = [
            StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=="),
            StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=="),
            StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=="),
            StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=="),
        ]

    def testUUID_test4_decomposed(self) -> None:
        ids: List[List[int]] = [None] * 4
        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370")
        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca")
        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8")

        standard: List[List[int]] = [None] * 4
        standard[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA==")
        standard[1] = StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA==")
        standard[2] = StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg==")
        standard[3] = StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A==")

        urlSafe1: List[List[int]] = [None] * 4
        urlSafe1[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA==")

    def testUUID_test3_decomposed(self) -> None:
        ids = [None] * 4
        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370")
        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca")
        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8")

        standard = [None] * 4
        standard[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA==")
        standard[1] = StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA==")
        standard[2] = StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg==")
        standard[3] = StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A==")

    def testUUID_test2_decomposed(self) -> None:
        ids: List[List[int]] = [None] * 4
        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370")
        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca")
        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8")

        standard: List[List[int]] = [None] * 4
        standard[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA==")

    def testUUID_test1_decomposed(self) -> None:
        ids: List[List[int]] = [None] * 4
        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370")
        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca")
        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8")

    def testUUID_test0_decomposed(self) -> None:
        ids: List[Optional[bytes]] = [None] * 4
        ids[0] = bytes(Hex.decodeHex2("94ed8d0319e4493399560fb67404d370"))

    def testUrlSafe_test1_decomposed(self) -> None:
        codec = Base64.Base644(True)
        for i in range(151):  # Loop from 0 to 150 inclusive
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            result = Base64.decodeBase640(encoded)

            self.assertListEqual(decoded, result, f"url-safe i={i}")
            self.assertFalse(
                BaseNTestData.bytesContain(encoded, ord("=")), f"url-safe i={i} no '='"
            )
            self.assertFalse(
                BaseNTestData.bytesContain(encoded, ord("\\")),
                f"url-safe i={i} no '\\'",
            )
            self.assertFalse(
                BaseNTestData.bytesContain(encoded, ord("+")), f"url-safe i={i} no '+'"
            )

    def testUrlSafe_test0_decomposed(self) -> None:
        codec = Base64.Base644(True)

    def testTripletsChunked_test0_decomposed(self) -> None:
        self.assertEqual(
            "AAAA\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 0])).decode("utf-8"),
            "Failed for input [0, 0, 0]",
        )
        self.assertEqual(
            "AAAB\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 1])).decode("utf-8"),
            "Failed for input [0, 0, 1]",
        )
        self.assertEqual(
            "AAAC\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 2])).decode("utf-8"),
            "Failed for input [0, 0, 2]",
        )
        self.assertEqual(
            "AAAD\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 3])).decode("utf-8"),
            "Failed for input [0, 0, 3]",
        )
        self.assertEqual(
            "AAAE\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 4])).decode("utf-8"),
            "Failed for input [0, 0, 4]",
        )
        self.assertEqual(
            "AAAF\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 5])).decode("utf-8"),
            "Failed for input [0, 0, 5]",
        )
        self.assertEqual(
            "AAAG\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 6])).decode("utf-8"),
            "Failed for input [0, 0, 6]",
        )
        self.assertEqual(
            "AAAH\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 7])).decode("utf-8"),
            "Failed for input [0, 0, 7]",
        )
        self.assertEqual(
            "AAAI\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 8])).decode("utf-8"),
            "Failed for input [0, 0, 8]",
        )
        self.assertEqual(
            "AAAJ\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 9])).decode("utf-8"),
            "Failed for input [0, 0, 9]",
        )
        self.assertEqual(
            "AAAK\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 10])).decode("utf-8"),
            "Failed for input [0, 0, 10]",
        )
        self.assertEqual(
            "AAAL\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 11])).decode("utf-8"),
            "Failed for input [0, 0, 11]",
        )
        self.assertEqual(
            "AAAM\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 12])).decode("utf-8"),
            "Failed for input [0, 0, 12]",
        )
        self.assertEqual(
            "AAAN\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 13])).decode("utf-8"),
            "Failed for input [0, 0, 13]",
        )
        self.assertEqual(
            "AAAO\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 14])).decode("utf-8"),
            "Failed for input [0, 0, 14]",
        )
        self.assertEqual(
            "AAAP\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 15])).decode("utf-8"),
            "Failed for input [0, 0, 15]",
        )
        self.assertEqual(
            "AAAQ\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 16])).decode("utf-8"),
            "Failed for input [0, 0, 16]",
        )
        self.assertEqual(
            "AAAR\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 17])).decode("utf-8"),
            "Failed for input [0, 0, 17]",
        )
        self.assertEqual(
            "AAAS\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 18])).decode("utf-8"),
            "Failed for input [0, 0, 18]",
        )
        self.assertEqual(
            "AAAT\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 19])).decode("utf-8"),
            "Failed for input [0, 0, 19]",
        )
        self.assertEqual(
            "AAAU\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 20])).decode("utf-8"),
            "Failed for input [0, 0, 20]",
        )
        self.assertEqual(
            "AAAV\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 21])).decode("utf-8"),
            "Failed for input [0, 0, 21]",
        )
        self.assertEqual(
            "AAAW\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 22])).decode("utf-8"),
            "Failed for input [0, 0, 22]",
        )
        self.assertEqual(
            "AAAX\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 23])).decode("utf-8"),
            "Failed for input [0, 0, 23]",
        )
        self.assertEqual(
            "AAAY\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 24])).decode("utf-8"),
            "Failed for input [0, 0, 24]",
        )
        self.assertEqual(
            "AAAZ\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 25])).decode("utf-8"),
            "Failed for input [0, 0, 25]",
        )
        self.assertEqual(
            "AAAa\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 26])).decode("utf-8"),
            "Failed for input [0, 0, 26]",
        )
        self.assertEqual(
            "AAAb\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 27])).decode("utf-8"),
            "Failed for input [0, 0, 27]",
        )
        self.assertEqual(
            "AAAc\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 28])).decode("utf-8"),
            "Failed for input [0, 0, 28]",
        )
        self.assertEqual(
            "AAAd\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 29])).decode("utf-8"),
            "Failed for input [0, 0, 29]",
        )
        self.assertEqual(
            "AAAe\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 30])).decode("utf-8"),
            "Failed for input [0, 0, 30]",
        )
        self.assertEqual(
            "AAAf\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 31])).decode("utf-8"),
            "Failed for input [0, 0, 31]",
        )
        self.assertEqual(
            "AAAg\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 32])).decode("utf-8"),
            "Failed for input [0, 0, 32]",
        )
        self.assertEqual(
            "AAAh\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 33])).decode("utf-8"),
            "Failed for input [0, 0, 33]",
        )
        self.assertEqual(
            "AAAi\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 34])).decode("utf-8"),
            "Failed for input [0, 0, 34]",
        )
        self.assertEqual(
            "AAAj\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 35])).decode("utf-8"),
            "Failed for input [0, 0, 35]",
        )
        self.assertEqual(
            "AAAk\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 36])).decode("utf-8"),
            "Failed for input [0, 0, 36]",
        )
        self.assertEqual(
            "AAAl\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 37])).decode("utf-8"),
            "Failed for input [0, 0, 37]",
        )
        self.assertEqual(
            "AAAm\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 38])).decode("utf-8"),
            "Failed for input [0, 0, 38]",
        )
        self.assertEqual(
            "AAAn\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 39])).decode("utf-8"),
            "Failed for input [0, 0, 39]",
        )
        self.assertEqual(
            "AAAo\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 40])).decode("utf-8"),
            "Failed for input [0, 0, 40]",
        )
        self.assertEqual(
            "AAAp\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 41])).decode("utf-8"),
            "Failed for input [0, 0, 41]",
        )
        self.assertEqual(
            "AAAq\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 42])).decode("utf-8"),
            "Failed for input [0, 0, 42]",
        )
        self.assertEqual(
            "AAAr\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 43])).decode("utf-8"),
            "Failed for input [0, 0, 43]",
        )
        self.assertEqual(
            "AAAs\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 44])).decode("utf-8"),
            "Failed for input [0, 0, 44]",
        )
        self.assertEqual(
            "AAAt\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 45])).decode("utf-8"),
            "Failed for input [0, 0, 45]",
        )
        self.assertEqual(
            "AAAu\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 46])).decode("utf-8"),
            "Failed for input [0, 0, 46]",
        )
        self.assertEqual(
            "AAAv\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 47])).decode("utf-8"),
            "Failed for input [0, 0, 47]",
        )
        self.assertEqual(
            "AAAw\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 48])).decode("utf-8"),
            "Failed for input [0, 0, 48]",
        )
        self.assertEqual(
            "AAAx\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 49])).decode("utf-8"),
            "Failed for input [0, 0, 49]",
        )
        self.assertEqual(
            "AAAy\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 50])).decode("utf-8"),
            "Failed for input [0, 0, 50]",
        )
        self.assertEqual(
            "AAAz\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 51])).decode("utf-8"),
            "Failed for input [0, 0, 51]",
        )
        self.assertEqual(
            "AAA0\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 52])).decode("utf-8"),
            "Failed for input [0, 0, 52]",
        )
        self.assertEqual(
            "AAA1\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 53])).decode("utf-8"),
            "Failed for input [0, 0, 53]",
        )
        self.assertEqual(
            "AAA2\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 54])).decode("utf-8"),
            "Failed for input [0, 0, 54]",
        )
        self.assertEqual(
            "AAA3\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 55])).decode("utf-8"),
            "Failed for input [0, 0, 55]",
        )
        self.assertEqual(
            "AAA4\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 56])).decode("utf-8"),
            "Failed for input [0, 0, 56]",
        )
        self.assertEqual(
            "AAA5\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 57])).decode("utf-8"),
            "Failed for input [0, 0, 57]",
        )
        self.assertEqual(
            "AAA6\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 58])).decode("utf-8"),
            "Failed for input [0, 0, 58]",
        )
        self.assertEqual(
            "AAA7\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 59])).decode("utf-8"),
            "Failed for input [0, 0, 59]",
        )
        self.assertEqual(
            "AAA8\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 60])).decode("utf-8"),
            "Failed for input [0, 0, 60]",
        )
        self.assertEqual(
            "AAA9\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 61])).decode("utf-8"),
            "Failed for input [0, 0, 61]",
        )
        self.assertEqual(
            "AAA+\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 62])).decode("utf-8"),
            "Failed for input [0, 0, 62]",
        )
        self.assertEqual(
            "AAA/\r\n",
            Base64.encodeBase64Chunked(bytearray([0, 0, 63])).decode("utf-8"),
            "Failed for input [0, 0, 63]",
        )

    def testTriplets_test0_decomposed(self) -> None:
        self.assertEqual(
            "AAAA",
            Base64.encodeBase640([0, 0, 0]).decode("utf-8"),
            "Encoding failed for input [0, 0, 0]",
        )
        self.assertEqual(
            "AAAB",
            Base64.encodeBase640([0, 0, 1]).decode("utf-8"),
            "Encoding failed for input [0, 0, 1]",
        )
        self.assertEqual(
            "AAAC",
            Base64.encodeBase640([0, 0, 2]).decode("utf-8"),
            "Encoding failed for input [0, 0, 2]",
        )
        self.assertEqual(
            "AAAD",
            Base64.encodeBase640([0, 0, 3]).decode("utf-8"),
            "Encoding failed for input [0, 0, 3]",
        )
        self.assertEqual(
            "AAAE",
            Base64.encodeBase640([0, 0, 4]).decode("utf-8"),
            "Encoding failed for input [0, 0, 4]",
        )
        self.assertEqual(
            "AAAF",
            Base64.encodeBase640([0, 0, 5]).decode("utf-8"),
            "Encoding failed for input [0, 0, 5]",
        )
        self.assertEqual(
            "AAAG",
            Base64.encodeBase640([0, 0, 6]).decode("utf-8"),
            "Encoding failed for input [0, 0, 6]",
        )
        self.assertEqual(
            "AAAH",
            Base64.encodeBase640([0, 0, 7]).decode("utf-8"),
            "Encoding failed for input [0, 0, 7]",
        )
        self.assertEqual(
            "AAAI",
            Base64.encodeBase640([0, 0, 8]).decode("utf-8"),
            "Encoding failed for input [0, 0, 8]",
        )
        self.assertEqual(
            "AAAJ",
            Base64.encodeBase640([0, 0, 9]).decode("utf-8"),
            "Encoding failed for input [0, 0, 9]",
        )
        self.assertEqual(
            "AAAK",
            Base64.encodeBase640([0, 0, 10]).decode("utf-8"),
            "Encoding failed for input [0, 0, 10]",
        )
        self.assertEqual(
            "AAAL",
            Base64.encodeBase640([0, 0, 11]).decode("utf-8"),
            "Encoding failed for input [0, 0, 11]",
        )
        self.assertEqual(
            "AAAM",
            Base64.encodeBase640([0, 0, 12]).decode("utf-8"),
            "Encoding failed for input [0, 0, 12]",
        )
        self.assertEqual(
            "AAAN",
            Base64.encodeBase640([0, 0, 13]).decode("utf-8"),
            "Encoding failed for input [0, 0, 13]",
        )
        self.assertEqual(
            "AAAO",
            Base64.encodeBase640([0, 0, 14]).decode("utf-8"),
            "Encoding failed for input [0, 0, 14]",
        )
        self.assertEqual(
            "AAAP",
            Base64.encodeBase640([0, 0, 15]).decode("utf-8"),
            "Encoding failed for input [0, 0, 15]",
        )
        self.assertEqual(
            "AAAQ",
            Base64.encodeBase640([0, 0, 16]).decode("utf-8"),
            "Encoding failed for input [0, 0, 16]",
        )
        self.assertEqual(
            "AAAR",
            Base64.encodeBase640([0, 0, 17]).decode("utf-8"),
            "Encoding failed for input [0, 0, 17]",
        )
        self.assertEqual(
            "AAAS",
            Base64.encodeBase640([0, 0, 18]).decode("utf-8"),
            "Encoding failed for input [0, 0, 18]",
        )
        self.assertEqual(
            "AAAT",
            Base64.encodeBase640([0, 0, 19]).decode("utf-8"),
            "Encoding failed for input [0, 0, 19]",
        )
        self.assertEqual(
            "AAAU",
            Base64.encodeBase640([0, 0, 20]).decode("utf-8"),
            "Encoding failed for input [0, 0, 20]",
        )
        self.assertEqual(
            "AAAV",
            Base64.encodeBase640([0, 0, 21]).decode("utf-8"),
            "Encoding failed for input [0, 0, 21]",
        )
        self.assertEqual(
            "AAAW",
            Base64.encodeBase640([0, 0, 22]).decode("utf-8"),
            "Encoding failed for input [0, 0, 22]",
        )
        self.assertEqual(
            "AAAX",
            Base64.encodeBase640([0, 0, 23]).decode("utf-8"),
            "Encoding failed for input [0, 0, 23]",
        )
        self.assertEqual(
            "AAAY",
            Base64.encodeBase640([0, 0, 24]).decode("utf-8"),
            "Encoding failed for input [0, 0, 24]",
        )
        self.assertEqual(
            "AAAZ",
            Base64.encodeBase640([0, 0, 25]).decode("utf-8"),
            "Encoding failed for input [0, 0, 25]",
        )
        self.assertEqual(
            "AAAa",
            Base64.encodeBase640([0, 0, 26]).decode("utf-8"),
            "Encoding failed for input [0, 0, 26]",
        )
        self.assertEqual(
            "AAAb",
            Base64.encodeBase640([0, 0, 27]).decode("utf-8"),
            "Encoding failed for input [0, 0, 27]",
        )
        self.assertEqual(
            "AAAc",
            Base64.encodeBase640([0, 0, 28]).decode("utf-8"),
            "Encoding failed for input [0, 0, 28]",
        )
        self.assertEqual(
            "AAAd",
            Base64.encodeBase640([0, 0, 29]).decode("utf-8"),
            "Encoding failed for input [0, 0, 29]",
        )
        self.assertEqual(
            "AAAe",
            Base64.encodeBase640([0, 0, 30]).decode("utf-8"),
            "Encoding failed for input [0, 0, 30]",
        )
        self.assertEqual(
            "AAAf",
            Base64.encodeBase640([0, 0, 31]).decode("utf-8"),
            "Encoding failed for input [0, 0, 31]",
        )
        self.assertEqual(
            "AAAg",
            Base64.encodeBase640([0, 0, 32]).decode("utf-8"),
            "Encoding failed for input [0, 0, 32]",
        )
        self.assertEqual(
            "AAAh",
            Base64.encodeBase640([0, 0, 33]).decode("utf-8"),
            "Encoding failed for input [0, 0, 33]",
        )
        self.assertEqual(
            "AAAi",
            Base64.encodeBase640([0, 0, 34]).decode("utf-8"),
            "Encoding failed for input [0, 0, 34]",
        )
        self.assertEqual(
            "AAAj",
            Base64.encodeBase640([0, 0, 35]).decode("utf-8"),
            "Encoding failed for input [0, 0, 35]",
        )
        self.assertEqual(
            "AAAk",
            Base64.encodeBase640([0, 0, 36]).decode("utf-8"),
            "Encoding failed for input [0, 0, 36]",
        )
        self.assertEqual(
            "AAAl",
            Base64.encodeBase640([0, 0, 37]).decode("utf-8"),
            "Encoding failed for input [0, 0, 37]",
        )
        self.assertEqual(
            "AAAm",
            Base64.encodeBase640([0, 0, 38]).decode("utf-8"),
            "Encoding failed for input [0, 0, 38]",
        )
        self.assertEqual(
            "AAAn",
            Base64.encodeBase640([0, 0, 39]).decode("utf-8"),
            "Encoding failed for input [0, 0, 39]",
        )
        self.assertEqual(
            "AAAo",
            Base64.encodeBase640([0, 0, 40]).decode("utf-8"),
            "Encoding failed for input [0, 0, 40]",
        )
        self.assertEqual(
            "AAAp",
            Base64.encodeBase640([0, 0, 41]).decode("utf-8"),
            "Encoding failed for input [0, 0, 41]",
        )
        self.assertEqual(
            "AAAq",
            Base64.encodeBase640([0, 0, 42]).decode("utf-8"),
            "Encoding failed for input [0, 0, 42]",
        )
        self.assertEqual(
            "AAAr",
            Base64.encodeBase640([0, 0, 43]).decode("utf-8"),
            "Encoding failed for input [0, 0, 43]",
        )
        self.assertEqual(
            "AAAs",
            Base64.encodeBase640([0, 0, 44]).decode("utf-8"),
            "Encoding failed for input [0, 0, 44]",
        )
        self.assertEqual(
            "AAAt",
            Base64.encodeBase640([0, 0, 45]).decode("utf-8"),
            "Encoding failed for input [0, 0, 45]",
        )
        self.assertEqual(
            "AAAu",
            Base64.encodeBase640([0, 0, 46]).decode("utf-8"),
            "Encoding failed for input [0, 0, 46]",
        )
        self.assertEqual(
            "AAAv",
            Base64.encodeBase640([0, 0, 47]).decode("utf-8"),
            "Encoding failed for input [0, 0, 47]",
        )
        self.assertEqual(
            "AAAw",
            Base64.encodeBase640([0, 0, 48]).decode("utf-8"),
            "Encoding failed for input [0, 0, 48]",
        )
        self.assertEqual(
            "AAAx",
            Base64.encodeBase640([0, 0, 49]).decode("utf-8"),
            "Encoding failed for input [0, 0, 49]",
        )
        self.assertEqual(
            "AAAy",
            Base64.encodeBase640([0, 0, 50]).decode("utf-8"),
            "Encoding failed for input [0, 0, 50]",
        )
        self.assertEqual(
            "AAAz",
            Base64.encodeBase640([0, 0, 51]).decode("utf-8"),
            "Encoding failed for input [0, 0, 51]",
        )
        self.assertEqual(
            "AAA0",
            Base64.encodeBase640([0, 0, 52]).decode("utf-8"),
            "Encoding failed for input [0, 0, 52]",
        )
        self.assertEqual(
            "AAA1",
            Base64.encodeBase640([0, 0, 53]).decode("utf-8"),
            "Encoding failed for input [0, 0, 53]",
        )
        self.assertEqual(
            "AAA2",
            Base64.encodeBase640([0, 0, 54]).decode("utf-8"),
            "Encoding failed for input [0, 0, 54]",
        )
        self.assertEqual(
            "AAA3",
            Base64.encodeBase640([0, 0, 55]).decode("utf-8"),
            "Encoding failed for input [0, 0, 55]",
        )
        self.assertEqual(
            "AAA4",
            Base64.encodeBase640([0, 0, 56]).decode("utf-8"),
            "Encoding failed for input [0, 0, 56]",
        )
        self.assertEqual(
            "AAA5",
            Base64.encodeBase640([0, 0, 57]).decode("utf-8"),
            "Encoding failed for input [0, 0, 57]",
        )
        self.assertEqual(
            "AAA6",
            Base64.encodeBase640([0, 0, 58]).decode("utf-8"),
            "Encoding failed for input [0, 0, 58]",
        )
        self.assertEqual(
            "AAA7",
            Base64.encodeBase640([0, 0, 59]).decode("utf-8"),
            "Encoding failed for input [0, 0, 59]",
        )
        self.assertEqual(
            "AAA8",
            Base64.encodeBase640([0, 0, 60]).decode("utf-8"),
            "Encoding failed for input [0, 0, 60]",
        )
        self.assertEqual(
            "AAA9",
            Base64.encodeBase640([0, 0, 61]).decode("utf-8"),
            "Encoding failed for input [0, 0, 61]",
        )
        self.assertEqual(
            "AAA+",
            Base64.encodeBase640([0, 0, 62]).decode("utf-8"),
            "Encoding failed for input [0, 0, 62]",
        )
        self.assertEqual(
            "AAA/",
            Base64.encodeBase640([0, 0, 63]).decode("utf-8"),
            "Encoding failed for input [0, 0, 63]",
        )

    def testSingletonsChunked_test0_decomposed(self) -> None:
        self.assertEqual(
            "AA==\r\n", Base64.encodeBase64Chunked(bytes([0])).decode("utf-8")
        )
        self.assertEqual(
            "AQ==\r\n", Base64.encodeBase64Chunked(bytes([1])).decode("utf-8")
        )
        self.assertEqual(
            "Ag==\r\n", Base64.encodeBase64Chunked(bytes([2])).decode("utf-8")
        )
        self.assertEqual(
            "Aw==\r\n", Base64.encodeBase64Chunked(bytes([3])).decode("utf-8")
        )
        self.assertEqual(
            "BA==\r\n", Base64.encodeBase64Chunked(bytes([4])).decode("utf-8")
        )
        self.assertEqual(
            "BQ==\r\n", Base64.encodeBase64Chunked(bytes([5])).decode("utf-8")
        )
        self.assertEqual(
            "Bg==\r\n", Base64.encodeBase64Chunked(bytes([6])).decode("utf-8")
        )
        self.assertEqual(
            "Bw==\r\n", Base64.encodeBase64Chunked(bytes([7])).decode("utf-8")
        )
        self.assertEqual(
            "CA==\r\n", Base64.encodeBase64Chunked(bytes([8])).decode("utf-8")
        )
        self.assertEqual(
            "CQ==\r\n", Base64.encodeBase64Chunked(bytes([9])).decode("utf-8")
        )
        self.assertEqual(
            "Cg==\r\n", Base64.encodeBase64Chunked(bytes([10])).decode("utf-8")
        )
        self.assertEqual(
            "Cw==\r\n", Base64.encodeBase64Chunked(bytes([11])).decode("utf-8")
        )
        self.assertEqual(
            "DA==\r\n", Base64.encodeBase64Chunked(bytes([12])).decode("utf-8")
        )
        self.assertEqual(
            "DQ==\r\n", Base64.encodeBase64Chunked(bytes([13])).decode("utf-8")
        )
        self.assertEqual(
            "Dg==\r\n", Base64.encodeBase64Chunked(bytes([14])).decode("utf-8")
        )
        self.assertEqual(
            "Dw==\r\n", Base64.encodeBase64Chunked(bytes([15])).decode("utf-8")
        )
        self.assertEqual(
            "EA==\r\n", Base64.encodeBase64Chunked(bytes([16])).decode("utf-8")
        )
        self.assertEqual(
            "EQ==\r\n", Base64.encodeBase64Chunked(bytes([17])).decode("utf-8")
        )
        self.assertEqual(
            "Eg==\r\n", Base64.encodeBase64Chunked(bytes([18])).decode("utf-8")
        )
        self.assertEqual(
            "Ew==\r\n", Base64.encodeBase64Chunked(bytes([19])).decode("utf-8")
        )
        self.assertEqual(
            "FA==\r\n", Base64.encodeBase64Chunked(bytes([20])).decode("utf-8")
        )
        self.assertEqual(
            "FQ==\r\n", Base64.encodeBase64Chunked(bytes([21])).decode("utf-8")
        )
        self.assertEqual(
            "Fg==\r\n", Base64.encodeBase64Chunked(bytes([22])).decode("utf-8")
        )
        self.assertEqual(
            "Fw==\r\n", Base64.encodeBase64Chunked(bytes([23])).decode("utf-8")
        )
        self.assertEqual(
            "GA==\r\n", Base64.encodeBase64Chunked(bytes([24])).decode("utf-8")
        )
        self.assertEqual(
            "GQ==\r\n", Base64.encodeBase64Chunked(bytes([25])).decode("utf-8")
        )
        self.assertEqual(
            "Gg==\r\n", Base64.encodeBase64Chunked(bytes([26])).decode("utf-8")
        )
        self.assertEqual(
            "Gw==\r\n", Base64.encodeBase64Chunked(bytes([27])).decode("utf-8")
        )
        self.assertEqual(
            "HA==\r\n", Base64.encodeBase64Chunked(bytes([28])).decode("utf-8")
        )
        self.assertEqual(
            "HQ==\r\n", Base64.encodeBase64Chunked(bytes([29])).decode("utf-8")
        )
        self.assertEqual(
            "Hg==\r\n", Base64.encodeBase64Chunked(bytes([30])).decode("utf-8")
        )
        self.assertEqual(
            "Hw==\r\n", Base64.encodeBase64Chunked(bytes([31])).decode("utf-8")
        )
        self.assertEqual(
            "IA==\r\n", Base64.encodeBase64Chunked(bytes([32])).decode("utf-8")
        )
        self.assertEqual(
            "IQ==\r\n", Base64.encodeBase64Chunked(bytes([33])).decode("utf-8")
        )
        self.assertEqual(
            "Ig==\r\n", Base64.encodeBase64Chunked(bytes([34])).decode("utf-8")
        )
        self.assertEqual(
            "Iw==\r\n", Base64.encodeBase64Chunked(bytes([35])).decode("utf-8")
        )
        self.assertEqual(
            "JA==\r\n", Base64.encodeBase64Chunked(bytes([36])).decode("utf-8")
        )
        self.assertEqual(
            "JQ==\r\n", Base64.encodeBase64Chunked(bytes([37])).decode("utf-8")
        )
        self.assertEqual(
            "Jg==\r\n", Base64.encodeBase64Chunked(bytes([38])).decode("utf-8")
        )
        self.assertEqual(
            "Jw==\r\n", Base64.encodeBase64Chunked(bytes([39])).decode("utf-8")
        )
        self.assertEqual(
            "KA==\r\n", Base64.encodeBase64Chunked(bytes([40])).decode("utf-8")
        )
        self.assertEqual(
            "KQ==\r\n", Base64.encodeBase64Chunked(bytes([41])).decode("utf-8")
        )
        self.assertEqual(
            "Kg==\r\n", Base64.encodeBase64Chunked(bytes([42])).decode("utf-8")
        )
        self.assertEqual(
            "Kw==\r\n", Base64.encodeBase64Chunked(bytes([43])).decode("utf-8")
        )
        self.assertEqual(
            "LA==\r\n", Base64.encodeBase64Chunked(bytes([44])).decode("utf-8")
        )
        self.assertEqual(
            "LQ==\r\n", Base64.encodeBase64Chunked(bytes([45])).decode("utf-8")
        )
        self.assertEqual(
            "Lg==\r\n", Base64.encodeBase64Chunked(bytes([46])).decode("utf-8")
        )
        self.assertEqual(
            "Lw==\r\n", Base64.encodeBase64Chunked(bytes([47])).decode("utf-8")
        )
        self.assertEqual(
            "MA==\r\n", Base64.encodeBase64Chunked(bytes([48])).decode("utf-8")
        )
        self.assertEqual(
            "MQ==\r\n", Base64.encodeBase64Chunked(bytes([49])).decode("utf-8")
        )
        self.assertEqual(
            "Mg==\r\n", Base64.encodeBase64Chunked(bytes([50])).decode("utf-8")
        )
        self.assertEqual(
            "Mw==\r\n", Base64.encodeBase64Chunked(bytes([51])).decode("utf-8")
        )
        self.assertEqual(
            "NA==\r\n", Base64.encodeBase64Chunked(bytes([52])).decode("utf-8")
        )
        self.assertEqual(
            "NQ==\r\n", Base64.encodeBase64Chunked(bytes([53])).decode("utf-8")
        )
        self.assertEqual(
            "Ng==\r\n", Base64.encodeBase64Chunked(bytes([54])).decode("utf-8")
        )
        self.assertEqual(
            "Nw==\r\n", Base64.encodeBase64Chunked(bytes([55])).decode("utf-8")
        )
        self.assertEqual(
            "OA==\r\n", Base64.encodeBase64Chunked(bytes([56])).decode("utf-8")
        )
        self.assertEqual(
            "OQ==\r\n", Base64.encodeBase64Chunked(bytes([57])).decode("utf-8")
        )
        self.assertEqual(
            "Og==\r\n", Base64.encodeBase64Chunked(bytes([58])).decode("utf-8")
        )
        self.assertEqual(
            "Ow==\r\n", Base64.encodeBase64Chunked(bytes([59])).decode("utf-8")
        )
        self.assertEqual(
            "PA==\r\n", Base64.encodeBase64Chunked(bytes([60])).decode("utf-8")
        )
        self.assertEqual(
            "PQ==\r\n", Base64.encodeBase64Chunked(bytes([61])).decode("utf-8")
        )
        self.assertEqual(
            "Pg==\r\n", Base64.encodeBase64Chunked(bytes([62])).decode("utf-8")
        )
        self.assertEqual(
            "Pw==\r\n", Base64.encodeBase64Chunked(bytes([63])).decode("utf-8")
        )
        self.assertEqual(
            "QA==\r\n", Base64.encodeBase64Chunked(bytes([64])).decode("utf-8")
        )
        self.assertEqual(
            "QQ==\r\n", Base64.encodeBase64Chunked(bytes([65])).decode("utf-8")
        )
        self.assertEqual(
            "Qg==\r\n", Base64.encodeBase64Chunked(bytes([66])).decode("utf-8")
        )
        self.assertEqual(
            "Qw==\r\n", Base64.encodeBase64Chunked(bytes([67])).decode("utf-8")
        )
        self.assertEqual(
            "RA==\r\n", Base64.encodeBase64Chunked(bytes([68])).decode("utf-8")
        )
        self.assertEqual(
            "RQ==\r\n", Base64.encodeBase64Chunked(bytes([69])).decode("utf-8")
        )
        self.assertEqual(
            "Rg==\r\n", Base64.encodeBase64Chunked(bytes([70])).decode("utf-8")
        )
        self.assertEqual(
            "Rw==\r\n", Base64.encodeBase64Chunked(bytes([71])).decode("utf-8")
        )
        self.assertEqual(
            "SA==\r\n", Base64.encodeBase64Chunked(bytes([72])).decode("utf-8")
        )
        self.assertEqual(
            "SQ==\r\n", Base64.encodeBase64Chunked(bytes([73])).decode("utf-8")
        )
        self.assertEqual(
            "Sg==\r\n", Base64.encodeBase64Chunked(bytes([74])).decode("utf-8")
        )
        self.assertEqual(
            "Sw==\r\n", Base64.encodeBase64Chunked(bytes([75])).decode("utf-8")
        )
        self.assertEqual(
            "TA==\r\n", Base64.encodeBase64Chunked(bytes([76])).decode("utf-8")
        )
        self.assertEqual(
            "TQ==\r\n", Base64.encodeBase64Chunked(bytes([77])).decode("utf-8")
        )
        self.assertEqual(
            "Tg==\r\n", Base64.encodeBase64Chunked(bytes([78])).decode("utf-8")
        )
        self.assertEqual(
            "Tw==\r\n", Base64.encodeBase64Chunked(bytes([79])).decode("utf-8")
        )
        self.assertEqual(
            "UA==\r\n", Base64.encodeBase64Chunked(bytes([80])).decode("utf-8")
        )
        self.assertEqual(
            "UQ==\r\n", Base64.encodeBase64Chunked(bytes([81])).decode("utf-8")
        )
        self.assertEqual(
            "Ug==\r\n", Base64.encodeBase64Chunked(bytes([82])).decode("utf-8")
        )
        self.assertEqual(
            "Uw==\r\n", Base64.encodeBase64Chunked(bytes([83])).decode("utf-8")
        )
        self.assertEqual(
            "VA==\r\n", Base64.encodeBase64Chunked(bytes([84])).decode("utf-8")
        )
        self.assertEqual(
            "VQ==\r\n", Base64.encodeBase64Chunked(bytes([85])).decode("utf-8")
        )
        self.assertEqual(
            "Vg==\r\n", Base64.encodeBase64Chunked(bytes([86])).decode("utf-8")
        )
        self.assertEqual(
            "Vw==\r\n", Base64.encodeBase64Chunked(bytes([87])).decode("utf-8")
        )
        self.assertEqual(
            "WA==\r\n", Base64.encodeBase64Chunked(bytes([88])).decode("utf-8")
        )
        self.assertEqual(
            "WQ==\r\n", Base64.encodeBase64Chunked(bytes([89])).decode("utf-8")
        )
        self.assertEqual(
            "Wg==\r\n", Base64.encodeBase64Chunked(bytes([90])).decode("utf-8")
        )
        self.assertEqual(
            "Ww==\r\n", Base64.encodeBase64Chunked(bytes([91])).decode("utf-8")
        )
        self.assertEqual(
            "XA==\r\n", Base64.encodeBase64Chunked(bytes([92])).decode("utf-8")
        )
        self.assertEqual(
            "XQ==\r\n", Base64.encodeBase64Chunked(bytes([93])).decode("utf-8")
        )
        self.assertEqual(
            "Xg==\r\n", Base64.encodeBase64Chunked(bytes([94])).decode("utf-8")
        )
        self.assertEqual(
            "Xw==\r\n", Base64.encodeBase64Chunked(bytes([95])).decode("utf-8")
        )
        self.assertEqual(
            "YA==\r\n", Base64.encodeBase64Chunked(bytes([96])).decode("utf-8")
        )
        self.assertEqual(
            "YQ==\r\n", Base64.encodeBase64Chunked(bytes([97])).decode("utf-8")
        )
        self.assertEqual(
            "Yg==\r\n", Base64.encodeBase64Chunked(bytes([98])).decode("utf-8")
        )
        self.assertEqual(
            "Yw==\r\n", Base64.encodeBase64Chunked(bytes([99])).decode("utf-8")
        )
        self.assertEqual(
            "ZA==\r\n", Base64.encodeBase64Chunked(bytes([100])).decode("utf-8")
        )
        self.assertEqual(
            "ZQ==\r\n", Base64.encodeBase64Chunked(bytes([101])).decode("utf-8")
        )
        self.assertEqual(
            "Zg==\r\n", Base64.encodeBase64Chunked(bytes([102])).decode("utf-8")
        )
        self.assertEqual(
            "Zw==\r\n", Base64.encodeBase64Chunked(bytes([103])).decode("utf-8")
        )
        self.assertEqual(
            "aA==\r\n", Base64.encodeBase64Chunked(bytes([104])).decode("utf-8")
        )

    def testSingletons_test1_decomposed(self) -> None:
        self.assertEqual("AA==", Base64.encodeBase640([0]).decode("utf-8"))
        self.assertEqual("AQ==", Base64.encodeBase640([1]).decode("utf-8"))
        self.assertEqual("Ag==", Base64.encodeBase640([2]).decode("utf-8"))
        self.assertEqual("Aw==", Base64.encodeBase640([3]).decode("utf-8"))
        self.assertEqual("BA==", Base64.encodeBase640([4]).decode("utf-8"))
        self.assertEqual("BQ==", Base64.encodeBase640([5]).decode("utf-8"))
        self.assertEqual("Bg==", Base64.encodeBase640([6]).decode("utf-8"))
        self.assertEqual("Bw==", Base64.encodeBase640([7]).decode("utf-8"))
        self.assertEqual("CA==", Base64.encodeBase640([8]).decode("utf-8"))
        self.assertEqual("CQ==", Base64.encodeBase640([9]).decode("utf-8"))
        self.assertEqual("Cg==", Base64.encodeBase640([10]).decode("utf-8"))
        self.assertEqual("Cw==", Base64.encodeBase640([11]).decode("utf-8"))
        self.assertEqual("DA==", Base64.encodeBase640([12]).decode("utf-8"))
        self.assertEqual("DQ==", Base64.encodeBase640([13]).decode("utf-8"))
        self.assertEqual("Dg==", Base64.encodeBase640([14]).decode("utf-8"))
        self.assertEqual("Dw==", Base64.encodeBase640([15]).decode("utf-8"))
        self.assertEqual("EA==", Base64.encodeBase640([16]).decode("utf-8"))
        self.assertEqual("EQ==", Base64.encodeBase640([17]).decode("utf-8"))
        self.assertEqual("Eg==", Base64.encodeBase640([18]).decode("utf-8"))
        self.assertEqual("Ew==", Base64.encodeBase640([19]).decode("utf-8"))
        self.assertEqual("FA==", Base64.encodeBase640([20]).decode("utf-8"))
        self.assertEqual("FQ==", Base64.encodeBase640([21]).decode("utf-8"))
        self.assertEqual("Fg==", Base64.encodeBase640([22]).decode("utf-8"))
        self.assertEqual("Fw==", Base64.encodeBase640([23]).decode("utf-8"))
        self.assertEqual("GA==", Base64.encodeBase640([24]).decode("utf-8"))
        self.assertEqual("GQ==", Base64.encodeBase640([25]).decode("utf-8"))
        self.assertEqual("Gg==", Base64.encodeBase640([26]).decode("utf-8"))
        self.assertEqual("Gw==", Base64.encodeBase640([27]).decode("utf-8"))
        self.assertEqual("HA==", Base64.encodeBase640([28]).decode("utf-8"))
        self.assertEqual("HQ==", Base64.encodeBase640([29]).decode("utf-8"))
        self.assertEqual("Hg==", Base64.encodeBase640([30]).decode("utf-8"))
        self.assertEqual("Hw==", Base64.encodeBase640([31]).decode("utf-8"))
        self.assertEqual("IA==", Base64.encodeBase640([32]).decode("utf-8"))
        self.assertEqual("IQ==", Base64.encodeBase640([33]).decode("utf-8"))
        self.assertEqual("Ig==", Base64.encodeBase640([34]).decode("utf-8"))
        self.assertEqual("Iw==", Base64.encodeBase640([35]).decode("utf-8"))
        self.assertEqual("JA==", Base64.encodeBase640([36]).decode("utf-8"))
        self.assertEqual("JQ==", Base64.encodeBase640([37]).decode("utf-8"))
        self.assertEqual("Jg==", Base64.encodeBase640([38]).decode("utf-8"))
        self.assertEqual("Jw==", Base64.encodeBase640([39]).decode("utf-8"))
        self.assertEqual("KA==", Base64.encodeBase640([40]).decode("utf-8"))
        self.assertEqual("KQ==", Base64.encodeBase640([41]).decode("utf-8"))
        self.assertEqual("Kg==", Base64.encodeBase640([42]).decode("utf-8"))
        self.assertEqual("Kw==", Base64.encodeBase640([43]).decode("utf-8"))
        self.assertEqual("LA==", Base64.encodeBase640([44]).decode("utf-8"))
        self.assertEqual("LQ==", Base64.encodeBase640([45]).decode("utf-8"))
        self.assertEqual("Lg==", Base64.encodeBase640([46]).decode("utf-8"))
        self.assertEqual("Lw==", Base64.encodeBase640([47]).decode("utf-8"))
        self.assertEqual("MA==", Base64.encodeBase640([48]).decode("utf-8"))
        self.assertEqual("MQ==", Base64.encodeBase640([49]).decode("utf-8"))
        self.assertEqual("Mg==", Base64.encodeBase640([50]).decode("utf-8"))
        self.assertEqual("Mw==", Base64.encodeBase640([51]).decode("utf-8"))
        self.assertEqual("NA==", Base64.encodeBase640([52]).decode("utf-8"))
        self.assertEqual("NQ==", Base64.encodeBase640([53]).decode("utf-8"))
        self.assertEqual("Ng==", Base64.encodeBase640([54]).decode("utf-8"))
        self.assertEqual("Nw==", Base64.encodeBase640([55]).decode("utf-8"))
        self.assertEqual("OA==", Base64.encodeBase640([56]).decode("utf-8"))
        self.assertEqual("OQ==", Base64.encodeBase640([57]).decode("utf-8"))
        self.assertEqual("Og==", Base64.encodeBase640([58]).decode("utf-8"))
        self.assertEqual("Ow==", Base64.encodeBase640([59]).decode("utf-8"))
        self.assertEqual("PA==", Base64.encodeBase640([60]).decode("utf-8"))
        self.assertEqual("PQ==", Base64.encodeBase640([61]).decode("utf-8"))
        self.assertEqual("Pg==", Base64.encodeBase640([62]).decode("utf-8"))
        self.assertEqual("Pw==", Base64.encodeBase640([63]).decode("utf-8"))
        self.assertEqual("QA==", Base64.encodeBase640([64]).decode("utf-8"))
        self.assertEqual("QQ==", Base64.encodeBase640([65]).decode("utf-8"))
        self.assertEqual("Qg==", Base64.encodeBase640([66]).decode("utf-8"))
        self.assertEqual("Qw==", Base64.encodeBase640([67]).decode("utf-8"))
        self.assertEqual("RA==", Base64.encodeBase640([68]).decode("utf-8"))
        self.assertEqual("RQ==", Base64.encodeBase640([69]).decode("utf-8"))
        self.assertEqual("Rg==", Base64.encodeBase640([70]).decode("utf-8"))
        self.assertEqual("Rw==", Base64.encodeBase640([71]).decode("utf-8"))
        self.assertEqual("SA==", Base64.encodeBase640([72]).decode("utf-8"))
        self.assertEqual("SQ==", Base64.encodeBase640([73]).decode("utf-8"))
        self.assertEqual("Sg==", Base64.encodeBase640([74]).decode("utf-8"))
        self.assertEqual("Sw==", Base64.encodeBase640([75]).decode("utf-8"))
        self.assertEqual("TA==", Base64.encodeBase640([76]).decode("utf-8"))
        self.assertEqual("TQ==", Base64.encodeBase640([77]).decode("utf-8"))
        self.assertEqual("Tg==", Base64.encodeBase640([78]).decode("utf-8"))
        self.assertEqual("Tw==", Base64.encodeBase640([79]).decode("utf-8"))
        self.assertEqual("UA==", Base64.encodeBase640([80]).decode("utf-8"))
        self.assertEqual("UQ==", Base64.encodeBase640([81]).decode("utf-8"))
        self.assertEqual("Ug==", Base64.encodeBase640([82]).decode("utf-8"))
        self.assertEqual("Uw==", Base64.encodeBase640([83]).decode("utf-8"))
        self.assertEqual("VA==", Base64.encodeBase640([84]).decode("utf-8"))
        self.assertEqual("VQ==", Base64.encodeBase640([85]).decode("utf-8"))
        self.assertEqual("Vg==", Base64.encodeBase640([86]).decode("utf-8"))
        self.assertEqual("Vw==", Base64.encodeBase640([87]).decode("utf-8"))
        self.assertEqual("WA==", Base64.encodeBase640([88]).decode("utf-8"))
        self.assertEqual("WQ==", Base64.encodeBase640([89]).decode("utf-8"))
        self.assertEqual("Wg==", Base64.encodeBase640([90]).decode("utf-8"))
        self.assertEqual("Ww==", Base64.encodeBase640([91]).decode("utf-8"))
        self.assertEqual("XA==", Base64.encodeBase640([92]).decode("utf-8"))
        self.assertEqual("XQ==", Base64.encodeBase640([93]).decode("utf-8"))
        self.assertEqual("Xg==", Base64.encodeBase640([94]).decode("utf-8"))
        self.assertEqual("Xw==", Base64.encodeBase640([95]).decode("utf-8"))
        self.assertEqual("YA==", Base64.encodeBase640([96]).decode("utf-8"))
        self.assertEqual("YQ==", Base64.encodeBase640([97]).decode("utf-8"))
        self.assertEqual("Yg==", Base64.encodeBase640([98]).decode("utf-8"))
        self.assertEqual("Yw==", Base64.encodeBase640([99]).decode("utf-8"))
        self.assertEqual("ZA==", Base64.encodeBase640([100]).decode("utf-8"))
        self.assertEqual("ZQ==", Base64.encodeBase640([101]).decode("utf-8"))
        self.assertEqual("Zg==", Base64.encodeBase640([102]).decode("utf-8"))
        self.assertEqual("Zw==", Base64.encodeBase640([103]).decode("utf-8"))
        self.assertEqual("aA==", Base64.encodeBase640([104]).decode("utf-8"))

        for i in range(-128, 128):
            test = [i & 0xFF]  # Convert to unsigned byte
            self.assertEqual(test, Base64.decodeBase640(Base64.encodeBase640(test)))

    def testSingletons_test0_decomposed(self) -> None:
        self.assertEqual("AA==", Base64.encodeBase640([0]).decode("utf-8"))
        self.assertEqual("AQ==", Base64.encodeBase640([1]).decode("utf-8"))
        self.assertEqual("Ag==", Base64.encodeBase640([2]).decode("utf-8"))
        self.assertEqual("Aw==", Base64.encodeBase640([3]).decode("utf-8"))
        self.assertEqual("BA==", Base64.encodeBase640([4]).decode("utf-8"))
        self.assertEqual("BQ==", Base64.encodeBase640([5]).decode("utf-8"))
        self.assertEqual("Bg==", Base64.encodeBase640([6]).decode("utf-8"))
        self.assertEqual("Bw==", Base64.encodeBase640([7]).decode("utf-8"))
        self.assertEqual("CA==", Base64.encodeBase640([8]).decode("utf-8"))
        self.assertEqual("CQ==", Base64.encodeBase640([9]).decode("utf-8"))
        self.assertEqual("Cg==", Base64.encodeBase640([10]).decode("utf-8"))
        self.assertEqual("Cw==", Base64.encodeBase640([11]).decode("utf-8"))
        self.assertEqual("DA==", Base64.encodeBase640([12]).decode("utf-8"))
        self.assertEqual("DQ==", Base64.encodeBase640([13]).decode("utf-8"))
        self.assertEqual("Dg==", Base64.encodeBase640([14]).decode("utf-8"))
        self.assertEqual("Dw==", Base64.encodeBase640([15]).decode("utf-8"))
        self.assertEqual("EA==", Base64.encodeBase640([16]).decode("utf-8"))
        self.assertEqual("EQ==", Base64.encodeBase640([17]).decode("utf-8"))
        self.assertEqual("Eg==", Base64.encodeBase640([18]).decode("utf-8"))
        self.assertEqual("Ew==", Base64.encodeBase640([19]).decode("utf-8"))
        self.assertEqual("FA==", Base64.encodeBase640([20]).decode("utf-8"))
        self.assertEqual("FQ==", Base64.encodeBase640([21]).decode("utf-8"))
        self.assertEqual("Fg==", Base64.encodeBase640([22]).decode("utf-8"))
        self.assertEqual("Fw==", Base64.encodeBase640([23]).decode("utf-8"))
        self.assertEqual("GA==", Base64.encodeBase640([24]).decode("utf-8"))
        self.assertEqual("GQ==", Base64.encodeBase640([25]).decode("utf-8"))
        self.assertEqual("Gg==", Base64.encodeBase640([26]).decode("utf-8"))
        self.assertEqual("Gw==", Base64.encodeBase640([27]).decode("utf-8"))
        self.assertEqual("HA==", Base64.encodeBase640([28]).decode("utf-8"))
        self.assertEqual("HQ==", Base64.encodeBase640([29]).decode("utf-8"))
        self.assertEqual("Hg==", Base64.encodeBase640([30]).decode("utf-8"))
        self.assertEqual("Hw==", Base64.encodeBase640([31]).decode("utf-8"))
        self.assertEqual("IA==", Base64.encodeBase640([32]).decode("utf-8"))
        self.assertEqual("IQ==", Base64.encodeBase640([33]).decode("utf-8"))
        self.assertEqual("Ig==", Base64.encodeBase640([34]).decode("utf-8"))
        self.assertEqual("Iw==", Base64.encodeBase640([35]).decode("utf-8"))
        self.assertEqual("JA==", Base64.encodeBase640([36]).decode("utf-8"))
        self.assertEqual("JQ==", Base64.encodeBase640([37]).decode("utf-8"))
        self.assertEqual("Jg==", Base64.encodeBase640([38]).decode("utf-8"))
        self.assertEqual("Jw==", Base64.encodeBase640([39]).decode("utf-8"))
        self.assertEqual("KA==", Base64.encodeBase640([40]).decode("utf-8"))
        self.assertEqual("KQ==", Base64.encodeBase640([41]).decode("utf-8"))
        self.assertEqual("Kg==", Base64.encodeBase640([42]).decode("utf-8"))
        self.assertEqual("Kw==", Base64.encodeBase640([43]).decode("utf-8"))
        self.assertEqual("LA==", Base64.encodeBase640([44]).decode("utf-8"))
        self.assertEqual("LQ==", Base64.encodeBase640([45]).decode("utf-8"))
        self.assertEqual("Lg==", Base64.encodeBase640([46]).decode("utf-8"))
        self.assertEqual("Lw==", Base64.encodeBase640([47]).decode("utf-8"))
        self.assertEqual("MA==", Base64.encodeBase640([48]).decode("utf-8"))
        self.assertEqual("MQ==", Base64.encodeBase640([49]).decode("utf-8"))
        self.assertEqual("Mg==", Base64.encodeBase640([50]).decode("utf-8"))
        self.assertEqual("Mw==", Base64.encodeBase640([51]).decode("utf-8"))
        self.assertEqual("NA==", Base64.encodeBase640([52]).decode("utf-8"))
        self.assertEqual("NQ==", Base64.encodeBase640([53]).decode("utf-8"))
        self.assertEqual("Ng==", Base64.encodeBase640([54]).decode("utf-8"))
        self.assertEqual("Nw==", Base64.encodeBase640([55]).decode("utf-8"))
        self.assertEqual("OA==", Base64.encodeBase640([56]).decode("utf-8"))
        self.assertEqual("OQ==", Base64.encodeBase640([57]).decode("utf-8"))
        self.assertEqual("Og==", Base64.encodeBase640([58]).decode("utf-8"))
        self.assertEqual("Ow==", Base64.encodeBase640([59]).decode("utf-8"))
        self.assertEqual("PA==", Base64.encodeBase640([60]).decode("utf-8"))
        self.assertEqual("PQ==", Base64.encodeBase640([61]).decode("utf-8"))
        self.assertEqual("Pg==", Base64.encodeBase640([62]).decode("utf-8"))
        self.assertEqual("Pw==", Base64.encodeBase640([63]).decode("utf-8"))
        self.assertEqual("QA==", Base64.encodeBase640([64]).decode("utf-8"))
        self.assertEqual("QQ==", Base64.encodeBase640([65]).decode("utf-8"))
        self.assertEqual("Qg==", Base64.encodeBase640([66]).decode("utf-8"))
        self.assertEqual("Qw==", Base64.encodeBase640([67]).decode("utf-8"))
        self.assertEqual("RA==", Base64.encodeBase640([68]).decode("utf-8"))
        self.assertEqual("RQ==", Base64.encodeBase640([69]).decode("utf-8"))
        self.assertEqual("Rg==", Base64.encodeBase640([70]).decode("utf-8"))
        self.assertEqual("Rw==", Base64.encodeBase640([71]).decode("utf-8"))
        self.assertEqual("SA==", Base64.encodeBase640([72]).decode("utf-8"))
        self.assertEqual("SQ==", Base64.encodeBase640([73]).decode("utf-8"))
        self.assertEqual("Sg==", Base64.encodeBase640([74]).decode("utf-8"))
        self.assertEqual("Sw==", Base64.encodeBase640([75]).decode("utf-8"))
        self.assertEqual("TA==", Base64.encodeBase640([76]).decode("utf-8"))
        self.assertEqual("TQ==", Base64.encodeBase640([77]).decode("utf-8"))
        self.assertEqual("Tg==", Base64.encodeBase640([78]).decode("utf-8"))
        self.assertEqual("Tw==", Base64.encodeBase640([79]).decode("utf-8"))
        self.assertEqual("UA==", Base64.encodeBase640([80]).decode("utf-8"))
        self.assertEqual("UQ==", Base64.encodeBase640([81]).decode("utf-8"))
        self.assertEqual("Ug==", Base64.encodeBase640([82]).decode("utf-8"))
        self.assertEqual("Uw==", Base64.encodeBase640([83]).decode("utf-8"))
        self.assertEqual("VA==", Base64.encodeBase640([84]).decode("utf-8"))
        self.assertEqual("VQ==", Base64.encodeBase640([85]).decode("utf-8"))
        self.assertEqual("Vg==", Base64.encodeBase640([86]).decode("utf-8"))
        self.assertEqual("Vw==", Base64.encodeBase640([87]).decode("utf-8"))
        self.assertEqual("WA==", Base64.encodeBase640([88]).decode("utf-8"))
        self.assertEqual("WQ==", Base64.encodeBase640([89]).decode("utf-8"))
        self.assertEqual("Wg==", Base64.encodeBase640([90]).decode("utf-8"))
        self.assertEqual("Ww==", Base64.encodeBase640([91]).decode("utf-8"))
        self.assertEqual("XA==", Base64.encodeBase640([92]).decode("utf-8"))
        self.assertEqual("XQ==", Base64.encodeBase640([93]).decode("utf-8"))
        self.assertEqual("Xg==", Base64.encodeBase640([94]).decode("utf-8"))
        self.assertEqual("Xw==", Base64.encodeBase640([95]).decode("utf-8"))
        self.assertEqual("YA==", Base64.encodeBase640([96]).decode("utf-8"))
        self.assertEqual("YQ==", Base64.encodeBase640([97]).decode("utf-8"))
        self.assertEqual("Yg==", Base64.encodeBase640([98]).decode("utf-8"))
        self.assertEqual("Yw==", Base64.encodeBase640([99]).decode("utf-8"))
        self.assertEqual("ZA==", Base64.encodeBase640([100]).decode("utf-8"))
        self.assertEqual("ZQ==", Base64.encodeBase640([101]).decode("utf-8"))
        self.assertEqual("Zg==", Base64.encodeBase640([102]).decode("utf-8"))
        self.assertEqual("Zw==", Base64.encodeBase640([103]).decode("utf-8"))
        self.assertEqual("aA==", Base64.encodeBase640([104]).decode("utf-8"))

    def testRfc4648Section10EncodeDecode_test0_decomposed(self) -> None:
        self.__testEncodeDecode("")
        self.__testEncodeDecode("f")
        self.__testEncodeDecode("fo")
        self.__testEncodeDecode("foo")
        self.__testEncodeDecode("foob")
        self.__testEncodeDecode("fooba")
        self.__testEncodeDecode("foobar")

    def testRfc4648Section10DecodeEncode_test0_decomposed(self) -> None:
        self.__testDecodeEncode("")
        self.__testDecodeEncode("Zg==")
        self.__testDecodeEncode("Zm8=")
        self.__testDecodeEncode("Zm9v")
        self.__testDecodeEncode("Zm9vYg==")
        self.__testDecodeEncode("Zm9vYmE=")
        self.__testDecodeEncode("Zm9vYmFy")

    def testRfc4648Section10Encode_test13_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )
        self.assertEqual(
            "Zm9vYmE=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fooba"))
        )
        self.assertEqual(
            "Zm9vYmFy", Base64.encodeBase64String(StringUtils.getBytesUtf8("foobar"))
        )

    def testRfc4648Section10Encode_test12_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )
        self.assertEqual(
            "Zm9vYmE=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fooba"))
        )
        self.assertEqual(
            "Zm9vYmFy", Base64.encodeBase64String(StringUtils.getBytesUtf8("foobar"))
        )

    def testRfc4648Section10Encode_test11_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )
        self.assertEqual(
            "Zm9vYmE=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fooba"))
        )

    def testRfc4648Section10Encode_test10_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )

    def testRfc4648Section10Encode_test9_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )

    def testRfc4648Section10Encode_test8_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )

    def testRfc4648Section10Encode_test7_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )

    def testRfc4648Section10Encode_test6_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )

    def testRfc4648Section10Encode_test5_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )

    def testRfc4648Section10Encode_test4_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )

    def testRfc4648Section10Encode_test3_decomposed(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )

    def testRfc4648Section10Encode_test2_decomposed(self) -> None:
        StringUtils.getBytesUtf8("")
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        StringUtils.getBytesUtf8("f")

    def testRfc4648Section10Encode_test1_decomposed(self) -> None:
        result = StringUtils.getBytesUtf8("")
        encoded = Base64.encodeBase64String(result)
        self.assertEqual("", encoded, "Encoded string does not match expected value")

    def testRfc4648Section10Encode_test0_decomposed(self) -> None:
        StringUtils.getBytesUtf8("")

    def testRfc4648Section10DecodeWithCrLf_test14_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )
        self.assertEqual(
            "fooba",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)),
        )
        self.assertEqual(
            "foobar",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy" + CRLF)),
        )

    def testRfc4648Section10DecodeWithCrLf_test13_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)

        # Test decoding with CRLF
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )

        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )

        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )

        Base64.decodeBase641("Zm9v" + CRLF)
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )

        Base64.decodeBase641("Zm9vYg==" + CRLF)
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )

        Base64.decodeBase641("Zm9vYmE=" + CRLF)
        self.assertEqual(
            "fooba",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)),
        )

        Base64.decodeBase641("Zm9vYmFy" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test12_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )
        self.assertEqual(
            "fooba",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)),
        )

    def testRfc4648Section10DecodeWithCrLf_test11_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        Base64.decodeBase641("Zm9v" + CRLF)
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        Base64.decodeBase641("Zm9vYg==" + CRLF)
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )
        Base64.decodeBase641("Zm9vYmE=" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test10_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )

    def testRfc4648Section10DecodeWithCrLf_test9_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)

        # Test decoding with CRLF
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )

        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )

        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )

        Base64.decodeBase641("Zm9v" + CRLF)
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )

        Base64.decodeBase641("Zm9vYg==" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test8_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        Base64.decodeBase641("Zm9v" + CRLF)
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )

    def testRfc4648Section10DecodeWithCrLf_test7_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        Base64.decodeBase641("Zm9v" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test6_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        Base64.decodeBase641("Zm8=" + CRLF)
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )

    def testRfc4648Section10DecodeWithCrLf_test5_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        Base64.decodeBase641("Zm8=" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test4_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )

    def testRfc4648Section10DecodeWithCrLf_test3_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        Base64.decodeBase641("Zg==" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test2_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        decoded = Base64.decodeBase641("" + CRLF)
        self.assertEqual("", StringUtils.newStringUsAscii(decoded))

    def testRfc4648Section10DecodeWithCrLf_test1_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        Base64.decodeBase641("" + CRLF)

    def testRfc4648Section10DecodeWithCrLf_test0_decomposed(self) -> None:
        CRLF = StringUtils.newStringUsAscii(BaseNCodec.CHUNK_SEPARATOR)

    def testRfc4648Section10Decode_test13_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )
        Base64.decodeBase641("Zm9vYmE=")
        self.assertEqual(
            "fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE="))
        )
        Base64.decodeBase641("Zm9vYmFy")
        self.assertEqual(
            "foobar", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy"))
        )

    def testRfc4648Section10Decode_test12_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )
        Base64.decodeBase641("Zm9vYmE=")
        self.assertEqual(
            "fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE="))
        )
        Base64.decodeBase641("Zm9vYmFy")

    def testRfc4648Section10Decode_test11_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )
        Base64.decodeBase641("Zm9vYmE=")
        self.assertEqual(
            "fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE="))
        )

    def testRfc4648Section10Decode_test10_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )
        Base64.decodeBase641("Zm9vYmE=")

    def testRfc4648Section10Decode_test9_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )

    def testRfc4648Section10Decode_test8_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        Base64.decodeBase641("Zm9vYg==")

    def testRfc4648Section10Decode_test7_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )

    def testRfc4648Section10Decode_test6_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        Base64.decodeBase641("Zm9v")

    def testRfc4648Section10Decode_test5_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )

    def testRfc4648Section10Decode_test4_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        Base64.decodeBase641("Zm8=")

    def testRfc4648Section10Decode_test3_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )

    def testRfc4648Section10Decode_test2_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        Base64.decodeBase641("Zg==")

    def testRfc4648Section10Decode_test1_decomposed(self) -> None:
        Base64.decodeBase641("")
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))

    def testRfc4648Section10Decode_test0_decomposed(self) -> None:
        Base64.decodeBase641("")

    def testRfc1421Section6Dot8ChunkSizeDefinition_test0_decomposed(self) -> None:
        self.assertEqual(64, BaseNCodec.PEM_CHUNK_SIZE)

    def testRfc2045Section6Dot8ChunkSizeDefinition_test0_decomposed(self) -> None:
        self.assertEqual(76, BaseNCodec.MIME_CHUNK_SIZE)

    def testRfc2045Section2Dot1CrLfDefinition_test0_decomposed(self) -> None:
        self.assertEqual([13, 10], Base64.CHUNK_SEPARATOR)

    def testPairs_test1_decomposed(self) -> None:
        self.assertEqual("AAA=", Base64.encodeBase640([0, 0]).decode("utf-8"))
        for i in range(-128, 128):  # range is inclusive of -128 and exclusive of 128
            test = [i & 0xFF, i & 0xFF]  # Simulate byte array with masking to 8 bits
            self.assertEqual(
                test,
                list(Base64.decodeBase640(Base64.encodeBase640(test))),
                f"Failed for input: {test}",
            )

    def testPairs_test0_decomposed(self) -> None:
        self.assertEqual("AAA=", Base64.encodeBase640([0, 0]).decode("ascii"))

    def testObjectEncode_test2_decomposed(self) -> None:
        b64 = Base64.Base645()
        input_string = "Hello World"
        input_bytes = input_string.encode(self.__CHARSET_UTF8)
        expected_output = "SGVsbG8gV29ybGQ="
        actual_output = b64.encode0(input_bytes).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

    def testObjectEncode_test1_decomposed(self) -> None:
        b64 = Base64.Base645()
        "Hello World".encode(self.__CHARSET_UTF8)

    def testObjectEncode_test0_decomposed(self) -> None:
        b64 = Base64.Base645()

    def testObjectEncodeWithValidParameter_test4_decomposed(self) -> None:
        original = "Hello World!"
        orig_obj = original.encode(
            self.__CHARSET_UTF8
        )  # Convert string to bytes using UTF-8
        b64 = Base64.Base645()  # Create an instance of Base64
        o_encoded = b64.encode3(orig_obj)  # Encode the byte array
        b_array = Base64.decodeBase640(o_encoded)  # Decode the encoded byte array
        dest = b_array.decode(
            self.__CHARSET_UTF8
        )  # Convert the decoded byte array back to a string
        self.assertEqual(
            "dest string does not equal original", original, dest
        )  # Assert equality

    def testObjectEncodeWithValidParameter_test3_decomposed(self) -> None:
        original = "Hello World!"
        orig_obj = original.encode(
            self.__CHARSET_UTF8
        )  # Equivalent to getBytes(CHARSET_UTF8) in Java
        b64 = Base64.Base645()
        o_encoded = b64.encode3(orig_obj)
        b_array = Base64.decodeBase640(o_encoded)

    def testObjectEncodeWithValidParameter_test2_decomposed(self) -> None:
        original = "Hello World!"
        orig_obj = original.encode(
            self.__CHARSET_UTF8
        )  # Convert string to bytes using UTF-8
        b64 = Base64.Base645()  # Create an instance of Base64
        o_encoded = b64.encode3(orig_obj)  # Encode the byte array

    def testObjectEncodeWithValidParameter_test1_decomposed(self) -> None:
        original = "Hello World!"
        orig_obj = original.encode(self.__CHARSET_UTF8)
        b64 = Base64.Base645()

    def testObjectEncodeWithValidParameter_test0_decomposed(self) -> None:
        original: str = "Hello World!"
        orig_obj: bytes = original.encode(self.__CHARSET_UTF8)

    def testObjectEncodeWithInvalidParameter_test1_decomposed(self) -> None:
        b64 = Base64.Base645()
        try:
            b64.encode3("Yadayadayada")
            pytest.fail(
                "encode(Object) didn't throw an exception when passed a String object"
            )
        except EncoderException:
            pass

    def testObjectEncodeWithInvalidParameter_test0_decomposed(self) -> None:
        b64 = Base64.Base645()

    def testObjectDecodeWithValidParameter_test4_decomposed(self) -> None:
        original = "Hello World!"
        original_bytes = original.encode(
            self.__CHARSET_UTF8
        )  # Convert string to bytes using UTF-8
        encoded_object = Base64.encodeBase640(
            original_bytes
        )  # Encode the bytes using Base64
        b64 = Base64.Base645()  # Create a Base64 instance
        decoded_object = b64.decode2(encoded_object)  # Decode the Base64-encoded object
        decoded_bytes = bytes(decoded_object)  # Cast the decoded object to bytes
        dest = decoded_bytes.decode(
            self.__CHARSET_UTF8
        )  # Convert bytes back to string using UTF-8
        self.assertEqual(
            "dest string does not equal original", original, dest
        )  # Assert equality

    def testObjectDecodeWithValidParameter_test3_decomposed(self) -> None:
        original = "Hello World!"
        original_bytes = original.encode(self.__CHARSET_UTF8)
        encoded_object = Base64.encodeBase640(original_bytes)
        b64 = Base64.Base645()
        decoded_object = b64.decode2(encoded_object)

    def testObjectDecodeWithValidParameter_test2_decomposed(self) -> None:
        original = "Hello World!"
        original_bytes = original.encode(self.__CHARSET_UTF8)
        o = Base64.encodeBase640(original_bytes)
        b64 = Base64.Base645()

    def testObjectDecodeWithValidParameter_test1_decomposed(self) -> None:
        original = "Hello World!"
        original_bytes = original.encode(self.__CHARSET_UTF8)
        encoded_object = Base64.encodeBase640(original_bytes)

    def testObjectDecodeWithValidParameter_test0_decomposed(self) -> None:
        original: str = "Hello World!"
        original_bytes: bytes = original.encode(self.__CHARSET_UTF8)

    def testObjectDecodeWithInvalidParameter_test1_decomposed(self) -> None:
        b64 = Base64.Base645()
        with pytest.raises(
            DecoderException,
            match="Parameter supplied to Base-N decode is not a byte[] or a String",
        ):
            b64.decode2(5)

    def testObjectDecodeWithInvalidParameter_test0_decomposed(self) -> None:
        b64 = Base64.Base645()

    def testNonBase64Test_test1_decomposed(self) -> None:
        b_array = [ord("%")]
        self.assertFalse(
            Base64.isBase641(b_array),
            "Invalid Base64 array was incorrectly validated as "
            "an array of Base64 encoded data",
        )
        try:
            b64 = Base64.Base645()
            result = b64.decode0(b_array)

            self.assertEqual(
                0,
                len(result),
                "The result should be empty as the test encoded content did "
                "not contain any valid base 64 characters",
            )
        except Exception as e:
            self.fail(
                "Exception was thrown when trying to decode "
                "invalid base64 encoded data - RFC 2045 requires that all "
                "non base64 characters be discarded, an exception should not "
                "have been thrown"
            )

    def testNonBase64Test_test0_decomposed(self) -> None:
        b_array = [ord("%")]
        self.assertFalse(
            Base64.isBase641(b_array),
            "Invalid Base64 array was incorrectly validated as an array of Base64 encoded data",
        )

    def testKnownEncodings_test13_decomposed(self) -> None:
        self.assertEqual(
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==",
            Base64.encodeBase640(
                "The quick brown fox jumped over the lazy dogs.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            + "bGFoIGJsYWg=\r\n",
            Base64.encodeBase64Chunked(
                "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==",
            Base64.encodeBase640(
                "It was the best of times, it was the worst of times.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==",
            Base64.encodeBase640(
                "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==",
            Base64.encodeBase640(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=",
            Base64.encodeBase640(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "eHl6enkh",
            Base64.encodeBase640("xyzzy!".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )

    def testKnownEncodings_test12_decomposed(self) -> None:
        self.assertEqual(
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==",
            Base64.encodeBase640(
                "The quick brown fox jumped over the lazy dogs.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            + "bGFoIGJsYWg=\r\n",
            Base64.encodeBase64Chunked(
                "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==",
            Base64.encodeBase640(
                "It was the best of times, it was the worst of times.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==",
            Base64.encodeBase640(
                "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==",
            Base64.encodeBase640(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=",
            Base64.encodeBase640(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownEncodings_test11_decomposed(self) -> None:
        self.assertEqual(
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==",
            Base64.encodeBase640(
                "The quick brown fox jumped over the lazy dogs.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            + "bGFoIGJsYWg=\r\n",
            Base64.encodeBase64Chunked(
                "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==",
            Base64.encodeBase640(
                "It was the best of times, it was the worst of times.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==",
            Base64.encodeBase640(
                "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==",
            Base64.encodeBase640(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

        self.assertEqual(
            "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=",
            Base64.encodeBase640(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8)
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownEncodings_test10_decomposed(self) -> None:
        # Test case 1
        input_data = "The quick brown fox jumped over the lazy dogs.".encode(
            self.__CHARSET_UTF8
        )
        expected_output = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output = Base64.encodeBase640(input_data).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 2
        input_data = "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah".encode(
            self.__CHARSET_UTF8
        )
        expected_output = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            + "bGFoIGJsYWg=\r\n"
        )
        actual_output = Base64.encodeBase64Chunked(input_data).decode(
            self.__CHARSET_UTF8
        )
        self.assertEqual(expected_output, actual_output)

        # Test case 3
        input_data = "It was the best of times, it was the worst of times.".encode(
            self.__CHARSET_UTF8
        )
        expected_output = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual_output = Base64.encodeBase640(input_data).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 4
        input_data = "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
        expected_output = "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
        actual_output = Base64.encodeBase640(input_data).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 5
        input_data = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
            self.__CHARSET_UTF8
        )
        expected_output = (
            "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg=="
        )
        actual_output = Base64.encodeBase640(input_data).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 6
        input_data = "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8)
        # No assertion provided in the original Java code for this case

    def testKnownEncodings_test9_decomposed(self) -> None:
        # Test case 1
        input_str = "The quick brown fox jumped over the lazy dogs."
        expected_output = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output = Base64.encodeBase640(
            input_str.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 2
        input_str = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        )
        expected_output = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual_output = Base64.encodeBase64Chunked(
            input_str.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 3
        input_str = "It was the best of times, it was the worst of times."
        expected_output = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual_output = Base64.encodeBase640(
            input_str.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 4
        input_str = "http://jakarta.apache.org/commmons"
        expected_output = "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
        actual_output = Base64.encodeBase640(
            input_str.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

        # Test case 5
        input_str = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        expected_output = (
            "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg=="
        )
        actual_output = Base64.encodeBase640(
            input_str.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output, actual_output)

    def testKnownEncodings_test8_decomposed(self) -> None:
        # Test case 1
        input_str1 = "The quick brown fox jumped over the lazy dogs."
        expected_output1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output1 = Base64.encodeBase640(
            input_str1.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output1, actual_output1)

        # Test case 2
        input_str2 = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        )
        expected_output2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual_output2 = Base64.encodeBase64Chunked(
            input_str2.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output2, actual_output2)

        # Test case 3
        input_str3 = "It was the best of times, it was the worst of times."
        expected_output3 = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual_output3 = Base64.encodeBase640(
            input_str3.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output3, actual_output3)

        # Test case 4
        input_str4 = "http://jakarta.apache.org/commmons"
        expected_output4 = "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
        actual_output4 = Base64.encodeBase640(
            input_str4.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output4, actual_output4)

        # Test case 5
        input_str5 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        input_str5.encode(
            self.__CHARSET_UTF8
        )  # This line is just to mimic the Java code, no assertion needed

    def testKnownEncodings_test7_decomposed(self) -> None:
        # Test case 1
        input_str1 = "The quick brown fox jumped over the lazy dogs."
        expected_output1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output1 = Base64.encodeBase640(
            input_str1.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output1, actual_output1)

        # Test case 2
        input_str2 = "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        expected_output2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            + "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            + "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            + "bGFoIGJsYWg=\r\n"
        )
        actual_output2 = Base64.encodeBase64Chunked(
            input_str2.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output2, actual_output2)

        # Test case 3
        input_str3 = "It was the best of times, it was the worst of times."
        expected_output3 = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual_output3 = Base64.encodeBase640(
            input_str3.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output3, actual_output3)

        # Test case 4
        input_str4 = "http://jakarta.apache.org/commmons"
        expected_output4 = "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
        actual_output4 = Base64.encodeBase640(
            input_str4.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output4, actual_output4)

    def testKnownEncodings_test6_decomposed(self) -> None:
        # Test case 1
        input1 = "The quick brown fox jumped over the lazy dogs.".encode(
            self.__CHARSET_UTF8
        )
        expected1 = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        actual1 = Base64.encodeBase640(input1).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected1, actual1)

        # Test case 2
        input2 = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        ).encode(self.__CHARSET_UTF8)
        expected2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual2 = Base64.encodeBase64Chunked(input2).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected2, actual2)

        # Test case 3
        input3 = "It was the best of times, it was the worst of times.".encode(
            self.__CHARSET_UTF8
        )
        expected3 = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual3 = Base64.encodeBase640(input3).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected3, actual3)

        # Test case 4
        input4 = "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
        # No assertion is made for this input in the original Java code

    def testKnownEncodings_test5_decomposed(self) -> None:
        # Test case 1
        input1 = "The quick brown fox jumped over the lazy dogs.".encode(
            self.__CHARSET_UTF8
        )
        expected1 = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        actual1 = Base64.encodeBase640(input1).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected1, actual1)

        # Test case 2
        input2 = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        ).encode(self.__CHARSET_UTF8)
        expected2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual2 = Base64.encodeBase64Chunked(input2).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected2, actual2)

        # Test case 3
        input3 = "It was the best of times, it was the worst of times.".encode(
            self.__CHARSET_UTF8
        )
        expected3 = (
            "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        actual3 = Base64.encodeBase640(input3).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected3, actual3)

    def testKnownEncodings_test4_decomposed(self) -> None:
        # Test case 1
        input_string1 = "The quick brown fox jumped over the lazy dogs."
        expected_output1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output1 = Base64.encodeBase640(
            input_string1.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output1, actual_output1)

        # Test case 2
        input_string2 = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        )
        expected_output2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual_output2 = Base64.encodeBase64Chunked(
            input_string2.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(expected_output2, actual_output2)

        # Test case 3
        input_string3 = "It was the best of times, it was the worst of times."
        input_string3.encode(
            self.__CHARSET_UTF8
        )  # This line doesn't perform any assertion or encoding, so it's effectively a no-op.

    def testKnownEncodings_test3_decomposed(self) -> None:
        # Test case 1
        input_string1 = "The quick brown fox jumped over the lazy dogs."
        expected_output1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        actual_output1 = Base64.encodeBase640(
            input_string1.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(
            expected_output1,
            actual_output1,
            "Test case 1 failed: Encoded output does not match expected output.",
        )

        # Test case 2
        input_string2 = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        )
        expected_output2 = (
            "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJs\r\n"
            "YWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFo\r\n"
            "IGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\r\n"
            "bGFoIGJsYWg=\r\n"
        )
        actual_output2 = Base64.encodeBase64Chunked(
            input_string2.encode(self.__CHARSET_UTF8)
        ).decode(self.__CHARSET_UTF8)
        self.assertEqual(
            expected_output2,
            actual_output2,
            "Test case 2 failed: Encoded output does not match expected output.",
        )

    def testKnownEncodings_test2_decomposed(self) -> None:
        input_string = "The quick brown fox jumped over the lazy dogs."
        input_bytes = input_string.encode(self.__CHARSET_UTF8)

        # Encoding the input string to Base64
        encoded_string = Base64.encodeBase640(input_bytes).decode(self.__CHARSET_UTF8)

        # Assert the Base64 encoded string matches the expected value
        self.assertEqual(
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==",
            encoded_string,
        )

        # Another input string (not used further in the test)
        long_string = (
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah "
            "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah"
        )
        long_string_bytes = long_string.encode(self.__CHARSET_UTF8)

    def testKnownEncodings_test1_decomposed(self) -> None:
        input_string = "The quick brown fox jumped over the lazy dogs."
        expected_output = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )

        # Convert the input string to bytes using UTF-8 encoding
        input_bytes = input_string.encode(self.__CHARSET_UTF8)

        # Encode the bytes using Base64
        actual_output = Base64.encodeBase640(input_bytes).decode(self.__CHARSET_UTF8)

        # Assert that the encoded output matches the expected output
        self.assertEqual(expected_output, actual_output)

    def testKnownEncodings_test0_decomposed(self) -> None:
        b"The quick brown fox jumped over the lazy dogs.".decode(
            self.__CHARSET_UTF8
        ).encode(self.__CHARSET_UTF8)

    def testKnownDecodings_test11_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
            Base64.decodeBase640(
                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "xyzzy!",
            Base64.decodeBase640("eHl6enkh".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )

    def testKnownDecodings_test10_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
            Base64.decodeBase640(
                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test9_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
            Base64.decodeBase640(
                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test8_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test7_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test6_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test5_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test4_decomposed(self) -> None:
        # Test case 1
        encoded1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                self.__CHARSET_UTF8
            )
        )
        decoded1 = Base64.decodeBase640(encoded1)
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            decoded1.decode(self.__CHARSET_UTF8),
        )

        # Test case 2
        encoded2 = "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
            self.__CHARSET_UTF8
        )
        decoded2 = Base64.decodeBase640(encoded2)
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            decoded2.decode(self.__CHARSET_UTF8),
        )

        # Test case 3 (no assertion, just encoding)
        encoded3 = "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
            self.__CHARSET_UTF8
        )

    def testKnownDecodings_test3_decomposed(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8),
        )

    def testKnownDecodings_test2_decomposed(self) -> None:
        encoded_string1 = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                self.__CHARSET_UTF8
            )
        )
        decoded_string1 = Base64.decodeBase640(encoded_string1).decode(
            self.__CHARSET_UTF8
        )
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.", decoded_string1
        )

        encoded_string2 = "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
            self.__CHARSET_UTF8
        )
        # The second string is encoded but not decoded or asserted in the original Java code.

    def testKnownDecodings_test1_decomposed(self) -> None:
        encoded_string = (
            "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        expected_output = "The quick brown fox jumped over the lazy dogs."

        # Decode the Base64 encoded string
        decoded_bytes = Base64.decodeBase640(encoded_string.encode(self.__CHARSET_UTF8))
        decoded_string = decoded_bytes.decode(self.__CHARSET_UTF8)

        # Assert the decoded string matches the expected output
        self.assertEqual(expected_output, decoded_string)

    def testKnownDecodings_test0_decomposed(self) -> None:
        b64_string = "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        result = b64_string.encode(self.__CHARSET_UTF8)

    def testIsUrlSafe_test2_decomposed(self) -> None:
        base64_standard = Base64.Base644(False)
        base64_url_safe = Base64.Base644(True)
        self.assertFalse(base64_standard.isUrlSafe(), "Base64.isUrlSafe=false")
        self.assertTrue(base64_url_safe.isUrlSafe(), "Base64.isUrlSafe=true")
        white_space = [ord(" "), ord("\n"), ord("\r"), ord("\t")]
        self.assertTrue(
            Base64.isBase641(white_space), "Base64.isBase641(whiteSpace)=true"
        )

    def testIsUrlSafe_test1_decomposed(self) -> None:
        base64_standard = Base64.Base644(False)
        base64_url_safe = Base64.Base644(True)
        self.assertFalse(base64_standard.isUrlSafe(), "Base64.isUrlSafe=false")
        self.assertTrue(base64_url_safe.isUrlSafe(), "Base64.isUrlSafe=true")

    def testIsUrlSafe_test0_decomposed(self) -> None:
        base64_standard = Base64.Base644(False)
        base64_url_safe = Base64.Base644(True)

    def testIsArrayByteBase64_test0_decomposed(self) -> None:
        self.assertFalse(Base64.isBase641([-(2**7)]))  # -128 in Java
        self.assertFalse(Base64.isBase641([-125]))
        self.assertFalse(Base64.isBase641([-10]))
        self.assertFalse(Base64.isBase641([0]))
        self.assertFalse(Base64.isBase641([64, (2**7) - 1]))  # 127 in Java
        self.assertFalse(Base64.isBase641([(2**7) - 1]))  # 127 in Java
        self.assertTrue(Base64.isBase641([ord("A")]))
        self.assertFalse(Base64.isBase641([ord("A"), -(2**7)]))  # -128 in Java
        self.assertTrue(Base64.isBase641([ord("A"), ord("Z"), ord("a")]))
        self.assertTrue(Base64.isBase641([ord("/"), ord("="), ord("+")]))
        self.assertFalse(Base64.isBase641([ord("$")]))

    def testIgnoringNonBase64InDecode_test1_decomposed(self) -> None:
        input_data = "VGhlIH@$#$@%F1aWN@#@#@@rIGJyb3duIGZve\n\r\t%#%#%#%CBqd##$#$W1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
            self.__CHARSET_UTF8
        )
        expected_output = "The quick brown fox jumped over the lazy dogs."
        decoded_output = Base64.decodeBase640(input_data)
        self.assertEqual(
            expected_output,
            decoded_output.decode(self.__CHARSET_UTF8),
            "Decoded output does not match the expected output.",
        )

    def testIgnoringNonBase64InDecode_test0_decomposed(self) -> None:
        "VGhlIH@$#$@%F1aWN@#@#@@rIGJyb3duIGZve\n\r\t%#%#%#%CBqd##$#$W1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
            self.__CHARSET_UTF8
        )

    def testCodec112_test1_decomposed(self) -> None:
        in_data = [0]
        out_data = Base64.encodeBase640(in_data)
        Base64.encodeBase643(in_data, False, False, len(out_data))

    def testCodec112_test0_decomposed(self) -> None:
        in_data = [0]
        out_data = Base64.encodeBase640(in_data)

    def testEncodeOverMaxSize0_test0_decomposed(self) -> None:
        self.__testEncodeOverMaxSize1(-1)
        self.__testEncodeOverMaxSize1(0)
        self.__testEncodeOverMaxSize1(1)
        self.__testEncodeOverMaxSize1(2)

    def testEncodeDecodeSmall_test0_decomposed(self) -> None:
        for i in range(12):
            data = bytearray(i)  # Create a byte array of size i
            self.getRandom().nextBytes(data)  # Fill the byte array with random bytes
            enc = Base64.encodeBase640(data)  # Encode the data using Base64
            self.assertTrue(
                Base64.isBase641(enc), f'"{enc.decode()}" is not valid Base64 data.'
            )  # Check if the encoded data is valid Base64
            data2 = Base64.decodeBase640(enc)  # Decode the Base64 encoded data
            self.assertEqual(
                list(data),
                list(data2),
                f"{self.__toString(data)} does not equal {self.__toString(data2)}",
            )  # Assert that the original and decoded data are the same

    def testEncodeDecodeRandom_test0_decomposed(self) -> None:
        for i in range(1, 5):
            data = os.urandom(self.getRandom().randint(1, 10000))
            enc = Base64.encodeBase640(data)
            self.assertTrue(Base64.isBase641(enc), "Encoded data is not valid Base64")
            data2 = Base64.decodeBase640(enc)
            self.assertSequenceEqual(
                data, data2, "Decoded data does not match original data"
            )

    def testEmptyBase64_test7_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        result = Base64.encodeBase640(empty)
        self.assertEqual(0, len(result), "empty base64 encode")
        self.assertIsNone(Base64.encodeBase640(None), "empty base64 encode")

        base64_instance = Base64.Base645()
        result = base64_instance.encode1(empty, 0, 1)
        self.assertEqual(0, len(result), "empty base64 encode")

        base64_instance = Base64.Base645()
        self.assertIsNone(base64_instance.encode1(None, 0, 1), "empty base64 encode")

        empty = bytearray()  # Equivalent to new byte[0];
        result = Base64.decodeBase640(empty)
        self.assertEqual(0, len(result), "empty base64 decode")
        self.assertIsNone(Base64.decodeBase640(None), "empty base64 encode")

    def testEmptyBase64_test6_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        result = Base64.encodeBase640(empty)
        self.assertEqual(
            len(result), 0, "empty base64 encode"
        )  # Assert result length is 0
        self.assertIsNone(
            Base64.encodeBase640(None), "empty base64 encode"
        )  # Assert None input returns None

        base64_instance = Base64.Base645()  # Create an instance of Base64.Base645()
        result = base64_instance.encode1(empty, 0, 0)  # Encode with Base64.Base645()
        self.assertEqual(
            len(result), 0, "empty base64 encode"
        )  # Assert result length is 0

        self.assertIsNone(
            base64_instance.encode1(None, 0, 0), "empty base64 encode"
        )  # Assert None input returns None

        empty = bytearray()  # Reinitialize empty as a new bytearray
        result = Base64.decodeBase640(empty)  # Decode the empty bytearray
        self.assertEqual(
            len(result), 0, "empty base64 decode"
        )  # Assert result length is 0

    def testEmptyBase64_test5_decomposed(self) -> None:
        empty = b""  # Empty byte array
        result = Base64.encodeBase640(empty)
        self.assertEqual(len(result), 0, "empty base64 encode")
        self.assertIsNone(Base64.encodeBase640(None), "empty base64 encode")

        base64_instance = Base64.Base645()
        result = base64_instance.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty base64 encode")

        base64_instance = Base64.Base645()
        self.assertIsNone(base64_instance.encode1(None, 0, 1), "empty base64 encode")

    def testEmptyBase64_test4_decomposed(self) -> None:
        empty = b""  # Equivalent to byte[] empty = {};
        result = Base64.encodeBase640(empty)
        self.assertEqual(len(result), 0, "empty base64 encode")
        self.assertIsNone(Base64.encodeBase640(None), "empty base64 encode")

        # Simulate Base64.Base645() and its encode1 method
        base64_instance = Base64.Base645()
        result = base64_instance.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty base64 encode")

        # Call Base64.Base645() again to match the Java code
        Base64.Base645()

    def testEmptyBase64_test3_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        result = Base64.encodeBase640(empty)  # Call the static method encodeBase640
        self.assertEqual(
            len(result), 0, "empty base64 encode"
        )  # Assert result length is 0 with a message
        self.assertIsNone(
            Base64.encodeBase640(None), "empty base64 encode"
        )  # Assert None is returned for None input
        base64_instance = Base64.Base645()  # Create an instance using Base645
        result = base64_instance.encode1(
            empty, 0, 1
        )  # Call encode1 with empty array, offset 0, and length 1

    def testEmptyBase64_test2_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        result = Base64.encodeBase640(empty)  # Call the static method encodeBase640
        self.assertEqual(
            len(result), 0, "empty base64 encode"
        )  # Assert the length is 0 with a message
        self.assertIsNone(
            Base64.encodeBase640(None), "empty base64 encode"
        )  # Assert the result is None with a message
        Base64.Base645()  # Call the static method Base645

    def testEmptyBase64_test1_decomposed(self) -> None:
        empty = b""  # Empty byte array
        result = Base64.encodeBase640(empty)
        self.assertEqual(len(result), 0, "empty base64 encode")
        self.assertIsNone(Base64.encodeBase640(None), "empty base64 encode")

    def testEmptyBase64_test0_decomposed(self) -> None:
        empty = []
        result = Base64.encodeBase640(empty)

    def testDecodeWithWhitespace_test5_decomposed(self) -> None:
        orig = "I am a late night coder."
        encoded_array = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))
        intermediate = list(encoded_array.decode(self.__CHARSET_UTF8))
        intermediate.insert(2, " ")
        intermediate.insert(5, "\t")
        intermediate.insert(10, "\r")
        intermediate.insert(15, "\n")
        encoded_with_ws = "".join(intermediate).encode(self.__CHARSET_UTF8)
        decoded_with_ws = Base64.decodeBase640(encoded_with_ws)
        dest = decoded_with_ws.decode(self.__CHARSET_UTF8)
        self.assertEqual("Dest string doesn't equal the original", orig, dest)

    def testDecodeWithWhitespace_test4_decomposed(self) -> None:
        orig = "I am a late night coder."
        encoded_array = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))
        intermediate = list(encoded_array.decode(self.__CHARSET_UTF8))
        intermediate.insert(2, " ")
        intermediate.insert(5, "\t")
        intermediate.insert(10, "\r")
        intermediate.insert(15, "\n")
        encoded_with_ws = "".join(intermediate).encode(self.__CHARSET_UTF8)
        decoded_with_ws = Base64.decodeBase640(encoded_with_ws)

    def testDecodeWithWhitespace_test3_decomposed(self) -> None:
        orig = "I am a late night coder."
        encoded_array = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))
        intermediate = list(encoded_array.decode(self.__CHARSET_UTF8))
        intermediate.insert(2, " ")
        intermediate.insert(5, "\t")
        intermediate.insert(10, "\r")
        intermediate.insert(15, "\n")
        encoded_with_ws = "".join(intermediate).encode(self.__CHARSET_UTF8)

    def testDecodeWithWhitespace_test2_decomposed(self) -> None:
        orig = "I am a late night coder."
        encoded_array = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))
        intermediate = list(encoded_array.decode(self.__CHARSET_UTF8))
        intermediate.insert(2, " ")
        intermediate.insert(5, "\t")
        intermediate.insert(10, "\r")
        intermediate.insert(15, "\n")
        result = "".join(intermediate)

    def testDecodeWithWhitespace_test1_decomposed(self) -> None:
        orig = "I am a late night coder."
        encoded_array = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))

    def testDecodeWithWhitespace_test0_decomposed(self) -> None:
        orig: str = "I am a late night coder."
        orig_bytes: bytes = orig.encode(self.__CHARSET_UTF8)

    def testDecodePadOnlyChunked_test11_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("=\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("\n".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnlyChunked_test10_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("=\n".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnlyChunked_test9_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("=\n".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnlyChunked_test8_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnlyChunked_test7_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnlyChunked_test6_decomposed(self) -> None:
        data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(data)))

        data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual("", Base64.decodeBase640(data).decode(self.__CHARSET_UTF8))

        data = "===\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(data)))

        data = "==\n".encode(self.__CHARSET_UTF8)

    def testDecodePadOnlyChunked_test5_decomposed(self) -> None:
        input_data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(input_data)))

        input_data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(
            "", Base64.decodeBase640(input_data).decode(self.__CHARSET_UTF8)
        )

        input_data = "===\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(input_data)))

    def testDecodePadOnlyChunked_test4_decomposed(self) -> None:
        input_data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(input_data)))

        decoded_string = Base64.decodeBase640(input_data).decode(self.__CHARSET_UTF8)
        self.assertEqual("", decoded_string)

        input_data = "===\n".encode(self.__CHARSET_UTF8)

    def testDecodePadOnlyChunked_test3_decomposed(self) -> None:
        input_data = "====\n".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(input_data)))
        self.assertEqual(
            "", Base64.decodeBase640(input_data).decode(self.__CHARSET_UTF8)
        )

    def testDecodePadOnlyChunked_test2_decomposed(self) -> None:
        input_data = "====\n".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(input_data)
        self.assertEqual(0, len(decoded_data))
        input_data = "====\n".encode(self.__CHARSET_UTF8)

    def testDecodePadOnlyChunked_test1_decomposed(self) -> None:
        input_data = "====\n".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(input_data)
        self.assertEqual(
            0,
            len(decoded_data),
            "Decoded data length does not match expected length = 0",
        )

    def testDecodePadOnlyChunked_test0_decomposed(self) -> None:
        b"====\n".decode(self.__CHARSET_UTF8)

    def testDecodePadOnly_test11_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("=".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly_test10_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("=".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly_test9_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("=".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly_test8_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly_test7_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly_test6_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnly_test5_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )

    def testDecodePadOnly_test4_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )

    def testDecodePadOnly_test3_decomposed(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )

    def testDecodePadOnly_test2_decomposed(self) -> None:
        data = "====".encode(self.__CHARSET_UTF8)
        self.assertEqual(0, len(Base64.decodeBase640(data)))
        data = "====".encode(self.__CHARSET_UTF8)

    def testDecodePadOnly_test1_decomposed(self) -> None:
        data = "====".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(data)
        self.assertEqual(
            0,
            len(decoded_data),
            "Decoded data length does not match expected length = 0",
        )

    def testDecodePadOnly_test0_decomposed(self) -> None:
        b"====".decode(self.__CHARSET_UTF8)

    def testDecodePadMarkerIndex3_test3_decomposed(self) -> None:
        self.assertEqual(
            "AA",
            Base64.decodeBase640("QUE=".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            "AAA",
            Base64.decodeBase640("QUFB".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )

    def testDecodePadMarkerIndex3_test2_decomposed(self) -> None:
        base64_data = "QUE=".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(base64_data)
        self.assertEqual("AA", decoded_data.decode(self.__CHARSET_UTF8))
        "QUFB".encode(self.__CHARSET_UTF8)

    def testDecodePadMarkerIndex3_test1_decomposed(self) -> None:
        base64_data = "QUE=".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(base64_data)
        self.assertEqual(
            "AA",
            decoded_data.decode(self.__CHARSET_UTF8),
            "Decoded data does not match expected value",
        )

    def testDecodePadMarkerIndex3_test0_decomposed(self) -> None:
        "QUE=".encode(self.__CHARSET_UTF8)

    def testDecodePadMarkerIndex2_test1_decomposed(self) -> None:
        base64_data = "QQ==".encode(self.__CHARSET_UTF8)
        decoded_data = Base64.decodeBase640(base64_data)
        self.assertEqual(
            "A",
            decoded_data.decode(self.__CHARSET_UTF8),
            "Decoded data does not match expected value",
        )

    def testDecodePadMarkerIndex2_test0_decomposed(self) -> None:
        "QQ==".encode(self.__CHARSET_UTF8)

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test3_decomposed(self) -> None:
        base64 = Base64.Base641(64, [ord("\t")], True)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expected_result = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expected_result = expected_result.replace("=", "")
        expected_result = expected_result.replace("\n", "\t")
        expected_result = expected_result.replace("+", "-")
        expected_result = expected_result.replace("/", "_")
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual("new Base64(64, \\t, true)", result, expected_result)

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test2_decomposed(self) -> None:
        base64 = Base64.Base641(64, [ord("\t")], True)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expected_result = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expected_result = expected_result.replace("=", "")
        expected_result = expected_result.replace("\n", "\t")
        expected_result = expected_result.replace("+", "-")
        expected_result = expected_result.replace("/", "_")
        result = StringUtils.newStringUtf8(encoded)

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test1_decomposed(self) -> None:
        base64 = Base64.Base641(64, [ord("\t")], True)
        encoded = base64.encode0(BaseNTestData.DECODED)

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test0_decomposed(self) -> None:
        base64 = Base64.Base641(64, [ord("\t")], True)

    def testConstructor_Int_ByteArray_Boolean_test3_decomposed(self) -> None:
        base64 = Base64.Base641(65, [ord("\t")], False)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expected_result = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "\t")
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual("new Base64(65, \\t, false)", expected_result, result)

    def testConstructor_Int_ByteArray_Boolean_test2_decomposed(self) -> None:
        base64 = Base64.Base641(65, [ord("\t")], False)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expected_result = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expected_result = expected_result.replace("\n", "\t")
        result = StringUtils.newStringUtf8(encoded)

    def testConstructor_Int_ByteArray_Boolean_test1_decomposed(self) -> None:
        base64 = Base64.Base641(65, [ord("\t")], False)
        encoded = base64.encode0(BaseNTestData.DECODED)

    def testConstructor_Int_ByteArray_Boolean_test0_decomposed(self) -> None:
        base64 = Base64.Base641(65, [ord("\t")], False)

    def testConstructors_test3_decomposed(self) -> None:
        base64 = None
        base64 = Base64.Base645()
        base64 = Base64.Base643(-1)
        base64 = Base64.Base642(-1, bytearray())
        base64 = Base64.Base642(64, bytearray())

        with pytest.raises(ValueError):
            base64 = Base64.Base642(-1, bytearray(b"A"))  # TODO do we need to
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"A"))
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"="))
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base64 = Base64.Base642(64, bytearray(b"$"))

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"A$"))
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

        base64 = Base64.Base642(64, bytearray(b" \n\r\t$"))
        self.assertIsNotNone(base64)

    def testConstructors_test2_decomposed(self) -> None:
        base64 = None
        base64 = Base64.Base645()
        base64 = Base64.Base643(-1)
        base64 = Base64.Base642(-1, bytearray())
        base64 = Base64.Base642(64, bytearray())

        with pytest.raises(ValueError):
            base64 = Base64.Base642(-1, bytearray(b"A"))  # TODO do we need to
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"A"))
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"="))
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base64 = Base64.Base642(64, bytearray(b"$"))

        with pytest.raises(ValueError):
            base64 = Base64.Base642(64, bytearray(b"A$"))
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

        base64 = Base64.Base642(64, bytearray(b" \n\r\t$"))

    def testConstructors_test1_decomposed(self) -> None:
        base64 = Base64.Base645()
        base64 = Base64.Base643(-1)

    def testConstructors_test0_decomposed(self) -> None:
        base64 = Base64.Base645()

    def testCodeIntegerNull_test0_decomposed(self) -> None:
        try:
            Base64.encodeInteger(None)
            self.fail(
                "Exception not thrown when passing in None to encodeInteger(BigInteger)"
            )
        except ValueError:
            pass  # Expected exception
        except Exception as e:
            self.fail(
                "Incorrect Exception caught when passing in None to encodeInteger(BigInteger)"
            )

    def testCodeInteger4_test2_decomposed(self) -> None:
        encoded_int4 = (
            "ctA8YGxrtngg/zKVvqEOefnwmViFztcnPBYPlJsvh6yKI"
            "4iDm68fnp4Mi3RrJ6bZAygFrUIQLxLjV+OJtgJAEto0xAs+Mehuq1DkSFEpP3o"
            "DzCTOsrOiS1DwQe4oIb7zVk/9l7aPtJMHW0LVlMdwZNFNNJoqMcT2ZfCPrfvYv"
            "Q0="
        )
        big_int4 = int(
            "80624726256040348115552042320"
            "6968135001872753709424419772586693950232350200555646471175944"
            "519297087885987040810778908507262272892702303774422853675597"
            "748008534040890923814202286633163248086055216976551456088015"
            "338880713818192088877057717530169381044092839402438015097654"
            "53542091716518238707344493641683483917"
        )
        # Assert that encoding the BigInteger produces the expected Base64 string
        self.assertEqual(
            encoded_int4, "".join(map(chr, Base64.encodeInteger(big_int4)))
        )

        # Assert that decoding the Base64 string produces the original BigInteger
        self.assertEqual(
            big_int4, Base64.decodeInteger(encoded_int4.encode(self.__CHARSET_UTF8))
        )

    def testCodeInteger4_test1_decomposed(self) -> None:
        encoded_int4 = (
            "ctA8YGxrtngg/zKVvqEOefnwmViFztcnPBYPlJsvh6yKI"
            "4iDm68fnp4Mi3RrJ6bZAygFrUIQLxLjV+OJtgJAEto0xAs+Mehuq1DkSFEpP3o"
            "DzCTOsrOiS1DwQe4oIb7zVk/9l7aPtJMHW0LVlMdwZNFNNJoqMcT2ZfCPrfvYv"
            "Q0="
        )
        big_int4 = int(
            "80624726256040348115552042320"
            "6968135001872753709424419772586693950232350200555646471175944"
            "519297087885987040810778908507262272892702303774422853675597"
            "748008534040890923814202286633163248086055216976551456088015"
            "338880713818192088877057717530169381044092839402438015097654"
            "53542091716518238707344493641683483917"
        )
        self.assertEqual(
            encoded_int4, Base64.encodeInteger(big_int4).decode(self.__CHARSET_UTF8)
        )
        encoded_int4_bytes = encoded_int4.encode(self.__CHARSET_UTF8)

    def testCodeInteger4_test0_decomposed(self) -> None:
        encoded_int4 = (
            "ctA8YGxrtngg/zKVvqEOefnwmViFztcnPBYPlJsvh6yKI"
            "4iDm68fnp4Mi3RrJ6bZAygFrUIQLxLjV+OJtgJAEto0xAs+Mehuq1DkSFEpP3o"
            "DzCTOsrOiS1DwQe4oIb7zVk/9l7aPtJMHW0LVlMdwZNFNNJoqMcT2ZfCPrfvYv"
            "Q0="
        )
        big_int4 = int(
            "80624726256040348115552042320"
            "6968135001872753709424419772586693950232350200555646471175944"
            "519297087885987040810778908507262272892702303774422853675597"
            "748008534040890923814202286633163248086055216976551456088015"
            "338880713818192088877057717530169381044092839402438015097654"
            "53542091716518238707344493641683483917"
        )
        self.assertEqual(
            encoded_int4,
            "".join(map(chr, Base64.encodeInteger(big_int4))),
            "Encoded integer does not match the expected Base64 string",
        )

    def testCodeInteger3_test2_decomposed(self) -> None:
        encoded_int3 = (
            "FKIhdgaG5LGKiEtF1vHy4f3y700zaD6QwDS3IrNVGzNp2"
            "rY+1LFWTK6D44AyiC1n8uWz1itkYMZF0/aKDK0Yjg=="
        )
        big_int3 = int(
            "108065481540938734619517485451196989136416448805819079363524309897749044958112417136240557"
            "4495062430572478766856090958495998158114332651671116876320938126"
        )
        self.assertEqual(
            encoded_int3, Base64.encodeInteger(big_int3).decode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            big_int3, Base64.decodeInteger(encoded_int3.encode(self.__CHARSET_UTF8))
        )

    def testCodeInteger3_test1_decomposed(self) -> None:
        encoded_int3 = (
            "FKIhdgaG5LGKiEtF1vHy4f3y700zaD6QwDS3IrNVGzNp2"
            "rY+1LFWTK6D44AyiC1n8uWz1itkYMZF0/aKDK0Yjg=="
        )
        big_int3 = int(
            "10806548154093873461951748545"
            "1196989136416448805819079363524309897749044958112417136240557"
            "4495062430572478766856090958495998158114332651671116876320938126"
        )
        self.assertEqual(
            encoded_int3, Base64.encodeInteger(big_int3).decode(self.__CHARSET_UTF8)
        )
        encoded_int3_bytes = encoded_int3.encode(self.__CHARSET_UTF8)

    def testCodeInteger3_test0_decomposed(self) -> None:
        encoded_int3 = (
            "FKIhdgaG5LGKiEtF1vHy4f3y700zaD6QwDS3IrNVGzNp2"
            "rY+1LFWTK6D44AyiC1n8uWz1itkYMZF0/aKDK0Yjg=="
        )
        big_int3 = int(
            "108065481540938734619517485451196989136416448805819079363524309897749044958112417136240557"
            "4495062430572478766856090958495998158114332651671116876320938126"
        )
        self.assertEqual(
            encoded_int3,
            "".join(map(chr, Base64.encodeInteger(big_int3))),
            "Encoded integer does not match the expected Base64 string",
        )

    def testCodeInteger2_test2_decomposed(self) -> None:
        encoded_int2 = "9B5ypLY9pMOmtxCeTDHgwdNFeGs="
        big_int2 = int("1393672757286116725466646726891466679477132949611")

        # Assert that encoding the BigInteger produces the expected Base64 string
        self.assertEqual(
            encoded_int2, "".join(map(chr, Base64.encodeInteger(big_int2)))
        )

        # Assert that decoding the Base64 string produces the original BigInteger
        self.assertEqual(
            big_int2, Base64.decodeInteger(encoded_int2.encode(self.__CHARSET_UTF8))
        )

    def testCodeInteger2_test1_decomposed(self) -> None:
        encoded_int2 = "9B5ypLY9pMOmtxCeTDHgwdNFeGs="
        big_int2 = int("1393672757286116725466646726891466679477132949611")
        self.assertEqual(
            encoded_int2, Base64.encodeInteger(big_int2).decode(self.__CHARSET_UTF8)
        )
        encoded_int2_bytes = encoded_int2.encode(self.__CHARSET_UTF8)

    def testCodeInteger2_test0_decomposed(self) -> None:
        encoded_int2 = "9B5ypLY9pMOmtxCeTDHgwdNFeGs="
        big_int2 = int("1393672757286116725466646726891466679477132949611")
        self.assertEqual(
            encoded_int2, "".join(map(chr, Base64.encodeInteger(big_int2)))
        )

    def testCodeInteger1_test2_decomposed(self) -> None:
        encoded_int1 = "li7dzDacuo67Jg7mtqEm2TRuOMU="
        big_int1 = int("857393771208094202104259627990318636601332086981")

        # Assert that encoding the BigInteger produces the expected Base64 string
        self.assertEqual(
            encoded_int1, "".join(map(chr, Base64.encodeInteger(big_int1)))
        )

        # Convert the encoded string to bytes using UTF-8
        encoded_bytes = encoded_int1.encode(self.__CHARSET_UTF8)

        # Assert that decoding the Base64 bytes produces the original BigInteger
        self.assertEqual(big_int1, Base64.decodeInteger(encoded_bytes))

    def testCodeInteger1_test1_decomposed(self) -> None:
        encoded_int1 = "li7dzDacuo67Jg7mtqEm2TRuOMU="
        big_int1 = int("857393771208094202104259627990318636601332086981")
        self.assertEqual(
            encoded_int1, Base64.encodeInteger(big_int1).decode(self.__CHARSET_UTF8)
        )
        encoded_int1_bytes = encoded_int1.encode(self.__CHARSET_UTF8)

    def testCodeInteger1_test0_decomposed(self) -> None:
        encoded_int1 = "li7dzDacuo67Jg7mtqEm2TRuOMU="
        big_int1 = int("857393771208094202104259627990318636601332086981")
        self.assertEqual(encoded_int1, Base64.encodeInteger(big_int1).decode("utf-8"))

    def testCodec68_test0_decomposed(self) -> None:
        x = [ord("n"), ord("A"), ord("="), ord("="), 0x9C]
        Base64.decodeBase640(x)

    def testChunkedEncodeMultipleOf76_test2_decomposed(self) -> None:
        expected_encode = Base64.encodeBase641(BaseNTestData.DECODED, True)
        actual_result = Base64TestData.ENCODED_76_CHARS_PER_LINE.replace("\n", "\r\n")
        actual_encode = StringUtils.getBytesUtf8(actual_result)
        self.assertEqual(expected_encode, actual_encode, "chunkedEncodeMultipleOf76")

    def testChunkedEncodeMultipleOf76_test1_decomposed(self) -> None:
        expected_encode = Base64.encodeBase641(BaseNTestData.DECODED, True)
        actual_result = Base64TestData.ENCODED_76_CHARS_PER_LINE.replace("\n", "\r\n")
        actual_encode = StringUtils.getBytesUtf8(actual_result)

    def testChunkedEncodeMultipleOf76_test0_decomposed(self) -> None:
        expected_encode = Base64.encodeBase641(BaseNTestData.DECODED, True)

    def testDecodeWithInnerPad_test2_decomposed(self) -> None:
        content = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        result = Base64.decodeBase641(content)
        shouldBe = StringUtils.getBytesUtf8("Hello World")
        self.assertEqual(result, shouldBe, "decode should halt at pad (=)")

    def testDecodeWithInnerPad_test1_decomposed(self) -> None:
        content = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        result = Base64.decodeBase641(content)
        shouldBe = StringUtils.getBytesUtf8("Hello World")

    def testDecodeWithInnerPad_test0_decomposed(self) -> None:
        content = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        result = Base64.decodeBase641(content)

    def testBase64_test13_decomposed(self) -> None:
        content = "Hello World"

        # Encoding "Hello World" using Base64
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with line length 0
        b64 = Base64.Base642(0, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Decoding a malformed Base64 string
        decode = b64.decode3("SGVsbG{\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9}8gV29ybGQ=")
        decode_string = StringUtils.newStringUtf8(decode)
        self.assertEqual("Hello World", decode_string, "decode hello world")

    def testBase64_test12_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding content using Base64
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with line length 0
        b64 = Base64.Base642(0, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Decoding a malformed Base64 string
        decode = b64.decode3("SGVsbG{\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9}8gV29ybGQ=")
        decode_string = StringUtils.newStringUtf8(decode)

    def testBase64_test11_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding using Base64.encodeBase640
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with line length 0
        b64 = Base64.Base642(0, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Decoding with invalid Base64 string
        with self.assertRaises(DecoderException):
            b64.decode3("SGVsbG{\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9}8gV29ybGQ=")

    def testBase64_test10_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding using Base64.encodeBase640
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with line length 0
        b64 = Base64.Base642(0, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)

    def testBase64_test9_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding using Base64.encodeBase640
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with line length 0
        b64 = Base64.Base642(0, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))

    def testBase64_test8_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding using Base64.encodeBase640
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Encoding using Base64.Base642 with line length 0
        b64 = Base64.Base642(0, None)
        StringUtils.getBytesUtf8(content)

    def testBase64_test7_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Encoding the content using Base64
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with MIME_CHUNK_SIZE
        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with line length 0
        b64 = Base64.Base642(0, None)

    def testBase64_test6_decomposed(self) -> None:
        content = "Hello World"
        # Encoding the content to Base64
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Using Base64 with MIME_CHUNK_SIZE
        b64 = Base64(BaseNCodec.MIME_CHUNK_SIZE, None)
        encoded_bytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)

    def testBase64_test5_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None

        # Convert content to bytes using UTF-8
        content_bytes = StringUtils.getBytesUtf8(content)

        # Encode the bytes using Base64
        encoded_bytes = Base64.encodeBase640(content_bytes)

        # Convert the encoded bytes back to a UTF-8 string
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)

        # Assert that the encoded content matches the expected Base64 string
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")

        # Create a Base64 instance with MIME_CHUNK_SIZE
        b64 = Base64(BaseNCodec.MIME_CHUNK_SIZE, None)

        # Encode the content bytes using the Base64 instance
        encoded_bytes = b64.encode0(content_bytes)

    def testBase64_test4_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")
        b64 = Base64(BaseNCodec.MIME_CHUNK_SIZE, None)
        StringUtils.getBytesUtf8(content)

    def testBase64_test3_decomposed(self) -> None:
        content = "Hello World"
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual("SGVsbG8gV29ybGQ=", encoded_content, "encoding hello world")
        b64 = Base64(BaseNCodec.MIME_CHUNK_SIZE, None)

    def testBase64_test2_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)

    def testBase64_test1_decomposed(self) -> None:
        content = "Hello World"
        encoded_content = None
        encoded_bytes = Base64.encodeBase640(StringUtils.getBytesUtf8(content))

    def testBase64_test0_decomposed(self) -> None:
        content: str = "Hello World"
        encoded_content: str
        StringUtils.getBytesUtf8(content)

    def testIsStringBase64_test1_decomposed(self) -> None:
        null_string = None
        empty_string = ""
        valid_string = (
            "abc===defg\n\r123456\r789\r\rABC\n\nDEF==GHI\r\nJKL=============="
        )
        invalid_string = valid_string + chr(0)

        with self.assertRaises(RuntimeError) as context:
            Base64.isBase642(null_string)
        self.assertIsNotNone(
            context.exception, "Base64.isStringBase64() should not be null-safe."
        )

        self.assertTrue(
            Base64.isBase642(empty_string),
            "Base64.isStringBase64(empty-string) is true",
        )
        self.assertTrue(
            Base64.isBase642(valid_string),
            "Base64.isStringBase64(valid-string) is true",
        )
        self.assertFalse(
            Base64.isBase642(invalid_string),
            "Base64.isStringBase64(invalid-string) is false",
        )

    def testIsStringBase64_test0_decomposed(self) -> None:
        null_string = None
        empty_string = ""
        valid_string = (
            "abc===defg\n\r123456\r789\r\rABC\n\nDEF==GHI\r\nJKL=============="
        )
        invalid_string = valid_string + chr(0)

        with pytest.raises(
            TypeError
        ) as excinfo:  # RuntimeError in Java maps to TypeError in Python for NoneType issues
            Base64.isBase642(null_string)
        self.assertIsNotNone(
            excinfo.value, "Base64.isStringBase64() should not be null-safe."
        )

    def getRandom(self) -> random.Random:
        return self.__random

    @staticmethod
    def __assertBase64DecodingOfTrailingBits(nbits: int) -> None:
        codec = Base64(0, None, False, CodecPolicy.STRICT)
        assert codec.isStrictDecoding()
        assert codec.getCodecPolicy() == CodecPolicy.STRICT

        default_codec = Base64Test.Base645()
        assert not default_codec.isStrictDecoding()
        assert default_codec.getCodecPolicy() == CodecPolicy.LENIENT

        length = nbits // 6
        encoded = [0] * 4
        encoded[:length] = [Base64Test.__STANDARD_ENCODE_TABLE[0]] * length
        encoded[length:] = [ord("=")] * (4 - length)

        discard = nbits % 8
        empty_bits_mask = (1 << discard) - 1
        invalid = length == 1
        last = length - 1

        for i in range(64):
            encoded[last] = Base64Test.__STANDARD_ENCODE_TABLE[i]
            if invalid or (i & empty_bits_mask) != 0:
                try:
                    codec.decode0(encoded)
                    pytest.fail("Final base-64 digit should not be allowed")
                except ValueError:
                    pass
                decoded = default_codec.decode0(encoded)
                assert not decoded == default_codec.encode0(decoded)
            else:
                decoded = codec.decode0(encoded)
                bits_encoded = i >> discard
                assert decoded[-1] == bits_encoded, "Invalid decoding of last character"
                assert encoded == codec.encode0(decoded)

    def __toString(self, data: typing.List[int]) -> str:
        buf = []
        for i in range(len(data)):
            buf.append(str(data[i]))
            if i != len(data) - 1:
                buf.append(",")
        return "".join(buf)

    def __testEncodeDecode(self, plainText: str) -> None:
        encoded_text = Base64.encodeBase64String(StringUtils.getBytesUtf8(plainText))
        decoded_text = StringUtils.newStringUsAscii(Base64.decodeBase641(encoded_text))
        self.assertEqual(plainText, decoded_text)

    def __testDecodeEncode(self, encodedText: str) -> None:
        decodedText = StringUtils.newStringUsAscii(Base64.decodeBase641(encodedText))
        encodedText2 = Base64.encodeBase64String(StringUtils.getBytesUtf8(decodedText))
        self.assertEqual(encodedText, encodedText2)

    def __testEncodeOverMaxSize1(self, maxSize: int) -> None:
        with pytest.raises(ValueError, match=r".*Input array too big.*"):
            Base64.encodeBase643(BaseNTestData.DECODED, True, False, maxSize)
