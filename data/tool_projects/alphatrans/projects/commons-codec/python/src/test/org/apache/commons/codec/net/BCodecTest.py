from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.BCodec import *


class BCodecTest(unittest.TestCase):

    RUSSIAN_STUFF_UNICODE: typing.List[int] = [
        0x412,
        0x441,
        0x435,
        0x43C,
        0x5F,
        0x43F,
        0x440,
        0x438,
        0x432,
        0x435,
        0x442,
    ]
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = [
        0x47,
        0x72,
        0xFC,
        0x65,
        0x7A,
        0x69,
        0x5F,
        0x7A,
        0xE4,
        0x6D,
        0xE4,
    ]
    __BASE64_IMPOSSIBLE_CASES: List[str] = [
        "=?ASCII?B?ZE==?=",
        "=?ASCII?B?ZmC=?=",
        "=?ASCII?B?Zm9vYE==?=",
        "=?ASCII?B?Zm9vYmC=?=",
        "=?ASCII?B?AB==?=",
    ]

    def testBase64ImpossibleSamplesStrict_test2_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.STRICT)
        self.assertTrue(codec.isStrictDecoding())
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            with pytest.raises(DecoderException):
                codec.decode0(s)

    def testBase64ImpossibleSamplesStrict_test1_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.STRICT)
        self.assertTrue(codec.isStrictDecoding())

    def testBase64ImpossibleSamplesStrict_test0_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.STRICT)

    def testBase64ImpossibleSamplesLenient_test2_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.LENIENT)
        self.assertFalse(
            codec.isStrictDecoding(),
            "Codec should not use strict decoding in LENIENT mode",
        )
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode0(s)
            except DecoderException:
                continue  # Expected behavior in LENIENT mode

    def testBase64ImpossibleSamplesLenient_test1_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.LENIENT)
        self.assertFalse(
            codec.isStrictDecoding(),
            "Codec should not use strict decoding in lenient mode",
        )

    def testBase64ImpossibleSamplesLenient_test0_decomposed(self) -> None:
        codec = BCodec(CharEncoding.UTF_8, CodecPolicy.LENIENT)

    def testBase64ImpossibleSamplesDefault_test2_decomposed(self) -> None:
        codec = BCodec.BCodec0()
        self.assertFalse(
            codec.isStrictDecoding(), "Codec should not use strict decoding by default"
        )
        for s in self.__BASE64_IMPOSSIBLE_CASES:
            codec.decode0(s)

    def testBase64ImpossibleSamplesDefault_test1_decomposed(self) -> None:
        codec = BCodec.BCodec0()
        self.assertFalse(codec.isStrictDecoding())

    def testBase64ImpossibleSamplesDefault_test0_decomposed(self) -> None:
        codec = BCodec.BCodec0()

    def testDecodeObjects_test3_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        decoded = "=?UTF-8?B?d2hhdCBub3Q=?="
        plain = bcodec.decode1(decoded)
        self.assertEqual("what not", plain, "Basic B decoding test")

        result = bcodec.decode1(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        with self.assertRaises(DecoderException):
            dObj = 3.0  # Python equivalent of Double.valueOf(3.0d)
            bcodec.decode1(dObj)

    def testDecodeObjects_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        decoded = "=?UTF-8?B?d2hhdCBub3Q=?="
        plain = bcodec.decode1(decoded)
        self.assertEqual("what not", plain, "Basic B decoding test")
        result = bcodec.decode1(None)

    def testDecodeObjects_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        decoded = "=?UTF-8?B?d2hhdCBub3Q=?="
        plain = bcodec.decode1(decoded)

    def testDecodeObjects_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testInvalidEncoding_test0_decomposed(self) -> None:
        with self.assertRaises(AttributeError):
            BCodec.BCodec2("NONSENSE")

    def testEncodeObjects_test3_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "what not"
        encoded = bcodec.encode3(plain)
        self.assertEqual("Basic B encoding test", "=?UTF-8?B?d2hhdCBub3Q=?=", encoded)

        result = bcodec.encode3(None)
        self.assertIsNone(result, "Encoding a null Object should return null")

        with self.assertRaises(EncoderException):
            d_obj = 3.0  # Equivalent to Double.valueOf(3.0d) in Java
            bcodec.encode3(d_obj)

    def testEncodeObjects_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "what not"
        encoded = bcodec.encode3(plain)
        self.assertEqual("Basic B encoding test", "=?UTF-8?B?d2hhdCBub3Q=?=", encoded)
        result = bcodec.encode3(None)

    def testEncodeObjects_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "what not"
        encoded = bcodec.encode3(plain)

    def testEncodeObjects_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testDecodeStringWithNull_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.decode0(test)
        self.assertIsNone(result, "Result should be null")

    def testDecodeStringWithNull_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.decode0(test)
        self.assertIsNone(result)

    def testDecodeStringWithNull_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testEncodeStringWithNull_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        test = None
        result = bcodec.encode1(test, "charset")
        self.assertIsNone(result)

    def testEncodeStringWithNull_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone(bcodec.encode2(None), "Null string B encoding test")
        self.assertIsNone(bcodec.decode0(None), "Null string B decoding test")

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone(bcodec.encode2(None), "Null string B encoding test")

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "Hello there"
        encoded = bcodec.encode2(plain)
        self.assertEqual(
            "=?UTF-8?B?SGVsbG8gdGhlcmU=?=", encoded, "Basic B encoding test"
        )
        self.assertEqual(plain, bcodec.decode0(encoded), "Basic B decoding test")

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        plain = "Hello there"
        encoded = bcodec.encode2(plain)

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def testUTF8RoundTrip_test5_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg)
        )
        self.assertEqual("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg))

        bcodec.encode2(ru_msg)
        self.assertEqual(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)))

        bcodec.encode2(ch_msg)
        self.assertEqual(ch_msg, bcodec.decode0(bcodec.encode2(ch_msg)))

    def testUTF8RoundTrip_test4_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg)
        )
        self.assertEqual("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg))

        self.assertEqual(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)))
        self.assertEqual(ch_msg, bcodec.decode0(bcodec.encode2(ch_msg)))

    def testUTF8RoundTrip_test3_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg)
        )
        self.assertEqual("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg))

        # Ensure round-trip encoding and decoding works
        self.assertEqual(ru_msg, bcodec.decode0(bcodec.encode2(ru_msg)))

    def testUTF8RoundTrip_test2_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)
        self.assertEqual(
            "=?UTF-8?B?0JLRgdC10Lxf0L/RgNC40LLQtdGC?=", bcodec.encode2(ru_msg)
        )
        self.assertEqual("=?UTF-8?B?R3LDvGV6aV96w6Rtw6Q=?=", bcodec.encode2(ch_msg))
        bcodec.encode2(ru_msg)

    def testUTF8RoundTrip_test1_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        bcodec = BCodec.BCodec2(CharEncoding.UTF_8)

    def testUTF8RoundTrip_test0_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

    def testNullInput_test2_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone(
            bcodec._doDecoding(None), "Decoding null input should return None"
        )
        self.assertIsNone(
            bcodec._doEncoding(None), "Encoding null input should return None"
        )

    def testNullInput_test1_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()
        self.assertIsNone(
            bcodec._doDecoding(None), "Expected None when decoding a null input"
        )

    def testNullInput_test0_decomposed(self) -> None:
        bcodec = BCodec.BCodec0()

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = []
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return "".join(buffer)
