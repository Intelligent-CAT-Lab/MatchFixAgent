from __future__ import annotations
import copy
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.util.StringUtils import *


class CommandLine:

    __isFile: bool = False

    __substitutionMap: typing.Dict[str, typing.Any] = None

    __executable: str = ""

    __arguments: typing.List[Argument] = []

    def toString(self) -> str:
        return "[" + ", ".join(self.toStrings()) + "]"

    def toStrings(self) -> List[str]:
        result = [None] * (len(self.__arguments) + 1)
        result[0] = self.getExecutable()
        result[1:] = self.getArguments()
        return result

    def setSubstitutionMap(self, substitutionMap: typing.Dict[str, typing.Any]) -> None:
        self.__substitutionMap = substitutionMap

    def isFile(self) -> bool:
        return self.__isFile

    def getSubstitutionMap(self) -> typing.Dict[str, typing.Any]:
        return self.__substitutionMap

    def getExecutable(self) -> str:
        return StringUtils.fixFileSeparatorChar(
            self.__expandArgument(self.__executable)
        )

    def getArguments(self) -> List[str]:
        result = [None] * len(self.__arguments)

        for i in range(len(result)):
            curr_argument = self.__arguments[i]
            expanded_argument = self.__expandArgument(
                curr_argument._Argument__getValue()
            )
            result[i] = (
                StringUtils.quoteArgument(expanded_argument)
                if curr_argument._Argument__isHandleQuoting()
                else expanded_argument
            )

        return result

    def addArguments3(
        self, addArguments: Optional[List[str]], handleQuoting: bool
    ) -> CommandLine:
        if addArguments is not None:
            for addArgument in addArguments:
                self.addArgument1(addArgument, handleQuoting)
        return self

    def addArguments2(self, addArguments: Optional[List[str]]) -> CommandLine:
        return self.addArguments3(addArguments, True)

    def addArguments1(self, addArguments: str, handleQuoting: bool) -> CommandLine:
        if addArguments is not None:
            argumentsArray = self.__translateCommandline(addArguments)
            self.addArguments3(argumentsArray, handleQuoting)
        return self

    def addArguments0(self, addArguments: str) -> CommandLine:
        return self.addArguments1(addArguments, True)

    def addArgument1(self, argument: str, handleQuoting: bool) -> CommandLine:
        if argument is None:
            return self

        # Check if we can really quote the argument - if not, raise an exception
        if handleQuoting:
            argument = StringUtils.quoteArgument(argument)

        self.__arguments.append(Argument(argument, handleQuoting))
        return self

    def addArgument0(self, argument: str) -> CommandLine:
        return self.addArgument1(argument, True)

    def __init__(
        self,
        constructorId: int,
        other: CommandLine = None,
        executable: pathlib.Path = None,
        executableString: str = None,
    ) -> None:
        if constructorId == 0:
            if other is None:
                raise ValueError(
                    "Parameter 'other' must not be None for constructorId 0"
                )
            self.__executable = other.getExecutable()
            self.__isFile = other.isFile()
            self.__arguments = (
                other._CommandLine__arguments.copy()
            )  # Copy the list of arguments

            if other.getSubstitutionMap() is not None:
                self.__substitutionMap = (
                    other.getSubstitutionMap().copy()
                )  # Create a copy of the substitution map

        elif constructorId == 1:
            if executable is None:
                raise ValueError(
                    "Parameter 'executable' must not be None for constructorId 1"
                )
            self.__isFile = True
            self.__executable = self.__toCleanExecutable(str(executable.absolute()))

        else:  # constructorId == 2
            if executableString is None:
                raise ValueError(
                    "Parameter 'executableString' must not be None for constructorId 2"
                )
            self.__isFile = False
            self.__executable = self.__toCleanExecutable(executableString)

    @staticmethod
    def parse1(line: str, substitutionMap: typing.Dict[str, typing.Any]) -> CommandLine:
        if line is None:
            raise ValueError("Command line can not be null")
        if line.strip() == "":
            raise ValueError("Command line can not be empty")

        tmp = CommandLine.__translateCommandline(line)

        cl = CommandLine(2, None, None, tmp[0])
        cl.setSubstitutionMap(substitutionMap)
        for i in range(1, len(tmp)):
            cl.addArgument0(tmp[i])

        return cl

    @staticmethod
    def parse0(line: str) -> CommandLine:
        return CommandLine.parse1(line, None)

    def __toCleanExecutable(self, dirtyExecutable: str) -> str:
        if dirtyExecutable is None:
            raise ValueError("dirtyExecutable")
        if dirtyExecutable.strip() == "":
            raise ValueError("Executable can not be empty")
        return StringUtils.fixFileSeparatorChar(dirtyExecutable)

    def __expandArgument(self, argument: str) -> str:
        string_buffer = StringUtils.stringSubstitution(
            argument, self.getSubstitutionMap(), True
        )
        return string_buffer.getvalue()

    @staticmethod
    def __translateCommandline(toProcess: str) -> List[str]:
        if toProcess is None or toProcess.strip() == "":
            # no command? no string
            return []

        # parse with a simple finite state machine.

        normal = 0
        inQuote = 1
        inDoubleQuote = 2
        state = normal
        tokens = iter(toProcess)  # Use an iterator to process the string
        list_ = []
        current = []
        lastTokenHasBeenQuoted = False

        for char in toProcess:
            if state == inQuote:
                if char == "'":
                    lastTokenHasBeenQuoted = True
                    state = normal
                else:
                    current.append(char)
            elif state == inDoubleQuote:
                if char == '"':
                    lastTokenHasBeenQuoted = True
                    state = normal
                else:
                    current.append(char)
            else:  # state == normal
                if char == "'":
                    state = inQuote
                elif char == '"':
                    state = inDoubleQuote
                elif char.isspace():
                    if lastTokenHasBeenQuoted or current:
                        list_.append("".join(current))
                        current = []
                else:
                    current.append(char)
                lastTokenHasBeenQuoted = False

        if lastTokenHasBeenQuoted or current:
            list_.append("".join(current))

        if state == inQuote or state == inDoubleQuote:
            raise ValueError(f"Unbalanced quotes in {toProcess}")

        return list_


class Argument:

    __handleQuoting: bool = False

    __value: str = ""

    def __isHandleQuoting(self) -> bool:
        return self.__handleQuoting

    def __getValue(self) -> str:
        return self.__value

    def __init__(self, value: str, handleQuoting: bool) -> None:
        self.__value = value.strip()
        self.__handleQuoting = handleQuoting
