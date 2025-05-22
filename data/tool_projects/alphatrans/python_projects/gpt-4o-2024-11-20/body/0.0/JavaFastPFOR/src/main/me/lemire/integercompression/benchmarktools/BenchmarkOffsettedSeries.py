from __future__ import annotations
import re
import os
import enum
import pathlib
from io import StringIO
import io
import typing
from typing import *
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.benchmarktools.PerformanceLogger import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *


class BenchmarkOffsettedSeries:

    __DEFAULT_WARMUP: int = 2
    __DEFAULT_REPEAT: int = 5
    __DEFAULT_RANGE: int = 1 << 10
    __DEFAULT_MEAN: int = 1 << 20

    @staticmethod
    def main(args: typing.List[str]) -> None:
        import time
        from pathlib import Path

        # Create the CSV file with a timestamped name
        timestamp = time.strftime("%Y%m%dT%H%M%S", time.gmtime())
        csv_file = Path(f"benchmark-offsetted-{timestamp}.csv")

        writer = None
        try:
            # Open the file for writing
            writer = open(csv_file, "w", encoding="utf-8")
            print(f"# Results will be written into a CSV file: {csv_file.name}")
            print()

            # Call the run method with the writer and parameters
            BenchmarkOffsettedSeries.run(writer, 8 * 1024, 1280)

            print()
            print(f"# Results were written into a CSV file: {csv_file.name}")
        finally:
            # Ensure the writer is closed
            if writer is not None:
                writer.close()

    @staticmethod
    def run(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO], count: int, length: int
    ) -> None:
        codecs = [
            JustCopy(),
            BinaryPacking(),
            DeltaZigzagBinaryPacking(),
            DeltaZigzagVariableByte(),
            IntegratedBinaryPacking(),
            XorBinaryPacking(),
            FastPFOR128.FastPFOR1281(),
            FastPFOR.FastPFOR1(),
        ]

        csvWriter.write(
            '"Dataset","CODEC","Bits per int",'
            '"Compress speed (MiS)","Decompress speed (MiS)"\n'
        )

        BenchmarkOffsettedSeries.__benchmark0(
            csvWriter,
            codecs,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE,
        )
        BenchmarkOffsettedSeries.__benchmark0(
            csvWriter,
            codecs,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 5,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE,
        )

        codecs2 = [
            JustCopy(),
            BinaryPacking(),
            DeltaZigzagBinaryPacking(),
            DeltaZigzagVariableByte(),
            IntegratedBinaryPacking(),
            XorBinaryPacking(),
            FastPFOR128.FastPFOR1281(),
            FastPFOR.FastPFOR1(),
        ]

        freq = length // 4
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 0,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 0,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 5,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 0,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 10,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 0,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 0,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 2,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 5,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 2,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 10,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 2,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 0,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 4,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 5,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 4,
            freq,
        )
        BenchmarkOffsettedSeries.__benchmarkSine(
            csvWriter,
            codecs2,
            count,
            length,
            BenchmarkOffsettedSeries.__DEFAULT_MEAN >> 10,
            BenchmarkOffsettedSeries.__DEFAULT_RANGE >> 4,
            freq,
        )

    @staticmethod
    def __sortDataChunks(
        src: typing.List[typing.List[int]],
    ) -> typing.List[typing.List[int]]:
        dst = [sorted(chunk) for chunk in src]
        return dst

    @staticmethod
    def __deltaDataChunks(
        src: typing.List[typing.List[int]],
    ) -> typing.List[typing.List[int]]:
        dst = [
            [0] * len(s) for s in src
        ]  # Create a destination list with the same structure as src
        for i, s in enumerate(src):
            d = dst[i]
            prev = 0
            for j, value in enumerate(s):
                d[j] = value - prev
                prev = value
        return dst

    @staticmethod
    def __generateDataChunks(
        seed: int, count: int, length: int, mean: int, range_: int
    ) -> typing.List[typing.List[int]]:
        offset = mean - range_ // 2
        chunks = []
        r = random.Random(seed)
        for i in range(count):
            chunk = [r.randint(0, range_ - 1) + offset for _ in range(length)]
            chunks.append(chunk)
        return chunks

    @staticmethod
    def __generateSineDataChunks(
        seed: int, count: int, length: int, mean: int, range_: int, freq: int
    ) -> typing.List[typing.List[int]]:
        import random
        import math

        chunks = []
        r = random.Random(seed)
        for i in range(count):
            chunk = [0] * length
            phase = r.randint(0, 2 * freq - 1)
            for j in range(length):
                angle = 2.0 * math.pi * (j + phase) / freq
                chunk[j] = int(mean + math.sin(angle) * range_)
            chunks.append(chunk)
        return chunks

    @staticmethod
    def __getMaxLen(data: typing.List[typing.List[int]]) -> int:
        max_len = 0
        for array in data:
            if len(array) > max_len:
                max_len = len(array)
        return max_len

    @staticmethod
    def __decompress(
        logger: PerformanceLogger,
        codec: IntegerCODEC,
        src: typing.List[int],
        srcLen: int,
        dst: typing.List[int],
    ) -> int:
        inpos = IntWrapper.IntWrapper1()
        outpos = IntWrapper.IntWrapper1()
        logger.decompressionTimer.start()
        codec.uncompress0(src, inpos, srcLen, dst, outpos)
        logger.decompressionTimer.end()
        return outpos.get()

    @staticmethod
    def __compress(
        logger: PerformanceLogger,
        codec: IntegerCODEC,
        src: typing.List[int],
        dst: typing.List[int],
    ) -> int:
        inpos = IntWrapper.IntWrapper1()
        outpos = IntWrapper.IntWrapper1()
        logger.compressionTimer.start()
        codec.compress0(src, inpos, len(src), dst, outpos)
        logger.compressionTimer.end()
        out_size = outpos.get()
        logger.addOriginalSize(len(src))
        logger.addCompressedSize(out_size)
        return out_size

    @staticmethod
    def __checkArray(
        expected: typing.List[int],
        actualArray: typing.List[int],
        actualLen: int,
        codec: IntegerCODEC,
    ) -> None:
        if actualLen != len(expected):
            raise RuntimeError(
                f"Length mismatch: expected={len(expected)} actual={actualLen} codec={codec}"
            )

        for i in range(len(expected)):
            if actualArray[i] != expected[i]:
                raise RuntimeError(
                    f"Value mismatch: where={i} expected={expected[i]} actual={actualArray[i]} codec={codec}"
                )

    @staticmethod
    def __benchmark2(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        dataName: str,
        codecName: str,
        codec: IntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
    ) -> None:
        logger = PerformanceLogger()

        maxLen = BenchmarkOffsettedSeries.__getMaxLen(data)
        compressBuffer = [0] * (4 * maxLen + 1024)
        decompressBuffer = [0] * maxLen

        for _ in range(repeat):
            for array in data:
                compSize = BenchmarkOffsettedSeries.__compress(
                    logger, codec, array, compressBuffer
                )
                decompSize = BenchmarkOffsettedSeries.__decompress(
                    logger, codec, compressBuffer, compSize, decompressBuffer
                )
                BenchmarkOffsettedSeries.__checkArray(
                    array, decompressBuffer, decompSize, codec
                )

        if csvWriter is not None:
            csvWriter.write(
                f'"{dataName}","{codecName}",{logger.getBitPerInt():.2f},{logger.getCompressSpeed():.0f},{logger.getDecompressSpeed():.0f}\n'
            )

    @staticmethod
    def __benchmark1(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        dataName: str,
        codecs: typing.List[IntegerCODEC],
        data: typing.List[typing.List[int]],
        repeat: int,
        warmup: int,
    ) -> None:
        print(f"Processing: {dataName}")
        for codec in codecs:
            codecName = str(codec)
            for _ in range(warmup):
                BenchmarkOffsettedSeries.__benchmark2(
                    None, None, None, codec, data, repeat
                )
            BenchmarkOffsettedSeries.__benchmark2(
                csvWriter, dataName, codecName, codec, data, repeat
            )

    @staticmethod
    def __benchmark0(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        codecs: typing.List[IntegerCODEC],
        count: int,
        length: int,
        mean: int,
        range_: int,
    ) -> None:
        dataProp = f"(mean={mean} range={range_})"

        randData = BenchmarkOffsettedSeries.__generateDataChunks(
            0, count, length, mean, range_
        )
        deltaData = BenchmarkOffsettedSeries.__deltaDataChunks(randData)
        sortedData = BenchmarkOffsettedSeries.__sortDataChunks(randData)
        sortedDeltaData = BenchmarkOffsettedSeries.__deltaDataChunks(sortedData)

        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Random {dataProp}",
            codecs,
            randData,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )
        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Random+delta {dataProp}",
            codecs,
            deltaData,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )
        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Sorted {dataProp}",
            codecs,
            sortedData,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )
        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Sorted+delta {dataProp}",
            codecs,
            sortedDeltaData,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )

    @staticmethod
    def __benchmarkSine(
        csvWriter: typing.Union[io.TextIOWrapper, io.StringIO],
        codecs: typing.List[IntegerCODEC],
        count: int,
        length: int,
        mean: int,
        range_: int,
        freq: int,
    ) -> None:
        dataProp = f"(mean={mean} range={range_} freq={freq})"
        data = BenchmarkOffsettedSeries.__generateSineDataChunks(
            0, count, length, mean, range_, freq
        )
        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Sine {dataProp}",
            codecs,
            data,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )
        BenchmarkOffsettedSeries.__benchmark1(
            csvWriter,
            f"Sine+delta {dataProp}",
            codecs,
            data,
            BenchmarkOffsettedSeries.__DEFAULT_REPEAT,
            BenchmarkOffsettedSeries.__DEFAULT_WARMUP,
        )
