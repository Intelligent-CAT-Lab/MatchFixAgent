from __future__ import annotations
import re
import random
import io
import typing
from typing import *
from src.main.me.lemire.integercompression.synth.UniformDataGenerator import *


class ClusteredDataGenerator:

    unidg: UniformDataGenerator = UniformDataGenerator(1, 0)

    @staticmethod
    def main(args: typing.List[str]) -> None:
        example = ClusteredDataGenerator().generateClustered(20, 1000)
        for k in range(len(example)):
            print(example[k])

    def generateClustered(self, N: int, Max: int) -> typing.List[int]:
        array = [0] * N
        self.fillClustered(array, 0, N, 0, Max)
        return array

    def __init__(self) -> None:
        pass

    def fillClustered(
        self, array: typing.List[int], offset: int, length: int, Min: int, Max: int
    ) -> None:
        range_ = Max - Min
        if range_ == length or length <= 10:
            self.fillUniform(array, offset, length, Min, Max)
            return

        cut = length // 2 + (
            self.unidg.rand.randint(0, range_ - length - 1)
            if range_ - length - 1 > 0
            else 0
        )
        p = self.unidg.rand.random()

        if p < 0.25:
            self.fillUniform(array, offset, length // 2, Min, Min + cut)
            self.fillClustered(
                array, offset + length // 2, length - length // 2, Min + cut, Max
            )
        elif p < 0.5:
            self.fillClustered(array, offset, length // 2, Min, Min + cut)
            self.fillUniform(
                array, offset + length // 2, length - length // 2, Min + cut, Max
            )
        else:
            self.fillClustered(array, offset, length // 2, Min, Min + cut)
            self.fillClustered(
                array, offset + length // 2, length - length // 2, Min + cut, Max
            )

    def fillUniform(
        self, array: typing.List[int], offset: int, length: int, Min: int, Max: int
    ) -> None:
        v = self.unidg.generateUniform(length, Max - Min)
        for k in range(len(v)):
            array[k + offset] = Min + v[k]
