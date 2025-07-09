from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *


class CharEncodingTest(unittest.TestCase):

    def testUtf8_test0_decomposed(self) -> None:
        self.assertEqual("UTF-8", CharEncoding.UTF_8)

    def testUtf16Le_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16LE", CharEncoding.UTF_16LE)

    def testUtf16Be_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16BE", CharEncoding.UTF_16BE)

    def testUtf16_test0_decomposed(self) -> None:
        self.assertEqual("UTF-16", CharEncoding.UTF_16)

    def testUsAscii_test0_decomposed(self) -> None:
        self.assertEqual("US-ASCII", CharEncoding.US_ASCII)

    def testIso8859_1_test0_decomposed(self) -> None:
        self.assertEqual("ISO-8859-1", CharEncoding.ISO_8859_1)

    def testConstructor_test0_decomposed(self) -> None:
        CharEncoding()
