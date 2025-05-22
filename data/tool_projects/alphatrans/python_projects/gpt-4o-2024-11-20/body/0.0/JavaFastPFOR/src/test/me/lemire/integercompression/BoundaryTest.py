from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *


class BoundaryTest(unittest.TestCase):

    def testComposition_test1_decomposed(self) -> None:
        c = Composition(BinaryPacking(), VariableByte())
        self.__testBoundary(c)

    def testComposition_test0_decomposed(self) -> None:
        c = Composition(BinaryPacking(), VariableByte())

    def testIntegratedComposition_test1_decomposed(self) -> None:
        c = IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        self.__testBoundary(c)

    def testIntegratedComposition_test0_decomposed(self) -> None:
        c = IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())

    @staticmethod
    def __testBoundary(c: IntegerCODEC) -> None:
        BoundaryTest.__around32(c)
        BoundaryTest.__around128(c)
        BoundaryTest.__around256(c)

    @staticmethod
    def __around256(c: IntegerCODEC) -> None:
        BoundaryTest.__compressAndUncompress(255, c)
        BoundaryTest.__compressAndUncompress(256, c)
        BoundaryTest.__compressAndUncompress(257, c)

    @staticmethod
    def __around128(c: IntegerCODEC) -> None:
        BoundaryTest.__compressAndUncompress(127, c)
        BoundaryTest.__compressAndUncompress(128, c)
        BoundaryTest.__compressAndUncompress(129, c)

    @staticmethod
    def __around32(c: IntegerCODEC) -> None:
        BoundaryTest.__compressAndUncompress(31, c)
        BoundaryTest.__compressAndUncompress(32, c)
        BoundaryTest.__compressAndUncompress(33, c)

    @staticmethod
    def __compressAndUncompress(length: int, c: IntegerCODEC) -> None:
        # Initialize array
        source = [i for i in range(length)]

        # Compress an array
        compressed = [0] * length
        c_inpos = IntWrapper(0)
        c_outpos = IntWrapper(0)
        c.compress0(source, c_inpos, len(source), compressed, c_outpos)
        assert c_outpos.get() <= length

        # Uncompress an array
        uncompressed = [0] * length
        u_inpos = IntWrapper(0)
        u_outpos = IntWrapper(0)
        c.uncompress0(compressed, u_inpos, c_outpos.get(), uncompressed, u_outpos)

        # Compare between uncompressed and original arrays
        target = uncompressed[: u_outpos.get()]
        if source != target:
            print(f"Problem with length = {length} and {c}")
            print(f"Source: {source}")
            print(f"Target: {target}")

        assert source == target
