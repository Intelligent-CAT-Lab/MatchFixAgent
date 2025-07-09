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
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.LongJustCopy import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class SkippableLongBasicTest(unittest.TestCase):

    codecs: typing.List[SkippableLongCODEC] = [
        LongJustCopy(),
        LongVariableByte(),
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
                comp = LongTestUtils._compressHeadless(codec, data[:L])
                answer = LongTestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(
                            f"L={L}: bug at k = {k} {answer[k]} {data[k]} for {codec}"
                        )

            L = 128
            while L <= N:
                comp = LongTestUtils._compressHeadless(codec, data[:L])
                answer = LongTestUtils._uncompressHeadless(codec, comp, L)
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
                comp = LongTestUtils._compressHeadless(codec, data[:L])
                answer = LongTestUtils._uncompressHeadless(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(f"bug {codec} {k} {answer[k]} {data[k]}")
            L = 128
            while L <= N:
                comp = LongTestUtils._compressHeadless(codec, data[:L])
                answer = LongTestUtils._uncompressHeadless(codec, comp, L)
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
            outBuf = [0] * (N + 1024)

            for n in range(N + 1):
                inPos = IntWrapper.IntWrapper1()
                outPos = IntWrapper.IntWrapper1()
                codec.headlessCompress(data, inPos, n, outBuf, outPos)

                inPoso = IntWrapper.IntWrapper1()
                outPoso = IntWrapper.IntWrapper1()
                codec.headlessUncompress(outBuf, inPoso, outPos.get(), rev, outPoso, n)

                if outPoso.get() != n:
                    raise RuntimeError(f"bug {n}")
                if inPoso.get() != outPos.get():
                    raise RuntimeError(f"bug {n} {inPoso.get()} {outPos.get()}")
                for j in range(n):
                    if data[j] != rev[j]:
                        raise RuntimeError("bug")
