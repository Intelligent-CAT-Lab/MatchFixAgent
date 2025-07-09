from __future__ import annotations
import re
import random
import datetime
import decimal
from io import StringIO
import io
import typing
from typing import *
import os
from src.main.com.kamikaze.pfordelta.PForDelta import *
from src.main.me.lemire.integercompression.BinaryPacking import *
from src.main.me.lemire.integercompression.ByteIntegerCODEC import *
from src.main.me.lemire.integercompression.Composition import *
from src.main.me.lemire.integercompression.DeltaZigzagBinaryPacking import *
from src.main.me.lemire.integercompression.DeltaZigzagVariableByte import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.GroupSimple9 import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.IntegerCODEC import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.VariableByte import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.differential.IntegratedBinaryPacking import *
from src.main.me.lemire.integercompression.differential.IntegratedByteIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedComposition import *
from src.main.me.lemire.integercompression.differential.IntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedVariableByte import *
from src.main.me.lemire.integercompression.differential.XorBinaryPacking import *
from src.main.me.lemire.integercompression.synth.ClusteredDataGenerator import *


class Benchmark:

    @staticmethod
    def testKamikaze(
        data: typing.List[typing.List[int]], repeat: int, verbose: bool
    ) -> None:
        from decimal import Decimal
        import time

        df = "{:.2f}"
        dfspeed = "{:.0f}"
        if verbose:
            print("# kamikaze PForDelta")
            print("# bits per int, compress speed (mis), decompression speed (mis) ")

        N = len(data)
        totalsize = sum(len(arr) for arr in data)
        maxlength = max(len(arr) for arr in data)

        buffer = [0] * (maxlength + 1024)
        size = 0
        comptime = 0
        decomptime = 0

        for r in range(repeat):
            size = 0
            for k in range(N):
                outpos = 0
                backupdata = data[k][:]  # Copy of data[k]

                # Compression
                bef = time.time_ns() // 1000
                Delta.delta0(backupdata)
                dataout = []
                for K in range(0, len(data[k]), 128):
                    compressedbuf = PForDelta.compressOneBlockOpt(
                        backupdata[K : K + 128], 128
                    )
                    dataout.append(compressedbuf)
                    outpos += len(compressedbuf)
                aft = time.time_ns() // 1000
                comptime += aft - bef
                thiscompsize = outpos
                size += thiscompsize

                # Decompression
                bef = time.time_ns() // 1000
                datauncomp = []
                deltaoffset = 0
                for compbuf in dataout:
                    tmpbuf = [0] * 128
                    PForDelta.decompressOneBlock(tmpbuf, compbuf, 128)
                    tmpbuf[0] += deltaoffset
                    Delta.fastinverseDelta0(tmpbuf)
                    deltaoffset = tmpbuf[127]
                    datauncomp.append(tmpbuf)
                aft = time.time_ns() // 1000
                decomptime += aft - bef

                # Validation
                if len(datauncomp) * 128 != len(data[k]):
                    raise RuntimeError(
                        f"we have a bug (diff length) expected {len(data[k])} got {len(datauncomp) * 128}"
                    )
                for m in range(len(data[k])):
                    if datauncomp[m // 128][m % 128] != data[k][m]:
                        raise RuntimeError(
                            f"we have a bug (actual difference), expected {data[k][m]} found {buffer[m]} at {m}"
                        )

        line = ""
        line += "\t" + df.format(size * 32.0 / totalsize)
        line += "\t" + dfspeed.format(totalsize * repeat / comptime)
        line += "\t" + dfspeed.format(totalsize * repeat / decomptime)
        if verbose:
            print(line)

    @staticmethod
    def main(args: typing.List[str]) -> None:
        print("# benchmark based on the ClusterData model from:")
        print("#     Vo Ngoc Anh and Alistair Moffat.")
        print("#     Index compression using 64-bit words.")
        print("#     Softw. Pract. Exper.40, 2 (February 2010), 131-147.")
        print()

        writer = None
        try:
            csv_file_name = "benchmark-{:%Y%m%dT%H%M%S}.csv".format(
                datetime.datetime.now()
            )
            writer = open(csv_file_name, "w", encoding="utf-8")
            print(f"# Results will be written into a CSV file: {csv_file_name}")
            print()
            Benchmark.__test(writer, 20, 18, 10)
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

        for sparsity in range(1, max_sparsity):
            print(f"# sparsity {sparsity}")
            print("# generating random data...")
            data = Benchmark.__generateTestData(cdg, N, nbr, sparsity)
            print("# generating random data... ok.")

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR128.FastPFOR1281(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR.FastPFOR1(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR.FastPFOR1(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(FastPFOR.FastPFOR1(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.testKamikaze(data, repeat, False)
            Benchmark.testKamikaze(data, repeat, False)
            Benchmark.testKamikaze(data, repeat, True)
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                IntegratedComposition(
                    IntegratedBinaryPacking(), IntegratedVariableByte()
                ),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                IntegratedComposition(
                    IntegratedBinaryPacking(), IntegratedVariableByte()
                ),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                IntegratedComposition(
                    IntegratedBinaryPacking(), IntegratedVariableByte()
                ),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(csvLog, sparsity, JustCopy(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, JustCopy(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, JustCopy(), data, repeat, True)
            print()

            Benchmark.__testByteCodec(
                csvLog, sparsity, VariableByte(), data, repeat, False
            )
            Benchmark.__testByteCodec(
                csvLog, sparsity, VariableByte(), data, repeat, False
            )
            Benchmark.__testByteCodec(
                csvLog, sparsity, VariableByte(), data, repeat, True
            )
            print()

            Benchmark.__testByteCodec(
                csvLog, sparsity, IntegratedVariableByte(), data, repeat, False
            )
            Benchmark.__testByteCodec(
                csvLog, sparsity, IntegratedVariableByte(), data, repeat, False
            )
            Benchmark.__testByteCodec(
                csvLog, sparsity, IntegratedVariableByte(), data, repeat, True
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(BinaryPacking(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(BinaryPacking(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(BinaryPacking(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFD(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFD(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFD(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS9(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS9(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS9(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS16(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS16(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(NewPFDS16(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFD(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFD(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFD(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS9(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS9(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS9(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS16(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS16(), VariableByte()),
                data,
                repeat,
                False,
            )
            Benchmark.__testCodec(
                csvLog,
                sparsity,
                Composition(OptPFDS16(), VariableByte()),
                data,
                repeat,
                True,
            )
            print()

            Benchmark.__testCodec(csvLog, sparsity, Simple16(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, Simple16(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, Simple16(), data, repeat, True)
            print()

            Benchmark.__testCodec(csvLog, sparsity, Simple9(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, Simple9(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, Simple9(), data, repeat, True)
            print()

            Benchmark.__testCodec(csvLog, sparsity, GroupSimple9(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, GroupSimple9(), data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, GroupSimple9(), data, repeat, True)
            print()

            c = Composition(XorBinaryPacking(), VariableByte())
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, True)
            print()

            c = Composition(DeltaZigzagBinaryPacking(), DeltaZigzagVariableByte())
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, False)
            Benchmark.__testCodec(csvLog, sparsity, c, data, repeat, True)
            print()

    @staticmethod
    def __generateTestData(
        dataGen: ClusteredDataGenerator, N: int, nbr: int, sparsity: int
    ) -> typing.List[typing.List[int]]:
        data = []
        dataSize = 1 << (nbr + sparsity)
        for i in range(N):
            data.append(dataGen.generateClustered((1 << nbr), dataSize))
        return data

    @staticmethod
    def __testByteCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: ByteIntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        if verbose:
            print(f"# {c}")
            print("# bits per int, compress speed (mis), decompression speed (mis) ")

        N = len(data)

        totalSize = 0
        maxLength = 0
        for k in range(N):
            totalSize += len(data[k])
            if len(data[k]) > maxLength:
                maxLength = len(data[k])

        compressBuffer = bytearray(8 * maxLength + 1024)
        decompressBuffer = [0] * (maxLength + 1024)

        # These variables hold time in microseconds (10^-6).
        compressTime = 0
        decompressTime = 0

        size = 0
        inpos = IntWrapper.IntWrapper1()
        outpos = IntWrapper.IntWrapper1()

        for r in range(repeat):
            size = 0
            for k in range(N):
                backupdata = data[k][:]  # Copy of data[k]

                # Compress data
                beforeCompress = time.time_ns() // 1000
                inpos.set_(1)
                outpos.set_(0)
                if not isinstance(c, IntegratedByteIntegerCODEC):
                    Delta.delta0(backupdata)
                c.compress1(
                    backupdata,
                    inpos,
                    len(backupdata) - inpos.get(),
                    compressBuffer,
                    outpos,
                )
                afterCompress = time.time_ns() // 1000

                # Measure time of compression
                compressTime += afterCompress - beforeCompress
                thiscompsize = outpos.get() + 1
                size += thiscompsize

                # Extract (uncompress) data
                beforeDecompress = time.time_ns() // 1000
                inpos.set_(0)
                outpos.set_(1)
                decompressBuffer[0] = backupdata[0]
                c.uncompress1(
                    compressBuffer, inpos, thiscompsize - 1, decompressBuffer, outpos
                )
                if not isinstance(c, IntegratedByteIntegerCODEC):
                    Delta.fastinverseDelta0(decompressBuffer)
                afterDecompress = time.time_ns() // 1000

                # Measure time of extraction (uncompression)
                decompressTime += afterDecompress - beforeDecompress
                if outpos.get() != len(data[k]):
                    raise RuntimeError(
                        f"we have a bug (diff length) {c} expected {len(data[k])} got {outpos.get()}"
                    )

                # Verify: compare original array with compressed and uncompressed
                for m in range(outpos.get()):
                    if decompressBuffer[m] != data[k][m]:
                        raise RuntimeError(
                            f"we have a bug (actual difference), expected {data[k][m]} found {decompressBuffer[m]} at {m}"
                        )

        if verbose:
            bitsPerInt = size * 8.0 / totalSize
            compressSpeed = totalSize * repeat / compressTime
            decompressSpeed = totalSize * repeat / decompressTime
            print(f"\t{bitsPerInt:.2f}\t{int(compressSpeed)}\t{int(decompressSpeed)}")
            csvLog.write(
                f'"{c}",{sparsity},{bitsPerInt:.2f},{int(compressSpeed)},{int(decompressSpeed)}\n'
            )
            csvLog.flush()

    @staticmethod
    def __testCodec(
        csvLog: typing.Union[io.TextIOWrapper, io.StringIO],
        sparsity: int,
        c: IntegerCODEC,
        data: typing.List[typing.List[int]],
        repeat: int,
        verbose: bool,
    ) -> None:
        if verbose:
            print(f"# {c}")
            print("# bits per int, compress speed (mis), decompression speed (mis) ")

        N = len(data)

        totalSize = sum(len(data[k]) for k in range(N))
        maxLength = max(len(data[k]) for k in range(N))

        # 4x + 1024 to account for the possibility of some negative compression.
        compressBuffer = [0] * (4 * maxLength + 1024)
        decompressBuffer = [0] * (maxLength + 1024)

        # These variables hold time in microseconds (10^-6).
        compressTime = 0
        decompressTime = 0

        size = 0
        inpos = IntWrapper.IntWrapper1()
        outpos = IntWrapper.IntWrapper1()

        for r in range(repeat):
            size = 0
            for k in range(N):
                backupdata = data[k][:]  # Copy of data[k]

                # Compress data
                beforeCompress = time.time_ns() // 1000
                inpos.set_(1)
                outpos.set_(0)
                if not isinstance(c, IntegratedIntegerCODEC):
                    Delta.delta0(backupdata)
                c.compress0(
                    backupdata,
                    inpos,
                    len(backupdata) - inpos.get(),
                    compressBuffer,
                    outpos,
                )
                afterCompress = time.time_ns() // 1000

                # Measure time of compression
                compressTime += afterCompress - beforeCompress
                thiscompsize = outpos.get() + 1
                size += thiscompsize

                # Extract (uncompress) data
                beforeDecompress = time.time_ns() // 1000
                inpos.set_(0)
                outpos.set_(1)
                decompressBuffer[0] = backupdata[0]
                c.uncompress0(
                    compressBuffer, inpos, thiscompsize - 1, decompressBuffer, outpos
                )
                if not isinstance(c, IntegratedIntegerCODEC):
                    Delta.fastinverseDelta0(decompressBuffer)
                afterDecompress = time.time_ns() // 1000

                # Measure time of extraction (uncompression)
                decompressTime += afterDecompress - beforeDecompress
                if outpos.get() != len(data[k]):
                    raise RuntimeError(
                        f"we have a bug (diff length) {c} expected {len(data[k])} got {outpos.get()}"
                    )

                # Verify: compare original array with compressed and uncompressed
                for m in range(outpos.get()):
                    if decompressBuffer[m] != data[k][m]:
                        raise RuntimeError(
                            f"we have a bug (actual difference), expected {data[k][m]} found {decompressBuffer[m]} at {m} out of {outpos.get()}"
                        )

        if verbose:
            bitsPerInt = size * 32.0 / totalSize
            compressSpeed = totalSize * repeat / compressTime
            decompressSpeed = totalSize * repeat / decompressTime
            print(f"\t{bitsPerInt:.2f}\t{int(compressSpeed)}\t{int(decompressSpeed)}")
            csvLog.write(
                f'"{c}",{sparsity},{bitsPerInt:.2f},{int(compressSpeed)},{int(decompressSpeed)}\n'
            )
            csvLog.flush()
