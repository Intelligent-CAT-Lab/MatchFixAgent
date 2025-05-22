from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.integercompression.DeltaZigzagEncoding import *


class DeltaZigzagEncodingTest(unittest.TestCase):

    def testcheckSpots_test1_decomposed(self) -> None:
        c = SpotChecker()
        c.check(0)
        c.check(1)
        c.check(1375228800)
        c.check(1 << 30)
        c.check(1 << 31)

    def testcheckSpots_test0_decomposed(self) -> None:
        c = SpotChecker()

    def testcheckDecodeSimple_test1_decomposed(self) -> None:
        d = Decoder(0)
        self._checkDecode(
            d, [0, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def testcheckDecodeSimple_test0_decomposed(self) -> None:
        d = Decoder(0)

    def testcheckEncodeSimple_test1_decomposed(self) -> None:
        e = Encoder(0)
        self._checkEncode(
            e, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        )

    def testcheckEncodeSimple_test0_decomposed(self) -> None:
        e = Encoder(0)

    def testcheckZigzagDecoder_test1_decomposed(self) -> None:
        d = Decoder(0)
        self.assertEqual(0, self._zigzagDecode(d, 0))
        self.assertEqual(-1, self._zigzagDecode(d, 1))
        self.assertEqual(1, self._zigzagDecode(d, 2))
        self.assertEqual(-2, self._zigzagDecode(d, 3))
        self.assertEqual(2, self._zigzagDecode(d, 4))
        self.assertEqual(-3, self._zigzagDecode(d, 5))

    def testcheckZigzagDecoder_test0_decomposed(self) -> None:
        d = Decoder(0)

    def testcheckZigzagEncode_test1_decomposed(self) -> None:
        e = Encoder(0)
        self.assertEqual(0, self._zigzagEncode(e, 0))
        self.assertEqual(2, self._zigzagEncode(e, 1))
        self.assertEqual(4, self._zigzagEncode(e, 2))
        self.assertEqual(6, self._zigzagEncode(e, 3))
        self.assertEqual(1, self._zigzagEncode(e, -1))
        self.assertEqual(3, self._zigzagEncode(e, -2))
        self.assertEqual(5, self._zigzagEncode(e, -3))

    def testcheckZigzagEncode_test0_decomposed(self) -> None:
        e = DeltaZigzagEncoding.Encoder(0)

    @staticmethod
    def _checkDecode(
        d: Decoder, data: typing.List[int], expected: typing.List[int]
    ) -> None:
        r = d.decodeArray2(data)
        unittest.TestCase().assertListEqual(expected, r)
        unittest.TestCase().assertEqual(r[-1], d.getContextValue())

    @staticmethod
    def _checkEncode(
        e: Encoder, data: typing.List[int], expected: typing.List[int]
    ) -> None:
        # Assert that the encoded array matches the expected array
        unittest.TestCase().assertListEqual(expected, e.encodeArray3(data))
        # Assert that the last value in the data matches the context value
        unittest.TestCase().assertEqual(data[-1], e.getContextValue())

    @staticmethod
    def _zigzagDecode(d: Decoder, value: int) -> int:
        d.setContextValue(0)
        return d.decodeInt(value)

    @staticmethod
    def _zigzagEncode(e: Encoder, value: int) -> int:
        e.setContextValue(0)
        return e.encodeInt(value)


class SpotChecker:

    __decoder: Decoder = None  # LLM could not translate this field

    __encoder: Encoder = None  # LLM could not translate this field

    def check(self, value: int) -> None:
        self.__encoder.setContextValue(0)
        self.__decoder.setContextValue(0)
        value2 = self.__decoder.decodeInt(self.__encoder.encodeInt(value))
        assert value == value2, f"Expected {value}, but got {value2}"
