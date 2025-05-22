from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.IntCompressor import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedIntCompressor import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class IntCompressorTest(unittest.TestCase):

    ic: typing.List[IntCompressor] = [
        IntCompressor(0, VariableByte()),
        IntCompressor(0, SkippableComposition(BinaryPacking(), VariableByte())),
    ]
    iic: typing.List[IntegratedIntCompressor] = [
        IntegratedIntCompressor(0, IntegratedVariableByte()),
        IntegratedIntCompressor(
            0,
            SkippableIntegratedComposition(
                IntegratedBinaryPacking(), IntegratedVariableByte()
            ),
        ),
    ]

    def testbasicIntegratedTest_test0_decomposed(self) -> None:
        for N in [10**i for i in range(0, 5)]:  # N = 1, 10, 100, 1000, 10000
            orig = [3 * k + 5 for k in range(N)]
            for i in self.iic:
                comp = i.compress(orig)
                back = i.uncompress(comp)
                self.assertEqual(back, orig)

    def testsuperSimpleExample_test3_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)
        recov = iic.uncompress(compressed)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {len(compressed) * 4 // 1024}KB"
        )
        if recov != data:
            raise RuntimeError("bug")

    def testsuperSimpleExample_test2_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)
        recov = iic.uncompress(compressed)

    def testsuperSimpleExample_test1_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)

    def testsuperSimpleExample_test0_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)

    def testbasicTest_test0_decomposed(self) -> None:
        for N in [10**i for i in range(5)]:  # N = 1, 10, 100, 1000, 10000
            orig = [3 * k + 5 for k in range(N)]
            for i in self.ic:
                comp = i.compress(orig)
                back = i.uncompress(comp)
                self.assertListEqual(back, orig)
