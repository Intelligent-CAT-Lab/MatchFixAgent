from __future__ import annotations
import time
import re
import io
import threading
import datetime
from src.main.org.apache.commons.exec.TimeoutObserver import *
from src.main.org.apache.commons.exec.Watchdog import *
from src.main.org.apache.commons.exec.util.DebugUtils import *


class ExecuteWatchdog(TimeoutObserver):

    INFINITE_TIMEOUT_DURATION: datetime.timedelta = datetime.timedelta(milliseconds=-1)
    INFINITE_TIMEOUT: int = -1
    __threadFactory: threading.Thread = None

    __processStarted: bool = False

    __watchdog: Watchdog = None

    __killedProcess: bool = False

    __caught: Exception = None

    __watch: bool = False

    __hasWatchdog: bool = False

    __process: subprocess.Popen = None

    def timeoutOccured(self, w: Watchdog) -> None:
        try:
            try:
                # We must check if the process was not stopped
                # before being here
                if self.__process is not None:
                    self.__process.wait(
                        timeout=0
                    )  # Check if the process has terminated
            except subprocess.TimeoutExpired:
                # The process is not terminated; if this is really
                # a timeout and not a manual stop, then destroy it.
                if self.__watch:
                    self.__killedProcess = True
                    self.__process.terminate()  # Destroy the process
            except Exception as itse:
                # Handle other exceptions related to process state
                if self.__watch:
                    self.__killedProcess = True
                    self.__process.terminate()
        except Exception as e:
            self.__caught = e
            DebugUtils.handleException(
                "Getting the exit value of the process failed", e
            )
        finally:
            self._cleanUp()

    @staticmethod
    def ExecuteWatchdog0(timeoutMillis: int) -> ExecuteWatchdog:
        return ExecuteWatchdog(
            threading.Thread, datetime.timedelta(milliseconds=timeoutMillis)
        )

    def stop(self) -> None:
        if self.__hasWatchdog:
            self.__watchdog.stop()
        self.__watch = False
        self.__process = None

    def start(self, processToMonitor: subprocess.Popen) -> None:
        if processToMonitor is None:
            raise ValueError("processToMonitor cannot be None")
        if self.__process is not None:
            raise RuntimeError("Already running.")
        self.__caught = None
        self.__killedProcess = False
        self.__watch = True
        self.__process = processToMonitor
        self.__processStarted = True
        with threading.Condition():
            threading.Condition().notify_all()
        if self.__hasWatchdog:
            self.__watchdog.start()

    def killedProcess(self) -> bool:
        return self.__killedProcess

    def isWatching(self) -> bool:
        self.__ensureStarted()
        return self.__watch

    def failedToStart(self, e: Exception) -> None:
        self.__processStarted = True
        self.__caught = e
        with threading.Condition():
            threading.Condition().notify_all()

    def destroyProcess(self) -> None:
        self.__ensureStarted()
        self.timeoutOccured(None)
        self.stop()

    def _cleanUp(self) -> None:
        self.__watch = False
        self.__process = None

    def checkException(self) -> None:
        if self.__caught is not None:
            raise self.__caught

    @staticmethod
    def builder() -> Builder:
        return Builder()

    def __ensureStarted(self) -> None:
        while not self.__processStarted and self.__caught is None:
            try:
                with threading.Condition():
                    threading.Condition().wait()
            except InterruptedError as e:
                raise RuntimeError(str(e)) from e

    def __init__(
        self, threadFactory: threading.Thread, timeout: datetime.timedelta
    ) -> None:
        self.__killedProcess = False
        self.__watch = False
        self.__hasWatchdog = timeout != self.INFINITE_TIMEOUT_DURATION
        self.__processStarted = False
        self.__threadFactory = (
            threadFactory if threadFactory is not None else threading.Thread
        )
        if self.__hasWatchdog:
            self.__watchdog = (
                Watchdog.builder()
                .setThreadFactory(self.__threadFactory)
                .setTimeout(timeout)
                .get()
            )
            self.__watchdog.addTimeoutObserver(self)
        else:
            self.__watchdog = None

    def setProcessNotStarted(self) -> None:
        self.__processStarted = False


class Builder:

    __timeout: datetime.timedelta = None

    __threadFactory: threading.Thread = None

    def get(self) -> ExecuteWatchdog:
        return ExecuteWatchdog(self.__threadFactory, self.__timeout)

    def setTimeout(self, timeout: datetime.timedelta) -> Builder:
        self.__timeout = timeout
        return self

    def setThreadFactory(self, threadFactory: threading.Thread) -> Builder:
        self.__threadFactory = threadFactory
        return self
