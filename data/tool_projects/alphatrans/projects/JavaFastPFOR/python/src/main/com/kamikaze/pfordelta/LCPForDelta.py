from __future__ import annotations
import time
import re
import io
import numbers
import typing
from typing import *
import os
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128 import *
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer import *
from src.main.com.kamikaze.pfordelta.Simple16 import *
from src.main.com.kamikaze.pfordelta.Simple16WithHardCodes import *


class LCPForDelta:

    __compBuffer: typing.List[int] = None

    __MASK: typing.List[int] = [
        0x00000000,
        0x00000001,
        0x00000003,
        0x00000007,
        0x0000000F,
        0x0000001F,
        0x0000003F,
        0x0000007F,
        0x000000FF,
        0x000001FF,
        0x000003FF,
        0x000007FF,
        0x00000FFF,
        0x00001FFF,
        0x00003FFF,
        0x00007FFF,
        0x0000FFFF,
        0x0001FFFF,
        0x0003FFFF,
        0x0007FFFF,
        0x000FFFFF,
        0x001FFFFF,
        0x003FFFFF,
        0x007FFFFF,
        0x00FFFFFF,
        0x01FFFFFF,
        0x03FFFFFF,
        0x07FFFFFF,
        0x0FFFFFFF,
        0x1FFFFFFF,
        0x3FFFFFFF,
        0x7FFFFFFF,
        0xFFFFFFFF,
    ]
    __HEADER_SIZE: int = 32 * 1
    __HEADER_NUM: int = 1
    __MAX_BITS: int = 32
    __POSSIBLE_B_BITS: int = 5
    __POSSIBLE_B: typing.List[int] = [
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
        16,
        20,
        28,
    ]

    @staticmethod
    def _readBitsWithBuffer(in_: typing.List[int], inOffset: int, bits: int) -> int:
        index = inOffset >> 5
        skip = inOffset & 0x1F
        val = in_[index] >> skip
        if 32 - skip < bits:
            val |= in_[index + 1] << (32 - skip)
        return val & (0xFFFFFFFF >> (32 - bits))

    @staticmethod
    def readBits(in_: typing.List[int], inOffset: int, bits: int) -> int:
        index = inOffset >> 5
        skip = inOffset & 0x1F
        val = in_[index] >> skip
        if 32 - skip < bits:
            val |= in_[index + 1] << (32 - skip)
        return val & (0xFFFFFFFF >> (32 - bits))

    @staticmethod
    def writeBits(out: typing.List[int], val: int, outOffset: int, bits: int) -> None:
        if bits == 0:
            return
        index = outOffset >> 5
        skip = outOffset & 0x1F
        val &= 0xFFFFFFFF >> (32 - bits)
        out[index] |= val << skip
        if 32 - skip < bits:
            out[index + 1] |= val >> (32 - skip)

    @staticmethod
    def _decompressBlockByS16WithIntBufferIntegrated(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        expPosBuffer: typing.List[int],
        oribits: int,
    ) -> None:
        outOffset = 0
        numLeft = blockSize

        while numLeft > 0:
            num = Simple16WithHardCodes._s16DecompressWithIntBufferIntegrated(
                outDecompBlock,
                outOffset,
                inCompBlock.pop(0),
                numLeft,
                expPosBuffer,
                oribits,
            )
            outOffset += num
            numLeft -= num

    @staticmethod
    def _decompressBlockByS16WithIntBuffer(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
    ) -> None:
        outOffset = 0
        numLeft = blockSize
        while numLeft > 0:
            # Retrieve the next compressed value from inCompBlock
            value = inCompBlock.pop(0)  # Assuming inCompBlock behaves like a queue
            # Decompress the value and get the number of decompressed integers
            num = Simple16WithHardCodes._s16DecompressWithIntBuffer(
                outDecompBlock, outOffset, value, numLeft
            )
            # Update the offset and remaining count
            outOffset += num
            numLeft -= num

    @staticmethod
    def decompressBlockByS16(
        outDecompBlock: typing.List[int],
        inCompBlock: typing.List[int],
        inStartOffsetInBits: int,
        blockSize: int,
    ) -> int:
        inOffset = (inStartOffsetInBits + 31) >> 5
        outOffset = 0
        numLeft = blockSize

        while numLeft > 0:
            num = Simple16.s16Decompress(
                outDecompBlock, outOffset, inCompBlock, inOffset, numLeft
            )
            outOffset += num
            inOffset += 1
            numLeft -= num

        compressedBitSize = (inOffset << 5) - inStartOffsetInBits
        return compressedBitSize

    @staticmethod
    def _decompressBBitSlotsWithHardCodesWithIntBuffer(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        bits: int,
    ) -> int:
        PForDeltaUnpack128WIthIntBuffer._unpack(outDecompSlots, inCompBlock, bits)
        return bits * blockSize

    @staticmethod
    def _decompressBBitSlotsWithHardCodes(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        compressedBitSize = 0
        PForDeltaUnpack128._unpack(outDecompSlots, inCompBlock, bits)
        compressedBitSize = bits * blockSize
        return compressedBitSize

    @staticmethod
    def decompressBBitSlots(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        compressedBitSize = 0
        offset = LCPForDelta.__HEADER_SIZE
        for i in range(blockSize):
            outDecompSlots[i] = LCPForDelta.readBits(inCompBlock, offset, bits)
            offset += bits
        compressedBitSize = bits * blockSize
        return compressedBitSize

    @staticmethod
    def checkBigNumbers(
        inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> bool:
        maxNoExp = (1 << bits) - 1
        for i in range(blockSize):
            if inputBlock[i] > maxNoExp:
                return True
        return False

    @staticmethod
    def estimateCompressedSize(
        inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        maxNoExp = (1 << bits) - 1
        # Size of the header and the bits-bit slots
        outputOffset = LCPForDelta.__HEADER_SIZE + bits * blockSize
        expNum = 0

        for i in range(blockSize):
            if inputBlock[i] > maxNoExp:
                expNum += 1

        outputOffset += expNum << 5

        return outputOffset

    @staticmethod
    def _decompressOneBlockWithSizeWithIntBuffer(
        decompBlock: typing.List[int],
        inBlock: typing.Union[array.array, typing.List[int]],
        blockSize: int,
        expPosBuffer: typing.List[int],
        expHighBitsBuffer: typing.List[int],
        inBlockLen: int,
    ) -> None:
        flag = inBlock.pop(0)  # Simulating `inBlock.get()` by popping the first element
        expNum = flag & LCPForDelta.__MASK[31 - LCPForDelta.__POSSIBLE_B_BITS]
        bits = (flag >> (31 - LCPForDelta.__POSSIBLE_B_BITS)) & 0x1F

        if bits == 0:
            decompBlock[:inBlockLen] = [0] * inBlockLen
        else:
            PForDeltaUnpack128WIthIntBuffer._unpack(decompBlock, inBlock, bits)

        if expNum > 0:
            # Decompress expPos
            num = 0
            outOffset = 0
            numLeft = expNum
            while numLeft > 0:
                num = Simple16WithHardCodes._s16DecompressWithIntBufferWithHardCodes(
                    expPosBuffer, outOffset, inBlock.pop(0), numLeft
                )
                outOffset += num
                numLeft -= num

            # Decompress expHighBits and decompBlock at the same time
            outOffset = 0
            numLeft = expNum
            while numLeft > 0:
                num = Simple16WithHardCodes._s16DecompressWithIntBufferIntegrated2(
                    decompBlock, outOffset, inBlock.pop(0), numLeft, expPosBuffer, bits
                )
                outOffset += num
                numLeft -= num

    @staticmethod
    def _decompressOneBlockWithSize(
        decompBlock: typing.List[int],
        inBlock: typing.List[int],
        blockSize: int,
        expPosBuffer: typing.List[int],
        expHighBitsBuffer: typing.List[int],
        inBlockLen: int,
    ) -> None:
        expNum = inBlock[0] & LCPForDelta.__MASK[31 - LCPForDelta.__POSSIBLE_B_BITS]
        bits = (inBlock[0] >> (31 - LCPForDelta.__POSSIBLE_B_BITS)) & 0x1F

        # Decompress the b-bit slots
        offset = LCPForDelta.__HEADER_SIZE
        compressedBits = 0
        if bits == 0:
            for i in range(inBlockLen):
                decompBlock[i] = 0
        else:
            compressedBits = LCPForDelta.decompressBBitSlots(
                decompBlock, inBlock, blockSize, bits
            )
        offset += compressedBits

        # Decompress exceptions
        if expNum > 0:
            compressedBits = LCPForDelta.decompressBlockByS16(
                expPosBuffer, inBlock, offset, expNum
            )
            offset += compressedBits
            compressedBits = LCPForDelta.decompressBlockByS16(
                expHighBitsBuffer, inBlock, offset, expNum
            )
            offset += compressedBits

            for i in range(expNum):
                curExpPos = expPosBuffer[i]
                curHighBits = expHighBitsBuffer[i]
                decompBlock[curExpPos] = (
                    decompBlock[curExpPos] & LCPForDelta.__MASK[bits]
                ) | ((curHighBits & LCPForDelta.__MASK[32 - bits]) << bits)

    @staticmethod
    def decompressOneBlock(
        decompBlock: typing.List[int], inBlock: typing.List[int], blockSize: int
    ) -> None:
        expNum = inBlock[0] & LCPForDelta.__MASK[31 - LCPForDelta.__POSSIBLE_B_BITS]
        bits = (inBlock[0] >> (31 - LCPForDelta.__POSSIBLE_B_BITS)) & 0x1F

        expPosBuffer = [0] * blockSize
        expHighBitsBuffer = [0] * blockSize

        # Decompress the b-bit slots
        offset = LCPForDelta.__HEADER_SIZE
        compressedBits = 0
        if bits == 0:
            decompBlock[:] = [0] * blockSize
        else:
            compressedBits = LCPForDelta.decompressBBitSlots(
                decompBlock, inBlock, blockSize, bits
            )
        offset += compressedBits

        # Decompress exceptions
        if expNum > 0:
            compressedBits = LCPForDelta.decompressBlockByS16(
                expPosBuffer, inBlock, offset, expNum
            )
            offset += compressedBits
            compressedBits = LCPForDelta.decompressBlockByS16(
                expHighBitsBuffer, inBlock, offset, expNum
            )
            offset += compressedBits

            for i in range(expNum):
                curExpPos = expPosBuffer[i]
                curHighBits = expHighBitsBuffer[i]
                decompBlock[curExpPos] = (
                    decompBlock[curExpPos] & LCPForDelta.__MASK[bits]
                ) | ((curHighBits & LCPForDelta.__MASK[32 - bits]) << bits)

    def _compressOneBlockCore2(
        self, inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        outputOffset = self.__HEADER_SIZE
        expUpperBound = 1 << bits
        expNum = 0
        maxCompBitSize = (
            self.__HEADER_SIZE
            + blockSize * (self.__MAX_BITS + self.__MAX_BITS + self.__MAX_BITS)
            + 32
        )
        tmpCompBuffer = [0] * (maxCompBitSize >> 5)

        expPosBuffer = [0] * blockSize
        expHighBitsBuffer = [0] * blockSize

        # Compress the b-bit slots
        for i in range(blockSize):
            value = inputBlock[i]
            if value < expUpperBound:
                self.writeBits(tmpCompBuffer, value, outputOffset, bits)
            else:  # Exception
                # Store the lower bits of the exception
                self.writeBits(
                    tmpCompBuffer, value & self.__MASK[bits], outputOffset, bits
                )
                # Write the position of the exception
                expPosBuffer[expNum] = i
                # Write the higher bits of the exception
                expHighBitsBuffer[expNum] = (value >> bits) & self.__MASK[32 - bits]
                expNum += 1
            outputOffset += bits

        tmpCompBuffer[0] = (
            (bits & self.__MASK[self.__POSSIBLE_B_BITS])
            << (31 - self.__POSSIBLE_B_BITS)
        ) | (expNum & self.__MASK[31 - self.__POSSIBLE_B_BITS])

        # Compress exceptions
        if expNum > 0:
            expBuffer = [0] * (expNum * 2)
            expBuffer[:expNum] = expPosBuffer[:expNum]
            expBuffer[expNum : 2 * expNum] = expHighBitsBuffer[:expNum]

            compressedBitSize = self.__compressBlockByS16(
                tmpCompBuffer,
                outputOffset,
                expBuffer,
                expNum * 2,
                blockSize,
                inputBlock,
            )
            outputOffset += compressedBitSize

        # Discard the redundant parts in the tmpCompressedBlock
        compressedSizeInInts = (outputOffset + 31) >> 5

        self.__compBuffer = tmpCompBuffer
        return compressedSizeInInts

    def compressOneBlockCore(
        self, inputBlock: typing.List[int], blockSize: int, bits: int
    ) -> int:
        outputOffset = self.__HEADER_SIZE
        expUpperBound = 1 << bits
        expNum = 0
        maxCompBitSize = (
            self.__HEADER_SIZE
            + blockSize * (self.__MAX_BITS + self.__MAX_BITS + self.__MAX_BITS)
            + 32
        )
        tmpCompBuffer = [0] * (maxCompBitSize >> 5)

        expPosBuffer = [0] * blockSize
        expHighBitsBuffer = [0] * blockSize

        # Compress the b-bit slots
        for i in range(blockSize):
            value = inputBlock[i]
            if value < expUpperBound:
                self.writeBits(tmpCompBuffer, value, outputOffset, bits)
            else:  # Exception
                # Store the lower bits of the exception
                self.writeBits(
                    tmpCompBuffer, value & self.__MASK[bits], outputOffset, bits
                )
                # Write the position of the exception
                expPosBuffer[expNum] = i
                # Write the higher bits of the exception
                expHighBitsBuffer[expNum] = (value >> bits) & self.__MASK[32 - bits]
                expNum += 1
            outputOffset += bits

        tmpCompBuffer[0] = (
            (bits & self.__MASK[self.__POSSIBLE_B_BITS])
            << (31 - self.__POSSIBLE_B_BITS)
        ) | (expNum & self.__MASK[31 - self.__POSSIBLE_B_BITS])

        # Compress exceptions
        if expNum > 0:
            compressedBitSize = self.__compressBlockByS16(
                tmpCompBuffer, outputOffset, expPosBuffer, expNum, blockSize, inputBlock
            )
            outputOffset += compressedBitSize

            compressedBitSize = self.__compressBlockByS16(
                tmpCompBuffer,
                outputOffset,
                expHighBitsBuffer,
                expNum,
                blockSize,
                inputBlock,
            )
            outputOffset += compressedBitSize

        # Discard the redundant parts in the tmpCompressedBlock
        compressedSizeInInts = (outputOffset + 31) >> 5

        self.__compBuffer = tmpCompBuffer
        return compressedSizeInInts

    def compress(self, inBlock: typing.List[int], blockSize: int) -> int:
        # Find the best b that can lead to the smallest overall compressed size
        currentB = self.__POSSIBLE_B[0]
        tmpB = currentB
        hasBigNum = self.checkBigNumbers(inBlock, blockSize, self.__POSSIBLE_B[-1])

        if hasBigNum:
            currentB = 4
        else:
            optSize = self.estimateCompressedSize(inBlock, blockSize, tmpB)
            for i in range(1, len(self.__POSSIBLE_B)):
                tmpB = self.__POSSIBLE_B[i]
                curSize = self.estimateCompressedSize(inBlock, blockSize, tmpB)
                if curSize < optSize:
                    currentB = tmpB
                    optSize = curSize

        # Compress the block using the above best b
        compressedSizeInInts = self.compressOneBlockCore(inBlock, blockSize, currentB)

        return compressedSizeInInts

    def _setCompBuffer(self, buffer: typing.List[int]) -> None:
        self.__compBuffer = buffer

    def _getCompBuffer(self) -> typing.List[int]:
        return self.__compBuffer

    @staticmethod
    def __compressBlockByS16(
        outCompBlock: typing.List[int],
        outStartOffsetInBits: int,
        inBlock: typing.List[int],
        blockSize: int,
        oriBlockSize: int,
        oriInputBlock: typing.List[int],
    ) -> int:
        outOffset = (outStartOffsetInBits + 31) >> 5
        inOffset = 0
        numLeft = blockSize

        while numLeft > 0:
            num = Simple16WithHardCodes.s16Compress(
                outCompBlock,
                outOffset,
                inBlock,
                inOffset,
                numLeft,
                blockSize,
                oriBlockSize,
                oriInputBlock,
            )
            outOffset += 1
            inOffset += num
            numLeft -= num

        compressedBitSize = (outOffset << 5) - outStartOffsetInBits
        return compressedBitSize
