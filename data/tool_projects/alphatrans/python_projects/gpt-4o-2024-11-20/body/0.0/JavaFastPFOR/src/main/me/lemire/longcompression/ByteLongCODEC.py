from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *


class ByteLongCODEC(ABC):

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        pass

    def compress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation of the method goes here
        pass
