from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class RefinedSoundex(StringEncoder):

    US_ENGLISH: RefinedSoundex = None
    US_ENGLISH_MAPPING_STRING: str = "01360240043788015936020505"
    __soundexMapping: typing.List[str] = None

    __US_ENGLISH_MAPPING: typing.List[str] = list(US_ENGLISH_MAPPING_STRING)

    @staticmethod
    def initialize_fields() -> None:
        RefinedSoundex.US_ENGLISH: RefinedSoundex = RefinedSoundex(2, None, None)

    def soundex(self, str_: str) -> str:
        if str_ is None:
            return None
        str_ = SoundexUtils.clean(str_)
        if not str_:
            return str_

        s_buf = [str_[0]]

        last = "*"

        for char in str_:
            current = self.getMappingCode(char)
            if current == last:
                continue
            if current != "\0":  # '\0' is the equivalent of 0 in Java
                s_buf.append(current)

            last = current

        return "".join(s_buf)

    def encode1(self, str_: str) -> str:
        return self.soundex(str_)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to RefinedSoundex encode is not of type java.lang.String",
                None,
            )
        return self.soundex(obj)

    def difference(self, s1: str, s2: str) -> int:
        return SoundexUtils.difference(self, s1, s2)

    def __init__(
        self,
        constructorId: int,
        mapping: Optional[str],
        mapping1: Optional[typing.List[str]],
    ) -> None:
        if constructorId == 0:
            self.__soundexMapping = list(mapping) if mapping else []
        elif constructorId == 1:
            self.__soundexMapping = mapping1.copy() if mapping1 else []
        else:
            self.__soundexMapping = self.__US_ENGLISH_MAPPING

    def getMappingCode(self, c: str) -> str:
        if not c.isalpha():
            return "\0"  # Return null character as equivalent to 0 in Java
        return self.__soundexMapping[ord(c.upper()) - ord("A")]


RefinedSoundex.initialize_fields()
