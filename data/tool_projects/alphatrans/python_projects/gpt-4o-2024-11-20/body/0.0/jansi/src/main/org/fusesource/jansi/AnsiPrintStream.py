from __future__ import annotations
import re
import sys
import io
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.AnsiMode import *
from src.main.org.fusesource.jansi.AnsiType import *
from src.main.org.fusesource.jansi.io.AnsiOutputStream import *


class AnsiPrintStream:

    def toString(self) -> str:
        return (
            f"AnsiPrintStream{{"
            f"type={self.getType()}, "
            f"colors={self.getColors()}, "
            f"mode={self.getMode()}, "
            f"resetAtUninstall={self.isResetAtUninstall()}"
            f"}}"
        )

    def uninstall(self) -> None:
        # If the system output stream has been closed, out should be None, so avoid an AttributeError
        out = self._getOut()
        if out is not None:
            out.uninstall()

    def install(self) -> None:
        self._getOut().install()

    def getTerminalWidth(self) -> int:
        return self._getOut().getTerminalWidth()

    def setResetAtUninstall(self, resetAtClose: bool) -> None:
        self._getOut().setResetAtUninstall(resetAtClose)

    def isResetAtUninstall(self) -> bool:
        return self._getOut().isResetAtUninstall()

    def setMode(self, ansiMode: AnsiMode) -> None:
        self._getOut().setMode(ansiMode)

    def getMode(self) -> AnsiMode:
        return self._getOut().getMode()

    def getColors(self) -> AnsiColors:
        return self._getOut().getColors()

    def getType(self) -> AnsiType:
        return self._getOut().getType()

    def _getOut(self) -> AnsiOutputStream:
        return self.out

    def __init__(
        self, out: AnsiOutputStream, autoFlush: bool, args: typing.Any
    ) -> None:
        super().__init__(out, autoFlush, self.__determineEncoding(args))

    @staticmethod
    def __determineEncoding(args: typing.Any) -> str:
        if args is None:
            return None  # Use default encoding
        elif isinstance(args, str):
            return args
        else:
            raise ValueError("Invalid argument type")
