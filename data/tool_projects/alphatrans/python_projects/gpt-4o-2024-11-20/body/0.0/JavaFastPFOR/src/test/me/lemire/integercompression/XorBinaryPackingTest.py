from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *


class XorBinaryPackingTest(unittest.TestCase):

    def testcompressAndUncompress5_test0_decomposed(self) -> None:
        data = [i for i in range(256)]
        self.__checkCompressAndUncompress("compressAndUncompress5", data)

    def testcompressAndUncompress4_test0_decomposed(self) -> None:
        data = [0] * 256
        data[0:128] = [3] * 128
        data[128:256] = [2] * 128
        self.__checkCompressAndUncompress("compressAndUncompress4", data)

    def testcompressAndUncompress3_test0_decomposed(self) -> None:
        data = [0] * 256
        data[0:127] = [2] * 127
        data[128:256] = [3] * 128
        self.__checkCompressAndUncompress("compressAndUncompress3", data)

    def testcompressAndUncompress2_test0_decomposed(self) -> None:
        data = [i * (i + 1) // 2 for i in range(128)]
        self.__checkCompressAndUncompress("compressAndUncompress2", data)

    def testcompressAndUncompress1_test0_decomposed(self) -> None:
        data = [i for i in range(128)]
        self.__checkCompressAndUncompress("compressAndUncompress1", data)

    def testcompressAndUncompress0_test0_decomposed(self) -> None:
        data = [0] * 128
        data[0:32] = [1] * 32
        data[32:64] = [2] * 32
        data[64:96] = [4] * 32
        data[96:128] = [8] * 32
        self.__checkCompressAndUncompress("compressAndUncompress0", data)

    @staticmethod
    def __checkCompressAndUncompress(label: str, data: typing.List[int]) -> None:
        codec = XorBinaryPacking()
        comp_buf = TestUtils.compress1(codec, data)
        decomp_buf = TestUtils._uncompress0(codec, comp_buf, len(data))
        assert (
            data == decomp_buf
        ), f"{label}: Decompressed data does not match the original"
