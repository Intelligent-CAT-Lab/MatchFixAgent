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
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *


class ByteBasicTest(unittest.TestCase):

    codecs: typing.List[ByteIntegerCODEC] = [
        VariableByte(),
        IntegratedVariableByte(),
    ]

    def testvaryingLengthTest2_test0_decomposed(self) -> None:
        N = 128
        data = [0] * N
        data[127] = -1
        for codec in self.codecs:
            try:
                # CODEC Simple9 is limited to "small" integers.
                if codec.__class__.__name__ == "Simple9":
                    continue
            except Exception as e:
                print(e)

            for L in range(1, 129):  # Loop from 1 to 128 (inclusive)
                comp = TestUtils._compress0(codec, data[:L])
                answer = TestUtils._uncompress1(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(f"bug at k = {k} {answer[k]} {data[k]}")

            L = 128
            while L <= N:
                comp = TestUtils._compress0(codec, data[:L])
                answer = TestUtils._uncompress1(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testvaryingLengthTest_test0_decomposed(self) -> None:
        N = 4096
        data = [k for k in range(N)]
        for codec in self.codecs:
            for L in range(1, 129):  # Loop from 1 to 128 (inclusive)
                comp = TestUtils._compress0(codec, data[:L])
                answer = TestUtils._uncompress1(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError(f"bug {codec} {k} {answer[k]} {data[k]}")
            L = 128
            while L <= N:
                comp = TestUtils._compress0(codec, data[:L])
                answer = TestUtils._uncompress1(codec, comp, L)
                for k in range(L):
                    if answer[k] != data[k]:
                        raise RuntimeError("bug")
                L *= 2

    def testsaulTest_test0_decomposed(self) -> None:
        for codec in self.codecs:
            for x in range(50 * 4):
                a = [2, 3, 4, 5]
                b = bytearray(90 * 4)  # Using bytearray to represent byte[] in Python
                c = [0] * len(a)

                a_offset = IntWrapper(0)
                b_offset = IntWrapper(x)
                codec.compress1(a, a_offset, len(a), b, b_offset)
                length = b_offset.get() - x

                b_offset.set_(x)
                c_offset = IntWrapper(0)
                codec.uncompress1(b, b_offset, length, c, c_offset)

                if (
                    a != c
                ):  # Arrays.equals(a, c) in Java is equivalent to `a != c` in Python
                    print(f"Problem with {codec}")

                self.assertEqual(
                    a, c
                )  # assertArrayEquals(a, c) in Java is equivalent to self.assertEqual(a, c) in Python
