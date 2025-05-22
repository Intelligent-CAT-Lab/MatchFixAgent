from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.AnsiRenderer import *


class Ansi:

    DISABLE: str = None
    __attributeOptions: typing.List[int] = []

    __builder: typing.Union[typing.List[str], io.StringIO] = None

    __holder: contextvars.ContextVar[typing.TypeVar("T", bound=bool)] = (
        None  # LLM could not translate this field
    )

    __detector: typing.Callable[[], bool] = None
    __SECOND_ESC_CHAR: str = "["
    __FIRST_ESC_CHAR: str = "\x1b"

    @staticmethod
    def initialize_fields() -> None:
        Ansi.DISABLE: str = f"{Ansi.__name__}.disable"

        Ansi.__detector: typing.Callable[[], bool] = lambda: not bool(
            os.getenv(Ansi.DISABLE, False)
        )

    def toString(self) -> str:
        self.__flushAttributes()
        return (
            self.__builder.getvalue()
            if isinstance(self.__builder, StringIO)
            else "".join(self.__builder)
        )

    def restorCursorPosition(self) -> Ansi:
        return self.restoreCursorPosition()

    def append2(self, c: str) -> Ansi:
        self.__builder.append(c)
        return self

    def append1(self, csq: str, start: int, end: int) -> Ansi:
        if isinstance(self.__builder, list):
            self.__builder.append(csq[start:end])
        elif isinstance(self.__builder, io.StringIO):
            self.__builder.write(csq[start:end])
        return self

    def append0(self, csq: str) -> Ansi:
        if isinstance(self.__builder, list):
            self.__builder.append(csq)
        elif isinstance(self.__builder, io.StringIO):
            self.__builder.write(csq)
        return self

    def render1(self, text: str, args: typing.List[typing.Any]) -> Ansi:
        self.a1(StringIO(AnsiRenderer.render0(text).format(*args)).getvalue())
        return self

    def render0(self, text: str) -> Ansi:
        self.a1(AnsiRenderer.render0(text))
        return self

    def apply(self, fun: Consumer) -> Ansi:
        fun.apply(self)
        return self

    def format_(self, pattern: str, args: typing.List[typing.Any]) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(pattern % tuple(args))
        return self

    def newline(self) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(os.linesep)
        elif isinstance(self.__builder, list):
            self.__builder.append(os.linesep)
        return self

    def a13(self, value: io.StringIO) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(value.getvalue())
        elif isinstance(self.__builder, list):
            self.__builder.append(value.getvalue())
        return self

    def a12(self, value: typing.Any) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a11(self, value: int) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a10(self, value: int) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a9(self, value: float) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a8(self, value: float) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a7(self, value: str) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(value)
        elif isinstance(self.__builder, list):
            self.__builder.append(value)
        return self

    def a6(self, value: str, start: int, end: int) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(value[start:end])
        elif isinstance(self.__builder, list):
            self.__builder.append(value[start:end])
        return self

    def a5(self, value: typing.List[str]) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write("".join(value))
        elif isinstance(self.__builder, list):
            self.__builder.extend(value)
        return self

    def a4(self, value: typing.List[str], offset: int, len_: int) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write("".join(value[offset : offset + len_]))
        elif isinstance(self.__builder, list):
            self.__builder.extend(value[offset : offset + len_])
        return self

    def a3(self, value: str) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(value)
        elif isinstance(self.__builder, list):
            self.__builder.append(value)
        return self

    def a2(self, value: bool) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(str(value))
        elif isinstance(self.__builder, list):
            self.__builder.append(str(value))
        return self

    def a1(self, value: str) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, StringIO):
            self.__builder.write(value)
        elif isinstance(self.__builder, list):
            self.__builder.append(value)
        return self

    def boldOff(self) -> Ansi:
        return self.a0(Attribute.INTENSITY_BOLD_OFF)

    def bold(self) -> Ansi:
        return self.a0(Attribute.INTENSITY_BOLD)

    def reset(self) -> Ansi:
        return self.a0(Attribute.RESET)

    def restoreCursorPositionDEC(self) -> Ansi:
        self.__builder.append(self.__FIRST_ESC_CHAR)
        self.__builder.append("8")
        return self

    def restoreCursorPositionSCO(self) -> Ansi:
        return self.__appendEscapeSequence0("u")

    def restoreCursorPosition(self) -> Ansi:
        self.restoreCursorPositionSCO()
        return self.restoreCursorPositionDEC()

    def saveCursorPositionDEC(self) -> Ansi:
        if isinstance(self.__builder, list):
            self.__builder.append(self.__FIRST_ESC_CHAR)
            self.__builder.append("7")
        elif isinstance(self.__builder, io.StringIO):
            self.__builder.write(self.__FIRST_ESC_CHAR)
            self.__builder.write("7")
        return self

    def saveCursorPositionSCO(self) -> Ansi:
        return self.__appendEscapeSequence0("s")

    def saveCursorPosition(self) -> Ansi:
        self.saveCursorPositionSCO()
        return self.saveCursorPositionDEC()

    def scrollDown(self, rows: int) -> Ansi:
        if rows == -2147483648:  # Equivalent to -2147483648 in Java
            return self.scrollUp(2147483647)  # Equivalent to 2147483647 in Java
        return (
            self.__appendEscapeSequence1("T", rows)
            if rows > 0
            else self.scrollUp(-rows) if rows < 0 else self
        )

    def scrollUp(self, rows: int) -> Ansi:
        if rows == -2147483648:  # Equivalent to -2147483648 in Java
            return self.scrollDown(2147483647)  # Equivalent to 2147483647 in Java
        return (
            self.__appendEscapeSequence1("S", rows)
            if rows > 0
            else self.scrollDown(-rows) if rows < 0 else self
        )

    def eraseLine1(self, kind: Erase) -> Ansi:
        return self.__appendEscapeSequence1("K", kind.value())

    def eraseLine0(self) -> Ansi:
        return self.__appendEscapeSequence0("K")

    def eraseScreen1(self, kind: Erase) -> Ansi:
        return self.__appendEscapeSequence1("J", kind.value())

    def eraseScreen0(self) -> Ansi:
        return self.__appendEscapeSequence1("J", Erase.ALL.value())

    def cursorUpLine1(self, n: int) -> Ansi:
        return (
            self.cursorDownLine1(-n) if n < 0 else self.__appendEscapeSequence1("F", n)
        )

    def cursorUpLine0(self) -> Ansi:
        return self.__appendEscapeSequence0("F")

    def cursorDownLine1(self, n: int) -> Ansi:
        return self.cursorUpLine1(-n) if n < 0 else self.__appendEscapeSequence1("E", n)

    def cursorDownLine0(self) -> Ansi:
        return self.__appendEscapeSequence0("E")

    def cursorMove(self, x: int, y: int) -> Ansi:
        return self.cursorRight(x).cursorDown(y)

    def cursorLeft(self, x: int) -> Ansi:
        return (
            self.__appendEscapeSequence1("D", x)
            if x > 0
            else self.cursorRight(-x) if x < 0 else self
        )

    def cursorRight(self, x: int) -> Ansi:
        return (
            self.__appendEscapeSequence1("C", x)
            if x > 0
            else self.cursorLeft(-x) if x < 0 else self
        )

    def cursorDown(self, y: int) -> Ansi:
        return (
            self.__appendEscapeSequence1("B", y)
            if y > 0
            else self.cursorUp(-y) if y < 0 else self
        )

    def cursorUp(self, y: int) -> Ansi:
        return (
            self.__appendEscapeSequence1("A", y)
            if y > 0
            else self.cursorDown(-y) if y < 0 else self
        )

    def cursorToColumn(self, x: int) -> Ansi:
        return self.__appendEscapeSequence1("G", max(1, x))

    def cursor(self, row: int, column: int) -> Ansi:
        return self.__appendEscapeSequence2("H", [max(1, row), max(1, column)])

    def a0(self, attribute: Attribute) -> Ansi:
        self.__attributeOptions.append(attribute.value())
        return self

    def bgBrightYellow(self) -> Ansi:
        return self.bgBright(Color.YELLOW)

    def bgBrightRed(self) -> Ansi:
        return self.bgBright(Color.RED)

    def bgBrightMagenta(self) -> Ansi:
        return self.bgBright(Color.MAGENTA)

    def bgBrightGreen(self) -> Ansi:
        return self.bgBright(Color.GREEN)

    def bgBrightDefault(self) -> Ansi:
        return self.bgBright(Color.DEFAULT)

    def bgBrightCyan(self) -> Ansi:
        return self.bgBright(Color.CYAN)

    def bgBright(self, color: Ansi.Color) -> Ansi:
        self.__attributeOptions.append(color.bgBright())
        return self

    def fgBrightYellow(self) -> Ansi:
        return self.fgBright(Color.YELLOW)

    def fgBrightRed(self) -> Ansi:
        return self.fgBright(Color.RED)

    def fgBrightMagenta(self) -> Ansi:
        return self.fgBright(Color.MAGENTA)

    def fgBrightGreen(self) -> Ansi:
        return self.fgBright(Color.GREEN)

    def fgBrightDefault(self) -> Ansi:
        return self.fgBright(Color.DEFAULT)

    def fgBrightCyan(self) -> Ansi:
        return self.fgBright(Color.CYAN)

    def fgBrightBlue(self) -> Ansi:
        return self.fgBright(Color.BLUE)

    def fgBrightBlack(self) -> Ansi:
        return self.fgBright(Color.BLACK)

    def fgBright(self, color: Ansi.Color) -> Ansi:
        self.__attributeOptions.append(color.fgBright())
        return self

    def bgYellow(self) -> Ansi:
        return self.bg0(Color.YELLOW)

    def bgRed(self) -> Ansi:
        return self.bg0(Color.RED)

    def bgMagenta(self) -> Ansi:
        return self.bg0(Color.MAGENTA)

    def bgGreen(self) -> Ansi:
        return self.bg0(Color.GREEN)

    def bgDefault(self) -> Ansi:
        return self.bg0(Color.DEFAULT)

    def bgCyan(self) -> Ansi:
        return self.bg0(Color.CYAN)

    def bgRgb1(self, r: int, g: int, b: int) -> Ansi:
        self.__attributeOptions.append(48)
        self.__attributeOptions.append(2)
        self.__attributeOptions.append(r & 0xFF)
        self.__attributeOptions.append(g & 0xFF)
        self.__attributeOptions.append(b & 0xFF)
        return self

    def bgRgb0(self, color: int) -> Ansi:
        return self.bgRgb1((color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF)

    def bg1(self, color: int) -> Ansi:
        self.__attributeOptions.append(48)
        self.__attributeOptions.append(5)
        self.__attributeOptions.append(color & 0xFF)
        return self

    def bg0(self, color: Ansi.Color) -> Ansi:
        self.__attributeOptions.append(color.bg())
        return self

    def fgYellow(self) -> Ansi:
        return self.fg0(Color.YELLOW)

    def fgRed(self) -> Ansi:
        return self.fg0(Color.RED)

    def fgMagenta(self) -> Ansi:
        return self.fg0(Color.MAGENTA)

    def fgGreen(self) -> Ansi:
        return self.fg0(Color.GREEN)

    def fgDefault(self) -> Ansi:
        return self.fg0(Color.DEFAULT)

    def fgCyan(self) -> Ansi:
        return self.fg0(Color.CYAN)

    def fgBlue(self) -> Ansi:
        return self.fg0(Color.BLUE)

    def fgBlack(self) -> Ansi:
        return self.fg0(Color.BLACK)

    def fgRgb1(self, r: int, g: int, b: int) -> Ansi:
        self.__attributeOptions.append(38)
        self.__attributeOptions.append(2)
        self.__attributeOptions.append(r & 0xFF)
        self.__attributeOptions.append(g & 0xFF)
        self.__attributeOptions.append(b & 0xFF)
        return self

    def fgRgb0(self, color: int) -> Ansi:
        return self.fgRgb1((color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF)

    def fg1(self, color: int) -> Ansi:
        self.__attributeOptions.append(38)
        self.__attributeOptions.append(5)
        self.__attributeOptions.append(color & 0xFF)
        return self

    def fg0(self, color: Ansi.Color) -> Ansi:
        self.__attributeOptions.append(color.fg())
        return self

    def __init__(
        self,
        constructorId: int,
        builder: typing.Union[typing.List[str], io.StringIO],
        parent: Ansi,
    ) -> None:
        self.__builder = builder
        self.__attributeOptions = []

        if constructorId == 1:
            self.__attributeOptions.extend(parent.__attributeOptions)

    @staticmethod
    def Ansi2(size: int) -> Ansi:
        return Ansi(0, StringIO(" " * size), None)

    @staticmethod
    def Ansi1(parent: Ansi) -> Ansi:
        return Ansi(1, io.StringIO(parent.__builder.getvalue()), parent)

    @staticmethod
    def Ansi0() -> Ansi:
        return Ansi(0, StringIO(), None)

    @staticmethod
    def ansi2(size: int) -> Ansi:
        if Ansi.isEnabled():
            return Ansi.Ansi2(size)
        else:
            return NoAnsi(size)

    @staticmethod
    def ansi1(builder: typing.Union[typing.List[str], io.StringIO]) -> Ansi:
        if Ansi.isEnabled():
            return Ansi(0, builder, None)
        else:
            return NoAnsi(builder)

    @staticmethod
    def ansi0() -> Ansi:
        if Ansi.isEnabled():
            return Ansi.Ansi0()
        else:
            return NoAnsi(None)

    @staticmethod
    def isEnabled() -> bool:
        return Ansi.__holder.get()

    @staticmethod
    def setEnabled(flag: bool) -> None:
        Ansi.__holder.set(flag)

    @staticmethod
    def isDetected() -> bool:
        try:
            return Ansi.__detector()
        except Exception:
            return True

    @staticmethod
    def setDetector(detector: typing.Callable[[], bool]) -> None:
        if detector is None:
            raise ValueError("detector cannot be None")
        Ansi.__detector = detector

    def ___appendEscapeSequence(
        self, command: str, options: typing.List[typing.Any]
    ) -> Ansi:
        if isinstance(self.__builder, io.StringIO):
            builder = self.__builder
        else:
            builder = io.StringIO()
            self.__builder = builder

        builder.write(self.__FIRST_ESC_CHAR)
        builder.write(self.__SECOND_ESC_CHAR)
        size = len(options)
        for i in range(size):
            if i != 0:
                builder.write(";")
            if options[i] is not None:
                builder.write(str(options[i]))
        builder.write(command)
        return self

    def __flushAttributes(self) -> None:
        if not self.__attributeOptions:
            return
        if len(self.__attributeOptions) == 1 and self.__attributeOptions[0] == 0:
            if isinstance(self.__builder, io.StringIO):
                self.__builder.write(self.__FIRST_ESC_CHAR)
                self.__builder.write(self.__SECOND_ESC_CHAR)
                self.__builder.write("m")
        else:
            self.___appendEscapeSequence("m", self.__attributeOptions)
        self.__attributeOptions.clear()

    def __appendEscapeSequence2(
        self, command: str, options: typing.List[typing.Any]
    ) -> Ansi:
        self.__flushAttributes()
        return self.___appendEscapeSequence(command, options)

    def __appendEscapeSequence1(self, command: str, option: int) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(self.__FIRST_ESC_CHAR)
            self.__builder.write(self.__SECOND_ESC_CHAR)
            self.__builder.write(str(option))
            self.__builder.write(command)
        elif isinstance(
            self.__builder, list
        ):  # Assuming __builder can also be a list of strings
            self.__builder.append(self.__FIRST_ESC_CHAR)
            self.__builder.append(self.__SECOND_ESC_CHAR)
            self.__builder.append(str(option))
            self.__builder.append(command)
        return self

    def __appendEscapeSequence0(self, command: str) -> Ansi:
        self.__flushAttributes()
        if isinstance(self.__builder, io.StringIO):
            self.__builder.write(self.__FIRST_ESC_CHAR)
            self.__builder.write(self.__SECOND_ESC_CHAR)
            self.__builder.write(command)
        elif isinstance(self.__builder, list):
            self.__builder.append(self.__FIRST_ESC_CHAR)
            self.__builder.append(self.__SECOND_ESC_CHAR)
            self.__builder.append(command)
        return self


class Consumer(ABC):

    def apply(self, ansi: Ansi) -> None:
        # Implementation goes here
        pass


class Color:

    DEFAULT: Ansi.Color = None
    WHITE: Ansi.Color = None
    CYAN: Ansi.Color = None
    MAGENTA: Ansi.Color = None
    BLUE: Ansi.Color = None
    YELLOW: Ansi.Color = None
    GREEN: Ansi.Color = None
    RED: Ansi.Color = None
    BLACK: Ansi.Color = None
    __name: str = ""

    __value: int = 0

    @staticmethod
    def initialize_fields() -> None:
        Color.DEFAULT: Ansi.Color = None
        Color.WHITE: Ansi.Color = None
        Color.CYAN: Ansi.Color = None
        Color.MAGENTA: Ansi.Color = None
        Color.BLUE: Ansi.Color = None
        Color.YELLOW: Ansi.Color = None
        Color.GREEN: Ansi.Color = None
        Color.RED: Ansi.Color = None
        Color.BLACK: Ansi.Color = None

    def toString(self) -> str:
        return self.__name

    def bgBright(self) -> int:
        return self.__value + 100

    def fgBright(self) -> int:
        return self.__value + 90

    def bg(self) -> int:
        return self.__value + 40

    def fg(self) -> int:
        return self.__value + 30

    def value(self) -> int:
        return self.__value

    def __init__(self, index: int, name: str) -> None:
        self.__value = index
        self.__name = name


class Erase:

    ALL: Erase = None

    BACKWARD: Erase = None

    FORWARD: Erase = None

    __name: str = ""

    __value: int = 0

    def toString(self) -> str:
        return self.__name

    def value(self) -> int:
        return self.__value

    def __init__(self, index: int, name: str) -> None:
        self.__value = index
        self.__name = name


class Attribute:

    STRIKETHROUGH_OFF: Attribute = None

    CONCEAL_OFF: Attribute = None

    NEGATIVE_OFF: Attribute = None

    BLINK_OFF: Attribute = None

    UNDERLINE_OFF: Attribute = None

    ITALIC_OFF: Attribute = None

    INTENSITY_BOLD_OFF: Attribute = None

    UNDERLINE_DOUBLE: Attribute = None

    STRIKETHROUGH_ON: Attribute = None

    CONCEAL_ON: Attribute = None

    NEGATIVE_ON: Attribute = None

    BLINK_FAST: Attribute = None

    BLINK_SLOW: Attribute = None

    UNDERLINE: Attribute = None

    ITALIC: Attribute = None

    INTENSITY_FAINT: Attribute = None

    INTENSITY_BOLD: Attribute = None

    RESET: Attribute = None

    __name: str = ""

    __value: int = 0

    def toString(self) -> str:
        return self.__name

    def value(self) -> int:
        return self.__value

    def __init__(self, index: int, name: str) -> None:
        self.__value = index
        self.__name = name


class NoAnsi(Ansi):

    def reset(self) -> Ansi:
        return self

    def restoreCursorPosition(self) -> Ansi:
        return self

    def restorCursorPosition(self) -> Ansi:
        return self

    def saveCursorPosition(self) -> Ansi:
        return self

    def scrollDown(self, rows: int) -> Ansi:
        return self

    def scrollUp(self, rows: int) -> Ansi:
        return self

    def cursorLeft(self, x: int) -> Ansi:
        return self

    def cursorDown(self, y: int) -> Ansi:
        return self

    def cursorRight(self, x: int) -> Ansi:
        return self

    def cursorUp(self, y: int) -> Ansi:
        return self

    def cursorToColumn(self, x: int) -> Ansi:
        return self

    def cursor(self, row: int, column: int) -> Ansi:
        return self

    def a0(self, attribute: Attribute) -> Ansi:
        return self

    def bgRgb1(self, r: int, g: int, b: int) -> Ansi:
        return self

    def fgRgb1(self, r: int, g: int, b: int) -> Ansi:
        return self

    def bgBright(self, color: Ansi.Color) -> Ansi:
        return self

    def fgBright(self, color: Ansi.Color) -> Ansi:
        return self

    def eraseLine1(self, kind: Erase) -> Ansi:
        return self

    def eraseLine0(self) -> Ansi:
        return self

    def eraseScreen1(self, kind: Erase) -> Ansi:
        return self

    def eraseScreen0(self) -> Ansi:
        return self

    def cursorUpLine1(self, n: int) -> Ansi:
        return self

    def cursorUpLine0(self) -> Ansi:
        return self

    def cursorDownLine1(self, n: int) -> Ansi:
        return self

    def cursorDownLine0(self) -> Ansi:
        return self

    def bg1(self, color: int) -> Ansi:
        return self

    def fg1(self, color: int) -> Ansi:
        return self

    def bg0(self, color: Ansi.Color) -> Ansi:
        return self

    def fg0(self, color: Ansi.Color) -> Ansi:
        return self

    def __init__(self, args: typing.Any) -> None:
        super().__init__(0, self.__determineStringBuilder(args), None)

    @staticmethod
    def __determineStringBuilder(args: typing.Any) -> typing.Union[io.StringIO]:
        if args is None:
            return io.StringIO()  # Equivalent to StringBuilder(80) in Java
        elif isinstance(args, int):
            return io.StringIO()  # Python's StringIO does not take an initial capacity
        elif isinstance(args, io.StringIO):
            return args
        else:
            raise ValueError("Invalid argument type")


Ansi.initialize_fields()

Color.initialize_fields()
