from __future__ import annotations
import re
import itertools
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.longcompression.ByteLongCODEC import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class TestLongVariableByte(unittest.TestCase):

    codec: LongVariableByte = LongVariableByte()

    def testCodec_intermediateHighPowerOfTwo_test2_decomposed(self) -> None:
        self.assertEqual(1, len(LongTestUtils._compress1(self.codec, [1 << 42])))
        self.assertEqual(7, len(LongTestUtils._compress0(self.codec, [1 << 42])))
        self.assertEqual(1, len(LongTestUtils._compressHeadless(self.codec, [1 << 42])))

    def testCodec_intermediateHighPowerOfTwo_test1_decomposed(self) -> None:
        self.assertEqual(1, len(LongTestUtils._compress1(self.codec, [1 << 42])))
        self.assertEqual(7, len(LongTestUtils._compress0(self.codec, [1 << 42])))

    def testCodec_intermediateHighPowerOfTwo_test0_decomposed(self) -> None:
        self.assertEqual(1, len(LongTestUtils._compress1(self.codec, [1 << 42])))

    def testCodec_ZeroThenAllPowerOfTwo_test0_decomposed(self) -> None:
        for i in range(64):
            self.__checkConsistency(self.codec, [0, 1 << i])

    def testCodec_allPowerOfTwo_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [1 << 42])
        for i in range(64):
            self.__checkConsistency(self.codec, [1 << i])

    def testCodec_ZeroMinValue_test0_decomposed(self) -> None:
        self.__checkConsistency(
            self.codec, [0, -9223372036854775808]
        )  # -9223372036854775808 in Python

    def testCodec_MinValue_test0_decomposed(self) -> None:
        self.__checkConsistency(
            self.codec, [-(2**63)]
        )  # -9223372036854775808 in Java is -(2^63)

    def testCodec_ZeroTimes128Minus1_test0_decomposed(self) -> None:
        array = [0] * 128 + [-1]
        self.__checkConsistency(self.codec, array)

    def testCodec_ZeroTimes127Minus1_test0_decomposed(self) -> None:
        array = list(itertools.chain((0 for _ in range(127)), [-1]))
        self.__checkConsistency(self.codec, array)

    def testCodec_ZeroTimes8Minus1_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [0, 0, 0, 0, 0, 0, 0, 0, -1])

    def testCodec_ZeroMinus1_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [-1])

    def __checkConsistency(self, codec: LongCODEC, array: typing.List[int]) -> None:
        # First block: General compression and decompression
        compressed = LongTestUtils._compress1(codec, array)
        uncompressed = LongTestUtils._uncompress0(codec, compressed, len(array))
        self.assertListEqual(array, uncompressed)

        # Second block: If codec is an instance of ByteLongCODEC
        if isinstance(codec, ByteLongCODEC):
            compressed = LongTestUtils._compress0(codec, array)
            uncompressed = LongTestUtils._uncompress1(codec, compressed, len(array))
            self.assertListEqual(array, uncompressed)

        # Third block: If codec is an instance of SkippableLongCODEC
        if isinstance(codec, SkippableLongCODEC):
            compressed = LongTestUtils._compressHeadless(codec, array)
            uncompressed = LongTestUtils._uncompressHeadless(
                codec, compressed, len(array)
            )
            self.assertListEqual(array, uncompressed)
