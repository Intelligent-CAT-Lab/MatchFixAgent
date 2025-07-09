from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class StringEncoderComparator:

    __stringEncoder: StringEncoder = None

    def compare(self, o1: typing.Any, o2: typing.Any) -> int:
        compare_code = 0

        try:
            s1 = self.__stringEncoder.encode(o1)
            s2 = self.__stringEncoder.encode(o2)
            if isinstance(s1, Comparable) and isinstance(s2, Comparable):
                compare_code = (s1 > s2) - (s1 < s2)
            else:
                raise EncoderException("Encoded objects are not comparable")
        except EncoderException as ee:
            compare_code = 0

        return compare_code

    def __init__(self, constructorId: int, stringEncoder: StringEncoder) -> None:
        if constructorId == 0:
            self.__stringEncoder = stringEncoder
        else:
            self.__stringEncoder = None  # Trying to use this will cause things to break
