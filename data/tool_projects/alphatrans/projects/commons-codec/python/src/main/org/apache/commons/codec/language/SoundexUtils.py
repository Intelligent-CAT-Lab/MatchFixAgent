from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class SoundexUtils:

    @staticmethod
    def differenceEncoded(es1: str, es2: str) -> int:
        if es1 is None or es2 is None:
            return 0
        length_to_match = min(len(es1), len(es2))
        diff = 0
        for i in range(length_to_match):
            if es1[i] == es2[i]:
                diff += 1
        return diff

    @staticmethod
    def difference(encoder: StringEncoder, s1: str, s2: str) -> int:
        return SoundexUtils.differenceEncoded(encoder.encode(s1), encoder.encode(s2))

    @staticmethod
    def clean(str_: str) -> str:
        if str_ is None or not str_:
            return str_
        len_ = len(str_)
        chars = []
        for i in range(len_):
            if str_[i].isalpha():
                chars.append(str_[i])
        if len(chars) == len_:
            return str_.upper()
        return "".join(chars).upper()
