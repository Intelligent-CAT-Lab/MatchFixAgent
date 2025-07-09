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
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.IntegratedLongCODEC import *
from src.main.me.lemire.longcompression.LongAs2IntsCodec import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.LongJustCopy import *
from src.test.me.lemire.longcompression.LongTestUtils import *
from src.main.me.lemire.longcompression.LongVariableByte import *
from src.main.me.lemire.longcompression.differential.LongDelta import *


class LongBasicTest(unittest.TestCase):

    codecs: typing.List[LongCODEC] = [
        LongJustCopy(),
        LongVariableByte(),
        LongAs2IntsCodec.LongAs2IntsCodec1(),
    ]

    def testfastPfor128Test_test0_decomposed(self) -> None:
        for codec in self.codecs:
            N = FastPFOR128.BLOCK_SIZE
            data = [0] * N
            data[126] = -1
            comp = LongTestUtils._compress1(codec, data[:N])
            answer = LongTestUtils._uncompress0(codec, comp, N)
            for k in range(N):
                if answer[k] != data[k]:
                    raise RuntimeError(f"bug {k} {answer[k]} != {data[k]}")

    def testfastPforTest_test0_decomposed(self) -> None:
        for codec in self.codecs:
            N = FastPFOR.BLOCK_SIZE
            data = [0] * N
            data[126] = -1
            comp = LongTestUtils._compress1(codec, data[:N])
            answer = LongTestUtils._uncompress0(codec, comp, N)
            for k in range(N):
                if answer[k] != data[k]:
                    raise RuntimeError(f"bug {k} {answer[k]} != {data[k]}")

    def testvaryingLengthTest2_test0_decomposed(self) -> None:
        N = 128
        data = [0] * N
        data[127] = -1

        for codec in self.codecs:
            print(f"[BasicTest.varyingLengthTest2] codec = {codec}")
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

            try:
                # CODEC GroupSimple9 is limited to "small" integers.
                if codec.__class__.__name__ == "GroupSimple9":
                    continue
            except Exception as e:
                print(e)

            for L in range(1, 129):
                comp = LongTestUtils._compress1(codec, data[:L])
                answer = LongTestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")

            L = 128
            while L <= N:
                comp = LongTestUtils._compress1(codec, data[:L])
                answer = LongTestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testvaryingLengthTest_test0_decomposed(self) -> None:
        N = 4096
        data = [k for k in range(N)]
        for codec in self.codecs:
            print(f"[BasicTest.varyingLengthTest] codec = {codec}")
            for L in range(1, 129):  # Loop for L from 1 to 128 (inclusive)
                comp = LongTestUtils._compress1(codec, data[:L])
                answer = LongTestUtils._uncompress0(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
            L = 128
            while L <= N:  # Loop for L doubling from 128 to N
                comp = LongTestUtils._compress1(codec, data[:L])
                answer = LongTestUtils._uncompress0(codec, comp, L)
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
                codec.uncompress1(b, b_offset, length, c, c_offset)

                if a != c:
                    print(f"Problem with {codec}")

                self.assertEqual(a, c)

    def testUnsorted(self, codec: LongCODEC) -> None:
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
            codec.uncompress1(
                compressed, IntWrapper(0), len(compressed), recovered, recoffset
            )
            self.assertEqual(data, recovered)

    def __testUnsorted3(self, codec: LongCODEC) -> None:
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
        codec.uncompress1(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

        # Assert that the original data matches the recovered data
        self.assertEqual(data, recovered)

    def __testUnsorted2(self, codec: LongCODEC) -> None:
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
        codec.uncompress1(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

        # Assert that the original data matches the recovered data
        self.assertEqual(data, recovered)

    @staticmethod
    def __testCodec(
        c: LongCODEC, co: LongCODEC, data: typing.List[typing.List[int]], max_: int
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
            if not isinstance(c, IntegratedLongCODEC):
                LongDelta.delta0(backupdata)

            c.compress0(
                backupdata, inpos, len(backupdata) - inpos.get(), dataout, outpos
            )
            thiscompsize = outpos.get() + 1

            inpos.set_(0)
            outpos.set_(1)
            buffer[0] = backupdata[0]
            co.uncompress1(dataout, inpos, thiscompsize - 1, buffer, outpos)

            if not isinstance(c, IntegratedLongCODEC):
                LongDelta.fastinverseDelta0(buffer)

            # Check assertions
            assert outpos.get() == len(data[k]), "length is not match"
            bufferCutout = buffer[: outpos.get()]
            assert bufferCutout == data[k], "failed to reconstruct original data"

    @staticmethod
    def __testZeroInZeroOut(c: LongCODEC) -> None:
        x = []  # Equivalent to new long[0] in Java
        y = []  # Equivalent to new long[0] in Java
        i0 = IntWrapper(0)
        i1 = IntWrapper(0)

        # Call the compress0 method
        c.compress0(x, i0, 0, y, i1)

        # Assert that i1.intValue() is 0
        assert (
            i1.intValue() == 0
        ), f"Expected i1.intValue() to be 0, but got {i1.intValue()}"

        out = []  # Equivalent to new long[0] in Java
        outpos = IntWrapper(0)

        # Call the uncompress1 method
        c.uncompress1(y, i1, 0, out, outpos)

        # Assert that outpos.intValue() is 0
        assert (
            outpos.intValue() == 0
        ), f"Expected outpos.intValue() to be 0, but got {outpos.intValue()}"

    @staticmethod
    def __testSpurious(c: LongCODEC) -> None:
        x = [0] * 1024  # Equivalent to `long[] x = new long[1024];`
        y = []  # Equivalent to `long[] y = new long[0];`
        i0 = IntWrapper(0)  # Equivalent to `IntWrapper i0 = new IntWrapper(0);`
        i1 = IntWrapper(0)  # Equivalent to `IntWrapper i1 = new IntWrapper(0);`
        for inlength in range(
            32
        ):  # Equivalent to `for (int inlength = 0; inlength < 32; ++inlength)`
            c.compress0(x, i0, inlength, y, i1)  # Call the `compress0` method
            assert i1.intValue() == 0  # Equivalent to `assertEquals(0, i1.intValue());`
