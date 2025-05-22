from __future__ import annotations
import time
import re
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.binary.StringUtils import *


class StringUtilsTest(unittest.TestCase):

    __STRING_FIXTURE: str = "ABC"
    __BYTES_FIXTURE_16LE: typing.List[int] = [ord("a"), 0, ord("b"), 0, ord("c"), 0]
    __BYTES_FIXTURE_16BE: typing.List[int] = [0, ord("a"), 0, ord("b"), 0, ord("c")]
    __BYTES_FIXTURE: typing.List[int] = [ord("a"), ord("b"), ord("c")]

    def testByteBufferUtf8_test2_decomposed(self) -> None:
        self.assertIsNone(StringUtils.getByteBufferUtf8(None), "Should be null safe")
        text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk"
        bb = StringUtils.getByteBufferUtf8(text)
        self.assertEqual(bytearray(text.encode("utf-8")), bb)

    def testByteBufferUtf8_test1_decomposed(self) -> None:
        self.assertIsNone(StringUtils.getByteBufferUtf8(None), "Should be null safe")
        text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk"
        bb = StringUtils.getByteBufferUtf8(text)

    def testByteBufferUtf8_test0_decomposed(self) -> None:
        self.assertIsNone(StringUtils.getByteBufferUtf8(None), "Should be null safe")

    def testEqualsCS2_test0_decomposed(self) -> None:
        self.assertTrue(StringUtils.equals("abc", "abc"))
        self.assertFalse(StringUtils.equals("abc", "abcd"))
        self.assertFalse(StringUtils.equals("abcd", "abc"))
        self.assertFalse(StringUtils.equals("abc", "ABC"))

    def testEqualsCS1_test0_decomposed(self) -> None:
        self.assertFalse(StringUtils.equals("abc", None))
        self.assertFalse(StringUtils.equals(None, "abc"))
        self.assertTrue(StringUtils.equals("abc", "abc"))
        self.assertFalse(StringUtils.equals("abc", "abcd"))
        self.assertFalse(StringUtils.equals("abcd", "abc"))
        self.assertFalse(StringUtils.equals("abc", "ABC"))

    def testEqualsString_test0_decomposed(self) -> None:
        self.assertTrue(StringUtils.equals(None, None))
        self.assertFalse(StringUtils.equals("abc", None))
        self.assertFalse(StringUtils.equals(None, "abc"))
        self.assertTrue(StringUtils.equals("abc", "abc"))
        self.assertFalse(StringUtils.equals("abc", "abcd"))
        self.assertFalse(StringUtils.equals("abcd", "abc"))
        self.assertFalse(StringUtils.equals("abc", "ABC"))

    def testNewStringUtf8_test2_decomposed(self) -> None:
        charset_name = "utf-8"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUtf8(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf8_test1_decomposed(self) -> None:
        charset_name = "utf-8"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUtf8(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf8_test0_decomposed(self) -> None:
        charset_name = "UTF-8"
        self.__testNewString(charset_name)

    def testNewStringUtf16Le_test2_decomposed(self) -> None:
        charset_name = "utf-16le"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE_16LE).decode(charset_name)
        actual = StringUtils.newStringUtf16Le(self.__BYTES_FIXTURE_16LE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Le_test1_decomposed(self) -> None:
        charset_name = "utf-16le"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE_16LE).decode(charset_name)
        actual = StringUtils.newStringUtf16Le(self.__BYTES_FIXTURE_16LE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Le_test0_decomposed(self) -> None:
        charset_name = "utf-16-le"
        self.__testNewString(charset_name)

    def testNewStringUtf16Be_test2_decomposed(self) -> None:
        charset_name = "utf-16-be"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE_16BE).decode(charset_name)
        actual = StringUtils.newStringUtf16Be(self.__BYTES_FIXTURE_16BE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Be_test1_decomposed(self) -> None:
        charset_name = "utf-16-be"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE_16BE).decode(charset_name)
        actual = StringUtils.newStringUtf16Be(self.__BYTES_FIXTURE_16BE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Be_test0_decomposed(self) -> None:
        charsetName = "UTF-16BE"
        self.__testNewString(charsetName)

    def testNewStringUtf16_test2_decomposed(self) -> None:
        charset_name = "utf-16"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUtf16(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16_test1_decomposed(self) -> None:
        charset_name = "utf-16"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUtf16(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16_test0_decomposed(self) -> None:
        charset_name = "utf-16"
        self.__testNewString(charset_name)

    def testNewStringUsAscii_test2_decomposed(self) -> None:
        charset_name = "ascii"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUsAscii(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUsAscii_test1_decomposed(self) -> None:
        charset_name = "ascii"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringUsAscii(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUsAscii_test0_decomposed(self) -> None:
        charset_name = "US-ASCII"
        self.__testNewString(charset_name)

    def testNewStringIso8859_1_test2_decomposed(self) -> None:
        charset_name = "ISO-8859-1"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringIso8859_1(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringIso8859_1_test1_decomposed(self) -> None:
        charset_name = "ISO-8859-1"
        self.__testNewString(charset_name)
        expected = bytearray(self.__BYTES_FIXTURE).decode(charset_name)
        actual = StringUtils.newStringIso8859_1(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringIso8859_1_test0_decomposed(self) -> None:
        charsetName = "ISO-8859-1"
        self.__testNewString(charsetName)

    def testNewStringNullInput_CODEC229_test5_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))
        self.assertIsNone(StringUtils.newStringUsAscii(None))
        self.assertIsNone(StringUtils.newStringUtf16(None))
        self.assertIsNone(StringUtils.newStringUtf16Be(None))
        self.assertIsNone(StringUtils.newStringUtf16Le(None))

    def testNewStringNullInput_CODEC229_test4_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))
        self.assertIsNone(StringUtils.newStringUsAscii(None))
        self.assertIsNone(StringUtils.newStringUtf16(None))
        self.assertIsNone(StringUtils.newStringUtf16Be(None))

    def testNewStringNullInput_CODEC229_test3_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))
        self.assertIsNone(StringUtils.newStringUsAscii(None))
        self.assertIsNone(StringUtils.newStringUtf16(None))

    def testNewStringNullInput_CODEC229_test2_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))
        self.assertIsNone(StringUtils.newStringUsAscii(None))

    def testNewStringNullInput_CODEC229_test1_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))

    def testNewStringNullInput_CODEC229_test0_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newStringUtf8(None))

    def testNewStringNullInput_test0_decomposed(self) -> None:
        self.assertIsNone(StringUtils.newString1(None, "UNKNOWN"))

    def testNewStringBadEnc_test0_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            StringUtils.newString1(self.__BYTES_FIXTURE, "UNKNOWN")

    def testGetBytesUncheckedNullInput_test0_decomposed(self) -> None:
        self.assertIsNone(StringUtils.getBytesUnchecked(None, "UNKNOWN"))

    def testGetBytesUncheckedBadName_test0_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            StringUtils.getBytesUnchecked(self.__STRING_FIXTURE, "UNKNOWN")

    def testGetBytesUtf8_test3_decomposed(self) -> None:
        charset_name: str = "UTF-8"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf8_test2_decomposed(self) -> None:
        charset_name: str = "UTF-8"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf8_test1_decomposed(self) -> None:
        charsetName: str = "UTF-8"
        self.__testGetBytesUnchecked(charsetName)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charsetName))

    def testGetBytesUtf8_test0_decomposed(self) -> None:
        charset_name: str = "UTF-8"
        self.__testGetBytesUnchecked(charset_name)

    def testGetBytesUtf16Le_test3_decomposed(self) -> None:
        charset_name: str = "utf-16le"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16Le_test2_decomposed(self) -> None:
        charset_name: str = "utf-16le"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16Le_test1_decomposed(self) -> None:
        charset_name: str = "UTF-16LE"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))

    def testGetBytesUtf16Le_test0_decomposed(self) -> None:
        charsetName: str = "UTF-16LE"
        self.__testGetBytesUnchecked(charsetName)

    def testGetBytesUtf16Be_test3_decomposed(self) -> None:
        charset_name: str = "utf-16be"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16Be_test2_decomposed(self) -> None:
        charset_name: str = "utf-16be"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16Be_test1_decomposed(self) -> None:
        charset_name: str = "UTF-16BE"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))

    def testGetBytesUtf16Be_test0_decomposed(self) -> None:
        charsetName: str = "UTF-16BE"
        self.__testGetBytesUnchecked(charsetName)

    def testGetBytesUtf16_test3_decomposed(self) -> None:
        charset_name: str = "utf-16"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16_test2_decomposed(self) -> None:
        charset_name: str = "utf-16"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUtf16(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16_test1_decomposed(self) -> None:
        charset_name: str = "UTF-16"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))

    def testGetBytesUtf16_test0_decomposed(self) -> None:
        charsetName: str = "UTF-16"
        self.__testGetBytesUnchecked(charsetName)

    def testGetBytesUsAscii_test3_decomposed(self) -> None:
        charset_name: str = "ascii"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUsAscii(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUsAscii_test2_decomposed(self) -> None:
        charset_name: str = "ascii"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesUsAscii(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUsAscii_test1_decomposed(self) -> None:
        charset_name: str = "US-ASCII"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))

    def testGetBytesUsAscii_test0_decomposed(self) -> None:
        charsetName: str = "US-ASCII"
        self.__testGetBytesUnchecked(charsetName)

    def testGetBytesIso8859_1_test3_decomposed(self) -> None:
        charset_name: str = "ISO-8859-1"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesIso8859_1(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesIso8859_1_test2_decomposed(self) -> None:
        charset_name: str = "ISO-8859-1"
        self.__testGetBytesUnchecked(charset_name)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charset_name))
        actual: List[int] = StringUtils.getBytesIso8859_1(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesIso8859_1_test1_decomposed(self) -> None:
        charsetName: str = "ISO-8859-1"
        self.__testGetBytesUnchecked(charsetName)
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charsetName))

    def testGetBytesIso8859_1_test0_decomposed(self) -> None:
        charsetName: str = "ISO-8859-1"
        self.__testGetBytesUnchecked(charsetName)

    def testConstructor_test0_decomposed(self) -> None:
        StringUtils()

    def __testNewString(self, charsetName: str) -> None:
        expected = bytearray(self.__BYTES_FIXTURE).decode(charsetName, errors="replace")
        actual = StringUtils.newString1(self.__BYTES_FIXTURE, charsetName)
        self.assertEqual(
            expected,
            actual,
            f"Expected and actual strings do not match for charset {charsetName}",
        )

    def __testGetBytesUnchecked(self, charsetName: str) -> None:
        expected: List[int] = list(self.__STRING_FIXTURE.encode(charsetName))
        actual: List[int] = StringUtils.getBytesUnchecked(
            self.__STRING_FIXTURE, charsetName
        )
        self.assertEqual(expected, actual)
