from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import typing
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class CSVFileParserTest:

    __BASE_DIR: pathlib.Path = pathlib.Path(
        "src/test/resources/org/apache/commons/csv/CSVFileParser"
    )

    @pytest.mark.skip(reason="Ignore")
    def testCSVUrl(self, testFile: pathlib.Path) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.skip(reason="Ignore")
    def testCSVFile(self, testFile: pathlib.Path) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def generateData() -> typing.Iterable[pathlib.Path]:
        files = list(CSVFileParserTest.__BASE_DIR.glob("test*.txt"))
        return files if files else []

    def __readTestData(self, reader: io.BufferedReader) -> str:
        line = None
        while True:
            line = reader.readline()
            if line is None or not line.startswith("#"):
                break
        return line
