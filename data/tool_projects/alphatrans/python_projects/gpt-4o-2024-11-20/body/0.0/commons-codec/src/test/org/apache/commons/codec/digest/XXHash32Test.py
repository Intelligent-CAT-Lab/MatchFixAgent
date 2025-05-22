from __future__ import annotations
import copy
import re
import unittest
import pytest
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.digest.XXHash32 import *


class XXHash32Test(unittest.TestCase):

    __expectedChecksum: str = ""

    __file: pathlib.Path = None

    def testverifyIncrementalChecksum_test4_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)
        checksum_value = h.getValue()
        file_name = self.__file.name
        self.assertEqual(
            f"checksum for {file_name}",
            self.__expectedChecksum,
            format(checksum_value, "x"),
        )

    def testverifyIncrementalChecksum_test3_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)
        h.getValue()
        self.__file.name

    def testverifyIncrementalChecksum_test2_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)
        h.getValue()

    def testverifyIncrementalChecksum_test1_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)

    def testverifyIncrementalChecksum_test0_decomposed(self) -> None:
        h = XXHash32.XXHash321()

    def testverifyChecksum_test4_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update1(b, 0, len(b))
        checksum_value = h.getValue()
        file_name = self.__file.name
        self.assertEqual(
            f"checksum for {file_name}",
            self.__expectedChecksum,
            format(checksum_value, "x"),
        )

    def testverifyChecksum_test3_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update1(b, 0, len(b))
        h.getValue()
        self.__file.name

    def testverifyChecksum_test2_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:
            b = self.__toByteArray(s)
            h.update1(b, 0, len(b))
        h.getValue()

    def testverifyChecksum_test1_decomposed(self) -> None:
        h = XXHash32.XXHash321()
        with self.__file.open("rb") as s:  # Open the file in binary read mode
            b = self.__toByteArray(s)  # Convert the file stream to a byte array
            h.update1(b, 0, len(b))  # Update the hash with the byte array

    def testverifyChecksum_test0_decomposed(self) -> None:
        h = XXHash32.XXHash321()

    @staticmethod
    def factory() -> typing.Collection[typing.List[typing.Any]]:
        return [
            ["org/apache/commons/codec/bla.tar", "fbb5c8d1"],
            ["org/apache/commons/codec/bla.tar.xz", "4106a208"],
            ["org/apache/commons/codec/small.bin", "f66c26f8"],
        ]

    @staticmethod
    def __copy(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        buffersize: int,
    ) -> int:
        buffer = bytearray(buffersize)
        count = 0
        while True:
            n = input_.readinto(buffer)
            if n == 0:
                break
            output.write(buffer[:n])
            count += n
        return count

    @staticmethod
    def __toByteArray(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> typing.List[int]:
        output = io.BytesIO()
        XXHash32Test.__copy(input_, output, 10240)
        return list(output.getvalue())
