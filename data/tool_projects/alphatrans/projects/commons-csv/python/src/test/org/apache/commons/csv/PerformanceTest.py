from __future__ import annotations
import time
import re
import tempfile
import sys
import os
import unittest
import pytest
from abc import ABC
import pathlib
from io import IOBase
import io
import typing
from typing import *
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *

# from src.main.org.apache.commons.io.IOUtils import *


class PerformanceTest:

    __BIG_FILE: pathlib.Path = (
        pathlib.Path(tempfile.gettempdir()) / "worldcitiespop.txt"
    )
    __TEST_RESRC: str = "org/apache/commons/csv/perf/worldcitiespop.txt.gz"
    __format: CSVFormat = CSVFormat.EXCEL
    __ELAPSED_TIMES: typing.List[int] = [0] * 11
    __num: int = 0

    __max: int = 11
    __PROPERTY_NAMES: List[str] = [
        "java.version",  # Java Runtime Environment version
        "java.vendor",  # Java Runtime Environment vendor
        "java.vm.version",  # Java Virtual Machine implementation version
        "java.vm.name",  # Java Virtual Machine implementation name
        "os.name",  # Operating system name
        "os.arch",  # Operating system architecture
        "os.version",  # Operating system version
    ]

    @staticmethod
    def main(args: typing.List[str]) -> None:
        if PerformanceTest.__BIG_FILE.exists():
            print(
                f"Found test fixture {PerformanceTest.__BIG_FILE}: {PerformanceTest.__BIG_FILE.stat().st_size:,} bytes."
            )
        else:
            print(f"Decompressing test fixture to: {PerformanceTest.__BIG_FILE}...")
            with gzip.open(PerformanceTest.__TEST_RESRC, "rb") as input_file, open(
                PerformanceTest.__BIG_FILE, "wb"
            ) as output_file:
                output_file.write(input_file.read())
                print(
                    f"Decompressed test fixture {PerformanceTest.__BIG_FILE}: {PerformanceTest.__BIG_FILE.stat().st_size:,} bytes."
                )

        argc = len(args)
        if argc > 0:
            PerformanceTest.__max = int(args[0])

        if argc > 1:
            tests = args[1:]
        else:
            tests = [
                "file",
                "split",
                "extb",
                "exts",
                "csv",
                "csv-path",
                "csv-path-db",
                "csv-url",
                "lexreset",
                "lexnew",
            ]

        for p in PerformanceTest.__PROPERTY_NAMES:
            print(f"{p}={getattr(platform, p.replace('.', '_'), 'Unknown')}")

        print(f"Max count: {PerformanceTest.__max}\n")

        for test in tests:
            if test == "file":
                PerformanceTest.__testReadBigFile(False)
            elif test == "split":
                PerformanceTest.__testReadBigFile(True)
            elif test == "csv":
                PerformanceTest.__testParseCommonsCSV()
            elif test == "csv-path":
                PerformanceTest.__testParsePath()
            elif test == "csv-path-db":
                PerformanceTest.__testParsePathDoubleBuffering()
            elif test == "csv-url":
                PerformanceTest.__testParseURL()
            elif test == "lexreset":
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "lexnew":
                PerformanceTest.__testCSVLexer(True, test)
            elif test.startswith("CSVLexer"):
                PerformanceTest.__testCSVLexer(False, test)
            elif test == "extb":
                PerformanceTest.__testExtendedBuffer(False)
            elif test == "exts":
                PerformanceTest.__testExtendedBuffer(True)
            else:
                print(f"Invalid test name: {test}")

    @staticmethod
    def __testReadBigFile(split: bool) -> None:
        for i in range(PerformanceTest.__max):
            start_millis: int
            stats: Stats
            with PerformanceTest.__createReader() as in_:
                start_millis = int(
                    time.time() * 1000
                )  # Equivalent to System.currentTimeMillis()
                stats = PerformanceTest.__readAll(in_, split)
            PerformanceTest.__show1(
                "file+split" if split else "file", stats, start_millis
            )
        PerformanceTest.__show0()

    @staticmethod
    def __testParseURL() -> None:
        PerformanceTest.__testParser(
            "CSV-URL",
            lambda: CSVParser.parse5(
                PerformanceTest.__BIG_FILE.as_uri(),
                "ISO-8859-1",
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParser(msg: str, fac: CSVParserFactory) -> None:
        for i in range(PerformanceTest.__max):
            start_millis: int
            stats: Stats
            with fac.createParser() as parser:
                start_millis = int(
                    time.time() * 1000
                )  # Equivalent to System.currentTimeMillis()
                stats = PerformanceTest.__iterate(parser)
            PerformanceTest.__show1(msg, stats, start_millis)
        PerformanceTest.__show0()

    @staticmethod
    def __testParsePathDoubleBuffering() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH-DB",
            lambda: CSVParser.parse3(
                PerformanceTest.__BIG_FILE.open("r", encoding="iso-8859-1"),
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParsePath() -> None:
        PerformanceTest.__testParser(
            "CSV-PATH",
            lambda: CSVParser.parse1(
                PerformanceTest.__BIG_FILE.open("rb"),
                "ISO-8859-1",
                PerformanceTest.__format,
            ),
        )

    @staticmethod
    def __testParseCommonsCSV() -> None:
        PerformanceTest.__testParser(
            "CSV",
            lambda: CSVParser.CSVParser1(createReader(), PerformanceTest.__format),
        )

    @staticmethod
    def __testExtendedBuffer(makeString: bool) -> None:
        for i in range(PerformanceTest.__max):
            fields = 0
            lines = 0
            startMillis = 0
            try:
                with ExtendedBufferedReader(PerformanceTest.__createReader()) as reader:
                    startMillis = int(time.time() * 1000)
                    if makeString:
                        sb = []
                        while True:
                            read = reader.read0()
                            if read == -1:
                                break
                            sb.append(chr(read))
                            if read == ord(","):
                                "".join(sb)
                                sb = []
                                fields += 1
                            elif read == ord("\n"):
                                "".join(sb)
                                sb = []
                                lines += 1
                    else:
                        while True:
                            read = reader.read0()
                            if read == -1:
                                break
                            if read == ord(","):
                                fields += 1
                            elif read == ord("\n"):
                                lines += 1
                    fields += lines
            except Exception as e:
                raise e
            PerformanceTest.__show1(
                f"Extended{' toString' if makeString else ''}",
                Stats(lines, fields),
                startMillis,
            )
        PerformanceTest.__show0()

    @staticmethod
    def __testCSVLexer(newToken: bool, test: str) -> None:
        token = Token()
        dynamic = ""
        for _ in range(PerformanceTest.__max):
            try:
                with PerformanceTest.__createReader() as input_, PerformanceTest.__createTestCSVLexer(
                    test, ExtendedBufferedReader(input_)
                ) as lexer:

                    if test.startswith("CSVLexer"):
                        dynamic = "!"

                    simpleName = lexer.__class__.__name__
                    count = 0
                    fields = 0
                    startMillis = int(
                        time.time() * 1000
                    )  # Current time in milliseconds

                    while True:
                        if newToken:
                            token = Token()
                        else:
                            token.reset()

                        lexer.nextToken(token)

                        if token.type == Token.Type.EOF:
                            break
                        elif token.type == Token.Type.EORECORD:
                            fields += 1
                            count += 1
                        elif token.type == Token.Type.INVALID:
                            raise IOError(
                                f"invalid parse sequence <{token.content.getvalue()}>"
                            )
                        elif token.type == Token.Type.TOKEN:
                            fields += 1
                        elif token.type == Token.Type.COMMENT:
                            pass  # Not really expecting these
                        else:
                            raise RuntimeError(f"Unexpected Token type: {token.type}")

                    stats = Stats(count, fields)

                PerformanceTest.__show1(
                    f"{simpleName}{dynamic} {'new' if newToken else 'reset'}",
                    stats,
                    startMillis,
                )

            except Exception as e:
                raise e

        PerformanceTest.__show0()

    @staticmethod
    def __show1(msg: str, s: Stats, start: int) -> None:
        elapsed = int(round(time.time() * 1000)) - start
        print(f"{msg:<20}: {elapsed:5d}ms {s.count} lines {s.fields} fields")
        PerformanceTest.__ELAPSED_TIMES[PerformanceTest.__num] = elapsed
        PerformanceTest.__num += 1

    @staticmethod
    def __show0() -> None:
        if PerformanceTest.__num > 1:
            tot = 0
            for i in range(1, PerformanceTest.__num):  # skip first test
                tot += PerformanceTest.__ELAPSED_TIMES[i]
            print(
                f"{'Average(not first)':<20}: {tot // (PerformanceTest.__num - 1):5}ms\n"
            )
        PerformanceTest.__num = 0  # ready for next set

    @staticmethod
    def __readAll(in_: io.BufferedReader, split: bool) -> Stats:
        count = 0
        fields = 0
        while (record := in_.readline().strip()) != "":
            count += 1
            fields += len(record.split(",")) if split else 1
        return Stats(count, fields)

    @staticmethod
    def __iterate(iterable: typing.Iterable[CSVRecord]) -> Stats:
        count = 0
        fields = 0
        for record in iterable:
            count += 1
            fields += record.size()
        return Stats(count, fields)

    @staticmethod
    def __getLexerCtor(clazz: str) -> typing.Callable[..., Lexer]:
        lexer_class = getattr(
            __import__("src.main.org.apache.commons.csv", fromlist=[clazz]), clazz
        )
        return lexer_class.__init__

    @staticmethod
    def __createTestCSVLexer(test: str, input_: ExtendedBufferedReader) -> Lexer:
        if test.startswith("CSVLexer"):
            return PerformanceTest.__getLexerCtor(test)(
                PerformanceTest.__format, input_
            )
        else:
            return Lexer(PerformanceTest.__format, input_)

    @staticmethod
    def __createReader() -> (
        typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase]
    ):
        return io.TextIOWrapper(
            open(PerformanceTest.__BIG_FILE, mode="rb"), encoding="ISO-8859-1"
        )


class Stats:

    fields: int = 0

    count: int = 0

    def __init__(self, c: int, f: int) -> None:
        self.count = c
        self.fields = f


class CSVParserFactory(ABC):

    def createParser(self) -> CSVParser:
        raise NotImplementedError("This method should be implemented by subclasses")
