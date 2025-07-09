from __future__ import annotations
import copy
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.internal.Kernel32 import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.io.Colors import *


class WindowsAnsiProcessor(AnsiProcessor):

    __savedY: int = -1
    __savedX: int = -1
    __negative: bool = False

    __originalColors: int = 0

    __info: Kernel32.CONSOLE_SCREEN_BUFFER_INFO = (
        None  # LLM could not translate this field
    )

    __BACKGROUND_WHITE: int = None  # LLM could not translate this field

    __BACKGROUND_CYAN: int = None  # LLM could not translate this field

    __BACKGROUND_MAGENTA: int = None  # LLM could not translate this field

    __BACKGROUND_YELLOW: int = None  # LLM could not translate this field

    __BACKGROUND_BLACK: int = 0

    __FOREGROUND_WHITE: int = None  # LLM could not translate this field

    __FOREGROUND_CYAN: int = None  # LLM could not translate this field

    __FOREGROUND_MAGENTA: int = None  # LLM could not translate this field

    __FOREGROUND_YELLOW: int = None  # LLM could not translate this field

    __FOREGROUND_BLACK: int = 0
    __console: int = 0

    __ANSI_BACKGROUND_COLOR_MAP: typing.List[int] = (
        None  # LLM could not translate this field
    )

    __ANSI_FOREGROUND_COLOR_MAP: typing.List[int] = (
        None  # LLM could not translate this field
    )

    def _processChangeWindowTitle(self, label: str) -> None:
        Kernel32.SetConsoleTitle(label)

    def _processDeleteLine(self, optionInt: int) -> None:
        self.__getConsoleInfo()
        scroll = self.__info.window.copy()
        scroll.top = self.__info.cursorPosition.y
        org = COORD()
        org.x = 0
        org.y = self.__info.cursorPosition.y - optionInt
        char_info = CHAR_INFO()
        char_info.attributes = self.__originalColors
        char_info.unicodeChar = " "
        if (
            Kernel32.ScrollConsoleScreenBuffer(
                self.__console, scroll, scroll, org, char_info
            )
            == 0
        ):
            raise IOError(Kernel32.getLastErrorMessage())

    def _processInsertLine(self, optionInt: int) -> None:
        self.__getConsoleInfo()
        scroll = self.__info.window.copy()
        scroll.top = self.__info.cursorPosition.y
        org = COORD()
        org.x = 0
        org.y = self.__info.cursorPosition.y + optionInt
        char_info = CHAR_INFO()
        char_info.attributes = self.__originalColors
        char_info.unicodeChar = " "
        if (
            Kernel32.ScrollConsoleScreenBuffer(
                self.__console, scroll, scroll, org, char_info
            )
            == 0
        ):
            raise IOError(Kernel32.getLastErrorMessage())

    def _processRestoreCursorPosition(self) -> None:
        # restore only if there was a save operation first
        if self.__savedX != -1 and self.__savedY != -1:
            self._os.flush()
            self.__info.cursorPosition.x = self.__savedX
            self.__info.cursorPosition.y = self.__savedY
            self.__applyCursorPosition()

    def _processSaveCursorPosition(self) -> None:
        self.__getConsoleInfo()
        self.__savedX = self.__info.cursorPosition.x
        self.__savedY = self.__info.cursorPosition.y

    def _processSetAttribute(self, attribute: int) -> None:
        if attribute == self._ATTRIBUTE_INTENSITY_BOLD:
            self.__info.attributes = (
                self.__info.attributes | Kernel32.FOREGROUND_INTENSITY
            )
            self.__applyAttribute()
        elif attribute == self._ATTRIBUTE_INTENSITY_NORMAL:
            self.__info.attributes = (
                self.__info.attributes & ~Kernel32.FOREGROUND_INTENSITY
            )
            self.__applyAttribute()
        elif attribute == self._ATTRIBUTE_UNDERLINE:
            # Setting the background intensity as a substitute for underlining
            self.__info.attributes = (
                self.__info.attributes | Kernel32.BACKGROUND_INTENSITY
            )
            self.__applyAttribute()
        elif attribute == self._ATTRIBUTE_UNDERLINE_OFF:
            self.__info.attributes = (
                self.__info.attributes & ~Kernel32.BACKGROUND_INTENSITY
            )
            self.__applyAttribute()
        elif attribute == self._ATTRIBUTE_NEGATIVE_ON:
            self.__negative = True
            self.__applyAttribute()
        elif attribute == self._ATTRIBUTE_NEGATIVE_OFF:
            self.__negative = False
            self.__applyAttribute()
        else:
            pass

    def _processAttributeReset(self) -> None:
        self.__info.attributes = (
            self.__info.attributes & ~0x00FF
        ) | self.__originalColors
        self.__negative = False
        self.__applyAttribute()

    def _processDefaultBackgroundColor(self) -> None:
        self.__info.attributes = (self.__info.attributes & ~0x00F0) | (
            self.__originalColors & 0xF0
        )
        self.__info.attributes = self.__info.attributes & ~Kernel32.BACKGROUND_INTENSITY
        self.__applyAttribute()

    def _processDefaultTextColor(self) -> None:
        self.__info.attributes = (self.__info.attributes & ~0x000F) | (
            self.__originalColors & 0xF
        )
        self.__info.attributes = self.__info.attributes & ~Kernel32.FOREGROUND_INTENSITY
        self.__applyAttribute()

    def _processSetBackgroundColor1(self, color: int, bright: bool) -> None:
        self.__info.attributes = (
            self.__info.attributes & ~0x0070
        ) | self.__ANSI_BACKGROUND_COLOR_MAP[color]
        if bright:
            self.__info.attributes |= Kernel32.BACKGROUND_INTENSITY
        self.__applyAttribute()

    def _processSetForegroundColor1(self, color: int, bright: bool) -> None:
        self.__info.attributes = (
            self.__info.attributes & ~0x0007
        ) | self.__ANSI_FOREGROUND_COLOR_MAP[color]
        if bright:
            self.__info.attributes |= Kernel32.FOREGROUND_INTENSITY
        self.__applyAttribute()

    def _processCursorDownLine(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.x = 0
        self.__info.cursorPosition.y = max(
            self.__info.window.top, self.__info.cursorPosition.y + count
        )
        self.__applyCursorPosition()

    def _processCursorUpLine(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.x = 0
        self.__info.cursorPosition.y = max(
            self.__info.window.top, self.__info.cursorPosition.y - count
        )
        self.__applyCursorPosition()

    def _processCursorToColumn(self, x: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.x = max(0, min(self.__info.window.width(), x - 1))
        self.__applyCursorPosition()

    def _processCursorTo(self, row: int, col: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.y = max(
            self.__info.window.top,
            min(self.__info.size.y, self.__info.window.top + row - 1),
        )
        self.__info.cursorPosition.x = max(0, min(self.__info.window.width(), col - 1))
        self.__applyCursorPosition()

    def _processCursorUp(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.y = max(
            self.__info.window.top, self.__info.cursorPosition.y - count
        )
        self.__applyCursorPosition()

    def _processCursorDown(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.y = max(
            0, min(self.__info.size.y - 1, self.__info.cursorPosition.y + count)
        )
        self.__applyCursorPosition()

    def _processCursorRight(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.x = min(
            self.__info.window.width(), self.__info.cursorPosition.x + count
        )
        self.__applyCursorPosition()

    def _processCursorLeft(self, count: int) -> None:
        self.__getConsoleInfo()
        self.__info.cursorPosition.x = max(0, self.__info.cursorPosition.x - count)
        self.__applyCursorPosition()

    def _processEraseLine(self, eraseOption: int) -> None:
        self.__getConsoleInfo()
        written = [0]

        if eraseOption == self._ERASE_LINE:
            leftColCurrRow = self.__info.cursorPosition.copy()
            leftColCurrRow.x = 0
            Kernel32.FillConsoleOutputAttribute(
                self.__console,
                self.__info.attributes,
                self.__info.size.x,
                leftColCurrRow,
                written,
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console, " ", self.__info.size.x, leftColCurrRow, written
            )

        elif eraseOption == self._ERASE_LINE_TO_BEGINING:
            leftColCurrRow2 = self.__info.cursorPosition.copy()
            leftColCurrRow2.x = 0
            Kernel32.FillConsoleOutputAttribute(
                self.__console,
                self.__info.attributes,
                self.__info.cursorPosition.x,
                leftColCurrRow2,
                written,
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console,
                " ",
                self.__info.cursorPosition.x,
                leftColCurrRow2,
                written,
            )

        elif eraseOption == self._ERASE_LINE_TO_END:
            lengthToLastCol = self.__info.size.x - self.__info.cursorPosition.x
            Kernel32.FillConsoleOutputAttribute(
                self.__console,
                self.__info.attributes,
                lengthToLastCol,
                self.__info.cursorPosition.copy(),
                written,
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console,
                " ",
                lengthToLastCol,
                self.__info.cursorPosition.copy(),
                written,
            )

    def _processEraseScreen(self, eraseOption: int) -> None:
        self.__getConsoleInfo()
        written = [0]

        if eraseOption == self._ERASE_SCREEN:
            topLeft = COORD()
            topLeft.x = 0
            topLeft.y = self.__info.window.top
            screenLength = self.__info.window.height() * self.__info.size.x
            Kernel32.FillConsoleOutputAttribute(
                self.__console, self.__info.attributes, screenLength, topLeft, written
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console, " ", screenLength, topLeft, written
            )

        elif eraseOption == self._ERASE_SCREEN_TO_BEGINING:
            topLeft = COORD()
            topLeft.x = 0
            topLeft.y = self.__info.window.top
            lengthToCursor = (
                self.__info.cursorPosition.y - self.__info.window.top
            ) * self.__info.size.x + self.__info.cursorPosition.x
            Kernel32.FillConsoleOutputAttribute(
                self.__console, self.__info.attributes, lengthToCursor, topLeft, written
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console, " ", lengthToCursor, topLeft, written
            )

        elif eraseOption == self._ERASE_SCREEN_TO_END:
            lengthToEnd = (
                self.__info.window.bottom - self.__info.cursorPosition.y
            ) * self.__info.size.x + (self.__info.size.x - self.__info.cursorPosition.x)
            Kernel32.FillConsoleOutputAttribute(
                self.__console,
                self.__info.attributes,
                lengthToEnd,
                self.__info.cursorPosition.copy(),
                written,
            )
            Kernel32.FillConsoleOutputCharacterW(
                self.__console,
                " ",
                lengthToEnd,
                self.__info.cursorPosition.copy(),
                written,
            )

    def _processSetBackgroundColorExt1(self, r: int, g: int, b: int) -> None:
        round_color = Colors.roundRgbColor(r, g, b, 16)
        self._processSetBackgroundColor1(
            round_color - 8 if round_color >= 8 else round_color, round_color >= 8
        )

    def _processSetBackgroundColorExt0(self, paletteIndex: int) -> None:
        round_ = Colors.roundColor0(paletteIndex, 16)
        self._processSetBackgroundColor1(
            round_ - 8 if round_ >= 8 else round_, round_ >= 8
        )

    def _processSetForegroundColorExt1(self, r: int, g: int, b: int) -> None:
        round_color = Colors.roundRgbColor(r, g, b, 16)
        self._processSetForegroundColor1(
            round_color - 8 if round_color >= 8 else round_color, round_color >= 8
        )

    def _processSetForegroundColorExt0(self, paletteIndex: int) -> None:
        round_color = Colors.roundColor0(paletteIndex, 16)
        self._processSetForegroundColor1(
            round_color - 8 if round_color >= 8 else round_color, round_color >= 8
        )

    def WindowsAnsiProcessor1(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> WindowsAnsiProcessor:
        return self.WindowsAnsiProcessor0(ps, True)

    def WindowsAnsiProcessor0(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], stdout: bool
    ) -> WindowsAnsiProcessor:
        return WindowsAnsiProcessor(
            ps,
            Kernel32.GetStdHandle(
                Kernel32.STD_OUTPUT_HANDLE if stdout else Kernel32.STD_ERROR_HANDLE
            ),
        )

    def __init__(
        self, ps: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], console: int
    ) -> None:
        super().__init__(ps)
        self.__console = console
        self.__getConsoleInfo()
        self.__originalColors = self.__info.attributes

    def __applyCursorPosition(self) -> None:
        if (
            Kernel32.SetConsoleCursorPosition(
                self.__console, self.__info.cursorPosition.copy()
            )
            == 0
        ):
            raise IOError(COORD.getLastErrorMessage())

    def __invertAttributeColors(self, attributes: int) -> int:
        # Swap the Foreground and Background bits.
        fg = 0x000F & attributes
        fg <<= 4
        bg = 0x00F0 & attributes
        bg >>= 4
        attributes = (attributes & 0xFF00) | fg | bg
        return attributes

    def __applyAttribute(self) -> None:
        self._os.flush()
        attributes = self.__info.attributes
        if self.__negative:
            attributes = self.__invertAttributeColors(attributes)
        if Kernel32.SetConsoleTextAttribute(self.__console, attributes) == 0:
            raise IOError(Kernel32.getLastErrorMessage())

    def __getConsoleInfo(self) -> None:
        self._os.flush()
        if Kernel32.GetConsoleScreenBufferInfo(self.__console, self.__info) == 0:
            raise IOError(
                f"Could not get the screen info: {Kernel32.getLastErrorMessage()}"
            )
        if self.__negative:
            self.__info.attributes = self.__invertAttributeColors(
                self.__info.attributes
            )
