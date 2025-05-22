from __future__ import annotations
import time
import re
import sys
from io import StringIO
import io
import threading
from io import BytesIO
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.exec.ExecuteException import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.InputStreamPumper import *
from src.main.org.apache.commons.exec.StreamPumper import *
from src.main.org.apache.commons.exec.ThreadUtil import *
from src.main.org.apache.commons.exec.util.DebugUtils import *


class PumpStreamHandler(ExecuteStreamHandler):

    __threadFactory: threading.Thread = None

    __caught: typing.Union[IOError, OSError] = None

    __stopTimeout: datetime.timedelta = datetime.timedelta(0)
    __inputStreamPumper: InputStreamPumper = None

    __inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    __errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None

    __outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None

    __inputThread: threading.Thread = None

    __errorThread: threading.Thread = None

    __outputThread: threading.Thread = None

    __STOP_TIMEOUT_ADDITION: datetime.timedelta = datetime.timedelta(seconds=2)

    def setStopTimeout1(self, timeout: int) -> None:
        self.__stopTimeout = datetime.timedelta(milliseconds=timeout)

    def setProcessOutputStream(
        self, is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        if self.__outputStream is not None:
            self._createProcessOutputPump(is_, self.__outputStream)

    def setProcessInputStream(
        self, os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        if self.__inputStream is not None:
            if self.__inputStream is sys.stdin:
                self.__inputThread = self.__createSystemInPump(self.__inputStream, os)
            else:
                self.__inputThread = self._createPump1(self.__inputStream, os, True)
        else:
            try:
                os.close()
            except IOError as e:
                msg = "Got exception while closing output stream"
                DebugUtils.handleException(msg, e)

    def setProcessErrorStream(
        self, is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        if self.__errorOutputStream is not None:
            self._createProcessErrorPump(is_, self.__errorOutputStream)

    def _stopThread(self, thread: threading.Thread, timeoutMillis: int) -> None:
        self.__stop1(thread, datetime.timedelta(milliseconds=timeoutMillis))

    def stop0(self) -> None:
        if self.__inputStreamPumper is not None:
            self.__inputStreamPumper.stopProcessing()

        self.__stop1(self.__outputThread, self.__stopTimeout)
        self.__stop1(self.__errorThread, self.__stopTimeout)
        self.__stop1(self.__inputThread, self.__stopTimeout)

        if (
            self.__errorOutputStream is not None
            and self.__errorOutputStream != self.__outputStream
        ):
            try:
                self.__errorOutputStream.flush()
            except IOError as e:
                msg = f"Got exception while flushing the error stream: {e}"
                DebugUtils.handleException(msg, e)

        if self.__outputStream is not None:
            try:
                self.__outputStream.flush()
            except IOError as e:
                msg = "Got exception while flushing the output stream"
                DebugUtils.handleException(msg, e)

        if self.__caught is not None:
            raise self.__caught

    def stop(self) -> None:
        self.stop0()

    def start0(self) -> None:
        self.__start1(self.__outputThread)
        self.__start1(self.__errorThread)
        self.__start1(self.__inputThread)

    def start(self) -> None:
        self.start0()

    def setStopTimeout0(self, timeout: datetime.timedelta) -> None:
        self.__stopTimeout = timeout if timeout is not None else datetime.timedelta(0)

    def _getOut(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        return self.__outputStream

    def _getErr(self) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]:
        return self.__errorOutputStream

    def _createPump1(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        closeWhenExhausted: bool,
    ) -> threading.Thread:
        return ThreadUtil.newThread(
            self.__threadFactory,
            StreamPumper(is_, os, closeWhenExhausted, -1),
            "CommonsExecStreamPumper-",
            True,
        )

    def _createPump0(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> threading.Thread:
        return self._createPump1(is_, os, isinstance(os, io.BytesIO))

    def _createProcessOutputPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        self.__outputThread = self._createPump0(is_, os)

    def _createProcessErrorPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        self.__errorThread = self._createPump0(is_, os)

    return PumpStreamHandler(
        threading.Thread, outputStream, errorOutputStream, inputStream
    )

    @staticmethod
    def PumpStreamHandler2(
        outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> PumpStreamHandler:
        return PumpStreamHandler.PumpStreamHandler3(
            outputStream, errorOutputStream, None
        )

    @staticmethod
    def PumpStreamHandler1(
        allOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> PumpStreamHandler:
        return PumpStreamHandler.PumpStreamHandler2(allOutputStream, allOutputStream)

    @staticmethod
    def PumpStreamHandler0() -> PumpStreamHandler:
        return PumpStreamHandler.PumpStreamHandler2(sys.stdout, sys.stderr)

    def __stop1(self, thread: threading.Thread, timeout: datetime.timedelta) -> None:
        if thread is not None:
            try:
                if timeout == datetime.timedelta(0):
                    thread.join()
                else:
                    time_to_wait = timeout + self.__STOP_TIMEOUT_ADDITION
                    start_time = datetime.datetime.now()
                    thread.join(time_to_wait.total_seconds())
                    if datetime.datetime.now() > start_time + time_to_wait:
                        self.__caught = ExecuteException(
                            f"The stop timeout of {timeout.total_seconds()} seconds was exceeded",
                            Executor.INVALID_EXITVALUE,
                            None,
                        )
            except InterruptedError:
                thread.interrupt()

    def __start1(self, thread: threading.Thread) -> None:
        if thread is not None:
            thread.start()

    def __createSystemInPump(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> threading.Thread:
        self.__inputStreamPumper = InputStreamPumper(is_, os)
        return ThreadUtil.newThread(
            self.__threadFactory,
            self.__inputStreamPumper,
            "CommonsExecStreamPumper-",
            True,
        )

    def __init__(
        self,
        threadFactory: threading.Thread,
        outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        errorOutputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> None:
        self.__threadFactory = threadFactory
        self.__outputStream = outputStream
        self.__errorOutputStream = errorOutputStream
        self.__inputStream = inputStream

    def getStopTimeout(self) -> datetime.timedelta:
        return self.__stopTimeout
