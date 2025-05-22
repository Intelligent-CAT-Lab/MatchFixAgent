from __future__ import annotations
import re
import io
import typing
from typing import *


class RoaringIntPacking:

    __TWO_64: int = 1 << 64

    @staticmethod
    def toUnsignedString(l: int) -> str:
        b = l
        if b < 0:
            b += RoaringIntPacking.__TWO_64
        return str(b)

    @staticmethod
    def compareUnsigned(x: int, y: int) -> int:
        return (x + (1 << 31)) - (y + (1 << 31))

    @staticmethod
    def unsignedComparator() -> typing.Callable[[int, int], int]:
        def compare(o1: int, o2: int) -> int:
            return (o1 & 0xFFFFFFFF) - (o2 & 0xFFFFFFFF)

        return compare

    @staticmethod
    def highestHigh(signedLongs: bool) -> int:
        if signedLongs:
            return (2**31) - 1  # Equivalent to 2147483647 in Java
        else:
            return -1

    @staticmethod
    def pack(high: int, low: int) -> int:
        return ((high & 0xFFFFFFFF) << 32) | (low & 0xFFFFFFFF)

    @staticmethod
    def low(id_: int) -> int:
        return id_ & 0xFFFFFFFF

    @staticmethod
    def high(id_: int) -> int:
        return int(id_ >> 32)
