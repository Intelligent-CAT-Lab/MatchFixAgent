from __future__ import annotations
import time
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.io.ColorsAnsiProcessor import *


class AnsiOutputStream:

    RESET_CODE: typing.List[int] = [27, 91, 48, 109]
    __resetAtUninstall: bool = False

    __mode: AnsiMode = None

    __uninstaller: AnsiOutputStream.IoRunnable = None
    __installer: AnsiOutputStream.IoRunnable = None
    __colors: AnsiColors = None

    __type: AnsiType = None

    __processor: AnsiProcessor = None

    __width: AnsiOutputStream.WidthSupplier = None
    __cs: str = ""

    __options: typing.List[typing.Any] = []

    __startOfValue: int = 0

    __pos: int = 0
    __MAX_ESCAPE_SEQUENCE_LENGTH: int = 100
    __ap: AnsiProcessor = None

    __SECOND_CHARSET1_CHAR: int = ord(")")
    __SECOND_CHARSET0_CHAR: int = ord("(")
    __SECOND_ST_CHAR: int = ord("\\")
    __BEL: int = 7
    __SECOND_OSC_CHAR: int = ord("]")
    __SECOND_ESC_CHAR: int = ord("[")
    __FIRST_ESC_CHAR: int = 27
    __LOOKING_FOR_CHARSET: int = 9
    __LOOKING_FOR_ST: int = 8
    __LOOKING_FOR_OSC_PARAM: int = 7
    __LOOKING_FOR_OSC_COMMAND_END: int = 6
    __LOOKING_FOR_OSC_COMMAND: int = 5
    __LOOKING_FOR_INT_ARG_END: int = 4
    __LOOKING_FOR_STR_ARG_END: int = 3
    __LOOKING_FOR_NEXT_ARG: int = 2
    __LOOKING_FOR_SECOND_ESC_CHAR: int = 1
    __LOOKING_FOR_FIRST_ESC_CHAR: int = 0
    __state: int = __LOOKING_FOR_FIRST_ESC_CHAR

    @staticmethod
    def initialize_fields() -> None:
        AnsiOutputStream.__uninstaller: AnsiOutputStream.IoRunnable = None
        AnsiOutputStream.__installer: AnsiOutputStream.IoRunnable = None
        AnsiOutputStream.__width: AnsiOutputStream.WidthSupplier = None

    def close(self) -> None:
        self.uninstall()
        super().close()

    def write(self, data: int) -> None:
        if self.__state == self.__LOOKING_FOR_FIRST_ESC_CHAR:
            if data == self.__FIRST_ESC_CHAR:
                self.__buffer[self.__pos] = data
                self.__pos += 1
                self.__state = self.__LOOKING_FOR_SECOND_ESC_CHAR
            else:
                self._os.write(bytes([data]))

        elif self.__state == self.__LOOKING_FOR_SECOND_ESC_CHAR:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data == self.__SECOND_ESC_CHAR:
                self.__state = self.__LOOKING_FOR_NEXT_ARG
            elif data == self.__SECOND_OSC_CHAR:
                self.__state = self.__LOOKING_FOR_OSC_COMMAND
            elif data == self.__SECOND_CHARSET0_CHAR:
                self.__options.append(0)
                self.__state = self.__LOOKING_FOR_CHARSET
            elif data == self.__SECOND_CHARSET1_CHAR:
                self.__options.append(1)
                self.__state = self.__LOOKING_FOR_CHARSET
            else:
                self.__reset(False)

        elif self.__state == self.__LOOKING_FOR_NEXT_ARG:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data == ord('"'):
                self.__startOfValue = self.__pos - 1
                self.__state = self.__LOOKING_FOR_STR_ARG_END
            elif ord("0") <= data <= ord("9"):
                self.__startOfValue = self.__pos - 1
                self.__state = self.__LOOKING_FOR_INT_ARG_END
            elif data == ord(";"):
                self.__options.append(None)
            elif data == ord("?"):
                self.__options.append("?")
            elif data == ord("="):
                self.__options.append("=")
            else:
                self.__processEscapeCommand(data)

        elif self.__state == self.__LOOKING_FOR_INT_ARG_END:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if not (ord("0") <= data <= ord("9")):
                str_value = bytes(
                    self.__buffer[self.__startOfValue : self.__pos - 1]
                ).decode()
                value = int(str_value)
                self.__options.append(value)
                if data == ord(";"):
                    self.__state = self.__LOOKING_FOR_NEXT_ARG
                else:
                    self.__processEscapeCommand(data)

        elif self.__state == self.__LOOKING_FOR_STR_ARG_END:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data != ord('"'):
                value = bytes(
                    self.__buffer[self.__startOfValue : self.__pos - 1]
                ).decode(self.__cs)
                self.__options.append(value)
                if data == ord(";"):
                    self.__state = self.__LOOKING_FOR_NEXT_ARG
                else:
                    self.__processEscapeCommand(data)

        elif self.__state == self.__LOOKING_FOR_OSC_COMMAND:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if ord("0") <= data <= ord("9"):
                self.__startOfValue = self.__pos - 1
                self.__state = self.__LOOKING_FOR_OSC_COMMAND_END
            else:
                self.__reset(False)

        elif self.__state == self.__LOOKING_FOR_OSC_COMMAND_END:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data == ord(";"):
                str_value = bytes(
                    self.__buffer[self.__startOfValue : self.__pos - 1]
                ).decode()
                value = int(str_value)
                self.__options.append(value)
                self.__startOfValue = self.__pos
                self.__state = self.__LOOKING_FOR_OSC_PARAM
            elif ord("0") <= data <= ord("9"):
                pass  # Keep looking
            else:
                self.__reset(False)

        elif self.__state == self.__LOOKING_FOR_OSC_PARAM:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data == self.__BEL:
                value = bytes(
                    self.__buffer[self.__startOfValue : self.__pos - 1]
                ).decode(self.__cs)
                self.__options.append(value)
                self.__processOperatingSystemCommand()
            elif data == self.__FIRST_ESC_CHAR:
                self.__state = self.__LOOKING_FOR_ST
            else:
                pass  # Keep looking

        elif self.__state == self.__LOOKING_FOR_ST:
            self.__buffer[self.__pos] = data
            self.__pos += 1
            if data == self.__SECOND_ST_CHAR:
                value = bytes(
                    self.__buffer[self.__startOfValue : self.__pos - 2]
                ).decode(self.__cs)
                self.__options.append(value)
                self.__processOperatingSystemCommand()
            else:
                self.__state = self.__LOOKING_FOR_OSC_PARAM

        elif self.__state == self.__LOOKING_FOR_CHARSET:
            self.__options.append(chr(data))
            self.__processCharsetSelect()

        if self.__pos >= len(self.__buffer):
            self.__reset(False)

    def uninstall(self) -> None:
        if (
            self.__resetAtUninstall
            and self.__type != AnsiType.Redirected
            and self.__type != AnsiType.Unsupported
        ):
            self.setMode(AnsiMode.Default)
            self.write(bytes(self.RESET_CODE))
            self.flush()
        if self.__uninstaller is not None:
            self.__uninstaller.run()

    def install(self) -> None:
        if self.__installer is not None:
            self.__installer.run()

    def setResetAtUninstall(self, resetAtUninstall: bool) -> None:
        self.__resetAtUninstall = resetAtUninstall

    def isResetAtUninstall(self) -> bool:
        return self.__resetAtUninstall

    def setMode(self, mode: AnsiMode) -> None:
        self.__ap = (
            AnsiProcessor(self._os)
            if mode == AnsiMode.Strip
            else (
                ColorsAnsiProcessor(self._os, self.__colors)
                if mode == AnsiMode.Force or self.__processor is None
                else self.__processor
            )
        )
        self.__mode = mode

    def getMode(self) -> AnsiMode:
        return self.__mode

    def getColors(self) -> AnsiColors:
        return self.__colors

    def getType(self) -> AnsiType:
        return self.__type

    def getTerminalWidth(self) -> int:
        return self.__width.getTerminalWidth()

    def __init__(
        self,
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        width: AnsiOutputStream.WidthSupplier,
        mode: AnsiMode,
        processor: AnsiProcessor,
        type_: AnsiType,
        colors: AnsiColors,
        cs: str,
        installer: AnsiOutputStream.IoRunnable,
        uninstaller: AnsiOutputStream.IoRunnable,
        resetAtUninstall: bool,
    ) -> None:

        pass  # LLM could not translate this method

    def __reset(self, skipBuffer: bool) -> None:
        if not skipBuffer:
            self._os.write(bytes(self.__buffer[: self.__pos]))
        self.__pos = 0
        self.__startOfValue = 0
        self.__options.clear()
        self.__state = self.__LOOKING_FOR_FIRST_ESC_CHAR

    def __processEscapeCommand(self, data: int) -> None:
        try:
            self.__reset(
                self.__ap is not None
                and self.__ap._processEscapeCommand(self.__options, data)
            )
        except RuntimeError as e:
            self.__reset(True)
            raise e

    def __processOperatingSystemCommand(self) -> None:
        try:
            self.__reset(
                self.__ap is not None
                and self.__ap._processOperatingSystemCommand(self.__options)
            )
        except RuntimeError as e:
            self.__reset(True)
            raise e

    def __processCharsetSelect(self) -> None:
        try:
            self.__reset(
                self.__ap is not None
                and self.__ap._processCharsetSelect0(self.__options)
            )
        except RuntimeError as e:
            self.__reset(True)
            raise e


class WidthSupplier(ABC):

    def getTerminalWidth(self) -> int:
        pass


class ZeroWidthSupplier:

    def getTerminalWidth(self) -> int:
        return 0


class IoRunnable(ABC):

    def run(self) -> None:
        raise io.UnsupportedOperation("This method should be implemented by subclasses")


AnsiOutputStream.initialize_fields()
