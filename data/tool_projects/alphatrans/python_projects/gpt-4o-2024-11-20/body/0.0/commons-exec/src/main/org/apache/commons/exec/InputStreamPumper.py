from __future__ import annotations
import time
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.exec.util.DebugUtils import *


class InputStreamPumper:

    SLEEPING_TIME: int = 100
    __stop: bool = False

    __os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter] = None

    __is: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    def run(self) -> None:
        try:
            while not self.__stop:
                while self.__is.readable() and self.__is.peek(1) and not self.__stop:
                    self.__os.write(self.__is.read(1))
                self.__os.flush()
                time.sleep(self.SLEEPING_TIME / 1000)  # Convert milliseconds to seconds
        except Exception as e:
            msg = "Got exception while reading/writing the stream"
            DebugUtils.handleException(msg, e)

    def stopProcessing(self) -> None:
        self.__stop = True

    def __init__(
        self,
        is_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        os: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> None:
        self.__is = is_
        self.__os = os
        self.__stop = False
