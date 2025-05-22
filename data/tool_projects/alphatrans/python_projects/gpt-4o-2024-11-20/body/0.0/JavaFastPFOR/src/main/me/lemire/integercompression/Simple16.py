from __future__ import annotations
import time
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *


class Simple16(IntegerCODEC, SkippableIntegerCODEC):

    __S16_BITS: typing.List[typing.List[int]] = [
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
        [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [4, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 4, 4, 4, 4, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 4, 4],
        [4, 4, 5, 5, 5, 5],
        [6, 6, 6, 5, 5],
        [5, 5, 6, 6, 6],
        [7, 7, 7, 7],
        [10, 9, 9],
        [14, 14],
        [28],
    ]
    __S16_NUM: typing.List[int] = [28, 21, 21, 21, 14, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]
    __S16_BITSSIZE: int = 28
    __S16_NUMSIZE: int = 16

    __SHIFTED_S16_BITS: typing.List[typing.List[int]] = (
        None  # LLM could not translate this field
    )

    def toString(self) -> str:
        return self.__class__.__name__

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return
        outlength = in_[inpos.get()]
        inpos.increment()
        self.headlessUncompress(in_, inpos, inlength, out, outpos, outlength)

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
        out[outpos.get()] = inlength
        outpos.increment()
        self.headlessCompress(in_, inpos, inlength, out, outpos)

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        i_inpos = inpos.get()
        i_outpos = outpos.get()
        while num > 0:
            howmany = self.decompressblock(out, i_outpos, in_, i_inpos, num)
            num -= howmany
            i_outpos += howmany
            i_inpos += 1
        inpos.set_(i_inpos)
        outpos.set_(i_outpos)

    @staticmethod
    def uncompress(
        in_: typing.List[int],
        tmpinpos: int,
        inlength: int,
        out: typing.List[int],
        currentPos: int,
        outlength: int,
    ) -> None:
        finalpos = tmpinpos + inlength
        while tmpinpos < finalpos:
            howmany = Simple16.decompressblock(
                out, currentPos, in_, tmpinpos, outlength
            )
            outlength -= howmany
            currentPos += howmany
            tmpinpos += 1

    @staticmethod
    def decompressblock(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        numIdx = in_[inOffset] >> Simple16.__S16_BITSSIZE
        num = min(Simple16.__S16_NUM[numIdx], n)
        bits = 0
        for j in range(num):
            out[outOffset + j] = (in_[inOffset] >> bits) & (
                0xFFFFFFFF >> (32 - Simple16.__S16_BITS[numIdx][j])
            )
            bits += Simple16.__S16_BITS[numIdx][j]
        return num

    @staticmethod
    def compressblock(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        for numIdx in range(Simple16.__S16_NUMSIZE):
            out[outOffset] = numIdx << Simple16.__S16_BITSSIZE
            num = min(Simple16.__S16_NUM[numIdx], n)

            j, bits = 0, 0
            while (
                j < num and in_[inOffset + j] < Simple16.__SHIFTED_S16_BITS[numIdx][j]
            ):
                out[outOffset] |= in_[inOffset + j] << bits
                bits += Simple16.__S16_BITS[numIdx][j]
                j += 1

            if j == num:
                return num

        return -1

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        i_inpos = inpos.get()
        i_outpos = outpos.get()
        finalin = i_inpos + inlength
        while i_inpos < finalin:
            inoffset = self.compressblock(out, i_outpos, in_, i_inpos, inlength)
            if inoffset == -1:
                raise RuntimeError("Too big a number")
            i_outpos += 1
            i_inpos += inoffset
            inlength -= inoffset
        inpos.set_(i_inpos)
        outpos.set_(i_outpos)

    @staticmethod
    def __shiftme(x: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        answer = [[0] * len(row) for row in x]
        for k in range(len(x)):
            answer[k] = [1 << x[k][z] for z in range(len(x[k]))]
        return answer
