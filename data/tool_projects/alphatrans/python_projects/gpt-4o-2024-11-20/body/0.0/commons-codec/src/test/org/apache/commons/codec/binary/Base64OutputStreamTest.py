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
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.Base64OutputStream import *
from src.test.org.apache.commons.codec.binary.Base64Test import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64OutputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [ord("\n")]
    __CR_LF: typing.List[int] = [ord("\r"), ord("\n")]

    def testStrictDecoding_test0_decomposed(self) -> None:
        for s in Base64Test.BASE64_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)

            # Test with non-strict decoding
            bout = io.BytesIO()
            out = Base64OutputStream.Base64OutputStream1(bout, False)
            self.assertFalse(out.isStrictDecoding())
            out.write(bytearray(encoded))
            out.close()
            self.assertTrue(len(bout.getvalue()) > 0)

            # Test with strict decoding
            bout = io.BytesIO()
            out = Base64OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
            self.assertTrue(out.isStrictDecoding())
            with self.assertRaises(ValueError):
                out.write(bytearray(encoded))
                out.close()

    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        bout = io.BytesIO()
        with self.assertRaises(ValueError, msg="array cannot be None"):
            with Base64OutputStream.Base64OutputStream0(bout) as out:
                out.write0(None, 0, 0)

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        buf = bytearray(1024)
        bout = io.BytesIO()
        with Base64OutputStream.Base64OutputStream0(bout) as out:
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

    def testBase64OutputStreamByteByByte_test9_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)
        for i in range(151):
            random_data = Base64.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase64OutputStreamByteByByte_test8_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)

    def testBase64OutputStreamByteByByte_test7_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase64OutputStreamByteByByte_test6_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)

    def testBase64OutputStreamByteByByte_test5_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

    def testBase64OutputStreamByteByByte_test4_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)

    def testBase64OutputStreamByteByByte_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

    def testBase64OutputStreamByteByByte_test2_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)
        encoded = StringUtils.getBytesUtf8("AA==\r\n")

    def testBase64OutputStreamByteByByte_test1_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

    def testBase64OutputStreamByteByByte_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase64OutputStreamByChunk_test9_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)
        for i in range(151):
            random_data = Base64.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByChunk(encoded, decoded, 0, self.__LF)

    def testBase64OutputStreamByChunk_test8_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)

    def testBase64OutputStreamByChunk_test7_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, 0, self.__LF)

    def testBase64OutputStreamByChunk_test6_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)

    def testBase64OutputStreamByChunk_test5_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

    def testBase64OutputStreamByChunk_test4_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)

    def testBase64OutputStreamByChunk_test3_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

    def testBase64OutputStreamByChunk_test2_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)
        encoded = StringUtils.getBytesUtf8("AA==\r\n")

    def testBase64OutputStreamByChunk_test1_decomposed(self) -> None:
        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

    def testBase64OutputStreamByChunk_test0_decomposed(self) -> None:
        encoded: List[int] = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase64EmptyOutputStreamPemChunkSize_test0_decomposed(self) -> None:
        self.__testBase64EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase64EmptyOutputStreamMimeChunkSize_test0_decomposed(self) -> None:
        self.__testBase64EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testCodec98NPE_test4_decomposed(self) -> None:
        codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)
        codec98_1024 = bytearray(1024)
        codec98_1024[: len(codec98)] = codec98
        data = io.BytesIO()
        with Base64OutputStream.Base64OutputStream1(data, False) as stream:
            stream.write0(codec98_1024, 0, 1024)
        decodedBytes = data.getvalue()
        decoded = StringUtils.newStringUtf8(list(decodedBytes))
        self.assertEqual(
            "codec-98 NPE Base64OutputStream",
            Base64TestData.CODEC_98_NPE_DECODED,
            decoded,
        )

    def testCodec98NPE_test3_decomposed(self) -> None:
        codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)
        codec98_1024 = [0] * 1024
        codec98_1024[: len(codec98)] = codec98
        data = io.BytesIO()
        with Base64OutputStream.Base64OutputStream1(data, False) as stream:
            stream.write0(codec98_1024, 0, 1024)
        decodedBytes = data.getvalue()
        decoded = StringUtils.newStringUtf8(decodedBytes)

    def testCodec98NPE_test2_decomposed(self) -> None:
        codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)
        codec98_1024 = bytearray(1024)
        codec98_1024[: len(codec98)] = codec98
        data = io.BytesIO()
        with Base64OutputStream.Base64OutputStream1(data, False) as stream:
            stream.write0(codec98_1024, 0, 1024)
        decoded_bytes = data.getvalue()

    def testCodec98NPE_test1_decomposed(self) -> None:
        codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)
        codec98_1024 = bytearray(1024)
        codec98_1024[: len(codec98)] = codec98
        data = io.BytesIO()
        stream = Base64OutputStream.Base64OutputStream1(data, False)
        try:
            stream.write0(codec98_1024, 0, 1024)
        finally:
            stream.close()

    def testCodec98NPE_test0_decomposed(self) -> None:
        codec98: List[int] = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        byte_out = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream2(
            byte_out, True, chunkSize, separator
        )
        for element in decoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(encoded, list(output), "Streaming byte-by-byte base64 encode")

        byte_out = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byte_out, False)
        for element in encoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(decoded, list(output), "Streaming byte-by-byte base64 decode")

        byte_out = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byte_out, False)
        for element in encoded:
            out.write(bytes([element]))
            out.flush()
        out.close()
        output = byte_out.getvalue()
        self.assertEqual(
            decoded, list(output), "Streaming byte-by-byte flush() base64 decode"
        )

        byte_out = io.BytesIO()
        out = byte_out
        for _ in range(10):
            out = Base64OutputStream.Base64OutputStream1(out, False)
            out = Base64OutputStream.Base64OutputStream2(
                out, True, chunkSize, separator
            )
        for element in decoded:
            out.write(bytes([element]))
        out.close()
        output = byte_out.getvalue()

        self.assertEqual(
            decoded, list(output), "Streaming byte-by-byte base64 wrap-wrap-wrap!"
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

        # Create a Base64OutputStream for encoding
        out = Base64OutputStream.Base64OutputStream2(
            byte_out, True, chunkSize, separator
        )
        out.write(bytes(decoded))  # Write the decoded bytes
        out.close()
        output = byte_out.getvalue()  # Get the encoded output
        self.assertEqual(encoded, list(output), "Streaming chunked base64 encode")

        # Reset ByteArrayOutputStream for decoding
        byte_out = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byte_out, False)
        out.write(bytes(encoded))  # Write the encoded bytes
        out.close()
        output = byte_out.getvalue()  # Get the decoded output
        self.assertEqual(decoded, list(output), "Streaming chunked base64 decode")

        # Test wrap-wrap-wrap scenario
        byte_out = io.BytesIO()
        out = byte_out
        for _ in range(10):
            out = Base64OutputStream.Base64OutputStream1(out, False)
            out = Base64OutputStream.Base64OutputStream2(
                out, True, chunkSize, separator
            )
        out.write(bytes(decoded))  # Write the decoded bytes
        out.close()
        output = byte_out.getvalue()  # Get the final output
        self.assertEqual(
            decoded, list(output), "Streaming chunked base64 wrap-wrap-wrap!"
        )

    def __testBase64EmptyOutputStream(self, chunkSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
