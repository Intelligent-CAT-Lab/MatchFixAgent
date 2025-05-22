from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class SkippableIntegratedComposition(SkippableIntegratedIntegerCODEC):

    F2: SkippableIntegratedIntegerCODEC = None

    F1: SkippableIntegratedIntegerCODEC = None

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
        if inlength == 0:
            return
        init = inpos.get()
        self.F1.headlessUncompress(in_, inpos, inlength, out, outpos, num, initvalue)
        if inpos.get() == init:
            inpos.increment()
        inlength -= inpos.get() - init

        num -= outpos.get()
        self.F2.headlessUncompress(in_, inpos, inlength, out, outpos, num, initvalue)

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        initvalue: IntWrapper,
    ) -> None:
        if inlength == 0:
            return
        init = inpos.get()
        outposInit = outpos.get()

        self.F1.headlessCompress(in_, inpos, inlength, out, outpos, initvalue)
        if outpos.get() == outposInit:
            out[outposInit] = 0
            outpos.increment()

        inlength -= inpos.get() - init
        self.F2.headlessCompress(in_, inpos, inlength, out, outpos, initvalue)

    def toString(self) -> str:
        return self.F1.toString() + " + " + self.F2.toString()

    def __init__(
        self, f1: SkippableIntegratedIntegerCODEC, f2: SkippableIntegratedIntegerCODEC
    ) -> None:
        self.F1 = f1
        self.F2 = f2
