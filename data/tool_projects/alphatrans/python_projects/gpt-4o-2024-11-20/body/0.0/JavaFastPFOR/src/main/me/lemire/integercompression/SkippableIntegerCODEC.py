from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *


class SkippableIntegerCODEC(ABC):

    def headlessUncompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
        num: int,
    ) -> None:
        # The implementation of this method would depend on the specific logic
        # of the Java method. Since the Java method is abstract (no body provided),
        # this Python method is also left as a placeholder (pass).
        pass

    def headlessCompress(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation of the method goes here
        pass
