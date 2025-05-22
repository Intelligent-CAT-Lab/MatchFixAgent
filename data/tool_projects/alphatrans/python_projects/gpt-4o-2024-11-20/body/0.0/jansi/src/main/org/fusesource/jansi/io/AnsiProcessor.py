from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os


class AnsiProcessor:

    _WHITE: int = 7
    _CYAN: int = 6
    _MAGENTA: int = 5
    _BLUE: int = 4
    _YELLOW: int = 3
    _GREEN: int = 2
    _RED: int = 1
    _BLACK: int = 0
    _ATTRIBUTE_CONCEAL_OFF: int = 28
    _ATTRIBUTE_NEGATIVE_OFF: int = 27
    _ATTRIBUTE_BLINK_OFF: int = 25
    _ATTRIBUTE_UNDERLINE_OFF: int = 24
    _ATTRIBUTE_INTENSITY_NORMAL: int = 22  # Intensity; Normal not bold and not faint
    _ATTRIBUTE_UNDERLINE_DOUBLE: int = 21
    _ATTRIBUTE_CONCEAL_ON: int = 8  # Conceal on
    _ATTRIBUTE_NEGATIVE_ON: int = 7
    _ATTRIBUTE_BLINK_FAST: int = 6
    _ATTRIBUTE_BLINK_SLOW: int = 5  # Blink; Slow less than 150 per minute
    _ATTRIBUTE_UNDERLINE: int = 4
    _ATTRIBUTE_ITALIC: int = 3
    _ATTRIBUTE_INTENSITY_FAINT: int = 2  # Intensity; Faint not widely supported
    _ATTRIBUTE_INTENSITY_BOLD: int = 1  # Intensity: Bold
    _ERASE_LINE: int = 2
    _ERASE_LINE_TO_BEGINING: int = 1
    _ERASE_LINE_TO_END: int = 0
    _ERASE_SCREEN: int = 2
    _ERASE_SCREEN_TO_BEGINING: int = 1
    _ERASE_SCREEN_TO_END: int = 0
    _os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None

    def _processCharsetSelect1(self, set_: int, seq: str) -> None:
        pass

    def _processUnknownOperatingSystemCommand(self, command: int, param: str) -> None:
        pass

    def _processChangeWindowTitle(self, label: str) -> None:
        pass

    def _processChangeIconName(self, label: str) -> None:
        pass

    def _processChangeIconNameAndWindowTitle(self, label: str) -> None:
        self._processChangeIconName(label)
        self._processChangeWindowTitle(label)

    def _processUnknownExtension(
        self, options: typing.List[typing.Any], command: int
    ) -> None:
        pass

    def _processCursorUp(self, count: int) -> None:
        pass

    def _processCursorDown(self, count: int) -> None:
        pass

    def _processCursorRight(self, count: int) -> None:
        # Poor man's implementation..
        for _ in range(count):
            self._os.write(b" ")

    def _processCursorLeft(self, count: int) -> None:
        pass

    def _processCursorDownLine(self, count: int) -> None:
        # Poor man's implementation
        for _ in range(count):
            self._os.write(b"\n")

    def _processCursorUpLine(self, count: int) -> None:
        pass

    def _processCursorToColumn(self, x: int) -> None:
        pass

    def _processCursorTo(self, row: int, col: int) -> None:
        pass

    def _processAttributeReset(self) -> None:
        pass

    def _processDefaultBackgroundColor(self) -> None:
        pass

    def _processDefaultTextColor(self) -> None:
        pass

    def _processSetBackgroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetBackgroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def _processSetBackgroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processSetBackgroundColor0(self, color: int) -> None:
        self._processSetBackgroundColor1(color, False)

    def _processSetForegroundColorExt1(self, r: int, g: int, b: int) -> None:
        pass

    def _processSetForegroundColorExt0(self, paletteIndex: int) -> None:
        pass

    def _processSetForegroundColor1(self, color: int, bright: bool) -> None:
        pass

    def _processSetForegroundColor0(self, color: int) -> None:
        self._processSetForegroundColor1(color, False)

    def _processSetAttribute(self, attribute: int) -> None:
        pass

    def _processEraseLine(self, eraseOption: int) -> None:
        pass

    def _processEraseScreen(self, eraseOption: int) -> None:
        pass

    def _processScrollUp(self, optionInt: int) -> None:
        pass

    def _processScrollDown(self, optionInt: int) -> None:
        pass

    def _processDeleteLine(self, optionInt: int) -> None:
        pass

    def _processInsertLine(self, optionInt: int) -> None:
        pass

    def _processSaveCursorPosition(self) -> None:
        # Placeholder for functionality to save the cursor position
        pass

    def _processRestoreCursorPosition(self) -> None:
        # This method is intentionally left empty, as in the Java code.
        pass

    def _processCharsetSelect0(self, options: typing.List[typing.Any]) -> bool:
        set_ = self.__optionInt0(options, 0)
        seq = options[1]
        if not isinstance(seq, str) or len(seq) != 1:
            raise ValueError("Second option must be a single character")
        self._processCharsetSelect1(set_, seq)
        return True

    def _processOperatingSystemCommand(self, options: typing.List[typing.Any]) -> bool:
        try:
            command = self.__optionInt0(options, 0)
            label = str(options[1])
            # For command > 2, label could be composed (i.e., contain ';'),
            # but we'll leave it to _processUnknownOperatingSystemCommand implementations to handle that
            if command == 0:
                self._processChangeIconNameAndWindowTitle(label)
                return True
            elif command == 1:
                self._processChangeIconName(label)
                return True
            elif command == 2:
                self._processChangeWindowTitle(label)
                return True
            else:
                # Not exactly unknown, but not supported through dedicated process methods:
                self._processUnknownOperatingSystemCommand(command, label)
                return True
        except (ValueError, IndexError, TypeError):
            pass
        return False

    def _processEscapeCommand(
        self, options: typing.List[typing.Any], command: int
    ) -> bool:
        try:
            if command == ord("A"):
                self._processCursorUp(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("B"):
                self._processCursorDown(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("C"):
                self._processCursorRight(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("D"):
                self._processCursorLeft(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("E"):
                self._processCursorDownLine(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("F"):
                self._processCursorUpLine(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("G"):
                self._processCursorToColumn(self.__optionInt0(options, 0))
                return True
            elif command in (ord("H"), ord("f")):
                self._processCursorTo(
                    self.__optionInt1(options, 0, 1), self.__optionInt1(options, 1, 1)
                )
                return True
            elif command == ord("J"):
                self._processEraseScreen(self.__optionInt1(options, 0, 0))
                return True
            elif command == ord("K"):
                self._processEraseLine(self.__optionInt1(options, 0, 0))
                return True
            elif command == ord("L"):
                self._processInsertLine(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("M"):
                self._processDeleteLine(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("S"):
                self._processScrollUp(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("T"):
                self._processScrollDown(self.__optionInt1(options, 0, 1))
                return True
            elif command == ord("m"):
                for next_option in options:
                    if next_option is not None and not isinstance(next_option, int):
                        raise ValueError("Invalid option type")

                count = 0
                options_iterator = iter(options)
                for next_option in options_iterator:
                    if next_option is not None:
                        count += 1
                        value = int(next_option)
                        if 30 <= value <= 37:
                            self._processSetForegroundColor0(value - 30)
                        elif 40 <= value <= 47:
                            self._processSetBackgroundColor0(value - 40)
                        elif 90 <= value <= 97:
                            self._processSetForegroundColor1(value - 90, True)
                        elif 100 <= value <= 107:
                            self._processSetBackgroundColor1(value - 100, True)
                        elif value in (38, 48):
                            arg2or5 = self._getNextOptionInt(options_iterator)
                            if arg2or5 == 2:
                                r = self._getNextOptionInt(options_iterator)
                                g = self._getNextOptionInt(options_iterator)
                                b = self._getNextOptionInt(options_iterator)
                                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                                    if value == 38:
                                        self._processSetForegroundColorExt1(r, g, b)
                                    else:
                                        self._processSetBackgroundColorExt1(r, g, b)
                                else:
                                    raise ValueError("Invalid RGB values")
                            elif arg2or5 == 5:
                                palette_index = self._getNextOptionInt(options_iterator)
                                if 0 <= palette_index <= 255:
                                    if value == 38:
                                        self._processSetForegroundColorExt0(
                                            palette_index
                                        )
                                    else:
                                        self._processSetBackgroundColorExt0(
                                            palette_index
                                        )
                                else:
                                    raise ValueError("Invalid palette index")
                            else:
                                raise ValueError("Invalid extended color argument")
                        else:
                            if value == 39:
                                self._processDefaultTextColor()
                            elif value == 49:
                                self._processDefaultBackgroundColor()
                            elif value == 0:
                                self._processAttributeReset()
                            else:
                                self._processSetAttribute(value)
                if count == 0:
                    self._processAttributeReset()
                return True
            elif command == ord("s"):
                self._processSaveCursorPosition()
                return True
            elif command == ord("u"):
                self._processRestoreCursorPosition()
                return True
            elif ord("a") <= command <= ord("z") or ord("A") <= command <= ord("Z"):
                self._processUnknownExtension(options, command)
                return True
            else:
                return False
        except ValueError:
            pass
        return False

    def _getNextOptionInt(self, optionsIterator: typing.Iterator[typing.Any]) -> int:
        while True:
            if not next(optionsIterator, None):
                raise ValueError("ValueError")
            arg = next(optionsIterator)
            if arg is not None:
                return int(arg)

    def __init__(
        self, os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        self._os = os

    def __optionInt1(
        self, options: typing.List[typing.Any], index: int, defaultValue: int
    ) -> int:
        if len(options) > index:
            value = options[index]
            if value is None:
                return defaultValue
            return int(value)
        return defaultValue

    def __optionInt0(self, options: typing.List[typing.Any], index: int) -> int:
        if len(options) <= index:
            raise ValueError("Index out of bounds")
        value = options[index]
        if value is None:
            raise ValueError("Value at index is None")
        if not isinstance(value, int):
            raise ValueError("Value at index is not an integer")
        return value
