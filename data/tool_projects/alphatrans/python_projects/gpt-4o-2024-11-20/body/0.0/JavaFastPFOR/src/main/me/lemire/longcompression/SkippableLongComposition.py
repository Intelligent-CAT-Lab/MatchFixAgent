from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.longcompression.SkippableLongCODEC import *


class SkippableLongComposition(SkippableLongCODEC):

    F2: SkippableLongCODEC = None

    F1: SkippableLongCODEC = None

    def toString(self) -> str:
        return self.F1.toString() + "+" + self.F2.toString()

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        init = inpos.get()
        self.F1.headlessUncompress(in_, inpos, inlength, out, outpos, num)
        if inpos.get() == init:
            inpos.increment()
        inlength -= inpos.get() - init
        num -= outpos.get()
        self.F2.headlessUncompress(in_, inpos, inlength, out, outpos, num)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        init = inpos.get()
        outposInit = outpos.get()
        self.F1.headlessCompress(in_, inpos, inlength, out, outpos)
        if outpos.get() == outposInit:
            out[outposInit] = 0
            outpos.increment()
        inlength -= inpos.get() - init
        self.F2.headlessCompress(in_, inpos, inlength, out, outpos)

    def __init__(self, f1: SkippableLongCODEC, f2: SkippableLongCODEC) -> None:
        self.F1 = f1
        self.F2 = f2
