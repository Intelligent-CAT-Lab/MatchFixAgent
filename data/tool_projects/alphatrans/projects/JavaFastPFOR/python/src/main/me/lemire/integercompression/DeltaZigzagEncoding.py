from __future__ import annotations
import re
import io
import typing
from typing import *


class DeltaZigzagEncoding:

    pass


class Context:

    contextValue: int = 0

    def getContextValue(self) -> int:
        return self.contextValue

    def setContextValue(self, contextValue: int) -> None:
        self.contextValue = contextValue

    def __init__(self, contextValue: int) -> None:
        self.contextValue = contextValue


class Encoder(Context):

    def encodeArray3(self, src: typing.List[int]) -> typing.List[int]:
        return self.encodeArray0(src, 0, len(src), [0] * len(src), 0)

    def encodeArray2(
        self, src: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        return self.encodeArray0(src, offset, length, [0] * length, 0)

    def encodeArray1(
        self, src: typing.List[int], srcoff: int, length: int, dst: typing.List[int]
    ) -> typing.List[int]:
        return self.encodeArray0(src, srcoff, length, dst, 0)

    def encodeArray0(
        self,
        src: typing.List[int],
        srcoff: int,
        length: int,
        dst: typing.List[int],
        dstoff: int,
    ) -> typing.List[int]:
        for i in range(length):
            dst[dstoff + i] = self.encodeInt(src[srcoff + i])
        return dst

    def encodeInt(self, value: int) -> int:
        n = value - self.contextValue
        self.contextValue = value
        return (n << 1) ^ (n >> 31)

    def __init__(self, contextValue: int) -> None:
        super().__init__(contextValue)


class Decoder(Context):

    def decodeArray2(self, src: typing.List[int]) -> typing.List[int]:
        return self.decodeArray1(src, 0, len(src))

    def decodeArray1(
        self, src: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        return self.decodeArray0(src, offset, length, [0] * length, 0)

    def decodeArray0(
        self,
        src: typing.List[int],
        srcoff: int,
        length: int,
        dst: typing.List[int],
        dstoff: int,
    ) -> typing.List[int]:
        for i in range(length):
            dst[dstoff + i] = self.decodeInt(src[srcoff + i])
        return dst

    def decodeInt(self, value: int) -> int:
        n = (value >> 1) ^ (-(value & 1))
        n += self.contextValue
        self.contextValue = n
        return n

    def __init__(self, contextValue: int) -> None:
        super().__init__(contextValue)
