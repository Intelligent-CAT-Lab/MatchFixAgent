from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class Metaphone(StringEncoder):

    __maxCodeLen: int = 4
    __VARSON: str = "CSPTG"
    __FRONTV: str = "EIY"
    __VOWELS: str = "AEIOU"

    def setMaxCodeLen(self, maxCodeLen: int) -> None:
        self.__maxCodeLen = maxCodeLen

    def getMaxCodeLen(self) -> int:
        return self.__maxCodeLen

    def isMetaphoneEqual(self, str1: str, str2: str) -> bool:
        return self.metaphone(str1) == self.metaphone(str2)

    def encode1(self, str_: str) -> str:
        return self.metaphone(str_)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Metaphone encode is not of type java.lang.String",
                None,
            )
        return self.metaphone(obj)

    def metaphone(self, txt: str) -> str:
        hard = False
        if txt is None or len(txt) == 0:
            return ""
        if len(txt) == 1:
            return txt.upper()

        inwd = list(txt.upper())
        local = []
        code = []

        # Handle initial letters
        if inwd[0] in {"K", "G", "P"} and len(inwd) > 1 and inwd[1] == "N":
            local.extend(inwd[1:])
        elif inwd[0] == "A" and len(inwd) > 1 and inwd[1] == "E":
            local.extend(inwd[1:])
        elif inwd[0] == "W" and len(inwd) > 1:
            if inwd[1] == "R":
                local.extend(inwd[1:])
            elif inwd[1] == "H":
                local.extend(inwd[1:])
                local[0] = "W"
            else:
                local.extend(inwd)
        elif inwd[0] == "X":
            inwd[0] = "S"
            local.extend(inwd)
        else:
            local.extend(inwd)

        wdsz = len(local)
        n = 0

        while len(code) < self.getMaxCodeLen() and n < wdsz:
            symb = local[n]
            if symb != "C" and self.__isPreviousChar(local, n, symb):
                n += 1
            else:
                if symb in {"A", "E", "I", "O", "U"}:
                    if n == 0:
                        code.append(symb)
                elif symb == "B":
                    if not (
                        self.__isPreviousChar(local, n, "M")
                        and self.__isLastChar(wdsz, n)
                    ):
                        code.append(symb)
                elif symb == "C":
                    if (
                        self.__isPreviousChar(local, n, "S")
                        and not self.__isLastChar(wdsz, n)
                        and self.__FRONTV.find(local[n + 1]) >= 0
                    ):
                        pass
                    elif self.__regionMatch(local, n, "CIA"):
                        code.append("X")
                    elif (
                        not self.__isLastChar(wdsz, n)
                        and self.__FRONTV.find(local[n + 1]) >= 0
                    ):
                        code.append("S")
                    elif self.__isPreviousChar(local, n, "S") and self.__isNextChar(
                        local, n, "H"
                    ):
                        code.append("K")
                    elif self.__isNextChar(local, n, "H"):
                        if n == 0 and wdsz >= 3 and self.__isVowel(local, 2):
                            code.append("K")
                        else:
                            code.append("X")
                    else:
                        code.append("K")
                elif symb == "D":
                    if (
                        not self.__isLastChar(wdsz, n + 1)
                        and self.__isNextChar(local, n, "G")
                        and self.__FRONTV.find(local[n + 2]) >= 0
                    ):
                        code.append("J")
                        n += 2
                    else:
                        code.append("T")
                elif symb == "G":
                    if self.__isLastChar(wdsz, n + 1) and self.__isNextChar(
                        local, n, "H"
                    ):
                        pass
                    elif (
                        not self.__isLastChar(wdsz, n + 1)
                        and self.__isNextChar(local, n, "H")
                        and not self.__isVowel(local, n + 2)
                    ):
                        pass
                    elif n > 0 and (
                        self.__regionMatch(local, n, "GN")
                        or self.__regionMatch(local, n, "GNED")
                    ):
                        pass
                    else:
                        hard = self.__isPreviousChar(local, n, "G")
                        if (
                            not self.__isLastChar(wdsz, n)
                            and self.__FRONTV.find(local[n + 1]) >= 0
                            and not hard
                        ):
                            code.append("J")
                        else:
                            code.append("K")
                elif symb == "H":
                    if (
                        not self.__isLastChar(wdsz, n)
                        and self.__VARSON.find(local[n - 1]) < 0
                        and self.__isVowel(local, n + 1)
                    ):
                        code.append("H")
                elif symb in {"F", "J", "L", "M", "N", "R"}:
                    code.append(symb)
                elif symb == "K":
                    if n == 0 or not self.__isPreviousChar(local, n, "C"):
                        code.append(symb)
                elif symb == "P":
                    if self.__isNextChar(local, n, "H"):
                        code.append("F")
                    else:
                        code.append(symb)
                elif symb == "Q":
                    code.append("K")
                elif symb == "S":
                    if (
                        self.__regionMatch(local, n, "SH")
                        or self.__regionMatch(local, n, "SIO")
                        or self.__regionMatch(local, n, "SIA")
                    ):
                        code.append("X")
                    else:
                        code.append("S")
                elif symb == "T":
                    if self.__regionMatch(local, n, "TIA") or self.__regionMatch(
                        local, n, "TIO"
                    ):
                        code.append("X")
                    elif self.__regionMatch(local, n, "TCH"):
                        pass
                    elif self.__regionMatch(local, n, "TH"):
                        code.append("0")
                    else:
                        code.append("T")
                elif symb == "V":
                    code.append("F")
                elif symb in {"W", "Y"}:
                    if not self.__isLastChar(wdsz, n) and self.__isVowel(local, n + 1):
                        code.append(symb)
                elif symb == "X":
                    code.append("K")
                    code.append("S")
                elif symb == "Z":
                    code.append("S")
                n += 1

            if len(code) > self.getMaxCodeLen():
                code = code[: self.getMaxCodeLen()]

        return "".join(code)

    def __init__(self) -> None:
        pass

    def __isLastChar(self, wdsz: int, n: int) -> bool:
        return n + 1 == wdsz

    def __regionMatch(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, test: str
    ) -> bool:
        matches = False
        if index >= 0 and index + len(test) - 1 < len(string):
            substring = string[index : index + len(test)]
            matches = substring == test
        return matches

    def __isNextChar(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, c: str
    ) -> bool:

        pass  # LLM could not translate this method

    def __isPreviousChar(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int, c: str
    ) -> bool:
        matches = False
        if index > 0 and index < len(string):
            matches = string[index - 1] == c
        return matches

    def __isVowel(
        self, string: typing.Union[typing.List[str], io.StringIO], index: int
    ) -> bool:
        return self.__VOWELS.find(string[index].upper()) >= 0
