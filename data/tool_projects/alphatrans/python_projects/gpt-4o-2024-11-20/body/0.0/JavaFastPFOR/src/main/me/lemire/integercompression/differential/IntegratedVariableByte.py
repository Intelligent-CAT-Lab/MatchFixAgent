from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class IntegratedVariableByte(
    IntegratedByteIntegerCODEC, IntegratedIntegerCODEC, SkippableIntegratedIntegerCODEC
):

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
        initvalue: IntWrapper,
    ) -> None:
        s = 0
        val = 0

        p = inpos.get()
        initoffset = initvalue.get()
        tmpoutpos = outpos.get()
        finaloutpos = num + tmpoutpos

        v = 0
        shift = 0

        while tmpoutpos < finaloutpos:
            val = in_[p]
            c = (val >> s) & 0xFF  # Extract the byte at position `s`
            s += 8
            p += s >> 5  # Move to the next integer if `s` exceeds 31 bits
            s = s & 31  # Keep `s` within the range [0, 31]
            v += (
                c & 127
            ) << shift  # Add the 7 least significant bits of `c` shifted by `shift`

            if (c & 128) == 128:  # Check if the most significant bit of `c` is set
                out[tmpoutpos] = initoffset + v
                initoffset = out[tmpoutpos]
                tmpoutpos += 1
                v = 0
                shift = 0
            else:
                shift += 7

        initvalue.set_(out[tmpoutpos - 1])
        outpos.set_(tmpoutpos)

        inpos.set_(p + (1 if s != 0 else 0))

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        initvalue: IntWrapper,
    ) -> None:
        if inlength == 0:
            return

        initoffset = initvalue.get()
        initvalue.set_(in_[inpos.get() + inlength - 1])

        buf = bytearray(inlength * 8)
        position = 0  # Tracks the current position in the buffer

        for k in range(inpos.get(), inpos.get() + inlength):
            val = (in_[k] - initoffset) & 0xFFFFFFFF  # Simulate unsigned 32-bit integer
            initoffset = in_[k]

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
            out[outpos.get()] = int.from_bytes(
                buf[i : i + 4], byteorder="little", signed=False
            )
            outpos.add(1)

        inpos.add(inlength)

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
        initoffset = 0
        finalp = inpos.get() + inlength
        tmpoutpos = outpos.get()

        while p < finalp:
            v = in_[p] & 0x7F
            if in_[p] < 0:
                p += 1
                out[tmpoutpos] = initoffset + v
                initoffset = out[tmpoutpos]
                tmpoutpos += 1
                continue

            v = ((in_[p + 1] & 0x7F) << 7) | v
            if in_[p + 1] < 0:
                p += 2
                out[tmpoutpos] = initoffset + v
                initoffset = out[tmpoutpos]
                tmpoutpos += 1
                continue

            v = ((in_[p + 2] & 0x7F) << 14) | v
            if in_[p + 2] < 0:
                p += 3
                out[tmpoutpos] = initoffset + v
                initoffset = out[tmpoutpos]
                tmpoutpos += 1
                continue

            v = ((in_[p + 3] & 0x7F) << 21) | v
            if in_[p + 3] < 0:
                p += 4
                out[tmpoutpos] = initoffset + v
                initoffset = out[tmpoutpos]
                tmpoutpos += 1
                continue

            v = ((in_[p + 4] & 0x7F) << 28) | v
            p += 5
            out[tmpoutpos] = initoffset + v
            initoffset = out[tmpoutpos]
            tmpoutpos += 1

        outpos.set_(tmpoutpos)
        inpos.add(p)

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
        initoffset = 0

        v = 0
        shift = 0
        while p < finalp:
            val = in_[p]
            c = (val >> s) & 0xFF  # Extract the byte at position `s`
            s += 8
            p += s >> 5
            s = s & 31
            v += (c & 127) << shift
            if (c & 128) == 128:  # Check if the most significant bit is set
                out[tmpoutpos] = v + initoffset
                initoffset = out[tmpoutpos]
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
        initoffset = 0
        outpostmp = outpos.get()
        for k in range(inpos.get(), inpos.get() + inlength):
            val = (
                in_[k] - initoffset
            ) & 0xFFFFFFFF  # To be consistent with unsigned integers in C/C++
            initoffset = in_[k]
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

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return
        initoffset = 0
        buf = bytearray(inlength * 8)
        position = 0  # To simulate ByteBuffer's position

        for k in range(inpos.get(), inpos.get() + inlength):
            val = (in_[k] - initoffset) & 0xFFFFFFFF  # Simulate unsigned int behavior
            initoffset = in_[k]

            if val < (1 << 7):
                buf[position] = (val | (1 << 7)) & 0xFF
                position += 1
            elif val < (1 << 14):
                buf[position] = self.__extract7bits(0, val) & 0xFF
                position += 1
                buf[position] = (self.__extract7bitsmaskless(1, val) | (1 << 7)) & 0xFF
                position += 1
            elif val < (1 << 21):
                buf[position] = self.__extract7bits(0, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(1, val) & 0xFF
                position += 1
                buf[position] = (self.__extract7bitsmaskless(2, val) | (1 << 7)) & 0xFF
                position += 1
            elif val < (1 << 28):
                buf[position] = self.__extract7bits(0, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(1, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(2, val) & 0xFF
                position += 1
                buf[position] = (self.__extract7bitsmaskless(3, val) | (1 << 7)) & 0xFF
                position += 1
            else:
                buf[position] = self.__extract7bits(0, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(1, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(2, val) & 0xFF
                position += 1
                buf[position] = self.__extract7bits(3, val) & 0xFF
                position += 1
                buf[position] = (self.__extract7bitsmaskless(4, val) | (1 << 7)) & 0xFF
                position += 1

        # Align to 4 bytes
        while position % 4 != 0:
            buf[position] = 0
            position += 1

        length = position
        int_buf = [
            int.from_bytes(buf[i : i + 4], byteorder="little")
            for i in range(0, length, 4)
        ]
        out[outpos.get() : outpos.get() + len(int_buf)] = int_buf
        outpos.add(len(int_buf))
        inpos.add(inlength)

    return bytearray(sizeInBytes)

    @staticmethod
    def __extract7bitsmaskless(i: int, val: int) -> int:
        return (val >> (7 * i)) & 0xFF

    @staticmethod
    def __extract7bits(i: int, val: int) -> int:
        return (val >> (7 * i)) & ((1 << 7) - 1)
