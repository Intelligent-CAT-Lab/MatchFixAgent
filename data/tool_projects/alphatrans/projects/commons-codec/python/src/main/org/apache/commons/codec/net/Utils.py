from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.DecoderException import *


class Utils:

    __RADIX: int = 16

    @staticmethod
    def hexDigit(b: int) -> str:
        return format(b & 0xF, "X")

    @staticmethod
    def digit16(b: int) -> int:
        i = int(chr(b), Utils.__RADIX) if 0 <= b < 256 else -1
        if i == -1:
            raise DecoderException(
                f"Invalid URL encoding: not a valid digit (radix {Utils.__RADIX}): {b}",
                None,
            )
        return i
