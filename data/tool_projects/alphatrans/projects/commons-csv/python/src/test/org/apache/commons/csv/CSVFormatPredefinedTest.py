from __future__ import annotations
import re
import unittest
import pytest
import io
import enum
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *


class CSVFormatPredefinedTest(unittest.TestCase):

    def testTDF_test0_decomposed(self) -> None:
        self.__test(CSVFormat.TDF, "TDF")

    def testRFC4180_test0_decomposed(self) -> None:
        self.__test(CSVFormat.RFC4180, "RFC4180")

    def testPostgreSqlText_test0_decomposed(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_TEXT, "PostgreSQLText")

    def testPostgreSqlCsv_test0_decomposed(self) -> None:
        self.__test(CSVFormat.POSTGRESQL_CSV, "PostgreSQLCsv")

    def testOracle_test0_decomposed(self) -> None:
        self.__test(CSVFormat.ORACLE, "Oracle")

    def testMySQL_test0_decomposed(self) -> None:
        self.__test(CSVFormat.MYSQL, "MySQL")

    def testMongoDbTsv_test0_decomposed(self) -> None:
        self.__test(CSVFormat.MONGODB_TSV, "MongoDBTsv")

    def testMongoDbCsv_test0_decomposed(self) -> None:
        self.__test(CSVFormat.MONGODB_CSV, "MongoDBCsv")

    def testExcel_test0_decomposed(self) -> None:
        self.__test(CSVFormat.EXCEL, "Excel")

    def testDefault_test0_decomposed(self) -> None:
        self.__test(CSVFormat.DEFAULT, "Default")

    def __test(self, format_: CSVFormat, enumName: str) -> None:
        self.assertEqual(format_, Predefined.__dict__[enumName].getFormat())
        self.assertEqual(format_, CSVFormat.valueOf(enumName))
