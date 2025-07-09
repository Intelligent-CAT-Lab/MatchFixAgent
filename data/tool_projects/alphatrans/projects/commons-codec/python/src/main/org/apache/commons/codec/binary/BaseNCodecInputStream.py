from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class BaseNCodecInputStream:

    __context: Context = Context()
    __buf: typing.List[int] = None

    __singleByte: typing.List[int] = [0]
    __doEncode: bool = False

    __baseNCodec: BaseNCodec = None

    def skip(self, n: int) -> int:
        if n < 0:
            raise ValueError(f"Negative skip length: {n}")

        b = [0] * 512  # Create a byte array of size 512
        todo = n

        while todo > 0:
            length = min(len(b), todo)
            length = self.read1(b, 0, length)
            if length == BaseNCodec.EOF:
                break
            todo -= length

        return n - todo

    def reset(self) -> None:
        raise IOError("mark/reset not supported")

    def markSupported(self) -> bool:
        return False  # not an easy job to support marks

    def mark(self, readLimit: int) -> None:
        pass

    def available(self) -> int:
        return 0 if self.__context.eof else 1

    def read1(self, array: typing.List[int], offset: int, len_: int) -> int:
        if array is None:
            raise ValueError("array cannot be None")
        if offset < 0 or len_ < 0:
            raise IndexError("offset or len_ cannot be negative")
        if offset > len(array) or offset + len_ > len(array):
            raise IndexError("offset + len_ exceeds array length")
        if len_ == 0:
            return 0

        read_len = 0

        while read_len < len_:
            if not self.__baseNCodec.hasData(self.__context):
                c = self.in_.read(self.__buf)
                if c == -1:  # EOF
                    return read_len if read_len != 0 else -1
                if self.__doEncode:
                    self.__baseNCodec.encode2(self.__buf, 0, c, self.__context)
                else:
                    self.__baseNCodec.decode1(self.__buf, 0, c, self.__context)

            read = self.__baseNCodec.readResults(
                array, offset + read_len, len_ - read_len, self.__context
            )
            if read < 0:
                return read_len if read_len != 0 else -1
            read_len += read

        return read_len

    def read0(self) -> int:
        r = self.read1(self.__singleByte, 0, 1)
        while r == 0:
            r = self.read1(self.__singleByte, 0, 1)
        if r > 0:
            b = self.__singleByte[0]
            return 256 + b if b < 0 else b
        return BaseNCodec.EOF

    def isStrictDecoding(self) -> bool:
        return self.__baseNCodec.isStrictDecoding()

    def __init__(
        self,
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        baseNCodec: BaseNCodec,
        doEncode: bool,
    ) -> None:
        super().__init__(input_)
        self.__doEncode = doEncode
        self.__baseNCodec = baseNCodec
        self.__buf = bytearray(4096 if doEncode else 8192)
