from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *


class LongCODEC(ABC):

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation logic goes here
        # Since the Java method is abstract (no implementation), this Python method is also left unimplemented.
        pass

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation of the method goes here
        # Since the Java method is abstract (no implementation), the Python method remains unimplemented
        pass
