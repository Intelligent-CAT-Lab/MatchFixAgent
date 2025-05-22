from __future__ import annotations
import re
import io
import typing
from typing import *


class Delta:

    @staticmethod
    def fastinverseDelta1(
        data: typing.List[int], start: int, length: int, init: int
    ) -> int:
        data[start] += init
        sz0 = (length // 4) * 4
        i = 1
        if sz0 >= 4:
            a = data[start]
            while i < sz0 - 4:
                a = data[start + i] + a
                data[start + i] = a
                a = data[start + i + 1] + a
                data[start + i + 1] = a
                a = data[start + i + 2] + a
                data[start + i + 2] = a
                a = data[start + i + 3] + a
                data[start + i + 3] = a
                i += 4

        while i != length:
            data[start + i] += data[start + i - 1]
            i += 1

        return data[start + length - 1]

    @staticmethod
    def fastinverseDelta0(data: typing.List[int]) -> None:
        sz0 = len(data) // 4 * 4
        i = 1
        if sz0 >= 4:
            a = data[0]
            while i < sz0 - 4:
                a = data[i] = data[i] + a
                a = data[i + 1] = data[i + 1] + a
                a = data[i + 2] = data[i + 2] + a
                a = data[i + 3] = data[i + 3] + a
                i += 4

        while i < len(data):
            data[i] += data[i - 1]
            i += 1

    @staticmethod
    def inverseDelta(data: typing.List[int]) -> None:
        for i in range(1, len(data)):
            data[i] += data[i - 1]

    @staticmethod
    def delta2(
        data: typing.List[int],
        start: int,
        length: int,
        init: int,
        out: typing.List[int],
    ) -> int:
        for i in range(length - 1, 0, -1):
            out[i] = data[start + i] - data[start + i - 1]
        out[0] = data[start] - init
        return data[start + length - 1]

    @staticmethod
    def delta1(data: typing.List[int], start: int, length: int, init: int) -> int:
        nextinit = data[start + length - 1]
        for i in range(length - 1, 0, -1):
            data[start + i] -= data[start + i - 1]
        data[start] -= init
        return nextinit

    @staticmethod
    def delta0(data: typing.List[int]) -> None:
        for i in range(len(data) - 1, 0, -1):
            data[i] -= data[i - 1]
