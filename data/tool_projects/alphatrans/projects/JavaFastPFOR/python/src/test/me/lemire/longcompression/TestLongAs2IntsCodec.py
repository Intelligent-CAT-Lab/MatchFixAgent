from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.longcompression.ByteLongCODEC import *
from src.main.me.lemire.longcompression.LongAs2IntsCodec import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class TestLongAs2IntsCodec(unittest.TestCase):

    codec: LongAs2IntsCodec = LongAs2IntsCodec.LongAs2IntsCodec1()

    def testCodec_intermediateHighPowerOfTwo_test0_decomposed(self) -> None:
        self.assertEqual(3, len(LongTestUtils._compress1(self.codec, [1 << 42])))

    def testCodec_ZeroThenAllPowerOfTwo_test0_decomposed(self) -> None:
        for i in range(64):
            self.__checkConsistency(self.codec, [0, 1 << i])

    def testCodec_allPowerOfTwo_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [1 << 42])
        for i in range(64):
            self.__checkConsistency(self.codec, [1 << i])

    def testCodec_ZeroMinValue_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [0, -9223372036854775808])

    def testCodec_MinValue_test0_decomposed(self) -> None:
        self.__checkConsistency(
            self.codec, [-(2**63)]
        )  # -9223372036854775808 in Java is -(2^63)

    def testCodec_ZeroTimes128Minus1_test0_decomposed(self) -> None:
        array = list(range(0, 128)) + [-1]
        array = [0] * len(
            array
        )  # Replace all elements in the range with 0, except the last element which is -1
        array[-1] = -1
        self.__checkConsistency(self.codec, array)

    def testCodec_ZeroTimes127Minus1_test0_decomposed(self) -> None:
        array = list(range(0, 127)) + [-1]
        array = [0] * len(
            array
        )  # Replace all elements in the range with 0, except the last element (-1)
        array[-1] = -1
        self.__checkConsistency(self.codec, array)

    def testCodec_ZeroTimes8Minus1_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [0, 0, 0, 0, 0, 0, 0, 0, -1])

    def testCodec_Minus1_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [-1])

    def testCodec_Zero_test0_decomposed(self) -> None:
        self.__checkConsistency(self.codec, [0])

    def __checkConsistency(self, codec: LongCODEC, array: typing.List[int]) -> None:
        # First block: General compression and decompression
        compressed = LongTestUtils._compress1(codec, array)
        uncompressed = LongTestUtils._uncompress0(codec, compressed, len(array))
        self.assertEqual(array, uncompressed)

        # Second block: If codec is an instance of ByteLongCODEC
        if isinstance(codec, ByteLongCODEC):
            compressed = LongTestUtils._compress0(codec, array)
            uncompressed = LongTestUtils._uncompress1(codec, compressed, len(array))
            self.assertEqual(array, uncompressed)

        # Third block: If codec is an instance of SkippableLongCODEC
        if isinstance(codec, SkippableLongCODEC):
            compressed = LongTestUtils._compressHeadless(codec, array)
            uncompressed = LongTestUtils._uncompressHeadless(
                codec, compressed, len(array)
            )
            self.assertEqual(array, uncompressed)
