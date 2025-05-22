from __future__ import annotations
import copy
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class ColognePhonetic(StringEncoder):

    __CHAR_IGNORE: str = "-"
    __DTX: typing.List[str] = ["D", "T", "X"]
    __AHKOQUX: typing.List[str] = ["A", "H", "K", "O", "Q", "U", "X"]
    __SZ: typing.List[str] = ["S", "Z"]
    __AHKLOQRUX: typing.List[str] = ["A", "H", "K", "L", "O", "Q", "R", "U", "X"]
    __CKQ: typing.List[str] = ["C", "K", "Q"]
    __GKQ: typing.List[str] = ["G", "K", "Q"]
    __FPVW: typing.List[str] = ["F", "P", "V", "W"]
    __CSZ: typing.List[str] = ["C", "S", "Z"]
    __AEIJOUY: typing.List[str] = ["A", "E", "I", "J", "O", "U", "Y"]

    def isEncodeEqual(self, text1: str, text2: str) -> bool:
        return self.colognePhonetic(text1) == self.colognePhonetic(text2)

    def encode1(self, text: str) -> str:
        return self.colognePhonetic(text)

    def encode0(self, object_: typing.Any) -> typing.Any:
        if not isinstance(object_, str):
            raise EncoderException(
                f"This method's parameter was expected to be of the type {str.__name__}. "
                f"But actually it was of the type {type(object_).__name__}.",
                None,
            )
        return self.encode1(object_)

    def colognePhonetic(self, text: str) -> str:
        if text is None:
            return None

        input_buffer = CologneInputBuffer(self.__preprocess(text))
        output_buffer = CologneOutputBuffer(input_buffer.length() * 2)

        next_char = self.__CHAR_IGNORE
        last_char = self.__CHAR_IGNORE

        while not input_buffer.isEmpty():
            chr = input_buffer.removeNext()

            if not input_buffer.isEmpty():
                next_char = input_buffer.getNextChar()
            else:
                next_char = self.__CHAR_IGNORE

            if chr < "A" or chr > "Z":
                continue  # ignore unwanted characters

            if self.__arrayContains(self.__AEIJOUY, chr):
                output_buffer.put("0")
            elif chr == "B" or (chr == "P" and next_char != "H"):
                output_buffer.put("1")
            elif (chr == "D" or chr == "T") and not self.__arrayContains(
                self.__CSZ, next_char
            ):
                output_buffer.put("2")
            elif self.__arrayContains(self.__FPVW, chr):
                output_buffer.put("3")
            elif self.__arrayContains(self.__GKQ, chr):
                output_buffer.put("4")
            elif chr == "X" and not self.__arrayContains(self.__CKQ, last_char):
                output_buffer.put("4")
                output_buffer.put("8")
            elif chr == "S" or chr == "Z":
                output_buffer.put("8")
            elif chr == "C":
                if output_buffer.isEmpty():
                    if self.__arrayContains(self.__AHKLOQRUX, next_char):
                        output_buffer.put("4")
                    else:
                        output_buffer.put("8")
                elif self.__arrayContains(
                    self.__SZ, last_char
                ) or not self.__arrayContains(self.__AHKOQUX, next_char):
                    output_buffer.put("8")
                else:
                    output_buffer.put("4")
            elif self.__arrayContains(self.__DTX, chr):
                output_buffer.put("8")
            else:
                if chr == "R":
                    output_buffer.put("7")
                elif chr == "L":
                    output_buffer.put("5")
                elif chr == "M" or chr == "N":
                    output_buffer.put("6")
                elif chr == "H":
                    output_buffer.put(self.__CHAR_IGNORE)  # needed by put
                # default case: do nothing

            last_char = chr

        return output_buffer.toString()

    def __preprocess(self, text: str) -> typing.List[str]:
        chrs = list(
            text.upper()
        )  # Convert text to uppercase and then to a list of characters

        for index in range(len(chrs)):
            if chrs[index] == "\u00c4":  # capital A, umlaut mark
                chrs[index] = "A"
            elif chrs[index] == "\u00dc":  # capital U, umlaut mark
                chrs[index] = "U"
            elif chrs[index] == "\u00d6":  # capital O, umlaut mark
                chrs[index] = "O"

        return chrs

    @staticmethod
    def __arrayContains(arr: typing.List[str], key: str) -> bool:
        for element in arr:
            if element == key:
                return True
        return False


class CologneBuffer(ABC):

    _length: int = 0
    _data: typing.List[str] = None

    def toString(self) -> str:
        return "".join(self._copyData(0, self._length))

    def isEmpty(self) -> bool:
        return self.length() == 0

    def length(self) -> int:
        return self._length

    def __init__(
        self, constructorId: int, data: typing.List[str], buffSize: int
    ) -> None:

        pass  # LLM could not translate this method

    def _copyData(self, start: int, length: int) -> typing.List[str]:
        return self.data[start : start + length]


class CologneOutputBuffer(CologneBuffer):

    __lastCode: str = "\u0000"

    def _copyData(self, start: int, length: int) -> typing.List[str]:
        newData = self.data[start : start + length]
        return newData

    def put(self, code: str) -> None:
        if (
            code != self.__CHAR_IGNORE
            and self.__lastCode != code
            and (code != "0" or self._length == 0)
        ):
            self._data[self._length] = code
            self._length += 1
        self.__lastCode = code

    def __init__(self, buffSize: int) -> None:
        super().__init__(0, None, buffSize)
        self.__lastCode = "/"  # impossible value


class CologneInputBuffer(CologneBuffer):

    def _copyData(self, start: int, length: int) -> typing.List[str]:
        newData = [""] * length
        newData[:] = self.data[
            len(self.data) - length + start : len(self.data) - length + start + length
        ]
        return newData

    def removeNext(self) -> str:
        ch = self.getNextChar()
        self.length -= 1
        return ch

    def _getNextPos(self) -> int:
        return len(self.data) - self.length

    def getNextChar(self) -> str:
        return self.data[self._getNextPos()]

    def __init__(self, data: typing.List[str]) -> None:
        super().__init__(1, data, 0)
