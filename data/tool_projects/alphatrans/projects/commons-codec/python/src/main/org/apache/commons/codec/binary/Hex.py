from __future__ import annotations
import re
import decimal
from io import BytesIO
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *


class Hex(BinaryDecoder, BinaryEncoder):

    DEFAULT_CHARSET_NAME: str = CharEncoding.UTF_8
    DEFAULT_CHARSET: str = "UTF-8"
    __charset: str = ""

    __DIGITS_UPPER: typing.List[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    __DIGITS_LOWER: typing.List[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]

    def toString(self) -> str:
        return super().__str__() + f"[charsetName={self.__charset}]"

    def getCharsetName(self) -> str:
        return self.__charset

    def getCharset(self) -> str:
        return self.__charset

    def encode2(self, object_: typing.Any) -> typing.Any:
        try:
            if isinstance(object_, str):
                byte_array = object_.encode(self.getCharset())
            elif isinstance(object_, (bytearray, memoryview)):
                byte_array = self.__toByteArray(object_)
            else:
                try:
                    byte_array = bytes(object_)
                except (TypeError, ValueError) as e:
                    raise EncoderException(str(e), e)
            return self.encodeHex0(byte_array)
        except Exception as e:
            raise EncoderException("Error during encoding", e)

    def encode1(self, array: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        return list(self.encodeHexString2(array).encode(self.getCharset()))

    def encode0(self, array: typing.List[int]) -> typing.List[int]:
        return list(self.encodeHexString0(array).encode(self.getCharset()))

    def decode2(self, object_: typing.Any) -> typing.Any:
        if isinstance(object_, str):
            return self.decode2(list(object_))  # Convert string to list of characters
        if isinstance(object_, (bytes, bytearray)):
            return bytearray(self.decode0(object_))  # Ensure the output is a bytearray
        if isinstance(object_, (io.BytesIO, memoryview)):
            return self.decode1(object_)
        try:
            return self.decodeHex0(object_)
        except TypeError as e:
            raise DecoderException(str(e), e)

    def decode1(self, buffer: typing.Union[bytearray, memoryview]) -> typing.List[int]:
        return self.decodeHex0(
            list(str(bytearray(self.__toByteArray(buffer)), self.getCharset()))
        )

    def decode0(self, array: typing.List[int]) -> typing.List[int]:
        return self.decodeHex0(list(str(bytearray(array), self.getCharset())))

    @staticmethod
    def Hex0(charsetName: str) -> Hex:
        return Hex(1, None, Charset.forName(charsetName))

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:
        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = Hex.DEFAULT_CHARSET

    @staticmethod
    def _toDigit(ch: str, index: int) -> int:
        digit = int(ch, 16) if ch in "0123456789abcdefABCDEF" else -1
        if digit == -1:
            raise DecoderException(
                f"Illegal hexadecimal character {ch} at index {index}", None
            )
        return digit

    @staticmethod
    def encodeHexString3(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> str:
        return "".join(Hex.encodeHex7(data, toLowerCase))

    @staticmethod
    def encodeHexString2(data: typing.Union[bytearray, memoryview]) -> str:
        return "".join(Hex.encodeHex6(data))

    @staticmethod
    def encodeHexString1(data: typing.List[int], toLowerCase: bool) -> str:
        return "".join(Hex.encodeHex1(data, toLowerCase))

    @staticmethod
    def encodeHexString0(data: typing.List[int]) -> str:
        return "".join(Hex.encodeHex0(data))

    @staticmethod
    def _encodeHex8(
        byteBuffer: typing.Union[bytearray, memoryview], toDigits: typing.List[str]
    ) -> typing.List[str]:
        return Hex._encodeHex2(Hex.__toByteArray(byteBuffer), toDigits)

    @staticmethod
    def encodeHex7(
        data: typing.Union[bytearray, memoryview], toLowerCase: bool
    ) -> typing.List[str]:
        return Hex._encodeHex8(
            data, Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER
        )

    @staticmethod
    def encodeHex6(data: typing.Union[bytearray, memoryview]) -> typing.List[str]:
        return Hex.encodeHex7(data, True)

    Hex.__encodeHex5(
        data,
        dataOffset,
        dataLen,
        Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER,
        out,
        outOffset,
    )

    @staticmethod
    def encodeHex3(
        data: typing.List[int], dataOffset: int, dataLen: int, toLowerCase: bool
    ) -> typing.List[str]:
        out = [""] * (
            dataLen << 1
        )  # Create a list of empty strings with size dataLen * 2
        Hex.__encodeHex5(
            data,
            dataOffset,
            dataLen,
            Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER,
            out,
            0,
        )
        return out

    @staticmethod
    def _encodeHex2(
        data: typing.List[int], toDigits: typing.List[str]
    ) -> typing.List[str]:
        dataLength = len(data)
        out = [""] * (dataLength << 1)
        Hex.__encodeHex5(data, 0, dataLength, toDigits, out, 0)
        return out

    @staticmethod
    def encodeHex1(data: typing.List[int], toLowerCase: bool) -> typing.List[str]:
        return Hex._encodeHex2(
            data, Hex.__DIGITS_LOWER if toLowerCase else Hex.__DIGITS_UPPER
        )

    @staticmethod
    def encodeHex0(data: typing.List[int]) -> typing.List[str]:
        return Hex.encodeHex1(data, True)

    @staticmethod
    def decodeHex2(data: str) -> typing.List[int]:
        return Hex.decodeHex0(list(data))

    @staticmethod
    def decodeHex1(
        data: typing.List[str], out: typing.List[int], outOffset: int
    ) -> int:
        length = len(data)

        # Check if the length of the input data is odd
        if (length & 0x01) != 0:
            raise DecoderException("Odd number of characters.", None)

        outLen = length >> 1
        # Check if the output array has enough space
        if len(out) - outOffset < outLen:
            raise DecoderException(
                "Output array is not large enough to accommodate decoded data.", None
            )

        # Decode the hex data
        j = 0
        for i in range(outOffset, outOffset + outLen):
            f = Hex._toDigit(data[j], j) << 4
            j += 1
            f |= Hex._toDigit(data[j], j)
            j += 1
            out[i] = f & 0xFF

        return outLen

    @staticmethod
    def decodeHex0(data: typing.List[str]) -> typing.List[int]:
        out = [0] * (
            len(data) >> 1
        )  # Create an output array with half the size of the input data
        Hex.decodeHex1(data, out, 0)  # Call decodeHex1 to perform the decoding
        return out

    @staticmethod
    def __toByteArray(
        byteBuffer: typing.Union[bytearray, memoryview],
    ) -> typing.List[int]:
        remaining = len(byteBuffer)
        if isinstance(byteBuffer, memoryview) and byteBuffer.contiguous:
            byteArray = byteBuffer.tobytes()
            if remaining == len(byteArray):
                return list(byteArray)
        byteArray = byteBuffer[:remaining]
        return list(byteArray)

    @staticmethod
    def __encodeHex5(
        data: typing.List[int],
        dataOffset: int,
        dataLen: int,
        toDigits: typing.List[str],
        out: typing.List[str],
        outOffset: int,
    ) -> None:
        for i in range(dataOffset, dataOffset + dataLen):
            out[outOffset] = toDigits[(0xF0 & data[i]) >> 4]
            outOffset += 1
            out[outOffset] = toDigits[0x0F & data[i]]
            outOffset += 1
