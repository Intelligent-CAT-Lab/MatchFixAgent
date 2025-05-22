from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.com.kamikaze.pfordelta.PForDelta import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class Kamikaze(IntegerCODEC, SkippableIntegerCODEC):

    __BLOCK_SIZE: int = 128

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
        inlength = Util.greatestMultiple(inlength, self.__BLOCK_SIZE)
        if inlength == 0:
            return
        out[outpos.get()] = inlength
        outpos.increment()
        self.headlessCompress(in_, inpos, inlength, out, outpos)

    def toString(self) -> str:
        return "Kamikaze's PForDelta"

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        num = Util.greatestMultiple(num, self.__BLOCK_SIZE)
        if num > 0:
            d = PForDelta.decompressOneBlock(out, in_, num)
            inpos.add(d // 32)
            outpos.add(num)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        inlength = Util.greatestMultiple(inlength, self.__BLOCK_SIZE)
        if inlength > 0:
            out2 = PForDelta.compressOneBlockOpt(in_, inlength)
            inpos.add(inlength)
            out[outpos.get() : outpos.get() + len(out2)] = out2
            outpos.add(len(out2))
