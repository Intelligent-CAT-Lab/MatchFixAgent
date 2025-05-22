from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class ExecuteStreamHandler(ABC):

    def stop(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def start(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    def setProcessOutputStream(
        self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        # Implementation would go here if provided in Java
        pass

    def setProcessInputStream(
        self, outputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        self.outputStream = outputStream

    def setProcessErrorStream(
        self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> None:
        self.process_error_stream = inputStream
