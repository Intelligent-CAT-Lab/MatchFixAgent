from __future__ import annotations
import re
from io import IOBase
import io
import enum
import typing
from typing import *
from src.main.org.fusesource.jansi.Ansi import *


class AnsiRenderer:

    CODE_LIST_SEPARATOR: str = ","
    CODE_TEXT_SEPARATOR: str = " "
    END_TOKEN: str = "|@"
    BEGIN_TOKEN: str = "@|"
    __END_TOKEN_LEN: int = 2
    __BEGIN_TOKEN_LEN: int = 2

    @staticmethod
    def test(text: str) -> bool:
        return text is not None and AnsiRenderer.BEGIN_TOKEN in text

    @staticmethod
    def renderCodes1(codes: str) -> str:
        return AnsiRenderer.renderCodes0(codes.split())

    @staticmethod
    def renderCodes0(codes: typing.List[str]) -> str:
        return AnsiRenderer.__render3(Ansi.ansi0(), codes).toString()

    @staticmethod
    def render2(text: str, codes: typing.List[str]) -> str:
        return AnsiRenderer.__render3(Ansi.ansi0(), codes).a1(text).reset().toString()

    @staticmethod
    def render1(
        input_: str, target: typing.Union[typing.List, io.TextIOBase]
    ) -> typing.Union[typing.List, io.TextIOBase]:
        i = 0

        while True:
            j = input_.find(AnsiRenderer.BEGIN_TOKEN, i)
            if j == -1:
                if i == 0:
                    target.append(input_)
                    return target
                target.append(input_[i:])
                return target

            target.append(input_[i:j])
            k = input_.find(AnsiRenderer.END_TOKEN, j)

            if k == -1:
                target.append(input_)
                return target

            j += AnsiRenderer.__BEGIN_TOKEN_LEN

            # Check for invalid string with END_TOKEN before BEGIN_TOKEN
            if k < j:
                raise ValueError("Invalid input string found.")

            spec = input_[j:k]
            items = spec.split(AnsiRenderer.CODE_TEXT_SEPARATOR, 1)

            if len(items) == 1:
                target.append(input_)
                return target

            replacement = AnsiRenderer.render2(
                items[1], items[0].split(AnsiRenderer.CODE_LIST_SEPARATOR)
            )
            target.append(replacement)

            i = k + AnsiRenderer.__END_TOKEN_LEN

    @staticmethod
    def render0(input_: str) -> str:
        try:
            return "".join(AnsiRenderer.render1(input_, []))
        except IOError as e:
            raise ValueError(e)

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")

    @staticmethod
    def __render3(ansi: Ansi, names: typing.List[str]) -> Ansi:
        for name in names:
            code = Code.valueOf(name.upper())
            if code.isColor():
                if code.isBackground():
                    ansi.bg0(code.getColor())
                else:
                    ansi.fg0(code.getColor())
            elif code.isAttribute():
                ansi.a0(code.getAttribute())
        return ansi


class Code:

    FAINT: Code = None

    BOLD: Code = None

    UNDERLINE_OFF: Code = None

    UNDERLINE_DOUBLE: Code = None

    CONCEAL_OFF: Code = None

    CONCEAL_ON: Code = None

    NEGATIVE_OFF: Code = None

    NEGATIVE_ON: Code = None

    BLINK_OFF: Code = None

    BLINK_FAST: Code = None

    BLINK_SLOW: Code = None

    UNDERLINE: Code = None

    ITALIC: Code = None

    INTENSITY_FAINT: Code = None

    INTENSITY_BOLD: Code = None

    RESET: Code = None

    BG_DEFAULT: Code = None

    BG_WHITE: Code = None

    BG_CYAN: Code = None

    BG_MAGENTA: Code = None

    BG_BLUE: Code = None

    BG_YELLOW: Code = None

    BG_GREEN: Code = None

    BG_RED: Code = None

    BG_BLACK: Code = None

    FG_DEFAULT: Code = None

    FG_WHITE: Code = None

    FG_CYAN: Code = None

    FG_MAGENTA: Code = None

    FG_BLUE: Code = None

    FG_YELLOW: Code = None

    FG_GREEN: Code = None

    FG_RED: Code = None

    FG_BLACK: Code = None

    DEFAULT: Code = None

    WHITE: Code = None

    CYAN: Code = None

    MAGENTA: Code = None

    BLUE: Code = None

    YELLOW: Code = None

    GREEN: Code = None

    RED: Code = None

    BLACK: Code = None

    __background: bool = False

    __n: enum.Enum = None

    def isBackground(self) -> bool:
        return self.__background

    def getAttribute(self) -> Attribute:
        return self.__n  # Assuming `Attribute` is a type that `self.__n` can be cast to

    def isAttribute(self) -> bool:
        return isinstance(self.__n, Attribute)

    def getColor(self) -> Ansi.Color:
        return self.__n

    def isColor(self) -> bool:
        return isinstance(self.__n, Ansi.Color)

    def __init__(self, n: enum.Enum, background: bool) -> None:
        self.__n = n
        self.__background = background
