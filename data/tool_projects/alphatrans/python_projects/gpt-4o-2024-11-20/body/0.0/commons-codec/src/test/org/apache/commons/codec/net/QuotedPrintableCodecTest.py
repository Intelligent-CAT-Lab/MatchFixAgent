from __future__ import annotations
import math
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
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *


class QuotedPrintableCodecTest(unittest.TestCase):

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

    def testFinalBytes_test1_decomposed(self) -> None:
        plain = "This is a example of a quoted=printable text file. There is no tt"
        expected = "This is a example of a quoted=3Dprintable text file. There is no tt"
        codec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(expected, codec.encode1(plain))

    def testFinalBytes_test0_decomposed(self) -> None:
        plain = "This is a example of a quoted=printable text file. There is no tt"
        expected = "This is a example of a quoted=3Dprintable text file. There is no tt"
        QuotedPrintableCodec.QuotedPrintableCodec3(True)

    def testUltimateSoftBreak_test4_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it\t"
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=20"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to   "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to=20=\r\n =20"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to=  "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to=3D=\r\n =20"
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testUltimateSoftBreak_test3_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it\t"
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=20"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to   "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to=20=\r\n =20"
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testUltimateSoftBreak_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        plain = (
            "This is a example of a quoted-printable text file. There is no end to it\t"
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09"
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. There is no end to it "
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=20"
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testUltimateSoftBreak_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        plain = (
            "This is a example of a quoted-printable text file. There is no end to it\t"
        )
        expected = "This is a example of a quoted-printable text file. There is no end to i=\r\nt=09"
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testUltimateSoftBreak_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

    def testTrailingSpecial_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

        plain = (
            "This is a example of a quoted-printable text file. This might contain sp=cial"
            + " chars."
        )
        expected = (
            "This is a example of a quoted-printable text file. This might contain sp=3D=\r\n"
            + "cial chars."
        )
        self.assertEqual(expected, qpcodec.encode1(plain))

        plain = (
            "This is a example of a quoted-printable text file. This might contain ta\tbs as"
            + " well."
        )
        expected = (
            "This is a example of a quoted-printable text file. This might contain ta=09=\r\n"
            + "bs as well."
        )
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testTrailingSpecial_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        plain = (
            "This is a example of a quoted-printable text file. This might contain sp=cial"
            + " chars."
        )
        expected = (
            "This is a example of a quoted-printable text file. This might contain sp=3D=\r\n"
            + "cial chars."
        )
        self.assertEqual(expected, qpcodec.encode1(plain))

    def testTrailingSpecial_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

    def testSkipNotEncodedCRLF_test3_decomposed(self) -> None:
        qpdata = (
            "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding."
        )
        expected = "CRLF in an encoded text should be skipped in the decoding."
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(expected, qpcodec.decode3(qpdata))
        encoded = qpcodec.encode1(expected)
        self.assertEqual(expected, qpcodec.decode3(encoded))

    def testSkipNotEncodedCRLF_test2_decomposed(self) -> None:
        qpdata = (
            "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding."
        )
        expected = "CRLF in an encoded text should be skipped in the decoding."
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(expected, qpcodec.decode3(qpdata))
        encoded = qpcodec.encode1(expected)

    def testSkipNotEncodedCRLF_test1_decomposed(self) -> None:
        qpdata = (
            "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding."
        )
        expected = "CRLF in an encoded text should be skipped in the decoding."
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(expected, qpcodec.decode3(qpdata))

    def testSkipNotEncodedCRLF_test0_decomposed(self) -> None:
        qpdata = (
            "CRLF in an\n encoded text should be=20=\r\n\rskipped in the\r decoding."
        )
        expected = "CRLF in an encoded text should be skipped in the decoding."
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        result = qpcodec.decode(qpdata)
        self.assertEqual(result, expected)

    def testSoftLineBreakEncode_test3_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
            + "eautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(qpdata, qpcodec.encode1(expected))
        decoded = qpcodec.decode3(qpdata)
        self.assertEqual(qpdata, qpcodec.encode1(decoded))

    def testSoftLineBreakEncode_test2_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
            + "eautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(qpdata, qpcodec.encode1(expected))
        decoded = qpcodec.decode3(qpdata)

    def testSoftLineBreakEncode_test1_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
            "eautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)
        self.assertEqual(qpdata, qpcodec.encode1(expected))

    def testSoftLineBreakEncode_test0_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely mathematics is the most b=\r\n"
            "eautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec3(True)

    def testSoftLineBreakDecode_test3_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            "mathematics is the most beautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertEqual(expected, qpcodec.decode3(qpdata))
        encoded = qpcodec.encode1(expected)
        self.assertEqual(expected, qpcodec.decode3(encoded))

    def testSoftLineBreakDecode_test2_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            "mathematics is the most beautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertEqual(expected, qpcodec.decode3(qpdata))
        encoded = qpcodec.encode1(expected)

    def testSoftLineBreakDecode_test1_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            "mathematics is the most beautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertEqual(expected, qpcodec.decode3(qpdata))

    def testSoftLineBreakDecode_test0_decomposed(self) -> None:
        qpdata = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            "mathematics is the most beautiful branch of philosophy."
        )
        expected = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            " branch of philosophy."
        )
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        result = qpcodec.decode(qpdata)
        self.assertEqual(result, expected)

    def testDefaultEncoding_test4_decomposed(self) -> None:
        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("UnicodeBig")
        qpcodec.encode1(plain)
        encoded1 = qpcodec.encode4(plain, "UnicodeBig")
        encoded2 = qpcodec.encode1(plain)
        self.assertEqual(encoded1, encoded2)

    def testDefaultEncoding_test3_decomposed(self) -> None:
        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("UnicodeBig")
        qpcodec.encode1(plain)
        encoded1 = qpcodec.encode4(plain, "UnicodeBig")
        encoded2 = qpcodec.encode1(plain)

    def testDefaultEncoding_test2_decomposed(self) -> None:
        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("utf-16-be")
        qpcodec.encode1(plain)
        encoded1 = qpcodec.encode4(plain, "utf-16-be")

    def testDefaultEncoding_test1_decomposed(self) -> None:
        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("utf-16-be")
        qpcodec.encode1(plain)

    def testDefaultEncoding_test0_decomposed(self) -> None:
        plain = "Hello there!"
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec0("UnicodeBig")

    def testDecodeObjects_test6_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"

        # Decode a string
        decoded = qpcodec.decode4(plain)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

        # Decode a byte array
        plainBA = plain.encode(CharEncoding.UTF_8)
        decodedBA = qpcodec.decode4(plainBA)
        decoded = decodedBA.decode(CharEncoding.UTF_8)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

        # Decode a null object
        result = qpcodec.decode4(None)
        self.assertIsNone(result, "Decoding a null Object should return null")

        # Attempt to decode an unsupported object type
        with pytest.raises(DecoderException):
            dObj = 3.0  # Double value
            qpcodec.decode4(dObj)

    def testDecodeObjects_test5_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"

        # Decode the plain string
        decoded = qpcodec.decode4(plain)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

        # Decode the plain string as bytes
        plainBA = plain.encode(CharEncoding.UTF_8)
        decodedBA = qpcodec.decode4(plainBA)
        decoded = decodedBA.decode(CharEncoding.UTF_8)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

        # Decode a None object
        result = qpcodec.decode4(None)
        self.assertIsNone(result)

    def testDecodeObjects_test4_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"

        # Decode the string
        decoded = qpcodec.decode4(plain)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

        # Decode the byte array
        plainBA = plain.encode(CharEncoding.UTF_8)
        decodedBA = qpcodec.decode4(plainBA)
        decoded = decodedBA.decode(CharEncoding.UTF_8)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")

    def testDecodeObjects_test3_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"
        decoded = qpcodec.decode4(plain)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")
        plainBA = plain.encode(CharEncoding.UTF_8)
        decodedBA = qpcodec.decode4(plainBA)

    def testDecodeObjects_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"
        decoded = qpcodec.decode4(plain)
        self.assertEqual("1+1 = 2", decoded, "Basic quoted-printable decoding test")
        plainBA = plain.encode("utf-8")

    def testDecodeObjects_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 =3D 2"
        decoded = qpcodec.decode4(plain)

    def testDecodeObjects_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testInvalidEncoding_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            QuotedPrintableCodec.QuotedPrintableCodec0("NONSENSE")
        self.assertEqual(str(context.exception), "Unsupported charset: NONSENSE")

    def testEncodeObjects_test6_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"

        # Test encoding a string
        encoded = qpcodec.encode2(plain)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

        # Test encoding a byte array
        plainBA = plain.encode("utf-8")
        encodedBA = qpcodec.encode2(plainBA)
        encoded = encodedBA.decode("utf-8")
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

        # Test encoding a null object
        result = qpcodec.encode2(None)
        self.assertIsNone(result, "Encoding a null Object should return null")

        # Test encoding an unsupported object type
        with self.assertRaises(EncoderException):
            dObj = 3.0  # Double in Java, float in Python
            qpcodec.encode2(dObj)

    def testEncodeObjects_test5_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

        plainBA = plain.encode(CharEncoding.UTF_8)
        encodedBA = qpcodec.encode2(plainBA)
        encoded = encodedBA.decode(CharEncoding.UTF_8)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

        result = qpcodec.encode2(None)

    def testEncodeObjects_test4_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

        plainBA = plain.encode(CharEncoding.UTF_8)
        encodedBA = qpcodec.encode2(plainBA)
        encoded = encodedBA.decode(CharEncoding.UTF_8)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")

    def testEncodeObjects_test3_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")
        plainBA = plain.encode("utf-8")
        encodedBA = qpcodec.encode2(plainBA)

    def testEncodeObjects_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")
        plainBA = plain.encode(CharEncoding.UTF_8)

    def testEncodeObjects_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        encoded = qpcodec.encode2(plain)

    def testEncodeObjects_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testDecodeStringWithNull_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.decode2(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testDecodeStringWithNull_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.decode2(test, "charset")
        self.assertIsNone(result)

    def testDecodeStringWithNull_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testEncodeStringWithNull_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.encode4(test, "charset")
        self.assertIsNone(result, "Result should be null")

    def testEncodeStringWithNull_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        test = None
        result = qpcodec.encode4(test, "charset")

    def testEncodeStringWithNull_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testDecodeWithNullArray_test1_decomposed(self) -> None:
        plain = None
        result = QuotedPrintableCodec.decodeQuotedPrintable(plain)
        self.assertIsNone(result, "Result should be null")

    def testDecodeWithNullArray_test0_decomposed(self) -> None:
        plain = None
        result = QuotedPrintableCodec.decodeQuotedPrintable(plain)
        self.assertIsNone(result)

    def testEncodeUrlWithNullBitSet_test3_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        plain_bytes = plain.encode("utf-8")
        encoded_bytes = QuotedPrintableCodec.encodeQuotedPrintable1(
            None, list(plain_bytes)
        )
        encoded = "".join(map(chr, encoded_bytes))
        self.assertEqual("1+1 =3D 2", encoded, "Basic quoted-printable encoding test")
        decoded = qpcodec.decode3(encoded)
        self.assertEqual(plain, decoded, "Basic quoted-printable decoding test")

    def testEncodeUrlWithNullBitSet_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        plain_bytes = plain.encode(CharEncoding.UTF_8)
        encoded = bytes(
            QuotedPrintableCodec.encodeQuotedPrintable1(None, plain_bytes)
        ).decode(CharEncoding.UTF_8)

    def testEncodeUrlWithNullBitSet_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "1+1 = 2"
        plain_bytes = plain.encode("utf-8")

    def testEncodeUrlWithNullBitSet_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testEncodeNull_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = None
        encoded = qpcodec.encode0(plain)
        self.assertIsNone(encoded, "Encoding a null string should return null")

    def testEncodeNull_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = None
        encoded = qpcodec.encode0(plain)

    def testEncodeNull_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testDecodeInvalid_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        with self.assertRaises(
            DecoderException, msg="DecoderException should have been thrown"
        ):
            qpcodec.decode3("=")

        with self.assertRaises(
            DecoderException, msg="DecoderException should have been thrown"
        ):
            qpcodec.decode3("=A")

        with self.assertRaises(
            DecoderException, msg="DecoderException should have been thrown"
        ):
            qpcodec.decode3("=WW")

    def testDecodeInvalid_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertIsNone(
            qpcodec.encode1(None), "Null string quoted-printable encoding test"
        )
        self.assertIsNone(
            qpcodec.decode3(None), "Null string quoted-printable decoding test"
        )

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        self.assertIsNone(
            qpcodec.encode1(None), "Null string quoted-printable encoding test"
        )

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testUnsafeEncodeDecode_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "=\r\n"
        encoded = qpcodec.encode1(plain)
        self.assertEqual(
            "=3D=0D=0A", encoded, "Unsafe chars quoted-printable encoding test"
        )
        self.assertEqual(
            plain,
            qpcodec.decode3(encoded),
            "Unsafe chars quoted-printable decoding test",
        )

    def testUnsafeEncodeDecode_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "=\r\n"
        encoded = qpcodec.encode1(plain)

    def testUnsafeEncodeDecode_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testSafeCharEncodeDecode_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = 'abc123_-.*~!@#$%^&()+{}"\\;:`,/[]'
        encoded = qpcodec.encode1(plain)
        self.assertEqual(plain, encoded, "Safe chars quoted-printable encoding test")
        self.assertEqual(
            plain, qpcodec.decode3(encoded), "Safe chars quoted-printable decoding test"
        )

    def testSafeCharEncodeDecode_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = 'abc123_-.*~!@#$%^&()+{}"\\;:`,/[]'
        encoded = qpcodec.encode1(plain)

    def testSafeCharEncodeDecode_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "= Hello there =\r\n"
        encoded = qpcodec.encode1(plain)
        self.assertEqual(
            "=3D Hello there =3D=0D=0A", encoded, "Basic quoted-printable encoding test"
        )
        self.assertEqual(
            plain, qpcodec.decode3(encoded), "Basic quoted-printable decoding test"
        )

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()
        plain = "= Hello there =\r\n"
        encoded = qpcodec.encode1(plain)

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testUTF8RoundTrip_test5_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        # Test encoding Russian message
        self.assertEqual(
            "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
            qpcodec.encode4(ru_msg, CharEncoding.UTF_8),
        )

        # Test encoding Swiss German message
        self.assertEqual(
            "Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        )

        # Test decoding Russian message
        encoded_ru_msg = qpcodec.encode4(ru_msg, CharEncoding.UTF_8)
        self.assertEqual(ru_msg, qpcodec.decode2(encoded_ru_msg, CharEncoding.UTF_8))

        # Test decoding Swiss German message
        encoded_ch_msg = qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        self.assertEqual(ch_msg, qpcodec.decode2(encoded_ch_msg, CharEncoding.UTF_8))

    def testUTF8RoundTrip_test4_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        self.assertEqual(
            "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
            qpcodec.encode4(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        )

        self.assertEqual(
            ru_msg,
            qpcodec.decode2(
                qpcodec.encode4(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

    def testUTF8RoundTrip_test3_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        self.assertEqual(
            "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
            qpcodec.encode4(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        )

        qpcodec.encode4(ru_msg, CharEncoding.UTF_8)

        self.assertEqual(
            ru_msg,
            qpcodec.decode2(
                qpcodec.encode4(ru_msg, CharEncoding.UTF_8), CharEncoding.UTF_8
            ),
        )

    def testUTF8RoundTrip_test2_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

        self.assertEqual(
            "=D0=92=D1=81=D0=B5=D0=BC_=D0=BF=D1=80=D0=B8=D0=B2=D0=B5=D1=82",
            qpcodec.encode4(ru_msg, CharEncoding.UTF_8),
        )
        self.assertEqual(
            "Gr=C3=BCezi_z=C3=A4m=C3=A4", qpcodec.encode4(ch_msg, CharEncoding.UTF_8)
        )
        qpcodec.encode4(ru_msg, CharEncoding.UTF_8)

    def testUTF8RoundTrip_test1_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)
        qpcodec = QuotedPrintableCodec.QuotedPrintableCodec4()

    def testUTF8RoundTrip_test0_decomposed(self) -> None:
        ru_msg = self.__constructString(self.RUSSIAN_STUFF_UNICODE)
        ch_msg = self.__constructString(self.SWISS_GERMAN_STUFF_UNICODE)

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        buffer = []
        if unicodeChars is not None:
            for unicodeChar in unicodeChars:
                buffer.append(chr(unicodeChar))
        return "".join(buffer)
