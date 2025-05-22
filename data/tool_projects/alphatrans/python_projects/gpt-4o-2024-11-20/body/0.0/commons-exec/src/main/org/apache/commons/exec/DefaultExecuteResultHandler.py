from __future__ import annotations
import time
import re
import io
import datetime
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteResultHandler import *
from src.main.org.apache.commons.exec.Executor import *


class DefaultExecuteResultHandler(ExecuteResultHandler):

    __exception: ExecuteException = None

    __exitValue: int = 0

    __hasResult: bool = False

    __SLEEP_TIME_MS: int = 50

    def waitFor2(self, timeoutMillis: int) -> None:
        untilMillis = datetime.datetime.now().timestamp() * 1000 + timeoutMillis
        while (
            not self.hasResult()
            and datetime.datetime.now().timestamp() * 1000 < untilMillis
        ):
            time.sleep(self.__SLEEP_TIME_MS / 1000)

    def onProcessFailed(self, e: ExecuteException) -> None:
        self.__exitValue = e.getExitValue()
        self.__exception = e
        self.__hasResult = True

    def onProcessComplete(self, exitValue: int) -> None:
        self.__exitValue = exitValue
        self.__exception = None
        self.__hasResult = True

    def waitFor1(self, timeout: datetime.timedelta) -> None:
        until = datetime.datetime.now() + timeout
        while not self.hasResult() and datetime.datetime.now() < until:
            time.sleep(self.__SLEEP_TIME_MS / 1000)

    def waitFor0(self) -> None:
        while not self.hasResult():
            time.sleep(self.__SLEEP_TIME_MS / 1000.0)

    def hasResult(self) -> bool:
        return self.__hasResult

    def getExitValue(self) -> int:
        if not self.__hasResult:
            raise RuntimeError(
                "The process has not exited yet therefore no result is available ..."
            )
        return self.__exitValue

    def getException(self) -> ExecuteException:
        if not self.__hasResult:
            raise RuntimeError(
                "The process has not exited yet therefore no result is available ..."
            )
        return self.__exception

    def __init__(self) -> None:
        self.__hasResult = False
        self.__exitValue = Executor.INVALID_EXITVALUE
