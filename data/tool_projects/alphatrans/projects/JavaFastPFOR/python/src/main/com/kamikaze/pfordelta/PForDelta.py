from __future__ import annotations
import re
import os
import io
import numbers
import typing
from typing import *
from src.main.com.kamikaze.pfordelta.PForDeltaUnpack128 import *
from src.main.com.kamikaze.pfordelta.Simple16 import *


class PForDelta:

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
    __HEADER_SIZE: int = 32 * 2
    __HEADER_NUM: int = 2
    __MAX_BITS: int = 32
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
    def readBits(in_: typing.List[int], inOffset: int, bits: int) -> int:
        index = inOffset >> 5
        skip = inOffset & 0x1F
        val = in_[index] >> skip
        if 32 - skip < bits:
            val |= in_[index + 1] << (32 - skip)
        return val & (0xFFFFFFFF >> (32 - bits))

    @staticmethod
    def decompressBBitSlotsWithHardCodes(
        decompressedSlots: typing.List[int],
        compBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        compressedBitSize = 0
        PForDeltaUnpack128._unpack(decompressedSlots, compBlock, bits)
        compressedBitSize = bits * blockSize
        return compressedBitSize

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
    def decompressBBitSlots(
        outDecompSlots: typing.List[int],
        inCompBlock: typing.List[int],
        blockSize: int,
        bits: int,
    ) -> int:
        compressedBitSize = 0
        offset = PForDelta.__HEADER_SIZE
        for i in range(blockSize):
            outDecompSlots[i] = PForDelta.readBits(inCompBlock, offset, bits)
            offset += bits
        compressedBitSize = bits * blockSize

        return compressedBitSize

    @staticmethod
    def compressOneBlock(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> typing.List[int]:
        expAux = [0] * (blockSize * 2)

        maxCompBitSize = (
            PForDelta.__HEADER_SIZE
            + blockSize
            * (PForDelta.__MAX_BITS + PForDelta.__MAX_BITS + PForDelta.__MAX_BITS)
            + 32
        )
        tmpCompressedBlock = [0] * (maxCompBitSize >> 5)

        outputOffset = PForDelta.__HEADER_SIZE
        expUpperBound = 1 << bits
        expNum = 0

        for elem in inputBlock:
            if elem >= expUpperBound:
                expNum += 1

        expIndex = 0
        # Compress the b-bit slots
        for i in range(blockSize):
            if inputBlock[i] < expUpperBound:
                PForDelta.writeBits(
                    tmpCompressedBlock, inputBlock[i], outputOffset, bits
                )
            else:  # Exception
                # Store the lower bits of the exception
                PForDelta.writeBits(
                    tmpCompressedBlock,
                    inputBlock[i] & PForDelta.__MASK[bits],
                    outputOffset,
                    bits,
                )
                # Write the position of the exception
                expAux[expIndex] = i
                # Write the higher bits of the exception
                expAux[expIndex + expNum] = (inputBlock[i] >> bits) & PForDelta.__MASK[
                    32 - bits
                ]
                expIndex += 1
            outputOffset += bits

        # The first int in the compressed block stores the value of b and the number of exceptions
        tmpCompressedBlock[0] = ((bits & PForDelta.__MASK[10]) << 10) | (expNum & 0x3FF)
        tmpCompressedBlock[1] = inputBlock[blockSize - 1]

        # Compress exceptions
        if expNum > 0:
            compressedBitSize = PForDelta.__compressBlockByS16(
                tmpCompressedBlock, outputOffset, expAux, expNum * 2
            )
            outputOffset += compressedBitSize

        # Discard the redundant parts in the tmpCompressedBlock
        compressedSizeInInts = (outputOffset + 31) >> 5
        compBlock = [0] * compressedSizeInInts
        compBlock[:compressedSizeInInts] = tmpCompressedBlock[:compressedSizeInInts]

        return compBlock

    @staticmethod
    def checkBigNumbers(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> bool:
        maxNoExp = (1 << bits) - 1
        for i in range(blockSize):
            if inputBlock[i] > maxNoExp:
                return True
        return False

    @staticmethod
    def estimateCompressedSize(
        inputBlock: typing.List[int], bits: int, blockSize: int
    ) -> int:
        maxNoExp = (1 << bits) - 1
        # Size of the header and the bits-bit slots
        outputOffset = PForDelta.__HEADER_SIZE + bits * blockSize
        expNum = 0

        for i in range(blockSize):
            if inputBlock[i] > maxNoExp:
                expNum += 1

        outputOffset += expNum << 5

        return outputOffset

    @staticmethod
    def decompressOneBlock(
        outBlock: typing.List[int], inBlock: typing.List[int], blockSize: int
    ) -> int:
        expAux = [0] * (blockSize * 2)

        expNum = inBlock[0] & 0x3FF
        bits = (inBlock[0] >> 10) & 0x1F

        # Decompress the b-bit slots
        offset = PForDelta.__HEADER_SIZE
        compressedBits = 0
        if bits == 0:
            outBlock[:] = [0] * blockSize
        else:
            compressedBits = PForDelta.decompressBBitSlots(
                outBlock, inBlock, blockSize, bits
            )
        offset += compressedBits

        # Decompress exceptions
        if expNum > 0:
            compressedBits = PForDelta.decompressBlockByS16(
                expAux, inBlock, offset, expNum * 2
            )
            offset += compressedBits

            for i in range(expNum):
                curExpPos = expAux[i]
                curHighBits = expAux[i + expNum]
                outBlock[curExpPos] = (outBlock[curExpPos] & PForDelta.__MASK[bits]) | (
                    (curHighBits & PForDelta.__MASK[32 - bits]) << bits
                )

        return offset

    @staticmethod
    def compressOneBlockOpt(
        inBlock: typing.List[int], blockSize: int
    ) -> typing.List[int]:
        # Find the best b that may lead to the smallest overall compressed size
        currentB = PForDelta.__POSSIBLE_B[0]
        outBlock = None
        tmpB = currentB

        # Deal with the large exception cases
        hasBigNum = PForDelta.checkBigNumbers(
            inBlock, PForDelta.__POSSIBLE_B[-1], blockSize
        )
        if hasBigNum:
            currentB = 4
            print(f"has big num and the currentB is: {currentB}")
        else:
            optSize = PForDelta.estimateCompressedSize(inBlock, tmpB, blockSize)
            for i in range(1, len(PForDelta.__POSSIBLE_B)):
                tmpB = PForDelta.__POSSIBLE_B[i]
                curSize = PForDelta.estimateCompressedSize(inBlock, tmpB, blockSize)
                if curSize < optSize:
                    currentB = tmpB
                    optSize = curSize

        # Compress the block using the above best b
        outBlock = PForDelta.compressOneBlock(inBlock, currentB, blockSize)

        return outBlock

    @staticmethod
    def __compressBlockByS16(
        outCompBlock: typing.List[int],
        outStartOffsetInBits: int,
        inBlock: typing.List[int],
        blockSize: int,
    ) -> int:
        outOffset = (outStartOffsetInBits + 31) >> 5
        inOffset = 0
        numLeft = blockSize

        while numLeft > 0:
            num = Simple16.s16Compress(
                outCompBlock, outOffset, inBlock, inOffset, numLeft, blockSize
            )
            outOffset += 1
            inOffset += num
            numLeft -= num

        compressedBitSize = (outOffset << 5) - outStartOffsetInBits
        return compressedBitSize
