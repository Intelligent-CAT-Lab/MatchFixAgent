from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.fusesource.jansi.AnsiColors import *
from src.main.org.fusesource.jansi.io.AnsiProcessor import *
from src.main.org.fusesource.jansi.io.Colors import *


class ColorsAnsiProcessor(AnsiProcessor):

    __colors: AnsiColors = None

    def _processCharsetSelect0(self, options: typing.List[typing.Any]) -> bool:
        return False

    def _processOperatingSystemCommand(self, options: typing.List[typing.Any]) -> bool:
        return False

    def _processEscapeCommand(
        self, options: typing.List[typing.Any], command: int
    ) -> bool:
        if command == ord("m") and (
            self.__colors == AnsiColors.Colors256
            or self.__colors == AnsiColors.Colors16
        ):
            # Validate all options are ints...
            has38or48 = False
            for next_option in options:
                if next_option is not None and not isinstance(next_option, int):
                    raise ValueError("Invalid option type, expected int")
                value = int(next_option)
                has38or48 |= value == 38 or value == 48

            # SGR commands do not contain an extended color, so just transfer the buffer
            if not has38or48:
                return False

            sb = []
            sb.append("\033[")
            first = True
            options_iterator = iter(options)

            while True:
                try:
                    next_option = next(options_iterator)
                except StopIteration:
                    break

                if next_option is not None:
                    value = int(next_option)
                    if value == 38 or value == 48:
                        # extended color like `esc[38;5;<index>m` or `esc[38;2;<r>;<g>;<b>m`
                        arg2or5 = self._getNextOptionInt(options_iterator)
                        if arg2or5 == 2:
                            # 24-bit color style like `esc[38;2;<r>;<g>;<b>m`
                            r = self._getNextOptionInt(options_iterator)
                            g = self._getNextOptionInt(options_iterator)
                            b = self._getNextOptionInt(options_iterator)
                            if self.__colors == AnsiColors.Colors256:
                                col = Colors.roundRgbColor(r, g, b, 256)
                                if not first:
                                    sb.append(";")
                                first = False
                                sb.append(f"{value};5;{col}")
                            else:
                                col = Colors.roundRgbColor(r, g, b, 16)
                                if not first:
                                    sb.append(";")
                                first = False
                                sb.append(
                                    f"{90 + col - 8 if col >= 8 else 30 + col}"
                                    if value == 38
                                    else f"{100 + col - 8 if col >= 8 else 40 + col}"
                                )
                        elif arg2or5 == 5:
                            # 256 color style like `esc[38;5;<index>m`
                            palette_index = self._getNextOptionInt(options_iterator)
                            if self.__colors == AnsiColors.Colors256:
                                if not first:
                                    sb.append(";")
                                first = False
                                sb.append(f"{value};5;{palette_index}")
                            else:
                                col = Colors.roundColor0(palette_index, 16)
                                if not first:
                                    sb.append(";")
                                first = False
                                sb.append(
                                    f"{90 + col - 8 if col >= 8 else 30 + col}"
                                    if value == 38
                                    else f"{100 + col - 8 if col >= 8 else 40 + col}"
                                )
                        else:
                            raise ValueError("Invalid argument for extended color")
                    else:
                        if not first:
                            sb.append(";")
                        first = False
                        sb.append(str(value))

            sb.append("m")
            os.write("".join(sb).encode())
            return True
        else:
            return False

    def __init__(
        self,
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        colors: AnsiColors,
    ) -> None:
        super().__init__(os)
        self.__colors = colors
