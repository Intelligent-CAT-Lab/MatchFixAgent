from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *


class MimeUtilityTestCase(unittest.TestCase):

    def testdecodeInvalidEncoding_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            MimeUtility.decodeText("=?invalid?B?xyz-?=")

    def testdecodeIso88591Base64EncodedWithWhiteSpace_test0_decomposed(self) -> None:
        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
            + '   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    def testdecodeIso88591Base64Encoded_test0_decomposed(self) -> None:
        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    def testdecodeUtf8Base64Encoded_test0_decomposed(self) -> None:
        self.__assertEncoded(
            " h\u00e9! \u00e0\u00e8\u00f4u !!!", "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
        )

    def testdecodeUtf8QuotedPrintableEncoded_test0_decomposed(self) -> None:
        self.__assertEncoded(
            " h\u00e9! \u00e0\u00e8\u00f4u !!!",
            "=?UTF-8?Q?_h=C3=A9!_=C3=A0=C3=A8=C3=B4u_!!!?=",
        )

    def testnoNeedToDecode_test0_decomposed(self) -> None:
        self.__assertEncoded("abc", "abc")

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:
        decoded = MimeUtility.decodeText(encoded)
        assert expected == decoded, f"Expected '{expected}' but got '{decoded}'"
