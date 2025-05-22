from __future__ import annotations
import re
import io
import numbers
import typing
from typing import *
import os


class Simple16WithHardCodes:

    __S16_BITS: typing.List[typing.List[int]] = [
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
        ],
        [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            4,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            3,
            4,
            4,
            4,
            4,
            3,
            3,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            4,
            4,
            4,
            4,
            4,
            4,
            4,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            5,
            5,
            5,
            5,
            4,
            4,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            4,
            4,
            5,
            5,
            5,
            5,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            6,
            6,
            6,
            5,
            5,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            5,
            5,
            6,
            6,
            6,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            7,
            7,
            7,
            7,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            10,
            9,
            9,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            14,
            14,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            28,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    ]
    __S16_NUM: typing.List[int] = [28, 21, 21, 21, 14, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]
    __S16_BITSSIZE: int = 28
    __S16_NUMSIZE: int = 16

    @staticmethod
    def _s16DecompressOneNumberWithHardCodesIntegrated(
        out: typing.List[int],
        outOffset: int,
        value: int,
        numIdx: int,
        oribits: int,
        expPos: typing.List[int],
    ) -> int:
        if numIdx == 0:
            for i in range(28):
                out[expPos[outOffset + i]] |= ((value >> i) & 0x00000001) << oribits
            return 28
        elif numIdx == 1:
            for i in range(7):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 2)) & 0x00000003
                ) << oribits
            for i in range(7, 21):
                out[expPos[outOffset + i]] |= (
                    (value >> (14 + (i - 7))) & 0x00000001
                ) << oribits
            return 21
        elif numIdx == 2:
            for i in range(7):
                out[expPos[outOffset + i]] |= ((value >> i) & 0x00000001) << oribits
            for i in range(7, 14):
                out[expPos[outOffset + i]] |= (
                    (value >> (7 + (i - 7) * 2)) & 0x00000003
                ) << oribits
            for i in range(14, 21):
                out[expPos[outOffset + i]] |= (
                    (value >> (21 + (i - 14))) & 0x00000001
                ) << oribits
            return 21
        elif numIdx == 3:
            for i in range(14):
                out[expPos[outOffset + i]] |= ((value >> i) & 0x00000001) << oribits
            for i in range(14, 21):
                out[expPos[outOffset + i]] |= (
                    (value >> (14 + (i - 14) * 2)) & 0x00000003
                ) << oribits
            return 21
        elif numIdx == 4:
            for i in range(14):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 2)) & 0x00000003
                ) << oribits
            return 14
        elif numIdx == 5:
            out[expPos[outOffset]] |= (value & 0x0000000F) << oribits
            for i in range(1, 9):
                out[expPos[outOffset + i]] |= (
                    (value >> (4 + (i - 1) * 3)) & 0x00000007
                ) << oribits
            return 9
        elif numIdx == 6:
            out[expPos[outOffset]] |= (value & 0x00000007) << oribits
            for i in range(1, 5):
                out[expPos[outOffset + i]] |= (
                    (value >> (3 + (i - 1) * 4)) & 0x0000000F
                ) << oribits
            for i in range(5, 8):
                out[expPos[outOffset + i]] |= (
                    (value >> (19 + (i - 5) * 3)) & 0x00000007
                ) << oribits
            return 8
        elif numIdx == 7:
            for i in range(7):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 4)) & 0x0000000F
                ) << oribits
            return 7
        elif numIdx == 8:
            for i in range(3):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 5)) & 0x0000001F
                ) << oribits
            out[expPos[outOffset + 4]] |= ((value >> 20) & 0x0000000F) << oribits
            out[expPos[outOffset + 5]] |= ((value >> 24) & 0x0000000F) << oribits
            return 6
        elif numIdx == 9:
            out[expPos[outOffset]] |= (value & 0x0000000F) << oribits
            for i in range(1, 6):
                out[expPos[outOffset + i]] |= (
                    (value >> (4 + (i - 1) * 5)) & 0x0000001F
                ) << oribits
            return 6
        elif numIdx == 10:
            for i in range(3):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 6)) & 0x0000003F
                ) << oribits
            out[expPos[outOffset + 3]] |= ((value >> 18) & 0x0000001F) << oribits
            out[expPos[outOffset + 4]] |= ((value >> 23) & 0x0000001F) << oribits
            return 5
        elif numIdx == 11:
            for i in range(2):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 5)) & 0x0000001F
                ) << oribits
            for i in range(2, 5):
                out[expPos[outOffset + i]] |= (
                    (value >> (10 + (i - 2) * 6)) & 0x0000003F
                ) << oribits
            return 5
        elif numIdx == 12:
            for i in range(4):
                out[expPos[outOffset + i]] |= (
                    (value >> (i * 7)) & 0x0000007F
                ) << oribits
            return 4
        elif numIdx == 13:
            out[expPos[outOffset]] |= (value & 0x000003FF) << oribits
            for i in range(1, 3):
                out[expPos[outOffset + i]] |= (
                    (value >> (10 + (i - 1) * 9)) & 0x000001FF
                ) << oribits
            return 3
        elif numIdx == 14:
            out[expPos[outOffset]] |= (value & 0x00003FFF) << oribits
            out[expPos[outOffset + 1]] |= ((value >> 14) & 0x00003FFF) << oribits
            return 2
        elif numIdx == 15:
            out[expPos[outOffset]] |= (value & 0x0FFFFFFF) << oribits
            return 1
        else:
            return -1

    @staticmethod
    def _s16DecompressOneNumberWithHardCodes(
        out: typing.List[int], outOffset: int, value: int, numIdx: int
    ) -> int:
        if numIdx == 0:
            for i in range(28):
                out[outOffset + i] = (value >> i) & 0x00000001
            return 28
        elif numIdx == 1:
            for i in range(7):
                out[outOffset + i] = (value >> (i * 2)) & 0x00000003
            for i in range(7, 21):
                out[outOffset + i] = (value >> (14 + (i - 7))) & 0x00000001
            return 21
        elif numIdx == 2:
            for i in range(7):
                out[outOffset + i] = (value >> i) & 0x00000001
            for i in range(7, 14):
                out[outOffset + i] = (value >> (7 + (i - 7) * 2)) & 0x00000003
            for i in range(14, 21):
                out[outOffset + i] = (value >> (21 + (i - 14))) & 0x00000001
            return 21
        elif numIdx == 3:
            for i in range(14):
                out[outOffset + i] = (value >> i) & 0x00000001
            for i in range(14, 21):
                out[outOffset + i] = (value >> (14 + (i - 14) * 2)) & 0x00000003
            return 21
        elif numIdx == 4:
            for i in range(14):
                out[outOffset + i] = (value >> (i * 2)) & 0x00000003
            return 14
        elif numIdx == 5:
            out[outOffset] = value & 0x0000000F
            for i in range(1, 9):
                out[outOffset + i] = (value >> (4 + (i - 1) * 3)) & 0x00000007
            return 9
        elif numIdx == 6:
            out[outOffset] = value & 0x00000007
            for i in range(1, 6):
                out[outOffset + i] = (value >> (3 + (i - 1) * 4)) & 0x0000000F
            for i in range(6, 8):
                out[outOffset + i] = (value >> (19 + (i - 6) * 3)) & 0x00000007
            return 8
        elif numIdx == 7:
            for i in range(7):
                out[outOffset + i] = (value >> (i * 4)) & 0x0000000F
            return 7
        elif numIdx == 8:
            for i in range(4):
                out[outOffset + i] = (value >> (i * 5)) & 0x0000001F
            for i in range(4, 6):
                out[outOffset + i] = (value >> (20 + (i - 4) * 4)) & 0x0000000F
            return 6
        elif numIdx == 9:
            out[outOffset] = value & 0x0000000F
            out[outOffset + 1] = (value >> 4) & 0x0000000F
            for i in range(2, 6):
                out[outOffset + i] = (value >> (8 + (i - 2) * 5)) & 0x0000001F
            return 6
        elif numIdx == 10:
            for i in range(3):
                out[outOffset + i] = (value >> (i * 6)) & 0x0000003F
            for i in range(3, 5):
                out[outOffset + i] = (value >> (18 + (i - 3) * 5)) & 0x0000001F
            return 5
        elif numIdx == 11:
            for i in range(2):
                out[outOffset + i] = (value >> (i * 5)) & 0x0000001F
            for i in range(2, 5):
                out[outOffset + i] = (value >> (10 + (i - 2) * 6)) & 0x0000003F
            return 5
        elif numIdx == 12:
            for i in range(4):
                out[outOffset + i] = (value >> (i * 7)) & 0x0000007F
            return 4
        elif numIdx == 13:
            out[outOffset] = value & 0x000003FF
            for i in range(1, 3):
                out[outOffset + i] = (value >> (10 + (i - 1) * 9)) & 0x000001FF
            return 3
        elif numIdx == 14:
            out[outOffset] = value & 0x00003FFF
            out[outOffset + 1] = (value >> 14) & 0x00003FFF
            return 2
        elif numIdx == 15:
            out[outOffset] = value & 0x0FFFFFFF
            return 1
        else:
            return -1

    @staticmethod
    def _s16DecompressWithIntBufferIntegratedBackup(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        j = 0
        shift = 0
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE
        num = min(Simple16WithHardCodes.__S16_NUM[numIdx], n)

        for j in range(num):
            s16Bits = Simple16WithHardCodes.__S16_BITS[numIdx][j]
            out[expPos[outOffset]] |= (
                (value >> shift) & (0xFFFFFFFF >> (32 - s16Bits))
            ) << oribits
            shift += s16Bits
            outOffset += 1

        return num

    @staticmethod
    def _s16DecompressWithIntBufferIntegrated2(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE
        return Simple16WithHardCodes._s16DecompressOneNumberWithHardCodesIntegrated(
            out, outOffset, value, numIdx, oribits, expPos
        )

    @staticmethod
    def _s16DecompressWithIntBufferIntegrated(
        out: typing.List[int],
        outOffset: int,
        value: int,
        n: int,
        expPos: typing.List[int],
        oribits: int,
    ) -> int:
        j = 0
        shift = 0
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE

        num = Simple16WithHardCodes.__S16_NUM[numIdx]
        while j < num:
            s16Bits = Simple16WithHardCodes.__S16_BITS[numIdx][j]
            out[expPos[outOffset + j]] |= (
                (value >> shift) & (0xFFFFFFFF >> (32 - s16Bits))
            ) << oribits
            shift += s16Bits
            j += 1
        return num

    @staticmethod
    def _s16DecompressWithIntBufferWithHardCodes(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE
        return Simple16WithHardCodes._s16DecompressOneNumberWithHardCodes(
            out, outOffset, value, numIdx
        )

    @staticmethod
    def _s16DecompressWithIntBuffer(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        j = 0
        shift = 0
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE

        num = Simple16WithHardCodes.__S16_NUM[numIdx]
        while j < num:
            s16Bits = Simple16WithHardCodes.__S16_BITS[numIdx][j]
            out[outOffset] = (value >> shift) & (0xFFFFFFFF >> (32 - s16Bits))
            outOffset += 1
            shift += s16Bits
            j += 1
        return num

    @staticmethod
    def _s16DecompressWithIntBufferBackup(
        out: typing.List[int], outOffset: int, value: int, n: int
    ) -> int:
        j = 0
        shift = 0
        numIdx = value >> Simple16WithHardCodes.__S16_BITSSIZE
        num = min(Simple16WithHardCodes.__S16_NUM[numIdx], n)

        while j < num:
            s16Bits = Simple16WithHardCodes.__S16_BITS[numIdx][j]
            out[outOffset] = (value >> shift) & (0xFFFFFFFF >> (32 - s16Bits))
            outOffset += 1
            shift += s16Bits
            j += 1

        return num

    @staticmethod
    def _s16Decompress(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
    ) -> int:
        numIdx = in_[inOffset] >> Simple16WithHardCodes.__S16_BITSSIZE
        num = min(Simple16WithHardCodes.__S16_NUM[numIdx], n)
        bits = 0

        for j in range(num):
            out[outOffset + j] = Simple16WithHardCodes.__readBitsForS16(
                in_, inOffset, bits, Simple16WithHardCodes.__S16_BITS[numIdx][j]
            )
            bits += Simple16WithHardCodes.__S16_BITS[numIdx][j]

        return num

    @staticmethod
    def _s16CompressBackup(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
        blockSize: int,
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
    ) -> int:
        for numIdx in range(Simple16WithHardCodes.__S16_NUMSIZE):
            out[outOffset] = numIdx << Simple16WithHardCodes.__S16_BITSSIZE
            num = min(Simple16WithHardCodes.__S16_NUM[numIdx], n)

            j, bits = 0, 0
            while j < num and in_[inOffset + j] < (
                1 << Simple16WithHardCodes.__S16_BITS[numIdx][j]
            ):
                out[outOffset] |= in_[inOffset + j] << bits
                bits += Simple16WithHardCodes.__S16_BITS[numIdx][j]
                j += 1

            if j == num:
                return num

        return -1

    @staticmethod
    def s16Compress(
        out: typing.List[int],
        outOffset: int,
        in_: typing.List[int],
        inOffset: int,
        n: int,
        blockSize: int,
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
    ) -> int:
        for numIdx in range(Simple16WithHardCodes.__S16_NUMSIZE):
            out[outOffset] = numIdx << Simple16WithHardCodes.__S16_BITSSIZE

            if Simple16WithHardCodes.__S16_NUM[numIdx] > n:
                continue
            num = Simple16WithHardCodes.__S16_NUM[numIdx]

            j = 0
            bits = 0
            while j < num and in_[inOffset + j] < (
                1 << Simple16WithHardCodes.__S16_BITS[numIdx][j]
            ):
                out[outOffset] |= in_[inOffset + j] << bits
                bits += Simple16WithHardCodes.__S16_BITS[numIdx][j]
                j += 1

            if j == num:
                return num

        return -1

    @staticmethod
    def __readBitsForS16(
        in_: typing.List[int], inIntOffset: int, inWithIntOffset: int, bits: int
    ) -> int:
        val = in_[inIntOffset] >> inWithIntOffset
        return val & (0xFFFFFFFF >> (32 - bits))
