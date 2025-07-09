from __future__ import annotations
import math
import re
from io import BytesIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *


class QuotedPrintableDecoderTestCase(unittest.TestCase):

    __US_ASCII_CHARSET: str = "US-ASCII"

    def testtruncatedEscape_test0_decomposed(self) -> None:
        self.__assertOSError("truncated", "=1")

    def testinvalidSoftBreak2_test0_decomposed(self) -> None:
        self.__assertOSError("CR must be followed by LF", "=\r\n")

    def testinvalidSoftBreak1_test0_decomposed(self) -> None:
        self.__assertOSError("CR must be followed by LF", "=\r\r")

    def testsoftLineBreakDecode_test0_decomposed(self) -> None:
        self.__assertEncoded(
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy.",
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            + "mathematics is the most beautiful branch of philosophy.",
        )

    def testinvalidCharDecode_test0_decomposed(self) -> None:
        with pytest.raises(
            io.UnsupportedOperation
        ):  # Assuming OSError maps to io.UnsupportedOperation
            self.__assertEncoded("=\r\n", "=3D=XD=XA")

    def testunsafeDecodeLowerCase_test0_decomposed(self) -> None:
        self.__assertEncoded("=\r\n", "=3d=0d=0a")

    def testunsafeDecode_test0_decomposed(self) -> None:
        self.__assertEncoded("=\r\n", "=3D=0D=0A")

    def testinvalidQuotedPrintableEncoding_test0_decomposed(self) -> None:
        self.__assertOSError(
            "truncated escape sequence",
            "YWJjMTIzXy0uKn4hQCMkJV4mKCkre31cIlxcOzpgLC9bXQ==",
        )

    def testbasicEncodeDecode_test0_decomposed(self) -> None:
        self.__assertEncoded("= Hello there =\r\n", "=3D Hello there =3D=0D=0A")

    def testplainDecode_test0_decomposed(self) -> None:
        self.__assertEncoded(
            "The quick brown fox jumps over the lazy dog.",
            "The quick brown fox jumps over the lazy dog.",
        )

    def testemptyDecode_test0_decomposed(self) -> None:
        self.__assertEncoded("", "")

    @staticmethod
    def __assertOSError(messageText: str, encoded: str) -> None:
        out = io.BytesIO()
        encoded_data = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        try:
            QuotedPrintableDecoder.decode(encoded_data, out)
            pytest.fail("Expected IOError")
        except IOError as e:
            em = str(e)
            assert messageText in em, f"Expected to find '{messageText}' in '{em}'"

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)

        out = io.BytesIO()
        encodedData = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        QuotedPrintableDecoder.decode(encodedData, out)
        actual = out.getvalue()

        assert expected == actual, f"Expected {expected}, but got {actual}"
