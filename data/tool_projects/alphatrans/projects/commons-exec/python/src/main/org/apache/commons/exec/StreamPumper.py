from __future__ import annotations
import re
import threading
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.exec.util.DebugUtils import *


class StreamPumper:

    __closeWhenExhausted: bool = False

    __finished: bool = False

    __size: int = 0

    __os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None

    __is: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    __DEFAULT_SIZE: int = 1024

    def run(self) -> None:
        from threading import Lock

        lock = Lock()
        with lock:
            # Just in case this object is reused in the future
            self.__finished = False

        buf = bytearray(self.__size)

        try:
            while True:
                length = self.__is.readinto(buf)
                if length <= 0:
                    break
                self.__os.write(buf[:length])
        except Exception as ignored:
            # nothing to do - happens quite often with watchdog
            pass
        finally:
            if self.__closeWhenExhausted:
                try:
                    self.__os.close()
                except IOError as e:
                    msg = "Got exception while closing exhausted output stream"
                    DebugUtils.handleException(msg, e)
            with lock:
                self.__finished = True
                # Notify all threads waiting on this object
                from threading import Condition

                condition = Condition(lock)
                with condition:
                    condition.notify_all()

    def waitFor(self) -> None:
        while not self.isFinished():
            with self.__condition:
                self.__condition.wait()

    def isFinished(self) -> bool:
        return self.__finished

    def __init__(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        closeWhenExhausted: bool,
        size: int,
    ) -> None:
        self.__is = is_
        self.__os = os
        self.__size = size if size > 0 else self.__DEFAULT_SIZE
        self.__closeWhenExhausted = closeWhenExhausted

    @staticmethod
    def StreamPumper0(
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> StreamPumper:
        return StreamPumper(is_, os, False, -1)
