from __future__ import annotations
import re
import decimal
import io
import typing
from typing import *
import os
from src.main.me.lemire.integercompression.BitPacking import *
from src.main.me.lemire.integercompression.differential.Delta import *
from src.main.me.lemire.integercompression.differential.IntegratedBitPacking import *


class BenchmarkBitPacking:

    @staticmethod
    def main(args: typing.List[typing.List[str]]) -> None:
        print("Testing packing and delta")
        BenchmarkBitPacking.__testWithDeltas(False)
        BenchmarkBitPacking.__testWithDeltas(True)
        print("Testing packing alone")
        BenchmarkBitPacking.__test(False)
        BenchmarkBitPacking.__test(True)

    @staticmethod
    def __testWithDeltas(verbose: bool) -> None:
        from decimal import Decimal
        import random
        import time

        dfspeed = lambda x: f"{x:.0f}"  # DecimalFormat equivalent
        N = 32
        times = 100000
        r = random.Random(0)
        data = [0] * N
        compressed = [0] * N
        icompressed = [0] * N
        uncompressed = [0] * N

        for bit in range(1, 31):
            comp = 0
            decomp = 0
            icomp = 0
            idecomp = 0

            for t in range(times):
                data[0] = r.randint(0, (1 << bit) - 1)
                for k in range(1, N):
                    data[k] = r.randint(0, (1 << bit) - 1) + data[k - 1]

                tmpdata = data[:]
                time1 = time.time_ns()
                Delta.delta0(tmpdata)
                BitPacking.fastpackwithoutmask(tmpdata, 0, compressed, 0, bit)
                time2 = time.time_ns()
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit)
                Delta.fastinverseDelta0(uncompressed)
                time3 = time.time_ns()

                if data != uncompressed:
                    raise RuntimeError("bug")

                comp += time2 - time1
                decomp += time3 - time2

                tmpdata = data[:]
                time1 = time.time_ns()
                IntegratedBitPacking.integratedpack(0, tmpdata, 0, icompressed, 0, bit)
                time2 = time.time_ns()
                IntegratedBitPacking.integratedunpack(
                    0, icompressed, 0, uncompressed, 0, bit
                )
                time3 = time.time_ns()

                if icompressed != compressed:
                    raise RuntimeError(f"ibug {bit}")
                if data != uncompressed:
                    raise RuntimeError(f"bug {bit}")

                icomp += time2 - time1
                idecomp += time3 - time2

            if verbose:
                print(
                    f"bit = {bit} "
                    f"comp. speed = {dfspeed(N * times * 1000.0 / comp)} "
                    f"decomp. speed = {dfspeed(N * times * 1000.0 / decomp)} "
                    f"icomp. speed = {dfspeed(N * times * 1000.0 / icomp)} "
                    f"idecomp. speed = {dfspeed(N * times * 1000.0 / idecomp)}"
                )

    @staticmethod
    def __test(verbose: bool) -> None:
        from decimal import Decimal
        import random
        import time

        dfspeed = lambda x: f"{x:.0f}"  # Equivalent to DecimalFormat("0")
        N = 32
        times = 100000
        r = random.Random(0)
        data = [0] * N
        compressed = [0] * N
        uncompressed = [0] * N

        for bit in range(31):
            comp = 0
            compwm = 0
            decomp = 0

            for t in range(times):
                for k in range(N):
                    data[k] = r.randint(0, (1 << bit) - 1)

                time1 = time.perf_counter_ns()
                BitPacking.fastpack(data, 0, compressed, 0, bit)
                time2 = time.perf_counter_ns()
                BitPacking.fastpackwithoutmask(data, 0, compressed, 0, bit)
                time3 = time.perf_counter_ns()
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit)
                time4 = time.perf_counter_ns()

                comp += time2 - time1
                compwm += time3 - time2
                decomp += time4 - time3

            if verbose:
                print(
                    f"bit = {bit} comp. speed = {dfspeed(N * times * 1000.0 / comp)} "
                    f"comp. speed wm = {dfspeed(N * times * 1000.0 / compwm)} "
                    f"decomp. speed = {dfspeed(N * times * 1000.0 / decomp)}"
                )
