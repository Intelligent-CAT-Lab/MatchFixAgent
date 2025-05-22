from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.Util import *
from src.main.me.lemire.integercompression.differential.IntegratedBitPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class IntegratedBinaryPacking(IntegratedIntegerCODEC, SkippableIntegratedIntegerCODEC):

    BLOCK_SIZE: int = 32

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
        outlength = Util.greatestMultiple(num, self.BLOCK_SIZE)
        tmpinpos = inpos.get()
        initoffset = initvalue.get()
        s = outpos.get()

        while s + self.BLOCK_SIZE * 4 - 1 < outpos.get() + outlength:
            mbits1 = in_[tmpinpos] >> 24
            mbits2 = (in_[tmpinpos] >> 16) & 0xFF
            mbits3 = (in_[tmpinpos] >> 8) & 0xFF
            mbits4 = in_[tmpinpos] & 0xFF

            tmpinpos += 1
            IntegratedBitPacking.integratedunpack(
                initoffset, in_, tmpinpos, out, s, mbits1
            )
            tmpinpos += mbits1
            initoffset = out[s + 31]

            IntegratedBitPacking.integratedunpack(
                initoffset, in_, tmpinpos, out, s + self.BLOCK_SIZE, mbits2
            )
            tmpinpos += mbits2
            initoffset = out[s + self.BLOCK_SIZE + 31]

            IntegratedBitPacking.integratedunpack(
                initoffset, in_, tmpinpos, out, s + 2 * self.BLOCK_SIZE, mbits3
            )
            tmpinpos += mbits3
            initoffset = out[s + 2 * self.BLOCK_SIZE + 31]

            IntegratedBitPacking.integratedunpack(
                initoffset, in_, tmpinpos, out, s + 3 * self.BLOCK_SIZE, mbits4
            )
            tmpinpos += mbits4
            initoffset = out[s + 3 * self.BLOCK_SIZE + 31]

            s += self.BLOCK_SIZE * 4

        while s < outpos.get() + outlength:
            mbits = in_[tmpinpos]
            tmpinpos += 1
            IntegratedBitPacking.integratedunpack(
                initoffset, in_, tmpinpos, out, s, mbits
            )
            initoffset = out[s + 31]
            tmpinpos += mbits
            s += self.BLOCK_SIZE

        outpos.add(outlength)
        initvalue.set(initoffset)
        inpos.set(tmpinpos)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        initvalue: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.BLOCK_SIZE)
        if inlength == 0:
            return

        tmpoutpos = outpos.get()
        initoffset = initvalue.get()
        initvalue.set_(in_[inpos.get() + inlength - 1])
        s = inpos.get()

        while s + self.BLOCK_SIZE * 4 - 1 < inpos.get() + inlength:
            mbits1 = Util.maxdiffbits(initoffset, in_, s, self.BLOCK_SIZE)
            initoffset2 = in_[s + 31]
            mbits2 = Util.maxdiffbits(
                initoffset2, in_, s + self.BLOCK_SIZE, self.BLOCK_SIZE
            )
            initoffset3 = in_[s + self.BLOCK_SIZE + 31]
            mbits3 = Util.maxdiffbits(
                initoffset3, in_, s + 2 * self.BLOCK_SIZE, self.BLOCK_SIZE
            )
            initoffset4 = in_[s + 2 * self.BLOCK_SIZE + 31]
            mbits4 = Util.maxdiffbits(
                initoffset4, in_, s + 3 * self.BLOCK_SIZE, self.BLOCK_SIZE
            )

            out[tmpoutpos] = (mbits1 << 24) | (mbits2 << 16) | (mbits3 << 8) | mbits4
            tmpoutpos += 1

            IntegratedBitPacking.integratedpack(
                initoffset, in_, s, out, tmpoutpos, mbits1
            )
            tmpoutpos += mbits1
            IntegratedBitPacking.integratedpack(
                initoffset2, in_, s + self.BLOCK_SIZE, out, tmpoutpos, mbits2
            )
            tmpoutpos += mbits2
            IntegratedBitPacking.integratedpack(
                initoffset3, in_, s + 2 * self.BLOCK_SIZE, out, tmpoutpos, mbits3
            )
            tmpoutpos += mbits3
            IntegratedBitPacking.integratedpack(
                initoffset4, in_, s + 3 * self.BLOCK_SIZE, out, tmpoutpos, mbits4
            )
            tmpoutpos += mbits4

            initoffset = in_[s + 3 * self.BLOCK_SIZE + 31]
            s += self.BLOCK_SIZE * 4

        while s < inpos.get() + inlength:
            mbits = Util.maxdiffbits(initoffset, in_, s, self.BLOCK_SIZE)
            out[tmpoutpos] = mbits
            tmpoutpos += 1

            IntegratedBitPacking.integratedpack(
                initoffset, in_, s, out, tmpoutpos, mbits
            )
            tmpoutpos += mbits

            initoffset = in_[s + 31]
            s += self.BLOCK_SIZE

        inpos.add(inlength)
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
        self.headlessUncompress(
            in_, inpos, inlength, out, outpos, outlength, IntWrapper(0)
        )

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
        self.headlessCompress(in_, inpos, inlength, out, outpos, IntWrapper(0))
