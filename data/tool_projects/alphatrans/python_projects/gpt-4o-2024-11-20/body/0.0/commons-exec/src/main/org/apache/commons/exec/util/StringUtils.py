from __future__ import annotations
import re
import os
from io import IOBase
from io import StringIO
import io
import typing
from typing import *


class StringUtils:

    __BACKSLASH_CHAR: str = "\\"
    __SLASH_CHAR: str = "/"
    __DOUBLE_QUOTE: str = '"'
    __SINGLE_QUOTE: str = "'"
    __EMPTY_STRING_ARRAY: List[str] = []

    @staticmethod
    def toString(strings: typing.List[str], separator: str) -> str:
        return separator.join(strings)

    @staticmethod
    def stringSubstitution(
        argStr: str, vars_: typing.Dict[str, typing.Any], isLenient: bool
    ) -> io.StringIO:
        argBuf = io.StringIO()

        if not argStr:
            return argBuf

        if not vars_:
            argBuf.write(argStr)
            return argBuf

        argStrLength = len(argStr)
        cIdx = 0

        while cIdx < argStrLength:
            ch = argStr[cIdx]
            del_ = " "

            if ch == "$":
                nameBuf = []
                del_ = argStr[cIdx + 1] if cIdx + 1 < argStrLength else None
                if del_ == "{":
                    cIdx += 1

                    cIdx += 1
                    while cIdx < argStrLength:
                        ch = argStr[cIdx]
                        if ch not in ("_", ".", "-", "+") and not ch.isalnum():
                            break
                        nameBuf.append(ch)
                        cIdx += 1

                    if nameBuf:
                        name = "".join(nameBuf)
                        temp = vars_.get(name)

                        if isinstance(temp, io.IOBase):  # Assuming File-like objects
                            value = StringUtils.fixFileSeparatorChar(temp.name)
                        else:
                            value = str(temp) if temp is not None else None

                        if value is not None:
                            argBuf.write(value)
                        else:
                            if not isLenient:
                                raise ValueError(f"No value found for : {name}")
                            argBuf.write(f"${{{name}}}")

                        del_ = argStr[cIdx] if cIdx < argStrLength else None

                        if del_ != "}":
                            raise ValueError(f"Delimiter not found for : {name}")
                        cIdx += 1  # Move past the closing '}'
                    else:
                        if not isLenient:
                            raise ValueError("Empty variable name in template")
                        argBuf.write("${}")
                else:
                    argBuf.write(ch)
                    cIdx += 1
            else:
                argBuf.write(ch)
                cIdx += 1

        argBuf.seek(0)
        return argBuf

    @staticmethod
    def split(input_: str, splitChar: str) -> List[str]:
        tokens = input_.split(splitChar)
        return tokens if tokens else StringUtils.__EMPTY_STRING_ARRAY

    @staticmethod
    def quoteArgument(argument: str) -> str:
        cleaned_argument = argument.strip()

        # Strip the quotes from both ends
        while cleaned_argument.startswith(
            StringUtils.__SINGLE_QUOTE
        ) or cleaned_argument.startswith(StringUtils.__DOUBLE_QUOTE):
            cleaned_argument = cleaned_argument[1:]

        while cleaned_argument.endswith(
            StringUtils.__SINGLE_QUOTE
        ) or cleaned_argument.endswith(StringUtils.__DOUBLE_QUOTE):
            cleaned_argument = cleaned_argument[:-1]

        if StringUtils.__DOUBLE_QUOTE in cleaned_argument:
            if StringUtils.__SINGLE_QUOTE in cleaned_argument:
                raise ValueError(
                    "Can't handle single and double quotes in same argument"
                )
            return f"{StringUtils.__SINGLE_QUOTE}{cleaned_argument}{StringUtils.__SINGLE_QUOTE}"

        if StringUtils.__SINGLE_QUOTE in cleaned_argument or " " in cleaned_argument:
            return f"{StringUtils.__DOUBLE_QUOTE}{cleaned_argument}{StringUtils.__DOUBLE_QUOTE}"

        return cleaned_argument

    @staticmethod
    def isQuoted(argument: str) -> bool:
        return (
            argument.startswith(StringUtils.__SINGLE_QUOTE)
            and argument.endswith(StringUtils.__SINGLE_QUOTE)
        ) or (
            argument.startswith(StringUtils.__DOUBLE_QUOTE)
            and argument.endswith(StringUtils.__DOUBLE_QUOTE)
        )

    @staticmethod
    def fixFileSeparatorChar(arg: str) -> str:
        return arg.replace(StringUtils.__SLASH_CHAR, os.sep).replace(
            StringUtils.__BACKSLASH_CHAR, os.sep
        )
