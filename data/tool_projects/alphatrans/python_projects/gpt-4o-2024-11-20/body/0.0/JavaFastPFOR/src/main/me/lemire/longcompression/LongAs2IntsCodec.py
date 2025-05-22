from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.longcompression.LongCODEC import *
from src.main.me.lemire.longcompression.RoaringIntPacking import *


class LongAs2IntsCodec(LongCODEC):

    lowPartsCodec: IntegerCODEC = None

    highPartsCodec: IntegerCODEC = None

    def uncompress1(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return

        long_index = inpos.get()

        nb_compressed_high_parts = RoaringIntPacking.high(in_[long_index])
        compressed_high_parts = [0] * nb_compressed_high_parts

        high_part = False
        for i in range(nb_compressed_high_parts):
            if high_part:
                next_int = RoaringIntPacking.high(in_[long_index + (i + 1) // 2])
            else:
                next_int = RoaringIntPacking.low(in_[long_index + (i + 1) // 2])
            compressed_high_parts[i] = next_int

            high_part = not high_part

        buffer = [0] * (inlength * 16)

        high_parts_out_position = IntWrapper.IntWrapper1()
        self.highPartsCodec.uncompress0(
            compressed_high_parts,
            IntWrapper.IntWrapper1(),
            len(compressed_high_parts),
            buffer,
            high_parts_out_position,
        )
        high_parts = buffer[: high_parts_out_position.get()]

        int_index_nb_compressed_low_parts = (
            long_index * 2 + 1 + nb_compressed_high_parts
        )
        if high_part:
            nb_compressed_low_parts = RoaringIntPacking.high(
                in_[int_index_nb_compressed_low_parts // 2]
            )
        else:
            nb_compressed_low_parts = RoaringIntPacking.low(
                in_[int_index_nb_compressed_low_parts // 2]
            )
        high_part = not high_part

        compressed_low_parts = [0] * nb_compressed_low_parts
        for i in range(nb_compressed_low_parts):
            if high_part:
                next_int = RoaringIntPacking.high(
                    in_[(int_index_nb_compressed_low_parts + 1 + i) // 2]
                )
            else:
                next_int = RoaringIntPacking.low(
                    in_[(int_index_nb_compressed_low_parts + 1 + i) // 2]
                )
            compressed_low_parts[i] = next_int

            high_part = not high_part

        low_parts_out_position = IntWrapper.IntWrapper1()
        self.lowPartsCodec.uncompress0(
            compressed_low_parts,
            IntWrapper.IntWrapper1(),
            len(compressed_low_parts),
            buffer,
            low_parts_out_position,
        )
        low_parts = buffer[: low_parts_out_position.get()]
        assert len(high_parts) == len(low_parts)

        out_position = outpos.get()
        for i in range(len(high_parts)):
            out[out_position] = RoaringIntPacking.pack(high_parts[i], low_parts[i])
            out_position += 1

        inpos.add(inlength)
        outpos.set_(out_position)

    def compress0(
        self,
        in_: typing.List[int],
        inpos: IntWrapper,
        inlength: int,
        out: typing.List[int],
        outpos: IntWrapper,
    ) -> None:
        if inlength == 0:
            return

        highParts = [0] * inlength
        lowParts = [0] * inlength

        for i in range(inlength):
            inPosition = inpos.get() + i
            highParts[i] = RoaringIntPacking.high(in_[inPosition])
            lowParts[i] = RoaringIntPacking.low(in_[inPosition])

        buffer = [0] * (inlength * 16)

        outPosition = outpos.get()

        hasLeftover = False
        highPartsOutPosition = IntWrapper(1)
        self.highPartsCodec.compress0(
            highParts, inpos, inlength, buffer, highPartsOutPosition
        )

        buffer[0] = highPartsOutPosition.get() - 1

        for i in range(highPartsOutPosition.get() // 2):
            pack = RoaringIntPacking.pack(buffer[i * 2], buffer[i * 2 + 1])
            out[outPosition] = pack
            outPosition += 1

        if highPartsOutPosition.get() % 2 == 1:
            hasLeftover = True
            buffer[0] = buffer[highPartsOutPosition.get() - 1]
        else:
            hasLeftover = False

        lowPartsOutPosition = IntWrapper(1)
        if hasLeftover:
            lowPartsOutPosition.set_(2)

        self.lowPartsCodec.compress0(
            lowParts, IntWrapper(0), inlength, buffer, lowPartsOutPosition
        )

        buffer[1 if hasLeftover else 0] = lowPartsOutPosition.get() - (
            2 if hasLeftover else 1
        )

        for i in range(lowPartsOutPosition.get() // 2):
            pack = RoaringIntPacking.pack(buffer[i * 2], buffer[i * 2 + 1])
            out[outPosition] = pack
            outPosition += 1

        if lowPartsOutPosition.get() % 2 == 1:
            pack = RoaringIntPacking.pack(buffer[lowPartsOutPosition.get() - 1], 0)
            out[outPosition] = pack
            outPosition += 1

        inpos.add(inlength)
        outpos.set_(outPosition)

    @staticmethod
    def LongAs2IntsCodec1() -> LongAs2IntsCodec:
        return LongAs2IntsCodec(
            VariableByte(), Composition(BinaryPacking(), VariableByte())
        )

    def __init__(
        self, highPartsCodec: IntegerCODEC, lowPartsCodec: IntegerCODEC
    ) -> None:
        self.highPartsCodec = highPartsCodec
        self.lowPartsCodec = lowPartsCodec
