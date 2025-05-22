from __future__ import annotations
import time
import re
import random
import sys
import enum
import threading
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32 import *


class PureJavaCrc32Test(unittest.TestCase):

    __ours: PureJavaCrc32 = PureJavaCrc32()
    __theirs: typing.Any = PureJavaCrc32()

    def testCorrectness_test7_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update1(104)
        self.__ours.update1(104)
        self.__checkSame()
        self.__checkOnBytes([40, 60, 97, -70], False)
        self.__checkOnBytes(list("hello world!".encode("utf-8")), False)

        random1 = Random()
        random2 = Random()
        for _ in range(10000):
            random_bytes = [0] * random1.randint(0, 2047)
            for i in range(len(random_bytes)):
                random_bytes[i] = random2.randint(-128, 127)
            self.__checkOnBytes(random_bytes, False)

    def testCorrectness_test6_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update1(104)
        self.__ours.update1(104)
        self.__checkSame()
        self.__checkOnBytes([40, 60, 97, -70], False)
        self.__checkOnBytes(list("hello world!".encode("utf-8")), False)

    def testCorrectness_test5_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update1(104)
        self.__ours.update1(104)
        self.__checkSame()
        self.__checkOnBytes([40, 60, 97, -70], False)
        "hello world!".encode("utf-8")

    def testCorrectness_test4_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update1(104)
        self.__ours.update1(104)
        self.__checkSame()
        self.__checkOnBytes([40, 60, 97, -70], False)

    def testCorrectness_test3_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update1(104)
        self.__ours.update1(104)
        self.__checkSame()

    def testCorrectness_test2_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update(104)
        self.__ours.update1(104)

    def testCorrectness_test1_decomposed(self) -> None:
        self.__checkSame()
        self.__theirs.update(104)

    def testCorrectness_test0_decomposed(self) -> None:
        self.__checkSame()

    def __checkSame(self) -> None:
        self.assertEqual(self.__theirs.getValue(), self.__ours.getValue())

    def __checkOnBytes(self, bytes_: typing.List[int], print_: bool) -> None:
        self.__theirs.reset()
        self.__ours.reset()
        self.__checkSame()

        for b in bytes_:
            self.__ours.update1(b)
            self.__theirs.update1(b)
            self.__checkSame()

        if print_:
            print(
                f"theirs:\t{hex(self.__theirs.getValue())}\n"
                f"ours:\t{hex(self.__ours.getValue())}"
            )

        self.__theirs.reset()
        self.__ours.reset()

        self.__ours.update0(bytes_, 0, len(bytes_))
        self.__theirs.update0(bytes_, 0, len(bytes_))
        if print_:
            print(
                f"theirs:\t{hex(self.__theirs.getValue())}\n"
                f"ours:\t{hex(self.__ours.getValue())}"
            )

        self.__checkSame()

        if len(bytes_) >= 10:
            self.__ours.update0(bytes_, 5, 5)
            self.__theirs.update0(bytes_, 5, 5)
            self.__checkSame()


