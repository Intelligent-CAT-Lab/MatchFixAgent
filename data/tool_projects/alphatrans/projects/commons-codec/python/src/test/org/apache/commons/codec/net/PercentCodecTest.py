from __future__ import annotations
import re
from abc import ABC
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.net.PercentCodec import *


class PercentCodecTest(unittest.TestCase):

    def testUnsafeCharEncodeDecode_test5_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6% "
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)
        encoded_str = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_str = decoded.decode("utf-8")
        self.assertEqual(
            "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 ",
            encoded_str,
            "Basic PercentCodec unsafe char encoding test",
        )
        self.assertEqual(
            input_str, decoded_str, "Basic PercentCodec unsafe char decoding test"
        )

    def testUnsafeCharEncodeDecode_test4_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6% "
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)
        encoded_str = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_str = decoded.decode("utf-8")
        self.assertEqual(
            "%CE%B1%CE%B2%CE%B3%CE%B4%CE%B5%CE%B6%25 ",
            encoded_str,
            "Basic PercentCodec unsafe char encoding test",
        )

    def testUnsafeCharEncodeDecode_test3_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6% "
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = bytes(encoded).decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_str = bytes(decoded).decode("utf-8")
        self.assertEqual(input_str, decoded_str)

    def testUnsafeCharEncodeDecode_test2_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6% "
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)

    def testUnsafeCharEncodeDecode_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6% "
        input_bytes = input_str.encode("utf-8")

    def testUnsafeCharEncodeDecode_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)

    def testSafeCharEncodeDecodeObject_test5_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode1(input_bytes)
        encoded_str = encoded.decode("utf-8")
        decoded = percent_codec.decode1(encoded)
        decoded_str = decoded.decode("utf-8")
        self.assertEqual(
            "Basic PercentCodec safe char encoding test", input_str, encoded_str
        )
        self.assertEqual(
            "Basic PercentCodec safe char decoding test", input_str, decoded_str
        )

    def testSafeCharEncodeDecodeObject_test4_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode1(input_bytes)
        encoded_str = bytes(encoded).decode(
            "utf-8"
        )  # Convert list to bytes before decoding
        decoded = percent_codec.decode1(encoded)
        decoded_str = bytes(decoded).decode(
            "utf-8"
        )  # Convert list to bytes before decoding
        self.assertEqual(
            input_str, encoded_str, "Basic PercentCodec safe char encoding test"
        )

    def testSafeCharEncodeDecodeObject_test3_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode1(input_bytes)
        encoded_str = encoded.decode("utf-8")
        decoded = percent_codec.decode1(encoded)

    def testSafeCharEncodeDecodeObject_test2_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode1(input_bytes)

    def testSafeCharEncodeDecodeObject_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        input_str = "abc123_-.*"
        input_bytes = input_str.encode("utf-8")

    def testSafeCharEncodeDecodeObject_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)

    def testPercentEncoderDecoderWithPlusForSpace_test5_decomposed(self) -> None:
        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        input_bytes = list(input_str.encode("utf-8"))  # Convert to list of integers
        encoded = percent_codec.encode0(input_bytes)
        encoded_str = "".join(
            map(chr, encoded)
        )  # Convert list of integers back to string
        self.assertEqual(
            "a+b+c+d", encoded_str, "PercentCodec plus for space encoding test"
        )
        decoded = percent_codec.decode0(encoded)
        decoded_str = "".join(
            map(chr, decoded)
        )  # Convert list of integers back to string
        self.assertEqual(
            input_str, decoded_str, "PercentCodec plus for space decoding test"
        )

    def testPercentEncoderDecoderWithPlusForSpace_test4_decomposed(self) -> None:
        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = "".join(map(chr, encoded))
        self.assertEqual(
            "a+b+c+d", encoded_str, "PercentCodec plus for space encoding test"
        )
        decoded = percent_codec.decode0(encoded)

    def testPercentEncoderDecoderWithPlusForSpace_test3_decomposed(self) -> None:
        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(
            list(input_bytes)
        )  # Convert bytes to list of integers
        encoded_str = bytes(encoded).decode(
            "utf-8"
        )  # Convert list of integers back to bytes, then decode
        self.assertEqual(
            "a+b+c+d", encoded_str, "PercentCodec plus for space encoding test"
        )

    def testPercentEncoderDecoderWithPlusForSpace_test2_decomposed(self) -> None:
        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)

    def testPercentEncoderDecoderWithPlusForSpace_test1_decomposed(self) -> None:
        input = "a b c d"
        percent_codec = PercentCodec(0, True, None)
        input_bytes = input.encode("utf-8")

    def testPercentEncoderDecoderWithPlusForSpace_test0_decomposed(self) -> None:
        input_str = "a b c d"
        percent_codec = PercentCodec(0, True, None)

    def testPercentEncoderDecoderWithNullOrEmptyInput_test5_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)

        # Null input value encoding test
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")

        # Null input value decoding test
        self.assertIsNone(percent_codec.decode0(None), "Null input value decoding test")

        # Empty input value encoding test
        empty_input = b""  # Corrected to use bytes directly
        self.assertEqual(
            percent_codec.encode0(empty_input),
            empty_input,
            "Empty input value encoding test",
        )

        # Empty input value decoding test
        self.assertEqual(
            percent_codec.decode0(empty_input),
            list(empty_input),
            "Empty input value decoding test",
        )

    def testPercentEncoderDecoderWithNullOrEmptyInput_test4_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)

        # Test for null input encoding
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")

        # Test for null input decoding
        self.assertIsNone(percent_codec.decode0(None), "Null input value decoding test")

        # Test for empty input encoding
        empty_input = b""  # Corrected to explicitly use a bytes object
        self.assertEqual(
            percent_codec.encode0(empty_input),
            list(empty_input),  # Corrected to match the expected list of bytes
            "Empty input value encoding test",
        )

    def testPercentEncoderDecoderWithNullOrEmptyInput_test3_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")
        self.assertIsNone(percent_codec.decode0(None), "Null input value decoding test")
        empty_input = "".encode("utf-8")

    def testPercentEncoderDecoderWithNullOrEmptyInput_test2_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")
        self.assertIsNone(percent_codec.decode0(None), "Null input value decoding test")

    def testPercentEncoderDecoderWithNullOrEmptyInput_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)
        self.assertIsNone(percent_codec.encode0(None), "Null input value encoding test")

    def testPercentEncoderDecoderWithNullOrEmptyInput_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(0, True, None)

    def testEncodeUnsupportedObject_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        with self.assertRaises(EncoderException):
            percent_codec.encode1("test")

    def testEncodeUnsupportedObject_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)

    def testEncodeNullObject_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        self.assertIsNone(percent_codec.encode1(None))

    def testEncodeNullObject_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)

    def testDecodeUnsupportedObject_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        with self.assertRaises(DecoderException):
            percent_codec.decode1("test")

    def testDecodeUnsupportedObject_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)

    def testDecodeNullObject_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        self.assertIsNone(percent_codec.decode1(None))

    def testDecodeNullObject_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)

    def testDecodeInvalidEncodedResultDecoding_test3_decomposed(self) -> None:
        input_s = "\u03b1\u03b2"  # Greek letters alpha and beta
        percent_codec = PercentCodec(1, False, None)
        input_bytes = input_s.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)

        try:
            # Exclude one byte from the encoded array
            percent_codec.decode0(encoded[:-1])
        except Exception as e:
            self.assertTrue(
                isinstance(e, DecoderException) and isinstance(e.__cause__, IndexError)
            )

    def testDecodeInvalidEncodedResultDecoding_test2_decomposed(self) -> None:
        input_s = "\u03b1\u03b2"  # Greek letters alpha and beta
        percent_codec = PercentCodec(1, False, None)
        input_bytes = input_s.encode(
            "utf-8"
        )  # Equivalent to getBytes(StandardCharsets.UTF_8) in Java
        encoded = percent_codec.encode0(input_bytes)

    def testDecodeInvalidEncodedResultDecoding_test1_decomposed(self) -> None:
        input_s = "\u03b1\u03b2"
        percent_codec = PercentCodec(1, False, None)
        input_s.encode("utf-8")

    def testDecodeInvalidEncodedResultDecoding_test0_decomposed(self) -> None:
        input_s = "\u03b1\u03b2"
        percent_codec = PercentCodec(1, False, None)

    def testConfigurablePercentEncoder_test5_decomposed(self) -> None:
        input_str = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, b"abcdef")

        # Encoding
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)
        encoded_str = encoded.decode("utf-8")
        self.assertEqual(
            "%61%62%63123_-.*%CE%B1%CE%B2",
            encoded_str,
            "Configurable PercentCodec encoding test",
        )

        # Decoding
        decoded = percent_codec.decode0(encoded)
        decoded_str = decoded.decode("utf-8")
        self.assertEqual(
            input_str, decoded_str, "Configurable PercentCodec decoding test"
        )

    def testConfigurablePercentEncoder_test4_decomposed(self) -> None:
        input_str = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, [ord(c) for c in "abcdef"])
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = "".join(
            f"%{b:02X}" if b > 127 or chr(b) not in "abcdef1234567890_-.*" else chr(b)
            for b in encoded
        )
        self.assertEqual(
            "%61%62%63123_-.*%CE%B1%CE%B2",
            encoded_str,
            "Configurable PercentCodec encoding test",
        )
        decoded = percent_codec.decode0(encoded)

    def testConfigurablePercentEncoder_test3_decomposed(self) -> None:
        input_str = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, [ord(c) for c in "abcdef"])
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = "".join(
            f"%{b:02X}" if b > 127 or chr(b) not in "abcdef1234567890_-.*" else chr(b)
            for b in encoded
        )
        self.assertEqual(
            "%61%62%63123_-.*%CE%B1%CE%B2",
            encoded_str,
            "Configurable PercentCodec encoding test",
        )

    def testConfigurablePercentEncoder_test2_decomposed(self) -> None:
        input_str = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, b"abcdef")
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)

    def testConfigurablePercentEncoder_test1_decomposed(self) -> None:
        input_str = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, b"abcdef")
        input_bytes = input_str.encode("utf-8")

    def testConfigurablePercentEncoder_test0_decomposed(self) -> None:
        input = "abc123_-.*\u03b1\u03b2"
        percent_codec = PercentCodec(0, False, b"abcdef")

    @pytest.mark.skip(reason="Ignore")
    def testBasicSpace_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = " "
        encoded = percent_codec.encode0(input_str.encode("utf-8"))
        self.assertEqual("%20".encode("utf-8"), encoded)

    def testBasicEncodeDecode_test5_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)
        encoded_str = encoded.decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_str = decoded.decode("utf-8")
        self.assertEqual("Basic PercentCodec encoding test", input_str, encoded_str)
        self.assertEqual("Basic PercentCodec decoding test", input_str, decoded_str)

    def testBasicEncodeDecode_test4_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = bytes(encoded).decode("utf-8")
        decoded = percent_codec.decode0(encoded)
        decoded_str = bytes(decoded).decode("utf-8")
        self.assertEqual(input_str, encoded_str, "Basic PercentCodec encoding test")

    def testBasicEncodeDecode_test3_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(list(input_bytes))
        encoded_str = bytes(encoded).decode("utf-8")
        decoded = percent_codec.decode0(encoded)

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        input_bytes = input_str.encode("utf-8")
        encoded = percent_codec.encode0(input_bytes)

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
        input_str = "abcdABCD"
        input_bytes = input_str.encode("utf-8")

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        percent_codec = PercentCodec(1, False, None)
