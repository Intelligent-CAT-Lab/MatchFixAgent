from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32C import *


class PureJavaCrc32CTest(unittest.TestCase):

    __data: typing.List[int] = [0] * 32
    __crc: PureJavaCrc32C = PureJavaCrc32C()

    def testDecreasing_test0_decomposed(self) -> None:
        for i in range(len(self.__data)):
            self.__data[i] = 31 - i
        self.__check(0x113FDB5C)

    def testIncreasing_test0_decomposed(self) -> None:
        for i in range(len(self.__data)):
            self.__data[i] = i
        self.__check(0x46DD794E)

    def testOnes_test1_decomposed(self) -> None:
        self.__data = [0xFF] * 32  # Fill the data array with 0xFF
        self.__check(0x62A8AB43)  # Call the check method with the expected value

    def testOnes_test0_decomposed(self) -> None:
        self.__data = [0xFF] * 32

    def testZeros_test1_decomposed(self) -> None:
        self.__data = [0] * 32  # Fill the data array with zeros
        self.__check(0x8A9136AA)  # Call the check method with the expected value

    def testZeros_test0_decomposed(self) -> None:
        self.__data = [0] * 32

    def __check(self, expected: int) -> None:
        self.__crc.reset()
        self.__crc.update0(self.__data, 0, len(self.__data))
        actual = self.__crc.getValue()
        self.assertEqual(
            hex(expected).lower(),
            hex(actual).lower(),
            f"Expected {hex(expected).lower()} but got {hex(actual).lower()}",
        )
