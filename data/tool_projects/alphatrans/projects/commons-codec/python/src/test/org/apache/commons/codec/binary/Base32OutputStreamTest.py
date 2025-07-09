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
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.Base32OutputStream import *
from src.test.org.apache.commons.codec.binary.Base32Test import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32OutputStreamTest(unittest.TestCase):

    __LF: typing.List[int] = [ord("\n")]
    __CR_LF: typing.List[int] = [ord("\r"), ord("\n")]

    def testStrictDecoding_test0_decomposed(self) -> None:
        for s in Base32Test.BASE32_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)

            # Test with non-strict decoding
            bout = io.BytesIO()
            out = Base32OutputStream.Base32OutputStream1(bout, False)
            self.assertFalse(out.isStrictDecoding())
            out.write(bytearray(encoded))
            out.close()
            self.assertTrue(len(bout.getvalue()) > 0)

            # Test with strict decoding
            bout = io.BytesIO()
            out = Base32OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
            self.assertTrue(out.isStrictDecoding())
            with self.assertRaises(ValueError):
                out.write(bytearray(encoded))
                out.close()

    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        bout = io.BytesIO()
        with self.assertRaises(ValueError, msg="array cannot be None"):
            with Base32OutputStream.Base32OutputStream0(bout) as out:
                out.write0(None, 0, 0)

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        buf = bytearray(1024)
        bout = io.BytesIO()
        with Base32OutputStream.Base32OutputStream0(bout) as out:
            # Test case 1: Negative offset
            with self.assertRaises(
                IndexError, msg="offset or length cannot be negative"
            ):
                out.write0(buf, -1, 1)

            # Test case 2: Negative length
            with self.assertRaises(
                IndexError, msg="offset or length cannot be negative"
            ):
                out.write0(buf, 1, -1)

            # Test case 3: Offset exceeds buffer length
            with self.assertRaises(
                IndexError, msg="offset and length exceed array bounds"
            ):
                out.write0(buf, len(buf) + 1, 0)

            # Test case 4: Offset + length exceeds buffer length
            with self.assertRaises(
                IndexError, msg="offset and length exceed array bounds"
            ):
                out.write0(buf, len(buf) - 1, 2)

    def testBase32OutputStreamByteByByte_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        codec = Base32.Base320()
        for i in range(151):  # Loop from 0 to 150 inclusive
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase32OutputStreamByteByByte_test2_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)
        codec = Base32.Base320()

    def testBase32OutputStreamByteByByte_test1_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

    def testBase32OutputStreamByteByByte_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testBase32OutputStreamByChunk_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        codec = Base32.Base320()
        for i in range(151):  # Loop from 0 to 150 inclusive
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByChunk(encoded, decoded, 0, self.__LF)

    def testBase32OutputStreamByChunk_test2_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)
        codec = Base32.Base320()

    def testBase32OutputStreamByChunk_test1_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

    def testBase32OutputStreamByChunk_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testBase32EmptyOutputStreamPemChunkSize_test0_decomposed(self) -> None:
        self.__testBase32EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyOutputStreamMimeChunkSize_test0_decomposed(self) -> None:
        self.__testBase32EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # Test Base32 encoding byte-by-byte
        byte_out = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream2(
            byte_out, True, chunkSize, separator
        )
        for element in decoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(encoded, list(output), "Streaming byte-by-byte Base32 encode")

        # Test Base32 decoding byte-by-byte
        byte_out = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byte_out, False)
        for element in encoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(decoded, list(output), "Streaming byte-by-byte Base32 decode")

        # Test Base32 decoding with flush() byte-by-byte
        byte_out = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byte_out, False)
        for element in encoded:
            out.write(bytes([element]))
            out.flush()
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(
            decoded, list(output), "Streaming byte-by-byte flush() Base32 decode"
        )

        # Test Base32 wrap-wrap-wrap encoding and decoding
        byte_out = io.BytesIO()
        out = byte_out
        for _ in range(10):
            out = Base32OutputStream.Base32OutputStream1(out, False)
            out = Base32OutputStream.Base32OutputStream2(
                out, True, chunkSize, separator
            )
        for element in decoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(
            decoded, list(output), "Streaming byte-by-byte Base32 wrap-wrap-wrap!"
        )

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # Create a ByteArrayOutputStream equivalent
        byte_out = io.BytesIO()

        # Create a Base32OutputStream for encoding
        out = Base32OutputStream.Base32OutputStream2(
            byte_out, True, chunkSize, separator
        )
        out.write(decoded)
        out.close()

        # Get the output bytes
        output = byte_out.getvalue()
        self.assertEqual(encoded, list(output), "Streaming chunked Base32 encode")

        # Reset ByteArrayOutputStream for decoding
        byte_out = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byte_out, False)
        out.write(encoded)
        out.close()

        # Get the output bytes
        output = byte_out.getvalue()
        self.assertEqual(decoded, list(output), "Streaming chunked Base32 decode")

        # Test wrap-wrap-wrap scenario
        byte_out = io.BytesIO()
        out = byte_out
        for _ in range(10):
            out = Base32OutputStream.Base32OutputStream1(out, False)
            out = Base32OutputStream.Base32OutputStream2(
                out, True, chunkSize, separator
            )

        out.write(decoded)
        out.close()

        # Get the output bytes
        output = byte_out.getvalue()
        self.assertEqual(
            decoded, list(output), "Streaming chunked Base32 wrap-wrap-wrap!"
        )

    def __testBase32EmptyOutputStream(self, chunkSize: int) -> None:
        empty_encoded: typing.List[int] = []
        empty_decoded: typing.List[int] = []
        self.__testByteByByte(empty_encoded, empty_decoded, chunkSize, self.__CR_LF)
        self.__testByChunk(empty_encoded, empty_decoded, chunkSize, self.__CR_LF)
