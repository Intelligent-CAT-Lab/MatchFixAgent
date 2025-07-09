from __future__ import annotations
import time
import re
import random
from io import StringIO
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.IntWrapper import *
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
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedComposition import *
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *


class BenchmarkSkippable:

    codecs: typing.List[typing.Any] = [
        SkippableIntegratedComposition(
            IntegratedBinaryPacking(), IntegratedVariableByte()
        ),
        JustCopy(),
        VariableByte(),
        SkippableComposition(BinaryPacking(), VariableByte()),
        SkippableComposition(NewPFD(), VariableByte()),
        SkippableComposition(NewPFDS9(), VariableByte()),
        SkippableComposition(NewPFDS16(), VariableByte()),
        SkippableComposition(OptPFD(), VariableByte()),
        SkippableComposition(OptPFDS9(), VariableByte()),
        SkippableComposition(OptPFDS16(), VariableByte()),
        SkippableComposition(FastPFOR.FastPFOR1(), VariableByte()),
        SkippableComposition(FastPFOR128.FastPFOR1281(), VariableByte()),
        Simple9(),
        Simple16(),
    ]

    @staticmethod
    def main(args: typing.List[str]) -> None:
        print("# benchmark based on the ClusterData model from:")
        print("#     Vo Ngoc Anh and Alistair Moffat.")
        print("#     Index compression using 64-bit words.")
        print("#     Softw. Pract. Exper.40, 2 (February 2010), 131-147.")
        print()

        writer = None
        try:
            csv_file_name = f"benchmark-{time.strftime('%Y%m%dT%H%M%S')}.csv"
            writer = open(csv_file_name, "w", encoding="utf-8")
            print(f"# Results will be written into a CSV file: {csv_file_name}")
            print()
            BenchmarkSkippable.__test(writer, 20, 18, 10)
            print()
            print(f"Results were written into a CSV file: {csv_file_name}")
        finally:
            if writer is not None:
                writer.close()

    @staticmethod
    def __test(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        N: int,
        nbr: int,
        repeat: int,
    ) -> None:
        csvLog.write(
            '"Algorithm","Sparsity","Bits per int","Compress speed (MiS)","Decompress speed (MiS)"\n'
        )
        cdg = ClusteredDataGenerator()
        max_sparsity = 31 - nbr

        for sparsity in range(1, max_sparsity, 4):
            print(f"# sparsity {sparsity}")
            print("# generating random data...")
            data = BenchmarkSkippable.__generateTestData(cdg, N, nbr, sparsity)
            print("# generating random data... ok.")
            for c in BenchmarkSkippable.codecs:
                BenchmarkSkippable.__testCodec(csvLog, sparsity, c, data, repeat, False)
                BenchmarkSkippable.__testCodec(csvLog, sparsity, c, data, repeat, False)
                BenchmarkSkippable.__testCodec(csvLog, sparsity, c, data, repeat, True)
                BenchmarkSkippable.__testCodec(csvLog, sparsity, c, data, repeat, True)
                BenchmarkSkippable.__testCodec(csvLog, sparsity, c, data, repeat, True)

    @staticmethod
    def __generateTestData(
        dataGen: ClusteredDataGenerator, N: int, nbr: int, sparsity: int
    ) -> typing.List[typing.List[int]]:
        data = [None] * N
        dataSize = 1 << (nbr + sparsity)
        for i in range(N):
            data[i] = dataGen.generateClustered((1 << nbr), dataSize)
        return data

    @staticmethod
    def __testCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: typing.Any,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        if verbose:
            print(f"# {c}")
            print("# bits per int, compress speed (mis), decompression speed (mis)")

        N = len(data)

        totalSize = 0
        maxLength = 0
        for k in range(N):
            totalSize += len(data[k])
            if len(data[k]) > maxLength:
                maxLength = len(data[k])

        # 4x + 1024 to account for the possibility of some negative compression.
        compressBuffer = [0] * (4 * maxLength + 1024)
        decompressBuffer = [0] * (maxLength + 1024)
        metadataBuffer = [0] * maxLength
        blocksize = 1024

        # These variables hold time in microseconds (10^-6).
        compressTime = 0
        decompressTime = 0
        times = 5

        size = 0

        for r in range(repeat):
            size = 0
            for k in range(N):
                backupdata = data[k][:]  # Copy of data[k]

                # Compress data.
                beforeCompress = time.time_ns() // 1000
                outpos = IntWrapper.IntWrapper1()
                BenchmarkSkippable.__compressWithSkipTable(
                    c, backupdata, compressBuffer, outpos, metadataBuffer, blocksize
                )
                afterCompress = time.time_ns() // 1000

                # Measure time of compression.
                compressTime += afterCompress - beforeCompress
                thiscompsize = outpos.get()
                size += thiscompsize

                # Dry run
                volume = 0
                compressedpos = IntWrapper(0)
                volume = BenchmarkSkippable.__decompressFromSkipTable(
                    c,
                    compressBuffer,
                    compressedpos,
                    metadataBuffer,
                    blocksize,
                    decompressBuffer,
                )

                # Check the output size.
                if volume != len(backupdata):
                    raise RuntimeError(f"Bad output size with codec {c}")
                for j in range(volume):
                    if data[k][j] != decompressBuffer[j]:
                        raise RuntimeError(f"Bug in codec {c}")

                # Extract (uncompress) data.
                beforeDecompress = time.time_ns() // 1000
                for t in range(times):
                    compressedpos = IntWrapper(0)
                    volume = BenchmarkSkippable.__decompressFromSkipTable(
                        c,
                        compressBuffer,
                        compressedpos,
                        metadataBuffer,
                        blocksize,
                        decompressBuffer,
                    )
                afterDecompress = time.time_ns() // 1000

                # Measure time of extraction (uncompression).
                decompressTime += (afterDecompress - beforeDecompress) / times
                if volume != len(data[k]):
                    raise RuntimeError(
                        f"We have a bug (diff length) {c} expected {len(data[k])} got {volume}"
                    )

                # Verify: compare original array with compressed and uncompressed.
                for m in range(outpos.get()):
                    if decompressBuffer[m] != data[k][m]:
                        raise RuntimeError(
                            f"We have a bug (actual difference), expected {data[k][m]} found {decompressBuffer[m]} at {m}"
                        )

        if verbose:
            bitsPerInt = size * 32.0 / totalSize
            compressSpeed = round(totalSize * repeat / compressTime)
            decompressSpeed = round(totalSize * repeat / decompressTime)
            print(f"\t{bitsPerInt:.2f}\t{compressSpeed}\t{decompressSpeed}")
            csvLog.write(
                f'"{c}",{sparsity},{bitsPerInt:.2f},{compressSpeed},{decompressSpeed}\n'
            )
            csvLog.flush()

    @staticmethod
    def __decompressFromSkipTable(
        c: typing.Any,
        compressed: typing.List[int],
        compressedpos: IntWrapper,
        metadata: typing.List[int],
        blocksize: int,
        data: typing.List[int],
    ) -> int:
        metapos = 0
        length = metadata[metapos]
        metapos += 1
        uncomppos = IntWrapper.IntWrapper1()
        ival = IntWrapper.IntWrapper1()

        while uncomppos.get() < length:
            num = blocksize
            if num > length - uncomppos.get():
                num = length - uncomppos.get()
            location = metadata[metapos]
            metapos += 1
            initvalue = metadata[metapos]
            metapos += 1
            outputlocation = uncomppos.get()

            if location != compressedpos.get():
                raise RuntimeError(f"Bug {location} {compressedpos.get()} codec {c}")

            if isinstance(c, SkippableIntegerCODEC):
                c.headlessUncompress(
                    compressed,
                    compressedpos,
                    len(compressed) - uncomppos.get(),
                    data,
                    uncomppos,
                    num,
                )
                initvalue = Delta.fastinverseDelta1(
                    data, outputlocation, num, initvalue
                )
            elif isinstance(c, SkippableIntegratedIntegerCODEC):
                ival.set_(initvalue)
                c.headlessUncompress(
                    compressed,
                    compressedpos,
                    len(compressed) - uncomppos.get(),
                    data,
                    uncomppos,
                    num,
                    ival,
                )
            else:
                raise RuntimeError(f"Unrecognized codec {c}")

        return length

    @staticmethod
    def __compressWithSkipTable(
        c: typing.Any,
        data: typing.List[int],
        output: typing.List[int],
        outpos: IntWrapper,
        metadata: typing.List[int],
        blocksize: int,
    ) -> int:
        metapos = 0
        metadata[metapos] = len(data)
        metapos += 1
        inpos = IntWrapper.IntWrapper1()
        initvalue = 0
        ival = IntWrapper(initvalue)

        while inpos.get() < len(data):
            metadata[metapos] = outpos.get()
            metapos += 1
            metadata[metapos] = initvalue
            metapos += 1

            if isinstance(c, SkippableIntegerCODEC):
                size = (
                    blocksize
                    if blocksize <= len(data) - inpos.get()
                    else len(data) - inpos.get()
                )
                initvalue = Delta.delta1(data, inpos.get(), size, initvalue)
                c.headlessCompress(data, inpos, blocksize, output, outpos)
            elif isinstance(c, SkippableIntegratedIntegerCODEC):
                ival.set_(initvalue)
                c.headlessCompress(data, inpos, blocksize, output, outpos, ival)
                initvalue = ival.get()
            else:
                raise RuntimeError(f"Unrecognized codec {c}")

        return metapos
