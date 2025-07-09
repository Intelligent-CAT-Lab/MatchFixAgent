from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.ByteLongCODEC import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class LongTestUtils:

    @staticmethod
    def longToBinaryWithLeading(l: int) -> str:
        return f"{l:064b}"

    @staticmethod
    def _uncompressHeadless(
        codec: SkippableLongCODEC, data: typing.List[int], len_: int
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
        codec: SkippableLongCODEC, data: typing.List[int]
    ) -> typing.List[int]:
        out_buf = [0] * (len(data) * 4)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.headlessCompress(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _uncompress1(
        codec: ByteLongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        out_buf = [0] * (len_ + 1024)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.uncompress1(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _compress0(codec: ByteLongCODEC, data: typing.List[int]) -> typing.List[int]:
        out_buf = [0] * (len(data) * 4 * 4)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.compress1(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _uncompress0(
        codec: LongCODEC, data: typing.List[int], len_: int
    ) -> typing.List[int]:
        out_buf = [0] * (len_ + 1024)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.uncompress1(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def _compress1(codec: LongCODEC, data: typing.List[int]) -> typing.List[int]:
        out_buf = [0] * (len(data) * 8)
        in_pos = IntWrapper.IntWrapper1()
        out_pos = IntWrapper.IntWrapper1()
        codec.compress0(data, in_pos, len(data), out_buf, out_pos)
        return out_buf[: out_pos.get()]

    @staticmethod
    def assertSymmetry(codec: LongCODEC, orig: typing.List[int]) -> None:
        # There are some cases where the compressed array is larger than the original array.
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

        # Assert that the compressed size does not exceed the allowed size
        assert c_outpos.get() <= len(orig) + EXTEND

        # Uncompress the array
        uncompressed = [0] * len(orig)
        u_inpos = IntWrapper(0)
        u_outpos = IntWrapper(0)
        codec.uncompress1(compressed, u_inpos, c_outpos.get(), uncompressed, u_outpos)

        # Compare the uncompressed array with the original array
        target = uncompressed[: u_outpos.get()]
        assert orig == target

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
            print(f" {data[i]:11d}", end="")
        print()
