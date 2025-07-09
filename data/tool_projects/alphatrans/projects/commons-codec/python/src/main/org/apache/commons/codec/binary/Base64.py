from __future__ import annotations
import time
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64(BaseNCodec):

    __encodeSize: int = 0

    __decodeSize: int = 0

    __lineSeparator: typing.List[int] = None

    __DECODE_TABLE: typing.List[int] = [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 00-0f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 10-1f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        62,
        -1,
        62,
        -1,
        63,  # 20-2f + - /
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 30-3f 0-9
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,  # 40-4f A-O
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        -1,
        -1,
        -1,
        -1,
        63,  # 50-5f P-Z _
        -1,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,  # 60-6f a-o
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,  # 70-7a p-z
    ]
    __encodeTable: typing.List[int] = None

    __MASK_2BITS: int = 0x3
    __MASK_4BITS: int = 0xF
    __MASK_6BITS: int = 0x3F
    __URL_SAFE_ENCODE_TABLE: typing.List[int] = [
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
        ord("g"),
        ord("h"),
        ord("i"),
        ord("j"),
        ord("k"),
        ord("l"),
        ord("m"),
        ord("n"),
        ord("o"),
        ord("p"),
        ord("q"),
        ord("r"),
        ord("s"),
        ord("t"),
        ord("u"),
        ord("v"),
        ord("w"),
        ord("x"),
        ord("y"),
        ord("z"),
        ord("0"),
        ord("1"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
        ord("8"),
        ord("9"),
        ord("-"),
        ord("_"),
    ]
    __STANDARD_ENCODE_TABLE: typing.List[int] = [
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
        ord("g"),
        ord("h"),
        ord("i"),
        ord("j"),
        ord("k"),
        ord("l"),
        ord("m"),
        ord("n"),
        ord("o"),
        ord("p"),
        ord("q"),
        ord("r"),
        ord("s"),
        ord("t"),
        ord("u"),
        ord("v"),
        ord("w"),
        ord("x"),
        ord("y"),
        ord("z"),
        ord("0"),
        ord("1"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
        ord("8"),
        ord("9"),
        ord("+"),
        ord("/"),
    ]
    __BYTES_PER_ENCODED_BLOCK: int = 4
    __BYTES_PER_UNENCODED_BLOCK: int = 3
    __BITS_PER_ENCODED_BYTE: int = 6

    def _isInAlphabet0(self, octet: int) -> bool:
        return (
            0 <= octet < len(self._Base64__decodeTable)
            and self._Base64__decodeTable[octet] != -1
        )

    @staticmethod
    def isArrayByteBase64(arrayOctet: typing.List[int]) -> bool:
        return Base64.isBase641(arrayOctet)

    def isUrlSafe(self) -> bool:
        return self._Base64__encodeTable == self._Base64__URL_SAFE_ENCODE_TABLE

    @staticmethod
    def Base645() -> Base64:
        return Base64.Base643(0)

    @staticmethod
    def Base644(urlSafe: bool) -> Base64:
        return Base64(BaseNCodec.MIME_CHUNK_SIZE, BaseNCodec.CHUNK_SEPARATOR, urlSafe)

    @staticmethod
    def Base643(lineLength: int) -> Base64:
        return Base64.Base642(lineLength, BaseNCodec.CHUNK_SEPARATOR)

    return Base64.Base641(lineLength, lineSeparator, False)

    @staticmethod
    def Base641(
        lineLength: int, lineSeparator: typing.List[int], urlSafe: bool
    ) -> Base64:
        return Base64(
            lineLength, lineSeparator, urlSafe, BaseNCodec._DECODING_POLICY_DEFAULT
        )

    def __init__(
        self,
        lineLength: int,
        lineSeparator: typing.List[int],
        urlSafe: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        super().__init__(
            2,
            self.__BYTES_PER_UNENCODED_BLOCK,
            self.__BYTES_PER_ENCODED_BLOCK,
            lineLength,
            len(lineSeparator) if lineSeparator is not None else 0,
            self._PAD_DEFAULT,
            decodingPolicy,
        )
        if lineSeparator is not None:
            if self._containsAlphabetOrPad(lineSeparator):
                sep = StringUtils.newStringUtf8(lineSeparator)
                raise ValueError(
                    f"lineSeparator must not contain base64 characters: [{sep}]"
                )
            if (
                lineLength > 0
            ):  # null line-sep forces no chunking rather than throwing IAE
                self.__encodeSize = self.__BYTES_PER_ENCODED_BLOCK + len(lineSeparator)
                self.__lineSeparator = lineSeparator[:]
            else:
                self.__encodeSize = self.__BYTES_PER_ENCODED_BLOCK
                self.__lineSeparator = None
        else:
            self.__encodeSize = self.__BYTES_PER_ENCODED_BLOCK
            self.__lineSeparator = None

        self.__decodeSize = self.__encodeSize - 1
        self.__encodeTable = (
            self.__URL_SAFE_ENCODE_TABLE if urlSafe else self.__STANDARD_ENCODE_TABLE
        )

    @staticmethod
    def toIntegerBytes(bigInt: int) -> typing.List[int]:
        bitlen = bigInt.bit_length()
        bitlen = ((bitlen + 7) >> 3) << 3
        bigBytes = bigInt.to_bytes(
            (bigInt.bit_length() + 7) // 8, byteorder="big", signed=True
        )

        if ((bigInt.bit_length() % 8) != 0) and (
            ((bigInt.bit_length() // 8) + 1) == (bitlen // 8)
        ):
            return list(bigBytes)

        startSrc = 0
        length = len(bigBytes)

        if (bigInt.bit_length() % 8) == 0:
            startSrc = 1
            length -= 1

        startDst = bitlen // 8 - length  # to pad with nulls as per spec
        resizedBytes = [0] * (bitlen // 8)
        resizedBytes[startDst : startDst + length] = bigBytes[
            startSrc : startSrc + length
        ]
        return resizedBytes

    @staticmethod
    def isBase642(base64: str) -> bool:
        return Base64.isBase641(StringUtils.getBytesUtf8(base64))

    @staticmethod
    def isBase641(arrayOctet: typing.List[int]) -> bool:
        for element in arrayOctet:
            if not Base64.isBase640(element) and not Base64._isWhiteSpace(element):
                return False
        return True

    @staticmethod
    def isBase640(octet: int) -> bool:
        PAD_DEFAULT = ord("=")  # Static default value
        return octet == PAD_DEFAULT or (
            0 <= octet < len(Base64.__DECODE_TABLE)
            and Base64.__DECODE_TABLE[octet] != -1
        )

    @staticmethod
    def encodeInteger(bigInteger: int) -> typing.List[int]:
        if bigInteger is None:
            raise ValueError("bigInteger cannot be None")
        return Base64.encodeBase641(Base64.toIntegerBytes(bigInteger), False)

    @staticmethod
    def encodeBase64URLSafeString(binaryData: typing.List[int]) -> str:
        return StringUtils.newStringUsAscii(
            Base64.encodeBase642(binaryData, False, True)
        )

    @staticmethod
    def encodeBase64URLSafe(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase642(binaryData, False, True)

    @staticmethod
    def encodeBase64String(binaryData: typing.List[int]) -> str:
        return StringUtils.newStringUsAscii(Base64.encodeBase641(binaryData, False))

    @staticmethod
    def encodeBase64Chunked(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase641(binaryData, True)

    @staticmethod
    def encodeBase643(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool, maxResultSize: int
    ) -> typing.List[int]:
        if binaryData is None or len(binaryData) == 0:
            return binaryData

        b64 = (
            Base64.Base644(urlSafe)
            if isChunked
            else Base64.Base641(0, BaseNCodec.CHUNK_SEPARATOR, urlSafe)
        )
        len_ = b64.getEncodedLength(binaryData)
        if len_ > maxResultSize:
            raise ValueError(
                f"Input array too big, the output array would be bigger ({len_}) than the specified maximum size of {maxResultSize}"
            )

        return b64.encode0(binaryData)

    @staticmethod
    def encodeBase642(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool
    ) -> typing.List[int]:
        return Base64.encodeBase643(binaryData, isChunked, urlSafe, int((1 << 31) - 1))

    @staticmethod
    def encodeBase641(
        binaryData: typing.List[int], isChunked: bool
    ) -> typing.List[int]:
        return Base64.encodeBase642(binaryData, isChunked, False)

    @staticmethod
    def encodeBase640(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase641(binaryData, False)

    @staticmethod
    def decodeInteger(pArray: typing.List[int]) -> int:
        return int.from_bytes(
            Base64.decodeBase640(pArray), byteorder="big", signed=False
        )

    @staticmethod
    def decodeBase641(base64String: str) -> typing.List[int]:
        return Base64.Base645().decode3(base64String)

    @staticmethod
    def decodeBase640(base64Data: typing.List[int]) -> typing.List[int]:
        return Base64.Base645().decode0(base64Data)

    def __validateTrailingCharacter(self) -> None:
        if self.isStrictDecoding():
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                " valid base 64 alphabet but not a possible encoding. Decoding requires"
                " at least two trailing 6-bit characters to create bytes."
            )

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        if self.isStrictDecoding() and (context.ibitWorkArea & emptyBitsMask) != 0:
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                " valid base 64 alphabet but not a possible encoding. Expected the"
                " discarded bits from the character to be zero."
            )

    def encode2(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True
            if context.modulus == 0 and self._lineLength == 0:
                return  # no leftovers to process and not using chunking
            buffer = self._ensureBufferSize(self.__encodeSize, context)
            savedPos = context.pos
            if context.modulus == 0:
                pass  # nothing to do here
            elif context.modulus == 1:  # 8 bits = 6 + 2
                buffer[context.pos] = self.__encodeTable[
                    (context.ibitWorkArea >> 2) & self.__MASK_6BITS
                ]
                context.pos += 1
                buffer[context.pos] = self.__encodeTable[
                    (context.ibitWorkArea << 4) & self.__MASK_6BITS
                ]
                context.pos += 1
                if self.__encodeTable == self.__STANDARD_ENCODE_TABLE:
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
            elif context.modulus == 2:  # 16 bits = 6 + 6 + 4
                buffer[context.pos] = self.__encodeTable[
                    (context.ibitWorkArea >> 10) & self.__MASK_6BITS
                ]
                context.pos += 1
                buffer[context.pos] = self.__encodeTable[
                    (context.ibitWorkArea >> 4) & self.__MASK_6BITS
                ]
                context.pos += 1
                buffer[context.pos] = self.__encodeTable[
                    (context.ibitWorkArea << 2) & self.__MASK_6BITS
                ]
                context.pos += 1
                if self.__encodeTable == self.__STANDARD_ENCODE_TABLE:
                    buffer[context.pos] = self._pad
                    context.pos += 1
            else:
                raise ValueError(f"Impossible modulus {context.modulus}")
            context.currentLinePos += (
                context.pos - savedPos
            )  # keep track of current line position
            if self._lineLength > 0 and context.currentLinePos > 0:
                buffer[context.pos : context.pos + len(self.__lineSeparator)] = (
                    self.__lineSeparator
                )
                context.pos += len(self.__lineSeparator)
        else:
            for i in range(inAvail):
                buffer = self._ensureBufferSize(self.__encodeSize, context)
                context.modulus = (
                    context.modulus + 1
                ) % self.__BYTES_PER_UNENCODED_BLOCK
                b = in_[inPos]
                inPos += 1
                if b < 0:
                    b += 256
                context.ibitWorkArea = (context.ibitWorkArea << 8) + b  # BITS_PER_BYTE
                if context.modulus == 0:  # 3 bytes = 24 bits = 4 * 6 bits to extract
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 18) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 12) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 6) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        context.ibitWorkArea & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    context.currentLinePos += self.__BYTES_PER_ENCODED_BLOCK
                    if (
                        self._lineLength > 0
                        and self._lineLength <= context.currentLinePos
                    ):
                        buffer[
                            context.pos : context.pos + len(self.__lineSeparator)
                        ] = self.__lineSeparator
                        context.pos += len(self.__lineSeparator)
                        context.currentLinePos = 0

    def decode1(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True

        for i in range(inAvail):
            buffer = self._ensureBufferSize(self.__decodeSize, context)
            b = in_[inPos]
            inPos += 1
            if b == self._pad:
                context.eof = True
                break
            if 0 <= b < len(self.__DECODE_TABLE):
                result = self.__DECODE_TABLE[b]
                if result >= 0:
                    context.modulus = (
                        context.modulus + 1
                    ) % self.__BYTES_PER_ENCODED_BLOCK
                    context.ibitWorkArea = (
                        context.ibitWorkArea << self.__BITS_PER_ENCODED_BYTE
                    ) + result
                    if context.modulus == 0:
                        buffer[context.pos] = (
                            context.ibitWorkArea >> 16
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = (
                            context.ibitWorkArea >> 8
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                        context.pos += 1

        if context.eof and context.modulus != 0:
            buffer = self._ensureBufferSize(self.__decodeSize, context)

            if (
                context.modulus == 1
            ):  # 6 bits - either ignore entirely, or raise an exception
                self.__validateTrailingCharacter()
            elif context.modulus == 2:  # 12 bits = 8 + 4
                self.__validateCharacter(self.__MASK_4BITS, context)
                context.ibitWorkArea = (
                    context.ibitWorkArea >> 4
                )  # dump the extra 4 bits
                buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 3:  # 18 bits = 8 + 8 + 2
                self.__validateCharacter(self.__MASK_2BITS, context)
                context.ibitWorkArea = context.ibitWorkArea >> 2  # dump 2 bits
                buffer[context.pos] = (context.ibitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                context.pos += 1
            else:
                raise RuntimeError(f"Impossible modulus {context.modulus}")
