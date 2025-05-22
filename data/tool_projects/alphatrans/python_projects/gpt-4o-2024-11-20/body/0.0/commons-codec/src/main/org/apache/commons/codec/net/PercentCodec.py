from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.Utils import *


class PercentCodec(BinaryDecoder, BinaryEncoder):

    __alwaysEncodeCharsMax: int = -2147483648
    __alwaysEncodeCharsMin: int = 2147483647
    __plusForSpace: bool = False

    __alwaysEncodeChars: typing.List[bool] = [False] * 256
    __ESCAPE_CHAR: int = ord("%")

    def decode1(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, (bytes, bytearray)):
            return self.decode0(list(obj))
        raise DecoderException(
            f"Objects of type {type(obj).__name__} cannot be Percent decoded", None
        )

    def encode1(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, (bytes, bytearray)):
            return self.encode0(obj)
        raise EncoderException(
            f"Objects of type {type(obj).__name__} cannot be Percent encoded", None
        )

    def decode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None

        buffer = bytearray(self.__expectedDecodingBytes(bytes_))
        i = 0
        while i < len(bytes_):
            b = bytes_[i]
            if b == self.__ESCAPE_CHAR:
                try:
                    i += 1
                    u = Utils.digit16(bytes_[i])
                    i += 1
                    l = Utils.digit16(bytes_[i])
                    buffer.append((u << 4) + l)
                except IndexError as e:
                    raise DecoderException("Invalid percent decoding: ", e)
            elif self.__plusForSpace and b == ord("+"):
                buffer.append(ord(" "))
            else:
                buffer.append(b)
            i += 1

        return list(buffer)

    def encode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        if bytes_ is None:
            return None

        expected_encoding_bytes = self.__expectedEncodingBytes(bytes_)
        will_encode = expected_encoding_bytes != len(bytes_)
        if will_encode or (self.__plusForSpace and self.__containsSpace(bytes_)):
            return self.__doEncode(bytes_, expected_encoding_bytes, will_encode)
        return bytes_

    def __init__(
        self,
        constructorId: int,
        plusForSpace: bool,
        alwaysEncodeChars: typing.List[int],
    ) -> None:
        if constructorId == 0:
            self.__plusForSpace = plusForSpace
            self.__insertAlwaysEncodeChars(alwaysEncodeChars)
        else:
            self.__plusForSpace = False
            self.__insertAlwaysEncodeChar(self.__ESCAPE_CHAR)

    def __expectedDecodingBytes(self, bytes_: typing.List[int]) -> int:
        byte_count = 0
        i = 0
        while i < len(bytes_):
            b = bytes_[i]
            i += 3 if b == self.__ESCAPE_CHAR else 1
            byte_count += 1
        return byte_count

    def __isAsciiChar(self, c: int) -> bool:
        return c >= 0

    def __inAlwaysEncodeCharsRange(self, c: int) -> bool:
        return self.__alwaysEncodeCharsMin <= c <= self.__alwaysEncodeCharsMax

    def __canEncode(self, c: int) -> bool:
        return not self.__isAsciiChar(c) or (
            self.__inAlwaysEncodeCharsRange(c) and self.__alwaysEncodeChars[c]
        )

    def __containsSpace(self, bytes_: typing.List[int]) -> bool:
        for b in bytes_:
            if b == ord(" "):  # Compare with the ASCII value of space
                return True
        return False

    def __expectedEncodingBytes(self, bytes_: typing.List[int]) -> int:
        byte_count = 0
        for b in bytes_:
            byte_count += 3 if self.__canEncode(b) else 1
        return byte_count

    def __doEncode(
        self, bytes_: typing.List[int], expectedLength: int, willEncode: bool
    ) -> typing.List[int]:
        buffer = bytearray(expectedLength)
        buffer_index = 0

        for b in bytes_:
            if willEncode and self.__canEncode(b):
                bb = b
                if bb < 0:
                    bb = 256 + bb
                hex1 = Utils.hexDigit(bb >> 4)
                hex2 = Utils.hexDigit(bb)
                buffer[buffer_index] = self.__ESCAPE_CHAR
                buffer_index += 1
                buffer[buffer_index] = ord(hex1)
                buffer_index += 1
                buffer[buffer_index] = ord(hex2)
                buffer_index += 1
            elif self.__plusForSpace and b == ord(" "):
                buffer[buffer_index] = ord("+")
                buffer_index += 1
            else:
                buffer[buffer_index] = b
                buffer_index += 1

        return list(buffer[:buffer_index])

    def __insertAlwaysEncodeChar(self, b: int) -> None:
        self.__alwaysEncodeChars[b] = True
        if b < self.__alwaysEncodeCharsMin:
            self.__alwaysEncodeCharsMin = b
        if b > self.__alwaysEncodeCharsMax:
            self.__alwaysEncodeCharsMax = b

    def __insertAlwaysEncodeChars(
        self, alwaysEncodeCharsArray: typing.List[int]
    ) -> None:
        if alwaysEncodeCharsArray is not None:
            for b in alwaysEncodeCharsArray:
                self.__insertAlwaysEncodeChar(b)
        self.__insertAlwaysEncodeChar(self.__ESCAPE_CHAR)
