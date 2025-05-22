from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.digest.B64 import *


class B64Test(unittest.TestCase):

    def testB64from24bit_test2_decomposed(self) -> None:
        buffer = io.StringIO()  # Using StringIO to mimic StringBuilder behavior
        B64.b64from24bit(8, 16, 64, 2, buffer)
        B64.b64from24bit(7, 77, 120, 4, buffer)
        self.assertEqual("./spo/", buffer.getvalue())  # Compare the resulting string

    def testB64from24bit_test1_decomposed(self) -> None:
        buffer = io.StringIO("")
        B64.b64from24bit(8, 16, 64, 2, buffer)
        B64.b64from24bit(7, 77, 120, 4, buffer)

    def testB64from24bit_test0_decomposed(self) -> None:
        buffer = io.StringIO("")
        B64.b64from24bit(8, 16, 64, 2, buffer)

    def testB64T_test1_decomposed(self) -> None:
        self.assertIsNotNone(B64())
        self.assertEqual(64, len(B64.B64T_ARRAY))

    def testB64T_test0_decomposed(self) -> None:
        self.assertIsNotNone(B64())
