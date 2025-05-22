from __future__ import annotations
import time
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *


class StringUtils:

    @staticmethod
    def newStringUtf8(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "utf-8")

    @staticmethod
    def newStringUtf16Le(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "utf-16le")

    @staticmethod
    def newStringUtf16Be(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "utf-16-be")

    @staticmethod
    def newStringUtf16(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "utf-16")

    @staticmethod
    def newStringUsAscii(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "ascii")

    @staticmethod
    def newStringIso8859_1(bytes_: typing.List[int]) -> str:
        return StringUtils.__newString0(bytes_, "ISO-8859-1")

    @staticmethod
    def newString1(bytes_: typing.List[int], charsetName: str) -> str:
        if bytes_ is None:
            return None
        try:
            return bytearray(bytes_).decode(charsetName)
        except (UnicodeEncodeError, LookupError) as e:
            raise StringUtils.__newRuntimeError(charsetName, e)

    @staticmethod
    def getBytesUtf8(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "utf-8")

    @staticmethod
    def getBytesUtf16Le(string: str) -> typing.List[int]:
        return list(StringUtils.__getBytes(string, "utf-16le"))

    @staticmethod
    def getBytesUtf16Be(string: str) -> typing.List[int]:
        return list(string.encode("utf-16be"))

    @staticmethod
    def getBytesUtf16(string: str) -> typing.List[int]:
        return list(StringUtils.__getBytes(string, "utf-16"))

    @staticmethod
    def getBytesUsAscii(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "ascii")

    @staticmethod
    def getBytesUnchecked(string: str, charsetName: str) -> typing.List[int]:
        if string is None:
            return None
        try:
            return list(string.encode(charsetName))
        except (UnicodeEncodeError, LookupError) as e:
            raise StringUtils.__newRuntimeError(charsetName, e)

    @staticmethod
    def getBytesIso8859_1(string: str) -> typing.List[int]:
        return StringUtils.__getBytes(string, "ISO-8859-1")

    @staticmethod
    def getByteBufferUtf8(string: str) -> typing.Union[bytearray, memoryview]:
        return StringUtils.__getByteBuffer(string, "utf-8")

    @staticmethod
    def equals(cs1: str, cs2: str) -> bool:
        if cs1 is cs2:
            return True
        if cs1 is None or cs2 is None:
            return False
        if isinstance(cs1, str) and isinstance(cs2, str):
            return cs1 == cs2
        return len(cs1) == len(cs2) and CharSequenceUtils.regionMatches(
            cs1, False, 0, cs2, 0, len(cs1)
        )

    @staticmethod
    def __newString0(bytes_: typing.List[int], charset: str) -> str:
        return None if bytes_ is None else bytes(bytearray(bytes_)).decode(charset)

    @staticmethod
    def __newRuntimeError(
        charsetName: str, e: typing.Union[UnicodeEncodeError, ValueError]
    ) -> RuntimeError:
        return RuntimeError(f"{charsetName}: {e}")

    @staticmethod
    def __getBytes(string: str, charset: str) -> typing.List[int]:
        if string is None:
            return None
        return list(string.encode(charset, errors="surrogatepass"))

    @staticmethod
    def __getByteBuffer(string: str, charset: str) -> typing.Optional[ByteBuffer]:
        if string is None:
            return None
        return ByteBuffer.wrap(string.encode(charset))
