from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.Charsets import *


class CharsetsTest(unittest.TestCase):

    def testUtf8_test0_decomposed(self) -> None:
        self.assertEqual("UTF-8", Charsets.UTF_8)

    def testUtf16Le_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16LE", Charsets.UTF_16LE)

    def testUtf16Be_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16BE", Charsets.UTF_16BE)

    def testUtf16_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16", Charsets.UTF_16)

    def testUsAscii_test0_decomposed(self) -> None:
        self.assertEqual("US-ASCII", Charsets.US_ASCII)

    def testIso8859_1_test0_decomposed(self) -> None:
        self.assertEqual("ISO-8859-1", Charsets.ISO_8859_1)

    def testToCharset_test1_decomposed(self) -> None:
        self.assertEqual(io.TextIOWrapper().encoding, Charsets.toCharset1(None))
        self.assertEqual(io.TextIOWrapper().encoding, Charsets.toCharset0(None))
        self.assertEqual(
            io.TextIOWrapper().encoding,
            Charsets.toCharset0(io.TextIOWrapper().encoding),
        )
        self.assertEqual(Charsets.UTF_8, Charsets.toCharset0(Charsets.UTF_8))

    def testToCharset_test0_decomposed(self) -> None:
        self.assertEqual(os.device_encoding(0), Charsets.toCharset1(None))
