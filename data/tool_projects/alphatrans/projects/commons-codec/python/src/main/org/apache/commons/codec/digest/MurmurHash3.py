from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class MurmurHash3:

    SHORT_BYTES: int = 2
    INTEGER_BYTES: int = int(32 / 8)
    LONG_BYTES: int = 8
    DEFAULT_SEED: int = 104729
    NULL_HASHCODE: int = 2862933555777941757
    __N2: int = 0x38495AB5
    __N1: int = 0x52DCE729
    __M: int = 5
    __R3: int = 33
    __R2: int = 27
    __R1: int = 31
    __C2: int = 0x4CF5AD432745937F
    __C1: int = 0x87C37B91114253D5
    __N_32: int = 0xE6546B64
    __M_32: int = 5
    __R2_32: int = 13
    __R1_32: int = 15
    __C2_32: int = 0x1B873593
    __C1_32: int = 0xCC9E2D51

    @staticmethod
    def hash1282(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        return MurmurHash3.__hash128x64Internal(data, offset, length, seed)

    @staticmethod
    def hash1281(data: str) -> typing.List[int]:
        bytes_data = StringUtils.getBytesUtf8(data)
        return MurmurHash3.hash1282(
            bytes_data, 0, len(bytes_data), MurmurHash3.DEFAULT_SEED
        )

    @staticmethod
    def hash645(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        hash_ = seed
        nblocks = length >> 3

        for i in range(nblocks):
            index = offset + (i << 3)
            k = MurmurHash3.__getLittleEndianLong(data, index)

            k *= MurmurHash3.__C1
            k = (
                (k << MurmurHash3.__R1) | (k >> (64 - MurmurHash3.__R1))
            ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
            k *= MurmurHash3.__C2
            hash_ ^= k
            hash_ = (
                (hash_ << MurmurHash3.__R2) | (hash_ >> (64 - MurmurHash3.__R2))
            ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
            hash_ = (hash_ * MurmurHash3.__M + MurmurHash3.__N1) & 0xFFFFFFFFFFFFFFFF

        k1 = 0
        index = offset + (nblocks << 3)
        remaining = length - (nblocks << 3)

        if remaining >= 7:
            k1 ^= (data[index + 6] & 0xFF) << 48
        if remaining >= 6:
            k1 ^= (data[index + 5] & 0xFF) << 40
        if remaining >= 5:
            k1 ^= (data[index + 4] & 0xFF) << 32
        if remaining >= 4:
            k1 ^= (data[index + 3] & 0xFF) << 24
        if remaining >= 3:
            k1 ^= (data[index + 2] & 0xFF) << 16
        if remaining >= 2:
            k1 ^= (data[index + 1] & 0xFF) << 8
        if remaining >= 1:
            k1 ^= data[index] & 0xFF
            k1 *= MurmurHash3.__C1
            k1 = (
                (k1 << MurmurHash3.__R1) | (k1 >> (64 - MurmurHash3.__R1))
            ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
            k1 *= MurmurHash3.__C2
            hash_ ^= k1

        hash_ ^= length
        hash_ = MurmurHash3.__fmix64(hash_)

        return hash_

    @staticmethod
    def hash644(data: typing.List[int], offset: int, length: int) -> int:
        return MurmurHash3.hash645(data, offset, length, MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash643(data: typing.List[int]) -> int:
        return MurmurHash3.hash645(data, 0, len(data), MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash642(data: int) -> int:
        hash_ = MurmurHash3.DEFAULT_SEED
        k1 = 0
        k1 ^= (data & 0xFF) << 8
        k1 ^= ((data & 0xFF00) >> 8) & 0xFF
        k1 *= MurmurHash3.__C1
        k1 = (
            (k1 << MurmurHash3.__R1) | (k1 >> (64 - MurmurHash3.__R1))
        ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
        k1 *= MurmurHash3.__C2
        hash_ ^= k1

        hash_ ^= MurmurHash3.SHORT_BYTES
        hash_ = MurmurHash3.__fmix64(hash_)
        return hash_ & 0xFFFFFFFFFFFFFFFF

    @staticmethod
    def hash641(data: int) -> int:
        k1 = (
            int.from_bytes(
                data.to_bytes(4, byteorder="big", signed=True),
                byteorder="little",
                signed=False,
            )
            & 0xFFFFFFFF
        )
        length = MurmurHash3.INTEGER_BYTES
        hash_ = MurmurHash3.DEFAULT_SEED
        k1 *= MurmurHash3.__C1
        k1 = (
            (k1 << MurmurHash3.__R1) | (k1 >> (64 - MurmurHash3.__R1))
        ) & 0xFFFFFFFFFFFFFFFF  # Long.rotateLeft equivalent
        k1 *= MurmurHash3.__C2
        hash_ ^= k1
        hash_ ^= length
        hash_ = MurmurHash3.__fmix64(hash_)
        return hash_

    @staticmethod
    def hash640(data: int) -> int:
        hash_ = MurmurHash3.DEFAULT_SEED
        k = int.from_bytes(
            data.to_bytes(8, byteorder="big"), byteorder="little", signed=False
        )  # Reverse bytes
        length = MurmurHash3.LONG_BYTES
        k *= MurmurHash3.__C1
        k = (
            (k << MurmurHash3.__R1) | (k >> (64 - MurmurHash3.__R1))
        ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
        k *= MurmurHash3.__C2
        hash_ ^= k
        hash_ = (
            (hash_ << MurmurHash3.__R2) | (hash_ >> (64 - MurmurHash3.__R2))
        ) & 0xFFFFFFFFFFFFFFFF  # Rotate left
        hash_ = (hash_ * MurmurHash3.__M + MurmurHash3.__N1) & 0xFFFFFFFFFFFFFFFF
        hash_ ^= length
        hash_ = MurmurHash3.__fmix64(hash_)
        return hash_

    @staticmethod
    def hash328(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        hash_ = seed
        nblocks = length >> 2

        # Process the main blocks
        for i in range(nblocks):
            index = offset + (i << 2)
            k = MurmurHash3.__getLittleEndianInt(data, index)
            hash_ = MurmurHash3.__mix32(k, hash_)

        # Process the tail
        index = offset + (nblocks << 2)
        k1 = 0
        remaining = offset + length - index
        if remaining == 3:
            k1 ^= (data[index + 2] & 0xFF) << 16
        if remaining >= 2:
            k1 ^= (data[index + 1] & 0xFF) << 8
        if remaining >= 1:
            k1 ^= data[index] & 0xFF

            k1 *= MurmurHash3.__C1_32
            k1 = (
                (k1 << MurmurHash3.__R1_32) | (k1 >> (32 - MurmurHash3.__R1_32))
            ) & 0xFFFFFFFF  # Rotate left
            k1 *= MurmurHash3.__C2_32
            hash_ ^= k1

        # Finalization
        hash_ ^= length
        hash_ = MurmurHash3.__fmix32(hash_)
        return hash_

    @staticmethod
    def hash327(data: typing.List[int], length: int, seed: int) -> int:
        return MurmurHash3.hash328(data, 0, length, seed)

    @staticmethod
    def hash326(data: typing.List[int], length: int) -> int:
        return MurmurHash3.hash327(data, length, MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash325(data: str) -> int:
        bytes_ = StringUtils.getBytesUtf8(data)
        return MurmurHash3.hash328(bytes_, 0, len(bytes_), MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash324(data: typing.List[int]) -> int:
        return MurmurHash3.hash328(data, 0, len(data), MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash128x641(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        return MurmurHash3.__hash128x64Internal(data, offset, length, seed & 0xFFFFFFFF)

    @staticmethod
    def hash128x640(data: typing.List[int]) -> typing.List[int]:
        return MurmurHash3.hash128x641(data, 0, len(data), 0)

    @staticmethod
    def hash1280(data: typing.List[int]) -> typing.List[int]:
        return MurmurHash3.hash1282(data, 0, len(data), MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash32x861(data: typing.List[int], offset: int, length: int, seed: int) -> int:
        hash_ = seed
        nblocks = length >> 2

        # Process the main body in 4-byte chunks
        for i in range(nblocks):
            index = offset + (i << 2)
            k = MurmurHash3.__getLittleEndianInt(data, index)
            hash_ = MurmurHash3.__mix32(k, hash_)

        # Process the tail (remaining bytes)
        index = offset + (nblocks << 2)
        k1 = 0
        remaining = offset + length - index
        if remaining == 3:
            k1 ^= (data[index + 2] & 0xFF) << 16
        if remaining >= 2:
            k1 ^= (data[index + 1] & 0xFF) << 8
        if remaining >= 1:
            k1 ^= data[index] & 0xFF
            k1 *= MurmurHash3.__C1_32
            k1 = (
                (k1 << MurmurHash3.__R1_32) | (k1 >> (32 - MurmurHash3.__R1_32))
            ) & 0xFFFFFFFF  # Rotate left
            k1 *= MurmurHash3.__C2_32
            hash_ ^= k1

        # Finalization
        hash_ ^= length
        return MurmurHash3.__fmix32(hash_)

    @staticmethod
    def hash32x860(data: typing.List[int]) -> int:
        return MurmurHash3.hash32x861(data, 0, len(data), 0)

    @staticmethod
    def hash323(data: int, seed: int) -> int:
        hash_ = seed
        r0 = int.from_bytes(
            data.to_bytes(8, byteorder="little", signed=True),
            byteorder="big",
            signed=False,
        )  # Reverse bytes

        hash_ = MurmurHash3.__mix32(r0 & 0xFFFFFFFF, hash_)  # Lower 32 bits
        hash_ = MurmurHash3.__mix32((r0 >> 32) & 0xFFFFFFFF, hash_)  # Upper 32 bits

        hash_ ^= MurmurHash3.LONG_BYTES
        return MurmurHash3.__fmix32(hash_)

    @staticmethod
    def hash322(data: int) -> int:
        return MurmurHash3.hash323(data & 0xFFFFFFFFFFFFFFFF, MurmurHash3.DEFAULT_SEED)

    @staticmethod
    def hash321(data1: int, data2: int, seed: int) -> int:
        hash_ = seed
        r0 = int.from_bytes(
            data1.to_bytes(8, byteorder="big", signed=False),
            byteorder="little",
            signed=False,
        )
        r1 = int.from_bytes(
            data2.to_bytes(8, byteorder="big", signed=False),
            byteorder="little",
            signed=False,
        )

        hash_ = MurmurHash3.__mix32(r0 & 0xFFFFFFFF, hash_)
        hash_ = MurmurHash3.__mix32((r0 >> 32) & 0xFFFFFFFF, hash_)
        hash_ = MurmurHash3.__mix32(r1 & 0xFFFFFFFF, hash_)
        hash_ = MurmurHash3.__mix32((r1 >> 32) & 0xFFFFFFFF, hash_)

        hash_ ^= MurmurHash3.LONG_BYTES * 2
        return MurmurHash3.__fmix32(hash_)

    @staticmethod
    def hash320(data1: int, data2: int) -> int:
        return MurmurHash3.hash321(
            data1 & 0xFFFFFFFFFFFFFFFF,
            data2 & 0xFFFFFFFFFFFFFFFF,
            MurmurHash3.DEFAULT_SEED,
        )

    @staticmethod
    def __fmix64(hash_: int) -> int:
        hash_ ^= hash_ >> 33
        hash_ = (hash_ * 0xFF51AFD7ED558CCD) & 0xFFFFFFFFFFFFFFFF
        hash_ ^= hash_ >> 33
        hash_ = (hash_ * 0xC4CEB9FE1A85EC53) & 0xFFFFFFFFFFFFFFFF
        hash_ ^= hash_ >> 33
        return hash_ & 0xFFFFFFFFFFFFFFFF

    @staticmethod
    def __fmix32(hash_: int) -> int:
        hash_ ^= hash_ >> 16
        hash_ = (hash_ * 0x85EBCA6B) & 0xFFFFFFFF  # Ensure 32-bit overflow behavior
        hash_ ^= hash_ >> 13
        hash_ = (hash_ * 0xC2B2AE35) & 0xFFFFFFFF  # Ensure 32-bit overflow behavior
        hash_ ^= hash_ >> 16
        return (
            hash_ & 0xFFFFFFFF
        )  # Ensure the final result is a 32-bit unsigned integer

    @staticmethod
    def __mix32(k: int, hash_: int) -> int:
        k *= MurmurHash3.__C1_32
        k = (
            (k << MurmurHash3.__R1_32) | (k >> (32 - MurmurHash3.__R1_32))
        ) & 0xFFFFFFFF  # Rotate left
        k *= MurmurHash3.__C2_32
        hash_ ^= k
        hash_ = (
            (hash_ << MurmurHash3.__R2_32) | (hash_ >> (32 - MurmurHash3.__R2_32))
        ) & 0xFFFFFFFF  # Rotate left
        return (hash_ * MurmurHash3.__M_32 + MurmurHash3.__N_32) & 0xFFFFFFFF

    @staticmethod
    def __getLittleEndianInt(data: typing.List[int], index: int) -> int:
        return (
            (data[index] & 0xFF)
            | ((data[index + 1] & 0xFF) << 8)
            | ((data[index + 2] & 0xFF) << 16)
            | ((data[index + 3] & 0xFF) << 24)
        )

    @staticmethod
    def __getLittleEndianLong(data: typing.List[int], index: int) -> int:
        return (
            (data[index] & 0xFF)
            | ((data[index + 1] & 0xFF) << 8)
            | ((data[index + 2] & 0xFF) << 16)
            | ((data[index + 3] & 0xFF) << 24)
            | ((data[index + 4] & 0xFF) << 32)
            | ((data[index + 5] & 0xFF) << 40)
            | ((data[index + 6] & 0xFF) << 48)
            | ((data[index + 7] & 0xFF) << 56)
        )

    @staticmethod
    def __hash128x64Internal(
        data: typing.List[int], offset: int, length: int, seed: int
    ) -> typing.List[int]:
        h1 = seed
        h2 = seed
        nblocks = length >> 4

        for i in range(nblocks):
            index = offset + (i << 4)
            k1 = MurmurHash3.__getLittleEndianLong(data, index)
            k2 = MurmurHash3.__getLittleEndianLong(data, index + 8)

            k1 = (k1 * MurmurHash3.__C1) & 0xFFFFFFFFFFFFFFFF
            k1 = (
                (k1 << MurmurHash3.__R1) | (k1 >> (64 - MurmurHash3.__R1))
            ) & 0xFFFFFFFFFFFFFFFF
            k1 = (k1 * MurmurHash3.__C2) & 0xFFFFFFFFFFFFFFFF
            h1 ^= k1
            h1 = (
                (h1 << MurmurHash3.__R2) | (h1 >> (64 - MurmurHash3.__R2))
            ) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 * MurmurHash3.__M + MurmurHash3.__N1) & 0xFFFFFFFFFFFFFFFF

            k2 = (k2 * MurmurHash3.__C2) & 0xFFFFFFFFFFFFFFFF
            k2 = (
                (k2 << MurmurHash3.__R3) | (k2 >> (64 - MurmurHash3.__R3))
            ) & 0xFFFFFFFFFFFFFFFF
            k2 = (k2 * MurmurHash3.__C1) & 0xFFFFFFFFFFFFFFFF
            h2 ^= k2
            h2 = (
                (h2 << MurmurHash3.__R1) | (h2 >> (64 - MurmurHash3.__R1))
            ) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 + h1) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 * MurmurHash3.__M + MurmurHash3.__N2) & 0xFFFFFFFFFFFFFFFF

        k1 = 0
        k2 = 0
        index = offset + (nblocks << 4)
        remaining = length - (nblocks << 4)

        if remaining >= 15:
            k2 ^= (data[index + 14] & 0xFF) << 48
        if remaining >= 14:
            k2 ^= (data[index + 13] & 0xFF) << 40
        if remaining >= 13:
            k2 ^= (data[index + 12] & 0xFF) << 32
        if remaining >= 12:
            k2 ^= (data[index + 11] & 0xFF) << 24
        if remaining >= 11:
            k2 ^= (data[index + 10] & 0xFF) << 16
        if remaining >= 10:
            k2 ^= (data[index + 9] & 0xFF) << 8
        if remaining >= 9:
            k2 ^= data[index + 8] & 0xFF
            k2 = (k2 * MurmurHash3.__C2) & 0xFFFFFFFFFFFFFFFF
            k2 = (
                (k2 << MurmurHash3.__R3) | (k2 >> (64 - MurmurHash3.__R3))
            ) & 0xFFFFFFFFFFFFFFFF
            k2 = (k2 * MurmurHash3.__C1) & 0xFFFFFFFFFFFFFFFF
            h2 ^= k2

        if remaining >= 8:
            k1 ^= (data[index + 7] & 0xFF) << 56
        if remaining >= 7:
            k1 ^= (data[index + 6] & 0xFF) << 48
        if remaining >= 6:
            k1 ^= (data[index + 5] & 0xFF) << 40
        if remaining >= 5:
            k1 ^= (data[index + 4] & 0xFF) << 32
        if remaining >= 4:
            k1 ^= (data[index + 3] & 0xFF) << 24
        if remaining >= 3:
            k1 ^= (data[index + 2] & 0xFF) << 16
        if remaining >= 2:
            k1 ^= (data[index + 1] & 0xFF) << 8
        if remaining >= 1:
            k1 ^= data[index] & 0xFF
            k1 = (k1 * MurmurHash3.__C1) & 0xFFFFFFFFFFFFFFFF
            k1 = (
                (k1 << MurmurHash3.__R1) | (k1 >> (64 - MurmurHash3.__R1))
            ) & 0xFFFFFFFFFFFFFFFF
            k1 = (k1 * MurmurHash3.__C2) & 0xFFFFFFFFFFFFFFFF
            h1 ^= k1

        h1 ^= length
        h2 ^= length

        h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
        h2 = (h2 + h1) & 0xFFFFFFFFFFFFFFFF

        h1 = MurmurHash3.__fmix64(h1)
        h2 = MurmurHash3.__fmix64(h2)

        h1 = (h1 + h2) & 0xFFFFFFFFFFFFFFFF
        h2 = (h2 + h1) & 0xFFFFFFFFFFFFFFFF

        return [h1, h2]

    def __init__(self) -> None:
        pass


class IncrementalHash32x86:

    __hash: int = 0

    __totalLen: int = 0

    __unprocessedLength: int = 0

    __unprocessed: typing.List[int] = [0] * 3
    __BLOCK_SIZE: int = 4

    def end(self) -> int:
        return self.finalise(
            self.__hash, self.__unprocessedLength, self.__unprocessed, self.__totalLen
        )

    def add(self, data: typing.List[int], offset: int, length: int) -> None:
        if length <= 0:
            return
        self.__totalLen += length

        if self.__unprocessedLength + length - self.__BLOCK_SIZE < 0:
            self.__unprocessed[
                self.__unprocessedLength : self.__unprocessedLength + length
            ] = data[offset : offset + length]
            self.__unprocessedLength += length
            return

        if self.__unprocessedLength > 0:
            k = -1
            if self.__unprocessedLength == 1:
                k = self.__orBytes(
                    self.__unprocessed[0],
                    data[offset],
                    data[offset + 1],
                    data[offset + 2],
                )
            elif self.__unprocessedLength == 2:
                k = self.__orBytes(
                    self.__unprocessed[0],
                    self.__unprocessed[1],
                    data[offset],
                    data[offset + 1],
                )
            elif self.__unprocessedLength == 3:
                k = self.__orBytes(
                    self.__unprocessed[0],
                    self.__unprocessed[1],
                    self.__unprocessed[2],
                    data[offset],
                )
            else:
                raise ValueError(
                    f"Unprocessed length should be 1, 2, or 3: {self.__unprocessedLength}"
                )

            self.__hash = MurmurHash3.__mix32(k, self.__hash)
            consumed = self.__BLOCK_SIZE - self.__unprocessedLength
            newOffset = offset + consumed
            newLength = length - consumed
        else:
            newOffset = offset
            newLength = length

        nblocks = newLength >> 2

        for i in range(nblocks):
            index = newOffset + (i << 2)
            k = MurmurHash3.__getLittleEndianInt(data, index)
            self.__hash = MurmurHash3.__mix32(k, self.__hash)

        consumed = nblocks << 2
        self.__unprocessedLength = newLength - consumed
        if self.__unprocessedLength != 0:
            self.__unprocessed[: self.__unprocessedLength] = data[
                newOffset + consumed : newOffset + consumed + self.__unprocessedLength
            ]

    def start(self, seed: int) -> None:
        self.__unprocessedLength = 0
        self.__totalLen = 0
        self.__hash = seed

    @staticmethod
    def __orBytes(b1: int, b2: int, b3: int, b4: int) -> int:
        return (
            (b1 & 0xFF) | ((b2 & 0xFF) << 8) | ((b3 & 0xFF) << 16) | ((b4 & 0xFF) << 24)
        )

    def finalise(
        self,
        hash_: int,
        unprocessedLength: int,
        unprocessed: typing.List[int],
        totalLen: int,
    ) -> int:
        result = hash_
        k1 = 0

        if unprocessedLength == 3:
            k1 ^= (unprocessed[2] & 0xFF) << 16
        if unprocessedLength >= 2:
            k1 ^= (unprocessed[1] & 0xFF) << 8
        if unprocessedLength >= 1:
            k1 ^= unprocessed[0] & 0xFF

            k1 *= MurmurHash3.__C1_32
            k1 = (
                (k1 << MurmurHash3.__R1_32) | (k1 >> (32 - MurmurHash3.__R1_32))
            ) & 0xFFFFFFFF  # Rotate left
            k1 *= MurmurHash3.__C2_32
            result ^= k1

        result ^= totalLen
        return MurmurHash3.__fmix32(result)


class IncrementalHash32(IncrementalHash32x86):

    def finalise(
        self,
        hash_: int,
        unprocessedLength: int,
        unprocessed: typing.List[int],
        totalLen: int,
    ) -> int:
        result = hash_
        k1 = 0

        if unprocessedLength == 3:
            k1 ^= unprocessed[2] << 16
        if unprocessedLength >= 2:
            k1 ^= unprocessed[1] << 8
        if unprocessedLength >= 1:
            k1 ^= unprocessed[0]

            k1 *= self.__C1_32
            k1 = (
                (k1 << self.__R1_32) | (k1 >> (32 - self.__R1_32))
            ) & 0xFFFFFFFF  # Rotate left
            k1 *= self.__C2_32
            result ^= k1

        result ^= totalLen
        return MurmurHash3.__fmix32(result)
