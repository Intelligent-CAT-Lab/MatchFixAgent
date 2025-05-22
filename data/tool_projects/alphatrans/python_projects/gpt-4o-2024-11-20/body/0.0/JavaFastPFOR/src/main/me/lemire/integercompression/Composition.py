from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *


class Composition(IntegerCODEC):

    F2: IntegerCODEC = None

    F1: IntegerCODEC = None

    def toString(self) -> str:
        return self.F1.toString() + " + " + self.F2.toString()

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
        init = inpos.get()
        self.F1.uncompress0(in_, inpos, inlength, out, outpos)
        inlength -= inpos.get() - init
        self.F2.uncompress0(in_, inpos, inlength, out, outpos)

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

        inpos_init = inpos.get()
        outpos_init = outpos.get()

        self.F1.compress0(in_, inpos, inlength, out, outpos)

        if outpos.get() == outpos_init:
            out[outpos_init] = 0
            outpos.increment()

        inlength -= inpos.get() - inpos_init
        self.F2.compress0(in_, inpos, inlength, out, outpos)

    def __init__(self, f1: IntegerCODEC, f2: IntegerCODEC) -> None:
        self.F1 = f1
        self.F2 = f2
