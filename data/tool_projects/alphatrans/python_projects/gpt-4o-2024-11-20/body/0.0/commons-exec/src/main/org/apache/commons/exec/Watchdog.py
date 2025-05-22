from __future__ import annotations
import time
import re
import io
import threading
import typing
from typing import *
import datetime
from src.main.org.apache.commons.exec.ThreadUtil import *
from src.main.org.apache.commons.exec.TimeoutObserver import *


class Watchdog:

    __threadFactory: threading.Thread = None

    __stopped: bool = False

    __timeoutMillis: int = 0

    __observers: typing.List[TimeoutObserver] = []

    def run(self) -> None:
        start_time_millis = int(datetime.datetime.now().timestamp() * 1000)
        is_waiting = False
        with threading.Condition() as condition:
            time_left_millis = self.__timeoutMillis - (
                int(datetime.datetime.now().timestamp() * 1000) - start_time_millis
            )
            is_waiting = time_left_millis > 0
            while not self.__stopped and is_waiting:
                try:
                    condition.wait(timeout=time_left_millis / 1000.0)
                except InterruptedError:
                    # ignore
                    pass
                time_left_millis = self.__timeoutMillis - (
                    int(datetime.datetime.now().timestamp() * 1000) - start_time_millis
                )
                is_waiting = time_left_millis > 0

        # Notify the listeners outside of the synchronized block
        if not is_waiting:
            self._fireTimeoutOccured()

    @staticmethod
    def Watchdog0(timeoutMillis: int) -> Watchdog:
        return Watchdog(None, datetime.timedelta(milliseconds=timeoutMillis))

    def stop(self) -> None:
        with threading.Lock():
            self.__stopped = True
            threading.Condition().notify_all()

    def start(self) -> None:
        self.__stopped = False
        ThreadUtil.newThread(
            self.__threadFactory, self, "CommonsExecWatchdog-", True
        ).start()

    def removeTimeoutObserver(self, to: TimeoutObserver) -> None:
        self.__observers.remove(to)

    def _fireTimeoutOccured(self) -> None:
        for observer in self.__observers:
            observer.timeoutOccured(self)

    def addTimeoutObserver(self, to: TimeoutObserver) -> None:
        self.__observers.append(to)

    @staticmethod
    def builder() -> Builder:
        return Builder()

    def __init__(
        self, threadFactory: threading.Thread, timeout: datetime.timedelta
    ) -> None:
        if timeout.total_seconds() <= 0:
            raise ValueError("timeout must not be less than 1.")
        self.__timeoutMillis = int(
            timeout.total_seconds() * 1000
        )  # Convert to milliseconds
        self.__threadFactory = threadFactory


class Builder:

    __timeout: datetime.timedelta = None

    __threadFactory: threading.Thread = None

    def get(self) -> Watchdog:
        return Watchdog(self.__threadFactory, self.__timeout)

    def setTimeout(self, timeout: datetime.timedelta) -> Builder:
        self.__timeout = timeout
        return self

    def setThreadFactory(self, threadFactory: threading.Thread) -> Builder:
        self.__threadFactory = threadFactory
        return self
