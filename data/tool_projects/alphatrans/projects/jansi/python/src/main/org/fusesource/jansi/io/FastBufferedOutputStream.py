from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class FastBufferedOutputStream:

    _count: int = 0

    _buf: typing.List[int] = [0] * 8192

    def flush(self) -> None:
        self.__flushBuffer()
        self.out.flush()

    def write1(self, b: typing.List[int], off: int, len_: int) -> None:
        if len_ >= len(self._buf):
            self.__flushBuffer()
            self.out.write(bytes(b[off : off + len_]))
            return
        if len_ > len(self._buf) - self._count:
            self.__flushBuffer()
        self._buf[self._count : self._count + len_] = b[off : off + len_]
        self._count += len_

    def write0(self, b: int) -> None:
        if self._count >= len(self._buf):
            self.__flushBuffer()
        self._buf[self._count] = (
            b & 0xFF
        )  # Ensure the value is within byte range (0-255)
        self._count += 1

    def __init__(
        self, out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> None:
        super().__init__(out)

    def __flushBuffer(self) -> None:
        if self._count > 0:
            self.out.write(bytes(self._buf[: self._count]))
            self._count = 0
