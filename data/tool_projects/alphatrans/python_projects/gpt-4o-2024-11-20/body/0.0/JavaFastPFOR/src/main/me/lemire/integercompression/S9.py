from __future__ import annotations
import time
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.Util import *


class S9:

    __codeNum: typing.List[int] = [28, 14, 9, 7, 5, 4, 3, 2, 1]
    __bitLength: typing.List[int] = [1, 2, 3, 4, 5, 7, 9, 14, 28]

    @staticmethod
    def uncompress(
        in_: typing.List[int],
        tmpinpos: int,
        inlength: int,
        out: typing.List[int],
        currentPos: int,
        outlength: int,
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def compress(
        in_: typing.List[int],
        currentPos: int,
        inlength: int,
        out: typing.List[int],
        tmpoutpos: int,
    ) -> int:
        origtmpoutpos = tmpoutpos
        finalpos = currentPos + inlength
        while currentPos < finalpos:
            for selector in range(8):
                res = 0
                compressedNum = S9.__codeNum[selector]
                if finalpos <= currentPos + compressedNum - 1:
                    compressedNum = finalpos - currentPos
                b = S9.__bitLength[selector]
                max_ = 1 << b
                i = 0
                for i in range(compressedNum):
                    if Util._smallerorequalthan(max_, in_[currentPos + i]):
                        break
                else:  # This else corresponds to the for-loop, executes if no break occurs
                    for i in range(compressedNum):
                        res = (res << b) + in_[currentPos + i]
                    if compressedNum != S9.__codeNum[selector]:
                        res <<= (S9.__codeNum[selector] - compressedNum) * b
                    res |= selector << 28
                    out[tmpoutpos] = res
                    tmpoutpos += 1
                    currentPos += compressedNum
                    break
            else:  # This else corresponds to the for-loop, executes if no break occurs
                selector = 8
                if in_[currentPos] >= 1 << S9.__bitLength[selector]:
                    raise RuntimeError("Too big a number")
                out[tmpoutpos] = in_[currentPos] | (selector << 28)
                tmpoutpos += 1
                currentPos += 1
        return tmpoutpos - origtmpoutpos

    @staticmethod
    def estimatecompress(in_: typing.List[int], currentPos: int, inlength: int) -> int:
        tmpoutpos = 0
        finalpos = currentPos + inlength
        while currentPos < finalpos:
            for selector in range(8):
                compressedNum = S9.__codeNum[selector]
                if finalpos <= currentPos + compressedNum - 1:
                    compressedNum = finalpos - currentPos
                b = S9.__bitLength[selector]
                max_ = 1 << b
                i = 0
                for i in range(compressedNum):
                    if Util._smallerorequalthan(max_, in_[currentPos + i]):
                        break
                else:  # This else corresponds to the for loop (executed if no break occurs)
                    currentPos += compressedNum
                    tmpoutpos += 1
                    break  # Continue the outer while loop
            else:  # This else corresponds to the for loop (executed if no break occurs in the for loop)
                selector = 8
                if in_[currentPos] >= 1 << S9.__bitLength[selector]:
                    raise RuntimeError("Too big a number")
                tmpoutpos += 1
                currentPos += 1
        return tmpoutpos
