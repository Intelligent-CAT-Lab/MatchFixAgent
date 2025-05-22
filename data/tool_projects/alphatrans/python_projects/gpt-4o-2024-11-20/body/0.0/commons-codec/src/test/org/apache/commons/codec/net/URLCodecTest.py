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
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.URLCodec import *


class URLCodecTest(unittest.TestCase):

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

    def testDefaultEncoding_test4_decomposed(self) -> None:
        plain = "Hello there!"
        urlCodec = URLCodec(
            "utf-16"
        )  # Corrected encoding from "UnicodeBig" to "utf-16"
        urlCodec.encode2(plain)
        encoded1 = urlCodec.encode1(plain, "utf-16")  # Corrected encoding
        encoded2 = urlCodec.encode2(plain)
        self.assertEqual(encoded1, encoded2)
        self.__validateState(urlCodec)

    def testDefaultEncoding_test3_decomposed(self) -> None:
        plain = "Hello there!"
        url_codec = URLCodec("UnicodeBig")
        url_codec.encode2(plain)
        encoded1 = url_codec.encode1(plain, "UnicodeBig")
        encoded2 = url_codec.encode2(plain)

    def testDefaultEncoding_test2_decomposed(self) -> None:
        plain = "Hello there!"
        url_codec = URLCodec(
            "utf-16"
        )  # Corrected encoding from "UnicodeBig" to "utf-16"
        url_codec.encode2(plain)
        encoded1 = url_codec.encode1(plain, "utf-16")

    def testDefaultEncoding_test1_decomposed(self) -> None:
        plain = "Hello there!"
        url_codec = URLCodec(
            "utf-16"
        )  # Corrected encoding from "UnicodeBig" to "utf-16"
        url_codec.encode2(plain)

    def testDefaultEncoding_test0_decomposed(self) -> None:
        plain: str = "Hello there!"
        url_codec = URLCodec("UnicodeBig")

    def testDecodeObjects_test7_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = "Hello+there%21"

        # Decode a string
        decoded = urlCodec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode a byte array
        plainBA = plain.encode("utf-8")
        decodedBA = urlCodec.decode3(plainBA)
        decoded = bytes(decodedBA).decode(
            "utf-8"
        )  # Convert list to bytes before decoding
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode a null object
        result = urlCodec.decode3(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        # Attempt to decode an unsupported object type
        with self.assertRaises(DecoderException):
            dObj = 3.0  # Double in Java, float in Python
            urlCodec.decode3(dObj)

        # Validate the state of the URLCodec
        self.__validateState(urlCodec)

    def testDecodeObjects_test6_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"

        # Decode a string
        decoded = url_codec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode a byte array
        plain_ba = plain.encode("utf-8")
        decoded_ba = url_codec.decode3(plain_ba)
        decoded = decoded_ba.decode("utf-8")
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode a null object
        result = url_codec.decode3(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        # Attempt to decode an unsupported object type
        with pytest.raises(DecoderException):
            d_obj = 3.0  # Double in Java, float in Python
            url_codec.decode3(d_obj)

    def testDecodeObjects_test5_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"

        # Decode the string
        decoded = url_codec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode the byte array
        plain_ba = plain.encode(CharEncoding.UTF_8)
        decoded_ba = url_codec.decode3(plain_ba)
        decoded = decoded_ba.decode(CharEncoding.UTF_8)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        # Decode a None object
        result = url_codec.decode3(None)
        self.assertIsNone(result)

    def testDecodeObjects_test4_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"
        decoded = url_codec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        plain_ba = plain.encode(CharEncoding.UTF_8)
        decoded_ba = url_codec.decode3(plain_ba)
        decoded = decoded_ba.decode(CharEncoding.UTF_8)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

    def testDecodeObjects_test3_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"
        decoded = url_codec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")

        plain_ba = plain.encode("utf-8")
        decoded_ba = url_codec.decode3(plain_ba)

    def testDecodeObjects_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"
        decoded = url_codec.decode3(plain)
        self.assertEqual("Hello there!", decoded, "Basic URL decoding test")
        plain_ba = plain.encode("utf-8")

    def testDecodeObjects_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello+there%21"
        decoded = url_codec.decode3(plain)

    def testDecodeObjects_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testInvalidEncoding_test3_decomposed(self) -> None:
        urlCodec = URLCodec("NONSENSE")
        plain = "Hello there!"

        with self.assertRaises(
            EncoderException,
            msg="We set the encoding to a bogus NONSENSE value, this shouldn't have worked.",
        ):
            urlCodec.encode2(plain)

        with self.assertRaises(
            DecoderException,
            msg="We set the encoding to a bogus NONSENSE value, this shouldn't have worked.",
        ):
            urlCodec.decode2(plain)

        self.__validateState(urlCodec)

    def testInvalidEncoding_test2_decomposed(self) -> None:
        url_codec = URLCodec("NONSENSE")
        plain = "Hello there!"

        with pytest.raises(EncoderException):
            url_codec.encode2(plain)

        with pytest.raises(DecoderException):
            url_codec.decode2(plain)

    def testInvalidEncoding_test1_decomposed(self) -> None:
        url_codec = URLCodec("NONSENSE")
        plain = "Hello there!"
        with self.assertRaises(
            LookupError,
            msg="We set the encoding to a bogus NONSENSE value, this shouldn't have worked.",
        ):
            url_codec.encode2(plain)

    def testInvalidEncoding_test0_decomposed(self) -> None:
        url_codec = URLCodec("NONSENSE")

    def testEncodeObjects_test7_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"

        # Encoding a string
        encoded = urlCodec.encode3(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

        # Encoding a byte array
        plainBA = plain.encode(CharEncoding.UTF_8)
        encodedBA = urlCodec.encode3(plainBA)
        encoded = bytes(encodedBA).decode(CharEncoding.UTF_8)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

        # Encoding a null object
        result = urlCodec.encode3(None)
        self.assertIsNone(result, "Encoding a null Object should return null")

        # Encoding an unsupported object type
        with self.assertRaises(EncoderException):
            dObj = 3.0  # Double value
            urlCodec.encode3(dObj)

        # Validate the state of the URLCodec
        self.__validateState(urlCodec)

    def testEncodeObjects_test6_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"

        # Test encoding a string
        encoded = url_codec.encode3(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

        # Test encoding a byte array
        plain_ba = plain.encode(CharEncoding.UTF_8)
        encoded_ba = url_codec.encode3(plain_ba)
        encoded = encoded_ba.decode(CharEncoding.UTF_8)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

        # Test encoding a null object
        result = url_codec.encode3(None)
        self.assertIsNone(result, "Encoding a null Object should return null")

        # Test encoding an unsupported object type
        with pytest.raises(EncoderException):
            d_obj = 3.0  # Double in Java, float in Python
            url_codec.encode3(d_obj)

    def testEncodeObjects_test5_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)

        plain_ba = plain.encode(CharEncoding.UTF_8)
        encoded_ba = url_codec.encode3(plain_ba)
        encoded = encoded_ba.decode(CharEncoding.UTF_8)
        self.assertEqual("Basic URL encoding test", "Hello+there%21", encoded)

        result = url_codec.encode3(None)
        self.assertIsNone(result)

    def testEncodeObjects_test4_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

        plain_ba = plain.encode("utf-8")
        encoded_ba = url_codec.encode3(plain_ba)
        encoded = encoded_ba.decode("utf-8")
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")

    def testEncodeObjects_test3_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        plain_ba = plain.encode("utf-8")
        encoded_ba = url_codec.encode3(plain_ba)

    def testEncodeObjects_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        plain_ba = plain.encode("utf-8")

    def testEncodeObjects_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode3(plain)

    def testEncodeObjects_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testDecodeStringWithNull_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        test = None
        result = url_codec.decode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testDecodeStringWithNull_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        test = None
        result = url_codec.decode1(test, "charset")

    def testDecodeStringWithNull_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testEncodeStringWithNull_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        test = None
        result = url_codec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        test = None
        result = url_codec.encode1(test, "charset")

    def testEncodeStringWithNull_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testDecodeWithNullArray_test1_decomposed(self) -> None:
        plain = None
        result = URLCodec.decodeUrl(plain)
        self.assertIsNone(result, "Result should be null")

    def testDecodeWithNullArray_test0_decomposed(self) -> None:
        plain: Optional[List[int]] = None
        result = URLCodec.decodeUrl(plain)
        self.assertIsNone(result)

    def testEncodeUrlWithNullBitSet_test4_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        plain_bytes = plain.encode(CharEncoding.UTF_8)
        encoded = "".join(map(chr, URLCodec.encodeUrl(None, plain_bytes)))
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        self.assertEqual(plain, urlCodec.decode2(encoded), "Basic URL decoding test")
        self.__validateState(urlCodec)

    def testEncodeUrlWithNullBitSet_test3_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        plain_bytes = plain.encode("utf-8")
        encoded = "".join(map(chr, URLCodec.encodeUrl(None, list(plain_bytes))))
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        self.assertEqual(plain, url_codec.decode2(encoded), "Basic URL decoding test")

    def testEncodeUrlWithNullBitSet_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        plain_bytes = plain.encode(CharEncoding.UTF_8)
        encoded = bytes(URLCodec.encodeUrl(None, plain_bytes))

    def testEncodeUrlWithNullBitSet_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        plain_bytes = plain.encode(CharEncoding.UTF_8)

    def testEncodeUrlWithNullBitSet_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testEncodeNull_test2_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = None
        encoded = urlCodec.encode0(plain)
        self.assertIsNone(encoded, "Encoding a null string should return null")
        self.__validateState(urlCodec)

    def testEncodeNull_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = None
        encoded = url_codec.encode0(plain)

    def testEncodeNull_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testDecodeInvalidContent_test4_decomposed(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        input_bytes = ch_msg.encode(CharEncoding.ISO_8859_1)
        output_bytes = urlCodec.decode0(input_bytes)
        self.assertEqual(len(input_bytes), len(output_bytes))
        for i in range(len(input_bytes)):
            self.assertEqual(input_bytes[i], output_bytes[i])
        self.__validateState(urlCodec)

    def testDecodeInvalidContent_test3_decomposed(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        url_codec = URLCodec.URLCodec1()
        input_bytes = ch_msg.encode(CharEncoding.ISO_8859_1)
        output_bytes = url_codec.decode0(input_bytes)

    def testDecodeInvalidContent_test2_decomposed(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        url_codec = URLCodec.URLCodec1()
        input_bytes = ch_msg.encode(CharEncoding.ISO_8859_1)

    def testDecodeInvalidContent_test1_decomposed(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        url_codec = URLCodec.URLCodec1()

    def testDecodeInvalidContent_test0_decomposed(self) -> None:
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

    def testDecodeInvalid_test2_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()

        with pytest.raises(DecoderException):
            urlCodec.decode2("%")

        with pytest.raises(DecoderException):
            urlCodec.decode2("%A")

        with pytest.raises(DecoderException):
            urlCodec.decode2("%WW")

        with pytest.raises(DecoderException):
            urlCodec.decode2("%0W")

        self.__validateState(urlCodec)

    def testDecodeInvalid_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

        with pytest.raises(DecoderException):
            url_codec.decode2("%")

        with pytest.raises(DecoderException):
            url_codec.decode2("%A")

        with pytest.raises(DecoderException):
            url_codec.decode2("%WW")

        with pytest.raises(DecoderException):
            url_codec.decode2("%0W")

    def testDecodeInvalid_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testEncodeDecodeNull_test3_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        self.assertIsNone(urlCodec.encode2(None), "Null string URL encoding test")
        self.assertIsNone(urlCodec.decode2(None), "Null string URL decoding test")
        self.__validateState(urlCodec)

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        self.assertIsNone(url_codec.encode2(None), "Null string URL encoding test")
        self.assertIsNone(url_codec.decode2(None), "Null string URL decoding test")

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        self.assertIsNone(url_codec.encode2(None), "Null string URL encoding test")

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testUnsafeEncodeDecode_test3_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = '~!@#$%^&()+{}"\\;:`,/[]'
        encoded = urlCodec.encode2(plain)
        self.assertEqual(
            "%7E%21%40%23%24%25%5E%26%28%29%2B%7B%7D%22%5C%3B%3A%60%2C%2F%5B%5D",
            encoded,
            "Unsafe chars URL encoding test",
        )
        self.assertEqual(
            plain, urlCodec.decode2(encoded), "Unsafe chars URL decoding test"
        )
        self.__validateState(urlCodec)

    def testUnsafeEncodeDecode_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = '~!@#$%^&()+{}"\\;:`,/[]'
        encoded = url_codec.encode2(plain)
        self.assertEqual(
            "%7E%21%40%23%24%25%5E%26%28%29%2B%7B%7D%22%5C%3B%3A%60%2C%2F%5B%5D",
            encoded,
            "Unsafe chars URL encoding test",
        )
        self.assertEqual(
            plain, url_codec.decode2(encoded), "Unsafe chars URL decoding test"
        )

    def testUnsafeEncodeDecode_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = '~!@#$%^&()+{}"\\;:`,/[]'
        encoded = url_codec.encode2(plain)

    def testUnsafeEncodeDecode_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testSafeCharEncodeDecode_test3_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = "abc123_-.*"
        encoded = urlCodec.encode2(plain)
        self.assertEqual(plain, encoded, "Safe chars URL encoding test")
        self.assertEqual(
            plain, urlCodec.decode2(encoded), "Safe chars URL decoding test"
        )
        self.__validateState(urlCodec)

    def testSafeCharEncodeDecode_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "abc123_-.*"
        encoded = url_codec.encode2(plain)
        self.assertEqual(plain, encoded, "Safe chars URL encoding test")
        self.assertEqual(
            plain, url_codec.decode2(encoded), "Safe chars URL decoding test"
        )

    def testSafeCharEncodeDecode_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "abc123_-.*"
        encoded = url_codec.encode2(plain)

    def testSafeCharEncodeDecode_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testBasicEncodeDecode_test3_decomposed(self) -> None:
        urlCodec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = urlCodec.encode2(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        self.assertEqual(plain, urlCodec.decode2(encoded), "Basic URL decoding test")
        self.__validateState(urlCodec)

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode2(plain)
        self.assertEqual("Hello+there%21", encoded, "Basic URL encoding test")
        self.assertEqual(plain, url_codec.decode2(encoded), "Basic URL decoding test")

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()
        plain = "Hello there!"
        encoded = url_codec.encode2(plain)

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        url_codec = URLCodec.URLCodec1()

    def testUTF8RoundTrip_test7_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )

        urlCodec.encode1(ru_msg, CharEncoding.UTF_8)
        self.assertEqual(
            ru_msg,
            urlCodec.decode1(
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

        urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        self.assertEqual(
            ch_msg,
            urlCodec.decode1(
                urlCodec.encode1(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

        self.__validateState(urlCodec)

    def testUTF8RoundTrip_test6_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )

        urlCodec.encode1(ru_msg, CharEncoding.UTF_8)
        self.assertEqual(
            ru_msg,
            urlCodec.decode1(
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

        urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        self.assertEqual(
            ch_msg,
            urlCodec.decode1(
                urlCodec.encode1(ch_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

    def testUTF8RoundTrip_test5_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )

        urlCodec.encode1(ru_msg, CharEncoding.UTF_8)
        self.assertEqual(
            ru_msg,
            urlCodec.decode1(
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

        urlCodec.encode1(ch_msg, CharEncoding.UTF_8)

    def testUTF8RoundTrip_test4_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )

        urlCodec.encode1(ru_msg, CharEncoding.UTF_8)

        self.assertEqual(
            ru_msg,
            urlCodec.decode1(
                urlCodec.encode1(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

    def testUTF8RoundTrip_test3_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)
        self.assertEqual(
            "%D0%92%D1%81%D0%B5%D0%BC_%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82",
            urlCodec.encode1(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr%C3%BCezi_z%C3%A4m%C3%A4", urlCodec.encode1(ch_msg, CharEncoding.UTF_8)
        )
        urlCodec.encode1(ru_msg, CharEncoding.UTF_8)

    def testUTF8RoundTrip_test2_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()
        self.__validateState(urlCodec)

    def testUTF8RoundTrip_test1_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        urlCodec = URLCodec.URLCodec1()

    def testUTF8RoundTrip_test0_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = []
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return "".join(buffer)

    def __validateState(self, urlCodec: URLCodec) -> None:
        pass
