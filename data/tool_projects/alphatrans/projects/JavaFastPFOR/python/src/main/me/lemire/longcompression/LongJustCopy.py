from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class LongJustCopy(LongCODEC, SkippableLongCODEC):

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
        out[outpos.get() : outpos.get() + num] = in_[inpos.get() : inpos.get() + num]
        inpos.add(num)
        outpos.add(num)

    def toString(self) -> str:
        return self.__class__.__name__

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        self.headlessUncompress(in_, inpos, inlength, out, outpos, inlength)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        out[outpos.get() : outpos.get() + inlength] = in_[
            inpos.get() : inpos.get() + inlength
        ]
        inpos.add(inlength)
        outpos.add(inlength)
