from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *


class XorBinaryPacking(IntegratedIntegerCODEC):

    __BLOCK_LENGTH: int = 128

    def toString(self) -> str:
        return self.__class__.__name__

    def uncompress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        if inLen == 0:
            return

        outLen = inBuf[inPos.get()]
        inPos.increment()

        context = 0
        work = [0] * 32

        ip = inPos.get()
        op = outPos.get()
        outPosLast = op + outLen

        while op < outPosLast:
            bits1 = (inBuf[ip] >> 24) & 0xFF
            bits2 = (inBuf[ip] >> 16) & 0xFF
            bits3 = (inBuf[ip] >> 8) & 0xFF
            bits4 = inBuf[ip] & 0xFF
            ip += 1

            ip += self.__xorUnpack(inBuf, ip, outBuf, op, bits1, context, work)
            ip += self.__xorUnpack(
                inBuf,
                ip,
                outBuf,
                op + 32,
                bits2,
                outBuf[op + 31] if op + 31 < len(outBuf) else 0,
                work,
            )
            ip += self.__xorUnpack(
                inBuf,
                ip,
                outBuf,
                op + 64,
                bits3,
                outBuf[op + 63] if op + 63 < len(outBuf) else 0,
                work,
            )
            ip += self.__xorUnpack(
                inBuf,
                ip,
                outBuf,
                op + 96,
                bits4,
                outBuf[op + 95] if op + 95 < len(outBuf) else 0,
                work,
            )

            context = outBuf[op + 127] if op + 127 < len(outBuf) else 0
            op += self.__BLOCK_LENGTH

        outPos.add(outLen)
        inPos.set_(ip)

    def compress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        inLen = inLen - inLen % self.__BLOCK_LENGTH
        if inLen == 0:
            return

        outBuf[outPos.get()] = inLen
        outPos.increment()

        context = 0
        work = [0] * 32

        op = outPos.get()
        ip = inPos.get()
        inPosLast = ip + inLen

        while ip < inPosLast:
            bits1 = self.__xorMaxBits(inBuf, ip + 0, 32, context)
            bits2 = self.__xorMaxBits(inBuf, ip + 32, 32, inBuf[ip + 31])
            bits3 = self.__xorMaxBits(inBuf, ip + 64, 32, inBuf[ip + 63])
            bits4 = self.__xorMaxBits(inBuf, ip + 96, 32, inBuf[ip + 95])

            outBuf[op] = (bits1 << 24) | (bits2 << 16) | (bits3 << 8) | (bits4 << 0)
            op += 1

            op += self.__xorPack(inBuf, ip + 0, outBuf, op, bits1, context, work)
            op += self.__xorPack(
                inBuf, ip + 32, outBuf, op, bits2, inBuf[ip + 31], work
            )
            op += self.__xorPack(
                inBuf, ip + 64, outBuf, op, bits3, inBuf[ip + 63], work
            )
            op += self.__xorPack(
                inBuf, ip + 96, outBuf, op, bits4, inBuf[ip + 95], work
            )

            context = inBuf[ip + 127]
            ip += self.__BLOCK_LENGTH

        inPos.add(inLen)
        outPos.set_(op)

    @staticmethod
    def __xorUnpack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
        context: int,
        work: typing.List[int],
    ) -> int:
        BitPacking.fastunpack(inBuf, inOff, work, 0, validBits)
        outBuf[outOff] = work[0] ^ context
        context = outBuf[outOff]
        for i in range(1, 32):
            outBuf[outOff + i] = work[i] ^ context
            context = outBuf[outOff + i]
        return validBits

    @staticmethod
    def __xorPack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
        context: int,
        work: typing.List[int],
    ) -> int:
        work[0] = inBuf[inOff] ^ context
        for i in range(1, 32):
            p = inOff + i
            work[i] = inBuf[p] ^ inBuf[p - 1]
        BitPacking.fastpackwithoutmask(work, 0, outBuf, outOff, validBits)
        return validBits

    @staticmethod
    def __xorMaxBits(
        buf: typing.List[int], offset: int, length: int, context: int
    ) -> int:
        mask = buf[offset] ^ context
        M = offset + length
        prev = offset
        for i in range(offset + 1, M):
            mask |= buf[i] ^ buf[prev]
            prev = i

        return 32 - (mask.bit_length() if mask != 0 else 0)
