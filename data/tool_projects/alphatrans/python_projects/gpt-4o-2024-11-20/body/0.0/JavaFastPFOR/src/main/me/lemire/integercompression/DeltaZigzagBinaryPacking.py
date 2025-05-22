from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.DeltaZigzagEncoding import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.Util import *


class DeltaZigzagBinaryPacking(IntegerCODEC):

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

        ctx = DeltaZigzagEncoding.Decoder(0)
        work = [0] * self.__BLOCK_LENGTH

        ip = inPos.get()
        op = outPos.get()
        outPosLast = op + outLen

        while op < outPosLast:
            n = inBuf[ip]
            ip += 1

            ip += self.__unpack(inBuf, ip, work, 0, (n >> 24) & 0x3F)
            ip += self.__unpack(inBuf, ip, work, 32, (n >> 16) & 0x3F)
            ip += self.__unpack(inBuf, ip, work, 64, (n >> 8) & 0x3F)
            ip += self.__unpack(inBuf, ip, work, 96, (n >> 0) & 0x3F)

            ctx.decodeArray0(work, 0, self.__BLOCK_LENGTH, outBuf, op)
            op += self.__BLOCK_LENGTH

        outPos.add(outLen)
        inPos.set(ip)

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

        ctx = DeltaZigzagEncoding.Encoder(0)
        work = [0] * self.__BLOCK_LENGTH

        op = outPos.get()
        ip = inPos.get()
        inPosLast = ip + inLen

        while ip < inPosLast:
            ctx.encodeArray1(inBuf, ip, self.__BLOCK_LENGTH, work)
            bits1 = Util._maxbits32(work, 0)
            bits2 = Util._maxbits32(work, 32)
            bits3 = Util._maxbits32(work, 64)
            bits4 = Util._maxbits32(work, 96)
            outBuf[op] = (bits1 << 24) | (bits2 << 16) | (bits3 << 8) | bits4
            op += 1
            op += self.__pack(work, 0, outBuf, op, bits1)
            op += self.__pack(work, 32, outBuf, op, bits2)
            op += self.__pack(work, 64, outBuf, op, bits3)
            op += self.__pack(work, 96, outBuf, op, bits4)
            ip += self.__BLOCK_LENGTH

        inPos.add(inLen)
        outPos.set_(op)

    @staticmethod
    def __unpack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
    ) -> int:
        BitPacking.fastunpack(inBuf, inOff, outBuf, outOff, validBits)
        return validBits

    @staticmethod
    def __pack(
        inBuf: typing.List[int],
        inOff: int,
        outBuf: typing.List[int],
        outOff: int,
        validBits: int,
    ) -> int:
        BitPacking.fastpackwithoutmask(inBuf, inOff, outBuf, outOff, validBits)
        return validBits
