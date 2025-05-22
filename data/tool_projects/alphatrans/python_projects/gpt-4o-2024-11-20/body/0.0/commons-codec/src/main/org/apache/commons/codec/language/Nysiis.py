from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class Nysiis(StringEncoder):

    __strict: bool = False

    __TRUE_LENGTH: int = 6
    __SPACE: str = " "
    __PAT_DT_ETC: re.Pattern = re.compile(r"(DT|RT|RD|NT|ND)$")
    __PAT_EE_IE: re.Pattern = re.compile(r"(EE|IE)$")
    __PAT_SCH: re.Pattern = re.compile(r"^SCH")
    __PAT_PH_PF: re.Pattern = re.compile(r"^(PH|PF)")
    __PAT_K: re.Pattern = re.compile(r"^K")
    __PAT_KN: re.Pattern = re.compile(r"^KN")
    __PAT_MAC: re.Pattern = re.compile(r"^MAC")
    __CHARS_SSS: typing.List[str] = ["S", "S", "S"]
    __CHARS_S: typing.List[str] = ["S"]
    __CHARS_NN: typing.List[str] = ["N", "N"]
    __CHARS_N: typing.List[str] = ["N"]
    __CHARS_G: typing.List[str] = ["G"]
    __CHARS_FF: typing.List[str] = ["F", "F"]
    __CHARS_C: typing.List[str] = ["C"]
    __CHARS_AF: typing.List[str] = ["A", "F"]
    __CHARS_A: typing.List[str] = ["A"]

    def nysiis(self, str_: str) -> str:
        if str_ is None:
            return None

        str_ = SoundexUtils.clean(str_)

        if not str_:
            return str_

        str_ = self.__PAT_MAC.sub("MCC", str_)
        str_ = self.__PAT_KN.sub("NN", str_)
        str_ = self.__PAT_K.sub("C", str_)
        str_ = self.__PAT_PH_PF.sub("FF", str_)
        str_ = self.__PAT_SCH.sub("SSS", str_)

        str_ = self.__PAT_EE_IE.sub("Y", str_)
        str_ = self.__PAT_DT_ETC.sub("D", str_)

        key = [str_[0]]

        chars = list(str_)
        len_ = len(chars)

        for i in range(1, len_):
            next_ = chars[i + 1] if i < len_ - 1 else self.__SPACE
            aNext = chars[i + 2] if i < len_ - 2 else self.__SPACE
            transcoded = self.__transcodeRemaining(chars[i - 1], chars[i], next_, aNext)
            chars[i : i + len(transcoded)] = transcoded

            if chars[i] != chars[i - 1]:
                key.append(chars[i])

        if len(key) > 1:
            lastChar = key[-1]

            if lastChar == "S":
                key.pop()
                lastChar = key[-1]

            if len(key) > 2:
                last2Char = key[-2]
                if last2Char == "A" and lastChar == "Y":
                    key.pop(-2)

            if lastChar == "A":
                key.pop()

        string = "".join(key)
        return string[: self.__TRUE_LENGTH] if self.isStrict() else string

    def isStrict(self) -> bool:
        return self.__strict

    def encode1(self, str_: str) -> str:
        return self.nysiis(str_)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Nysiis encode is not of type java.lang.String",
                None,
            )
        return self.nysiis(obj)

    @staticmethod
    def Nysiis1() -> Nysiis:
        return Nysiis(True)

    def __init__(self, strict: bool) -> None:
        self.__strict = strict

    @staticmethod
    def __transcodeRemaining(
        prev: str, curr: str, next_: str, aNext: str
    ) -> typing.List[str]:
        if curr == "E" and next_ == "V":
            return Nysiis.__CHARS_AF

        if Nysiis.__isVowel(curr):
            return Nysiis.__CHARS_A

        match curr:
            case "Q":
                return Nysiis.__CHARS_G
            case "Z":
                return Nysiis.__CHARS_S
            case "M":
                return Nysiis.__CHARS_N
            case "K":
                if next_ == "N":
                    return Nysiis.__CHARS_NN
                return Nysiis.__CHARS_C

        if curr == "S" and next_ == "C" and aNext == "H":
            return Nysiis.__CHARS_SSS

        if curr == "P" and next_ == "H":
            return Nysiis.__CHARS_FF

        if curr == "H" and (not Nysiis.__isVowel(prev) or not Nysiis.__isVowel(next_)):
            return [prev]

        if curr == "W" and Nysiis.__isVowel(prev):
            return [prev]

        return [curr]

    @staticmethod
    def __isVowel(c: str) -> bool:
        return c in {"A", "E", "I", "O", "U"}
