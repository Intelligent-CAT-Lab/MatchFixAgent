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
from src.main.org.apache.commons.codec.binary.Base32InputStream import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [ord("\n")]
    __CRLF: typing.List[int] = [ord("\r"), ord("\n")]
    __ENCODED_FOO: str = "MZXW6==="

    def testSkipWrongArgument_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with pytest.raises(ValueError, match="Negative skip length: -10"):
            b32stream = Base32InputStream.Base32InputStream0(ins)
            try:
                b32stream.skip(-10)
            finally:
                b32stream.close()

    def testSkipWrongArgument_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testSkipToEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(3), "Failed to skip 3 bytes")
            self.assertEqual(
                -1, b32stream.read0(), "Expected EOF after skipping to the end"
            )
            self.assertEqual(-1, b32stream.read0(), "Expected EOF on subsequent read")

    def testSkipToEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testSkipPastEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(10), "Expected to skip 3 bytes")
            self.assertEqual(
                -1,
                b32stream.read0(),
                "Expected end of stream (-1) after skipping past end",
            )
            self.assertEqual(
                -1, b32stream.read0(), "Expected end of stream (-1) on subsequent read"
            )

    def testSkipPastEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testSkipBig_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(1024))
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())

    def testSkipBig_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testSkipNone_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            actualBytes = bytearray(6)
            self.assertEqual(0, b32stream.skip(0))
            b32stream.read1(actualBytes, 0, len(actualBytes))
            self.assertListEqual(list(actualBytes), [102, 111, 111, 0, 0, 0])
            self.assertEqual(-1, b32stream.read0())

    def testSkipNone_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testReadOutOfBounds_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = bytearray(1024)
        bin_ = io.BytesIO(bytes(decoded))
        with Base32InputStream.Base32InputStream2(bin_, True, 4, [0, 0, 0]) as in_:

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
        decoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testReadNull_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin_stream = io.BytesIO(bytearray(decoded))
        with Base32InputStream.Base32InputStream2(
            bin_stream, True, 4, [0, 0, 0]
        ) as in_stream:
            with self.assertRaises(ValueError, msg="array cannot be None"):
                in_stream.read1(None, 0, 0)

    def testReadNull_test0_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testRead0_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = bytearray(1024)
        bin_stream = io.BytesIO(bytearray(decoded))

        with Base32InputStream.Base32InputStream2(
            bin_stream, True, 4, [0, 0, 0]
        ) as in_stream:
            bytes_read = in_stream.read1(buf, 0, 0)
            self.assertEqual(
                0, bytes_read, "Base32InputStream.read(buf, 0, 0) returns 0"
            )

    def testRead0_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testMarkSupported_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin = io.BytesIO(bytes(decoded))
        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as in_stream:
            self.assertFalse(
                in_stream.markSupported(), "Base32InputStream.markSupported() is false"
            )

    def testMarkSupported_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)

    def testBase32EmptyInputStreamPemChuckSize_test0_decomposed(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyInputStreamMimeChuckSize_test0_decomposed(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(
                1, b32stream.available(), "Initial available bytes should be 1"
            )
            self.assertEqual(3, b32stream.skip(10), "Skipped bytes should be 3")
            self.assertEqual(
                0, b32stream.available(), "Available bytes should be 0 after skip"
            )
            self.assertEqual(-1, b32stream.read0(), "Read should return -1 at EOF")
            self.assertEqual(
                -1, b32stream.read0(), "Read should return -1 at EOF again"
            )
            self.assertEqual(
                0, b32stream.available(), "Available bytes should remain 0 at EOF"
            )

    def testAvailable_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

    def testCodec105_test0_decomposed(self) -> None:
        with Base32InputStream.Base32InputStream2(
            Codec105ErrorInputStream(), True, 0, None
        ) as in_stream:
            for _ in range(5):
                in_stream.read0()

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # Test encoding
        in_stream = Base32InputStream.Base32InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output = bytearray(len(encoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(list(encoded), list(output), "Streaming base32 encode")

        in_stream.close()

        # Test decoding
        in_stream = Base32InputStream.Base32InputStream0(io.BytesIO(encoded))
        output = bytearray(len(decoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(list(decoded), list(output), "Streaming base32 decode")

        in_stream.close()

        # Test wrapping multiple times
        in_stream = io.BytesIO(decoded)
        for _ in range(10):
            in_stream = Base32InputStream.Base32InputStream2(
                in_stream, True, chunkSize, separator
            )
            in_stream = Base32InputStream.Base32InputStream1(in_stream, False)

        output = bytearray(len(decoded))
        for i in range(len(output)):
            output[i] = in_stream.read(1)[0]

        self.assertEqual(-1, in_stream.read(1), "EOF")
        self.assertEqual(-1, in_stream.read(1), "Still EOF")
        self.assertEqual(
            list(decoded), list(output), "Streaming base32 wrap-wrap-wrap!"
        )

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        # Create an input stream for encoding
        in_stream = Base32InputStream.Base32InputStream2(
            io.BytesIO(bytearray(decoded)), True, chunkSize, separator
        )
        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(encoded, output, "Streaming base32 encode")

        # Create an input stream for decoding
        in_stream = Base32InputStream.Base32InputStream0(io.BytesIO(bytearray(encoded)))
        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base32 decode")

        # Wrap the input stream multiple times
        in_stream = io.BytesIO(bytearray(decoded))
        for _ in range(10):
            in_stream = Base32InputStream.Base32InputStream2(
                in_stream, True, chunkSize, separator
            )
            in_stream = Base32InputStream.Base32InputStream1(in_stream, False)

        output = BaseNTestData.streamToBytes0(in_stream)

        # Assert EOF after reading
        self.assertEqual(-1, in_stream.read(), "EOF")
        self.assertEqual(-1, in_stream.read(), "Still EOF")
        self.assertListEqual(decoded, output, "Streaming base32 wrap-wrap-wrap!")

        # Close the stream
        in_stream.close()

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:
        empty_encoded: typing.List[int] = []
        empty_decoded: typing.List[int] = []
        self.__testByteByByte(empty_encoded, empty_decoded, chuckSize, self.__CRLF)
        self.__testByChunk(empty_encoded, empty_decoded, chuckSize, self.__CRLF)
