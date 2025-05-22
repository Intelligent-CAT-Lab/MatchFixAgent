from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.ByteLongCODEC import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class LongVariableByte(ByteLongCODEC, LongCODEC, SkippableLongCODEC):

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:

        pass  # LLM could not translate this method

    def toString(self) -> str:
        return self.__class__.__name__

    def compress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return
        outpostmp = outpos.get()
        for k in range(inpos.get(), inpos.get() + inlength):
            val = in_[k]
            if 0 <= val < (1 << 7):
                out[outpostmp] = (val | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 14):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(1, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 21):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(2, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 28):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(3, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 35):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(4, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 42):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(4, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(5, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 49):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(4, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(5, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(6, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 56):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(4, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(5, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(6, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(7, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif 0 <= val < (1 << 63):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(4, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(5, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(6, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(7, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(8, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            else:
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(3, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(4, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(5, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(6, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(7, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(8, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(9, val) | (1 << 7)) & 0xFF
                outpostmp += 1
        outpos.set_(outpostmp)
        inpos.add(inlength)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return

        # Worst case: we write 10 bytes per long, hence 2 longs for a long, hence 16 bytes per long
        buf = memoryview(bytearray(inlength * 16))
        position = 0  # To track the current position in the buffer

        for k in range(inpos.get(), inpos.get() + inlength):
            val = in_[k]
            if 0 <= val < (1 << 7):
                buf[position] = (val | (1 << 7)) & 0xFF
                position += 1
            elif 0 <= val < (1 << 14):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = (
                    self.__extract7bitsmaskless(1, val) | (1 << 7)
                ) & 0xFF
                position += 2
            elif 0 <= val < (1 << 21):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = (
                    self.__extract7bitsmaskless(2, val) | (1 << 7)
                ) & 0xFF
                position += 3
            elif 0 <= val < (1 << 28):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = (
                    self.__extract7bitsmaskless(3, val) | (1 << 7)
                ) & 0xFF
                position += 4
            elif 0 <= val < (1 << 35):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = (
                    self.__extract7bitsmaskless(4, val) | (1 << 7)
                ) & 0xFF
                position += 5
            elif 0 <= val < (1 << 42):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = self.__extract7bits(4, val)
                buf[position + 5] = (
                    self.__extract7bitsmaskless(5, val) | (1 << 7)
                ) & 0xFF
                position += 6
            elif 0 <= val < (1 << 49):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = self.__extract7bits(4, val)
                buf[position + 5] = self.__extract7bits(5, val)
                buf[position + 6] = (
                    self.__extract7bitsmaskless(6, val) | (1 << 7)
                ) & 0xFF
                position += 7
            elif 0 <= val < (1 << 56):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = self.__extract7bits(4, val)
                buf[position + 5] = self.__extract7bits(5, val)
                buf[position + 6] = self.__extract7bits(6, val)
                buf[position + 7] = (
                    self.__extract7bitsmaskless(7, val) | (1 << 7)
                ) & 0xFF
                position += 8
            elif 0 <= val < (1 << 63):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = self.__extract7bits(4, val)
                buf[position + 5] = self.__extract7bits(5, val)
                buf[position + 6] = self.__extract7bits(6, val)
                buf[position + 7] = self.__extract7bits(7, val)
                buf[position + 8] = (
                    self.__extract7bitsmaskless(8, val) | (1 << 7)
                ) & 0xFF
                position += 9
            else:
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = self.__extract7bits(4, val)
                buf[position + 5] = self.__extract7bits(5, val)
                buf[position + 6] = self.__extract7bits(6, val)
                buf[position + 7] = self.__extract7bits(7, val)
                buf[position + 8] = self.__extract7bits(8, val)
                buf[position + 9] = (
                    self.__extract7bitsmaskless(9, val) | (1 << 7)
                ) & 0xFF
                position += 10

        # Pad the buffer to align to 8 bytes
        while position % 8 != 0:
            buf[position] = 0
            position += 1

        length = position
        longs = length // 8
        for i in range(longs):
            out[outpos.get() + i] = int.from_bytes(
                buf[i * 8 : (i + 1) * 8], byteorder="little"
            )

        outpos.add(longs)
        inpos.add(inlength)

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        self.headlessCompress(in_, inpos, inlength, out, outpos)

    return memoryview(bytearray(sizeInBytes))

    @staticmethod
    def __extract7bitsmaskless(i: int, val: int) -> int:
        return (val >> (7 * i)) & 0xFF

    @staticmethod
    def __extract7bits(i: int, val: int) -> int:
        return (val >> (7 * i)) & ((1 << 7) - 1)
