from __future__ import annotations
import time
import re
import random
import os
import io
import typing
from typing import *


class UniformDataGenerator:

    rand: random.Random = random.Random()

    def generateUniform(self, N: int, Max: int) -> typing.List[int]:
        if N * 2 > Max:
            return self.negate(self.generateUniform(Max - N, Max), Max)
        if 2048 * N > Max:
            return self.generateUniformBitmap(N, Max)
        return self.generateUniformHash(N, Max)

    @staticmethod
    def negate(x: typing.List[int], Max: int) -> typing.List[int]:
        ans = [0] * (Max - len(x))
        i = 0
        c = 0
        for j in range(len(x)):
            v = x[j]
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

    def generateUniformBitmap(self, N: int, Max: int) -> typing.List[int]:
        if N > Max:
            raise RuntimeError("not possible")

        ans = [0] * N
        bs = set()
        cardinality = 0

        while cardinality < N:
            v = self.rand.randint(0, Max - 1)
            if v not in bs:
                bs.add(v)
                cardinality += 1

        pos = 0
        for i in sorted(bs):
            ans[pos] = i
            pos += 1

        return ans

    def generateUniformHash(self, N: int, Max: int) -> typing.List[int]:
        if N > Max:
            raise RuntimeError("not possible")

        ans = []
        s = set()

        while len(s) < N:
            s.add(self.rand.randint(0, Max - 1))

        ans = list(s)
        ans.sort()

        return ans
