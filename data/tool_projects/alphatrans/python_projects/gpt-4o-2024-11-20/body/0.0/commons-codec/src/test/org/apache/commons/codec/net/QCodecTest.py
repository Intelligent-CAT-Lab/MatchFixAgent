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
from src.main.org.apache.commons.codec.net.QCodec import *


class QCodecTest(unittest.TestCase):

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

    def testLetUsMakeCloverHappy_test4_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(True)
        self.assertTrue(qcodec.isEncodeBlanks())
        qcodec.setEncodeBlanks(False)
        self.assertFalse(qcodec.isEncodeBlanks())

    def testLetUsMakeCloverHappy_test3_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(True)
        self.assertTrue(qcodec.isEncodeBlanks())
        qcodec.setEncodeBlanks(False)

    def testLetUsMakeCloverHappy_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(True)
        self.assertTrue(qcodec.isEncodeBlanks())

    def testLetUsMakeCloverHappy_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(True)

    def testLetUsMakeCloverHappy_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testEncodeDecodeBlanks_test7_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()

        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded1, s, "Blanks encoding with the Q codec test")

        qcodec.setEncodeBlanks(True)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded2, s, "Blanks encoding with the Q codec test")

        s = qcodec.decode0(encoded1)
        self.assertEqual(plain, s, "Blanks decoding with the Q codec test")

        s = qcodec.decode0(encoded2)
        self.assertEqual(plain, s, "Blanks decoding with the Q codec test")

    def testEncodeDecodeBlanks_test6_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()

        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded1, s, "Blanks encoding with the Q codec test")

        qcodec.setEncodeBlanks(True)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded2, s, "Blanks encoding with the Q codec test")

        s = qcodec.decode0(encoded1)
        self.assertEqual(plain, s, "Blanks decoding with the Q codec test")

        s = qcodec.decode0(encoded2)
        self.assertEqual(plain, s, "Blanks decoding with the Q codec test")

    def testEncodeDecodeBlanks_test5_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()

        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded1, s, "Blanks encoding with the Q codec test")

        qcodec.setEncodeBlanks(True)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded2, s, "Blanks encoding with the Q codec test")

        s = qcodec.decode0(encoded1)

    def testEncodeDecodeBlanks_test4_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()

        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded1, s, "Blanks encoding with the Q codec test")

        qcodec.setEncodeBlanks(True)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded2, s)

    def testEncodeDecodeBlanks_test3_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(encoded1, s, "Blanks encoding with the Q codec test")
        qcodec.setEncodeBlanks(True)

    def testEncodeDecodeBlanks_test2_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(False)
        s = qcodec.encode2(plain)
        self.assertEqual(s, encoded1)

    def testEncodeDecodeBlanks_test1_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()
        qcodec.setEncodeBlanks(False)

    def testEncodeDecodeBlanks_test0_decomposed(self) -> None:
        plain = "Mind those pesky blanks"
        encoded1 = "=?UTF-8?Q?Mind those pesky blanks?="
        encoded2 = "=?UTF-8?Q?Mind_those_pesky_blanks?="
        qcodec = QCodec.QCodec2()

    def testDecodeObjects_test3_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        decoded = "=?UTF-8?Q?1+1 =3D 2?="
        plain = qcodec.decode1(decoded)
        self.assertEqual("1+1 = 2", plain, "Basic Q decoding test")

        result = qcodec.decode1(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        with pytest.raises(DecoderException):
            d_obj = 3.0  # Double value in Java, equivalent to float in Python
            qcodec.decode1(d_obj)

    def testDecodeObjects_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        decoded = "=?UTF-8?Q?1+1 =3D 2?="
        plain = qcodec.decode1(decoded)
        self.assertEqual("1+1 = 2", plain, "Basic Q decoding test")
        result = qcodec.decode1(None)

    def testDecodeObjects_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        decoded = "=?UTF-8?Q?1+1 =3D 2?="
        plain = qcodec.decode1(decoded)

    def testDecodeObjects_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testInvalidEncoding_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            QCodec.QCodec0("NONSENSE")

    def testEncodeObjects_test3_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "1+1 = 2"
        encoded = qcodec.encode3(plain)
        self.assertEqual("=?UTF-8?Q?1+1 =3D 2?=", encoded, "Basic Q encoding test")

        result = qcodec.encode3(None)
        self.assertIsNone(result, "Encoding a null Object should return null")

        with pytest.raises(EncoderException):
            d_obj = 3.0  # Double value in Python
            qcodec.encode3(d_obj)

    def testEncodeObjects_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "1+1 = 2"
        encoded = qcodec.encode3(plain)
        self.assertEqual("=?UTF-8?Q?1+1 =3D 2?=", encoded, "Basic Q encoding test")
        result = qcodec.encode3(None)
        self.assertIsNone(result, "Encoding None should return None")

    def testEncodeObjects_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "1+1 = 2"
        encoded = qcodec.encode3(plain)

    def testEncodeObjects_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testDecodeStringWithNull_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.decode0(test)
        self.assertIsNone(result, "Result should be null")

    def testDecodeStringWithNull_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.decode0(test)

    def testDecodeStringWithNull_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testEncodeStringWithNull_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.encode1(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        test = None
        result = qcodec.encode1(test, "charset")

    def testEncodeStringWithNull_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        self.assertIsNone(qcodec.encode2(None), "Null string Q encoding test")
        self.assertIsNone(qcodec.decode0(None), "Null string Q decoding test")

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        self.assertIsNone(qcodec.encode2(None), "Null string Q encoding test")

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testUnsafeEncodeDecode_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "?_=\r\n"
        encoded = qcodec.encode2(plain)
        self.assertEqual(
            "=?UTF-8?Q?=3F=5F=3D=0D=0A?=", encoded, "Unsafe chars Q encoding test"
        )
        self.assertEqual(plain, qcodec.decode0(encoded), "Unsafe chars Q decoding test")

    def testUnsafeEncodeDecode_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "?_=\r\n"
        try:
            encoded = qcodec.encode2(plain)
            self.assertIsNotNone(encoded)
        except EncoderException as e:
            self.fail(f"EncoderException was raised: {e}")

    def testUnsafeEncodeDecode_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "= Hello there =\r\n"
        encoded = qcodec.encode2(plain)
        self.assertEqual(
            "=?UTF-8?Q?=3D Hello there =3D=0D=0A?=", encoded, "Basic Q encoding test"
        )
        self.assertEqual(plain, qcodec.decode0(encoded), "Basic Q decoding test")

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        plain = "= Hello there =\r\n"
        try:
            encoded = qcodec.encode2(plain)
        except EncoderException as e:
            raise EncoderException("Encoded bytes cannot be None") from e

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def testUTF8RoundTrip_test5_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?Q?=D0=92=D1=81=D0=B5=D0=BC=5F=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82?=",
            qcodec.encode2(ru_msg),
        )
        self.assertEqual(
            "=?UTF-8?Q?Gr=C3=BCezi=5Fz=C3=A4m=C3=A4?=", qcodec.encode2(ch_msg)
        )

        self.assertEqual(ru_msg, qcodec.decode0(qcodec.encode2(ru_msg)))
        self.assertEqual(ch_msg, qcodec.decode0(qcodec.encode2(ch_msg)))

    def testUTF8RoundTrip_test4_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?Q?=D0=92=D1=81=D0=B5=D0=BC=5F=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82?=",
            qcodec.encode2(ru_msg),
        )
        self.assertEqual(
            "=?UTF-8?Q?Gr=C3=BCezi=5Fz=C3=A4m=C3=A4?=", qcodec.encode2(ch_msg)
        )

        qcodec.encode2(ru_msg)
        self.assertEqual(ru_msg, qcodec.decode0(qcodec.encode2(ru_msg)))
        qcodec.encode2(ch_msg)

    def testUTF8RoundTrip_test3_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?Q?=D0=92=D1=81=D0=B5=D0=BC=5F=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82?=",
            qcodec.encode2(ru_msg),
        )
        self.assertEqual(
            "=?UTF-8?Q?Gr=C3=BCezi=5Fz=C3=A4m=C3=A4?=", qcodec.encode2(ch_msg)
        )
        self.assertEqual(ru_msg, qcodec.decode0(qcodec.encode2(ru_msg)))

    def testUTF8RoundTrip_test2_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

        self.assertEqual(
            "=?UTF-8?Q?=D0=92=D1=81=D0=B5=D0=BC=5F=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82?=",
            qcodec.encode2(ru_msg),
        )
        self.assertEqual(
            "=?UTF-8?Q?Gr=C3=BCezi=5Fz=C3=A4m=C3=A4?=", qcodec.encode2(ch_msg)
        )
        qcodec.encode2(ru_msg)

    def testUTF8RoundTrip_test1_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qcodec = QCodec.QCodec0(CharEncoding.UTF_8)

    def testUTF8RoundTrip_test0_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

    def testNullInput_test2_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        self.assertIsNone(qcodec._doDecoding(None))
        self.assertIsNone(qcodec._doEncoding(None))

    def testNullInput_test1_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()
        self.assertIsNone(qcodec._doDecoding(None))

    def testNullInput_test0_decomposed(self) -> None:
        qcodec = QCodec.QCodec2()

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = []
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return "".join(buffer)
