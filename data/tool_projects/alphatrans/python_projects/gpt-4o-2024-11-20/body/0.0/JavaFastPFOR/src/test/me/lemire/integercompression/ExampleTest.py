from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedIntCompressor import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *


class ExampleTest(unittest.TestCase):

    def testheadlessDemo_test10_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()

        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()

        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )
        length2 = outPos.get() - previous.get()
        compressed = compressed[: length1 + length2]

        print(
            f"compressed unsorted integers from {len(uncompressed1) * 4}B to {length1 * 4}B"
        )
        print(
            f"compressed unsorted integers from {len(uncompressed2) * 4}B to {length2 * 4}B"
        )
        print(f"Total compressed output {len(compressed)}")

        recovered1 = [0] * len(uncompressed1)
        recovered2 = [0] * len(uncompressed2)
        inPos = IntWrapper.IntWrapper1()

        print(f"Decoding first array starting at pos = {inPos.get()}")
        codec.headlessUncompress(
            compressed,
            inPos,
            len(compressed),
            recovered1,
            IntWrapper(0),
            len(uncompressed1),
        )

        print(f"Decoding second array starting at pos = {inPos.get()}")
        codec.headlessUncompress(
            compressed,
            inPos,
            len(compressed),
            recovered2,
            IntWrapper(0),
            len(uncompressed2),
        )

        if uncompressed1 != recovered1:
            raise RuntimeError("First array does not match.")
        if uncompressed2 != recovered2:
            raise RuntimeError("Second array does not match.")

        print("The arrays match, your code is probably ok.")

    def testheadlessDemo_test9_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()

        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()

        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )
        length2 = outPos.get() - previous.get()
        compressed = compressed[: length1 + length2]

        print(
            f"compressed unsorted integers from {len(uncompressed1) * 4}B to {length1 * 4}B"
        )
        print(
            f"compressed unsorted integers from {len(uncompressed2) * 4}B to {length2 * 4}B"
        )
        print(f"Total compressed output {len(compressed)}")

        recovered1 = [0] * len(uncompressed1)
        recovered2 = [0] * len(uncompressed2)
        inPos = IntWrapper.IntWrapper1()

        print(f"Decoding first array starting at pos = {inPos.get()}")
        codec.headlessUncompress(
            compressed,
            inPos,
            len(compressed),
            recovered1,
            IntWrapper(0),
            len(uncompressed1),
        )

        print(f"Decoding second array starting at pos = {inPos.get()}")
        codec.headlessUncompress(
            compressed,
            inPos,
            len(compressed),
            recovered2,
            IntWrapper(0),
            len(uncompressed2),
        )

    def testheadlessDemo_test8_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()

        # Compress the first array
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()

        # Compress the second array
        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )
        length2 = outPos.get() - previous.get()

        # Resize the compressed array
        compressed = compressed[: length1 + length2]

        print(
            f"compressed unsorted integers from {len(uncompressed1) * 4}B to {length1 * 4}B"
        )
        print(
            f"compressed unsorted integers from {len(uncompressed2) * 4}B to {length2 * 4}B"
        )
        print(f"Total compressed output {len(compressed)}")

        # Decompress the arrays
        recovered1 = [0] * len(uncompressed1)
        recovered2 = [0] * len(uncompressed2)
        inPos = IntWrapper.IntWrapper1()
        print(f"Decoding first array starting at pos = {inPos.get()}")
        codec.headlessUncompress(
            compressed,
            inPos,
            len(compressed),
            recovered1,
            IntWrapper(0),
            len(uncompressed1),
        )

    def testheadlessDemo_test7_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()

        # Compress the first array
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()

        # Compress the second array
        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )
        length2 = outPos.get() - previous.get()

        # Resize the compressed array
        compressed = compressed[: length1 + length2]

        print(
            f"compressed unsorted integers from {len(uncompressed1) * 4}B to {length1 * 4}B"
        )
        print(
            f"compressed unsorted integers from {len(uncompressed2) * 4}B to {length2 * 4}B"
        )
        print(f"Total compressed output {len(compressed)}")

        recovered1 = [0] * len(uncompressed1)
        recovered2 = [0] * len(uncompressed2)
        inPos = IntWrapper.IntWrapper1()

    def testheadlessDemo_test6_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )
        length2 = outPos.get() - previous.get()

    def testheadlessDemo_test5_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed2,
            IntWrapper.IntWrapper1(),
            len(uncompressed2),
            compressed,
            outPos,
        )

    def testheadlessDemo_test4_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())
        IntWrapper.IntWrapper1()

    def testheadlessDemo_test3_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )
        length1 = outPos.get() - previous.get()
        previous = IntWrapper(outPos.get())

    def testheadlessDemo_test2_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()
        codec.headlessCompress(
            uncompressed1,
            IntWrapper.IntWrapper1(),
            len(uncompressed1),
            compressed,
            outPos,
        )

    def testheadlessDemo_test1_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())
        outPos = IntWrapper.IntWrapper1()
        previous = IntWrapper.IntWrapper1()
        IntWrapper.IntWrapper1()

    def testheadlessDemo_test0_decomposed(self) -> None:
        print("Compressing arrays with minimal header...")
        uncompressed1 = [1, 2, 1, 3, 1]
        uncompressed2 = [3, 2, 4, 6, 1]
        compressed = [0] * (len(uncompressed1) + len(uncompressed2) + 1024)
        codec = SkippableComposition(BinaryPacking(), VariableByte())

    def testadvancedExample_test9_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        for k in range(TotalSize // ChunkSize):
            regularcodec.compress0(
                data, inputoffset, ChunkSize, compressed, outputoffset
            )

        lastcodec.compress0(
            data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset
        )

        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * ChunkSize
        compoff = IntWrapper(0)
        currentpos = 0

        while compoff.get() < len(compressed):
            recoffset = IntWrapper(0)
            regularcodec.uncompress0(
                compressed,
                compoff,
                len(compressed) - compoff.get(),
                recovered,
                recoffset,
            )

            if recoffset.get() < ChunkSize:  # last chunk detected
                ivb.uncompress0(
                    compressed,
                    compoff,
                    len(compressed) - compoff.get(),
                    recovered,
                    recoffset,
                )

            for i in range(recoffset.get()):
                if data[currentpos + i] != recovered[i]:
                    raise RuntimeError("bug")  # could use assert

            currentpos += recoffset.get()

        print("data is recovered without loss")
        print()

    def testadvancedExample_test8_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]
        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        for k in range(TotalSize // ChunkSize):
            regularcodec.compress0(
                data, inputoffset, ChunkSize, compressed, outputoffset
            )

        lastcodec.compress0(
            data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset
        )

        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * ChunkSize
        compoff = IntWrapper(0)
        currentpos = 0

        while compoff.get() < len(compressed):
            recoffset = IntWrapper(0)
            regularcodec.uncompress0(
                compressed,
                compoff,
                len(compressed) - compoff.get(),
                recovered,
                recoffset,
            )

            if recoffset.get() < ChunkSize:  # last chunk detected
                ivb.uncompress0(
                    compressed,
                    compoff,
                    len(compressed) - compoff.get(),
                    recovered,
                    recoffset,
                )

            for i in range(recoffset.get()):
                if data[currentpos + i] != recovered[i]:
                    raise RuntimeError("bug")  # could use assert

            currentpos += recoffset.get()

    def testadvancedExample_test7_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        for k in range(TotalSize // ChunkSize):
            regularcodec.compress0(
                data, inputoffset, ChunkSize, compressed, outputoffset
            )

        lastcodec.compress0(
            data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset
        )

        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * ChunkSize
        compoff = IntWrapper(0)

    def testadvancedExample_test6_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        for k in range(TotalSize // ChunkSize):
            regularcodec.compress0(
                data, inputoffset, ChunkSize, compressed, outputoffset
            )

        lastcodec.compress0(
            data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset
        )

        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]

    def testadvancedExample_test5_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        for k in range(TotalSize // ChunkSize):
            regularcodec.compress0(
                data, inputoffset, ChunkSize, compressed, outputoffset
            )

        lastcodec.compress0(
            data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset
        )

    def testadvancedExample_test4_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

    def testadvancedExample_test3_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )

        data = [k for k in range(TotalSize)]

        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

        compressed = [0] * (TotalSize + 1024)
        inputoffset = IntWrapper(0)

    def testadvancedExample_test2_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )
        data = [k for k in range(TotalSize)]
        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()
        lastcodec = IntegratedComposition(regularcodec, ivb)

    def testadvancedExample_test1_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )
        data = [k for k in range(TotalSize)]
        regularcodec = IntegratedBinaryPacking()
        ivb = IntegratedVariableByte()

    def testadvancedExample_test0_decomposed(self) -> None:
        TotalSize = 2342351
        ChunkSize = 16384
        print(
            f"Compressing {TotalSize} integers using chunks of {ChunkSize} integers ({ChunkSize * 4 // 1024}KB)"
        )
        print(
            "(It is often better for applications to work in chunks fitting in CPU cache.)"
        )
        data = [k for k in range(TotalSize)]
        regularcodec = IntegratedBinaryPacking()

    def testunsortedExample_test7_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000

        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed unsorted integers from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * N
        recoffset = IntWrapper(0)

        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

        if data == recovered:
            print("data is recovered without loss")
        else:
            raise RuntimeError("bug")

        print()

    def testunsortedExample_test6_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000

        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed unsorted integers from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * N
        recoffset = IntWrapper(0)

        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

    def testunsortedExample_test5_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000

        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

        print(
            f"compressed unsorted integers from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * N
        recoffset = IntWrapper(0)

    def testunsortedExample_test4_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000
        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed unsorted integers from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]

    def testunsortedExample_test3_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000
        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

    def testunsortedExample_test2_decomposed(self) -> None:
        N = 1333333
        data = [3] * N  # Initialize the array with 3
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000
        compressed = [0] * (N + 1024)  # Initialize the compressed array
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

    def testunsortedExample_test1_decomposed(self) -> None:
        N = 1333333
        data = [0] * N
        for k in range(0, N, 1):
            data[k] = 3
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000
        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())
        inputoffset = IntWrapper(0)

    def testunsortedExample_test0_decomposed(self) -> None:
        N = 1333333
        data = [3] * N
        for k in range(0, N, 5):
            data[k] = 100
        for k in range(0, N, 533):
            data[k] = 10000
        compressed = [0] * (N + 1024)
        codec = Composition(FastPFOR.FastPFOR1(), VariableByte())

    def testbasicExampleHeadless_test7_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k

        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)
        compressed[0] = len(data)

        codec.headlessCompress(
            data, inputoffset, len(data), compressed, outputoffset, IntWrapper(0)
        )
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        howmany = compressed[0]
        recovered = [0] * howmany
        recoffset = IntWrapper(0)

        codec.headlessUncompress(
            compressed,
            IntWrapper(1),
            len(compressed),
            recovered,
            recoffset,
            howmany,
            IntWrapper(0),
        )

        if data == recovered:
            print("data is recovered without loss")
        else:
            raise RuntimeError("bug")

        print()

    def testbasicExampleHeadless_test6_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k

        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)
        compressed[0] = len(data)

        codec.headlessCompress(
            data, inputoffset, len(data), compressed, outputoffset, IntWrapper(0)
        )
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        howmany = compressed[0]
        recovered = [0] * howmany
        recoffset = IntWrapper(0)

        codec.headlessUncompress(
            compressed,
            IntWrapper(1),
            len(compressed),
            recovered,
            recoffset,
            howmany,
            IntWrapper(0),
        )

    def testbasicExampleHeadless_test5_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k

        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)
        compressed[0] = len(data)

        codec.headlessCompress(
            data, inputoffset, len(data), compressed, outputoffset, IntWrapper(0)
        )
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )

        compressed = compressed[: outputoffset.intValue()]
        howmany = compressed[0]
        recovered = [0] * howmany
        recoffset = IntWrapper(0)

    def testbasicExampleHeadless_test4_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k

        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)
        compressed[0] = len(data)

        codec.headlessCompress(
            data, inputoffset, len(data), compressed, outputoffset, IntWrapper(0)
        )

        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]

    def testbasicExampleHeadless_test3_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k
        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)
        compressed[0] = len(data)
        codec.headlessCompress(
            data, inputoffset, len(data), compressed, outputoffset, IntWrapper(0)
        )

    def testbasicExampleHeadless_test2_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k
        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(1)

    def testbasicExampleHeadless_test1_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k
        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)

    def testbasicExampleHeadless_test0_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go using the headless approach")
        for k in range(len(data)):
            data[k] = k
        codec = SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )

    def testbasicExample_test7_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * len(data)
        recoffset = IntWrapper(0)
        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )
        if data == recovered:
            print("data is recovered without loss")
        else:
            raise RuntimeError("bug")
        print()

    def testbasicExample_test6_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * len(data)
        recoffset = IntWrapper(0)
        codec.uncompress0(
            compressed, IntWrapper(0), len(compressed), recovered, recoffset
        )

    def testbasicExample_test5_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]
        recovered = [0] * len(data)
        recoffset = IntWrapper(0)

    def testbasicExample_test4_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {outputoffset.intValue() * 4 // 1024}KB"
        )
        compressed = compressed[: outputoffset.intValue()]

    def testbasicExample_test3_decomposed(self) -> None:
        data = [0] * 2342351
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (len(data) + 1024)
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)
        codec.compress0(data, inputoffset, len(data), compressed, outputoffset)

    def testbasicExample_test2_decomposed(self) -> None:
        data = [0] * 2342351  # Create an array of size 2342351 initialized to 0
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k  # Populate the array with values from 0 to len(data) - 1
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (
            len(data) + 1024
        )  # Create a compressed array with extra space
        inputoffset = IntWrapper(0)
        outputoffset = IntWrapper(0)

    def testbasicExample_test1_decomposed(self) -> None:
        data = [0] * 2342351  # Create an array of size 2342351 initialized to 0
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k  # Populate the array with values from 0 to len(data) - 1
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )
        compressed = [0] * (
            len(data) + 1024
        )  # Create a compressed array with extra space
        inputoffset = IntWrapper(0)  # Initialize IntWrapper with value 0

    def testbasicExample_test0_decomposed(self) -> None:
        data = [0] * 2342351  # Create a list of 2342351 integers initialized to 0
        print(f"Compressing {len(data)} integers in one go")
        for k in range(len(data)):
            data[k] = k  # Assign each index its value
        codec = IntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        )

    def testsuperSimpleExample_test3_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)
        recov = iic.uncompress(compressed)
        print(
            f"compressed from {len(data) * 4 // 1024}KB to {len(compressed) * 4 // 1024}KB"
        )
        if recov != data:
            raise RuntimeError("bug")

    def testsuperSimpleExample_test2_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)
        recov = iic.uncompress(compressed)

    def testsuperSimpleExample_test1_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
        data = [k for k in range(2342351)]
        print(f"Compressing {len(data)} integers using friendly interface")
        compressed = iic.compress(data)

    def testsuperSimpleExample_test0_decomposed(self) -> None:
        iic = IntegratedIntCompressor(1, None)
