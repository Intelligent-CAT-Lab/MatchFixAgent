from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv253Test(unittest.TestCase):

    def testHandleAbsentValues_test3_decomposed(self) -> None:
        source = '"John",,"Doe"\n' + ',"AA",123\n' + '"John",90,\n' + '"",,90'
        csv_format_builder = CSVFormat.DEFAULT.builder()
        csv_format_builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        csv_format = csv_format_builder.build()

        with io.StringIO(source) as reader:
            parser = csv_format.parse(reader)
            csv_records = parser.iterator()

            self.__assertArrayEqual(["John", None, "Doe"], next(csv_records))
            self.__assertArrayEqual([None, "AA", "123"], next(csv_records))
            self.__assertArrayEqual(["John", "90", None], next(csv_records))
            self.__assertArrayEqual(["", None, "90"], next(csv_records))

    def testHandleAbsentValues_test2_decomposed(self) -> None:
        source = '"John",,"Doe"\n' + ',"AA",123\n' + '"John",90,\n' + '"",,90'
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        csv_format = builder.setQuoteMode(QuoteMode.NON_NUMERIC).build()

    def testHandleAbsentValues_test1_decomposed(self) -> None:
        source = '"John",,"Doe"\n' + ',"AA",123\n' + '"John",90,\n' + '"",,90'
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)

    def testHandleAbsentValues_test0_decomposed(self) -> None:
        source = '"John",,"Doe"\n' + ',"AA",123\n' + '"John",90,\n' + '"",,90'
        CSVFormat.DEFAULT.builder()

    def __assertArrayEqual(self, expected: List[str], actual: CSVRecord) -> None:
        for i in range(len(expected)):
            self.assertEqual(expected[i], actual.get1(i))
