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
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.VariableByte import *


class SkippableBasicTest(unittest.TestCase):

    codecs: typing.List[SkippableIntegerCODEC] = [
        JustCopy(),
        VariableByte(),
        SkippableComposition(BinaryPacking(), VariableByte()),
        SkippableComposition(NewPFD(), VariableByte()),
        SkippableComposition(NewPFDS9(), VariableByte()),
        SkippableComposition(NewPFDS16(), VariableByte()),
        SkippableComposition(OptPFD(), VariableByte()),
        SkippableComposition(OptPFDS9(), VariableByte()),
        SkippableComposition(OptPFDS16(), VariableByte()),
        SkippableComposition(FastPFOR128.FastPFOR1281(), VariableByte()),
        SkippableComposition(FastPFOR.FastPFOR1(), VariableByte()),
        Simple9(),
        Simple16(),
    ]

    def testvaryingLengthTest2_test0_decomposed(self) -> None:
        N = 128
        data = [0] * N
        data[127] = -1
        for codec in self.codecs:
            print(f"[SkippableBasicTest.varyingLengthTest2] codec = {codec}")

            try:
                # CODEC Simple9 is limited to "small" integers.
                if codec.__class__.__name__ == "Simple9":
                    continue
            except Exception as e:
                print(e)

            try:
                # CODEC Simple16 is limited to "small" integers.
                if codec.__class__.__name__ == "Simple16":
                    continue
            except Exception as e:
                print(e)

            for L in range(1, 129):
                comp = TestUtils._compressHeadless(codec, data[:L])
                answer = TestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(
                            f"bug at k = {k} {answer[k]} {data[k]} for {codec}"
                        )

            L = 128
            while L <= N:
                comp = TestUtils._compressHeadless(codec, data[:L])
                answer = TestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testvaryingLengthTest_test0_decomposed(self) -> None:
        N = 4096
        data = [k for k in range(N)]
        for codec in self.codecs:
            print(f"[SkippableBasicTest.varyingLengthTest] codec = {codec}")
            for L in range(1, 129):
                comp = TestUtils._compressHeadless(codec, data[:L])
                answer = TestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(f"bug {codec} {k} {answer[k]} {data[k]}")
            L = 128
            while L <= N:
                comp = TestUtils._compressHeadless(codec, data[:L])
                answer = TestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testconsistentTest_test0_decomposed(self) -> None:
        N = 4096
        data = [k % 128 for k in range(N)]
        rev = [0] * N

        for codec in self.codecs:
            print(f"[SkippableBasicTest.consistentTest] codec = {codec}")
            out_buf = [0] * (N + 1024)

            for n in range(N + 1):
                in_pos = IntWrapper.IntWrapper1()
                out_pos = IntWrapper.IntWrapper1()
                codec.headlessCompress(data, in_pos, n, out_buf, out_pos)

                in_poso = IntWrapper.IntWrapper1()
                out_poso = IntWrapper.IntWrapper1()
                codec.headlessUncompress(
                    out_buf, in_poso, out_pos.get(), rev, out_poso, n
                )

                if out_poso.get() != n:
                    raise RuntimeError(f"bug {n}")
                if in_poso.get() != out_pos.get():
                    raise RuntimeError(f"bug {n} {in_poso.get()} {out_pos.get()}")
                for j in range(n):
                    if data[j] != rev[j]:
                        raise RuntimeError("bug")
