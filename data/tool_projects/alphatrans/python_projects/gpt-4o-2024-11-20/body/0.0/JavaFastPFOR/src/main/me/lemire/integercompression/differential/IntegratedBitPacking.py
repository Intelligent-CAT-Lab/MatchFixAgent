from __future__ import annotations
import re
import io
import typing
from typing import *
import os


class IntegratedBitPacking:

    @staticmethod
    def _integratedunpack9(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 511) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 9) & 511) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 18) & 511) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[0 + inpos] >> 27) | ((in_[1 + inpos] & 15) << (9 - 4))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[1 + inpos] >> 4) & 511) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[1 + inpos] >> 13) & 511) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[1 + inpos] >> 22) & 511) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[1 + inpos] >> 31) | ((in_[2 + inpos] & 255) << (9 - 8))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[2 + inpos] >> 8) & 511) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[2 + inpos] >> 17) & 511) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[2 + inpos] >> 26) | ((in_[3 + inpos] & 7) << (9 - 3))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[3 + inpos] >> 3) & 511) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[3 + inpos] >> 12) & 511) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[3 + inpos] >> 21) & 511) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[3 + inpos] >> 30) | ((in_[4 + inpos] & 127) << (9 - 7))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[4 + inpos] >> 7) & 511) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[4 + inpos] >> 16) & 511) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[4 + inpos] >> 25) | ((in_[5 + inpos] & 3) << (9 - 2))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[5 + inpos] >> 2) & 511) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[5 + inpos] >> 11) & 511) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[5 + inpos] >> 20) & 511) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[5 + inpos] >> 29) | ((in_[6 + inpos] & 63) << (9 - 6))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[6 + inpos] >> 6) & 511) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[6 + inpos] >> 15) & 511) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[6 + inpos] >> 24) | ((in_[7 + inpos] & 1) << (9 - 1))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[7 + inpos] >> 1) & 511) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[7 + inpos] >> 10) & 511) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[7 + inpos] >> 19) & 511) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[7 + inpos] >> 28) | ((in_[8 + inpos] & 31) << (9 - 5))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[8 + inpos] >> 5) & 511) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[8 + inpos] >> 14) & 511) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[8 + inpos] >> 23) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack8(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 255) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 8) & 255) + out[0 + outpos]
        out[2 + outpos] = ((in_[0 + inpos] >> 16) & 255) + out[1 + outpos]
        out[3 + outpos] = (in_[0 + inpos] >> 24) + out[2 + outpos]
        out[4 + outpos] = ((in_[1 + inpos] >> 0) & 255) + out[3 + outpos]
        out[5 + outpos] = ((in_[1 + inpos] >> 8) & 255) + out[4 + outpos]
        out[6 + outpos] = ((in_[1 + inpos] >> 16) & 255) + out[5 + outpos]
        out[7 + outpos] = (in_[1 + inpos] >> 24) + out[6 + outpos]
        out[8 + outpos] = ((in_[2 + inpos] >> 0) & 255) + out[7 + outpos]
        out[9 + outpos] = ((in_[2 + inpos] >> 8) & 255) + out[8 + outpos]
        out[10 + outpos] = ((in_[2 + inpos] >> 16) & 255) + out[9 + outpos]
        out[11 + outpos] = (in_[2 + inpos] >> 24) + out[10 + outpos]
        out[12 + outpos] = ((in_[3 + inpos] >> 0) & 255) + out[11 + outpos]
        out[13 + outpos] = ((in_[3 + inpos] >> 8) & 255) + out[12 + outpos]
        out[14 + outpos] = ((in_[3 + inpos] >> 16) & 255) + out[13 + outpos]
        out[15 + outpos] = (in_[3 + inpos] >> 24) + out[14 + outpos]
        out[16 + outpos] = ((in_[4 + inpos] >> 0) & 255) + out[15 + outpos]
        out[17 + outpos] = ((in_[4 + inpos] >> 8) & 255) + out[16 + outpos]
        out[18 + outpos] = ((in_[4 + inpos] >> 16) & 255) + out[17 + outpos]
        out[19 + outpos] = (in_[4 + inpos] >> 24) + out[18 + outpos]
        out[20 + outpos] = ((in_[5 + inpos] >> 0) & 255) + out[19 + outpos]
        out[21 + outpos] = ((in_[5 + inpos] >> 8) & 255) + out[20 + outpos]
        out[22 + outpos] = ((in_[5 + inpos] >> 16) & 255) + out[21 + outpos]
        out[23 + outpos] = (in_[5 + inpos] >> 24) + out[22 + outpos]
        out[24 + outpos] = ((in_[6 + inpos] >> 0) & 255) + out[23 + outpos]
        out[25 + outpos] = ((in_[6 + inpos] >> 8) & 255) + out[24 + outpos]
        out[26 + outpos] = ((in_[6 + inpos] >> 16) & 255) + out[25 + outpos]
        out[27 + outpos] = (in_[6 + inpos] >> 24) + out[26 + outpos]
        out[28 + outpos] = ((in_[7 + inpos] >> 0) & 255) + out[27 + outpos]
        out[29 + outpos] = ((in_[7 + inpos] >> 8) & 255) + out[28 + outpos]
        out[30 + outpos] = ((in_[7 + inpos] >> 16) & 255) + out[29 + outpos]
        out[31 + outpos] = (in_[7 + inpos] >> 24) + out[30 + outpos]

    @staticmethod
    def _integratedunpack7(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 127)) + initoffset
        out[1 + outpos] = (((in_[0 + inpos] >> 7) & 127)) + out[1 + outpos - 1]
        out[2 + outpos] = (((in_[0 + inpos] >> 14) & 127)) + out[2 + outpos - 1]
        out[3 + outpos] = (((in_[0 + inpos] >> 21) & 127)) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[0 + inpos] >> 28) | ((in_[1 + inpos] & 7) << (7 - 3))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (((in_[1 + inpos] >> 3) & 127)) + out[5 + outpos - 1]
        out[6 + outpos] = (((in_[1 + inpos] >> 10) & 127)) + out[6 + outpos - 1]
        out[7 + outpos] = (((in_[1 + inpos] >> 17) & 127)) + out[7 + outpos - 1]
        out[8 + outpos] = (((in_[1 + inpos] >> 24) & 127)) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[1 + inpos] >> 31) | ((in_[2 + inpos] & 63) << (7 - 6))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (((in_[2 + inpos] >> 6) & 127)) + out[10 + outpos - 1]
        out[11 + outpos] = (((in_[2 + inpos] >> 13) & 127)) + out[11 + outpos - 1]
        out[12 + outpos] = (((in_[2 + inpos] >> 20) & 127)) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[2 + inpos] >> 27) | ((in_[3 + inpos] & 3) << (7 - 2))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (((in_[3 + inpos] >> 2) & 127)) + out[14 + outpos - 1]
        out[15 + outpos] = (((in_[3 + inpos] >> 9) & 127)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[3 + inpos] >> 16) & 127)) + out[16 + outpos - 1]
        out[17 + outpos] = (((in_[3 + inpos] >> 23) & 127)) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[3 + inpos] >> 30) | ((in_[4 + inpos] & 31) << (7 - 5))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (((in_[4 + inpos] >> 5) & 127)) + out[19 + outpos - 1]
        out[20 + outpos] = (((in_[4 + inpos] >> 12) & 127)) + out[20 + outpos - 1]
        out[21 + outpos] = (((in_[4 + inpos] >> 19) & 127)) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[4 + inpos] >> 26) | ((in_[5 + inpos] & 1) << (7 - 1))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (((in_[5 + inpos] >> 1) & 127)) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[5 + inpos] >> 8) & 127)) + out[24 + outpos - 1]
        out[25 + outpos] = (((in_[5 + inpos] >> 15) & 127)) + out[25 + outpos - 1]
        out[26 + outpos] = (((in_[5 + inpos] >> 22) & 127)) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[5 + inpos] >> 29) | ((in_[6 + inpos] & 15) << (7 - 4))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[6 + inpos] >> 4) & 127)) + out[28 + outpos - 1]
        out[29 + outpos] = (((in_[6 + inpos] >> 11) & 127)) + out[29 + outpos - 1]
        out[30 + outpos] = (((in_[6 + inpos] >> 18) & 127)) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[6 + inpos] >> 25)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack6(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 63) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 6) & 63) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 12) & 63) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[0 + inpos] >> 18) & 63) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[0 + inpos] >> 24) & 63) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 15) << (6 - 4))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[1 + inpos] >> 4) & 63) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[1 + inpos] >> 10) & 63) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[1 + inpos] >> 16) & 63) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[1 + inpos] >> 22) & 63) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 3) << (6 - 2))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[2 + inpos] >> 2) & 63) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[2 + inpos] >> 8) & 63) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[2 + inpos] >> 14) & 63) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[2 + inpos] >> 20) & 63) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[2 + inpos] >> 26)) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[3 + inpos] >> 0) & 63) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[3 + inpos] >> 6) & 63) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[3 + inpos] >> 12) & 63) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[3 + inpos] >> 18) & 63) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[3 + inpos] >> 24) & 63) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[3 + inpos] >> 30) | ((in_[4 + inpos] & 15) << (6 - 4))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[4 + inpos] >> 4) & 63) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[4 + inpos] >> 10) & 63) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[4 + inpos] >> 16) & 63) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[4 + inpos] >> 22) & 63) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[4 + inpos] >> 28) | ((in_[5 + inpos] & 3) << (6 - 2))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[5 + inpos] >> 2) & 63) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[5 + inpos] >> 8) & 63) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[5 + inpos] >> 14) & 63) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[5 + inpos] >> 20) & 63) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[5 + inpos] >> 26)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack5(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 31) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 5) & 31) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 10) & 31) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[0 + inpos] >> 15) & 31) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[0 + inpos] >> 20) & 31) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[0 + inpos] >> 25) & 31) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 7) << (5 - 3))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[1 + inpos] >> 3) & 31) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[1 + inpos] >> 8) & 31) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[1 + inpos] >> 13) & 31) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[1 + inpos] >> 18) & 31) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[1 + inpos] >> 23) & 31) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 1) << (5 - 1))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[2 + inpos] >> 1) & 31) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[2 + inpos] >> 6) & 31) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[2 + inpos] >> 11) & 31) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[2 + inpos] >> 16) & 31) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[2 + inpos] >> 21) & 31) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[2 + inpos] >> 26) & 31) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[2 + inpos] >> 31) | ((in_[3 + inpos] & 15) << (5 - 4))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[3 + inpos] >> 4) & 31) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[3 + inpos] >> 9) & 31) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[3 + inpos] >> 14) & 31) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[3 + inpos] >> 19) & 31) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[3 + inpos] >> 24) & 31) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[3 + inpos] >> 29) | ((in_[4 + inpos] & 3) << (5 - 2))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[4 + inpos] >> 2) & 31) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[4 + inpos] >> 7) & 31) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[4 + inpos] >> 12) & 31) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[4 + inpos] >> 17) & 31) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[4 + inpos] >> 22) & 31) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[4 + inpos] >> 27) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack4(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 15) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 4) & 15) + out[0 + outpos]
        out[2 + outpos] = ((in_[0 + inpos] >> 8) & 15) + out[1 + outpos]
        out[3 + outpos] = ((in_[0 + inpos] >> 12) & 15) + out[2 + outpos]
        out[4 + outpos] = ((in_[0 + inpos] >> 16) & 15) + out[3 + outpos]
        out[5 + outpos] = ((in_[0 + inpos] >> 20) & 15) + out[4 + outpos]
        out[6 + outpos] = ((in_[0 + inpos] >> 24) & 15) + out[5 + outpos]
        out[7 + outpos] = (in_[0 + inpos] >> 28) + out[6 + outpos]
        out[8 + outpos] = ((in_[1 + inpos] >> 0) & 15) + out[7 + outpos]
        out[9 + outpos] = ((in_[1 + inpos] >> 4) & 15) + out[8 + outpos]
        out[10 + outpos] = ((in_[1 + inpos] >> 8) & 15) + out[9 + outpos]
        out[11 + outpos] = ((in_[1 + inpos] >> 12) & 15) + out[10 + outpos]
        out[12 + outpos] = ((in_[1 + inpos] >> 16) & 15) + out[11 + outpos]
        out[13 + outpos] = ((in_[1 + inpos] >> 20) & 15) + out[12 + outpos]
        out[14 + outpos] = ((in_[1 + inpos] >> 24) & 15) + out[13 + outpos]
        out[15 + outpos] = (in_[1 + inpos] >> 28) + out[14 + outpos]
        out[16 + outpos] = ((in_[2 + inpos] >> 0) & 15) + out[15 + outpos]
        out[17 + outpos] = ((in_[2 + inpos] >> 4) & 15) + out[16 + outpos]
        out[18 + outpos] = ((in_[2 + inpos] >> 8) & 15) + out[17 + outpos]
        out[19 + outpos] = ((in_[2 + inpos] >> 12) & 15) + out[18 + outpos]
        out[20 + outpos] = ((in_[2 + inpos] >> 16) & 15) + out[19 + outpos]
        out[21 + outpos] = ((in_[2 + inpos] >> 20) & 15) + out[20 + outpos]
        out[22 + outpos] = ((in_[2 + inpos] >> 24) & 15) + out[21 + outpos]
        out[23 + outpos] = (in_[2 + inpos] >> 28) + out[22 + outpos]
        out[24 + outpos] = ((in_[3 + inpos] >> 0) & 15) + out[23 + outpos]
        out[25 + outpos] = ((in_[3 + inpos] >> 4) & 15) + out[24 + outpos]
        out[26 + outpos] = ((in_[3 + inpos] >> 8) & 15) + out[25 + outpos]
        out[27 + outpos] = ((in_[3 + inpos] >> 12) & 15) + out[26 + outpos]
        out[28 + outpos] = ((in_[3 + inpos] >> 16) & 15) + out[27 + outpos]
        out[29 + outpos] = ((in_[3 + inpos] >> 20) & 15) + out[28 + outpos]
        out[30 + outpos] = ((in_[3 + inpos] >> 24) & 15) + out[29 + outpos]
        out[31 + outpos] = (in_[3 + inpos] >> 28) + out[30 + outpos]

    out[outpos : outpos + 32] = in_[inpos : inpos + 32]

    @staticmethod
    def _integratedunpack31(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 2147483647) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 31) | ((in_[1 + inpos] & 1073741823) << (31 - 30))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 30) | ((in_[2 + inpos] & 536870911) << (31 - 29))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 29) | ((in_[3 + inpos] & 268435455) << (31 - 28))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 28) | ((in_[4 + inpos] & 134217727) << (31 - 27))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[4 + inpos] >> 27) | ((in_[5 + inpos] & 67108863) << (31 - 26))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[5 + inpos] >> 26) | ((in_[6 + inpos] & 33554431) << (31 - 25))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[6 + inpos] >> 25) | ((in_[7 + inpos] & 16777215) << (31 - 24))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[7 + inpos] >> 24) | ((in_[8 + inpos] & 8388607) << (31 - 23))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[8 + inpos] >> 23) | ((in_[9 + inpos] & 4194303) << (31 - 22))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[9 + inpos] >> 22) | ((in_[10 + inpos] & 2097151) << (31 - 21))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[10 + inpos] >> 21) | ((in_[11 + inpos] & 1048575) << (31 - 20))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[11 + inpos] >> 20) | ((in_[12 + inpos] & 524287) << (31 - 19))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[12 + inpos] >> 19) | ((in_[13 + inpos] & 262143) << (31 - 18))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[13 + inpos] >> 18) | ((in_[14 + inpos] & 131071) << (31 - 17))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[14 + inpos] >> 17) | ((in_[15 + inpos] & 65535) << (31 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[15 + inpos] >> 16) | ((in_[16 + inpos] & 32767) << (31 - 15))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[16 + inpos] >> 15) | ((in_[17 + inpos] & 16383) << (31 - 14))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[17 + inpos] >> 14) | ((in_[18 + inpos] & 8191) << (31 - 13))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[18 + inpos] >> 13) | ((in_[19 + inpos] & 4095) << (31 - 12))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[19 + inpos] >> 12) | ((in_[20 + inpos] & 2047) << (31 - 11))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[20 + inpos] >> 11) | ((in_[21 + inpos] & 1023) << (31 - 10))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[21 + inpos] >> 10) | ((in_[22 + inpos] & 511) << (31 - 9))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[22 + inpos] >> 9) | ((in_[23 + inpos] & 255) << (31 - 8))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[23 + inpos] >> 8) | ((in_[24 + inpos] & 127) << (31 - 7))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[24 + inpos] >> 7) | ((in_[25 + inpos] & 63) << (31 - 6))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[25 + inpos] >> 6) | ((in_[26 + inpos] & 31) << (31 - 5))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[26 + inpos] >> 5) | ((in_[27 + inpos] & 15) << (31 - 4))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[27 + inpos] >> 4) | ((in_[28 + inpos] & 7) << (31 - 3))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[28 + inpos] >> 3) | ((in_[29 + inpos] & 3) << (31 - 2))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[29 + inpos] >> 2) | ((in_[30 + inpos] & 1) << (31 - 1))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[30 + inpos] >> 1)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack30(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 1073741823) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 268435455) << (30 - 28))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 67108863) << (30 - 26))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 26) | ((in_[3 + inpos] & 16777215) << (30 - 24))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 4194303) << (30 - 22))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[4 + inpos] >> 22) | ((in_[5 + inpos] & 1048575) << (30 - 20))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[5 + inpos] >> 20) | ((in_[6 + inpos] & 262143) << (30 - 18))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[6 + inpos] >> 18) | ((in_[7 + inpos] & 65535) << (30 - 16))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[7 + inpos] >> 16) | ((in_[8 + inpos] & 16383) << (30 - 14))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[8 + inpos] >> 14) | ((in_[9 + inpos] & 4095) << (30 - 12))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[9 + inpos] >> 12) | ((in_[10 + inpos] & 1023) << (30 - 10))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[10 + inpos] >> 10) | ((in_[11 + inpos] & 255) << (30 - 8))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[11 + inpos] >> 8) | ((in_[12 + inpos] & 63) << (30 - 6))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[12 + inpos] >> 6) | ((in_[13 + inpos] & 15) << (30 - 4))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[13 + inpos] >> 4) | ((in_[14 + inpos] & 3) << (30 - 2))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[14 + inpos] >> 2)) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[15 + inpos] >> 0) & 1073741823) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[15 + inpos] >> 30) | ((in_[16 + inpos] & 268435455) << (30 - 28))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[16 + inpos] >> 28) | ((in_[17 + inpos] & 67108863) << (30 - 26))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[17 + inpos] >> 26) | ((in_[18 + inpos] & 16777215) << (30 - 24))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[18 + inpos] >> 24) | ((in_[19 + inpos] & 4194303) << (30 - 22))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[19 + inpos] >> 22) | ((in_[20 + inpos] & 1048575) << (30 - 20))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[20 + inpos] >> 20) | ((in_[21 + inpos] & 262143) << (30 - 18))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[21 + inpos] >> 18) | ((in_[22 + inpos] & 65535) << (30 - 16))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[22 + inpos] >> 16) | ((in_[23 + inpos] & 16383) << (30 - 14))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[23 + inpos] >> 14) | ((in_[24 + inpos] & 4095) << (30 - 12))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[24 + inpos] >> 12) | ((in_[25 + inpos] & 1023) << (30 - 10))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[25 + inpos] >> 10) | ((in_[26 + inpos] & 255) << (30 - 8))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[26 + inpos] >> 8) | ((in_[27 + inpos] & 63) << (30 - 6))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[27 + inpos] >> 6) | ((in_[28 + inpos] & 15) << (30 - 4))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[28 + inpos] >> 4) | ((in_[29 + inpos] & 3) << (30 - 2))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[29 + inpos] >> 2)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack3(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 7) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 3) & 7) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 6) & 7) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[0 + inpos] >> 9) & 7) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[0 + inpos] >> 12) & 7) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[0 + inpos] >> 15) & 7) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[0 + inpos] >> 18) & 7) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[0 + inpos] >> 21) & 7) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[0 + inpos] >> 24) & 7) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[0 + inpos] >> 27) & 7) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 1) << (3 - 1))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[1 + inpos] >> 1) & 7) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[1 + inpos] >> 4) & 7) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[1 + inpos] >> 7) & 7) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[1 + inpos] >> 10) & 7) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[1 + inpos] >> 13) & 7) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[1 + inpos] >> 16) & 7) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[1 + inpos] >> 19) & 7) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[1 + inpos] >> 22) & 7) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[1 + inpos] >> 25) & 7) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[1 + inpos] >> 28) & 7) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[1 + inpos] >> 31) | ((in_[2 + inpos] & 3) << (3 - 2))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[2 + inpos] >> 2) & 7) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[2 + inpos] >> 5) & 7) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[2 + inpos] >> 8) & 7) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[2 + inpos] >> 11) & 7) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[2 + inpos] >> 14) & 7) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[2 + inpos] >> 17) & 7) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[2 + inpos] >> 20) & 7) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[2 + inpos] >> 23) & 7) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[2 + inpos] >> 26) & 7) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[2 + inpos] >> 29) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack29(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 536870911) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 29) | ((in_[1 + inpos] & 67108863) << (29 - 26))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 26) | ((in_[2 + inpos] & 8388607) << (29 - 23))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 23) | ((in_[3 + inpos] & 1048575) << (29 - 20))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 20) | ((in_[4 + inpos] & 131071) << (29 - 17))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[4 + inpos] >> 17) | ((in_[5 + inpos] & 16383) << (29 - 14))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[5 + inpos] >> 14) | ((in_[6 + inpos] & 2047) << (29 - 11))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[6 + inpos] >> 11) | ((in_[7 + inpos] & 255) << (29 - 8))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[7 + inpos] >> 8) | ((in_[8 + inpos] & 31) << (29 - 5))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[8 + inpos] >> 5) | ((in_[9 + inpos] & 3) << (29 - 2))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[9 + inpos] >> 2) & 536870911) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[9 + inpos] >> 31) | ((in_[10 + inpos] & 268435455) << (29 - 28))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[10 + inpos] >> 28) | ((in_[11 + inpos] & 33554431) << (29 - 25))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[11 + inpos] >> 25) | ((in_[12 + inpos] & 4194303) << (29 - 22))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[12 + inpos] >> 22) | ((in_[13 + inpos] & 524287) << (29 - 19))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[13 + inpos] >> 19) | ((in_[14 + inpos] & 65535) << (29 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[14 + inpos] >> 16) | ((in_[15 + inpos] & 8191) << (29 - 13))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[15 + inpos] >> 13) | ((in_[16 + inpos] & 1023) << (29 - 10))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[16 + inpos] >> 10) | ((in_[17 + inpos] & 127) << (29 - 7))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[17 + inpos] >> 7) | ((in_[18 + inpos] & 15) << (29 - 4))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[18 + inpos] >> 4) | ((in_[19 + inpos] & 1) << (29 - 1))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[19 + inpos] >> 1) & 536870911) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[19 + inpos] >> 30) | ((in_[20 + inpos] & 134217727) << (29 - 27))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[20 + inpos] >> 27) | ((in_[21 + inpos] & 16777215) << (29 - 24))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[21 + inpos] >> 24) | ((in_[22 + inpos] & 2097151) << (29 - 21))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[22 + inpos] >> 21) | ((in_[23 + inpos] & 262143) << (29 - 18))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[23 + inpos] >> 18) | ((in_[24 + inpos] & 32767) << (29 - 15))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[24 + inpos] >> 15) | ((in_[25 + inpos] & 4095) << (29 - 12))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[25 + inpos] >> 12) | ((in_[26 + inpos] & 511) << (29 - 9))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[26 + inpos] >> 9) | ((in_[27 + inpos] & 63) << (29 - 6))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[27 + inpos] >> 6) | ((in_[28 + inpos] & 7) << (29 - 3))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[28 + inpos] >> 3) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack28(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 268435455)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 28) | ((in_[1 + inpos] & 16777215) << (28 - 24))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 24) | ((in_[2 + inpos] & 1048575) << (28 - 20))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 20) | ((in_[3 + inpos] & 65535) << (28 - 16))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 16) | ((in_[4 + inpos] & 4095) << (28 - 12))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[4 + inpos] >> 12) | ((in_[5 + inpos] & 255) << (28 - 8))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[5 + inpos] >> 8) | ((in_[6 + inpos] & 15) << (28 - 4))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[6 + inpos] >> 4)) + out[7 + outpos - 1]
        out[8 + outpos] = (((in_[7 + inpos] >> 0) & 268435455)) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[7 + inpos] >> 28) | ((in_[8 + inpos] & 16777215) << (28 - 24))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[8 + inpos] >> 24) | ((in_[9 + inpos] & 1048575) << (28 - 20))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[9 + inpos] >> 20) | ((in_[10 + inpos] & 65535) << (28 - 16))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[10 + inpos] >> 16) | ((in_[11 + inpos] & 4095) << (28 - 12))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[11 + inpos] >> 12) | ((in_[12 + inpos] & 255) << (28 - 8))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[12 + inpos] >> 8) | ((in_[13 + inpos] & 15) << (28 - 4))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[13 + inpos] >> 4)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[14 + inpos] >> 0) & 268435455)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[14 + inpos] >> 28) | ((in_[15 + inpos] & 16777215) << (28 - 24))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[15 + inpos] >> 24) | ((in_[16 + inpos] & 1048575) << (28 - 20))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[16 + inpos] >> 20) | ((in_[17 + inpos] & 65535) << (28 - 16))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[17 + inpos] >> 16) | ((in_[18 + inpos] & 4095) << (28 - 12))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[18 + inpos] >> 12) | ((in_[19 + inpos] & 255) << (28 - 8))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[19 + inpos] >> 8) | ((in_[20 + inpos] & 15) << (28 - 4))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[20 + inpos] >> 4)) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[21 + inpos] >> 0) & 268435455)) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[21 + inpos] >> 28) | ((in_[22 + inpos] & 16777215) << (28 - 24))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[22 + inpos] >> 24) | ((in_[23 + inpos] & 1048575) << (28 - 20))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[23 + inpos] >> 20) | ((in_[24 + inpos] & 65535) << (28 - 16))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[24 + inpos] >> 16) | ((in_[25 + inpos] & 4095) << (28 - 12))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[25 + inpos] >> 12) | ((in_[26 + inpos] & 255) << (28 - 8))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[26 + inpos] >> 8) | ((in_[27 + inpos] & 15) << (28 - 4))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[27 + inpos] >> 4)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack27(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 134217727) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 27) | ((in_[1 + inpos] & 4194303) << (27 - 22))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 22) | ((in_[2 + inpos] & 131071) << (27 - 17))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 17) | ((in_[3 + inpos] & 4095) << (27 - 12))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 12) | ((in_[4 + inpos] & 127) << (27 - 7))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[4 + inpos] >> 7) | ((in_[5 + inpos] & 3) << (27 - 2))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[5 + inpos] >> 2) & 134217727) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[5 + inpos] >> 29) | ((in_[6 + inpos] & 16777215) << (27 - 24))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[6 + inpos] >> 24) | ((in_[7 + inpos] & 524287) << (27 - 19))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[7 + inpos] >> 19) | ((in_[8 + inpos] & 16383) << (27 - 14))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[8 + inpos] >> 14) | ((in_[9 + inpos] & 511) << (27 - 9))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[9 + inpos] >> 9) | ((in_[10 + inpos] & 15) << (27 - 4))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[10 + inpos] >> 4) & 134217727) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[10 + inpos] >> 31) | ((in_[11 + inpos] & 67108863) << (27 - 26))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[11 + inpos] >> 26) | ((in_[12 + inpos] & 2097151) << (27 - 21))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[12 + inpos] >> 21) | ((in_[13 + inpos] & 65535) << (27 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[13 + inpos] >> 16) | ((in_[14 + inpos] & 2047) << (27 - 11))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[14 + inpos] >> 11) | ((in_[15 + inpos] & 63) << (27 - 6))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[15 + inpos] >> 6) | ((in_[16 + inpos] & 1) << (27 - 1))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[16 + inpos] >> 1) & 134217727) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[16 + inpos] >> 28) | ((in_[17 + inpos] & 8388607) << (27 - 23))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[17 + inpos] >> 23) | ((in_[18 + inpos] & 262143) << (27 - 18))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[18 + inpos] >> 18) | ((in_[19 + inpos] & 8191) << (27 - 13))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[19 + inpos] >> 13) | ((in_[20 + inpos] & 255) << (27 - 8))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[20 + inpos] >> 8) | ((in_[21 + inpos] & 7) << (27 - 3))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[21 + inpos] >> 3) & 134217727) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[21 + inpos] >> 30) | ((in_[22 + inpos] & 33554431) << (27 - 25))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[22 + inpos] >> 25) | ((in_[23 + inpos] & 1048575) << (27 - 20))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[23 + inpos] >> 20) | ((in_[24 + inpos] & 32767) << (27 - 15))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[24 + inpos] >> 15) | ((in_[25 + inpos] & 1023) << (27 - 10))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[25 + inpos] >> 10) | ((in_[26 + inpos] & 31) << (27 - 5))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[26 + inpos] >> 5) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack26(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 67108863)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 26) | ((in_[1 + inpos] & 1048575) << (26 - 20))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 20) | ((in_[2 + inpos] & 16383) << (26 - 14))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 14) | ((in_[3 + inpos] & 255) << (26 - 8))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[3 + inpos] >> 8) | ((in_[4 + inpos] & 3) << (26 - 2))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (((in_[4 + inpos] >> 2) & 67108863)) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[4 + inpos] >> 28) | ((in_[5 + inpos] & 4194303) << (26 - 22))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[5 + inpos] >> 22) | ((in_[6 + inpos] & 65535) << (26 - 16))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[6 + inpos] >> 16) | ((in_[7 + inpos] & 1023) << (26 - 10))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[7 + inpos] >> 10) | ((in_[8 + inpos] & 15) << (26 - 4))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (((in_[8 + inpos] >> 4) & 67108863)) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[8 + inpos] >> 30) | ((in_[9 + inpos] & 16777215) << (26 - 24))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[9 + inpos] >> 24) | ((in_[10 + inpos] & 262143) << (26 - 18))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[10 + inpos] >> 18) | ((in_[11 + inpos] & 4095) << (26 - 12))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[11 + inpos] >> 12) | ((in_[12 + inpos] & 63) << (26 - 6))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[12 + inpos] >> 6)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[13 + inpos] >> 0) & 67108863)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[13 + inpos] >> 26) | ((in_[14 + inpos] & 1048575) << (26 - 20))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[14 + inpos] >> 20) | ((in_[15 + inpos] & 16383) << (26 - 14))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[15 + inpos] >> 14) | ((in_[16 + inpos] & 255) << (26 - 8))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[16 + inpos] >> 8) | ((in_[17 + inpos] & 3) << (26 - 2))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (((in_[17 + inpos] >> 2) & 67108863)) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[17 + inpos] >> 28) | ((in_[18 + inpos] & 4194303) << (26 - 22))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[18 + inpos] >> 22) | ((in_[19 + inpos] & 65535) << (26 - 16))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[19 + inpos] >> 16) | ((in_[20 + inpos] & 1023) << (26 - 10))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[20 + inpos] >> 10) | ((in_[21 + inpos] & 15) << (26 - 4))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (((in_[21 + inpos] >> 4) & 67108863)) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[21 + inpos] >> 30) | ((in_[22 + inpos] & 16777215) << (26 - 24))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[22 + inpos] >> 24) | ((in_[23 + inpos] & 262143) << (26 - 18))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[23 + inpos] >> 18) | ((in_[24 + inpos] & 4095) << (26 - 12))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[24 + inpos] >> 12) | ((in_[25 + inpos] & 63) << (26 - 6))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[25 + inpos] >> 6)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack25(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 33554431)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 25) | ((in_[1 + inpos] & 262143) << (25 - 18))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 18) | ((in_[2 + inpos] & 2047) << (25 - 11))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[2 + inpos] >> 11) | ((in_[3 + inpos] & 15) << (25 - 4))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (((in_[3 + inpos] >> 4) & 33554431)) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[3 + inpos] >> 29) | ((in_[4 + inpos] & 4194303) << (25 - 22))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[4 + inpos] >> 22) | ((in_[5 + inpos] & 32767) << (25 - 15))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[5 + inpos] >> 15) | ((in_[6 + inpos] & 255) << (25 - 8))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[6 + inpos] >> 8) | ((in_[7 + inpos] & 1) << (25 - 1))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (((in_[7 + inpos] >> 1) & 33554431)) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[7 + inpos] >> 26) | ((in_[8 + inpos] & 524287) << (25 - 19))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[8 + inpos] >> 19) | ((in_[9 + inpos] & 4095) << (25 - 12))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[9 + inpos] >> 12) | ((in_[10 + inpos] & 31) << (25 - 5))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (((in_[10 + inpos] >> 5) & 33554431)) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[10 + inpos] >> 30) | ((in_[11 + inpos] & 8388607) << (25 - 23))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[11 + inpos] >> 23) | ((in_[12 + inpos] & 65535) << (25 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[12 + inpos] >> 16) | ((in_[13 + inpos] & 511) << (25 - 9))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[13 + inpos] >> 9) | ((in_[14 + inpos] & 3) << (25 - 2))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (((in_[14 + inpos] >> 2) & 33554431)) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[14 + inpos] >> 27) | ((in_[15 + inpos] & 1048575) << (25 - 20))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[15 + inpos] >> 20) | ((in_[16 + inpos] & 8191) << (25 - 13))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[16 + inpos] >> 13) | ((in_[17 + inpos] & 63) << (25 - 6))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (((in_[17 + inpos] >> 6) & 33554431)) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[17 + inpos] >> 31) | ((in_[18 + inpos] & 16777215) << (25 - 24))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[18 + inpos] >> 24) | ((in_[19 + inpos] & 131071) << (25 - 17))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[19 + inpos] >> 17) | ((in_[20 + inpos] & 1023) << (25 - 10))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[20 + inpos] >> 10) | ((in_[21 + inpos] & 7) << (25 - 3))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (((in_[21 + inpos] >> 3) & 33554431)) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[21 + inpos] >> 28) | ((in_[22 + inpos] & 2097151) << (25 - 21))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[22 + inpos] >> 21) | ((in_[23 + inpos] & 16383) << (25 - 14))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[23 + inpos] >> 14) | ((in_[24 + inpos] & 127) << (25 - 7))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[24 + inpos] >> 7)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack24(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 16777215)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 24) | ((in_[1 + inpos] & 65535) << (24 - 16))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 16) | ((in_[2 + inpos] & 255) << (24 - 8))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[2 + inpos] >> 8)) + out[3 + outpos - 1]
        out[4 + outpos] = (((in_[3 + inpos] >> 0) & 16777215)) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 65535) << (24 - 16))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[4 + inpos] >> 16) | ((in_[5 + inpos] & 255) << (24 - 8))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[5 + inpos] >> 8)) + out[7 + outpos - 1]
        out[8 + outpos] = (((in_[6 + inpos] >> 0) & 16777215)) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[6 + inpos] >> 24) | ((in_[7 + inpos] & 65535) << (24 - 16))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[7 + inpos] >> 16) | ((in_[8 + inpos] & 255) << (24 - 8))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[8 + inpos] >> 8)) + out[11 + outpos - 1]
        out[12 + outpos] = (((in_[9 + inpos] >> 0) & 16777215)) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[9 + inpos] >> 24) | ((in_[10 + inpos] & 65535) << (24 - 16))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[10 + inpos] >> 16) | ((in_[11 + inpos] & 255) << (24 - 8))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[11 + inpos] >> 8)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[12 + inpos] >> 0) & 16777215)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[12 + inpos] >> 24) | ((in_[13 + inpos] & 65535) << (24 - 16))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[13 + inpos] >> 16) | ((in_[14 + inpos] & 255) << (24 - 8))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[14 + inpos] >> 8)) + out[19 + outpos - 1]
        out[20 + outpos] = (((in_[15 + inpos] >> 0) & 16777215)) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[15 + inpos] >> 24) | ((in_[16 + inpos] & 65535) << (24 - 16))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[16 + inpos] >> 16) | ((in_[17 + inpos] & 255) << (24 - 8))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[17 + inpos] >> 8)) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[18 + inpos] >> 0) & 16777215)) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[18 + inpos] >> 24) | ((in_[19 + inpos] & 65535) << (24 - 16))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[19 + inpos] >> 16) | ((in_[20 + inpos] & 255) << (24 - 8))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[20 + inpos] >> 8)) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[21 + inpos] >> 0) & 16777215)) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[21 + inpos] >> 24) | ((in_[22 + inpos] & 65535) << (24 - 16))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[22 + inpos] >> 16) | ((in_[23 + inpos] & 255) << (24 - 8))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[23 + inpos] >> 8)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack23(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 8388607)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 23) | ((in_[1 + inpos] & 16383) << (23 - 14))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 14) | ((in_[2 + inpos] & 31) << (23 - 5))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (((in_[2 + inpos] >> 5) & 8388607)) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[2 + inpos] >> 28) | ((in_[3 + inpos] & 524287) << (23 - 19))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[3 + inpos] >> 19) | ((in_[4 + inpos] & 1023) << (23 - 10))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[4 + inpos] >> 10) | ((in_[5 + inpos] & 1) << (23 - 1))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (((in_[5 + inpos] >> 1) & 8388607)) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[5 + inpos] >> 24) | ((in_[6 + inpos] & 32767) << (23 - 15))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[6 + inpos] >> 15) | ((in_[7 + inpos] & 63) << (23 - 6))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (((in_[7 + inpos] >> 6) & 8388607)) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[7 + inpos] >> 29) | ((in_[8 + inpos] & 1048575) << (23 - 20))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[8 + inpos] >> 20) | ((in_[9 + inpos] & 2047) << (23 - 11))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[9 + inpos] >> 11) | ((in_[10 + inpos] & 3) << (23 - 2))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (((in_[10 + inpos] >> 2) & 8388607)) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[10 + inpos] >> 25) | ((in_[11 + inpos] & 65535) << (23 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[11 + inpos] >> 16) | ((in_[12 + inpos] & 127) << (23 - 7))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (((in_[12 + inpos] >> 7) & 8388607)) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[12 + inpos] >> 30) | ((in_[13 + inpos] & 2097151) << (23 - 21))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[13 + inpos] >> 21) | ((in_[14 + inpos] & 4095) << (23 - 12))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[14 + inpos] >> 12) | ((in_[15 + inpos] & 7) << (23 - 3))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (((in_[15 + inpos] >> 3) & 8388607)) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[15 + inpos] >> 26) | ((in_[16 + inpos] & 131071) << (23 - 17))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[16 + inpos] >> 17) | ((in_[17 + inpos] & 255) << (23 - 8))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[17 + inpos] >> 8) & 8388607)) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[17 + inpos] >> 31) | ((in_[18 + inpos] & 4194303) << (23 - 22))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[18 + inpos] >> 22) | ((in_[19 + inpos] & 8191) << (23 - 13))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[19 + inpos] >> 13) | ((in_[20 + inpos] & 15) << (23 - 4))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[20 + inpos] >> 4) & 8388607)) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[20 + inpos] >> 27) | ((in_[21 + inpos] & 262143) << (23 - 18))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[21 + inpos] >> 18) | ((in_[22 + inpos] & 511) << (23 - 9))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[22 + inpos] >> 9)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack22(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 4194303)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 22) | ((in_[1 + inpos] & 4095) << (22 - 12))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[1 + inpos] >> 12) | ((in_[2 + inpos] & 3) << (22 - 2))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (((in_[2 + inpos] >> 2) & 4194303)) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[2 + inpos] >> 24) | ((in_[3 + inpos] & 16383) << (22 - 14))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[3 + inpos] >> 14) | ((in_[4 + inpos] & 15) << (22 - 4))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (((in_[4 + inpos] >> 4) & 4194303)) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[4 + inpos] >> 26) | ((in_[5 + inpos] & 65535) << (22 - 16))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[5 + inpos] >> 16) | ((in_[6 + inpos] & 63) << (22 - 6))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (((in_[6 + inpos] >> 6) & 4194303)) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[6 + inpos] >> 28) | ((in_[7 + inpos] & 262143) << (22 - 18))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[7 + inpos] >> 18) | ((in_[8 + inpos] & 255) << (22 - 8))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (((in_[8 + inpos] >> 8) & 4194303)) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[8 + inpos] >> 30) | ((in_[9 + inpos] & 1048575) << (22 - 20))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[9 + inpos] >> 20) | ((in_[10 + inpos] & 1023) << (22 - 10))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[10 + inpos] >> 10)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[11 + inpos] >> 0) & 4194303)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[11 + inpos] >> 22) | ((in_[12 + inpos] & 4095) << (22 - 12))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[12 + inpos] >> 12) | ((in_[13 + inpos] & 3) << (22 - 2))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (((in_[13 + inpos] >> 2) & 4194303)) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[13 + inpos] >> 24) | ((in_[14 + inpos] & 16383) << (22 - 14))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[14 + inpos] >> 14) | ((in_[15 + inpos] & 15) << (22 - 4))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (((in_[15 + inpos] >> 4) & 4194303)) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[15 + inpos] >> 26) | ((in_[16 + inpos] & 65535) << (22 - 16))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[16 + inpos] >> 16) | ((in_[17 + inpos] & 63) << (22 - 6))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (((in_[17 + inpos] >> 6) & 4194303)) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[17 + inpos] >> 28) | ((in_[18 + inpos] & 262143) << (22 - 18))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[18 + inpos] >> 18) | ((in_[19 + inpos] & 255) << (22 - 8))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[19 + inpos] >> 8) & 4194303)) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[19 + inpos] >> 30) | ((in_[20 + inpos] & 1048575) << (22 - 20))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[20 + inpos] >> 20) | ((in_[21 + inpos] & 1023) << (22 - 10))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[21 + inpos] >> 10)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack21(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def _integratedunpack20(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 1048575) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 20) | ((in_[1 + inpos] & 255) << (20 - 8))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[1 + inpos] >> 8) & 1048575) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 65535) << (20 - 16))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[2 + inpos] >> 16) | ((in_[3 + inpos] & 15) << (20 - 4))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[3 + inpos] >> 4) & 1048575) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 4095) << (20 - 12))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[4 + inpos] >> 12)) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[5 + inpos] >> 0) & 1048575) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[5 + inpos] >> 20) | ((in_[6 + inpos] & 255) << (20 - 8))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[6 + inpos] >> 8) & 1048575) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[6 + inpos] >> 28) | ((in_[7 + inpos] & 65535) << (20 - 16))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[7 + inpos] >> 16) | ((in_[8 + inpos] & 15) << (20 - 4))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[8 + inpos] >> 4) & 1048575) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[8 + inpos] >> 24) | ((in_[9 + inpos] & 4095) << (20 - 12))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[9 + inpos] >> 12)) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[10 + inpos] >> 0) & 1048575) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[10 + inpos] >> 20) | ((in_[11 + inpos] & 255) << (20 - 8))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[11 + inpos] >> 8) & 1048575) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[11 + inpos] >> 28) | ((in_[12 + inpos] & 65535) << (20 - 16))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[12 + inpos] >> 16) | ((in_[13 + inpos] & 15) << (20 - 4))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[13 + inpos] >> 4) & 1048575) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[13 + inpos] >> 24) | ((in_[14 + inpos] & 4095) << (20 - 12))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[14 + inpos] >> 12)) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[15 + inpos] >> 0) & 1048575) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[15 + inpos] >> 20) | ((in_[16 + inpos] & 255) << (20 - 8))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[16 + inpos] >> 8) & 1048575) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[16 + inpos] >> 28) | ((in_[17 + inpos] & 65535) << (20 - 16))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[17 + inpos] >> 16) | ((in_[18 + inpos] & 15) << (20 - 4))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[18 + inpos] >> 4) & 1048575) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[18 + inpos] >> 24) | ((in_[19 + inpos] & 4095) << (20 - 12))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[19 + inpos] >> 12)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack2(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 3) + initoffset
        for i in range(1, 32):
            if i < 16:
                out[i + outpos] = ((in_[0 + inpos] >> (i * 2)) & 3) + out[
                    i + outpos - 1
                ]
            else:
                out[i + outpos] = ((in_[1 + inpos] >> ((i - 16) * 2)) & 3) + out[
                    i + outpos - 1
                ]

    @staticmethod
    def _integratedunpack19(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 524287)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 19) | ((in_[1 + inpos] & 63) << (19 - 6))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (((in_[1 + inpos] >> 6) & 524287)) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[1 + inpos] >> 25) | ((in_[2 + inpos] & 4095) << (19 - 12))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (((in_[2 + inpos] >> 12) & 524287)) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[2 + inpos] >> 31) | ((in_[3 + inpos] & 262143) << (19 - 18))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[3 + inpos] >> 18) | ((in_[4 + inpos] & 31) << (19 - 5))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (((in_[4 + inpos] >> 5) & 524287)) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[4 + inpos] >> 24) | ((in_[5 + inpos] & 2047) << (19 - 11))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (((in_[5 + inpos] >> 11) & 524287)) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[5 + inpos] >> 30) | ((in_[6 + inpos] & 131071) << (19 - 17))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[6 + inpos] >> 17) | ((in_[7 + inpos] & 15) << (19 - 4))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (((in_[7 + inpos] >> 4) & 524287)) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[7 + inpos] >> 23) | ((in_[8 + inpos] & 1023) << (19 - 10))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (((in_[8 + inpos] >> 10) & 524287)) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[8 + inpos] >> 29) | ((in_[9 + inpos] & 65535) << (19 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[9 + inpos] >> 16) | ((in_[10 + inpos] & 7) << (19 - 3))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (((in_[10 + inpos] >> 3) & 524287)) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[10 + inpos] >> 22) | ((in_[11 + inpos] & 511) << (19 - 9))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (((in_[11 + inpos] >> 9) & 524287)) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[11 + inpos] >> 28) | ((in_[12 + inpos] & 32767) << (19 - 15))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[12 + inpos] >> 15) | ((in_[13 + inpos] & 3) << (19 - 2))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (((in_[13 + inpos] >> 2) & 524287)) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[13 + inpos] >> 21) | ((in_[14 + inpos] & 255) << (19 - 8))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[14 + inpos] >> 8) & 524287)) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[14 + inpos] >> 27) | ((in_[15 + inpos] & 16383) << (19 - 14))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[15 + inpos] >> 14) | ((in_[16 + inpos] & 1) << (19 - 1))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (((in_[16 + inpos] >> 1) & 524287)) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[16 + inpos] >> 20) | ((in_[17 + inpos] & 127) << (19 - 7))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (((in_[17 + inpos] >> 7) & 524287)) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[17 + inpos] >> 26) | ((in_[18 + inpos] & 8191) << (19 - 13))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[18 + inpos] >> 13)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack18(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 262143)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 18) | ((in_[1 + inpos] & 15) << (18 - 4))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (((in_[1 + inpos] >> 4) & 262143)) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[1 + inpos] >> 22) | ((in_[2 + inpos] & 255) << (18 - 8))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (((in_[2 + inpos] >> 8) & 262143)) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[2 + inpos] >> 26) | ((in_[3 + inpos] & 4095) << (18 - 12))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (((in_[3 + inpos] >> 12) & 262143)) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[3 + inpos] >> 30) | ((in_[4 + inpos] & 65535) << (18 - 16))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[4 + inpos] >> 16) | ((in_[5 + inpos] & 3) << (18 - 2))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (((in_[5 + inpos] >> 2) & 262143)) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[5 + inpos] >> 20) | ((in_[6 + inpos] & 63) << (18 - 6))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (((in_[6 + inpos] >> 6) & 262143)) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[6 + inpos] >> 24) | ((in_[7 + inpos] & 1023) << (18 - 10))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (((in_[7 + inpos] >> 10) & 262143)) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[7 + inpos] >> 28) | ((in_[8 + inpos] & 16383) << (18 - 14))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[8 + inpos] >> 14)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[9 + inpos] >> 0) & 262143)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[9 + inpos] >> 18) | ((in_[10 + inpos] & 15) << (18 - 4))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (((in_[10 + inpos] >> 4) & 262143)) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[10 + inpos] >> 22) | ((in_[11 + inpos] & 255) << (18 - 8))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (((in_[11 + inpos] >> 8) & 262143)) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[11 + inpos] >> 26) | ((in_[12 + inpos] & 4095) << (18 - 12))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (((in_[12 + inpos] >> 12) & 262143)) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[12 + inpos] >> 30) | ((in_[13 + inpos] & 65535) << (18 - 16))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[13 + inpos] >> 16) | ((in_[14 + inpos] & 3) << (18 - 2))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (((in_[14 + inpos] >> 2) & 262143)) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[14 + inpos] >> 20) | ((in_[15 + inpos] & 63) << (18 - 6))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (((in_[15 + inpos] >> 6) & 262143)) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[15 + inpos] >> 24) | ((in_[16 + inpos] & 1023) << (18 - 10))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (((in_[16 + inpos] >> 10) & 262143)) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[16 + inpos] >> 28) | ((in_[17 + inpos] & 16383) << (18 - 14))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[17 + inpos] >> 14)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack17(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 131071)) + initoffset
        out[1 + outpos] = (
            (in_[0 + inpos] >> 17) | ((in_[1 + inpos] & 3) << (17 - 2))
        ) + out[1 + outpos - 1]
        out[2 + outpos] = (((in_[1 + inpos] >> 2) & 131071)) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[1 + inpos] >> 19) | ((in_[2 + inpos] & 15) << (17 - 4))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = (((in_[2 + inpos] >> 4) & 131071)) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[2 + inpos] >> 21) | ((in_[3 + inpos] & 63) << (17 - 6))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = (((in_[3 + inpos] >> 6) & 131071)) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[3 + inpos] >> 23) | ((in_[4 + inpos] & 255) << (17 - 8))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (((in_[4 + inpos] >> 8) & 131071)) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[4 + inpos] >> 25) | ((in_[5 + inpos] & 1023) << (17 - 10))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (((in_[5 + inpos] >> 10) & 131071)) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[5 + inpos] >> 27) | ((in_[6 + inpos] & 4095) << (17 - 12))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = (((in_[6 + inpos] >> 12) & 131071)) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[6 + inpos] >> 29) | ((in_[7 + inpos] & 16383) << (17 - 14))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = (((in_[7 + inpos] >> 14) & 131071)) + out[14 + outpos - 1]
        out[15 + outpos] = (
            (in_[7 + inpos] >> 31) | ((in_[8 + inpos] & 65535) << (17 - 16))
        ) + out[15 + outpos - 1]
        out[16 + outpos] = (
            (in_[8 + inpos] >> 16) | ((in_[9 + inpos] & 1) << (17 - 1))
        ) + out[16 + outpos - 1]
        out[17 + outpos] = (((in_[9 + inpos] >> 1) & 131071)) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[9 + inpos] >> 18) | ((in_[10 + inpos] & 7) << (17 - 3))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = (((in_[10 + inpos] >> 3) & 131071)) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[10 + inpos] >> 20) | ((in_[11 + inpos] & 31) << (17 - 5))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = (((in_[11 + inpos] >> 5) & 131071)) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[11 + inpos] >> 22) | ((in_[12 + inpos] & 127) << (17 - 7))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (((in_[12 + inpos] >> 7) & 131071)) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[12 + inpos] >> 24) | ((in_[13 + inpos] & 511) << (17 - 9))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (((in_[13 + inpos] >> 9) & 131071)) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[13 + inpos] >> 26) | ((in_[14 + inpos] & 2047) << (17 - 11))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = (((in_[14 + inpos] >> 11) & 131071)) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[14 + inpos] >> 28) | ((in_[15 + inpos] & 8191) << (17 - 13))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = (((in_[15 + inpos] >> 13) & 131071)) + out[29 + outpos - 1]
        out[30 + outpos] = (
            (in_[15 + inpos] >> 30) | ((in_[16 + inpos] & 32767) << (17 - 15))
        ) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[16 + inpos] >> 15)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack16(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 65535) + initoffset
        out[1 + outpos] = (in_[0 + inpos] >> 16) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[1 + inpos] >> 0) & 65535) + out[2 + outpos - 1]
        out[3 + outpos] = (in_[1 + inpos] >> 16) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[2 + inpos] >> 0) & 65535) + out[4 + outpos - 1]
        out[5 + outpos] = (in_[2 + inpos] >> 16) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[3 + inpos] >> 0) & 65535) + out[6 + outpos - 1]
        out[7 + outpos] = (in_[3 + inpos] >> 16) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[4 + inpos] >> 0) & 65535) + out[8 + outpos - 1]
        out[9 + outpos] = (in_[4 + inpos] >> 16) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[5 + inpos] >> 0) & 65535) + out[10 + outpos - 1]
        out[11 + outpos] = (in_[5 + inpos] >> 16) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[6 + inpos] >> 0) & 65535) + out[12 + outpos - 1]
        out[13 + outpos] = (in_[6 + inpos] >> 16) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[7 + inpos] >> 0) & 65535) + out[14 + outpos - 1]
        out[15 + outpos] = (in_[7 + inpos] >> 16) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[8 + inpos] >> 0) & 65535) + out[16 + outpos - 1]
        out[17 + outpos] = (in_[8 + inpos] >> 16) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[9 + inpos] >> 0) & 65535) + out[18 + outpos - 1]
        out[19 + outpos] = (in_[9 + inpos] >> 16) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[10 + inpos] >> 0) & 65535) + out[20 + outpos - 1]
        out[21 + outpos] = (in_[10 + inpos] >> 16) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[11 + inpos] >> 0) & 65535) + out[22 + outpos - 1]
        out[23 + outpos] = (in_[11 + inpos] >> 16) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[12 + inpos] >> 0) & 65535) + out[24 + outpos - 1]
        out[25 + outpos] = (in_[12 + inpos] >> 16) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[13 + inpos] >> 0) & 65535) + out[26 + outpos - 1]
        out[27 + outpos] = (in_[13 + inpos] >> 16) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[14 + inpos] >> 0) & 65535) + out[28 + outpos - 1]
        out[29 + outpos] = (in_[14 + inpos] >> 16) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[15 + inpos] >> 0) & 65535) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[15 + inpos] >> 16) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack15(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 32767)) + initoffset
        out[1 + outpos] = (((in_[0 + inpos] >> 15) & 32767)) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 8191) << (15 - 13))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (((in_[1 + inpos] >> 13) & 32767)) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 2047) << (15 - 11))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (((in_[2 + inpos] >> 11) & 32767)) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[2 + inpos] >> 26) | ((in_[3 + inpos] & 511) << (15 - 9))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = (((in_[3 + inpos] >> 9) & 32767)) + out[7 + outpos - 1]
        out[8 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 127) << (15 - 7))
        ) + out[8 + outpos - 1]
        out[9 + outpos] = (((in_[4 + inpos] >> 7) & 32767)) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[4 + inpos] >> 22) | ((in_[5 + inpos] & 31) << (15 - 5))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = (((in_[5 + inpos] >> 5) & 32767)) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[5 + inpos] >> 20) | ((in_[6 + inpos] & 7) << (15 - 3))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (((in_[6 + inpos] >> 3) & 32767)) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[6 + inpos] >> 18) | ((in_[7 + inpos] & 1) << (15 - 1))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (((in_[7 + inpos] >> 1) & 32767)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[7 + inpos] >> 16) & 32767)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[7 + inpos] >> 31) | ((in_[8 + inpos] & 16383) << (15 - 14))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (((in_[8 + inpos] >> 14) & 32767)) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[8 + inpos] >> 29) | ((in_[9 + inpos] & 4095) << (15 - 12))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (((in_[9 + inpos] >> 12) & 32767)) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[9 + inpos] >> 27) | ((in_[10 + inpos] & 1023) << (15 - 10))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = (((in_[10 + inpos] >> 10) & 32767)) + out[22 + outpos - 1]
        out[23 + outpos] = (
            (in_[10 + inpos] >> 25) | ((in_[11 + inpos] & 255) << (15 - 8))
        ) + out[23 + outpos - 1]
        out[24 + outpos] = (((in_[11 + inpos] >> 8) & 32767)) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[11 + inpos] >> 23) | ((in_[12 + inpos] & 63) << (15 - 6))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = (((in_[12 + inpos] >> 6) & 32767)) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[12 + inpos] >> 21) | ((in_[13 + inpos] & 15) << (15 - 4))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[13 + inpos] >> 4) & 32767)) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[13 + inpos] >> 19) | ((in_[14 + inpos] & 3) << (15 - 2))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (((in_[14 + inpos] >> 2) & 32767)) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[14 + inpos] >> 17)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack14(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 16383) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 14) & 16383) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[0 + inpos] >> 28) | ((in_[1 + inpos] & 1023) << (14 - 10))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[1 + inpos] >> 10) & 16383) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[1 + inpos] >> 24) | ((in_[2 + inpos] & 63) << (14 - 6))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[2 + inpos] >> 6) & 16383) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[2 + inpos] >> 20) | ((in_[3 + inpos] & 3) << (14 - 2))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[3 + inpos] >> 2) & 16383) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[3 + inpos] >> 16) & 16383) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[3 + inpos] >> 30) | ((in_[4 + inpos] & 4095) << (14 - 12))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[4 + inpos] >> 12) & 16383) + out[10 + outpos - 1]
        out[11 + outpos] = (
            (in_[4 + inpos] >> 26) | ((in_[5 + inpos] & 255) << (14 - 8))
        ) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[5 + inpos] >> 8) & 16383) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[5 + inpos] >> 22) | ((in_[6 + inpos] & 15) << (14 - 4))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[6 + inpos] >> 4) & 16383) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[6 + inpos] >> 18)) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[7 + inpos] >> 0) & 16383) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[7 + inpos] >> 14) & 16383) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[7 + inpos] >> 28) | ((in_[8 + inpos] & 1023) << (14 - 10))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[8 + inpos] >> 10) & 16383) + out[19 + outpos - 1]
        out[20 + outpos] = (
            (in_[8 + inpos] >> 24) | ((in_[9 + inpos] & 63) << (14 - 6))
        ) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[9 + inpos] >> 6) & 16383) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[9 + inpos] >> 20) | ((in_[10 + inpos] & 3) << (14 - 2))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[10 + inpos] >> 2) & 16383) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[10 + inpos] >> 16) & 16383) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[10 + inpos] >> 30) | ((in_[11 + inpos] & 4095) << (14 - 12))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[11 + inpos] >> 12) & 16383) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[11 + inpos] >> 26) | ((in_[12 + inpos] & 255) << (14 - 8))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[12 + inpos] >> 8) & 16383) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[12 + inpos] >> 22) | ((in_[13 + inpos] & 15) << (14 - 4))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[13 + inpos] >> 4) & 16383) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[13 + inpos] >> 18)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack13(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (((in_[0 + inpos] >> 0) & 8191)) + initoffset
        out[1 + outpos] = (((in_[0 + inpos] >> 13) & 8191)) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[0 + inpos] >> 26) | ((in_[1 + inpos] & 127) << (13 - 7))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = (((in_[1 + inpos] >> 7) & 8191)) + out[3 + outpos - 1]
        out[4 + outpos] = (
            (in_[1 + inpos] >> 20) | ((in_[2 + inpos] & 1) << (13 - 1))
        ) + out[4 + outpos - 1]
        out[5 + outpos] = (((in_[2 + inpos] >> 1) & 8191)) + out[5 + outpos - 1]
        out[6 + outpos] = (((in_[2 + inpos] >> 14) & 8191)) + out[6 + outpos - 1]
        out[7 + outpos] = (
            (in_[2 + inpos] >> 27) | ((in_[3 + inpos] & 255) << (13 - 8))
        ) + out[7 + outpos - 1]
        out[8 + outpos] = (((in_[3 + inpos] >> 8) & 8191)) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[3 + inpos] >> 21) | ((in_[4 + inpos] & 3) << (13 - 2))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = (((in_[4 + inpos] >> 2) & 8191)) + out[10 + outpos - 1]
        out[11 + outpos] = (((in_[4 + inpos] >> 15) & 8191)) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[4 + inpos] >> 28) | ((in_[5 + inpos] & 511) << (13 - 9))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = (((in_[5 + inpos] >> 9) & 8191)) + out[13 + outpos - 1]
        out[14 + outpos] = (
            (in_[5 + inpos] >> 22) | ((in_[6 + inpos] & 7) << (13 - 3))
        ) + out[14 + outpos - 1]
        out[15 + outpos] = (((in_[6 + inpos] >> 3) & 8191)) + out[15 + outpos - 1]
        out[16 + outpos] = (((in_[6 + inpos] >> 16) & 8191)) + out[16 + outpos - 1]
        out[17 + outpos] = (
            (in_[6 + inpos] >> 29) | ((in_[7 + inpos] & 1023) << (13 - 10))
        ) + out[17 + outpos - 1]
        out[18 + outpos] = (((in_[7 + inpos] >> 10) & 8191)) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[7 + inpos] >> 23) | ((in_[8 + inpos] & 15) << (13 - 4))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = (((in_[8 + inpos] >> 4) & 8191)) + out[20 + outpos - 1]
        out[21 + outpos] = (((in_[8 + inpos] >> 17) & 8191)) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[8 + inpos] >> 30) | ((in_[9 + inpos] & 2047) << (13 - 11))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = (((in_[9 + inpos] >> 11) & 8191)) + out[23 + outpos - 1]
        out[24 + outpos] = (
            (in_[9 + inpos] >> 24) | ((in_[10 + inpos] & 31) << (13 - 5))
        ) + out[24 + outpos - 1]
        out[25 + outpos] = (((in_[10 + inpos] >> 5) & 8191)) + out[25 + outpos - 1]
        out[26 + outpos] = (((in_[10 + inpos] >> 18) & 8191)) + out[26 + outpos - 1]
        out[27 + outpos] = (
            (in_[10 + inpos] >> 31) | ((in_[11 + inpos] & 4095) << (13 - 12))
        ) + out[27 + outpos - 1]
        out[28 + outpos] = (((in_[11 + inpos] >> 12) & 8191)) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[11 + inpos] >> 25) | ((in_[12 + inpos] & 63) << (13 - 6))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = (((in_[12 + inpos] >> 6) & 8191)) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[12 + inpos] >> 19)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack12(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 4095) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 12) & 4095) + out[1 + outpos - 1]
        out[2 + outpos] = (
            (in_[0 + inpos] >> 24) | ((in_[1 + inpos] & 15) << (12 - 4))
        ) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[1 + inpos] >> 4) & 4095) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[1 + inpos] >> 16) & 4095) + out[4 + outpos - 1]
        out[5 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 255) << (12 - 8))
        ) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[2 + inpos] >> 8) & 4095) + out[6 + outpos - 1]
        out[7 + outpos] = (in_[2 + inpos] >> 20) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[3 + inpos] >> 0) & 4095) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[3 + inpos] >> 12) & 4095) + out[9 + outpos - 1]
        out[10 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 15) << (12 - 4))
        ) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[4 + inpos] >> 4) & 4095) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[4 + inpos] >> 16) & 4095) + out[12 + outpos - 1]
        out[13 + outpos] = (
            (in_[4 + inpos] >> 28) | ((in_[5 + inpos] & 255) << (12 - 8))
        ) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[5 + inpos] >> 8) & 4095) + out[14 + outpos - 1]
        out[15 + outpos] = (in_[5 + inpos] >> 20) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[6 + inpos] >> 0) & 4095) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[6 + inpos] >> 12) & 4095) + out[17 + outpos - 1]
        out[18 + outpos] = (
            (in_[6 + inpos] >> 24) | ((in_[7 + inpos] & 15) << (12 - 4))
        ) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[7 + inpos] >> 4) & 4095) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[7 + inpos] >> 16) & 4095) + out[20 + outpos - 1]
        out[21 + outpos] = (
            (in_[7 + inpos] >> 28) | ((in_[8 + inpos] & 255) << (12 - 8))
        ) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[8 + inpos] >> 8) & 4095) + out[22 + outpos - 1]
        out[23 + outpos] = (in_[8 + inpos] >> 20) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[9 + inpos] >> 0) & 4095) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[9 + inpos] >> 12) & 4095) + out[25 + outpos - 1]
        out[26 + outpos] = (
            (in_[9 + inpos] >> 24) | ((in_[10 + inpos] & 15) << (12 - 4))
        ) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[10 + inpos] >> 4) & 4095) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[10 + inpos] >> 16) & 4095) + out[28 + outpos - 1]
        out[29 + outpos] = (
            (in_[10 + inpos] >> 28) | ((in_[11 + inpos] & 255) << (12 - 8))
        ) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[11 + inpos] >> 8) & 4095) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[11 + inpos] >> 20) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack11(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 2047) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 11) & 2047) + out[0 + outpos]
        out[2 + outpos] = (
            (in_[0 + inpos] >> 22) | ((in_[1 + inpos] & 1) << (11 - 1))
        ) + out[1 + outpos]
        out[3 + outpos] = ((in_[1 + inpos] >> 1) & 2047) + out[2 + outpos]
        out[4 + outpos] = ((in_[1 + inpos] >> 12) & 2047) + out[3 + outpos]
        out[5 + outpos] = (
            (in_[1 + inpos] >> 23) | ((in_[2 + inpos] & 3) << (11 - 2))
        ) + out[4 + outpos]
        out[6 + outpos] = ((in_[2 + inpos] >> 2) & 2047) + out[5 + outpos]
        out[7 + outpos] = ((in_[2 + inpos] >> 13) & 2047) + out[6 + outpos]
        out[8 + outpos] = (
            (in_[2 + inpos] >> 24) | ((in_[3 + inpos] & 7) << (11 - 3))
        ) + out[7 + outpos]
        out[9 + outpos] = ((in_[3 + inpos] >> 3) & 2047) + out[8 + outpos]
        out[10 + outpos] = ((in_[3 + inpos] >> 14) & 2047) + out[9 + outpos]
        out[11 + outpos] = (
            (in_[3 + inpos] >> 25) | ((in_[4 + inpos] & 15) << (11 - 4))
        ) + out[10 + outpos]
        out[12 + outpos] = ((in_[4 + inpos] >> 4) & 2047) + out[11 + outpos]
        out[13 + outpos] = ((in_[4 + inpos] >> 15) & 2047) + out[12 + outpos]
        out[14 + outpos] = (
            (in_[4 + inpos] >> 26) | ((in_[5 + inpos] & 31) << (11 - 5))
        ) + out[13 + outpos]
        out[15 + outpos] = ((in_[5 + inpos] >> 5) & 2047) + out[14 + outpos]
        out[16 + outpos] = ((in_[5 + inpos] >> 16) & 2047) + out[15 + outpos]
        out[17 + outpos] = (
            (in_[5 + inpos] >> 27) | ((in_[6 + inpos] & 63) << (11 - 6))
        ) + out[16 + outpos]
        out[18 + outpos] = ((in_[6 + inpos] >> 6) & 2047) + out[17 + outpos]
        out[19 + outpos] = ((in_[6 + inpos] >> 17) & 2047) + out[18 + outpos]
        out[20 + outpos] = (
            (in_[6 + inpos] >> 28) | ((in_[7 + inpos] & 127) << (11 - 7))
        ) + out[19 + outpos]
        out[21 + outpos] = ((in_[7 + inpos] >> 7) & 2047) + out[20 + outpos]
        out[22 + outpos] = ((in_[7 + inpos] >> 18) & 2047) + out[21 + outpos]
        out[23 + outpos] = (
            (in_[7 + inpos] >> 29) | ((in_[8 + inpos] & 255) << (11 - 8))
        ) + out[22 + outpos]
        out[24 + outpos] = ((in_[8 + inpos] >> 8) & 2047) + out[23 + outpos]
        out[25 + outpos] = ((in_[8 + inpos] >> 19) & 2047) + out[24 + outpos]
        out[26 + outpos] = (
            (in_[8 + inpos] >> 30) | ((in_[9 + inpos] & 511) << (11 - 9))
        ) + out[25 + outpos]
        out[27 + outpos] = ((in_[9 + inpos] >> 9) & 2047) + out[26 + outpos]
        out[28 + outpos] = ((in_[9 + inpos] >> 20) & 2047) + out[27 + outpos]
        out[29 + outpos] = (
            (in_[9 + inpos] >> 31) | ((in_[10 + inpos] & 1023) << (11 - 10))
        ) + out[28 + outpos]
        out[30 + outpos] = ((in_[10 + inpos] >> 10) & 2047) + out[29 + outpos]
        out[31 + outpos] = (in_[10 + inpos] >> 21) + out[30 + outpos]

    @staticmethod
    def _integratedunpack10(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 1023) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 10) & 1023) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 20) & 1023) + out[2 + outpos - 1]
        out[3 + outpos] = (
            (in_[0 + inpos] >> 30) | ((in_[1 + inpos] & 255) << (10 - 8))
        ) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[1 + inpos] >> 8) & 1023) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[1 + inpos] >> 18) & 1023) + out[5 + outpos - 1]
        out[6 + outpos] = (
            (in_[1 + inpos] >> 28) | ((in_[2 + inpos] & 63) << (10 - 6))
        ) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[2 + inpos] >> 6) & 1023) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[2 + inpos] >> 16) & 1023) + out[8 + outpos - 1]
        out[9 + outpos] = (
            (in_[2 + inpos] >> 26) | ((in_[3 + inpos] & 15) << (10 - 4))
        ) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[3 + inpos] >> 4) & 1023) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[3 + inpos] >> 14) & 1023) + out[11 + outpos - 1]
        out[12 + outpos] = (
            (in_[3 + inpos] >> 24) | ((in_[4 + inpos] & 3) << (10 - 2))
        ) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[4 + inpos] >> 2) & 1023) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[4 + inpos] >> 12) & 1023) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[4 + inpos] >> 22)) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[5 + inpos] >> 0) & 1023) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[5 + inpos] >> 10) & 1023) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[5 + inpos] >> 20) & 1023) + out[18 + outpos - 1]
        out[19 + outpos] = (
            (in_[5 + inpos] >> 30) | ((in_[6 + inpos] & 255) << (10 - 8))
        ) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[6 + inpos] >> 8) & 1023) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[6 + inpos] >> 18) & 1023) + out[21 + outpos - 1]
        out[22 + outpos] = (
            (in_[6 + inpos] >> 28) | ((in_[7 + inpos] & 63) << (10 - 6))
        ) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[7 + inpos] >> 6) & 1023) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[7 + inpos] >> 16) & 1023) + out[24 + outpos - 1]
        out[25 + outpos] = (
            (in_[7 + inpos] >> 26) | ((in_[8 + inpos] & 15) << (10 - 4))
        ) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[8 + inpos] >> 4) & 1023) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[8 + inpos] >> 14) & 1023) + out[27 + outpos - 1]
        out[28 + outpos] = (
            (in_[8 + inpos] >> 24) | ((in_[9 + inpos] & 3) << (10 - 2))
        ) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[9 + inpos] >> 2) & 1023) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[9 + inpos] >> 12) & 1023) + out[30 + outpos - 1]
        out[31 + outpos] = ((in_[9 + inpos] >> 22)) + out[31 + outpos - 1]

    @staticmethod
    def _integratedunpack1(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = ((in_[0 + inpos] >> 0) & 1) + initoffset
        out[1 + outpos] = ((in_[0 + inpos] >> 1) & 1) + out[1 + outpos - 1]
        out[2 + outpos] = ((in_[0 + inpos] >> 2) & 1) + out[2 + outpos - 1]
        out[3 + outpos] = ((in_[0 + inpos] >> 3) & 1) + out[3 + outpos - 1]
        out[4 + outpos] = ((in_[0 + inpos] >> 4) & 1) + out[4 + outpos - 1]
        out[5 + outpos] = ((in_[0 + inpos] >> 5) & 1) + out[5 + outpos - 1]
        out[6 + outpos] = ((in_[0 + inpos] >> 6) & 1) + out[6 + outpos - 1]
        out[7 + outpos] = ((in_[0 + inpos] >> 7) & 1) + out[7 + outpos - 1]
        out[8 + outpos] = ((in_[0 + inpos] >> 8) & 1) + out[8 + outpos - 1]
        out[9 + outpos] = ((in_[0 + inpos] >> 9) & 1) + out[9 + outpos - 1]
        out[10 + outpos] = ((in_[0 + inpos] >> 10) & 1) + out[10 + outpos - 1]
        out[11 + outpos] = ((in_[0 + inpos] >> 11) & 1) + out[11 + outpos - 1]
        out[12 + outpos] = ((in_[0 + inpos] >> 12) & 1) + out[12 + outpos - 1]
        out[13 + outpos] = ((in_[0 + inpos] >> 13) & 1) + out[13 + outpos - 1]
        out[14 + outpos] = ((in_[0 + inpos] >> 14) & 1) + out[14 + outpos - 1]
        out[15 + outpos] = ((in_[0 + inpos] >> 15) & 1) + out[15 + outpos - 1]
        out[16 + outpos] = ((in_[0 + inpos] >> 16) & 1) + out[16 + outpos - 1]
        out[17 + outpos] = ((in_[0 + inpos] >> 17) & 1) + out[17 + outpos - 1]
        out[18 + outpos] = ((in_[0 + inpos] >> 18) & 1) + out[18 + outpos - 1]
        out[19 + outpos] = ((in_[0 + inpos] >> 19) & 1) + out[19 + outpos - 1]
        out[20 + outpos] = ((in_[0 + inpos] >> 20) & 1) + out[20 + outpos - 1]
        out[21 + outpos] = ((in_[0 + inpos] >> 21) & 1) + out[21 + outpos - 1]
        out[22 + outpos] = ((in_[0 + inpos] >> 22) & 1) + out[22 + outpos - 1]
        out[23 + outpos] = ((in_[0 + inpos] >> 23) & 1) + out[23 + outpos - 1]
        out[24 + outpos] = ((in_[0 + inpos] >> 24) & 1) + out[24 + outpos - 1]
        out[25 + outpos] = ((in_[0 + inpos] >> 25) & 1) + out[25 + outpos - 1]
        out[26 + outpos] = ((in_[0 + inpos] >> 26) & 1) + out[26 + outpos - 1]
        out[27 + outpos] = ((in_[0 + inpos] >> 27) & 1) + out[27 + outpos - 1]
        out[28 + outpos] = ((in_[0 + inpos] >> 28) & 1) + out[28 + outpos - 1]
        out[29 + outpos] = ((in_[0 + inpos] >> 29) & 1) + out[29 + outpos - 1]
        out[30 + outpos] = ((in_[0 + inpos] >> 30) & 1) + out[30 + outpos - 1]
        out[31 + outpos] = (in_[0 + inpos] >> 31) + out[31 + outpos - 1]

    out[outpos : outpos + 32] = [initoffset] * 32

    @staticmethod
    def integratedunpack(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
        bit: int,
    ) -> None:
        if bit == 0:
            IntegratedBitPacking._integratedunpack0(initoffset, in_, inpos, out, outpos)
        elif bit == 1:
            IntegratedBitPacking._integratedunpack1(initoffset, in_, inpos, out, outpos)
        elif bit == 2:
            IntegratedBitPacking._integratedunpack2(initoffset, in_, inpos, out, outpos)
        elif bit == 3:
            IntegratedBitPacking._integratedunpack3(initoffset, in_, inpos, out, outpos)
        elif bit == 4:
            IntegratedBitPacking._integratedunpack4(initoffset, in_, inpos, out, outpos)
        elif bit == 5:
            IntegratedBitPacking._integratedunpack5(initoffset, in_, inpos, out, outpos)
        elif bit == 6:
            IntegratedBitPacking._integratedunpack6(initoffset, in_, inpos, out, outpos)
        elif bit == 7:
            IntegratedBitPacking._integratedunpack7(initoffset, in_, inpos, out, outpos)
        elif bit == 8:
            IntegratedBitPacking._integratedunpack8(initoffset, in_, inpos, out, outpos)
        elif bit == 9:
            IntegratedBitPacking._integratedunpack9(initoffset, in_, inpos, out, outpos)
        elif bit == 10:
            IntegratedBitPacking._integratedunpack10(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 11:
            IntegratedBitPacking._integratedunpack11(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 12:
            IntegratedBitPacking._integratedunpack12(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 13:
            IntegratedBitPacking._integratedunpack13(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 14:
            IntegratedBitPacking._integratedunpack14(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 15:
            IntegratedBitPacking._integratedunpack15(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 16:
            IntegratedBitPacking._integratedunpack16(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 17:
            IntegratedBitPacking._integratedunpack17(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 18:
            IntegratedBitPacking._integratedunpack18(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 19:
            IntegratedBitPacking._integratedunpack19(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 20:
            IntegratedBitPacking._integratedunpack20(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 21:
            IntegratedBitPacking._integratedunpack21(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 22:
            IntegratedBitPacking._integratedunpack22(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 23:
            IntegratedBitPacking._integratedunpack23(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 24:
            IntegratedBitPacking._integratedunpack24(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 25:
            IntegratedBitPacking._integratedunpack25(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 26:
            IntegratedBitPacking._integratedunpack26(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 27:
            IntegratedBitPacking._integratedunpack27(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 28:
            IntegratedBitPacking._integratedunpack28(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 29:
            IntegratedBitPacking._integratedunpack29(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 30:
            IntegratedBitPacking._integratedunpack30(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 31:
            IntegratedBitPacking._integratedunpack31(
                initoffset, in_, inpos, out, outpos
            )
        elif bit == 32:
            IntegratedBitPacking._integratedunpack32(
                initoffset, in_, inpos, out, outpos
            )
        else:
            raise ValueError("Unsupported bit width.")

    @staticmethod
    def _integratedpack9(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 9)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 18)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 27)
        )
        out[1 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (9 - 4))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 4)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 13)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 22)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 31)
        )
        out[2 + outpos] = (
            ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (9 - 8))
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 8)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 17)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 26)
        )
        out[3 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (9 - 3))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 3)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 12)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 21)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 30)
        )
        out[4 + outpos] = (
            ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (9 - 7))
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 7)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 25)
        )
        out[5 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (9 - 2))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 2)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 11)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 20)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 29)
        )
        out[6 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (9 - 6))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 6)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 15)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 24)
        )
        out[7 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (9 - 1))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 1)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 10)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 19)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 28)
        )
        out[8 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (9 - 5))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 5)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 14)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 23)
        )

    @staticmethod
    def _integratedpack8(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def _integratedpack7(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 7)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 14)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 21)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 28)
        )
        out[1 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (7 - 3))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 3)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 10)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 17)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 31)
        )
        out[2 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (7 - 6))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 6)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 13)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 20)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 27)
        )
        out[3 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (7 - 2))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 2)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 9)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 23)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 30)
        )
        out[4 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (7 - 5))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 5)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 12)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 19)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 26)
        )
        out[5 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (7 - 1))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 1)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 15)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 22)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 29)
        )
        out[6 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (7 - 4))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 4)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 11)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 18)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 25)
        )

    @staticmethod
    def _integratedpack6(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 6)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 12)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 18)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 24)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 30)
        )

        out[1 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (6 - 4))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 4)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 10)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 16)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 22)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 28)
        )

        out[2 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (6 - 2))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 2)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 8)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 14)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 20)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 26)
        )

        out[3 + outpos] = (
            (in_[16 + inpos] - in_[16 + inpos - 1])
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 6)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 12)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 18)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 24)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 30)
        )

        out[4 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (6 - 4))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 4)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 10)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 16)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 22)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 28)
        )

        out[5 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (6 - 2))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 2)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 8)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 14)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 20)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 26)
        )

    @staticmethod
    def _integratedpack5(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 5)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 10)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 15)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 20)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 25)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 30)
        )

        out[1 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (5 - 3))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 3)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 8)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 13)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 18)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 23)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 28)
        )

        out[2 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (5 - 1))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 1)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 6)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 11)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 21)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 26)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 31)
        )

        out[3 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (5 - 4))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 4)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 9)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 14)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 19)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 24)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 29)
        )

        out[4 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (5 - 2))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 2)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 7)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 12)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 17)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 22)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 27)
        )

    @staticmethod
    def _integratedpack4(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 4)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 8)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 12)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 16)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 20)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 24)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 28)
        )

        out[1 + outpos] = (
            (in_[8 + inpos] - in_[8 + inpos - 1])
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 4)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 8)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 12)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 16)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 20)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 24)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 28)
        )

        out[2 + outpos] = (
            (in_[16 + inpos] - in_[16 + inpos - 1])
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 4)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 8)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 12)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 16)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 20)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 24)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 28)
        )

        out[3 + outpos] = (
            (in_[24 + inpos] - in_[24 + inpos - 1])
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 4)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 8)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 12)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 16)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 20)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 24)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 28)
        )

    @staticmethod
    def _integratedpack32(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[outpos : outpos + 32] = in_[inpos : inpos + 32]

    @staticmethod
    def _integratedpack31(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 31
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (31 - 30)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 30
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (31 - 29)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 29
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (31 - 28)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 28
        )
        out[4 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (31 - 27)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 27
        )
        out[5 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (31 - 26)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 26
        )
        out[6 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (31 - 25)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 25
        )
        out[7 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (31 - 24)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 24
        )
        out[8 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (31 - 23)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 23
        )
        out[9 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (31 - 22)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 22
        )
        out[10 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (31 - 21)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 21
        )
        out[11 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (31 - 20)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 20
        )
        out[12 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (31 - 19)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 19
        )
        out[13 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (31 - 18)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 18
        )
        out[14 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (31 - 17)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 17
        )
        out[15 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (31 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[16 + outpos] = ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (31 - 15)) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 15
        )
        out[17 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (31 - 14)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 14
        )
        out[18 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (31 - 13)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 13
        )
        out[19 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (31 - 12)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 12
        )
        out[20 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (31 - 11)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 11
        )
        out[21 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (31 - 10)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 10
        )
        out[22 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (31 - 9)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 9
        )
        out[23 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (31 - 8)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 8
        )
        out[24 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (31 - 7)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 7
        )
        out[25 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (31 - 6)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 6
        )
        out[26 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (31 - 5)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 5
        )
        out[27 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (31 - 4)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 4
        )
        out[28 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (31 - 3)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 3
        )
        out[29 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (31 - 2)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 2
        )
        out[30 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (31 - 1)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 1
        )

    @staticmethod
    def _integratedpack30(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 30
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (30 - 28)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 28
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (30 - 26)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 26
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (30 - 24)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 24
        )
        out[4 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (30 - 22)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 22
        )
        out[5 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (30 - 20)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 20
        )
        out[6 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (30 - 18)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 18
        )
        out[7 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (30 - 16)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 16
        )
        out[8 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (30 - 14)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 14
        )
        out[9 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (30 - 12)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 12
        )
        out[10 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (30 - 10)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 10
        )
        out[11 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (30 - 8)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 8
        )
        out[12 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (30 - 6)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 6
        )
        out[13 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (30 - 4)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 4
        )
        out[14 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (30 - 2)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 2
        )
        out[15 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 30
        )
        out[16 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (30 - 28)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 28
        )
        out[17 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (30 - 26)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 26
        )
        out[18 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (30 - 24)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 24
        )
        out[19 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (30 - 22)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 22
        )
        out[20 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (30 - 20)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 20
        )
        out[21 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (30 - 18)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 18
        )
        out[22 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (30 - 16)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 16
        )
        out[23 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (30 - 14)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 14
        )
        out[24 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (30 - 12)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 12
        )
        out[25 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (30 - 10)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 10
        )
        out[26 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (30 - 8)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 8
        )
        out[27 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (30 - 6)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 6
        )
        out[28 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (30 - 4)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 4
        )
        out[29 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (30 - 2)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 2
        )

    @staticmethod
    def _integratedpack3(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 3)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 6)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 9)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 12)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 15)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 18)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 21)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 27)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 30)
        )

        out[1 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (3 - 1))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 1)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 4)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 7)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 10)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 13)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 19)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 22)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 25)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 28)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 31)
        )

        out[2 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (3 - 2))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 2)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 5)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 11)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 14)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 17)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 20)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 23)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 26)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 29)
        )

    @staticmethod
    def _integratedpack29(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 29
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (29 - 26)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 26
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (29 - 23)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 23
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (29 - 20)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 20
        )
        out[4 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (29 - 17)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 17
        )
        out[5 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (29 - 14)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 14
        )
        out[6 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (29 - 11)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 11
        )
        out[7 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (29 - 8)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 8
        )
        out[8 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (29 - 5)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 5
        )
        out[9 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (29 - 2))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 2)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 31)
        )
        out[10 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (29 - 28)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 28
        )
        out[11 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (29 - 25)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 25
        )
        out[12 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (29 - 22)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 22
        )
        out[13 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (29 - 19)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 19
        )
        out[14 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (29 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[15 + outpos] = ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (29 - 13)) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 13
        )
        out[16 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (29 - 10)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 10
        )
        out[17 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (29 - 7)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 7
        )
        out[18 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (29 - 4)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 4
        )
        out[19 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (29 - 1))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 1)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 30)
        )
        out[20 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (29 - 27)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 27
        )
        out[21 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (29 - 24)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 24
        )
        out[22 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (29 - 21)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 21
        )
        out[23 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (29 - 18)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 18
        )
        out[24 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (29 - 15)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 15
        )
        out[25 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (29 - 12)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 12
        )
        out[26 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (29 - 9)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 9
        )
        out[27 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (29 - 6)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 6
        )
        out[28 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (29 - 3)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 3
        )

    @staticmethod
    def _integratedpack28(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 28
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (28 - 24)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 24
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (28 - 20)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 20
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (28 - 16)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 16
        )
        out[4 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (28 - 12)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 12
        )
        out[5 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (28 - 8)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 8
        )
        out[6 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (28 - 4)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 4
        )
        out[7 + outpos] = (in_[8 + inpos] - in_[8 + inpos - 1]) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 28
        )
        out[8 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (28 - 24)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 24
        )
        out[9 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (28 - 20)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 20
        )
        out[10 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (28 - 16)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 16
        )
        out[11 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (28 - 12)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 12
        )
        out[12 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (28 - 8)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 8
        )
        out[13 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (28 - 4)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 4
        )
        out[14 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 28
        )
        out[15 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (28 - 24)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 24
        )
        out[16 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (28 - 20)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 20
        )
        out[17 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (28 - 16)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 16
        )
        out[18 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (28 - 12)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 12
        )
        out[19 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (28 - 8)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 8
        )
        out[20 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (28 - 4)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 4
        )
        out[21 + outpos] = (in_[24 + inpos] - in_[24 + inpos - 1]) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 28
        )
        out[22 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (28 - 24)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 24
        )
        out[23 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (28 - 20)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 20
        )
        out[24 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (28 - 16)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 16
        )
        out[25 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (28 - 12)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 12
        )
        out[26 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (28 - 8)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 8
        )
        out[27 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (28 - 4)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 4
        )

    @staticmethod
    def _integratedpack27(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 27
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (27 - 22)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 22
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (27 - 17)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 17
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (27 - 12)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 12
        )
        out[4 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (27 - 7)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 7
        )
        out[5 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (27 - 2))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 2)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 29)
        )
        out[6 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (27 - 24)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 24
        )
        out[7 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (27 - 19)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 19
        )
        out[8 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (27 - 14)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 14
        )
        out[9 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (27 - 9)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 9
        )
        out[10 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (27 - 4))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 4)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 31)
        )
        out[11 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (27 - 26)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 26
        )
        out[12 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (27 - 21)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 21
        )
        out[13 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (27 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[14 + outpos] = ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (27 - 11)) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 11
        )
        out[15 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (27 - 6)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 6
        )
        out[16 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (27 - 1))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 1)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 28)
        )
        out[17 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (27 - 23)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 23
        )
        out[18 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (27 - 18)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 18
        )
        out[19 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (27 - 13)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 13
        )
        out[20 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (27 - 8)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 8
        )
        out[21 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (27 - 3))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 3)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 30)
        )
        out[22 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (27 - 25)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 25
        )
        out[23 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (27 - 20)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 20
        )
        out[24 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (27 - 15)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 15
        )
        out[25 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (27 - 10)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 10
        )
        out[26 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (27 - 5)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 5
        )

    @staticmethod
    def _integratedpack26(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 26
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (26 - 20)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 20
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (26 - 14)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 14
        )
        out[3 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (26 - 8)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 8
        )
        out[4 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (26 - 2))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 2)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 28)
        )
        out[5 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (26 - 22)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 22
        )
        out[6 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (26 - 16)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 16
        )
        out[7 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (26 - 10)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 10
        )
        out[8 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (26 - 4))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 4)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 30)
        )
        out[9 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (26 - 24)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 24
        )
        out[10 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (26 - 18)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 18
        )
        out[11 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (26 - 12)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 12
        )
        out[12 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (26 - 6)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 6
        )
        out[13 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 26
        )
        out[14 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (26 - 20)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 20
        )
        out[15 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (26 - 14)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 14
        )
        out[16 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (26 - 8)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 8
        )
        out[17 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (26 - 2))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 2)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 28)
        )
        out[18 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (26 - 22)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 22
        )
        out[19 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (26 - 16)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 16
        )
        out[20 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (26 - 10)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 10
        )
        out[21 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (26 - 4))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 4)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 30)
        )
        out[22 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (26 - 24)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 24
        )
        out[23 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (26 - 18)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 18
        )
        out[24 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (26 - 12)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 12
        )
        out[25 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (26 - 6)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 6
        )

    @staticmethod
    def _integratedpack25(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 25
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (25 - 18)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 18
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (25 - 11)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 11
        )
        out[3 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (25 - 4))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 4)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 29)
        )
        out[4 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (25 - 22)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 22
        )
        out[5 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (25 - 15)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 15
        )
        out[6 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (25 - 8)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 8
        )
        out[7 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (25 - 1))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 1)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 26)
        )
        out[8 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (25 - 19)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 19
        )
        out[9 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (25 - 12)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 12
        )
        out[10 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (25 - 5))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 5)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 30)
        )
        out[11 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (25 - 23)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 23
        )
        out[12 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (25 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[13 + outpos] = ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (25 - 9)) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 9
        )
        out[14 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (25 - 2))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 2)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 27)
        )
        out[15 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (25 - 20)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 20
        )
        out[16 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (25 - 13)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 13
        )
        out[17 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (25 - 6))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 6)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 31)
        )
        out[18 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (25 - 24)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 24
        )
        out[19 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (25 - 17)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 17
        )
        out[20 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (25 - 10)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 10
        )
        out[21 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (25 - 3))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 3)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 28)
        )
        out[22 + outpos] = ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (25 - 21)) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 21
        )
        out[23 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (25 - 14)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 14
        )
        out[24 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (25 - 7)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 7
        )

    @staticmethod
    def _integratedpack24(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 24
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (24 - 16)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 16
        )
        out[2 + outpos] = ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (24 - 8)) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 8
        )
        out[3 + outpos] = (in_[4 + inpos] - in_[4 + inpos - 1]) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 24
        )
        out[4 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (24 - 16)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 16
        )
        out[5 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (24 - 8)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 8
        )
        out[6 + outpos] = (in_[8 + inpos] - in_[8 + inpos - 1]) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 24
        )
        out[7 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (24 - 16)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 16
        )
        out[8 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (24 - 8)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 8
        )
        out[9 + outpos] = (in_[12 + inpos] - in_[12 + inpos - 1]) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 24
        )
        out[10 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (24 - 16)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 16
        )
        out[11 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (24 - 8)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 8
        )
        out[12 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 24
        )
        out[13 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (24 - 16)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 16
        )
        out[14 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (24 - 8)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 8
        )
        out[15 + outpos] = (in_[20 + inpos] - in_[20 + inpos - 1]) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 24
        )
        out[16 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (24 - 16)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 16
        )
        out[17 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (24 - 8)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 8
        )
        out[18 + outpos] = (in_[24 + inpos] - in_[24 + inpos - 1]) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 24
        )
        out[19 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (24 - 16)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 16
        )
        out[20 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (24 - 8)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 8
        )
        out[21 + outpos] = (in_[28 + inpos] - in_[28 + inpos - 1]) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 24
        )
        out[22 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (24 - 16)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 16
        )
        out[23 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (24 - 8)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 8
        )

    @staticmethod
    def _integratedpack23(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 23
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (23 - 14)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 14
        )
        out[2 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (23 - 5))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 5)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 28)
        )
        out[3 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (23 - 19)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 19
        )
        out[4 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (23 - 10)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 10
        )
        out[5 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (23 - 1))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 1)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
        )
        out[6 + outpos] = ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (23 - 15)) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 15
        )
        out[7 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (23 - 6))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 6)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 29)
        )
        out[8 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (23 - 20)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 20
        )
        out[9 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (23 - 11)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 11
        )
        out[10 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (23 - 2))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 2)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 25)
        )
        out[11 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (23 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[12 + outpos] = (
            ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (23 - 7))
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 7)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 30)
        )
        out[13 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (23 - 21)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 21
        )
        out[14 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (23 - 12)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 12
        )
        out[15 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (23 - 3))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 3)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 26)
        )
        out[16 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (23 - 17)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 17
        )
        out[17 + outpos] = (
            ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (23 - 8))
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 31)
        )
        out[18 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (23 - 22)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 22
        )
        out[19 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (23 - 13)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 13
        )
        out[20 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (23 - 4))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 4)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 27)
        )
        out[21 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (23 - 18)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 18
        )
        out[22 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (23 - 9)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 9
        )

    @staticmethod
    def _integratedpack22(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 22
        )
        out[1 + outpos] = ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (22 - 12)) | (
            (in_[2 + inpos] - in_[2 + inpos - 1]) << 12
        )
        out[2 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (22 - 2))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 2)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 24)
        )
        out[3 + outpos] = ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (22 - 14)) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 14
        )
        out[4 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (22 - 4))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 4)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 26)
        )
        out[5 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (22 - 16)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 16
        )
        out[6 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (22 - 6))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 6)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 28)
        )
        out[7 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (22 - 18)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 18
        )
        out[8 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (22 - 8))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 8)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 30)
        )
        out[9 + outpos] = ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (22 - 20)) | (
            (in_[14 + inpos] - in_[14 + inpos - 1]) << 20
        )
        out[10 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (22 - 10)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 10
        )
        out[11 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 22
        )
        out[12 + outpos] = ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (22 - 12)) | (
            (in_[18 + inpos] - in_[18 + inpos - 1]) << 12
        )
        out[13 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (22 - 2))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 2)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 24)
        )
        out[14 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (22 - 14)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 14
        )
        out[15 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (22 - 4))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 4)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 26)
        )
        out[16 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (22 - 16)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 16
        )
        out[17 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (22 - 6))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 6)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 28)
        )
        out[18 + outpos] = ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (22 - 18)) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 18
        )
        out[19 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (22 - 8))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 8)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 30)
        )
        out[20 + outpos] = ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (22 - 20)) | (
            (in_[30 + inpos] - in_[30 + inpos - 1]) << 20
        )
        out[21 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (22 - 10)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 10
        )

    @staticmethod
    def _integratedpack21(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 21
        )
        out[1 + outpos] = (
            ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (21 - 10))
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 10)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 31)
        )
        out[2 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (21 - 20)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 20
        )
        out[3 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (21 - 9))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 9)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 30)
        )
        out[4 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (21 - 19)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 19
        )
        out[5 + outpos] = (
            ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (21 - 8))
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 8)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 29)
        )
        out[6 + outpos] = ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (21 - 18)) | (
            (in_[10 + inpos] - in_[10 + inpos - 1]) << 18
        )
        out[7 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (21 - 7))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 7)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 28)
        )
        out[8 + outpos] = ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (21 - 17)) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 17
        )
        out[9 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (21 - 6))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 6)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 27)
        )
        out[10 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (21 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[11 + outpos] = (
            ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (21 - 5))
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 5)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 26)
        )
        out[12 + outpos] = ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (21 - 15)) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 15
        )
        out[13 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (21 - 4))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 4)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 25)
        )
        out[14 + outpos] = ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (21 - 14)) | (
            (in_[22 + inpos] - in_[22 + inpos - 1]) << 14
        )
        out[15 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (21 - 3))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 3)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 24)
        )
        out[16 + outpos] = ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (21 - 13)) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 13
        )
        out[17 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (21 - 2))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 2)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 23)
        )
        out[18 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (21 - 12)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 12
        )
        out[19 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (21 - 1))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 1)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 22)
        )
        out[20 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (21 - 11)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 11
        )

    @staticmethod
    def _integratedpack20(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 20
        )
        out[1 + outpos] = (
            ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (20 - 8))
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 8)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 28)
        )
        out[2 + outpos] = ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (20 - 16)) | (
            (in_[4 + inpos] - in_[4 + inpos - 1]) << 16
        )
        out[3 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (20 - 4))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 4)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 24)
        )
        out[4 + outpos] = ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (20 - 12)) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 12
        )
        out[5 + outpos] = (in_[8 + inpos] - in_[8 + inpos - 1]) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 20
        )
        out[6 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (20 - 8))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 8)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 28)
        )
        out[7 + outpos] = ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (20 - 16)) | (
            (in_[12 + inpos] - in_[12 + inpos - 1]) << 16
        )
        out[8 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (20 - 4))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 4)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 24)
        )
        out[9 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (20 - 12)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 12
        )
        out[10 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 20
        )
        out[11 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (20 - 8))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 8)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 28)
        )
        out[12 + outpos] = ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (20 - 16)) | (
            (in_[20 + inpos] - in_[20 + inpos - 1]) << 16
        )
        out[13 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (20 - 4))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 4)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 24)
        )
        out[14 + outpos] = ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (20 - 12)) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 12
        )
        out[15 + outpos] = (in_[24 + inpos] - in_[24 + inpos - 1]) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 20
        )
        out[16 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (20 - 8))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 8)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 28)
        )
        out[17 + outpos] = ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (20 - 16)) | (
            (in_[28 + inpos] - in_[28 + inpos - 1]) << 16
        )
        out[18 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (20 - 4))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 4)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 24)
        )
        out[19 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (20 - 12)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 12
        )

    @staticmethod
    def _integratedpack2(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def _integratedpack19(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 19
        )
        out[1 + outpos] = (
            ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (19 - 6))
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 6)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 25)
        )
        out[2 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (19 - 12))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 12)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 31)
        )
        out[3 + outpos] = ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (19 - 18)) | (
            (in_[6 + inpos] - in_[6 + inpos - 1]) << 18
        )
        out[4 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (19 - 5))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 5)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
        )
        out[5 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (19 - 11))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 11)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 30)
        )
        out[6 + outpos] = ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (19 - 17)) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 17
        )
        out[7 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (19 - 4))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 4)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 23)
        )
        out[8 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (19 - 10))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 10)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 29)
        )
        out[9 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (19 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[10 + outpos] = (
            ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (19 - 3))
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 3)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 22)
        )
        out[11 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (19 - 9))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 9)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 28)
        )
        out[12 + outpos] = ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (19 - 15)) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 15
        )
        out[13 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (19 - 2))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 2)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 21)
        )
        out[14 + outpos] = (
            ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (19 - 8))
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 27)
        )
        out[15 + outpos] = ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (19 - 14)) | (
            (in_[26 + inpos] - in_[26 + inpos - 1]) << 14
        )
        out[16 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (19 - 1))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 1)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 20)
        )
        out[17 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (19 - 7))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 7)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 26)
        )
        out[18 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (19 - 13)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 13
        )

    @staticmethod
    def _integratedpack18(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 18
        )
        out[1 + outpos] = (
            ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (18 - 4))
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 4)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 22)
        )
        out[2 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (18 - 8))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 8)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 26)
        )
        out[3 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (18 - 12))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 12)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 30)
        )
        out[4 + outpos] = ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (18 - 16)) | (
            (in_[8 + inpos] - in_[8 + inpos - 1]) << 16
        )
        out[5 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (18 - 2))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 2)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 20)
        )
        out[6 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (18 - 6))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 6)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 24)
        )
        out[7 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (18 - 10))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 10)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 28)
        )
        out[8 + outpos] = ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (18 - 14)) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 14
        )
        out[9 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 18
        )
        out[10 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (18 - 4))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 4)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 22)
        )
        out[11 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (18 - 8))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 8)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 26)
        )
        out[12 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (18 - 12))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 12)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 30)
        )
        out[13 + outpos] = ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (18 - 16)) | (
            (in_[24 + inpos] - in_[24 + inpos - 1]) << 16
        )
        out[14 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (18 - 2))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 2)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 20)
        )
        out[15 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (18 - 6))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 6)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 24)
        )
        out[16 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (18 - 10))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 10)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 28)
        )
        out[17 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (18 - 14)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 14
        )

    @staticmethod
    def _integratedpack17(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 17
        )
        out[1 + outpos] = (
            ((in_[1 + inpos] - in_[1 + inpos - 1]) >> (17 - 2))
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 2)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 19)
        )
        out[2 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (17 - 4))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 4)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 21)
        )
        out[3 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (17 - 6))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 6)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 23)
        )
        out[4 + outpos] = (
            ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (17 - 8))
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 8)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 25)
        )
        out[5 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (17 - 10))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 10)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 27)
        )
        out[6 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (17 - 12))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 12)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 29)
        )
        out[7 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (17 - 14))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 14)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 31)
        )
        out[8 + outpos] = ((in_[15 + inpos] - in_[15 + inpos - 1]) >> (17 - 16)) | (
            (in_[16 + inpos] - in_[16 + inpos - 1]) << 16
        )
        out[9 + outpos] = (
            ((in_[16 + inpos] - in_[16 + inpos - 1]) >> (17 - 1))
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 1)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 18)
        )
        out[10 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (17 - 3))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 3)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 20)
        )
        out[11 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (17 - 5))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 5)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 22)
        )
        out[12 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (17 - 7))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 7)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 24)
        )
        out[13 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (17 - 9))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 9)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 26)
        )
        out[14 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (17 - 11))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 11)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 28)
        )
        out[15 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (17 - 13))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 13)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 30)
        )
        out[16 + outpos] = ((in_[30 + inpos] - in_[30 + inpos - 1]) >> (17 - 15)) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 15
        )

    @staticmethod
    def _integratedpack16(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (in_[0 + inpos] - initoffset) | (
            (in_[1 + inpos] - in_[1 + inpos - 1]) << 16
        )
        out[1 + outpos] = (in_[2 + inpos] - in_[2 + inpos - 1]) | (
            (in_[3 + inpos] - in_[3 + inpos - 1]) << 16
        )
        out[2 + outpos] = (in_[4 + inpos] - in_[4 + inpos - 1]) | (
            (in_[5 + inpos] - in_[5 + inpos - 1]) << 16
        )
        out[3 + outpos] = (in_[6 + inpos] - in_[6 + inpos - 1]) | (
            (in_[7 + inpos] - in_[7 + inpos - 1]) << 16
        )
        out[4 + outpos] = (in_[8 + inpos] - in_[8 + inpos - 1]) | (
            (in_[9 + inpos] - in_[9 + inpos - 1]) << 16
        )
        out[5 + outpos] = (in_[10 + inpos] - in_[10 + inpos - 1]) | (
            (in_[11 + inpos] - in_[11 + inpos - 1]) << 16
        )
        out[6 + outpos] = (in_[12 + inpos] - in_[12 + inpos - 1]) | (
            (in_[13 + inpos] - in_[13 + inpos - 1]) << 16
        )
        out[7 + outpos] = (in_[14 + inpos] - in_[14 + inpos - 1]) | (
            (in_[15 + inpos] - in_[15 + inpos - 1]) << 16
        )
        out[8 + outpos] = (in_[16 + inpos] - in_[16 + inpos - 1]) | (
            (in_[17 + inpos] - in_[17 + inpos - 1]) << 16
        )
        out[9 + outpos] = (in_[18 + inpos] - in_[18 + inpos - 1]) | (
            (in_[19 + inpos] - in_[19 + inpos - 1]) << 16
        )
        out[10 + outpos] = (in_[20 + inpos] - in_[20 + inpos - 1]) | (
            (in_[21 + inpos] - in_[21 + inpos - 1]) << 16
        )
        out[11 + outpos] = (in_[22 + inpos] - in_[22 + inpos - 1]) | (
            (in_[23 + inpos] - in_[23 + inpos - 1]) << 16
        )
        out[12 + outpos] = (in_[24 + inpos] - in_[24 + inpos - 1]) | (
            (in_[25 + inpos] - in_[25 + inpos - 1]) << 16
        )
        out[13 + outpos] = (in_[26 + inpos] - in_[26 + inpos - 1]) | (
            (in_[27 + inpos] - in_[27 + inpos - 1]) << 16
        )
        out[14 + outpos] = (in_[28 + inpos] - in_[28 + inpos - 1]) | (
            (in_[29 + inpos] - in_[29 + inpos - 1]) << 16
        )
        out[15 + outpos] = (in_[30 + inpos] - in_[30 + inpos - 1]) | (
            (in_[31 + inpos] - in_[31 + inpos - 1]) << 16
        )

    @staticmethod
    def _integratedpack15(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 15)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 30)
        )
        out[1 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (15 - 13))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 13)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 28)
        )
        out[2 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (15 - 11))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 11)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 26)
        )
        out[3 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (15 - 9))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 9)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
        )
        out[4 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (15 - 7))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 7)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 22)
        )
        out[5 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (15 - 5))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 5)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 20)
        )
        out[6 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (15 - 3))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 3)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 18)
        )
        out[7 + outpos] = (
            ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (15 - 1))
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 1)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 31)
        )
        out[8 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (15 - 14))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 14)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 29)
        )
        out[9 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (15 - 12))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 12)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 27)
        )
        out[10 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (15 - 10))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 10)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 25)
        )
        out[11 + outpos] = (
            ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (15 - 8))
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 23)
        )
        out[12 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (15 - 6))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 6)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 21)
        )
        out[13 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (15 - 4))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 4)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 19)
        )
        out[14 + outpos] = (
            ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (15 - 2))
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 2)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 17)
        )

    @staticmethod
    def _integratedpack14(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 14)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 28)
        )
        out[1 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (14 - 10))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 10)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 24)
        )
        out[2 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (14 - 6))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 6)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 20)
        )
        out[3 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (14 - 2))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 2)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 16)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 30)
        )
        out[4 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (14 - 12))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 12)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 26)
        )
        out[5 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (14 - 8))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 8)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 22)
        )
        out[6 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (14 - 4))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 4)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 18)
        )
        out[7 + outpos] = (
            (in_[16 + inpos] - in_[16 + inpos - 1])
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 14)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 28)
        )
        out[8 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (14 - 10))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 10)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 24)
        )
        out[9 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (14 - 6))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 6)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 20)
        )
        out[10 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (14 - 2))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 2)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 16)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 30)
        )
        out[11 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (14 - 12))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 12)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 26)
        )
        out[12 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (14 - 8))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 8)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 22)
        )
        out[13 + outpos] = (
            ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (14 - 4))
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 4)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 18)
        )

    @staticmethod
    def _integratedpack13(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 13)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 26)
        )
        out[1 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (13 - 7))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 7)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 20)
        )
        out[2 + outpos] = (
            ((in_[4 + inpos] - in_[4 + inpos - 1]) >> (13 - 1))
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 1)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 14)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 27)
        )
        out[3 + outpos] = (
            ((in_[7 + inpos] - in_[7 + inpos - 1]) >> (13 - 8))
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 8)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 21)
        )
        out[4 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (13 - 2))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 2)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 15)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 28)
        )
        out[5 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (13 - 9))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 9)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 22)
        )
        out[6 + outpos] = (
            ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (13 - 3))
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 3)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 29)
        )
        out[7 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (13 - 10))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 10)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 23)
        )
        out[8 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (13 - 4))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 4)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 17)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 30)
        )
        out[9 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (13 - 11))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 11)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 24)
        )
        out[10 + outpos] = (
            ((in_[24 + inpos] - in_[24 + inpos - 1]) >> (13 - 5))
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 5)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 18)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 31)
        )
        out[11 + outpos] = (
            ((in_[27 + inpos] - in_[27 + inpos - 1]) >> (13 - 12))
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 12)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 25)
        )
        out[12 + outpos] = (
            ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (13 - 6))
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 6)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 19)
        )

    @staticmethod
    def _integratedpack12(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 12)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 24)
        )
        out[1 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (12 - 4))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 4)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 16)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 28)
        )
        out[2 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (12 - 8))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 8)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 20)
        )
        out[3 + outpos] = (
            (in_[8 + inpos] - in_[8 + inpos - 1])
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 12)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 24)
        )
        out[4 + outpos] = (
            ((in_[10 + inpos] - in_[10 + inpos - 1]) >> (12 - 4))
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 4)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 16)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 28)
        )
        out[5 + outpos] = (
            ((in_[13 + inpos] - in_[13 + inpos - 1]) >> (12 - 8))
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 8)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 20)
        )
        out[6 + outpos] = (
            (in_[16 + inpos] - in_[16 + inpos - 1])
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 12)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 24)
        )
        out[7 + outpos] = (
            ((in_[18 + inpos] - in_[18 + inpos - 1]) >> (12 - 4))
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 4)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 16)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 28)
        )
        out[8 + outpos] = (
            ((in_[21 + inpos] - in_[21 + inpos - 1]) >> (12 - 8))
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 8)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 20)
        )
        out[9 + outpos] = (
            (in_[24 + inpos] - in_[24 + inpos - 1])
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 12)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 24)
        )
        out[10 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (12 - 4))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 4)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 16)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 28)
        )
        out[11 + outpos] = (
            ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (12 - 8))
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 8)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 20)
        )

    @staticmethod
    def _integratedpack11(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 11)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 22)
        )
        out[1 + outpos] = (
            ((in_[2 + inpos] - in_[2 + inpos - 1]) >> (11 - 1))
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 1)
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 12)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 23)
        )
        out[2 + outpos] = (
            ((in_[5 + inpos] - in_[5 + inpos - 1]) >> (11 - 2))
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 2)
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 13)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 24)
        )
        out[3 + outpos] = (
            ((in_[8 + inpos] - in_[8 + inpos - 1]) >> (11 - 3))
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 3)
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 14)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 25)
        )
        out[4 + outpos] = (
            ((in_[11 + inpos] - in_[11 + inpos - 1]) >> (11 - 4))
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 4)
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 15)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 26)
        )
        out[5 + outpos] = (
            ((in_[14 + inpos] - in_[14 + inpos - 1]) >> (11 - 5))
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 5)
            | ((in_[16 + inpos] - in_[16 + inpos - 1]) << 16)
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 27)
        )
        out[6 + outpos] = (
            ((in_[17 + inpos] - in_[17 + inpos - 1]) >> (11 - 6))
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 6)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 17)
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 28)
        )
        out[7 + outpos] = (
            ((in_[20 + inpos] - in_[20 + inpos - 1]) >> (11 - 7))
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 7)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 18)
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 29)
        )
        out[8 + outpos] = (
            ((in_[23 + inpos] - in_[23 + inpos - 1]) >> (11 - 8))
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 8)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 19)
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 30)
        )
        out[9 + outpos] = (
            ((in_[26 + inpos] - in_[26 + inpos - 1]) >> (11 - 9))
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 9)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 20)
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 31)
        )
        out[10 + outpos] = (
            ((in_[29 + inpos] - in_[29 + inpos - 1]) >> (11 - 10))
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 10)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 21)
        )

    @staticmethod
    def _integratedpack10(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        out[0 + outpos] = (
            (in_[0 + inpos] - initoffset)
            | ((in_[1 + inpos] - in_[1 + inpos - 1]) << 10)
            | ((in_[2 + inpos] - in_[2 + inpos - 1]) << 20)
            | ((in_[3 + inpos] - in_[3 + inpos - 1]) << 30)
        )
        out[1 + outpos] = (
            ((in_[3 + inpos] - in_[3 + inpos - 1]) >> (10 - 8))
            | ((in_[4 + inpos] - in_[4 + inpos - 1]) << 8)
            | ((in_[5 + inpos] - in_[5 + inpos - 1]) << 18)
            | ((in_[6 + inpos] - in_[6 + inpos - 1]) << 28)
        )
        out[2 + outpos] = (
            ((in_[6 + inpos] - in_[6 + inpos - 1]) >> (10 - 6))
            | ((in_[7 + inpos] - in_[7 + inpos - 1]) << 6)
            | ((in_[8 + inpos] - in_[8 + inpos - 1]) << 16)
            | ((in_[9 + inpos] - in_[9 + inpos - 1]) << 26)
        )
        out[3 + outpos] = (
            ((in_[9 + inpos] - in_[9 + inpos - 1]) >> (10 - 4))
            | ((in_[10 + inpos] - in_[10 + inpos - 1]) << 4)
            | ((in_[11 + inpos] - in_[11 + inpos - 1]) << 14)
            | ((in_[12 + inpos] - in_[12 + inpos - 1]) << 24)
        )
        out[4 + outpos] = (
            ((in_[12 + inpos] - in_[12 + inpos - 1]) >> (10 - 2))
            | ((in_[13 + inpos] - in_[13 + inpos - 1]) << 2)
            | ((in_[14 + inpos] - in_[14 + inpos - 1]) << 12)
            | ((in_[15 + inpos] - in_[15 + inpos - 1]) << 22)
        )
        out[5 + outpos] = (
            (in_[16 + inpos] - in_[16 + inpos - 1])
            | ((in_[17 + inpos] - in_[17 + inpos - 1]) << 10)
            | ((in_[18 + inpos] - in_[18 + inpos - 1]) << 20)
            | ((in_[19 + inpos] - in_[19 + inpos - 1]) << 30)
        )
        out[6 + outpos] = (
            ((in_[19 + inpos] - in_[19 + inpos - 1]) >> (10 - 8))
            | ((in_[20 + inpos] - in_[20 + inpos - 1]) << 8)
            | ((in_[21 + inpos] - in_[21 + inpos - 1]) << 18)
            | ((in_[22 + inpos] - in_[22 + inpos - 1]) << 28)
        )
        out[7 + outpos] = (
            ((in_[22 + inpos] - in_[22 + inpos - 1]) >> (10 - 6))
            | ((in_[23 + inpos] - in_[23 + inpos - 1]) << 6)
            | ((in_[24 + inpos] - in_[24 + inpos - 1]) << 16)
            | ((in_[25 + inpos] - in_[25 + inpos - 1]) << 26)
        )
        out[8 + outpos] = (
            ((in_[25 + inpos] - in_[25 + inpos - 1]) >> (10 - 4))
            | ((in_[26 + inpos] - in_[26 + inpos - 1]) << 4)
            | ((in_[27 + inpos] - in_[27 + inpos - 1]) << 14)
            | ((in_[28 + inpos] - in_[28 + inpos - 1]) << 24)
        )
        out[9 + outpos] = (
            ((in_[28 + inpos] - in_[28 + inpos - 1]) >> (10 - 2))
            | ((in_[29 + inpos] - in_[29 + inpos - 1]) << 2)
            | ((in_[30 + inpos] - in_[30 + inpos - 1]) << 12)
            | ((in_[31 + inpos] - in_[31 + inpos - 1]) << 22)
        )

    out[outpos] = (
        (in_[inpos] - initoffset)
        | ((in_[inpos + 1] - in_[inpos]) << 1)
        | ((in_[inpos + 2] - in_[inpos + 1]) << 2)
        | ((in_[inpos + 3] - in_[inpos + 2]) << 3)
        | ((in_[inpos + 4] - in_[inpos + 3]) << 4)
        | ((in_[inpos + 5] - in_[inpos + 4]) << 5)
        | ((in_[inpos + 6] - in_[inpos + 5]) << 6)
        | ((in_[inpos + 7] - in_[inpos + 6]) << 7)
        | ((in_[inpos + 8] - in_[inpos + 7]) << 8)
        | ((in_[inpos + 9] - in_[inpos + 8]) << 9)
        | ((in_[inpos + 10] - in_[inpos + 9]) << 10)
        | ((in_[inpos + 11] - in_[inpos + 10]) << 11)
        | ((in_[inpos + 12] - in_[inpos + 11]) << 12)
        | ((in_[inpos + 13] - in_[inpos + 12]) << 13)
        | ((in_[inpos + 14] - in_[inpos + 13]) << 14)
        | ((in_[inpos + 15] - in_[inpos + 14]) << 15)
        | ((in_[inpos + 16] - in_[inpos + 15]) << 16)
        | ((in_[inpos + 17] - in_[inpos + 16]) << 17)
        | ((in_[inpos + 18] - in_[inpos + 17]) << 18)
        | ((in_[inpos + 19] - in_[inpos + 18]) << 19)
        | ((in_[inpos + 20] - in_[inpos + 19]) << 20)
        | ((in_[inpos + 21] - in_[inpos + 20]) << 21)
        | ((in_[inpos + 22] - in_[inpos + 21]) << 22)
        | ((in_[inpos + 23] - in_[inpos + 22]) << 23)
        | ((in_[inpos + 24] - in_[inpos + 23]) << 24)
        | ((in_[inpos + 25] - in_[inpos + 24]) << 25)
        | ((in_[inpos + 26] - in_[inpos + 25]) << 26)
        | ((in_[inpos + 27] - in_[inpos + 26]) << 27)
        | ((in_[inpos + 28] - in_[inpos + 27]) << 28)
        | ((in_[inpos + 29] - in_[inpos + 28]) << 29)
        | ((in_[inpos + 30] - in_[inpos + 29]) << 30)
        | ((in_[inpos + 31] - in_[inpos + 30]) << 31)
    )

    @staticmethod
    def _integratedpack0(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
    ) -> None:
        # nothing
        pass

    @staticmethod
    def integratedpack(
        initoffset: int,
        in_: typing.List[int],
        inpos: int,
        out: typing.List[int],
        outpos: int,
        bit: int,
    ) -> None:
        if bit == 0:
            IntegratedBitPacking._integratedpack0(initoffset, in_, inpos, out, outpos)
        elif bit == 1:
            IntegratedBitPacking._integratedpack1(initoffset, in_, inpos, out, outpos)
        elif bit == 2:
            IntegratedBitPacking._integratedpack2(initoffset, in_, inpos, out, outpos)
        elif bit == 3:
            IntegratedBitPacking._integratedpack3(initoffset, in_, inpos, out, outpos)
        elif bit == 4:
            IntegratedBitPacking._integratedpack4(initoffset, in_, inpos, out, outpos)
        elif bit == 5:
            IntegratedBitPacking._integratedpack5(initoffset, in_, inpos, out, outpos)
        elif bit == 6:
            IntegratedBitPacking._integratedpack6(initoffset, in_, inpos, out, outpos)
        elif bit == 7:
            IntegratedBitPacking._integratedpack7(initoffset, in_, inpos, out, outpos)
        elif bit == 8:
            IntegratedBitPacking._integratedpack8(initoffset, in_, inpos, out, outpos)
        elif bit == 9:
            IntegratedBitPacking._integratedpack9(initoffset, in_, inpos, out, outpos)
        elif bit == 10:
            IntegratedBitPacking._integratedpack10(initoffset, in_, inpos, out, outpos)
        elif bit == 11:
            IntegratedBitPacking._integratedpack11(initoffset, in_, inpos, out, outpos)
        elif bit == 12:
            IntegratedBitPacking._integratedpack12(initoffset, in_, inpos, out, outpos)
        elif bit == 13:
            IntegratedBitPacking._integratedpack13(initoffset, in_, inpos, out, outpos)
        elif bit == 14:
            IntegratedBitPacking._integratedpack14(initoffset, in_, inpos, out, outpos)
        elif bit == 15:
            IntegratedBitPacking._integratedpack15(initoffset, in_, inpos, out, outpos)
        elif bit == 16:
            IntegratedBitPacking._integratedpack16(initoffset, in_, inpos, out, outpos)
        elif bit == 17:
            IntegratedBitPacking._integratedpack17(initoffset, in_, inpos, out, outpos)
        elif bit == 18:
            IntegratedBitPacking._integratedpack18(initoffset, in_, inpos, out, outpos)
        elif bit == 19:
            IntegratedBitPacking._integratedpack19(initoffset, in_, inpos, out, outpos)
        elif bit == 20:
            IntegratedBitPacking._integratedpack20(initoffset, in_, inpos, out, outpos)
        elif bit == 21:
            IntegratedBitPacking._integratedpack21(initoffset, in_, inpos, out, outpos)
        elif bit == 22:
            IntegratedBitPacking._integratedpack22(initoffset, in_, inpos, out, outpos)
        elif bit == 23:
            IntegratedBitPacking._integratedpack23(initoffset, in_, inpos, out, outpos)
        elif bit == 24:
            IntegratedBitPacking._integratedpack24(initoffset, in_, inpos, out, outpos)
        elif bit == 25:
            IntegratedBitPacking._integratedpack25(initoffset, in_, inpos, out, outpos)
        elif bit == 26:
            IntegratedBitPacking._integratedpack26(initoffset, in_, inpos, out, outpos)
        elif bit == 27:
            IntegratedBitPacking._integratedpack27(initoffset, in_, inpos, out, outpos)
        elif bit == 28:
            IntegratedBitPacking._integratedpack28(initoffset, in_, inpos, out, outpos)
        elif bit == 29:
            IntegratedBitPacking._integratedpack29(initoffset, in_, inpos, out, outpos)
        elif bit == 30:
            IntegratedBitPacking._integratedpack30(initoffset, in_, inpos, out, outpos)
        elif bit == 31:
            IntegratedBitPacking._integratedpack31(initoffset, in_, inpos, out, outpos)
        elif bit == 32:
            IntegratedBitPacking._integratedpack32(initoffset, in_, inpos, out, outpos)
        else:
            raise ValueError("Unsupported bit width.")
