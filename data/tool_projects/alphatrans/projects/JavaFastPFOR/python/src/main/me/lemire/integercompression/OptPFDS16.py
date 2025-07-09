from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.S16 import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class OptPFDS16(IntegerCODEC, SkippableIntegerCODEC):

    BLOCK_SIZE: int = 128
    __invbits: typing.List[int] = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        14,
        14,
        15,
        15,
        15,
        15,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
        16,
    ]
    __bits: typing.List[int] = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        16,
        20,
        32,
    ]
    exceptbuffer: typing.List[int] = [0] * (2 * BLOCK_SIZE)

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
        inlength = (inlength // self.BLOCK_SIZE) * self.BLOCK_SIZE
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
        mynvalue: int,
    ) -> None:
        if inlength == 0:
            return
        mynvalue = Util.greatestMultiple(mynvalue, self.BLOCK_SIZE)
        self.__decodePage(in_, inpos, out, outpos, mynvalue)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.BLOCK_SIZE)
        if inlength == 0:
            return

        self.__encodePage(in_, inpos, inlength, out, outpos)

    def __init__(self) -> None:
        pass

    def __decodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        out: typing.List[int],
        outpos: IntWrapper,
        thissize: int,
    ) -> None:
        tmpoutpos = outpos.get()
        tmpinpos = inpos.get()

        for run in range(thissize // self.BLOCK_SIZE):
            b = in_[tmpinpos] & 0xFF
            cexcept = (in_[tmpinpos] >> 8) & 0xFF
            exceptsize = in_[tmpinpos] >> 16
            tmpinpos += 1

            S16.uncompress(in_, tmpinpos, exceptsize, self.exceptbuffer, 0, 2 * cexcept)
            tmpinpos += exceptsize

            for k in range(0, self.BLOCK_SIZE, 32):
                BitPacking.fastunpack(in_, tmpinpos, out, tmpoutpos + k, self.__bits[b])
                tmpinpos += self.__bits[b]

            for k in range(cexcept):
                out[tmpoutpos + self.exceptbuffer[k + cexcept]] |= (
                    self.exceptbuffer[k] << self.__bits[b]
                )

            tmpoutpos += self.BLOCK_SIZE

        outpos.set_(tmpoutpos)
        inpos.set_(tmpinpos)

    def __encodePage(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        thissize: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        tmpoutpos = outpos.get()
        tmpinpos = inpos.get()
        bestb = IntWrapper.IntWrapper1()
        bestexcept = IntWrapper.IntWrapper1()

        finalinpos = tmpinpos + thissize
        while tmpinpos + self.BLOCK_SIZE <= finalinpos:
            self.__getBestBFromData(in_, tmpinpos, bestb, bestexcept)
            tmpbestb = bestb.get()
            nbrexcept = bestexcept.get()
            exceptsize = 0
            remember = tmpoutpos
            tmpoutpos += 1

            if nbrexcept > 0:
                c = 0
                for i in range(self.BLOCK_SIZE):
                    if (in_[tmpinpos + i] >> self.__bits[tmpbestb]) != 0:
                        self.exceptbuffer[c + nbrexcept] = i
                        self.exceptbuffer[c] = (
                            in_[tmpinpos + i] >> self.__bits[tmpbestb]
                        )
                        c += 1

                exceptsize = S16.compress(
                    self.exceptbuffer, 0, 2 * nbrexcept, out, tmpoutpos
                )
                tmpoutpos += exceptsize

            out[remember] = tmpbestb | (nbrexcept << 8) | (exceptsize << 16)

            for k in range(0, self.BLOCK_SIZE, 32):
                BitPacking.fastpack(
                    in_, tmpinpos + k, out, tmpoutpos, self.__bits[tmpbestb]
                )
                tmpoutpos += self.__bits[tmpbestb]

            tmpinpos += self.BLOCK_SIZE

        inpos.set_(tmpinpos)
        outpos.set_(tmpoutpos)

    def __getBestBFromData(
        self, in_: typing.List[int], pos: int, bestb: IntWrapper, bestexcept: IntWrapper
    ) -> None:
        mb = Util.maxbits(in_, pos, self.BLOCK_SIZE)
        mini = 0
        if mini + 28 < self.__bits[self.__invbits[mb]]:
            mini = self.__bits[self.__invbits[mb]] - 28  # 28 is the max for exceptions
        besti = len(self.__bits) - 1
        bestcost = self.__bits[besti] * 4
        exceptcounter = 0

        for i in range(mini, len(self.__bits) - 1):
            tmpcounter = 0
            for k in range(pos, self.BLOCK_SIZE + pos):
                if (in_[k] >> self.__bits[i]) != 0:
                    tmpcounter += 1
            if tmpcounter == self.BLOCK_SIZE:
                continue  # no need

            for k, c in zip(range(pos, pos + self.BLOCK_SIZE), range(tmpcounter)):
                if (in_[k] >> self.__bits[i]) != 0:
                    self.exceptbuffer[tmpcounter + c] = k - pos
                    self.exceptbuffer[c] = in_[k] >> self.__bits[i]

            thiscost = self.__bits[i] * 4 + S16.estimatecompress(
                self.exceptbuffer, 0, 2 * tmpcounter
            )
            if thiscost <= bestcost:
                bestcost = thiscost
                besti = i
                exceptcounter = tmpcounter

        bestb.set_(besti)
        bestexcept.set_(exceptcounter)
