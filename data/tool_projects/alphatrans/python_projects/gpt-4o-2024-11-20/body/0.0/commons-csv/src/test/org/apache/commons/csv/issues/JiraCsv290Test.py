from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv290Test(unittest.TestCase):

    def testPostgresqlText_test0_decomposed(self) -> None:
        self.__testHelper("psql.tsv", CSVFormat.POSTGRESQL_TEXT)

    def testPostgresqlCsv_test0_decomposed(self) -> None:
        self.__testHelper("psql.csv", CSVFormat.POSTGRESQL_CSV)

    def __testHelper(self, filename: str, format_: CSVFormat) -> None:
        content = []
        with CSVParser.parse3(
            io.TextIOWrapper(
                self.__class__.__module__.get_resource_as_stream(
                    f"/org/apache/commons/csv/CSV-290/{filename}"
                )
            ),
            format_,
        ) as csv_parser:
            content = list(map(lambda record: record.to_list(), csv_parser.stream()))

        self.assertEqual(3, len(content))

        self.assertEqual("1", content[0][0])
        self.assertEqual("abc", content[0][1])
        self.assertEqual("test line 1\ntest line 2", content[0][2])  # new line
        self.assertIsNone(content[0][3])  # null
        self.assertEqual("", content[0][4])

        self.assertEqual("2", content[1][0])
        self.assertEqual("\\b:\b \\t:\t \\n:\n \\r:\r", content[1][2])  # \b, \t, \n, \r

        self.assertEqual("3", content[2][0])
        self.assertEqual("b,c,d", content[2][2])  # value has comma
        self.assertEqual('"quoted"', content[2][3])  # quoted
