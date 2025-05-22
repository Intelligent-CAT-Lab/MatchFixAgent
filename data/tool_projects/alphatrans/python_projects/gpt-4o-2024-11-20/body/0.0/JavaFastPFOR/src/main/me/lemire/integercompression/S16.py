from __future__ import annotations
import time
import re
import io
import typing
from typing import *
import os


class S16:

    __SHIFTED_S16_BITS: typing.List[typing.List[int]] = None
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

    @staticmethod
    def initialize_fields() -> None:
        S16.__SHIFTED_S16_BITS: typing.List[typing.List[int]] = S16.__shiftme(
            [
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
        )

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
            howmany = S16.decompressblock(out, currentPos, in_, tmpinpos, outlength)
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
        numIdx = in_[inOffset] >> S16.__S16_BITSSIZE
        num = min(S16.__S16_NUM[numIdx], n)
        bits = 0
        for j in range(num):
            out[outOffset + j] = (in_[inOffset] >> bits) & (
                0xFFFFFFFF >> (32 - S16.__S16_BITS[numIdx][j])
            )
            bits += S16.__S16_BITS[numIdx][j]
        return num

    @staticmethod
    def compressblock(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        for numIdx in range(S16.__S16_NUMSIZE):
            out[outOffset] = numIdx << S16.__S16_BITSSIZE
            num = min(S16.__S16_NUM[numIdx], n)

            j, bits = 0, 0
            while j < num and in_[inOffset + j] < S16.__SHIFTED_S16_BITS[numIdx][j]:
                out[outOffset] |= in_[inOffset + j] << bits
                bits += S16.__S16_BITS[numIdx][j]
                j += 1

            if j == num:
                return num

        return -1

    @staticmethod
    def estimatecompress(in_: typing.List[int], currentPos: int, inlength: int) -> int:
        finalin = currentPos + inlength
        counter = 0
        while currentPos < finalin:
            inoffset = S16.__fakecompressblock(in_, currentPos, inlength)
            if inoffset == -1:
                raise RuntimeError("Too big a number")
            currentPos += inoffset
            inlength -= inoffset
            counter += 1
        return counter

    @staticmethod
    def compress(
        in_: typing.List[int],
        currentPos: int,
        inlength: int,
        out: typing.List[int],
        tmpoutpos: int,
    ) -> int:
        outpos = tmpoutpos
        finalin = currentPos + inlength
        while currentPos < finalin:
            inoffset = S16.compressblock(out, outpos, in_, currentPos, inlength)
            if inoffset == -1:
                raise RuntimeError("Too big a number")
            currentPos += inoffset
            inlength -= inoffset
            outpos += 1
        return outpos - tmpoutpos

    @staticmethod
    def __shiftme(x: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
        answer = [[0] * len(row) for row in x]
        for k in range(len(x)):
            answer[k] = [1 << x[k][z] for z in range(len(x[k]))]
        return answer

    @staticmethod
    def __fakecompressblock(in_: typing.List[int], inOffset: int, n: int) -> int:
        for numIdx in range(S16.__S16_NUMSIZE):
            num = min(S16.__S16_NUM[numIdx], n)

            j = 0
            while j < num and in_[inOffset + j] < S16.__SHIFTED_S16_BITS[numIdx][j]:
                j += 1

            if j == num:
                return num

        return -1


S16.initialize_fields()
