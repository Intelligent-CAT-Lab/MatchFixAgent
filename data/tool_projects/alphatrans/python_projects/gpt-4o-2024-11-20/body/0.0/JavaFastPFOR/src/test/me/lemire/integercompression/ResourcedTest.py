from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntCompressor import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedIntCompressor import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class ResourcedTest(unittest.TestCase):

    codecs: typing.List[SkippableIntegerCODEC] = [
        JustCopy(),
        VariableByte(),
        SkippableComposition(BinaryPacking(), VariableByte()),
        SkippableComposition(NewPFD(), VariableByte()),
        SkippableComposition(NewPFDS9(), VariableByte()),
        SkippableComposition(NewPFDS16(), VariableByte()),
        SkippableComposition(OptPFD(), VariableByte()),
        SkippableComposition(OptPFDS9(), VariableByte()),
        SkippableComposition(OptPFDS16(), VariableByte()),
        SkippableComposition(FastPFOR128.FastPFOR1281(), VariableByte()),
        SkippableComposition(FastPFOR.FastPFOR1(), VariableByte()),
        Simple9(),
        Simple16(),
    ]

    def testIntCompressorTest_test3_decomposed(self) -> None:
        file_path = "src/test/resources/integers.txt"
        print(f"loading test data from {os.path.abspath(file_path)}")

        # Read integers from the file
        with open(file_path, "r") as file:
            data = [int(line.strip()) for line in file if line.strip()]

        # Test each codec
        for codec in self.codecs:
            iic = IntCompressor(0, codec)
            compressed = iic.compress(data)
            recovered = iic.uncompress(compressed)
            self.assertEqual(recovered, data, f"Codec {codec} failed for IntCompressor")

        # Test integrated codecs
        for codec in self.codecs:
            if isinstance(codec, SkippableIntegratedIntegerCODEC):
                iic = IntegratedIntCompressor(0, codec)
                compressed = iic.compress(data)
                recovered = iic.uncompress(compressed)
                self.assertEqual(
                    recovered,
                    data,
                    f"Integrated Codec {codec} failed for IntegratedIntCompressor",
                )

    def testIntCompressorTest_test2_decomposed(self) -> None:
        file_path = "src/test/resources/integers.txt"
        print(f"loading test data from {os.path.abspath(file_path)}")

        # Read integers from the file
        with open(file_path, "r") as file:
            data = [int(line.strip()) for line in file]

        # Iterate through each codec and test compression and decompression
        for codec in self.codecs:
            iic = IntegratedIntCompressor(0, codec)
            compressed = iic.compress(data)
            recovered = iic.uncompress(compressed)

            # Assert that the recovered data matches the original data
            self.assertEqual(recovered, data)

    def testIntCompressorTest_test1_decomposed(self) -> None:
        file_path = "src/test/resources/integers.txt"
        print(f"loading test data from {os.path.abspath(file_path)}")

        with open(file_path, "r") as file:
            lines = file.readlines()

        ai = [int(line.strip()) for line in lines]
        data = ai  # In Python, we can directly use the list as an array of integers

    def testIntCompressorTest_test0_decomposed(self) -> None:
        file_path = "src/test/resources/integers.txt"
        print(f"loading test data from {os.path.abspath(file_path)}")

        with open(file_path, "r") as file:
            lines = file.readlines()

        ai = [int(line.strip()) for line in lines]
