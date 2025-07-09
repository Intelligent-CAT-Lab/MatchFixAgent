from __future__ import annotations
import time
import re
import unittest
import pytest
import pathlib
from io import IOBase
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *

# from src.main.org.apache.commons.io.IOUtils import *


class PerformanceTest(unittest.TestCase):

    __max: int = 10
    __BIG_FILE: pathlib.Path = (
        pathlib.Path(os.getenv("TMPDIR", "/tmp")) / "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"

    def testReadBigFile_test2_decomposed(self) -> None:
        best_time = float("inf")
        count = 0
        for i in range(self.__max):
            start_millis = 0
            with self.__createBufferedReader() as in_:
                start_millis = int(
                    round(time.time() * 1000)
                )  # Current time in milliseconds
                count = self.__readAll(in_)
            total_millis = int(round(time.time() * 1000)) - start_millis
            best_time = min(total_millis, best_time)
            self.__println(
                f"File read in {total_millis:,} milliseconds: {count:,} lines."
            )
        self.__println(
            f"Best time out of {self.__max:,} is {best_time:,} milliseconds."
        )

    def testReadBigFile_test1_decomposed(self) -> None:
        best_time = float("inf")
        count = 0
        for _ in range(self.__max):
            start_millis = 0
            with self.__createBufferedReader() as in_:
                start_millis = int(
                    round(time.time() * 1000)
                )  # Current time in milliseconds
                count = self.__readAll(in_)
            total_millis = int(round(time.time() * 1000)) - start_millis
            best_time = min(total_millis, best_time)
            self.__println(
                f"File read in {total_millis:,} milliseconds: {count:,} lines."
            )
        self.__println(
            f"Best time out of {self.__max:,} is {best_time:,} milliseconds."
        )

    def testReadBigFile_test0_decomposed(self) -> None:
        best_time = float("inf")
        count = 0
        for _ in range(self.__max):
            start_millis = 0
            with self.__createBufferedReader() as in_:
                start_millis = int(
                    round(time.time() * 1000)
                )  # Current time in milliseconds
                count = self.__readAll(in_)
            total_millis = int(round(time.time() * 1000)) - start_millis
            best_time = min(total_millis, best_time)
            self.__println(
                f"File read in {total_millis:,} milliseconds: {count:,} lines."
            )

    def testParseBigFileRepeat_test2_decomposed(self) -> None:
        best_time = float("inf")  # Equivalent to 9223372036854775807 in Java
        for _ in range(self.__max):
            best_time = min(self.testParseBigFile(False), best_time)
        formatted_message = (
            f"Best time out of {self.__max:,} is {best_time:,} milliseconds."
        )
        self.__println(formatted_message)

    def testParseBigFileRepeat_test1_decomposed(self) -> None:
        best_time = float("inf")  # Equivalent to 9223372036854775807 in Java
        for _ in range(self.__max):
            best_time = min(self.testParseBigFile(False), best_time)
        print(f"Best time out of {self.__max:,} is {best_time:,} milliseconds.")

    def testParseBigFileRepeat_test0_decomposed(self) -> None:
        best_time = float("inf")  # Equivalent to 9223372036854775807 in Java
        for _ in range(self.__max):
            best_time = min(self.testParseBigFile(False), best_time)

    def testParseBigFile(self, traverseColumns: bool) -> int:
        start_millis = int(
            round(time.time() * 1000)
        )  # Get current time in milliseconds
        with self.__createBufferedReader() as reader:
            count = self.__parse(reader, traverseColumns)
            total_millis = int(round(time.time() * 1000)) - start_millis
            self.__println(
                f"File parsed in {total_millis:,} milliseconds with Commons CSV: {count:,} lines."
            )
            return total_millis

    def __readAll(self, in_: io.BufferedReader) -> int:
        count = 0
        while in_.readline() != "":
            count += 1
        return count

    def __println(self, s: str) -> None:
        print(s)

    def __parse(
        self,
        reader: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        traverseColumns: bool,
    ) -> int:
        format = CSVFormat.DEFAULT.builder().setIgnoreSurroundingSpaces(False).build()
        record_count = 0
        with format.parse(reader) as parser:
            for record in parser:
                record_count += 1
                if traverseColumns:
                    for value in record:
                        pass  # Do nothing, just traverse the columns
        return record_count

    def __createBufferedReader(self) -> io.BufferedReader:
        return open(self.__BIG_FILE, mode="r", buffering=io.DEFAULT_BUFFER_SIZE)
