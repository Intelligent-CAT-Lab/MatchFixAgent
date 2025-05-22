from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class BinaryPacking(IntegerCODEC, SkippableIntegerCODEC):

    BLOCK_SIZE: int = 32

    def toString(self) -> str:
        return self.__class__.__name__

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        outlength = Util.greatestMultiple(num, self.BLOCK_SIZE)
        tmpinpos = inpos.get()
        s = outpos.get()

        while s + self.BLOCK_SIZE * 4 - 1 < outpos.get() + outlength:
            mbits1 = in_[tmpinpos] >> 24
            mbits2 = (in_[tmpinpos] >> 16) & 0xFF
            mbits3 = (in_[tmpinpos] >> 8) & 0xFF
            mbits4 = in_[tmpinpos] & 0xFF
            tmpinpos += 1

            BitPacking.fastunpack(in_, tmpinpos, out, s, mbits1)
            tmpinpos += mbits1
            BitPacking.fastunpack(in_, tmpinpos, out, s + self.BLOCK_SIZE, mbits2)
            tmpinpos += mbits2
            BitPacking.fastunpack(in_, tmpinpos, out, s + 2 * self.BLOCK_SIZE, mbits3)
            tmpinpos += mbits3
            BitPacking.fastunpack(in_, tmpinpos, out, s + 3 * self.BLOCK_SIZE, mbits4)
            tmpinpos += mbits4

            s += self.BLOCK_SIZE * 4

        while s < outpos.get() + outlength:
            mbits = in_[tmpinpos]
            tmpinpos += 1
            BitPacking.fastunpack(in_, tmpinpos, out, s, mbits)
            tmpinpos += mbits
            s += self.BLOCK_SIZE

        outpos.add(outlength)
        inpos.set_(tmpinpos)

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
        self.headlessUncompress(in_, inpos, inlength - 1, out, outpos, outlength)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.BLOCK_SIZE)
        tmpoutpos = outpos.get()
        s = inpos.get()
        while s + self.BLOCK_SIZE * 4 - 1 < inpos.get() + inlength:
            mbits1 = Util.maxbits(in_, s, self.BLOCK_SIZE)
            mbits2 = Util.maxbits(in_, s + self.BLOCK_SIZE, self.BLOCK_SIZE)
            mbits3 = Util.maxbits(in_, s + 2 * self.BLOCK_SIZE, self.BLOCK_SIZE)
            mbits4 = Util.maxbits(in_, s + 3 * self.BLOCK_SIZE, self.BLOCK_SIZE)
            out[tmpoutpos] = (mbits1 << 24) | (mbits2 << 16) | (mbits3 << 8) | mbits4
            tmpoutpos += 1
            BitPacking.fastpackwithoutmask(in_, s, out, tmpoutpos, mbits1)
            tmpoutpos += mbits1
            BitPacking.fastpackwithoutmask(
                in_, s + self.BLOCK_SIZE, out, tmpoutpos, mbits2
            )
            tmpoutpos += mbits2
            BitPacking.fastpackwithoutmask(
                in_, s + 2 * self.BLOCK_SIZE, out, tmpoutpos, mbits3
            )
            tmpoutpos += mbits3
            BitPacking.fastpackwithoutmask(
                in_, s + 3 * self.BLOCK_SIZE, out, tmpoutpos, mbits4
            )
            tmpoutpos += mbits4
            s += self.BLOCK_SIZE * 4
        while s < inpos.get() + inlength:
            mbits = Util.maxbits(in_, s, self.BLOCK_SIZE)
            out[tmpoutpos] = mbits
            tmpoutpos += 1
            BitPacking.fastpackwithoutmask(in_, s, out, tmpoutpos, mbits)
            tmpoutpos += mbits
            s += self.BLOCK_SIZE
        inpos.add(inlength)
        outpos.set_(tmpoutpos)

    def compress0(
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
        out[outpos.get()] = inlength
        outpos.increment()
        self.headlessCompress(in_, inpos, inlength, out, outpos)
