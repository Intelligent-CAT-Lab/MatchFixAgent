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


class Simple9(IntegerCODEC, SkippableIntegerCODEC):

    __codeNum: typing.List[int] = [28, 14, 9, 7, 5, 4, 3, 2, 1]
    __bitLength: typing.List[int] = [1, 2, 3, 4, 5, 7, 9, 14, 28]

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
        outlength: int,
    ) -> None:

        pass  # LLM could not translate this method

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

        # Outer loop for processing chunks of 28 integers
        while currentPos < finalin - 28:
            for selector in range(8):
                res = 0
                compressedNum = self.__codeNum[selector]
                b = self.__bitLength[selector]
                max_ = 1 << b
                i = 0

                # Check if the current block can be compressed with the current selector
                for i in range(compressedNum):
                    if max_ <= in_[currentPos + i]:
                        break
                    res = (res << b) + in_[currentPos + i]
                else:
                    # If the loop completes without breaking, the block is compressible
                    res |= selector << 28
                    out[tmpoutpos] = res
                    tmpoutpos += 1
                    currentPos += compressedNum
                    break
            else:
                # If no selector works, use selector 8
                selector = 8
                if in_[currentPos] >= 1 << self.__bitLength[selector]:
                    raise RuntimeError("Too big a number")
                out[tmpoutpos] = in_[currentPos] | (selector << 28)
                tmpoutpos += 1
                currentPos += 1

        # Outer loop for processing the remaining integers
        while currentPos < finalin:
            for selector in range(8):
                res = 0
                compressedNum = self.__codeNum[selector]
                if finalin <= currentPos + compressedNum - 1:
                    compressedNum = finalin - currentPos
                b = self.__bitLength[selector]
                max_ = 1 << b
                i = 0

                # Check if the current block can be compressed with the current selector
                for i in range(compressedNum):
                    if max_ <= in_[currentPos + i]:
                        break
                    res = (res << b) + in_[currentPos + i]
                else:
                    # If the loop completes without breaking, the block is compressible
                    if compressedNum != self.__codeNum[selector]:
                        res <<= (self.__codeNum[selector] - compressedNum) * b
                    res |= selector << 28
                    out[tmpoutpos] = res
                    tmpoutpos += 1
                    currentPos += compressedNum
                    break
            else:
                # If no selector works, use selector 8
                selector = 8
                if in_[currentPos] >= 1 << self.__bitLength[selector]:
                    raise RuntimeError("Too big a number")
                out[tmpoutpos] = in_[currentPos] | (selector << 28)
                tmpoutpos += 1
                currentPos += 1

        # Update the positions
        inpos.set_(currentPos)
        outpos.set_(tmpoutpos)
