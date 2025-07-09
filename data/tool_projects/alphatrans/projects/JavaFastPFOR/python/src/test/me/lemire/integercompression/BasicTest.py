from __future__ import annotations
import time
import copy
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.GroupSimple9 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *


class BasicTest(unittest.TestCase):

    codecs: typing.List[IntegerCODEC] = [
        IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte()),
        JustCopy(),
        VariableByte(),
        GroupSimple9(),
        IntegratedVariableByte(),
        Composition(BinaryPacking(), VariableByte()),
        Composition(NewPFD(), VariableByte()),
        Composition(NewPFDS16(), VariableByte()),
        Composition(OptPFDS9(), VariableByte()),
        Composition(OptPFDS16(), VariableByte()),
        Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
        Composition(FastPFOR.FastPFOR1(), VariableByte()),
        Simple9(),
        Simple16(),
        GroupSimple9(),
        Composition(XorBinaryPacking(), VariableByte()),
        Composition(DeltaZigzagBinaryPacking(), DeltaZigzagVariableByte()),
    ]

    def testfastPfor128Test_test3_decomposed(self) -> None:
        codec1 = FastPFOR128.FastPFOR1281()
        codec2 = FastPFOR128.FastPFOR1281()
        N = FastPFOR128.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data[:N])
        answer = TestUtils._uncompress0(codec2, comp, N)
        for k in range(N):
            if answer[k] != data[k]:
                raise RuntimeError(f"bug {k} {answer[k]} != {data[k]}")

    def testfastPfor128Test_test2_decomposed(self) -> None:
        codec1 = FastPFOR128.FastPFOR1281()
        codec2 = FastPFOR128.FastPFOR1281()
        N = FastPFOR128.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data[:N])
        answer = TestUtils._uncompress0(codec2, comp, N)

    def testfastPfor128Test_test1_decomposed(self) -> None:
        codec1 = FastPFOR128.FastPFOR1281()
        codec2 = FastPFOR128.FastPFOR1281()
        N = FastPFOR128.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data.copy())

    def testfastPfor128Test_test0_decomposed(self) -> None:
        codec1 = FastPFOR128.FastPFOR1281()
        codec2 = FastPFOR128.FastPFOR1281()

    def testfastPforTest_test3_decomposed(self) -> None:
        codec1 = FastPFOR.FastPFOR1()
        codec2 = FastPFOR.FastPFOR1()
        N = FastPFOR.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data[:N])
        answer = TestUtils._uncompress0(codec2, comp, N)
        for k in range(N):
            if answer[k] != data[k]:
                raise RuntimeError(f"bug {k} {answer[k]} != {data[k]}")

    def testfastPforTest_test2_decomposed(self) -> None:
        codec1 = FastPFOR.FastPFOR1()
        codec2 = FastPFOR.FastPFOR1()
        N = FastPFOR.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data[:N])
        answer = TestUtils._uncompress0(codec2, comp, N)

    def testfastPforTest_test1_decomposed(self) -> None:
        codec1 = FastPFOR.FastPFOR1()
        codec2 = FastPFOR.FastPFOR1()
        N = FastPFOR.BLOCK_SIZE
        data = [0] * N
        data[126] = -1
        comp = TestUtils.compress1(codec1, data.copy())

    def testfastPforTest_test0_decomposed(self) -> None:
        codec1 = FastPFOR.FastPFOR1()
        codec2 = FastPFOR.FastPFOR1()

    def testUnsortedExample_test44_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted3(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted3(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted2(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted2(Composition(IntegratedBinaryPacking(), VariableByte()))

    def testUnsortedExample_test43_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted3(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted3(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted2(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )

    def testUnsortedExample_test42_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted3(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted3(Composition(FastPFOR.FastPFOR1(), VariableByte()))

    def testUnsortedExample_test41_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted3(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()

    def testUnsortedExample_test40_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted3(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))

    def testUnsortedExample_test39_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()

    def testUnsortedExample_test38_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS16(), VariableByte()))

    def testUnsortedExample_test37_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFDS9(), VariableByte()))

    def testUnsortedExample_test36_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted3(Composition(OptPFD(), VariableByte()))

    def testUnsortedExample_test35_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS16(), VariableByte()))

    def testUnsortedExample_test34_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFDS9(), VariableByte()))

    def testUnsortedExample_test33_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted3(Composition(NewPFD(), VariableByte()))

    def testUnsortedExample_test32_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())
        self.__testUnsorted3(Composition(BinaryPacking(), VariableByte()))

    def testUnsortedExample_test31_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())
        self.__testUnsorted3(IntegratedVariableByte())

    def testUnsortedExample_test30_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted3(VariableByte())

    def testUnsortedExample_test29_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.__testUnsorted3(Composition(IntegratedBinaryPacking(), VariableByte()))

    def testUnsortedExample_test28_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testUnsorted3(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )

    def testUnsortedExample_test27_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.__testUnsorted2(Composition(FastPFOR.FastPFOR1(), VariableByte()))

    def testUnsortedExample_test26_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()

    def testUnsortedExample_test25_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testUnsorted2(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))

    def testUnsortedExample_test24_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()

    def testUnsortedExample_test23_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS16(), VariableByte()))

    def testUnsortedExample_test22_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFDS9(), VariableByte()))

    def testUnsortedExample_test21_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))
        self.__testUnsorted2(Composition(OptPFD(), VariableByte()))

    def testUnsortedExample_test20_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS16(), VariableByte()))

    def testUnsortedExample_test19_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFDS9(), VariableByte()))

    def testUnsortedExample_test18_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))
        self.__testUnsorted2(Composition(NewPFD(), VariableByte()))

    def testUnsortedExample_test17_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())
        self.__testUnsorted2(Composition(BinaryPacking(), VariableByte()))

    def testUnsortedExample_test16_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())
        self.__testUnsorted2(IntegratedVariableByte())

    def testUnsortedExample_test15_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testUnsorted2(VariableByte())

    def testUnsortedExample_test14_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )
        self.testUnsorted(Composition(IntegratedBinaryPacking(), VariableByte()))

    def testUnsortedExample_test13_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.testUnsorted(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )

    def testUnsortedExample_test12_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        fast_pfor_128_instance = FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(fast_pfor_128_instance, VariableByte()))
        fast_pfor_instance = FastPFOR.FastPFOR1()
        self.testUnsorted(Composition(fast_pfor_instance, VariableByte()))

    def testUnsortedExample_test11_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(FastPFOR128.FastPFOR1281(), VariableByte()))
        FastPFOR.FastPFOR1()

    def testUnsortedExample_test10_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        fast_pfor_instance = FastPFOR128.FastPFOR1281()
        self.testUnsorted(Composition(fast_pfor_instance, VariableByte()))

    def testUnsortedExample_test9_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()

    def testUnsortedExample_test8_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS16(), VariableByte()))

    def testUnsortedExample_test7_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))
        self.testUnsorted(Composition(OptPFDS9(), VariableByte()))

    def testUnsortedExample_test6_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))
        self.testUnsorted(Composition(OptPFD(), VariableByte()))

    def testUnsortedExample_test5_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS16(), VariableByte()))

    def testUnsortedExample_test4_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))
        self.testUnsorted(Composition(NewPFDS9(), VariableByte()))

    def testUnsortedExample_test3_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))
        self.testUnsorted(Composition(NewPFD(), VariableByte()))

    def testUnsortedExample_test2_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())
        self.testUnsorted(Composition(BinaryPacking(), VariableByte()))

    def testUnsortedExample_test1_decomposed(self) -> None:
        self.testUnsorted(VariableByte())
        self.testUnsorted(IntegratedVariableByte())

    def testUnsortedExample_test0_decomposed(self) -> None:
        self.testUnsorted(VariableByte())

    def testzeroinzerouttest_test26_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(
            Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        )
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(Composition(FastPFOR.FastPFOR1(), VariableByte()))
        self.__testZeroInZeroOut(
            IntegratedComposition(IntegratedBinaryPacking(), IntegratedVariableByte())
        )

    def testzeroinzerouttest_test25_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(
            Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        )
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(Composition(FastPFOR.FastPFOR1(), VariableByte()))

    def testzeroinzerouttest_test24_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(
            Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        )
        FastPFOR.FastPFOR1()

    def testzeroinzerouttest_test23_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(
            Composition(FastPFOR128.FastPFOR1281(), VariableByte())
        )

    def testzeroinzerouttest_test22_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))
        FastPFOR128.FastPFOR1281()

    def testzeroinzerouttest_test21_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS16(), VariableByte()))

    def testzeroinzerouttest_test20_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFDS9(), VariableByte()))

    def testzeroinzerouttest_test19_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))
        self.__testZeroInZeroOut(Composition(OptPFD(), VariableByte()))

    def testzeroinzerouttest_test18_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS16(), VariableByte()))

    def testzeroinzerouttest_test17_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFDS9(), VariableByte()))

    def testzeroinzerouttest_test16_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(NewPFD(), VariableByte()))

    def testzeroinzerouttest_test15_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))
        self.__testZeroInZeroOut(Composition(BinaryPacking(), VariableByte()))

    def testzeroinzerouttest_test14_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())
        self.__testZeroInZeroOut(Composition(IntegratedBinaryPacking(), VariableByte()))

    def testzeroinzerouttest_test13_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())
        self.__testZeroInZeroOut(VariableByte())

    def testzeroinzerouttest_test12_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()
        self.__testZeroInZeroOut(FastPFOR.FastPFOR1())

    def testzeroinzerouttest_test11_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()

    def testzeroinzerouttest_test10_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        self.__testZeroInZeroOut(FastPFOR128.FastPFOR1281())

    def testzeroinzerouttest_test9_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())
        FastPFOR128.FastPFOR1281()

    def testzeroinzerouttest_test8_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())
        self.__testZeroInZeroOut(OptPFDS16())

    def testzeroinzerouttest_test7_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())
        self.__testZeroInZeroOut(OptPFDS9())

    def testzeroinzerouttest_test6_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())
        self.__testZeroInZeroOut(OptPFD())

    def testzeroinzerouttest_test5_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())
        self.__testZeroInZeroOut(NewPFDS16())

    def testzeroinzerouttest_test4_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())
        self.__testZeroInZeroOut(NewPFDS9())

    def testzeroinzerouttest_test3_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())
        self.__testZeroInZeroOut(NewPFD())

    def testzeroinzerouttest_test2_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())
        self.__testZeroInZeroOut(BinaryPacking())

    def testzeroinzerouttest_test1_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())
        self.__testZeroInZeroOut(IntegratedVariableByte())

    def testzeroinzerouttest_test0_decomposed(self) -> None:
        self.__testZeroInZeroOut(IntegratedBinaryPacking())

    def testspuriousouttest_test11_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())
        self.__testSpurious(OptPFDS16())
        self.__testSpurious(FastPFOR128.FastPFOR1281())
        self.__testSpurious(FastPFOR.FastPFOR1())

    def testspuriousouttest_test10_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())
        self.__testSpurious(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testSpurious(FastPFOR128.FastPFOR1281())
        FastPFOR.FastPFOR1()

    def testspuriousouttest_test9_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())
        self.__testSpurious(OptPFDS16())
        FastPFOR128.FastPFOR1281()
        self.__testSpurious(FastPFOR128.FastPFOR1281())

    def testspuriousouttest_test8_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())
        self.__testSpurious(OptPFDS16())
        FastPFOR128.FastPFOR1281()

    def testspuriousouttest_test7_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())
        self.__testSpurious(OptPFDS16())

    def testspuriousouttest_test6_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())
        self.__testSpurious(OptPFDS9())

    def testspuriousouttest_test5_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())
        self.__testSpurious(OptPFD())

    def testspuriousouttest_test4_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())
        self.__testSpurious(NewPFDS16())

    def testspuriousouttest_test3_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())
        self.__testSpurious(NewPFDS9())

    def testspuriousouttest_test2_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())
        self.__testSpurious(NewPFD())

    def testspuriousouttest_test1_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())
        self.__testSpurious(BinaryPacking())

    def testspuriousouttest_test0_decomposed(self) -> None:
        self.__testSpurious(IntegratedBinaryPacking())

    def testbasictest_test0_decomposed(self) -> None:
        self.__test1(5, 10)
        self.__test1(5, 14)
        self.__test1(2, 18)

    def testverifyWithExceptions_test0_decomposed(self) -> None:
        N = 32
        TIMES = 1000
        r = Random()
        data = [0] * N
        compressed = [0] * N
        uncompressed = [0] * N

        for bit in range(31):
            for t in range(TIMES):
                for k in range(N):
                    data[k] = r.randint(
                        0, 2**31 - 1
                    )  # Simulating Java's Random.nextInt()

                BitPacking.fastpack(data, 0, compressed, 0, bit)
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit)

                # Check assertions
                self.maskArray(data, (1 << bit) - 1)
                self.assertEqual(data, uncompressed)

    def testverifyWithoutMask_test0_decomposed(self) -> None:
        N = 32
        TIMES = 1000
        r = Random()
        data = [0] * N
        compressed = [0] * N
        uncompressed = [0] * N

        for bit in range(31):
            for t in range(TIMES):
                for k in range(N):
                    data[k] = r.randint(0, (1 << bit) - 1)
                BitPacking.fastpackwithoutmask(data, 0, compressed, 0, bit)
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit)
                self.assertEqual(uncompressed, data)

    def testverifyBitPacking_test0_decomposed(self) -> None:
        N = 32
        TIMES = 1000
        r = random.Random()
        data = [0] * N
        compressed = [0] * N
        uncompressed = [0] * N

        for bit in range(31):
            for t in range(TIMES):
                for k in range(N):
                    data[k] = r.randint(0, (1 << bit) - 1)
                BitPacking.fastpack(data, 0, compressed, 0, bit)
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit)
                self.assertEqual(uncompressed, data)

    def testcheckXorBinaryPacking3_test2_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())
        co = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())
        self.__test0(c, co, 5, 10)
        self.__test0(c, co, 5, 14)
        self.__test0(c, co, 2, 18)

    def testcheckXorBinaryPacking3_test1_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())
        co = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())

    def testcheckXorBinaryPacking3_test0_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())

    def testcheckXorBinaryPacking2_test1_decomposed(self) -> None:
        codec = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())
        self.testUnsorted(codec)

    def testcheckXorBinaryPacking2_test0_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())

    def testcheckXorBinaryPacking1_test1_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())
        self.__testZeroInZeroOut(c)

    def testcheckXorBinaryPacking1_test0_decomposed(self) -> None:
        c = IntegratedComposition(XorBinaryPacking(), IntegratedVariableByte())

    def testcheckXorBinaryPacking_test1_decomposed(self) -> None:
        self.__testZeroInZeroOut(XorBinaryPacking())
        self.__testSpurious(XorBinaryPacking())

    def testcheckXorBinaryPacking_test0_decomposed(self) -> None:
        self.__testZeroInZeroOut(XorBinaryPacking())

    def testcheckDeltaZigzagPacking_test7_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)

        compo = Composition(DeltaZigzagBinaryPacking(), VariableByte())
        compo2 = Composition(DeltaZigzagBinaryPacking(), VariableByte())

        self.__testZeroInZeroOut(compo)
        self.testUnsorted(compo)
        self.__test0(compo, compo2, 5, 10)
        self.__test0(compo, compo2, 5, 14)
        self.__test0(compo, compo2, 2, 18)

    def testcheckDeltaZigzagPacking_test6_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)

        compo = Composition(DeltaZigzagBinaryPacking(), VariableByte())
        compo2 = Composition(DeltaZigzagBinaryPacking(), VariableByte())

        self.__testZeroInZeroOut(compo)
        self.testUnsorted(compo)

    def testcheckDeltaZigzagPacking_test5_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)

        compo = Composition(DeltaZigzagBinaryPacking(), VariableByte())
        compo2 = Composition(DeltaZigzagBinaryPacking(), VariableByte())

        self.__testZeroInZeroOut(compo)

    def testcheckDeltaZigzagPacking_test4_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)

        compo = Composition(DeltaZigzagBinaryPacking(), VariableByte())
        compo2 = Composition(DeltaZigzagBinaryPacking(), VariableByte())

    def testcheckDeltaZigzagPacking_test3_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)
        compo = Composition(DeltaZigzagBinaryPacking(), VariableByte())

    def testcheckDeltaZigzagPacking_test2_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()
        self.__testZeroInZeroOut(codec)
        self.__testSpurious(codec)

    def testcheckDeltaZigzagPacking_test1_decomposed(self) -> None:
        codec = (
            DeltaZigzagBinaryPacking()
        )  # Instantiate the DeltaZigzagBinaryPacking codec
        self.__testZeroInZeroOut(
            codec
        )  # Call the static helper method to test the codec

    def testcheckDeltaZigzagPacking_test0_decomposed(self) -> None:
        codec = DeltaZigzagBinaryPacking()

    def testcheckDeltaZigzagVB_test3_decomposed(self) -> None:
        codec = DeltaZigzagVariableByte()
        codeco = DeltaZigzagVariableByte()
        self.__testZeroInZeroOut(codec)
        self.__test0(codec, codeco, 5, 10)
        self.__test0(codec, codeco, 5, 14)
        self.__test0(codec, codeco, 2, 18)

    def testcheckDeltaZigzagVB_test2_decomposed(self) -> None:
        codec = DeltaZigzagVariableByte()
        codeco = DeltaZigzagVariableByte()
        self.__testZeroInZeroOut(codec)

    def testcheckDeltaZigzagVB_test1_decomposed(self) -> None:
        codec = DeltaZigzagVariableByte()
        codeco = DeltaZigzagVariableByte()

    def testcheckDeltaZigzagVB_test0_decomposed(self) -> None:
        codec = DeltaZigzagVariableByte()

    def testvaryingLengthTest2_test0_decomposed(self) -> None:
        N = 128
        data = [0] * N
        data[127] = -1

        for codec in self.codecs:
            print(f"[BasicTest.varyingLengthTest2] codec = {codec}")
            try:
                # CODEC Simple9 is limited to "small" integers.
                if isinstance(codec, Simple9):
                    continue
            except Exception as e:
                print(e)

            try:
                # CODEC Simple16 is limited to "small" integers.
                if isinstance(codec, Simple16):
                    continue
            except Exception as e:
                print(e)

            try:
                # CODEC GroupSimple9 is limited to "small" integers.
                if isinstance(codec, GroupSimple9):
                    continue
            except Exception as e:
                print(e)

            for L in range(1, 129):
                comp = TestUtils.compress1(codec, data[:L])
                answer = TestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")

            L = 128
            while L <= N:
                comp = TestUtils.compress1(codec, data[:L])
                answer = TestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testvaryingLengthTest_test0_decomposed(self) -> None:
        N = 4096
        data = [k for k in range(N)]
        for codec in self.codecs:
            print(f"[BasicTest.varyingLengthTest] codec = {codec}")
            for L in range(1, 129):  # L from 1 to 128 inclusive
                comp = TestUtils.compress1(codec, data[:L])
                answer = TestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
            L = 128
            while L <= N:
                comp = TestUtils.compress1(codec, data[:L])
                answer = TestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        print(answer[:L])
                        print(data[:L])
                        raise RuntimeError("bug")
                L *= 2

    def testsaulTest_test0_decomposed(self) -> None:
        for codec in self.codecs:
            for x in range(50):
                a = [2, 3, 4, 5]
                b = [0] * 90
                c = [0] * len(a)

                a_offset = IntWrapper(0)
                b_offset = IntWrapper(x)
                codec.compress0(a, a_offset, len(a), b, b_offset)
                length = b_offset.get() - x

                b_offset.set_(x)
                c_offset = IntWrapper(0)
                codec.uncompress0(b, b_offset, length, c, c_offset)

                if a != c:
                    print(f"Problem with {codec}")

                self.assertEqual(a, c)

    def testUnsorted(self, codec: IntegerCODEC) -> None:
        lengths = [133, 1026, 1333333]
        for N in lengths:
            data = [3] * N
            # initialize the data (most will be small)
            for k in range(0, N, 5):
                data[k] = 100
            for k in range(0, N, 533):
                data[k] = 10000
            data[5] = -311

            # could need more compressing
            compressed = [0] * (int(N * 1.01) + 1024)
            inputoffset = IntWrapper(0)
            outputoffset = IntWrapper(0)
            codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

            # we can repack the data: (optional)
            compressed = compressed[: outputoffset.intValue()]

            recovered = [0] * N
            recoffset = IntWrapper(0)
            codec.uncompress0(
                compressed, IntWrapper(0), len(compressed), recovered, recoffset
            )

            self.assertEqual(data, recovered)

    @staticmethod
    def maskArray(array: typing.List[int], mask: int) -> None:
        for i in range(len(array)):
            array[i] &= mask

    def __testUnsorted3(self, codec: IntegerCODEC) -> None:
        data = [0] * 128
        data[127] = -1
        compressed = [0] * 1024
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        # Compress the data
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

        # Repack the data (optional)
        compressed = compressed[: outputoffset.intValue()]

        recovered = [0] * 128
        recoffset = IntWrapper(0)

        # Uncompress the data
        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

        # Assert that the original data and the recovered data are the same
        self.assertEqual(data, recovered)

    def __testUnsorted2(self, codec: IntegerCODEC) -> None:
        data = [0] * 128
        data[5] = -1
        compressed = [0] * 1024
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        # Compress the data
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

        # Repack the data (optional)
        compressed = compressed[: outputoffset.intValue()]

        recovered = [0] * 128
        recoffset = IntWrapper(0)

        # Uncompress the data
        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

        # Assert that the original data matches the recovered data
        self.assertEqual(data, recovered)

    @staticmethod
    def __testCodec(
        c: IntegerCODEC,
        co: IntegerCODEC,
        data: typing.List[typing.List[int]],
        max_: int,
    ) -> None:
        N = len(data)
        maxlength = 0
        for k in range(N):
            if len(data[k]) > maxlength:
                maxlength = len(data[k])

        buffer = [0] * (maxlength + 1024)
        dataout = [0] * (
            4 * maxlength + 1024
        )  # 4x + 1024 to account for the possibility of some negative compression.
        inpos = IntWrapper.IntWrapper1()
        outpos = IntWrapper.IntWrapper1()

        for k in range(N):
            backupdata = data[k][:]  # Copy of data[k]

            inpos.set_(1)
            outpos.set_(0)
            if not isinstance(c, IntegratedIntegerCODEC):
                Delta.delta0(backupdata)

            c.compress0(
                backupdata, inpos, len(backupdata) - inpos.get(), dataout, outpos
            )
            thiscompsize = outpos.get() + 1

            inpos.set_(0)
            outpos.set_(1)
            buffer[0] = backupdata[0]
            co.uncompress0(dataout, inpos, thiscompsize - 1, buffer, outpos)

            if not isinstance(c, IntegratedIntegerCODEC):
                Delta.fastinverseDelta0(buffer)

            # Check assertions
            assert outpos.get() == len(data[k]), "length is not match"
            bufferCutout = buffer[: outpos.get()]
            assert bufferCutout == data[k], "failed to reconstruct original data"

    @staticmethod
    def __test1(N: int, nbr: int) -> None:
        cdg = ClusteredDataGenerator()
        print(f"[BasicTest.test] N = {N} {nbr}")
        for sparsity in range(1, 31 - nbr, 4):
            data = [None] * N
            max_ = 1 << (nbr + sparsity)
            for k in range(N):
                data[k] = cdg.generateClustered((1 << nbr), max_)

            BasicTest.__testCodec(
                IntegratedComposition(
                    IntegratedBinaryPacking(), IntegratedVariableByte()
                ),
                IntegratedComposition(
                    IntegratedBinaryPacking(), IntegratedVariableByte()
                ),
                data,
                max_,
            )
            BasicTest.__testCodec(JustCopy(), JustCopy(), data, max_)
            BasicTest.__testCodec(VariableByte(), VariableByte(), data, max_)
            BasicTest.__testCodec(
                IntegratedVariableByte(), IntegratedVariableByte(), data, max_
            )
            BasicTest.__testCodec(
                Composition(BinaryPacking(), VariableByte()),
                Composition(BinaryPacking(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(NewPFD(), VariableByte()),
                Composition(NewPFD(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(NewPFDS9(), VariableByte()),
                Composition(NewPFDS9(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(NewPFDS16(), VariableByte()),
                Composition(NewPFDS16(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(OptPFD(), VariableByte()),
                Composition(OptPFD(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(OptPFDS9(), VariableByte()),
                Composition(OptPFDS9(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(OptPFDS16(), VariableByte()),
                Composition(OptPFDS16(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
                Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(
                Composition(FastPFOR.FastPFOR1(), VariableByte()),
                Composition(FastPFOR.FastPFOR1(), VariableByte()),
                data,
                max_,
            )
            BasicTest.__testCodec(Simple9(), Simple9(), data, max_)

    @staticmethod
    def __test0(c: IntegerCODEC, co: IntegerCODEC, N: int, nbr: int) -> None:
        cdg = ClusteredDataGenerator()
        for sparsity in range(1, 31 - nbr, 4):
            data = []
            max_ = 1 << (nbr + sparsity)
            for k in range(N):
                data.append(cdg.generateClustered((1 << nbr), max_))
            BasicTest.__testCodec(c, co, data, max_)

    @staticmethod
    def __testZeroInZeroOut(c: IntegerCODEC) -> None:
        x = []  # Equivalent to int[] x = new int[0];
        y = []  # Equivalent to int[] y = new int[0];
        i0 = IntWrapper(0)  # Equivalent to IntWrapper i0 = new IntWrapper(0);
        i1 = IntWrapper(0)  # Equivalent to IntWrapper i1 = new IntWrapper(0);

        # Call the compress0 method
        c.compress0(x, i0, 0, y, i1)

        # Assert that i1.intValue() is 0
        assert (
            i1.intValue() == 0
        ), f"Expected i1.intValue() to be 0, but got {i1.intValue()}"

        out = []  # Equivalent to int[] out = new int[0];
        outpos = IntWrapper(0)  # Equivalent to IntWrapper outpos = new IntWrapper(0);

        # Call the uncompress0 method
        c.uncompress0(y, i1, 0, out, outpos)

        # Assert that outpos.intValue() is 0
        assert (
            outpos.intValue() == 0
        ), f"Expected outpos.intValue() to be 0, but got {outpos.intValue()}"

    @staticmethod
    def __testSpurious(c: IntegerCODEC) -> None:
        x = [0] * 1024
        y = []
        i0 = IntWrapper(0)
        i1 = IntWrapper(0)
        for inlength in range(32):
            c.compress0(x, i0, inlength, y, i1)
            assert i1.intValue() == 0
