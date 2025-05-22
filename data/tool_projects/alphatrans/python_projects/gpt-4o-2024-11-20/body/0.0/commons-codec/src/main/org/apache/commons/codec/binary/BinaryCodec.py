from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryCodec(BinaryDecoder, BinaryEncoder):

    __BIT_7: int = 0x80
    __BIT_6: int = 0x40
    __BIT_5: int = 0x20
    __BIT_4: int = 0x10
    __BIT_3: int = 0x08
    __BIT_2: int = 0x04
    __BIT_1: int = 0x02
    __BIT_0: int = 1
    __EMPTY_BYTE_ARRAY: typing.List[int] = []
    __EMPTY_CHAR_ARRAY: typing.List[str] = []

    def toByteArray(self, ascii_: str) -> typing.List[int]:
        if ascii_ is None:
            return self.__EMPTY_BYTE_ARRAY
        return self.fromAscii1(list(ascii_))

    def encode1(self, raw: typing.Any) -> typing.Any:
        if not isinstance(raw, (bytes, bytearray)):
            raise EncoderException("argument not a byte array", None)
        return self.toAsciiChars(list(raw))

    def encode0(self, raw: typing.List[int]) -> typing.List[int]:
        return self.toAsciiBytes(raw)

    def decode1(self, ascii_: typing.Any) -> typing.Any:
        if ascii_ is None:
            return self.__EMPTY_BYTE_ARRAY
        if isinstance(ascii_, bytes):
            return self.fromAscii0(list(ascii_))
        if isinstance(ascii_, list) and all(isinstance(c, str) for c in ascii_):
            return self.fromAscii1(ascii_)
        if isinstance(ascii_, str):
            return self.fromAscii1(list(ascii_))
        raise DecoderException("argument not a byte array", None)

    def decode0(self, ascii_: typing.List[int]) -> typing.List[int]:
        return self.fromAscii0(ascii_)

    @staticmethod
    def toAsciiString(raw: typing.List[int]) -> str:
        return "".join(BinaryCodec.toAsciiChars(raw))

    @staticmethod
    def toAsciiChars(raw: typing.List[int]) -> typing.List[str]:
        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_CHAR_ARRAY

        raw_length = len(raw)
        l_ascii = [""] * (
            raw_length << 3
        )  # Create a list of empty strings with the required size

        # Iterate through the raw bytes and convert to ASCII characters
        for ii in range(raw_length):
            jj = (raw_length - ii) * 8 - 1  # Calculate the starting index for this byte
            for bits in range(len(BinaryCodec.__BITS)):
                if (raw[ii] & BinaryCodec.__BITS[bits]) == 0:
                    l_ascii[jj - bits] = "0"
                else:
                    l_ascii[jj - bits] = "1"

        return l_ascii

    @staticmethod
    def toAsciiBytes(raw: typing.List[int]) -> typing.List[int]:
        if BinaryCodec.__isEmpty(raw):
            return BinaryCodec.__EMPTY_BYTE_ARRAY

        raw_length = len(raw)
        l_ascii = [0] * (raw_length << 3)  # Create a list of size raw_length * 8

        # Iterate through each byte in the raw array
        for ii in range(raw_length):
            jj = (
                raw_length - ii
            ) * 8 - 1  # Calculate the starting index for this byte in l_ascii
            for bits in range(len(BinaryCodec.__BITS)):
                if (raw[ii] & BinaryCodec.__BITS[bits]) == 0:
                    l_ascii[jj - bits] = ord("0")  # ASCII value for '0'
                else:
                    l_ascii[jj - bits] = ord("1")  # ASCII value for '1'

        return l_ascii

    @staticmethod
    def fromAscii1(ascii_: typing.List[str]) -> typing.List[int]:
        if ascii_ is None or len(ascii_) == 0:
            return BinaryCodec.__EMPTY_BYTE_ARRAY

        ascii_length = len(ascii_)
        l_raw = [0] * (ascii_length >> 3)

        for ii in range(len(l_raw)):
            jj = ascii_length - 1 - (ii * 8)
            for bits in range(len(BinaryCodec.__BITS)):
                if ascii_[jj - bits] == "1":
                    l_raw[ii] |= BinaryCodec.__BITS[bits]

        return l_raw

    @staticmethod
    def fromAscii0(ascii_: typing.List[int]) -> typing.List[int]:
        if BinaryCodec.__isEmpty(ascii_):
            return BinaryCodec.__EMPTY_BYTE_ARRAY

        ascii_length = len(ascii_)
        l_raw = [0] * (ascii_length >> 3)

        # Iterate through the ascii array and populate l_raw
        for ii in range(len(l_raw)):
            jj = ascii_length - 1 - (ii * 8)
            for bits in range(len(BinaryCodec.__BITS)):
                if ascii_[jj - bits] == ord("1"):  # Compare with ASCII value of '1'
                    l_raw[ii] |= BinaryCodec.__BITS[bits]

        return l_raw

    @staticmethod
    def __isEmpty(array: typing.List[int]) -> bool:
        return array is None or len(array) == 0
