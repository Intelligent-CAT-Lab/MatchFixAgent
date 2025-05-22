from __future__ import annotations
import re
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.binary.Base16InputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __ENCODED_B16: str = "CAFEBABEFFFF"

    def testSkipWrongArgument_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            with self.assertRaises(ValueError) as context:
                b16Stream.skip(-10)
            self.assertEqual(str(context.exception), "Negative skip length: -10")

    def testSkipWrongArgument_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def testSkipToEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(
                6, b16Stream.skip(6), "Failed to skip the correct number of bytes"
            )
            self.assertEqual(
                -1, b16Stream.read0(), "Expected end of stream (-1) after skipping"
            )
            self.assertEqual(
                -1, b16Stream.read0(), "Expected end of stream (-1) on subsequent read"
            )

    def testSkipToEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def testSkipPastEnd_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(10), "Expected to skip 6 bytes")
            self.assertEqual(
                -1, b16Stream.read0(), "Expected to read -1 after skipping past end"
            )
            self.assertEqual(
                -1,
                b16Stream.read0(),
                "Expected to read -1 again after skipping past end",
            )

    def testSkipPastEnd_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def testSkipNone_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            actualBytes = bytearray(6)
            self.assertEqual(0, b16Stream.skip(0))
            b16Stream.read1(actualBytes, 0, len(actualBytes))
            self.assertListEqual(
                list(actualBytes),
                [202, 254, 186, 190, 255, 255],
                "The actual bytes do not match the expected bytes",
            )
            self.assertEqual(
                -1, b16Stream.read0(), "Expected EOF (-1) after reading all bytes"
            )

    def testSkipNone_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def testSkipBig_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(
                6, b16Stream.skip(2147483647)
            )  # Corrected from float('inf') to 2147483647
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testSkipBig_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def testReadOutOfBounds_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = [0] * 1024
        bin_ = io.BytesIO(bytes(decoded))

        with Base16InputStream.Base16InputStream2(bin_, True) as in_:
            # Test case 1: Negative offset
            with self.assertRaises(IndexError, msg="offset or len_ cannot be negative"):
                in_.read1(buf, -1, 0)

            # Test case 2: Negative length
            with self.assertRaises(IndexError, msg="offset or len_ cannot be negative"):
                in_.read1(buf, 0, -1)

            # Test case 3: Offset exceeds buffer length
            with self.assertRaises(
                IndexError, msg="offset + len_ exceeds array length"
            ):
                in_.read1(buf, len(buf) + 1, 0)

            # Test case 4: Offset + length exceeds buffer length
            with self.assertRaises(
                IndexError, msg="offset + len_ exceeds array length"
            ):
                in_.read1(buf, len(buf) - 1, 2)

    def testReadOutOfBounds_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testReadNull_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin_ = io.BytesIO(bytearray(decoded))
        with pytest.raises(ValueError, match="array cannot be None"):
            with Base16InputStream.Base16InputStream2(bin_, True) as in_:
                in_.read1(None, 0, 0)

    def testReadNull_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testRead0_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)  # Create a buffer of size 1024
        bin_stream = io.BytesIO(
            bytearray(decoded)
        )  # Create a ByteArrayInputStream equivalent

        with Base16InputStream.Base16InputStream2(bin_stream, True) as in_stream:
            bytes_read = in_stream.read1(buf, 0, 0)
            self.assertEqual(
                0, bytes_read, "Base16InputStream.read(buf, 0, 0) returns 0"
            )

    def testRead0_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testMarkSupported_test1_decomposed(self) -> None:
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(bytearray(decoded))
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            self.assertFalse(
                in_.markSupported(), "Base16InputStream.markSupported() is false"
            )

    def testMarkSupported_test0_decomposed(self) -> None:
        decoded: List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)

    def testBase16EmptyInputStream_test1_decomposed(self) -> None:
        empty_encoded: List[int] = []
        empty_decoded: List[int] = []
        self.__testByteByByte0(empty_encoded, empty_decoded)
        self.__testByChunk0(empty_encoded, empty_decoded)

    def testBase16EmptyInputStream_test0_decomposed(self) -> None:
        empty_encoded = []
        empty_decoded = []
        self.__testByteByByte0(empty_encoded, empty_decoded)

    def testAvailable_test1_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(
                1, b16Stream.available(), "Initial available bytes should be 1"
            )
            self.assertEqual(6, b16Stream.skip(10), "Skipped bytes should be 6")
            self.assertEqual(
                0, b16Stream.available(), "Available bytes after skip should be 0"
            )
            self.assertEqual(
                -1,
                b16Stream.read0(),
                "Read should return -1 when no bytes are available",
            )
            self.assertEqual(
                -1,
                b16Stream.read0(),
                "Read should return -1 when no bytes are available",
            )
            self.assertEqual(
                0,
                b16Stream.available(),
                "Available bytes should remain 0 after reading",
            )

    def testAvailable_test0_decomposed(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        # Test encoding
        with Base16InputStream(
            io.BytesIO(decoded), doEncode=True, lowerCase=lowerCase
        ) as in_stream:
            output = bytearray(len(encoded))
            for i in range(len(output)):
                output[i] = in_stream.read()

            self.assertEqual(-1, in_stream.read(), "EOF")
            self.assertEqual(-1, in_stream.read(), "Still EOF")
            self.assertEqual(list(encoded), list(output), "Streaming Base16 encode")

        # Test decoding
        with Base16InputStream(
            io.BytesIO(encoded), doEncode=False, lowerCase=lowerCase
        ) as in_stream:
            output = bytearray(len(decoded))
            for i in range(len(output)):
                output[i] = in_stream.read()

            self.assertEqual(-1, in_stream.read(), "EOF")
            self.assertEqual(-1, in_stream.read(), "Still EOF")
            self.assertEqual(list(decoded), list(output), "Streaming Base16 decode")

        # Test wrap-wrap (encode and decode)
        with io.BytesIO(decoded) as in_stream, Base16InputStream(
            in_stream, doEncode=True, lowerCase=lowerCase
        ) as in_encode, Base16InputStream(
            in_encode, doEncode=False, lowerCase=lowerCase
        ) as in_decode:

            output = bytearray(len(decoded))
            for i in range(len(output)):
                output[i] = in_decode.read()

            self.assertEqual(-1, in_decode.read(), "EOF")
            self.assertEqual(-1, in_decode.read(), "Still EOF")
            self.assertEqual(list(decoded), list(output), "Streaming Base16 wrap-wrap!")

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        # First try block: Encoding
        with Base16InputStream(
            io.BytesIO(bytes(decoded)), doEncode=True, lowerCase=lowerCase
        ) as in_stream:
            output = BaseNTestData.streamToBytes0(in_stream)
            self.assertEqual(-1, in_stream.read(), "EOF")
            self.assertEqual(-1, in_stream.read(), "Still EOF")
            self.assertEqual(encoded, output, "Streaming Base16 encode")

        # Second try block: Decoding
        with Base16InputStream(
            io.BytesIO(bytes(encoded)), doEncode=False, lowerCase=lowerCase
        ) as in_stream:
            output = BaseNTestData.streamToBytes0(in_stream)
            self.assertEqual(-1, in_stream.read(), "EOF")
            self.assertEqual(-1, in_stream.read(), "Still EOF")
            self.assertEqual(decoded, output, "Streaming Base16 decode")

        # Third try block: Wrap-wrap (encode and decode)
        with io.BytesIO(bytes(decoded)) as in_stream, Base16InputStream(
            in_stream, doEncode=True, lowerCase=lowerCase
        ) as in_encode_stream, Base16InputStream(
            in_encode_stream, doEncode=False, lowerCase=lowerCase
        ) as in_decode_stream:
            output = BaseNTestData.streamToBytes0(in_decode_stream)
            self.assertEqual(-1, in_decode_stream.read(), "EOF")
            self.assertEqual(-1, in_decode_stream.read(), "Still EOF")
            self.assertEqual(decoded, output, "Streaming Base16 wrap-wrap!")

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByChunk1(encoded, decoded, False)
