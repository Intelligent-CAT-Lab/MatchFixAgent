from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.ExecuteWatchdog import *
from src.main.org.apache.commons.exec.ProcessDestroyer import *


class Executor(ABC):

    INVALID_EXITVALUE: int = 0xDEADBEEF

    def setWorkingDirectory(self, dir_: pathlib.Path) -> None:
        self.working_directory = dir_

    def setWatchdog(self, watchDog: ExecuteWatchdog) -> None:
        self.watchDog = watchDog

    def setStreamHandler(self, streamHandler: ExecuteStreamHandler) -> None:
        self.streamHandler = streamHandler

    def setProcessDestroyer(self, processDestroyer: ProcessDestroyer) -> None:
        self.processDestroyer = processDestroyer

    def setExitValues(self, values: typing.List[int]) -> None:
        self.exit_values = values

    def setExitValue(self, value: int) -> None:
        self.exit_value = value

    def isFailure(self, exitValue: int) -> bool:
        return exitValue != 0

    def getWorkingDirectory(self) -> pathlib.Path:
        return pathlib.Path.cwd()

    def getWatchdog(self) -> ExecuteWatchdog:
        return self._watchdog

    def getStreamHandler(self) -> ExecuteStreamHandler:
        return ExecuteStreamHandler()

    def getProcessDestroyer(self) -> ProcessDestroyer:
        return self._process_destroyer

    def execute3(
        self,
        command: CommandLine,
        environment: typing.Dict[str, str],
        handler: ExecuteResultHandler,
    ) -> None:
        # The method does not return anything (void in Java -> None in Python)
        # The implementation would depend on the specific logic of the method.
        # Since the Java method is abstract (no body), we leave it as a placeholder.
        pass

    def execute2(self, command: CommandLine, environment: typing.Dict[str, str]) -> int:
        # Implementation would go here, but since the Java method is abstract,
        # we leave it as a placeholder in Python as well.
        pass

    def execute1(self, command: CommandLine, handler: ExecuteResultHandler) -> None:
        raise ExecuteException("Method not implemented")

    def execute0(self, command: CommandLine) -> int:
        raise NotImplementedError("This method needs to be implemented.")
