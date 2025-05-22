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
from src.main.me.lemire.integercompression.Util import *


class GroupSimple9(IntegerCODEC, SkippableIntegerCODEC):

    __codeNum: typing.List[int] = [28, 14, 9, 7, 5, 4, 3, 2, 1]
    __bitLength: typing.List[int] = [1, 2, 3, 4, 5, 7, 9, 14, 28]
    __M: typing.List[typing.List[int]] = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49, 50, 51, 52, 53],
        [54, 55, 56, 57, 58, 59, 60, 61, 62],
        [63, 64, 65, 66, 67, 68, 69, 70, 71],
        [72, 73, 74, 75, 76, 77, 78, 79, 80],
    ]

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        currentPos = outpos.get()
        tmpinpos = inpos.get()
        finalout = currentPos + num

        while currentPos < finalout - 2 * 28:
            val = in_[tmpinpos]
            tmpinpos += 1
            valn = in_[tmpinpos]
            tmpinpos += 1
            header = val >> 24

            decode_method = getattr(self, f"_GroupSimple9__decode{header}", None)
            if decode_method is None:
                raise RuntimeError(f"Wrong code: {header}")
            decode_method(val, valn, out, currentPos)

            currentPos += {
                0: 56,
                1: 42,
                2: 37,
                3: 35,
                4: 33,
                5: 32,
                6: 31,
                7: 30,
                8: 29,
                9: 42,
                10: 28,
                11: 23,
                12: 21,
                13: 19,
                14: 18,
                15: 17,
                16: 16,
                17: 15,
                18: 37,
                19: 23,
                20: 18,
                21: 16,
                22: 14,
                23: 13,
                24: 12,
                25: 11,
                26: 10,
                27: 35,
                28: 21,
                29: 16,
                30: 14,
                31: 12,
                32: 11,
                33: 10,
                34: 9,
                35: 8,
                36: 33,
                37: 19,
                38: 14,
                39: 12,
                40: 10,
                41: 9,
                42: 8,
                43: 7,
                44: 6,
                45: 32,
                46: 18,
                47: 13,
                48: 11,
                49: 9,
                50: 8,
                51: 7,
                52: 6,
                53: 5,
                54: 31,
                55: 17,
                56: 12,
                57: 10,
                58: 8,
                59: 7,
                60: 6,
                61: 5,
                62: 4,
                63: 30,
                64: 16,
                65: 11,
                66: 9,
                67: 7,
                68: 6,
                69: 5,
                70: 4,
                71: 3,
                72: 29,
                73: 15,
                74: 10,
                75: 8,
                76: 6,
                77: 5,
                78: 4,
                79: 3,
                80: 2,
            }.get(header, 0)

        while currentPos < finalout:
            val = in_[tmpinpos]
            tmpinpos += 1
            header = val >> 28

            if header == 0:
                howmany = min(finalout - currentPos, 28)
                for k in range(howmany):
                    out[currentPos] = (val << (k + 4)) >> 31
                    currentPos += 1
            elif header == 1:
                howmany = min(finalout - currentPos, 14)
                for k in range(howmany):
                    out[currentPos] = (val << (2 * k + 4)) >> 30
                    currentPos += 1
            elif header == 2:
                howmany = min(finalout - currentPos, 9)
                for k in range(howmany):
                    out[currentPos] = (val << (3 * k + 5)) >> 29
                    currentPos += 1
            elif header == 3:
                howmany = min(finalout - currentPos, 7)
                for k in range(howmany):
                    out[currentPos] = (val << (4 * k + 4)) >> 28
                    currentPos += 1
            elif header == 4:
                howmany = min(finalout - currentPos, 5)
                for k in range(howmany):
                    out[currentPos] = (val << (5 * k + 7)) >> 27
                    currentPos += 1
            elif header == 5:
                howmany = min(finalout - currentPos, 4)
                for k in range(howmany):
                    out[currentPos] = (val << (7 * k + 4)) >> 25
                    currentPos += 1
            elif header == 6:
                howmany = min(finalout - currentPos, 3)
                for k in range(howmany):
                    out[currentPos] = (val << (9 * k + 5)) >> 23
                    currentPos += 1
            elif header == 7:
                howmany = min(finalout - currentPos, 2)
                for k in range(howmany):
                    out[currentPos] = (val << (14 * k + 4)) >> 18
                    currentPos += 1
            elif header == 8:
                out[currentPos] = (val << 4) >> 4
                currentPos += 1
            else:
                raise RuntimeError("shouldn't happen")

        outpos.set_(finalout)
        inpos.set_(tmpinpos)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        tmpoutpos = outpos.get()
        currentPos = inpos.get()
        finalin = currentPos + inlength

        while currentPos < finalin - 28 * 2:
            nextCurrentPos = currentPos
            for selector1 in range(9):
                compressedNum = self.__codeNum[selector1]
                b = self.__bitLength[selector1]
                max_ = 1 << b
                for i in range(compressedNum):
                    if Util._smallerorequalthan(max_, in_[nextCurrentPos + i]):
                        break
                else:
                    nextCurrentPos += compressedNum
                    break

            for selector2 in range(9):
                compressedNum = self.__codeNum[selector2]
                b = self.__bitLength[selector2]
                max_ = 1 << b
                for i in range(compressedNum):
                    if Util._smallerorequalthan(max_, in_[nextCurrentPos + i]):
                        break
                else:
                    nextCurrentPos += compressedNum
                    break

            code = self.__M[selector1][selector2]
            out[tmpoutpos] = 0
            out[tmpoutpos + 1] = 0

            encode_method = getattr(self, f"_GroupSimple9__encode{code}", None)
            if encode_method is not None:
                encode_method(in_, currentPos, code, out, tmpoutpos)
            else:
                raise RuntimeError("unsupported code")

            tmpoutpos += 2
            currentPos = nextCurrentPos

        while currentPos < finalin:
            for selector in range(8):
                res = 0
                compressedNum = self.__codeNum[selector]
                if finalin <= currentPos + compressedNum - 1:
                    compressedNum = finalin - currentPos
                b = self.__bitLength[selector]
                max_ = 1 << b
                for i in range(compressedNum):
                    if Util._smallerorequalthan(max_, in_[currentPos + i]):
                        break
                    res = (res << b) + in_[currentPos + i]
                else:
                    if compressedNum != self.__codeNum[selector]:
                        res <<= (self.__codeNum[selector] - compressedNum) * b
                    res |= selector << 28
                    out[tmpoutpos] = res
                    tmpoutpos += 1
                    currentPos += compressedNum
                    break
            else:
                selector = 8
                out[tmpoutpos] = in_[currentPos] | (selector << 28)
                tmpoutpos += 1
                currentPos += 1

        inpos.set_(currentPos)
        outpos.set_(tmpoutpos)

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

    def __decode0(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode1(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode2(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31  # 头部1bit
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode3(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31  # 头部3bit
        currentPos += 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27
        currentPos += 1

    def __decode5(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25
        currentPos += 1

    def __decode6(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23
        currentPos += 1

    def __decode7(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18
        currentPos += 1

    def __decode8(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 28, bitwidth : 1
        out[currentPos] = (val << 8) >> 31
        currentPos += 1
        out[currentPos] = (val << 9) >> 31
        currentPos += 1
        out[currentPos] = (val << 10) >> 31
        currentPos += 1
        out[currentPos] = (val << 11) >> 31
        currentPos += 1
        out[currentPos] = (val << 12) >> 31
        currentPos += 1
        out[currentPos] = (val << 13) >> 31
        currentPos += 1
        out[currentPos] = (val << 14) >> 31
        currentPos += 1
        out[currentPos] = (val << 15) >> 31
        currentPos += 1
        out[currentPos] = (val << 16) >> 31
        currentPos += 1
        out[currentPos] = (val << 17) >> 31
        currentPos += 1
        out[currentPos] = (val << 18) >> 31
        currentPos += 1
        out[currentPos] = (val << 19) >> 31
        currentPos += 1
        out[currentPos] = (val << 20) >> 31
        currentPos += 1
        out[currentPos] = (val << 21) >> 31
        currentPos += 1
        out[currentPos] = (val << 22) >> 31
        currentPos += 1
        out[currentPos] = (val << 23) >> 31
        currentPos += 1
        out[currentPos] = (val << 24) >> 31
        currentPos += 1
        out[currentPos] = (val << 25) >> 31
        currentPos += 1
        out[currentPos] = (val << 26) >> 31
        currentPos += 1
        out[currentPos] = (val << 27) >> 31
        currentPos += 1
        out[currentPos] = (val << 28) >> 31
        currentPos += 1
        out[currentPos] = (val << 29) >> 31
        currentPos += 1
        out[currentPos] = (val << 30) >> 31
        currentPos += 1
        out[currentPos] = (val << 31) >> 31
        currentPos += 1
        out[currentPos] = valn >> 31
        currentPos += 1
        out[currentPos] = (valn << 1) >> 31
        currentPos += 1
        out[currentPos] = (valn << 2) >> 31
        currentPos += 1
        out[currentPos] = (valn << 3) >> 31
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode9(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode10(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode11(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 1) >> 30
        currentPos += 1
        out[currentPos] = (valn << 3) >> 30
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode12(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30  # 10
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode13(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30  # 10
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 3) >> 30
        currentPos += 1
        out[currentPos] = (valn << 5) >> 30
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27
        currentPos += 1

    def __decode14(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25
        currentPos += 1

    def __decode15(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30  # 10
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 1) >> 30
        currentPos += 1
        out[currentPos] = (valn << 3) >> 30
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23
        currentPos += 1

    def __decode16(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18
        currentPos += 1

    def __decode17(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 14, bitwidth : 2
        out[currentPos] = (val << 8) >> 30
        currentPos += 1
        out[currentPos] = (val << 10) >> 30
        currentPos += 1
        out[currentPos] = (val << 12) >> 30
        currentPos += 1
        out[currentPos] = (val << 14) >> 30
        currentPos += 1
        out[currentPos] = (val << 16) >> 30
        currentPos += 1
        out[currentPos] = (val << 18) >> 30
        currentPos += 1
        out[currentPos] = (val << 20) >> 30
        currentPos += 1
        out[currentPos] = (val << 22) >> 30
        currentPos += 1
        out[currentPos] = (val << 24) >> 30
        currentPos += 1
        out[currentPos] = (val << 26) >> 30
        currentPos += 1
        out[currentPos] = (val << 28) >> 30
        currentPos += 1
        out[currentPos] = (val << 30) >> 30
        currentPos += 1
        out[currentPos] = (valn << 0) >> 30
        currentPos += 1
        out[currentPos] = (valn << 2) >> 30
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode18(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode19(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode20(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 2) >> 29
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode21(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode22(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 4) >> 29
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27
        currentPos += 1

    def __decode23(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25

    def __decode24(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 2) >> 29
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23

    def __decode25(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode26(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 9, bitwidth : 3
        out[currentPos] = (val << 8) >> 29
        currentPos += 1
        out[currentPos] = (val << 11) >> 29
        currentPos += 1
        out[currentPos] = (val << 14) >> 29
        currentPos += 1
        out[currentPos] = (val << 17) >> 29
        currentPos += 1
        out[currentPos] = (val << 20) >> 29
        currentPos += 1
        out[currentPos] = (val << 23) >> 29
        currentPos += 1
        out[currentPos] = (val << 26) >> 29
        currentPos += 1
        out[currentPos] = (val << 29) >> 29
        currentPos += 1
        out[currentPos] = (valn << 1) >> 29
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode27(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 0) >> 28
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode28(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 0) >> 28
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode29(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 1) >> 28
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) & 0xF
        currentPos += 1
        out[currentPos] = (val << 12) & 0xF
        currentPos += 1
        out[currentPos] = (val << 16) & 0xF
        currentPos += 1
        out[currentPos] = (val << 20) & 0xF
        currentPos += 1
        out[currentPos] = (val << 24) & 0xF
        currentPos += 1
        out[currentPos] = (val << 28) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 0) & 0xF
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 8) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 12) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 16) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 20) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 24) & 0xF
        currentPos += 1
        out[currentPos] = (valn << 28) & 0xF
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 3) >> 28
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27
        currentPos += 1

    def __decode32(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 0) >> 28
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25

    def __decode33(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 1) >> 28
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23
        currentPos += 1

    def __decode34(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 0) >> 28
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode35(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 7, bitwidth : 4
        out[currentPos] = (val << 8) >> 28
        currentPos += 1
        out[currentPos] = (val << 12) >> 28
        currentPos += 1
        out[currentPos] = (val << 16) >> 28
        currentPos += 1
        out[currentPos] = (val << 20) >> 28
        currentPos += 1
        out[currentPos] = (val << 24) >> 28
        currentPos += 1
        out[currentPos] = (val << 28) >> 28
        currentPos += 1
        out[currentPos] = (valn << 0) >> 28
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode36(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 28)
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode37(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 28)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode38(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 27)
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode39(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 28)
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode40(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 13) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 18) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 23) & 0x1F
        currentPos += 1
        out[currentPos] = ((val << 28) & 0x1F) | ((valn >> 25) & 0x1F)
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) & 0x1F
        currentPos += 1
        out[currentPos] = (valn << 12) & 0x1F
        currentPos += 1
        out[currentPos] = (valn << 17) & 0x1F
        currentPos += 1
        out[currentPos] = (valn << 22) & 0x1F
        currentPos += 1
        out[currentPos] = (valn << 27) & 0x1F

    def __decode41(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 13) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 18) & 0x1F
        currentPos += 1
        out[currentPos] = (val << 23) & 0x1F
        currentPos += 1
        out[currentPos] = ((val << 28) & 0x1F) | ((valn >> 28) & 0x1F)
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 11) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 18) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 25) & 0x7F

    def __decode42(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 27)
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23

    def __decode43(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 28)
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode44(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = (val << 8) >> 27
        currentPos += 1
        out[currentPos] = (val << 13) >> 27
        currentPos += 1
        out[currentPos] = (val << 18) >> 27
        currentPos += 1
        out[currentPos] = (val << 23) >> 27
        currentPos += 1
        out[currentPos] = ((val << 28) >> 27) | (valn >> 28)
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 28)
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode46(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 28)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode47(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 27)
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode48(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 28)
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28

    def __decode49(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 25)
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27

    def __decode50(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) & 0x7F
        currentPos += 1
        out[currentPos] = (val << 15) & 0x7F
        currentPos += 1
        out[currentPos] = (val << 22) & 0x7F
        currentPos += 1
        out[currentPos] = ((val << 29) & 0x7F) | (valn >> 28)
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 11) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 18) & 0x7F
        currentPos += 1
        out[currentPos] = (valn << 25) & 0x7F

    def __decode51(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) & 0x7F000000 >> 25
        currentPos += 1
        out[currentPos] = (val << 15) & 0x7F000000 >> 25
        currentPos += 1
        out[currentPos] = (val << 22) & 0x7F000000 >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) & 0x7F000000 >> 25) | (valn >> 27)
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) & 0xFF800000 >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) & 0xFF800000 >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) & 0xFF800000 >> 23

    def __decode52(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 28)
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode53(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 4, bitwidth : 7
        out[currentPos] = (val << 8) >> 25
        currentPos += 1
        out[currentPos] = (val << 15) >> 25
        currentPos += 1
        out[currentPos] = (val << 22) >> 25
        currentPos += 1
        out[currentPos] = ((val << 29) >> 25) | (valn >> 28)
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode54(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31  # 10
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31  # 20
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode55(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode56(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 27)
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode57(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode58(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 25)
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27

    def __decode59(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) & 0x1FF
        currentPos += 1
        out[currentPos] = (val << 17) & 0x1FF
        currentPos += 1
        out[currentPos] = ((val << 26) & 0x1FF) | ((valn >> 27) & 0x1FF)
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) & 0x1FF
        currentPos += 1
        out[currentPos] = (valn << 14) & 0x1FF
        currentPos += 1
        out[currentPos] = (valn << 23) & 0x1FF

    def __decode61(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode62(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 3, bitwidth : 9
        out[currentPos] = (val << 8) >> 23
        currentPos += 1
        out[currentPos] = (val << 17) >> 23
        currentPos += 1
        out[currentPos] = ((val << 26) >> 23) | (valn >> 28)
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode63(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 28)
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31  # 10
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31  # 20
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode64(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 28)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode65(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 27)
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode66(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 28)
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode67(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 25)
        currentPos += 1
        # number : 5, bitwidth : 5
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27

    def __decode68(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 28)
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25

    def __decode69(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 27)
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) & 0x3FFF
        currentPos += 1
        out[currentPos] = ((val << 22) & 0x3FFF) | (valn >> 28)
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) & 0x3FFF
        currentPos += 1
        out[currentPos] = (valn << 18) & 0x3FFF
        currentPos += 1

    def __decode71(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 2, bitwidth : 14
        out[currentPos] = (val << 8) >> 18
        currentPos += 1
        out[currentPos] = ((val << 22) >> 18) | (valn >> 28)
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __decode72(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = ((val << 8) >> 4) | (valn >> 28)
        currentPos += 1
        # number : 28, bitwidth : 1
        out[currentPos] = (valn << 4) >> 31
        currentPos += 1
        out[currentPos] = (valn << 5) >> 31
        currentPos += 1
        out[currentPos] = (valn << 6) >> 31
        currentPos += 1
        out[currentPos] = (valn << 7) >> 31
        currentPos += 1
        out[currentPos] = (valn << 8) >> 31
        currentPos += 1
        out[currentPos] = (valn << 9) >> 31
        currentPos += 1
        out[currentPos] = (valn << 10) >> 31
        currentPos += 1
        out[currentPos] = (valn << 11) >> 31
        currentPos += 1
        out[currentPos] = (valn << 12) >> 31
        currentPos += 1
        out[currentPos] = (valn << 13) >> 31  # 10
        currentPos += 1
        out[currentPos] = (valn << 14) >> 31
        currentPos += 1
        out[currentPos] = (valn << 15) >> 31
        currentPos += 1
        out[currentPos] = (valn << 16) >> 31
        currentPos += 1
        out[currentPos] = (valn << 17) >> 31
        currentPos += 1
        out[currentPos] = (valn << 18) >> 31
        currentPos += 1
        out[currentPos] = (valn << 19) >> 31
        currentPos += 1
        out[currentPos] = (valn << 20) >> 31
        currentPos += 1
        out[currentPos] = (valn << 21) >> 31
        currentPos += 1
        out[currentPos] = (valn << 22) >> 31
        currentPos += 1
        out[currentPos] = (valn << 23) >> 31  # 20
        currentPos += 1
        out[currentPos] = (valn << 24) >> 31
        currentPos += 1
        out[currentPos] = (valn << 25) >> 31
        currentPos += 1
        out[currentPos] = (valn << 26) >> 31
        currentPos += 1
        out[currentPos] = (valn << 27) >> 31
        currentPos += 1
        out[currentPos] = (valn << 28) >> 31
        currentPos += 1
        out[currentPos] = (valn << 29) >> 31
        currentPos += 1
        out[currentPos] = (valn << 30) >> 31
        currentPos += 1
        out[currentPos] = (valn << 31) >> 31
        currentPos += 1

    def __decode73(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 28)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 4) >> 30
        currentPos += 1
        out[currentPos] = (valn << 6) >> 30
        currentPos += 1
        out[currentPos] = (valn << 8) >> 30
        currentPos += 1
        out[currentPos] = (valn << 10) >> 30
        currentPos += 1
        out[currentPos] = (valn << 12) >> 30
        currentPos += 1
        out[currentPos] = (valn << 14) >> 30
        currentPos += 1
        out[currentPos] = (valn << 16) >> 30
        currentPos += 1
        out[currentPos] = (valn << 18) >> 30
        currentPos += 1
        out[currentPos] = (valn << 20) >> 30
        currentPos += 1
        out[currentPos] = (valn << 22) >> 30
        currentPos += 1
        out[currentPos] = (valn << 24) >> 30
        currentPos += 1
        out[currentPos] = (valn << 26) >> 30
        currentPos += 1
        out[currentPos] = (valn << 28) >> 30
        currentPos += 1
        out[currentPos] = (valn << 30) >> 30
        currentPos += 1

    def __decode74(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 27)
        currentPos += 1
        # number : 9, bitwidth : 3
        out[currentPos] = (valn << 5) >> 29
        currentPos += 1
        out[currentPos] = (valn << 8) >> 29
        currentPos += 1
        out[currentPos] = (valn << 11) >> 29
        currentPos += 1
        out[currentPos] = (valn << 14) >> 29
        currentPos += 1
        out[currentPos] = (valn << 17) >> 29
        currentPos += 1
        out[currentPos] = (valn << 20) >> 29
        currentPos += 1
        out[currentPos] = (valn << 23) >> 29
        currentPos += 1
        out[currentPos] = (valn << 26) >> 29
        currentPos += 1
        out[currentPos] = (valn << 29) >> 29
        currentPos += 1

    def __decode75(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 28)
        currentPos += 1
        # number : 7, bitwidth : 4
        out[currentPos] = (valn << 4) >> 28
        currentPos += 1
        out[currentPos] = (valn << 8) >> 28
        currentPos += 1
        out[currentPos] = (valn << 12) >> 28
        currentPos += 1
        out[currentPos] = (valn << 16) >> 28
        currentPos += 1
        out[currentPos] = (valn << 20) >> 28
        currentPos += 1
        out[currentPos] = (valn << 24) >> 28
        currentPos += 1
        out[currentPos] = (valn << 28) >> 28
        currentPos += 1

    def __decode76(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 5, bitwidth : 5
        out[currentPos] = ((val << 8) >> 4) | (valn >> 25)
        currentPos += 1
        # number : 14, bitwidth : 2
        out[currentPos] = (valn << 7) >> 27
        currentPos += 1
        out[currentPos] = (valn << 12) >> 27
        currentPos += 1
        out[currentPos] = (valn << 17) >> 27
        currentPos += 1
        out[currentPos] = (valn << 22) >> 27
        currentPos += 1
        out[currentPos] = (valn << 27) >> 27
        currentPos += 1

    def __decode77(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 28)
        currentPos += 1
        # number : 4, bitwidth : 7
        out[currentPos] = (valn << 4) >> 25
        currentPos += 1
        out[currentPos] = (valn << 11) >> 25
        currentPos += 1
        out[currentPos] = (valn << 18) >> 25
        currentPos += 1
        out[currentPos] = (valn << 25) >> 25

    def __decode78(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 27)
        currentPos += 1
        # number : 3, bitwidth : 9
        out[currentPos] = (valn << 5) >> 23
        currentPos += 1
        out[currentPos] = (valn << 14) >> 23
        currentPos += 1
        out[currentPos] = (valn << 23) >> 23

    def __decode79(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 28)
        currentPos += 1
        # number : 2, bitwidth : 14
        out[currentPos] = (valn << 4) >> 18
        currentPos += 1
        out[currentPos] = (valn << 18) >> 18

    def __decode80(
        self, val: int, valn: int, out: typing.List[int], currentPos: int
    ) -> None:
        # number : 1, bitwidth : 28
        out[currentPos] = (val << 8) >> 4 | (valn >> 28)
        currentPos += 1
        # number : 1, bitwidth : 28
        out[currentPos] = (valn << 4) >> 4

    def __encode80(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(
            1
        ):  # The loop runs only once, so range(1) is equivalent to `for (int i = 0; i < 1; i++)`
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode79(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode78(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode77(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode76(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode75(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode74(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode73(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode72(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 24) + (in_[inf] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf] << 28) >> 28)
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 1 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode71(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(1):  # Equivalent to `for (int i = 0; i < 1; i++)` in Java
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode70(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode69(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode68(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode67(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode66(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode65(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode64(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode63(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        out[outf + 0] = (out[outf + 0] << 14) + in_[inf]
        out[outf + 0] = (out[outf + 0] << 10) + (in_[inf + 1] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 1] << 28) >> 28)
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 2 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode62(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode61(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode60(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode59(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode58(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode57(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode56(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode55(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode54(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(2):
            out[outf + 0] = (out[outf + 0] << 9) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 6) + (in_[inf + 2] >> 3)
        out[outf + 1] = (out[outf + 1] << 3) + ((in_[inf + 2] << 29) >> 29)
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 3 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode53(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode52(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode51(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode50(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode49(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode48(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode47(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode46(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode45(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(3):
            out[outf + 0] = (out[outf + 0] << 7) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 3) + (in_[inf + 3] >> 4)
        out[outf + 1] = (out[outf + 1] << 4) + ((in_[inf + 3] << 28) >> 28)
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 4 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode44(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode43(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode42(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode41(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode40(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode39(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode38(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode37(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode36(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(4):
            out[outf + 0] = (out[outf + 0] << 5) + in_[inf + i]
        out[outf + 0] = (out[outf + 0] << 4) + (in_[inf + 4] >> 1)
        out[outf + 1] = (out[outf + 1] << 1) + ((in_[inf + 4] << 31) >> 31)
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 5 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode35(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode34(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode33(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode32(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode31(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode30(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode29(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode28(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode27(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(6):
            out[outf + 0] = (out[outf + 0] << 4) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 6 + i]
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 7 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode26(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode25(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode24(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode23(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode22(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode21(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 9 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode20(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 9 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode19(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 9 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode18(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(8):
            out[outf + 0] = (out[outf + 0] << 3) + in_[inf + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 8 + i]
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 9 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode17(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode16(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode15(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode14(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode13(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode12(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode11(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode10(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]

        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]

        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode9(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(12):
            out[outf + 0] = (out[outf + 0] << 2) + in_[inf + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 12 + i]
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 14 + i]

        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode8(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(1):
            out[outf + 1] = (out[outf + 1] << 28) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode7(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(2):
            out[outf + 1] = (out[outf + 1] << 14) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode6(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(3):
            out[outf + 1] = (out[outf + 1] << 9) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode5(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 7) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode4(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(5):
            out[outf + 1] = (out[outf + 1] << 5) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode3(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(7):
            out[outf + 1] = (out[outf + 1] << 4) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode2(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(9):
            out[outf + 1] = (out[outf + 1] << 3) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode1(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(14):
            out[outf + 1] = (out[outf + 1] << 2) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]

    def __encode0(
        self,
        in_: typing.List[int],
        inf: int,
        code: int,
        out: typing.List[int],
        outf: int,
    ) -> None:
        for i in range(24):
            out[outf + 0] = (out[outf + 0] << 1) + in_[inf + i]
        for i in range(4):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 24 + i]
        for i in range(28):
            out[outf + 1] = (out[outf + 1] << 1) + in_[inf + 28 + i]
        out[outf + 0] = (code << 24) | out[outf + 0]
