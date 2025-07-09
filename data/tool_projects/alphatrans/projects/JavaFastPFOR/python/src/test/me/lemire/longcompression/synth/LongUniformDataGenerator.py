from __future__ import annotations
import time
import re
import random
import os
import unittest
import pytest
import io
import typing
from typing import *


class LongUniformDataGenerator:

    rand: random.Random = random.Random()

    @staticmethod
    def negate(x: typing.List[int], Max: int) -> typing.List[int]:
        new_length = LongUniformDataGenerator.__saturatedCast(Max - len(x))
        ans = [0] * new_length
        i = 0
        c = 0
        for v in x:
            while i < v:
                ans[c] = i
                c += 1
                i += 1
            i += 1
        while c < len(ans):
            ans[c] = i
            c += 1
            i += 1
        return ans

    def __init__(self, constructorId: int, seed: int) -> None:
        if constructorId == 0:
            self.rand = random.Random(seed)
        else:
            self.rand = random.Random()

    @staticmethod
    def __saturatedCast(toInt: int) -> int:
        if toInt > (2**31 - 1):  # 2147483647 in Java is 2**31 - 1
            return 2**31 - 1
        else:
            return int(toInt)

    def generateUniformHash(self, N: int, Max: int) -> typing.List[int]:
        if N > Max:
            raise RuntimeError("not possible")

        ans = []
        s = set()

        while len(s) < N:
            s.add(int(self.rand.random() * Max))

        ans = list(s)
        ans.sort()

        return ans
