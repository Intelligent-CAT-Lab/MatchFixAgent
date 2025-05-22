from __future__ import annotations
import re
import io
import typing
from typing import *
import os


class Util:

    @staticmethod
    def greatestMultiple(value: int, factor: int) -> int:
        return value - value % factor

    @staticmethod
    def _unpackw(
        sourcearray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        num: int,
        b: int,
    ) -> int:
        howmanyfit = 32 // b
        if num > howmanyfit:
            data[:num] = sourcearray[arraypos : arraypos + num]
            return num + arraypos
        mask = (1 << b) - 1
        val = sourcearray[arraypos]
        for k in range(num):
            data[k] = val & mask
            val >>= b
        return arraypos + 1

    @staticmethod
    def _packw(
        outputarray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        num: int,
        b: int,
    ) -> int:
        howmanyfit = 32 // b
        if num > howmanyfit:
            outputarray[arraypos : arraypos + num] = data[:num]
            return num + arraypos

        outputarray[arraypos] = 0
        inwordpointer = 0
        for k in range(num):
            outputarray[arraypos] |= data[k] << inwordpointer
            inwordpointer += b

        return arraypos + 1

    @staticmethod
    def _packsizew(num: int, b: int) -> int:
        howmanyfit = 32 // b
        if num <= howmanyfit:
            return 1
        return num

    @staticmethod
    def _unpack(
        sourcearray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        datapos: int,
        num: int,
        b: int,
    ) -> int:
        if b > 16:
            data[datapos : datapos + num] = sourcearray[arraypos : arraypos + num]
            return num + arraypos

        mask = (1 << b) - 1
        inwordpointer = 0
        for k in range(num):
            data[k + datapos] = (sourcearray[arraypos] >> inwordpointer) & mask
            inwordpointer += b
            increment = (inwordpointer + b - 1) >> 5
            arraypos += increment
            inwordpointer &= ~(-increment)

        return arraypos + (1 if inwordpointer > 0 else 0)

    @staticmethod
    def _pack(
        outputarray: typing.List[int],
        arraypos: int,
        data: typing.List[int],
        datapos: int,
        num: int,
        b: int,
    ) -> int:
        if num == 0:
            return arraypos
        if b > 16:
            outputarray[arraypos : arraypos + num] = data[datapos : datapos + num]
            return num + arraypos
        for k in range(Util._packsize(num, b)):
            outputarray[k + arraypos] = 0
        inwordpointer = 0
        for k in range(num):
            outputarray[arraypos] |= data[k + datapos] << inwordpointer
            inwordpointer += b
            increment = (inwordpointer + b - 1) >> 5
            arraypos += increment
            inwordpointer &= ~(-increment)
        return arraypos + (1 if inwordpointer > 0 else 0)

    @staticmethod
    def _packsize(num: int, b: int) -> int:
        if b > 16:
            return num
        howmanyfit = 32 // b
        return (num + howmanyfit - 1) // howmanyfit

    @staticmethod
    def bits(i: int) -> int:
        return 32 - (i.bit_length() if i > 0 else 0)

    @staticmethod
    def maxdiffbits(initoffset: int, i: typing.List[int], pos: int, length: int) -> int:
        mask = 0
        mask |= i[pos] - initoffset
        for k in range(pos + 1, pos + length):
            mask |= i[k] - i[k - 1]
        return Util.bits(mask)

    @staticmethod
    def _maxbits32(i: typing.List[int], pos: int) -> int:
        mask = i[pos]
        mask |= i[pos + 1]
        mask |= i[pos + 2]
        mask |= i[pos + 3]
        mask |= i[pos + 4]
        mask |= i[pos + 5]
        mask |= i[pos + 6]
        mask |= i[pos + 7]
        mask |= i[pos + 8]
        mask |= i[pos + 9]
        mask |= i[pos + 10]
        mask |= i[pos + 11]
        mask |= i[pos + 12]
        mask |= i[pos + 13]
        mask |= i[pos + 14]
        mask |= i[pos + 15]
        mask |= i[pos + 16]
        mask |= i[pos + 17]
        mask |= i[pos + 18]
        mask |= i[pos + 19]
        mask |= i[pos + 20]
        mask |= i[pos + 21]
        mask |= i[pos + 22]
        mask |= i[pos + 23]
        mask |= i[pos + 24]
        mask |= i[pos + 25]
        mask |= i[pos + 26]
        mask |= i[pos + 27]
        mask |= i[pos + 28]
        mask |= i[pos + 29]
        mask |= i[pos + 30]
        mask |= i[pos + 31]
        return Util.bits(mask)

    @staticmethod
    def maxbits(i: typing.List[int], pos: int, length: int) -> int:
        mask = 0
        for k in range(pos, pos + length):
            mask |= i[k]
        return Util.bits(mask)

    @staticmethod
    def _smallerorequalthan(x: int, y: int) -> bool:
        return (x + (-(2**31))) <= (y + (-(2**31)))
