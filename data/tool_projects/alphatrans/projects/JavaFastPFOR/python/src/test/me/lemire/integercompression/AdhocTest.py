from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class AdhocTest(unittest.TestCase):

    def testbiggerCompressedArray2_test3_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [65535] * 65535)
        c = Composition(FastPFOR.FastPFOR1(), VariableByte())
        TestUtils.assertSymmetry(c, [65535] * 65535)

    def testbiggerCompressedArray2_test2_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [65535] * 65535)
        c = Composition(FastPFOR.FastPFOR1(), VariableByte())

    def testbiggerCompressedArray2_test1_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [65535, 65535])

    def testbiggerCompressedArray2_test0_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())

    def testbiggerCompressedArray1_test1_decomposed(self) -> None:
        c = VariableByte()
        TestUtils.assertSymmetry(c, [-1])

    def testbiggerCompressedArray1_test0_decomposed(self) -> None:
        c = VariableByte()

    def testbiggerCompressedArray0_test3_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [0] * 16384)
        c = Composition(FastPFOR.FastPFOR1(), VariableByte())
        TestUtils.assertSymmetry(c, [0] * 16384)

    def testbiggerCompressedArray0_test2_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [0] * 16384)
        c = Composition(FastPFOR.FastPFOR1(), VariableByte())

    def testbiggerCompressedArray0_test1_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        TestUtils.assertSymmetry(c, [0] * 16384)

    def testbiggerCompressedArray0_test0_decomposed(self) -> None:
        c = Composition(FastPFOR128.FastPFOR1281(), VariableByte())

    def testIssue41_test0_decomposed(self) -> None:
        for x in range(64):
            a = [2, 3, 4, 5]
            b = [0] * 90
            c = [0] * len(a)
            codec = SkippableIntegratedComposition(
                IntegratedBinaryPacking(), IntegratedVariableByte()
            )
            a_offset = IntWrapper(0)
            b_offset = IntWrapper(x)
            init_value = IntWrapper(0)

            # Compress
            codec.headlessCompress(a, a_offset, len(a), b, b_offset, init_value)
            length = b_offset.get() - x
            b_offset.set_(x)

            # Uncompress
            c_offset = IntWrapper(0)
            init_value = IntWrapper(0)
            codec.headlessUncompress(
                b, b_offset, length, c, c_offset, len(a), init_value
            )

            # Assert that the original array and the decompressed array are equal
            self.assertListEqual(a, c)

    def testIssue29b_test0_decomposed(self) -> None:
        for x in range(64):
            a = [2, 3, 4, 5]
            b = [0] * 90
            c = [0] * len(a)
            codec = SkippableComposition(BinaryPacking(), VariableByte())
            a_offset = IntWrapper(0)
            b_offset = IntWrapper(x)

            # Compress
            codec.headlessCompress(a, a_offset, len(a), b, b_offset)
            length = b_offset.get() - x

            # Reset b_offset for decompression
            b_offset.set_(x)
            c_offset = IntWrapper(0)

            # Decompress
            codec.headlessUncompress(b, b_offset, length, c, c_offset, len(a))

            # Assert that the decompressed array matches the original
            self.assertListEqual(
                a, c, "Decompressed array does not match the original array"
            )

    def testIssue29_test0_decomposed(self) -> None:
        for x in range(64):
            a = [2, 3, 4, 5]
            b = [0] * 90
            c = [0] * len(a)
            codec = Composition(BinaryPacking(), VariableByte())

            a_offset = IntWrapper(0)
            b_offset = IntWrapper(x)
            codec.compress0(a, a_offset, len(a), b, b_offset)
            length = b_offset.get() - x
            b_offset.set_(x)
            c_offset = IntWrapper(0)
            codec.uncompress0(b, b_offset, length, c, c_offset)
            self.assertListEqual(
                a, c, "Decompressed array does not match the original array"
            )
