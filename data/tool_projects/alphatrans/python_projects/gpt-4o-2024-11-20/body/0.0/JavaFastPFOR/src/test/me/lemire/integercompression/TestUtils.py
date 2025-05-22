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
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class TestUtils(unittest.TestCase):

    def testPackingw_test0_decomposed(self) -> None:
        outputarray = [0] * 32
        for b in range(1, 32):
            data = [0] * 32
            newdata = [0] * 32
            mask = (1 << b) - 1
            for j in range(len(data)):
                data[j] = mask - (j % mask)
            for n in range(33):  # range(0, 33) in Python
                outputarray = [0] * 32
                howmany = Util._packw(outputarray, 0, data, n, b)
                if howmany != Util._packsizew(n, b):
                    raise RuntimeError(f"bug {n} {b}")
                Util._unpackw(outputarray[:howmany], 0, newdata, n, b)
                for i in range(n):
                    if newdata[i] != data[i]:
                        print(data[:n])
                        print(newdata[:n])
                        raise RuntimeError(f"bug {b} {n}")

    def testPacking_test0_decomposed(self) -> None:
        outputarray = [0] * 32
        for b in range(1, 32):
            data = [0] * 32
            newdata = [0] * 32
            mask = (1 << b) - 1
            for j in range(len(data)):
                data[j] = mask - (j % mask)
            for n in range(33):  # range(0, 33) in Python
                outputarray = [0] * 32
                howmany = Util._pack(outputarray, 0, data, 0, n, b)
                if howmany != Util._packsize(n, b):
                    raise RuntimeError(f"bug {n} {b}")
                Util._unpack(outputarray[:howmany], 0, newdata, 0, n, b)
                for i in range(n):
                    if newdata[i] != data[i]:
                        print(data[:n])
                        print(newdata[:n])
                        raise RuntimeError(f"bug {b} {n}")

    @staticmethod
    def _uncompressHeadless(
        codec: SkippableIntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        out_buf = [0] * (len_ + 1024)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.headlessUncompress(data, in_pos, len(data), out_buf, out_pos, len_)
        if out_pos.get() < len_:
            raise RuntimeError("Insufficient output.")
        return out_buf[: out_pos.get()]

    @staticmethod
    def _compressHeadless(
        codec: SkippableIntegerCODEC, data: typing.List[int]
    ) -> typing.List[int]:
        out_buf = [0] * (len(data) * 4)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.headlessCompress(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _uncompress1(
        codec: ByteIntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        out_buf = [0] * (len_ + 1024)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.uncompress1(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _compress0(codec: ByteIntegerCODEC, data: typing.List[int]) -> typing.List[int]:
        out_buf = [0] * (len(data) * 4 * 4)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.compress1(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _uncompress0(
        codec: IntegerCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        out_buf = [0] * (len_ + 1024)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.uncompress0(data, in_pos, len_, out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def compress1(codec: IntegerCODEC, data: typing.List[int]) -> typing.List[int]:
        out_buf = [0] * (len(data) * 4)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.compress0(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def assertSymmetry(codec: IntegerCODEC, orig: typing.List[int]) -> None:
        # There are some cases where the compressed array is bigger than the original array.
        # So the output array for compression must be larger.
        #
        # Example:
        #  - VariableByte compresses an array like [-1].
        #  - Composition compresses a short array.
        EXTEND = 1

        # Create a compressed array with extra space
        compressed = [0] * (len(orig) + EXTEND)
        c_inpos = IntWrapper(0)
        c_outpos = IntWrapper(0)

        # Compress the original array
        codec.compress0(orig, c_inpos, len(orig), compressed, c_outpos)

        # Assert that the compressed size does not exceed the original size + EXTEND
        assert c_outpos.get() <= len(orig) + EXTEND

        # Create an array for uncompressed data
        uncompressed = [0] * len(orig)
        u_inpos = IntWrapper(0)
        u_outpos = IntWrapper(0)

        # Uncompress the compressed array
        codec.uncompress0(compressed, u_inpos, c_outpos.get(), uncompressed, u_outpos)

        # Compare the uncompressed array with the original array
        target = uncompressed[: u_outpos.get()]
        assert orig == target, f"Expected {orig}, but got {target}"

    @staticmethod
    def _dumpIntArrayAsHex(data: typing.List[int], label: str) -> None:
        print(label, end="")
        for i in range(len(data)):
            if i % 8 == 0:
                print()
            print(f" {data[i]:08X}", end="")
        print()

    @staticmethod
    def _dumpIntArray(data: typing.List[int], label: str) -> None:
        print(label, end="")
        for i in range(len(data)):
            if i % 6 == 0:
                print()
            print(f"{data[i]:11d}", end="")
        print()