class PerformanceTest:

    CRCS: typing.List[typing.Type[typing.Any]] = []

    zip: typing.Type[typing.Any] = None  # LLM could not translate this field

    BYTES_PER_SIZE: int = 32 * 1024 * 1024 * 4
    MAX_LEN: int = 32 * 1024 * 1024  # up to 32MB chunks

    @staticmethod
    def run_static_init():
        PerformanceTest.CRCS.append(PerformanceTest.zip)
        PerformanceTest.CRCS.append(PureJavaCrc32)

    @staticmethod
    def main(args: typing.List[str]) -> None:
        PerformanceTest.__printSystemProperties(sys.stdout)
        PerformanceTest.__doBench0(PerformanceTest.CRCS, sys.stdout)

    @staticmethod
    def __printSystemProperties(out: typing.IO) -> None:
        names = [
            "java.version",
            "java.runtime.name",
            "java.runtime.version",
            "java.vm.version",
            "java.vm.vendor",
            "java.vm.name",
            "java.vm.specification.version",
            "java.specification.version",
            "os.arch",
            "os.name",
            "os.version",
        ]
        properties = {
            "java.version": "N/A",
            "java.runtime.name": "N/A",
            "java.runtime.version": "N/A",
            "java.vm.version": "N/A",
            "java.vm.vendor": "N/A",
            "java.vm.name": "N/A",
            "java.vm.specification.version": "N/A",
            "java.specification.version": "N/A",
            "os.arch": os.uname().machine,
            "os.name": os.uname().sysname,
            "os.version": os.uname().release,
        }
        for name in names:
            out.write(f"{name} = {properties.get(name, 'N/A')}\n")

    @staticmethod
    def __doBench2(
        clazz: typing.Type[typing.Any],
        numThreads: int,
        bytes_: typing.List[int],
        size: int,
    ) -> BenchResult:
        threads = [None] * numThreads
        results = [None] * numThreads

        trials = PerformanceTest.BYTES_PER_SIZE // size
        mbProcessed = trials * size / 1024.0 / 1024.0

        ctor = (
            clazz.__init__
        )  # Assuming clazz is a Python class with a default constructor

        def thread_function(index: int):
            crc = clazz()  # Create an instance of the Checksum class
            start_time = time.time_ns()
            crc.reset()
            for _ in range(trials):
                crc.update(bytes_, 0, size)
            end_time = time.time_ns()
            seconds_elapsed = (end_time - start_time) / 1_000_000_000.0
            results[index] = BenchResult(crc.getValue(), mbProcessed / seconds_elapsed)

        # Create threads
        for i in range(numThreads):
            threads[i] = threading.Thread(target=thread_function, args=(i,))

        # Start threads
        for thread in threads:
            thread.start()

        # Join threads
        for thread in threads:
            thread.join()

        # Validate results
        expected = results[0].value
        total_mbps = results[0].mbps
        for i in range(1, len(results)):
            if results[i].value != expected:
                raise AssertionError(f"{clazz.__name__} results not matched.")
            total_mbps += results[i].mbps

        return BenchResult(expected, total_mbps / len(results))

    @staticmethod
    def __doBench1(
        crcs: typing.List[typing.Type[Checksum]],
        bytes_: typing.List[int],
        size: int,
        out: typing.IO,
    ) -> None:
        numBytesStr = " #Bytes "
        numThreadsStr = "#T"
        diffStr = "% diff"

        out.write("|")
        PerformanceTest.__printCell(numBytesStr, 0, out)
        PerformanceTest.__printCell(numThreadsStr, 0, out)
        for i, c in enumerate(crcs):
            out.write("|")
            PerformanceTest.__printCell(c.__name__, 8, out)
            for j in range(i):
                PerformanceTest.__printCell(diffStr, len(diffStr), out)
        out.write("\n")

        numThreads = 1
        while numThreads <= 16:
            out.write("|")
            PerformanceTest.__printCell(str(size), len(numBytesStr), out)
            PerformanceTest.__printCell(str(numThreads), len(numThreadsStr), out)

            expected = None
            previous = []
            for c in crcs:
                os.system("gc")  # Simulating System.gc() in Python

                result = PerformanceTest.__doBench2(c, numThreads, bytes_, size)
                PerformanceTest.__printCell(
                    f"{result.mbps:9.1f}", len(c.__name__) + 1, out
                )

                if c == PerformanceTest.zip:
                    expected = result
                elif expected is None:
                    raise RuntimeError(
                        f"The first class is {c.__name__} but not {PerformanceTest.zip.__name__}"
                    )
                elif result.value != expected.value:
                    raise RuntimeError(f"{c} has bugs!")

                for p in previous:
                    diff = (result.mbps - p.mbps) / p.mbps * 100
                    PerformanceTest.__printCell(f"{diff:5.1f}%", len(diffStr), out)
                previous.append(result)

            out.write("\n")
            numThreads <<= 1

    @staticmethod
    def __doBench0(crcs: typing.List[typing.Type[typing.Any]], out: typing.IO) -> None:
        bytes_ = bytearray(PerformanceTest.MAX_LEN)
        random = os.urandom(len(bytes_))
        bytes_[:] = random

        out.write("\nPerformance Table (The unit is MB/sec; #T = #Threads)\n")

        for c in crcs:
            PerformanceTest.__doBench2(c, 1, bytes_, 2)
            PerformanceTest.__doBench2(c, 1, bytes_, 2101)

        size = 32
        while size <= PerformanceTest.MAX_LEN:
            PerformanceTest.__doBench1(crcs, bytes_, size, out)
            size <<= 1

    @staticmethod
    def __printCell(s: str, width: int, out: typing.IO) -> None:
        w = len(s) if len(s) > width else width
        out.write(f" {s:>{w}} |")


class Table:

    __tables: typing.List[typing.List[int]] = None

    def toString(self) -> str:
        b = []

        table_format = f"T{(self.__tables[0].__len__() - 1).bit_length()}_%d"
        start_format = f"  private static final int {table_format}_start = %d*256;"

        for j in range(len(self.__tables)):
            b.append(start_format % (j, j))
            b.append("\n")

        b.append("  private static final int[] T = new int[] {")
        for s in self.toStrings(table_format):
            b.append("\n")
            b.append(s)
        b[-1] = "\n"  # Replace the last character with a newline
        b.append(" };\n")
        return "".join(b)

    @staticmethod
    def main(args: typing.List[str]) -> None:
        if len(args) != 1:
            print(f"Usage: {Table.__name__} <polynomial>", file=sys.stderr)
            sys.exit(1)

        polynomial = int(args[0], 16)

        i = 8
        t = Table(i, 16, polynomial)
        s = t.toString()
        print(s)

        with open(f"table{i}.txt", "w") as out:
            out.write(s)

    def __init__(self, nBits: int, nTables: int, polynomial: int) -> None:
        self.__tables = []
        size = 1 << nBits
        for _ in range(nTables):
            self.__tables.append([0] * size)

        first = self.__tables[0]
        for i in range(len(first)):
            crc = i
            for _ in range(nBits):
                if (crc & 1) == 1:
                    crc >>= 1
                    crc ^= polynomial
                else:
                    crc >>= 1
            first[i] = crc

        mask = len(first) - 1
        for j in range(1, len(self.__tables)):
            previous = self.__tables[j - 1]
            current = self.__tables[j]
            for i in range(len(current)):
                current[i] = (previous[i] >> nBits) ^ first[previous[i] & mask]

    def toStrings(self, nameformat: str) -> typing.List[str]:
        s = [None] * len(self.__tables)
        for j, t in enumerate(self.__tables):
            b = []
            b.append(f"    /* {nameformat} */".format(j))
            i = 0
            while i < len(t):
                b.append("\n    ")
                for k in range(4):
                    if i < len(t):
                        b.append(f"0x{t[i]:08X}, ")
                        i += 1
            s[j] = "".join(b)
        return s


class BenchResult:

    mbps: float = 0.0

    value: int = 0

    def __init__(self, value: int, mbps: float) -> None:
        self.value = value
        self.mbps = mbps


PerformanceTest.run_static_init()
