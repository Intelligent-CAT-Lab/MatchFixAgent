from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *


class JustCopy(IntegerCODEC, SkippableIntegerCODEC):

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

    def uncompress0(
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
