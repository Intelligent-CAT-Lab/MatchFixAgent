from __future__ import annotations
import time
import re
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.binary.Base64InputStream import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [10]
    __CRLF: typing.List[int] = [13, 10]
    __ENCODED_B64: str = "AAAA////"

    def testSkipWrongArgument_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            with self.assertRaises(ValueError) as context:
                b64stream.skip(-10)
            self.assertEqual(str(context.exception), "Negative skip length: -10")

    def testSkipWrongArgument_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testSkipToEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(6), "Failed to skip 6 bytes")
            self.assertEqual(
                -1, b64stream.read0(), "Expected end of stream (-1) after skipping"
            )
            self.assertEqual(
                -1, b64stream.read0(), "Expected end of stream (-1) on subsequent read"
            )

    def testSkipToEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testSkipPastEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(10), "Expected to skip 6 bytes")
            self.assertEqual(
                -1, b64stream.read0(), "Expected EOF (-1) after skipping past end"
            )
            self.assertEqual(
                -1, b64stream.read0(), "Expected EOF (-1) on subsequent read"
            )

    def testSkipPastEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testSkipNone_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            actual_bytes = bytearray(6)
            self.assertEqual(0, b64stream.skip(0))
            b64stream.read1(actual_bytes, 0, len(actual_bytes))
            self.assertListEqual(list(actual_bytes), [0, 0, 0, 255, 255, 255])
            self.assertEqual(-1, b64stream.read0())

    def testSkipNone_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testSkipBig_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(2147483647), "Expected to skip 6 bytes")
            self.assertEqual(
                -1, b64stream.read0(), "Expected end of stream (-1) after skipping"
            )
            self.assertEqual(
                -1, b64stream.read0(), "Expected end of stream (-1) on subsequent read"
            )

    def testSkipBig_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testReadOutOfBounds_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = [0] * 1024
        bin_ = io.BytesIO(bytes(decoded))
        with Base64InputStream.Base64InputStream2(bin_, True, 4, [0, 0, 0]) as in_:

            with self.assertRaises(IndexError, msg="offset or len_ cannot be negative"):
                in_.read1(buf, -1, 0)

            with self.assertRaises(IndexError, msg="offset or len_ cannot be negative"):
                in_.read1(buf, 0, -1)

            with self.assertRaises(
                IndexError, msg="offset + len_ exceeds array length"
            ):
                in_.read1(buf, len(buf) + 1, 0)

            with self.assertRaises(
                IndexError, msg="offset + len_ exceeds array length"
            ):
                in_.read1(buf, len(buf) - 1, 2)

    def testReadOutOfBounds_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testReadNull_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin_stream = io.BytesIO(bytearray(decoded))
        with pytest.raises(ValueError, match="array cannot be None"):
            with Base64InputStream.Base64InputStream2(
                bin_stream, True, 4, [0, 0, 0]
            ) as in_stream:
                in_stream.read1(None, 0, 0)

    def testReadNull_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testRead0_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bytes_read = 0
        bin_ = io.BytesIO(bytearray(decoded))

        with Base64InputStream.Base64InputStream2(bin_, True, 4, [0, 0, 0]) as in_:
            bytes_read = in_.read1(buf, 0, 0)
            self.assertEqual(
                0, bytes_read, "Base64InputStream.read(buf, 0, 0) returns 0"
            )

    def testRead0_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testMarkSupported_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(bytearray(decoded))
        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            self.assertFalse(
                in_.markSupported(), "Base64InputStream.markSupported() is false"
            )

    def testMarkSupported_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase64EmptyInputStreamPemChuckSize_test0_decomposed(self) -> None:
        self.__testBase64EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase64EmptyInputStreamMimeChuckSize_test0_decomposed(self) -> None:
        self.__testBase64EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(
                1, b64stream.available(), "Initial available bytes should be 1"
            )
            self.assertEqual(6, b64stream.skip(10), "Skipped bytes should be 6")
            self.assertEqual(
                0, b64stream.available(), "Available bytes after skip should be 0"
            )
            self.assertEqual(
                -1,
                b64stream.read0(),
                "Read should return -1 when no more data is available",
            )
            self.assertEqual(
                -1,
                b64stream.read0(),
                "Read should return -1 when no more data is available",
            )
            self.assertEqual(
                0,
                b64stream.available(),
                "Available bytes should remain 0 after reading",
            )

    def testAvailable_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))

    def testInputStreamReader_test2_decomposed(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(bytes(codec101))
        in_ = Base64InputStream.Base64InputStream0(bais)
        isr = io.TextIOWrapper(in_, encoding="utf-8")
        with io.BufferedReader(isr) as br:
            line = br.readline()
            self.assertIsNotNone(line, "Codec101: InputStreamReader works!")

    def testInputStreamReader_test1_decomposed(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(bytes(codec101))
        in_ = Base64InputStream.Base64InputStream0(bais)

    def testInputStreamReader_test0_decomposed(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )

    def testCodec101_test1_decomposed(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(bytes(codec101))
        with Base64InputStream.Base64InputStream0(bais) as in_:
            result = bytearray(8192)
            c = in_.readinto(result)
            self.assertTrue(c > 0, f"Codec101: First read successful [c={c}]")

            c = in_.readinto(result)
            self.assertTrue(
                c < 0, f"Codec101: Second read should report end-of-stream [c={c}]"
            )

    def testCodec101_test0_decomposed(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )

    def testCodec105_test0_decomposed(self) -> None:
        with Base64InputStream.Base64InputStream2(
            Codec105ErrorInputStream(), True, 0, None
        ) as in_:
            for _ in range(5):
                in_.read0()

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # First test: Streaming base64 encode
        in_stream = Base64InputStream.Base64InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output = bytearray(len(encoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(encoded, list(output), "Streaming base64 encode")

        in_stream.close()

        # Second test: Streaming base64 decode
        in_stream = Base64InputStream.Base64InputStream0(io.BytesIO(encoded))
        output = bytearray(len(decoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(decoded, list(output), "Streaming base64 decode")

        in_stream.close()

        # Third test: Wrap-wrap-wrap
        in_stream = io.BytesIO(decoded)
        for _ in range(10):
            in_stream = Base64InputStream.Base64InputStream2(
                in_stream, True, chunkSize, separator
            )
            in_stream = Base64InputStream.Base64InputStream1(in_stream, False)

        output = bytearray(len(decoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(decoded, list(output), "Streaming base64 wrap-wrap-wrap!")

        in_stream.close()

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # Create an input stream for encoding
        in_stream = Base64InputStream.Base64InputStream2(
            io.BytesIO(bytearray(decoded)), True, chunkSize, separator
        )
        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(encoded, output, "Streaming base64 encode")

        in_stream.close()

        # Create an input stream for decoding
        in_stream = Base64InputStream.Base64InputStream0(io.BytesIO(bytearray(encoded)))
        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base64 decode")

        # Wrap the input stream multiple times
        in_stream = io.BytesIO(bytearray(decoded))
        for _ in range(10):
            in_stream = Base64InputStream.Base64InputStream2(
                in_stream, True, chunkSize, separator
            )
            in_stream = Base64InputStream.Base64InputStream1(in_stream, False)

        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base64 wrap-wrap-wrap!")

        in_stream.close()

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
