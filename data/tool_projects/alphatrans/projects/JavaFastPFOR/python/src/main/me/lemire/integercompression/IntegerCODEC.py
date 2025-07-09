from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.IntWrapper import *


class IntegerCODEC(ABC):

    def uncompress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation of the method goes here
        # Since the Java method is abstract, no specific logic is provided.
        # You can implement the logic here if needed.
        pass

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        # Implementation of the method should go here
        # Since the Java method is abstract, no specific logic is provided
        pass
