from __future__ import annotations
import re
import enum
import io
import typing
from typing import *


class PForDeltaUnpack128WIthIntBuffer:

    @staticmethod
    def _unpack(
        out: typing.List[int],
        in_: typing.Union[array.array, typing.List[int]],
        bits: int,
    ) -> None:
        if bits == 0:
            PForDeltaUnpack128WIthIntBuffer.__unpack0(out, in_)
        elif bits == 1:
            PForDeltaUnpack128WIthIntBuffer.__unpack1(out, in_)
        elif bits == 2:
            PForDeltaUnpack128WIthIntBuffer.__unpack2(out, in_)
        elif bits == 3:
            PForDeltaUnpack128WIthIntBuffer.__unpack3(out, in_)
        elif bits == 4:
            PForDeltaUnpack128WIthIntBuffer.__unpack4(out, in_)
        elif bits == 5:
            PForDeltaUnpack128WIthIntBuffer.__unpack5(out, in_)
        elif bits == 6:
            PForDeltaUnpack128WIthIntBuffer.__unpack6(out, in_)
        elif bits == 7:
            PForDeltaUnpack128WIthIntBuffer.__unpack7(out, in_)
        elif bits == 8:
            PForDeltaUnpack128WIthIntBuffer.__unpack8(out, in_)
        elif bits == 9:
            PForDeltaUnpack128WIthIntBuffer.__unpack9(out, in_)
        elif bits == 10:
            PForDeltaUnpack128WIthIntBuffer.__unpack10(out, in_)
        elif bits == 11:
            PForDeltaUnpack128WIthIntBuffer.__unpack11(out, in_)
        elif bits == 12:
            PForDeltaUnpack128WIthIntBuffer.__unpack12(out, in_)
        elif bits == 13:
            PForDeltaUnpack128WIthIntBuffer.__unpack13(out, in_)
        elif bits == 16:
            PForDeltaUnpack128WIthIntBuffer.__unpack16(out, in_)
        elif bits == 20:
            PForDeltaUnpack128WIthIntBuffer.__unpack20(out, in_)
        elif bits == 28:
            PForDeltaUnpack128WIthIntBuffer.__unpack28(out, in_)
        else:
            # No action for unsupported bit values
            pass

    @staticmethod
    def __unpack28(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 268435455
        for _ in range(4):
            cur_input_values = [in_.pop(0) for _ in range(28)]

            out[0 + out_offset] = cur_input_values[0] & mask
            out[1 + out_offset] = (
                (cur_input_values[0] >> 28) | (cur_input_values[1] << 4)
            ) & mask
            out[2 + out_offset] = (
                (cur_input_values[1] >> 24) | (cur_input_values[2] << 8)
            ) & mask
            out[3 + out_offset] = (
                (cur_input_values[2] >> 20) | (cur_input_values[3] << 12)
            ) & mask
            out[4 + out_offset] = (
                (cur_input_values[3] >> 16) | (cur_input_values[4] << 16)
            ) & mask
            out[5 + out_offset] = (
                (cur_input_values[4] >> 12) | (cur_input_values[5] << 20)
            ) & mask
            out[6 + out_offset] = (
                (cur_input_values[5] >> 8) | (cur_input_values[6] << 24)
            ) & mask
            out[7 + out_offset] = cur_input_values[6] >> 4
            out[8 + out_offset] = cur_input_values[7] & mask
            out[9 + out_offset] = (
                (cur_input_values[7] >> 28) | (cur_input_values[8] << 4)
            ) & mask
            out[10 + out_offset] = (
                (cur_input_values[8] >> 24) | (cur_input_values[9] << 8)
            ) & mask
            out[11 + out_offset] = (
                (cur_input_values[9] >> 20) | (cur_input_values[10] << 12)
            ) & mask
            out[12 + out_offset] = (
                (cur_input_values[10] >> 16) | (cur_input_values[11] << 16)
            ) & mask
            out[13 + out_offset] = (
                (cur_input_values[11] >> 12) | (cur_input_values[12] << 20)
            ) & mask
            out[14 + out_offset] = (
                (cur_input_values[12] >> 8) | (cur_input_values[13] << 24)
            ) & mask
            out[15 + out_offset] = cur_input_values[13] >> 4
            out[16 + out_offset] = cur_input_values[14] & mask
            out[17 + out_offset] = (
                (cur_input_values[14] >> 28) | (cur_input_values[15] << 4)
            ) & mask
            out[18 + out_offset] = (
                (cur_input_values[15] >> 24) | (cur_input_values[16] << 8)
            ) & mask
            out[19 + out_offset] = (
                (cur_input_values[16] >> 20) | (cur_input_values[17] << 12)
            ) & mask
            out[20 + out_offset] = (
                (cur_input_values[17] >> 16) | (cur_input_values[18] << 16)
            ) & mask
            out[21 + out_offset] = (
                (cur_input_values[18] >> 12) | (cur_input_values[19] << 20)
            ) & mask
            out[22 + out_offset] = (
                (cur_input_values[19] >> 8) | (cur_input_values[20] << 24)
            ) & mask
            out[23 + out_offset] = cur_input_values[20] >> 4
            out[24 + out_offset] = cur_input_values[21] & mask
            out[25 + out_offset] = (
                (cur_input_values[21] >> 28) | (cur_input_values[22] << 4)
            ) & mask
            out[26 + out_offset] = (
                (cur_input_values[22] >> 24) | (cur_input_values[23] << 8)
            ) & mask
            out[27 + out_offset] = (
                (cur_input_values[23] >> 20) | (cur_input_values[24] << 12)
            ) & mask
            out[28 + out_offset] = (
                (cur_input_values[24] >> 16) | (cur_input_values[25] << 16)
            ) & mask
            out[29 + out_offset] = (
                (cur_input_values[25] >> 12) | (cur_input_values[26] << 20)
            ) & mask
            out[30 + out_offset] = (
                (cur_input_values[26] >> 8) | (cur_input_values[27] << 24)
            ) & mask
            out[31 + out_offset] = cur_input_values[27] >> 4

            out_offset += 32

    @staticmethod
    def __unpack20(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 1048575
        in_iter = iter(in_)  # Create an iterator for the input buffer
        for _ in range(4):
            cur_input_value = [
                next(in_iter) for _ in range(20)
            ]  # Read 20 values from the input buffer
            out[0 + out_offset] = cur_input_value[0] & mask
            out[1 + out_offset] = (
                (cur_input_value[0] >> 20) | (cur_input_value[1] << 12)
            ) & mask
            out[2 + out_offset] = (cur_input_value[1] >> 8) & mask
            out[3 + out_offset] = (
                (cur_input_value[1] >> 28) | (cur_input_value[2] << 4)
            ) & mask
            out[4 + out_offset] = (
                (cur_input_value[2] >> 16) | (cur_input_value[3] << 16)
            ) & mask
            out[5 + out_offset] = (cur_input_value[3] >> 4) & mask
            out[6 + out_offset] = (
                (cur_input_value[3] >> 24) | (cur_input_value[4] << 8)
            ) & mask
            out[7 + out_offset] = cur_input_value[4] >> 12
            out[8 + out_offset] = cur_input_value[5] & mask
            out[9 + out_offset] = (
                (cur_input_value[5] >> 20) | (cur_input_value[6] << 12)
            ) & mask
            out[10 + out_offset] = (cur_input_value[6] >> 8) & mask
            out[11 + out_offset] = (
                (cur_input_value[6] >> 28) | (cur_input_value[7] << 4)
            ) & mask
            out[12 + out_offset] = (
                (cur_input_value[7] >> 16) | (cur_input_value[8] << 16)
            ) & mask
            out[13 + out_offset] = (cur_input_value[8] >> 4) & mask
            out[14 + out_offset] = (
                (cur_input_value[8] >> 24) | (cur_input_value[9] << 8)
            ) & mask
            out[15 + out_offset] = cur_input_value[9] >> 12
            out[16 + out_offset] = cur_input_value[10] & mask
            out[17 + out_offset] = (
                (cur_input_value[10] >> 20) | (cur_input_value[11] << 12)
            ) & mask
            out[18 + out_offset] = (cur_input_value[11] >> 8) & mask
            out[19 + out_offset] = (
                (cur_input_value[11] >> 28) | (cur_input_value[12] << 4)
            ) & mask
            out[20 + out_offset] = (
                (cur_input_value[12] >> 16) | (cur_input_value[13] << 16)
            ) & mask
            out[21 + out_offset] = (cur_input_value[13] >> 4) & mask
            out[22 + out_offset] = (
                (cur_input_value[13] >> 24) | (cur_input_value[14] << 8)
            ) & mask
            out[23 + out_offset] = cur_input_value[14] >> 12
            out[24 + out_offset] = cur_input_value[15] & mask
            out[25 + out_offset] = (
                (cur_input_value[15] >> 20) | (cur_input_value[16] << 12)
            ) & mask
            out[26 + out_offset] = (cur_input_value[16] >> 8) & mask
            out[27 + out_offset] = (
                (cur_input_value[16] >> 28) | (cur_input_value[17] << 4)
            ) & mask
            out[28 + out_offset] = (
                (cur_input_value[17] >> 16) | (cur_input_value[18] << 16)
            ) & mask
            out[29 + out_offset] = (cur_input_value[18] >> 4) & mask
            out[30 + out_offset] = (
                (cur_input_value[18] >> 24) | (cur_input_value[19] << 8)
            ) & mask
            out[31 + out_offset] = cur_input_value[19] >> 12
            out_offset += 32

    @staticmethod
    def __unpack16(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 65535
        for _ in range(4):
            cur_input_values = [in_.pop(0) for _ in range(16)]
            for i, cur_input_value in enumerate(cur_input_values):
                out[out_offset + 2 * i] = cur_input_value & mask
                out[out_offset + 2 * i + 1] = cur_input_value >> 16
            out_offset += 32

    @staticmethod
    def __unpack13(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 8191
        in_iter = iter(in_)
        for _ in range(4):
            cur_input_value0 = next(in_iter)
            cur_input_value1 = next(in_iter)
            cur_input_value2 = next(in_iter)
            cur_input_value3 = next(in_iter)
            cur_input_value4 = next(in_iter)
            cur_input_value5 = next(in_iter)
            cur_input_value6 = next(in_iter)
            cur_input_value7 = next(in_iter)
            cur_input_value8 = next(in_iter)
            cur_input_value9 = next(in_iter)
            cur_input_value10 = next(in_iter)
            cur_input_value11 = next(in_iter)
            cur_input_value12 = next(in_iter)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 13) & mask
            out[2 + out_offset] = (
                (cur_input_value0 >> 26) | (cur_input_value1 << 6)
            ) & mask
            out[3 + out_offset] = (cur_input_value1 >> 7) & mask
            out[4 + out_offset] = (
                (cur_input_value1 >> 20) | (cur_input_value2 << 12)
            ) & mask
            out[5 + out_offset] = (cur_input_value2 >> 1) & mask
            out[6 + out_offset] = (cur_input_value2 >> 14) & mask
            out[7 + out_offset] = (
                (cur_input_value2 >> 27) | (cur_input_value3 << 5)
            ) & mask
            out[8 + out_offset] = (cur_input_value3 >> 8) & mask
            out[9 + out_offset] = (
                (cur_input_value3 >> 21) | (cur_input_value4 << 11)
            ) & mask
            out[10 + out_offset] = (cur_input_value4 >> 2) & mask
            out[11 + out_offset] = (cur_input_value4 >> 15) & mask
            out[12 + out_offset] = (
                (cur_input_value4 >> 28) | (cur_input_value5 << 4)
            ) & mask
            out[13 + out_offset] = (cur_input_value5 >> 9) & mask
            out[14 + out_offset] = (
                (cur_input_value5 >> 22) | (cur_input_value6 << 10)
            ) & mask
            out[15 + out_offset] = (cur_input_value6 >> 3) & mask
            out[16 + out_offset] = (cur_input_value6 >> 16) & mask
            out[17 + out_offset] = (
                (cur_input_value6 >> 29) | (cur_input_value7 << 3)
            ) & mask
            out[18 + out_offset] = (cur_input_value7 >> 10) & mask
            out[19 + out_offset] = (
                (cur_input_value7 >> 23) | (cur_input_value8 << 9)
            ) & mask
            out[20 + out_offset] = (cur_input_value8 >> 4) & mask
            out[21 + out_offset] = (cur_input_value8 >> 17) & mask
            out[22 + out_offset] = (
                (cur_input_value8 >> 30) | (cur_input_value9 << 2)
            ) & mask
            out[23 + out_offset] = (cur_input_value9 >> 11) & mask
            out[24 + out_offset] = (
                (cur_input_value9 >> 24) | (cur_input_value10 << 8)
            ) & mask
            out[25 + out_offset] = (cur_input_value10 >> 5) & mask
            out[26 + out_offset] = (cur_input_value10 >> 18) & mask
            out[27 + out_offset] = (
                (cur_input_value10 >> 31) | (cur_input_value11 << 1)
            ) & mask
            out[28 + out_offset] = (cur_input_value11 >> 12) & mask
            out[29 + out_offset] = (
                (cur_input_value11 >> 25) | (cur_input_value12 << 7)
            ) & mask
            out[30 + out_offset] = (cur_input_value12 >> 6) & mask
            out[31 + out_offset] = cur_input_value12 >> 19
            out_offset += 32

    @staticmethod
    def __unpack12(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 4095
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)
            cur_input_value5 = in_.pop(0)
            cur_input_value6 = in_.pop(0)
            cur_input_value7 = in_.pop(0)
            cur_input_value8 = in_.pop(0)
            cur_input_value9 = in_.pop(0)
            cur_input_value10 = in_.pop(0)
            cur_input_value11 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 12) & mask
            out[2 + out_offset] = (
                (cur_input_value0 >> 24) | (cur_input_value1 << 8)
            ) & mask
            out[3 + out_offset] = (cur_input_value1 >> 4) & mask
            out[4 + out_offset] = (cur_input_value1 >> 16) & mask
            out[5 + out_offset] = (
                (cur_input_value1 >> 28) | (cur_input_value2 << 4)
            ) & mask
            out[6 + out_offset] = (cur_input_value2 >> 8) & mask
            out[7 + out_offset] = cur_input_value2 >> 20
            out[8 + out_offset] = cur_input_value3 & mask
            out[9 + out_offset] = (cur_input_value3 >> 12) & mask
            out[10 + out_offset] = (
                (cur_input_value3 >> 24) | (cur_input_value4 << 8)
            ) & mask
            out[11 + out_offset] = (cur_input_value4 >> 4) & mask
            out[12 + out_offset] = (cur_input_value4 >> 16) & mask
            out[13 + out_offset] = (
                (cur_input_value4 >> 28) | (cur_input_value5 << 4)
            ) & mask
            out[14 + out_offset] = (cur_input_value5 >> 8) & mask
            out[15 + out_offset] = cur_input_value5 >> 20
            out[16 + out_offset] = cur_input_value6 & mask
            out[17 + out_offset] = (cur_input_value6 >> 12) & mask
            out[18 + out_offset] = (
                (cur_input_value6 >> 24) | (cur_input_value7 << 8)
            ) & mask
            out[19 + out_offset] = (cur_input_value7 >> 4) & mask
            out[20 + out_offset] = (cur_input_value7 >> 16) & mask
            out[21 + out_offset] = (
                (cur_input_value7 >> 28) | (cur_input_value8 << 4)
            ) & mask
            out[22 + out_offset] = (cur_input_value8 >> 8) & mask
            out[23 + out_offset] = cur_input_value8 >> 20
            out[24 + out_offset] = cur_input_value9 & mask
            out[25 + out_offset] = (cur_input_value9 >> 12) & mask
            out[26 + out_offset] = (
                (cur_input_value9 >> 24) | (cur_input_value10 << 8)
            ) & mask
            out[27 + out_offset] = (cur_input_value10 >> 4) & mask
            out[28 + out_offset] = (cur_input_value10 >> 16) & mask
            out[29 + out_offset] = (
                (cur_input_value10 >> 28) | (cur_input_value11 << 4)
            ) & mask
            out[30 + out_offset] = (cur_input_value11 >> 8) & mask
            out[31 + out_offset] = cur_input_value11 >> 20

            out_offset += 32

    @staticmethod
    def __unpack11(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 2047
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)
            cur_input_value5 = in_.pop(0)
            cur_input_value6 = in_.pop(0)
            cur_input_value7 = in_.pop(0)
            cur_input_value8 = in_.pop(0)
            cur_input_value9 = in_.pop(0)
            cur_input_value10 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 11) & mask
            out[2 + out_offset] = (
                (cur_input_value0 >> 22) | (cur_input_value1 << 10)
            ) & mask
            out[3 + out_offset] = (cur_input_value1 >> 1) & mask
            out[4 + out_offset] = (cur_input_value1 >> 12) & mask
            out[5 + out_offset] = (
                (cur_input_value1 >> 23) | (cur_input_value2 << 9)
            ) & mask
            out[6 + out_offset] = (cur_input_value2 >> 2) & mask
            out[7 + out_offset] = (cur_input_value2 >> 13) & mask
            out[8 + out_offset] = (
                (cur_input_value2 >> 24) | (cur_input_value3 << 8)
            ) & mask
            out[9 + out_offset] = (cur_input_value3 >> 3) & mask
            out[10 + out_offset] = (cur_input_value3 >> 14) & mask
            out[11 + out_offset] = (
                (cur_input_value3 >> 25) | (cur_input_value4 << 7)
            ) & mask
            out[12 + out_offset] = (cur_input_value4 >> 4) & mask
            out[13 + out_offset] = (cur_input_value4 >> 15) & mask
            out[14 + out_offset] = (
                (cur_input_value4 >> 26) | (cur_input_value5 << 6)
            ) & mask
            out[15 + out_offset] = (cur_input_value5 >> 5) & mask
            out[16 + out_offset] = (cur_input_value5 >> 16) & mask
            out[17 + out_offset] = (
                (cur_input_value5 >> 27) | (cur_input_value6 << 5)
            ) & mask
            out[18 + out_offset] = (cur_input_value6 >> 6) & mask
            out[19 + out_offset] = (cur_input_value6 >> 17) & mask
            out[20 + out_offset] = (
                (cur_input_value6 >> 28) | (cur_input_value7 << 4)
            ) & mask
            out[21 + out_offset] = (cur_input_value7 >> 7) & mask
            out[22 + out_offset] = (cur_input_value7 >> 18) & mask
            out[23 + out_offset] = (
                (cur_input_value7 >> 29) | (cur_input_value8 << 3)
            ) & mask
            out[24 + out_offset] = (cur_input_value8 >> 8) & mask
            out[25 + out_offset] = (cur_input_value8 >> 19) & mask
            out[26 + out_offset] = (
                (cur_input_value8 >> 30) | (cur_input_value9 << 2)
            ) & mask
            out[27 + out_offset] = (cur_input_value9 >> 9) & mask
            out[28 + out_offset] = (cur_input_value9 >> 20) & mask
            out[29 + out_offset] = (
                (cur_input_value9 >> 31) | (cur_input_value10 << 1)
            ) & mask
            out[30 + out_offset] = (cur_input_value10 >> 10) & mask
            out[31 + out_offset] = cur_input_value10 >> 21
            out_offset += 32

    @staticmethod
    def __unpack10(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 1023
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)
            cur_input_value5 = in_.pop(0)
            cur_input_value6 = in_.pop(0)
            cur_input_value7 = in_.pop(0)
            cur_input_value8 = in_.pop(0)
            cur_input_value9 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 10) & mask
            out[2 + out_offset] = (cur_input_value0 >> 20) & mask
            out[3 + out_offset] = (
                (cur_input_value0 >> 30) | (cur_input_value1 << 2)
            ) & mask
            out[4 + out_offset] = (cur_input_value1 >> 8) & mask
            out[5 + out_offset] = (cur_input_value1 >> 18) & mask
            out[6 + out_offset] = (
                (cur_input_value1 >> 28) | (cur_input_value2 << 4)
            ) & mask
            out[7 + out_offset] = (cur_input_value2 >> 6) & mask
            out[8 + out_offset] = (cur_input_value2 >> 16) & mask
            out[9 + out_offset] = (
                (cur_input_value2 >> 26) | (cur_input_value3 << 6)
            ) & mask
            out[10 + out_offset] = (cur_input_value3 >> 4) & mask
            out[11 + out_offset] = (cur_input_value3 >> 14) & mask
            out[12 + out_offset] = (
                (cur_input_value3 >> 24) | (cur_input_value4 << 8)
            ) & mask
            out[13 + out_offset] = (cur_input_value4 >> 2) & mask
            out[14 + out_offset] = (cur_input_value4 >> 12) & mask
            out[15 + out_offset] = cur_input_value4 >> 22
            out[16 + out_offset] = cur_input_value5 & mask
            out[17 + out_offset] = (cur_input_value5 >> 10) & mask
            out[18 + out_offset] = (cur_input_value5 >> 20) & mask
            out[19 + out_offset] = (
                (cur_input_value5 >> 30) | (cur_input_value6 << 2)
            ) & mask
            out[20 + out_offset] = (cur_input_value6 >> 8) & mask
            out[21 + out_offset] = (cur_input_value6 >> 18) & mask
            out[22 + out_offset] = (
                (cur_input_value6 >> 28) | (cur_input_value7 << 4)
            ) & mask
            out[23 + out_offset] = (cur_input_value7 >> 6) & mask
            out[24 + out_offset] = (cur_input_value7 >> 16) & mask
            out[25 + out_offset] = (
                (cur_input_value7 >> 26) | (cur_input_value8 << 6)
            ) & mask
            out[26 + out_offset] = (cur_input_value8 >> 4) & mask
            out[27 + out_offset] = (cur_input_value8 >> 14) & mask
            out[28 + out_offset] = (
                (cur_input_value8 >> 24) | (cur_input_value9 << 8)
            ) & mask
            out[29 + out_offset] = (cur_input_value9 >> 2) & mask
            out[30 + out_offset] = (cur_input_value9 >> 12) & mask
            out[31 + out_offset] = cur_input_value9 >> 22
            out_offset += 32

    @staticmethod
    def __unpack9(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 511
        in_iter = iter(in_)
        for _ in range(4):
            cur_input_value0 = next(in_iter)
            cur_input_value1 = next(in_iter)
            cur_input_value2 = next(in_iter)
            cur_input_value3 = next(in_iter)
            cur_input_value4 = next(in_iter)
            cur_input_value5 = next(in_iter)
            cur_input_value6 = next(in_iter)
            cur_input_value7 = next(in_iter)
            cur_input_value8 = next(in_iter)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 9) & mask
            out[2 + out_offset] = (cur_input_value0 >> 18) & mask
            out[3 + out_offset] = (
                (cur_input_value0 >> 27) | (cur_input_value1 << 5)
            ) & mask
            out[4 + out_offset] = (cur_input_value1 >> 4) & mask
            out[5 + out_offset] = (cur_input_value1 >> 13) & mask
            out[6 + out_offset] = (cur_input_value1 >> 22) & mask
            out[7 + out_offset] = (
                (cur_input_value1 >> 31) | (cur_input_value2 << 1)
            ) & mask
            out[8 + out_offset] = (cur_input_value2 >> 8) & mask
            out[9 + out_offset] = (cur_input_value2 >> 17) & mask
            out[10 + out_offset] = (
                (cur_input_value2 >> 26) | (cur_input_value3 << 6)
            ) & mask
            out[11 + out_offset] = (cur_input_value3 >> 3) & mask
            out[12 + out_offset] = (cur_input_value3 >> 12) & mask
            out[13 + out_offset] = (cur_input_value3 >> 21) & mask
            out[14 + out_offset] = (
                (cur_input_value3 >> 30) | (cur_input_value4 << 2)
            ) & mask
            out[15 + out_offset] = (cur_input_value4 >> 7) & mask
            out[16 + out_offset] = (cur_input_value4 >> 16) & mask
            out[17 + out_offset] = (
                (cur_input_value4 >> 25) | (cur_input_value5 << 7)
            ) & mask
            out[18 + out_offset] = (cur_input_value5 >> 2) & mask
            out[19 + out_offset] = (cur_input_value5 >> 11) & mask
            out[20 + out_offset] = (cur_input_value5 >> 20) & mask
            out[21 + out_offset] = (
                (cur_input_value5 >> 29) | (cur_input_value6 << 3)
            ) & mask
            out[22 + out_offset] = (cur_input_value6 >> 6) & mask
            out[23 + out_offset] = (cur_input_value6 >> 15) & mask
            out[24 + out_offset] = (
                (cur_input_value6 >> 24) | (cur_input_value7 << 8)
            ) & mask
            out[25 + out_offset] = (cur_input_value7 >> 1) & mask
            out[26 + out_offset] = (cur_input_value7 >> 10) & mask
            out[27 + out_offset] = (cur_input_value7 >> 19) & mask
            out[28 + out_offset] = (
                (cur_input_value7 >> 28) | (cur_input_value8 << 4)
            ) & mask
            out[29 + out_offset] = (cur_input_value8 >> 5) & mask
            out[30 + out_offset] = (cur_input_value8 >> 14) & mask
            out[31 + out_offset] = cur_input_value8 >> 23
            out_offset += 32

    @staticmethod
    def __unpack8(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 255
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)
            cur_input_value5 = in_.pop(0)
            cur_input_value6 = in_.pop(0)
            cur_input_value7 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 8) & mask
            out[2 + out_offset] = (cur_input_value0 >> 16) & mask
            out[3 + out_offset] = cur_input_value0 >> 24
            out[4 + out_offset] = cur_input_value1 & mask
            out[5 + out_offset] = (cur_input_value1 >> 8) & mask
            out[6 + out_offset] = (cur_input_value1 >> 16) & mask
            out[7 + out_offset] = cur_input_value1 >> 24
            out[8 + out_offset] = cur_input_value2 & mask
            out[9 + out_offset] = (cur_input_value2 >> 8) & mask
            out[10 + out_offset] = (cur_input_value2 >> 16) & mask
            out[11 + out_offset] = cur_input_value2 >> 24
            out[12 + out_offset] = cur_input_value3 & mask
            out[13 + out_offset] = (cur_input_value3 >> 8) & mask
            out[14 + out_offset] = (cur_input_value3 >> 16) & mask
            out[15 + out_offset] = cur_input_value3 >> 24
            out[16 + out_offset] = cur_input_value4 & mask
            out[17 + out_offset] = (cur_input_value4 >> 8) & mask
            out[18 + out_offset] = (cur_input_value4 >> 16) & mask
            out[19 + out_offset] = cur_input_value4 >> 24
            out[20 + out_offset] = cur_input_value5 & mask
            out[21 + out_offset] = (cur_input_value5 >> 8) & mask
            out[22 + out_offset] = (cur_input_value5 >> 16) & mask
            out[23 + out_offset] = cur_input_value5 >> 24
            out[24 + out_offset] = cur_input_value6 & mask
            out[25 + out_offset] = (cur_input_value6 >> 8) & mask
            out[26 + out_offset] = (cur_input_value6 >> 16) & mask
            out[27 + out_offset] = cur_input_value6 >> 24
            out[28 + out_offset] = cur_input_value7 & mask
            out[29 + out_offset] = (cur_input_value7 >> 8) & mask
            out[30 + out_offset] = (cur_input_value7 >> 16) & mask
            out[31 + out_offset] = cur_input_value7 >> 24
            out_offset += 32

    @staticmethod
    def __unpack7(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 127
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)
            cur_input_value5 = in_.pop(0)
            cur_input_value6 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 7) & mask
            out[2 + out_offset] = (cur_input_value0 >> 14) & mask
            out[3 + out_offset] = (cur_input_value0 >> 21) & mask
            out[4 + out_offset] = (
                (cur_input_value0 >> 28) | (cur_input_value1 << 4)
            ) & mask
            out[5 + out_offset] = (cur_input_value1 >> 3) & mask
            out[6 + out_offset] = (cur_input_value1 >> 10) & mask
            out[7 + out_offset] = (cur_input_value1 >> 17) & mask
            out[8 + out_offset] = (cur_input_value1 >> 24) & mask
            out[9 + out_offset] = (
                (cur_input_value1 >> 31) | (cur_input_value2 << 1)
            ) & mask
            out[10 + out_offset] = (cur_input_value2 >> 6) & mask
            out[11 + out_offset] = (cur_input_value2 >> 13) & mask
            out[12 + out_offset] = (cur_input_value2 >> 20) & mask
            out[13 + out_offset] = (
                (cur_input_value2 >> 27) | (cur_input_value3 << 5)
            ) & mask
            out[14 + out_offset] = (cur_input_value3 >> 2) & mask
            out[15 + out_offset] = (cur_input_value3 >> 9) & mask
            out[16 + out_offset] = (cur_input_value3 >> 16) & mask
            out[17 + out_offset] = (cur_input_value3 >> 23) & mask
            out[18 + out_offset] = (
                (cur_input_value3 >> 30) | (cur_input_value4 << 2)
            ) & mask
            out[19 + out_offset] = (cur_input_value4 >> 5) & mask
            out[20 + out_offset] = (cur_input_value4 >> 12) & mask
            out[21 + out_offset] = (cur_input_value4 >> 19) & mask
            out[22 + out_offset] = (
                (cur_input_value4 >> 26) | (cur_input_value5 << 6)
            ) & mask
            out[23 + out_offset] = (cur_input_value5 >> 1) & mask
            out[24 + out_offset] = (cur_input_value5 >> 8) & mask
            out[25 + out_offset] = (cur_input_value5 >> 15) & mask
            out[26 + out_offset] = (cur_input_value5 >> 22) & mask
            out[27 + out_offset] = (
                (cur_input_value5 >> 29) | (cur_input_value6 << 3)
            ) & mask
            out[28 + out_offset] = (cur_input_value6 >> 4) & mask
            out[29 + out_offset] = (cur_input_value6 >> 11) & mask
            out[30 + out_offset] = (cur_input_value6 >> 18) & mask
            out[31 + out_offset] = cur_input_value6 >> 25
            out_offset += 32

    @staticmethod
    def __unpack6(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 63
        in_iter = iter(in_)  # Create an iterator for the input buffer
        for _ in range(4):
            cur_input_value0 = next(in_iter)
            cur_input_value1 = next(in_iter)
            cur_input_value2 = next(in_iter)
            cur_input_value3 = next(in_iter)
            cur_input_value4 = next(in_iter)
            cur_input_value5 = next(in_iter)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 6) & mask
            out[2 + out_offset] = (cur_input_value0 >> 12) & mask
            out[3 + out_offset] = (cur_input_value0 >> 18) & mask
            out[4 + out_offset] = (cur_input_value0 >> 24) & mask
            out[5 + out_offset] = (
                (cur_input_value0 >> 30) | (cur_input_value1 << 2)
            ) & mask
            out[6 + out_offset] = (cur_input_value1 >> 4) & mask
            out[7 + out_offset] = (cur_input_value1 >> 10) & mask
            out[8 + out_offset] = (cur_input_value1 >> 16) & mask
            out[9 + out_offset] = (cur_input_value1 >> 22) & mask
            out[10 + out_offset] = (
                (cur_input_value1 >> 28) | (cur_input_value2 << 4)
            ) & mask
            out[11 + out_offset] = (cur_input_value2 >> 2) & mask
            out[12 + out_offset] = (cur_input_value2 >> 8) & mask
            out[13 + out_offset] = (cur_input_value2 >> 14) & mask
            out[14 + out_offset] = (cur_input_value2 >> 20) & mask
            out[15 + out_offset] = cur_input_value2 >> 26
            out[16 + out_offset] = cur_input_value3 & mask
            out[17 + out_offset] = (cur_input_value3 >> 6) & mask
            out[18 + out_offset] = (cur_input_value3 >> 12) & mask
            out[19 + out_offset] = (cur_input_value3 >> 18) & mask
            out[20 + out_offset] = (cur_input_value3 >> 24) & mask
            out[21 + out_offset] = (
                (cur_input_value3 >> 30) | (cur_input_value4 << 2)
            ) & mask
            out[22 + out_offset] = (cur_input_value4 >> 4) & mask
            out[23 + out_offset] = (cur_input_value4 >> 10) & mask
            out[24 + out_offset] = (cur_input_value4 >> 16) & mask
            out[25 + out_offset] = (cur_input_value4 >> 22) & mask
            out[26 + out_offset] = (
                (cur_input_value4 >> 28) | (cur_input_value5 << 4)
            ) & mask
            out[27 + out_offset] = (cur_input_value5 >> 2) & mask
            out[28 + out_offset] = (cur_input_value5 >> 8) & mask
            out[29 + out_offset] = (cur_input_value5 >> 14) & mask
            out[30 + out_offset] = (cur_input_value5 >> 20) & mask
            out[31 + out_offset] = cur_input_value5 >> 26
            out_offset += 32

    @staticmethod
    def __unpack5(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 31
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)
            cur_input_value4 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 5) & mask
            out[2 + out_offset] = (cur_input_value0 >> 10) & mask
            out[3 + out_offset] = (cur_input_value0 >> 15) & mask
            out[4 + out_offset] = (cur_input_value0 >> 20) & mask
            out[5 + out_offset] = (cur_input_value0 >> 25) & mask
            out[6 + out_offset] = (
                (cur_input_value0 >> 30) | (cur_input_value1 << 2)
            ) & mask
            out[7 + out_offset] = (cur_input_value1 >> 3) & mask
            out[8 + out_offset] = (cur_input_value1 >> 8) & mask
            out[9 + out_offset] = (cur_input_value1 >> 13) & mask
            out[10 + out_offset] = (cur_input_value1 >> 18) & mask
            out[11 + out_offset] = (cur_input_value1 >> 23) & mask
            out[12 + out_offset] = (
                (cur_input_value1 >> 28) | (cur_input_value2 << 4)
            ) & mask
            out[13 + out_offset] = (cur_input_value2 >> 1) & mask
            out[14 + out_offset] = (cur_input_value2 >> 6) & mask
            out[15 + out_offset] = (cur_input_value2 >> 11) & mask
            out[16 + out_offset] = (cur_input_value2 >> 16) & mask
            out[17 + out_offset] = (cur_input_value2 >> 21) & mask
            out[18 + out_offset] = (cur_input_value2 >> 26) & mask
            out[19 + out_offset] = (
                (cur_input_value2 >> 31) | (cur_input_value3 << 1)
            ) & mask
            out[20 + out_offset] = (cur_input_value3 >> 4) & mask
            out[21 + out_offset] = (cur_input_value3 >> 9) & mask
            out[22 + out_offset] = (cur_input_value3 >> 14) & mask
            out[23 + out_offset] = (cur_input_value3 >> 19) & mask
            out[24 + out_offset] = (cur_input_value3 >> 24) & mask
            out[25 + out_offset] = (
                (cur_input_value3 >> 29) | (cur_input_value4 << 3)
            ) & mask
            out[26 + out_offset] = (cur_input_value4 >> 2) & mask
            out[27 + out_offset] = (cur_input_value4 >> 7) & mask
            out[28 + out_offset] = (cur_input_value4 >> 12) & mask
            out[29 + out_offset] = (cur_input_value4 >> 17) & mask
            out[30 + out_offset] = (cur_input_value4 >> 22) & mask
            out[31 + out_offset] = cur_input_value4 >> 27

            out_offset += 32

    @staticmethod
    def __unpack4(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 15
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            cur_input_value3 = in_.pop(0)

            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 4) & mask
            out[2 + out_offset] = (cur_input_value0 >> 8) & mask
            out[3 + out_offset] = (cur_input_value0 >> 12) & mask
            out[4 + out_offset] = (cur_input_value0 >> 16) & mask
            out[5 + out_offset] = (cur_input_value0 >> 20) & mask
            out[6 + out_offset] = (cur_input_value0 >> 24) & mask
            out[7 + out_offset] = cur_input_value0 >> 28
            out[8 + out_offset] = cur_input_value1 & mask
            out[9 + out_offset] = (cur_input_value1 >> 4) & mask
            out[10 + out_offset] = (cur_input_value1 >> 8) & mask
            out[11 + out_offset] = (cur_input_value1 >> 12) & mask
            out[12 + out_offset] = (cur_input_value1 >> 16) & mask
            out[13 + out_offset] = (cur_input_value1 >> 20) & mask
            out[14 + out_offset] = (cur_input_value1 >> 24) & mask
            out[15 + out_offset] = cur_input_value1 >> 28
            out[16 + out_offset] = cur_input_value2 & mask
            out[17 + out_offset] = (cur_input_value2 >> 4) & mask
            out[18 + out_offset] = (cur_input_value2 >> 8) & mask
            out[19 + out_offset] = (cur_input_value2 >> 12) & mask
            out[20 + out_offset] = (cur_input_value2 >> 16) & mask
            out[21 + out_offset] = (cur_input_value2 >> 20) & mask
            out[22 + out_offset] = (cur_input_value2 >> 24) & mask
            out[23 + out_offset] = cur_input_value2 >> 28
            out[24 + out_offset] = cur_input_value3 & mask
            out[25 + out_offset] = (cur_input_value3 >> 4) & mask
            out[26 + out_offset] = (cur_input_value3 >> 8) & mask
            out[27 + out_offset] = (cur_input_value3 >> 12) & mask
            out[28 + out_offset] = (cur_input_value3 >> 16) & mask
            out[29 + out_offset] = (cur_input_value3 >> 20) & mask
            out[30 + out_offset] = (cur_input_value3 >> 24) & mask
            out[31 + out_offset] = cur_input_value3 >> 28
            out_offset += 32

    @staticmethod
    def __unpack3(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 7
        for _ in range(4):
            cur_input_value0 = in_.pop(0)
            cur_input_value1 = in_.pop(0)
            cur_input_value2 = in_.pop(0)
            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 3) & mask
            out[2 + out_offset] = (cur_input_value0 >> 6) & mask
            out[3 + out_offset] = (cur_input_value0 >> 9) & mask
            out[4 + out_offset] = (cur_input_value0 >> 12) & mask
            out[5 + out_offset] = (cur_input_value0 >> 15) & mask
            out[6 + out_offset] = (cur_input_value0 >> 18) & mask
            out[7 + out_offset] = (cur_input_value0 >> 21) & mask
            out[8 + out_offset] = (cur_input_value0 >> 24) & mask
            out[9 + out_offset] = (cur_input_value0 >> 27) & mask
            out[10 + out_offset] = (
                (cur_input_value0 >> 30) | (cur_input_value1 << 2)
            ) & mask
            out[11 + out_offset] = (cur_input_value1 >> 1) & mask
            out[12 + out_offset] = (cur_input_value1 >> 4) & mask
            out[13 + out_offset] = (cur_input_value1 >> 7) & mask
            out[14 + out_offset] = (cur_input_value1 >> 10) & mask
            out[15 + out_offset] = (cur_input_value1 >> 13) & mask
            out[16 + out_offset] = (cur_input_value1 >> 16) & mask
            out[17 + out_offset] = (cur_input_value1 >> 19) & mask
            out[18 + out_offset] = (cur_input_value1 >> 22) & mask
            out[19 + out_offset] = (cur_input_value1 >> 25) & mask
            out[20 + out_offset] = (cur_input_value1 >> 28) & mask
            out[21 + out_offset] = (
                (cur_input_value1 >> 31) | (cur_input_value2 << 1)
            ) & mask
            out[22 + out_offset] = (cur_input_value2 >> 2) & mask
            out[23 + out_offset] = (cur_input_value2 >> 5) & mask
            out[24 + out_offset] = (cur_input_value2 >> 8) & mask
            out[25 + out_offset] = (cur_input_value2 >> 11) & mask
            out[26 + out_offset] = (cur_input_value2 >> 14) & mask
            out[27 + out_offset] = (cur_input_value2 >> 17) & mask
            out[28 + out_offset] = (cur_input_value2 >> 20) & mask
            out[29 + out_offset] = (cur_input_value2 >> 23) & mask
            out[30 + out_offset] = (cur_input_value2 >> 26) & mask
            out[31 + out_offset] = cur_input_value2 >> 29
            out_offset += 32

    @staticmethod
    def __unpack2(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __unpack1(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        out_offset = 0
        mask = 1
        for _ in range(4):
            cur_input_value0 = in_.pop(
                0
            )  # Simulating `in.get()` by popping the first element
            out[0 + out_offset] = cur_input_value0 & mask
            out[1 + out_offset] = (cur_input_value0 >> 1) & mask
            out[2 + out_offset] = (cur_input_value0 >> 2) & mask
            out[3 + out_offset] = (cur_input_value0 >> 3) & mask
            out[4 + out_offset] = (cur_input_value0 >> 4) & mask
            out[5 + out_offset] = (cur_input_value0 >> 5) & mask
            out[6 + out_offset] = (cur_input_value0 >> 6) & mask
            out[7 + out_offset] = (cur_input_value0 >> 7) & mask
            out[8 + out_offset] = (cur_input_value0 >> 8) & mask
            out[9 + out_offset] = (cur_input_value0 >> 9) & mask
            out[10 + out_offset] = (cur_input_value0 >> 10) & mask
            out[11 + out_offset] = (cur_input_value0 >> 11) & mask
            out[12 + out_offset] = (cur_input_value0 >> 12) & mask
            out[13 + out_offset] = (cur_input_value0 >> 13) & mask
            out[14 + out_offset] = (cur_input_value0 >> 14) & mask
            out[15 + out_offset] = (cur_input_value0 >> 15) & mask
            out[16 + out_offset] = (cur_input_value0 >> 16) & mask
            out[17 + out_offset] = (cur_input_value0 >> 17) & mask
            out[18 + out_offset] = (cur_input_value0 >> 18) & mask
            out[19 + out_offset] = (cur_input_value0 >> 19) & mask
            out[20 + out_offset] = (cur_input_value0 >> 20) & mask
            out[21 + out_offset] = (cur_input_value0 >> 21) & mask
            out[22 + out_offset] = (cur_input_value0 >> 22) & mask
            out[23 + out_offset] = (cur_input_value0 >> 23) & mask
            out[24 + out_offset] = (cur_input_value0 >> 24) & mask
            out[25 + out_offset] = (cur_input_value0 >> 25) & mask
            out[26 + out_offset] = (cur_input_value0 >> 26) & mask
            out[27 + out_offset] = (cur_input_value0 >> 27) & mask
            out[28 + out_offset] = (cur_input_value0 >> 28) & mask
            out[29 + out_offset] = (cur_input_value0 >> 29) & mask
            out[30 + out_offset] = (cur_input_value0 >> 30) & mask
            out[31 + out_offset] = cur_input_value0 >> 31
            out_offset += 32

    @staticmethod
    def __unpack0(
        out: typing.List[int], in_: typing.Union[array.array, typing.List[int]]
    ) -> None:
        # The method is currently empty in the Java code, so the Python translation is also empty.
        pass
