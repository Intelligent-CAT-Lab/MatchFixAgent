from __future__ import annotations
import re
import random
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16OutputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"

    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        bout = io.BytesIO()
        try:
            out = Base16OutputStream.Base16OutputStream3(bout)
            out.write0(None, 0, 0)
            self.fail("Expected Base16OutputStream.write0(None) to throw a ValueError")
        except ValueError as e:
            self.assertEqual(str(e), "array cannot be None")

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        buf = bytearray(1024)
        bout = io.BytesIO()
        out = Base16OutputStream.Base16OutputStream3(bout)

        with self.assertRaises(IndexError, msg="offset or length cannot be negative"):
            out.write0(buf, -1, 1)

        with self.assertRaises(IndexError, msg="offset or length cannot be negative"):
            out.write0(buf, 1, -1)

        with self.assertRaises(IndexError, msg="offset and length exceed array bounds"):
            out.write0(buf, len(buf) + 1, 0)

        with self.assertRaises(IndexError, msg="offset and length exceed array bounds"):
            out.write0(buf, len(buf) - 1, 2)

    def testBase16OutputStreamByteByByte_test5_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByteByByte0(encoded, decoded)

        codec = Base16.Base161(True)
        for i in range(151):  # Loop from 0 to 150 inclusive
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByteByByte1(encoded, decoded, True)

    def testBase16OutputStreamByteByByte_test4_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByteByByte0(encoded, decoded)

        codec = Base16.Base161(True)

    def testBase16OutputStreamByteByByte_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)
        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByteByByte0(encoded, decoded)

    def testBase16OutputStreamByteByByte_test2_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)
        encoded = StringUtils.getBytesUtf8("41")

    def testBase16OutputStreamByteByByte_test1_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)

    def testBase16OutputStreamByteByByte_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase16OutputStreamByChunk_test5_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByChunk0(encoded, decoded)

        codec = Base16.Base161(True)
        for i in range(151):  # Loop from 0 to 150 inclusive
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByChunk1(encoded, decoded, True)

    def testBase16OutputStreamByChunk_test4_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByChunk0(encoded, decoded)

        codec = Base16.Base161(True)

    def testBase16OutputStreamByChunk_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByChunk0(encoded, decoded)

    def testBase16OutputStreamByChunk_test2_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)
        encoded = StringUtils.getBytesUtf8("41")

    def testBase16OutputStreamByChunk_test1_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)

    def testBase16OutputStreamByChunk_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase16EmptyOutputStream_test1_decomposed(self) -> None:
        empty_encoded = []
        empty_decoded = []
        self.__testByteByByte0(empty_encoded, empty_decoded)
        self.__testByChunk0(empty_encoded, empty_decoded)

    def testBase16EmptyOutputStream_test0_decomposed(self) -> None:
        empty_encoded: List[int] = []
        empty_decoded: List[int] = []
        self.__testByteByByte0(empty_encoded, empty_decoded)

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        # Test encoding byte-by-byte
        with io.BytesIO() as byteOut:
            out = Base16OutputStream.Base16OutputStream1(byteOut, True, lowerCase)
            try:
                for element in decoded:
                    out.write(bytes([element]))
            finally:
                out.close()
            output = byteOut.getvalue()
            self.assertEqual(
                bytes(encoded), output, "Streaming byte-by-byte base16 encode"
            )

        # Test decoding byte-by-byte
        with io.BytesIO() as byteOut:
            out = Base16OutputStream.Base16OutputStream1(byteOut, False, lowerCase)
            try:
                for element in encoded:
                    out.write(bytes([element]))
            finally:
                out.close()
            output = byteOut.getvalue()
            self.assertEqual(
                bytes(decoded), output, "Streaming byte-by-byte base16 decode"
            )

        # Test decoding with flush
        with io.BytesIO() as byteOut:
            out = Base16OutputStream.Base16OutputStream1(byteOut, False, lowerCase)
            try:
                for element in encoded:
                    out.write(bytes([element]))
                    out.flush()
            finally:
                out.close()
            output = byteOut.getvalue()
            self.assertEqual(
                bytes(decoded), output, "Streaming byte-by-byte flush() base16 decode"
            )

        # Test wrap-wrap encoding and decoding
        with io.BytesIO() as byteOut:
            decoderOut = Base16OutputStream.Base16OutputStream1(
                byteOut, False, lowerCase
            )
            encoderOut = Base16OutputStream.Base16OutputStream1(
                decoderOut, True, lowerCase
            )
            try:
                for element in decoded:
                    encoderOut.write(bytes([element]))
            finally:
                encoderOut.close()
                decoderOut.close()
            output = byteOut.getvalue()
            self.assertEqual(
                bytes(decoded), output, "Streaming byte-by-byte base16 wrap-wrap!"
            )

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        # First try block: Encoding
        byteOut = io.BytesIO()
        out = Base16OutputStream.Base16OutputStream1(byteOut, True, lowerCase)
        try:
            out.write(bytearray(decoded))
        finally:
            out.close()
        output = byteOut.getvalue()
        self.assertEqual(list(encoded), list(output), "Streaming chunked base16 encode")

        # Second try block: Decoding
        byteOut = io.BytesIO()
        out = Base16OutputStream.Base16OutputStream1(byteOut, False, lowerCase)
        try:
            out.write(bytearray(encoded))
        finally:
            out.close()
        output = byteOut.getvalue()
        self.assertEqual(list(decoded), list(output), "Streaming chunked base16 decode")

        # Third try block: Wrap-wrap
        byteOut = io.BytesIO()
        decoderOut = Base16OutputStream.Base16OutputStream1(byteOut, False, lowerCase)
        encoderOut = Base16OutputStream.Base16OutputStream1(decoderOut, True, lowerCase)
        try:
            encoderOut.write(bytearray(decoded))
        finally:
            encoderOut.close()
        output = byteOut.getvalue()
        self.assertEqual(
            list(decoded), list(output), "Streaming chunked base16 wrap-wrap!"
        )

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByChunk1(encoded, decoded, False)
