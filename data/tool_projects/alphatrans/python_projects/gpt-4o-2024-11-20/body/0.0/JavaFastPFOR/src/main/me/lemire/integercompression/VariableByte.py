from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *


class VariableByte(ByteIntegerCODEC, IntegerCODEC, SkippableIntegerCODEC):

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        s = 0
        val = 0
        p = inpos.get()
        tmpoutpos = outpos.get()
        finaloutpos = num + tmpoutpos

        v = 0
        shift = 0

        while tmpoutpos < finaloutpos:
            val = in_[p]
            c = val >> s
            # Shift to next byte
            s += 8
            # Shift to next integer if s == 32
            p += s >> 5
            # Cycle from 31 to 0
            s = s & 31
            v += (c & 127) << shift
            if (c & 128) == 128:
                out[tmpoutpos] = v
                tmpoutpos += 1
                v = 0
                shift = 0
            else:
                shift += 7

        outpos.set_(tmpoutpos)
        inpos.set_(p + (1 if s != 0 else 0))

    def toString(self) -> str:
        return self.__class__.__name__

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        p = inpos.get()
        finalp = inpos.get() + inlength
        tmpoutpos = outpos.get()

        while p < finalp:
            v = in_[p] & 0x7F
            if in_[p] < 0:
                p += 1
                out[tmpoutpos] = v
                tmpoutpos += 1
                continue

            v = ((in_[p + 1] & 0x7F) << 7) | v
            if in_[p + 1] < 0:
                p += 2
                out[tmpoutpos] = v
                tmpoutpos += 1
                continue

            v = ((in_[p + 2] & 0x7F) << 14) | v
            if in_[p + 2] < 0:
                p += 3
                out[tmpoutpos] = v
                tmpoutpos += 1
                continue

            v = ((in_[p + 3] & 0x7F) << 21) | v
            if in_[p + 3] < 0:
                p += 4
                out[tmpoutpos] = v
                tmpoutpos += 1
                continue

            v = ((in_[p + 4] & 0x7F) << 28) | v
            p += 5
            out[tmpoutpos] = v
            tmpoutpos += 1

        outpos.set_(tmpoutpos)
        inpos.add(p - inpos.get())

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        s = 0
        val = 0
        p = inpos.get()
        finalp = inpos.get() + inlength
        tmpoutpos = outpos.get()
        v = 0
        shift = 0

        while p < finalp:
            val = in_[p]
            c = (val >> s) & 0xFF  # Extract the byte at position `s`
            # Shift to next byte
            s += 8
            # Shift to next integer if s == 32
            p += s >> 5
            # Cycle from 31 to 0
            s = s & 31
            v += (c & 127) << shift
            if (c & 128) == 128:
                out[tmpoutpos] = v
                tmpoutpos += 1
                v = 0
                shift = 0
            else:
                shift += 7

        outpos.set_(tmpoutpos)
        inpos.add(inlength)

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
            val = (
                in_[k] & 0xFFFFFFFF
            )  # To be consistent with unsigned integers in C/C++
            if val < (1 << 7):
                out[outpostmp] = (val | (1 << 7)) & 0xFF
                outpostmp += 1
            elif val < (1 << 14):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(1, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif val < (1 << 21):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(2, val) | (1 << 7)) & 0xFF
                outpostmp += 1
            elif val < (1 << 28):
                out[outpostmp] = self.__extract7bits(0, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(1, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = self.__extract7bits(2, val) & 0xFF
                outpostmp += 1
                out[outpostmp] = (self.__extract7bitsmaskless(3, val) | (1 << 7)) & 0xFF
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
                out[outpostmp] = (self.__extract7bitsmaskless(4, val) | (1 << 7)) & 0xFF
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

        # Create a buffer with enough space
        buf = bytearray(inlength * 8)
        position = 0  # Tracks the current position in the buffer

        for k in range(inpos.get(), inpos.get() + inlength):
            val = in_[k] & 0xFFFFFFFF  # Ensure unsigned 32-bit integer

            if val < (1 << 7):
                buf[position] = (val | (1 << 7)) & 0xFF
                position += 1
            elif val < (1 << 14):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = (
                    self.__extract7bitsmaskless(1, val) | (1 << 7)
                ) & 0xFF
                position += 2
            elif val < (1 << 21):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = (
                    self.__extract7bitsmaskless(2, val) | (1 << 7)
                ) & 0xFF
                position += 3
            elif val < (1 << 28):
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = (
                    self.__extract7bitsmaskless(3, val) | (1 << 7)
                ) & 0xFF
                position += 4
            else:
                buf[position] = self.__extract7bits(0, val)
                buf[position + 1] = self.__extract7bits(1, val)
                buf[position + 2] = self.__extract7bits(2, val)
                buf[position + 3] = self.__extract7bits(3, val)
                buf[position + 4] = (
                    self.__extract7bitsmaskless(4, val) | (1 << 7)
                ) & 0xFF
                position += 5

        # Pad the buffer to align to 4 bytes
        while position % 4 != 0:
            buf[position] = 0
            position += 1

        # Convert the buffer to integers and store in the output array
        length = position
        for i in range(0, length, 4):
            out[outpos.get()] = int.from_bytes(buf[i : i + 4], byteorder="little")
            outpos.add(1)

        # Update the input position
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
