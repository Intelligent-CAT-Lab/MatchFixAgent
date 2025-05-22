from __future__ import annotations
import time
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Hex import *


class Base32Test(unittest.TestCase):

    BASE32_IMPOSSIBLE_CASES: List[str] = [
        "MC======",
        "MZXE====",
        "MZXWB===",
        "MZXW6YB=",
        "MZXW6YTBOC======",
        "AB======",
    ]
    __BASE32_PAD_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY%%%%%%"],
        ["fo", "MZXQ%%%%"],
        ["foo", "MZXW6%%%"],
        ["foob", "MZXW6YQ%"],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI%%%%%%"],
    ]
    __BASE32_TEST_CASES_CHUNKED: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY======\r\n"],
        ["fo", "MZXQ====\r\n"],
        ["foo", "MZXW6===\r\n"],
        ["foob", "MZXW6YQ=\r\n"],
        ["fooba", "MZXW6YTB\r\n"],
        ["foobar", "MZXW6YTBOI======\r\n"],
    ]
    __BASE32HEX_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "CO======"],
        ["fo", "CPNG===="],
        ["foo", "CPNMU==="],
        ["foob", "CPNMUOG="],
        ["fooba", "CPNMUOJ1"],
        ["foobar", "CPNMUOJ1E8======"],
    ]
    __BASE32_BINARY_TEST_CASES: typing.List[typing.List[typing.Any]] = None

    __ENCODE_TABLE: typing.List[int] = [
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
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
    ]
    __BASE32HEX_IMPOSSIBLE_CASES: List[str] = [
        "C2======",
        "CPN4====",
        "CPNM1===",
        "CPNMUO1=",
        "CPNMUOJ1E2======",
    ]
    BASE32_IMPOSSIBLE_CASES_CHUNKED: List[str] = [
        "M2======\r\n",
        "MZX0====\r\n",
        "MZXW0===\r\n",
        "MZXW6Y2=\r\n",
        "MZXW6YTBO2======\r\n",
    ]
    __BASE32_TEST_CASES: typing.List[typing.List[str]] = [
        ["", ""],
        ["f", "MY======"],
        ["fo", "MZXQ===="],
        ["foo", "MZXW6==="],
        ["foob", "MZXW6YQ="],
        ["fooba", "MZXW6YTB"],
        ["foobar", "MZXW6YTBOI======"],
    ]
    __CHARSET_UTF8: str = "UTF-8"

    @staticmethod
    def run_static_init():
        hex = Hex(2, None, None)
        try:
            Base32Test.__BASE32_BINARY_TEST_CASES = [
                [
                    hex.decode2("623a01735836e9a126e12fbf95e013ee6892997c"),
                    "MI5AC42YG3U2CJXBF67ZLYAT5ZUJFGL4",
                ],
                [
                    hex.decode2("623a01735836e9a126e12fbf95e013ee6892997c"),
                    "mi5ac42yg3u2cjxbf67zlyat5zujfgl4",
                ],
                [hex.decode2("739ce42108"), "OOOOIIII"],
            ]
        except DecoderException as de:
            raise RuntimeError(":(") from de

    def testBase32DecodingOfTrailing35Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(35)

    def testBase32DecodingOfTrailing30Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(30)

    def testBase32DecodingOfTrailing25Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(25)

    def testBase32DecodingOfTrailing20Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(20)

    def testBase32DecodingOfTrailing15Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(15)

    def testBase32DecodingOfTrailing10Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(10)

    def testBase32DecodingOfTrailing5Bits_test0_decomposed(self) -> None:
        self.__assertBase32DecodingOfTrailingBits(5)

    def testBase32HexImpossibleSamples_test0_decomposed(self) -> None:
        self.__testImpossibleCases(
            Base32(0, None, True, BaseNCodec._PAD_DEFAULT, CodecPolicy.STRICT),
            self.__BASE32HEX_IMPOSSIBLE_CASES,
        )

    def testBase32ImpossibleChunked_test0_decomposed(self) -> None:
        codec = Base32(
            lineLength=20,
            lineSeparator=BaseNCodec.CHUNK_SEPARATOR,
            useHex=False,
            padding=BaseNCodec._PAD_DEFAULT,
            decodingPolicy=CodecPolicy.STRICT,
        )
        self.__testImpossibleCases(codec, self.BASE32_IMPOSSIBLE_CASES_CHUNKED)

    def testBase32ImpossibleSamples_test0_decomposed(self) -> None:
        self.__testImpossibleCases(
            Base32(0, None, False, BaseNCodec._PAD_DEFAULT, CodecPolicy.STRICT),
            self.BASE32_IMPOSSIBLE_CASES,
        )

    def testSingleCharEncoding_test0_decomposed(self) -> None:
        for i in range(20):
            codec = Base32.Base320()
            context = Context()
            unencoded = bytearray(i)
            all_in_one = codec.encode0(unencoded)

            codec = Base32.Base320()
            for j in range(len(unencoded)):
                codec.encode2(unencoded, j, 1, context)
            codec.encode2(unencoded, 0, -1, context)

            singly = bytearray(len(all_in_one))
            codec.readResults(singly, 0, len(singly), context)

            self.assertTrue(all_in_one == singly, "Encoded outputs do not match")

    def testRandomBytesHex_test0_decomposed(self) -> None:
        for i in range(20):
            codec = Base32.Base321(True)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                codec.getEncodedLength(b[0]), len(b[1]), f"{i} {codec._lineLength}"
            )

    def testRandomBytesChunked_test0_decomposed(self) -> None:
        for i in range(20):
            codec = Base32.Base324(10)
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                codec.getEncodedLength(b[0]), len(b[1]), f"{i} {codec._lineLength}"
            )

    def testRandomBytes_test0_decomposed(self) -> None:
        for i in range(20):
            codec = Base32.Base320()
            b = BaseNTestData.randomData(codec, i)
            self.assertEqual(
                codec.getEncodedLength(b[0]), len(b[1]), f"{i} {codec._lineLength}"
            )

    def testIsInAlphabet_test5_decomposed(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))

        b32 = Base32.Base321(False)
        for c in range(ord("2"), ord("7") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("Z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))

        self.assertFalse(b32.isInAlphabet0(ord("1")))
        self.assertFalse(b32.isInAlphabet0(ord("8")))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("Z") + 1))

        b32 = Base32.Base321(True)
        for c in range(ord("0"), ord("9") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("V") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("v") + 1):
            self.assertTrue(b32.isInAlphabet0(c))

        self.assertFalse(b32.isInAlphabet0(ord("0") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("9") + 1))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("V") + 1))
        self.assertFalse(b32.isInAlphabet0(ord("a") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("v") + 1))

    def testIsInAlphabet_test4_decomposed(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))

        b32 = Base32.Base321(False)
        for c in range(ord("2"), ord("7") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("Z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))

        self.assertFalse(b32.isInAlphabet0(ord("1")))
        self.assertFalse(b32.isInAlphabet0(ord("8")))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("Z") + 1))

        b32 = Base32.Base321(True)

    def testIsInAlphabet_test3_decomposed(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))

        b32 = Base32.Base321(False)
        for c in range(ord("2"), ord("7") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("A"), ord("Z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))
        for c in range(ord("a"), ord("z") + 1):
            self.assertTrue(b32.isInAlphabet0(c))

        self.assertFalse(b32.isInAlphabet0(ord("1")))
        self.assertFalse(b32.isInAlphabet0(ord("8")))
        self.assertFalse(b32.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b32.isInAlphabet0(ord("Z") + 1))

    def testIsInAlphabet_test2_decomposed(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))
        b32 = Base32.Base321(False)

    def testIsInAlphabet_test1_decomposed(self) -> None:
        b32 = Base32.Base321(True)
        self.assertFalse(b32.isInAlphabet0(0))
        self.assertFalse(b32.isInAlphabet0(1))
        self.assertFalse(b32.isInAlphabet0(-1))
        self.assertFalse(b32.isInAlphabet0(-15))
        self.assertFalse(b32.isInAlphabet0(-32))
        self.assertFalse(b32.isInAlphabet0(127))
        self.assertFalse(b32.isInAlphabet0(128))
        self.assertFalse(b32.isInAlphabet0(255))

    def testIsInAlphabet_test0_decomposed(self) -> None:
        b32 = Base32.Base321(True)

    def testEmptyBase32_test11_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")

        # Test encoding with offset and None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode with offset")

        # Test decoding an empty byte array
        empty = bytearray()  # Equivalent to new byte[0];
        result = base32.decode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 decode")

        # Test decoding a None value
        self.assertIsNone(base32.decode0(None), "empty Base32 encode")

    def testEmptyBase32_test10_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")
        self.assertIsNone(base32.encode0(None), "empty Base32 encode with offset")

        # Test decoding an empty byte array
        empty = bytearray()  # Equivalent to empty = new byte[0];
        result = base32.decode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 decode")

    def testEmptyBase32_test9_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")

        # Test encoding with offset and None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode with offset")

        # Test decoding an empty byte array
        empty = bytearray()  # Equivalent to empty = new byte[0];
        result = base32.decode0(empty)

    def testEmptyBase32_test8_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Initialize Base32 instance

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")

        # Test encoding with offset and None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode with offset")

        # Reassign empty to a new empty byte array
        empty = bytearray()

    def testEmptyBase32_test7_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")

        # Test encoding with offset and None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode with offset")

    def testEmptyBase32_test6_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Create a Base32 instance

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with offset and length
        result = base32.encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base32 encode with offset")

    def testEmptyBase32_test5_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Create an instance of Base32

        # Test encoding an empty byte array
        result = base32.encode0(empty)
        self.assertEqual(len(result), 0, "empty Base32 encode")

        # Test encoding a None value
        self.assertIsNone(base32.encode0(None), "empty Base32 encode")

        # Test encoding with specific parameters
        result = base32.encode1(empty, 0, 1)

    def testEmptyBase32_test4_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Initialize Base32 instance
        result = base32.encode0(empty)  # Call encode0 with empty byte array
        self.assertEqual(
            len(result), 0, "empty Base32 encode"
        )  # Assert result length is 0
        self.assertIsNone(
            base32.encode0(None), "empty Base32 encode"
        )  # Assert encoding None returns None

    def testEmptyBase32_test3_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Initialize Base32 instance
        result = base32.encode0(empty)  # Call encode0 with empty byte array
        self.assertEqual(
            len(result), 0, "empty Base32 encode"
        )  # Assert result length is 0
        self.assertIsNone(
            base32.encode0(None), "empty Base32 encode"
        )  # Assert encoding None returns None

    def testEmptyBase32_test2_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = Base32.Base320()  # Instantiate Base32 using the static method
        result = base32.encode0(
            empty
        )  # Call the encode0 method with the empty byte array
        self.assertEqual(
            len(result), 0, "empty Base32 encode"
        )  # Assert the result length is 0 with a message
        base32 = Base32.Base320()  # Re-instantiate Base32 (as in the Java code)

    def testEmptyBase32_test1_decomposed(self) -> None:
        empty = bytearray()  # Equivalent to byte[] empty = {};
        base32 = (
            Base32.Base320()
        )  # Call the static method Base320() to get a Base32 instance
        result = base32.encode0(
            empty
        )  # Call the encode0 method with the empty byte array
        self.assertEqual(
            result, empty
        )  # Assert that the result is the same as the input

    def testEmptyBase32_test0_decomposed(self) -> None:
        empty = bytes()  # Equivalent to byte[] empty = {};
        Base32.Base320()  # Call the static method Base320() from the Base32 class

    def testConstructors_test7_decomposed(self) -> None:
        base32 = None
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)
        base32 = Base32.Base325(-1, [ord("A")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, None)
            pytest.fail("Should have rejected null line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A")])
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("=")])
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base32 = Base32.Base325(32, [ord("$")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A"), ord("$")])
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord("A"))
            pytest.fail("Should have rejected attempt to use 'A' as padding")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord(" "))
            pytest.fail("Should have rejected attempt to use ' ' as padding")

        base32 = Base32.Base325(
            32, [ord(" "), ord("$"), ord("\n"), ord("\r"), ord("\t")]
        )
        self.assertIsNotNone(base32)

    def testConstructors_test6_decomposed(self) -> None:
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)
        base32 = Base32.Base325(-1, [ord("A")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, None)
            pytest.fail("Should have rejected null line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A")])
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("=")])
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base32 = Base32.Base325(32, [ord("$")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A"), ord("$")])
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord("A"))
            pytest.fail("Should have rejected attempt to use 'A' as padding")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord(" "))
            pytest.fail("Should have rejected attempt to use ' ' as padding")

        base32 = Base32.Base325(
            32, [ord(" "), ord("$"), ord("\n"), ord("\r"), ord("\t")]
        )

    def testConstructors_test5_decomposed(self) -> None:
        base32 = None
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)
        base32 = Base32.Base325(-1, [ord("A")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, None)
            pytest.fail("Should have rejected null line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A")])
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("=")])
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base32 = Base32.Base325(32, [ord("$")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A"), ord("$")])
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord("A"))
            pytest.fail("Should have rejected attempt to use 'A' as padding")

        with pytest.raises(ValueError):
            base32 = Base32.Base327(32, [ord("\n")], False, ord(" "))
            pytest.fail("Should have rejected attempt to use ' ' as padding")

    def testConstructors_test4_decomposed(self) -> None:
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)
        base32 = Base32.Base325(-1, [ord("A")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, None)
            pytest.fail("Should have rejected null line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A")])
            pytest.fail("Should have rejected attempt to use 'A' as a line separator")

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("=")])
            pytest.fail("Should have rejected attempt to use '=' as a line separator")

        base32 = Base32.Base325(32, [ord("$")])

        with pytest.raises(ValueError):
            base32 = Base32.Base325(32, [ord("A"), ord("$")])
            pytest.fail("Should have rejected attempt to use 'A$' as a line separator")

    def testConstructors_test3_decomposed(self) -> None:
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])
        base32 = Base32.Base326(32, [], False)

    def testConstructors_test2_decomposed(self) -> None:
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)
        base32 = Base32.Base325(-1, [])
        base32 = Base32.Base325(32, [])

    def testConstructors_test1_decomposed(self) -> None:
        base32 = Base32.Base320()
        base32 = Base32.Base324(-1)

    def testConstructors_test0_decomposed(self) -> None:
        base32 = Base32.Base320()

    def testCodec200_test1_decomposed(self) -> None:
        codec = Base32.Base322(True, ord("W"))
        self.assertIsNotNone(codec)

    def testCodec200_test0_decomposed(self) -> None:
        codec = Base32.Base322(True, ord("W"))

    def testBase32SamplesNonDefaultPadding_test1_decomposed(self) -> None:
        codec = Base32.Base323(
            0x25
        )  # Create a Base32 codec with custom padding (0x25 = '%')
        for element in self.__BASE32_PAD_TEST_CASES:
            expected = element[1]
            actual = codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            self.assertEqual(expected, actual, f"Failed for input: {element[0]}")

    def testBase32SamplesNonDefaultPadding_test0_decomposed(self) -> None:
        codec = Base32.Base323(0x25)

    def testBase32BinarySamplesReverse_test1_decomposed(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            self.assertListEqual(
                list(element[0]),
                codec.decode3(element[1]),
                "Decoded output does not match expected output",
            )

    def testBase32BinarySamplesReverse_test0_decomposed(self) -> None:
        codec = Base32.Base320()

    def testBase32BinarySamples_test1_decomposed(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_BINARY_TEST_CASES:
            if len(element) > 2:
                expected = element[2]
            else:
                expected = element[1]
            self.assertEqual(
                expected.upper(),
                codec.encodeAsString(element[0]),
                "Encoded string does not match the expected value",
            )

    def testBase32BinarySamples_test0_decomposed(self) -> None:
        codec = Base32.Base320()

    def testBase32Samples_test1_decomposed(self) -> None:
        codec = Base32.Base320()
        for element in self.__BASE32_TEST_CASES:
            expected = element[1]
            actual = codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8))
            self.assertEqual(expected, actual, f"Failed for input: {element[0]}")

    def testBase32Samples_test0_decomposed(self) -> None:
        codec = Base32.Base320()

    def testBase32HexSamplesReverseLowercase_test1_decomposed(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[0],
                codec.decode3(element[1].lower()).decode(self.__CHARSET_UTF8),
                f"Decoding failed for input: {element[1]}",
            )

    def testBase32HexSamplesReverseLowercase_test0_decomposed(self) -> None:
        codec = Base32.Base321(True)

    def testBase32HexSamplesReverse_test1_decomposed(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            decoded = codec.decode3(element[1]).decode(self.__CHARSET_UTF8)
            self.assertEqual(
                element[0], decoded, f"Decoding failed for input: {element[1]}"
            )

    def testBase32HexSamplesReverse_test0_decomposed(self) -> None:
        codec = Base32.Base321(True)

    def testBase32HexSamples_test1_decomposed(self) -> None:
        codec = Base32.Base321(True)
        for element in self.__BASE32HEX_TEST_CASES:
            self.assertEqual(
                element[1],
                codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8)),
                f"Failed for input: {element[0]}",
            )

    def testBase32HexSamples_test0_decomposed(self) -> None:
        codec = Base32.Base321(True)

    def testBase32Chunked_test1_decomposed(self) -> None:
        codec = Base32.Base324(20)
        for element in self.__BASE32_TEST_CASES_CHUNKED:
            self.assertEqual(
                element[1],
                codec.encodeAsString(element[0].encode(self.__CHARSET_UTF8)),
                f"Encoding mismatch for input: {element[0]}",
            )

    def testBase32Chunked_test0_decomposed(self) -> None:
        codec = Base32.Base324(20)

    @staticmethod
    def __assertBase32DecodingOfTrailingBits(nbits: int) -> None:
        codec = Base32(0, None, False, BaseNCodec._PAD_DEFAULT, CodecPolicy.STRICT)
        assert codec.isStrictDecoding()
        assert codec.getCodecPolicy() == CodecPolicy.STRICT

        default_codec = Base32.Base320()
        assert not default_codec.isStrictDecoding()
        assert default_codec.getCodecPolicy() == CodecPolicy.LENIENT

        length = nbits // 5
        encoded = [0] * 8
        encoded[:length] = [Base32Test.__ENCODE_TABLE[0]] * length
        encoded[length:] = [BaseNCodec._PAD_DEFAULT] * (8 - length)

        discard = nbits % 8
        empty_bits_mask = (1 << discard) - 1
        invalid = length in (1, 3, 6)
        last = length - 1

        for i in range(32):
            encoded[last] = Base32Test.__ENCODE_TABLE[i]
            if invalid or (i & empty_bits_mask) != 0:
                try:
                    codec.decode0(encoded)
                    pytest.fail("Final base-32 digit should not be allowed")
                except ValueError:
                    pass
                decoded = default_codec.decode0(encoded)
                assert not decoded == default_codec.encode0(decoded)
            else:
                decoded = codec.decode0(encoded)
                bits_encoded = i >> discard
                assert decoded[-1] == bits_encoded, "Invalid decoding of last character"
                assert encoded == codec.encode0(decoded)

    def __testImpossibleCases(self, codec: Base32, impossible_cases: List[str]) -> None:
        for impossible in impossible_cases:
            with pytest.raises(ValueError):
                codec.decode3(impossible)


Base32Test.run_static_init()
