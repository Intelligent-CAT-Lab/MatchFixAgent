from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.DeltaZigzagEncoding import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *


class DeltaZigzagVariableByte(IntegerCODEC):

    def uncompress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        ctx = Decoder(0)

        ip = inPos.get()
        op = outPos.get()
        vbcNum = 0
        vbcShift = 24  # Variable Byte Context
        inPosLast = ip + inLen

        while ip < inPosLast:
            # Fetch a byte value
            n = (inBuf[ip] >> vbcShift) & 0xFF
            if vbcShift > 0:
                vbcShift -= 8
            else:
                vbcShift = 24
                ip += 1

            # Decode variable byte and delta+zigzag
            vbcNum = (vbcNum << 7) + (n & 0x7F)
            if (n & 0x80) == 0:
                outBuf[op] = ctx.decodeInt(vbcNum)
                op += 1
                vbcNum = 0

        outPos.set_(op)
        inPos.set_(inPosLast)

    def compress0(
        self,
        inBuf: typing.List[int],
        inPos: IntWrapper,
        inLen: int,
        outBuf: typing.List[int],
        outPos: IntWrapper,
    ) -> None:
        if inLen == 0:
            return

        # Create a buffer for encoding
        byteBuf = self._makeBuffer(inLen * 5 + 3)
        ctx = Encoder(0)

        # Delta+Zigzag+VariableByte encoding
        ip = inPos.get()
        inPosLast = ip + inLen
        byteBufPos = 0

        while ip < inPosLast:
            # Filter with delta+zigzag encoding
            n = ctx.encodeInt(inBuf[ip])
            ip += 1

            # Variable byte encoding
            if n >= (1 << 28):
                byteBuf[byteBufPos] = ((n >> 28) & 0x7F) | 0x80
                byteBufPos += 1
            if n >= (1 << 21):
                byteBuf[byteBufPos] = ((n >> 21) & 0x7F) | 0x80
                byteBufPos += 1
            if n >= (1 << 14):
                byteBuf[byteBufPos] = ((n >> 14) & 0x7F) | 0x80
                byteBufPos += 1
            if n >= (1 << 7):
                byteBuf[byteBufPos] = ((n >> 7) & 0x7F) | 0x80
                byteBufPos += 1
            byteBuf[byteBufPos] = n & 0x7F
            byteBufPos += 1

        # Padding buffer to make it compatible as IntBuffer
        padding = (4 - (byteBufPos % 4)) % 4
        for _ in range(padding):
            byteBuf[byteBufPos] = 0x80
            byteBufPos += 1

        # Convert byte buffer to int buffer
        outLen = byteBufPos // 4
        intBuf = memoryview(byteBuf).cast("I")  # Cast byte buffer to int buffer
        outBuf[outPos.get() : outPos.get() + outLen] = intBuf[:outLen]

        # Update positions
        inPos.add(inLen)
        outPos.add(outLen)

    def toString(self) -> str:
        return self.__class__.__name__

    def _makeBuffer(self, sizeInBytes: int) -> typing.Union[bytearray, memoryview]:
        return bytearray(sizeInBytes)
