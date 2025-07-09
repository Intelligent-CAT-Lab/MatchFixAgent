from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
import os


class LogOutputStream(ABC):

    __charset: str = ""

    __level: int = 0

    __skip: bool = False

    __INTIAL_SIZE: int = 132
    __LF: int = 0x0A
    __CR: int = 0x0D

    def flush(self) -> None:
        if self.__buffer.size() > 0:
            self._processBuffer()

    def close(self) -> None:
        if self.__buffer.size() > 0:
            self._processBuffer()
        super().close()

    def write1(self, cc: int) -> None:
        c = cc.to_bytes(1, byteorder="big", signed=True)  # Convert int to byte
        c = c.decode(
            "latin1"
        )  # Decode byte to string using 'latin1' to match Java's behavior

        if c == "\n" or c == "\r":
            if not self.__skip:
                self._processBuffer()
        else:
            self.__buffer.write(cc)

        self.__skip = c == "\r"

    def write0(self, b: typing.List[int], off: int, len_: int) -> None:
        # Find the line breaks and pass other chars through in blocks
        offset = off
        block_start_offset = offset
        remaining = len_

        while remaining > 0:
            # Find the next line separator or end of buffer
            while remaining > 0 and b[offset] != self.__LF and b[offset] != self.__CR:
                offset += 1
                remaining -= 1

            # Either end of buffer or a line separator char
            block_length = offset - block_start_offset
            if block_length > 0:
                self.__buffer.write(
                    b[block_start_offset : block_start_offset + block_length]
                )

            # Process line separator characters
            while remaining > 0 and (b[offset] == self.__LF or b[offset] == self.__CR):
                self.write1(b[offset])
                offset += 1
                remaining -= 1

            block_start_offset = offset

    def _processLine0(self, line: str) -> None:
        self._processLine1(line, self.__level)

    def _processBuffer(self) -> None:
        self._processLine0(self.__buffer.toString(self.__charset))
        self.__buffer.reset()

    def getMessageLevel(self) -> int:
        return self.__level

    def __init__(self, constructorId: int, level: int, charset: str | None) -> None:
        if constructorId == 0:
            self.__level = 999
            self.__charset = None
        elif constructorId == 1:
            self.__level = level
            self.__charset = None
        else:
            self.__level = level
            self.__charset = (
                charset if charset is not None else os.device_encoding(0)
            )  # Default charset equivalent

    def _processLine1(self, line: str, logLevel: int) -> None:
        raise NotImplementedError("Subclasses must implement this method")


class ByteArrayOutputStreamX:

    def toString(self, charset: str) -> str:
        return str(self.buf[: self.count], charset)

    def __init__(self, size: int) -> None:
        super().__init__(size)
