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


class JiraCsv93Test(unittest.TestCase):

    __objects2: typing.List[typing.Any] = ["abc", "NULL", None, "a,b,c", 123]
    __objects1: typing.List[typing.Any] = ["abc", "", None, "a,b,c", 123]

    def testWithSetNullStringNULL_test29_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setEscape0("?")
        builder.setNullString("NULL").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 6
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c",123',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test28_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setEscape0("?")
        builder.setNullString("NULL").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 6
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC).build()
        )

    def testWithSetNullStringNULL_test27_decomposed(self) -> None:
        # Test case 1
        csv_format = CSVFormat.DEFAULT.builder().setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test26_decomposed(self) -> None:
        # Test case 1
        csv_format = CSVFormat.DEFAULT.builder().setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test25_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test24_decomposed(self) -> None:
        # Test case 1
        csv_format = CSVFormat.DEFAULT.builder().setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            "abc,NULL,NULL,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test23_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setEscape0("?")
        builder.setNullString("NULL").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("NULL")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )

    def testWithSetNullStringNULL_test22_decomposed(self) -> None:
        # Create a builder and set null string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Set null string and quote mode ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Set null string and quote mode ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Set null string and quote mode MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Set null string and escape character
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setEscape0("?").setQuoteMode(QuoteMode.NONE)

    def testWithSetNullStringNULL_test21_decomposed(self) -> None:
        # Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test with default quote mode
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test with QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test setting escape character
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setEscape0("?")

    def testWithSetNullStringNULL_test20_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test19_decomposed(self) -> None:
        # Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test with default null string
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test with QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test18_decomposed(self) -> None:
        # Test case 1: Default CSVFormat with null string set to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2: CSVFormat with null string "NULL" and QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3: CSVFormat with null string "NULL" and QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Test case 4: CSVFormat with null string "NULL" and QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test17_decomposed(self) -> None:
        # Create a builder and set the null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test with the first configuration
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set the null string and quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test with the second configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set the null string and quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

        # Test with the third configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Create a builder and set the null string and quote mode to MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build()
        )

    def testWithSetNullStringNULL_test16_decomposed(self) -> None:
        # Step 1: Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Step 2: Test with the first configuration
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 3: Set QuoteMode to ALL and test
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 4: Set QuoteMode to ALL_NON_NULL and test
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Step 5: Set QuoteMode to MINIMAL (no test performed here)
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL)

    def testWithSetNullStringNULL_test15_decomposed(self) -> None:
        # Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test with the first configuration
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set null string to "NULL", and set quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test with the second configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set null string to "NULL", and set quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

        # Test with the third configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

        # Create a builder and set null string to "NULL" again
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")

    def testWithSetNullStringNULL_test14_decomposed(self) -> None:
        # Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test with the first configuration
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set null string to "NULL" with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test with the second configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set null string to "NULL" with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

        # Test with the third configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test13_decomposed(self) -> None:
        # Step 1: Create a builder and set null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Step 2: Test with the first configuration
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 3: Create a builder, set null string to "NULL", and set quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Step 4: Test with the second configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 5: Create a builder, set null string to "NULL", and set quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

        # Step 6: Test with the third configuration
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL",NULL,"a,b,c","123"',
            ["abc", "NULL", None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test12_decomposed(self) -> None:
        # Create a builder and set the null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set the null string to "NULL", and set the quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test the second case
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set the null string to "NULL", and set the quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build()

    def testWithSetNullStringNULL_test11_decomposed(self) -> None:
        # Create a builder and set the null string to "NULL"
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set the null string to "NULL", and set the quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test the second case
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set the null string to "NULL" with quote mode ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL)

    def testWithSetNullStringNULL_test10_decomposed(self) -> None:
        # Create a builder instance
        builder = CSVFormat.DEFAULT.builder()

        # Set null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with null string set
        csv_format = builder.setNullString("NULL").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Set quote mode to ALL and build the CSVFormat
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        csv_format_with_quotes = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        )

        # Test the second case
        self.__every(
            csv_format_with_quotes,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test9_decomposed(self) -> None:
        # Create a builder instance
        builder = CSVFormat.DEFAULT.builder()

        # Set null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with null string set
        csv_format_with_null = builder.setNullString("NULL").build()

        # Test the first case
        self.__every(
            csv_format_with_null,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Set null string and quote mode
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)

        # Build the CSVFormat with null string and quote mode set
        csv_format_with_null_and_quote = (
            builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()
        )

        # Test the second case
        self.__every(
            csv_format_with_null_and_quote,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test8_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("NULL").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create another builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL" and the quote mode to ALL
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)

        # Build the CSVFormat with the null string and quote mode set
        csv_format = builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

        # Test the second case
        self.__every(
            csv_format,
            self.__objects2,
            '"abc","NULL","NULL","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test7_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("NULL").build()

        # Call the __every method with the appropriate parameters
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Additional builder configurations
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL).build()

    def testWithSetNullStringNULL_test6_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("NULL").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Additional builder calls
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").setQuoteMode(QuoteMode.ALL)

    def testWithSetNullStringNULL_test5_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("NULL").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Additional builder calls (not strictly necessary for the test logic)
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")

    def testWithSetNullStringNULL_test4_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to "NULL"
        builder.setNullString("NULL")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("NULL").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create another builder from the default CSVFormat (no further action needed)
        CSVFormat.DEFAULT.builder()

    def testWithSetNullStringNULL_test3_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        csv_format = builder.setNullString("NULL").build()
        self.__every(
            csv_format,
            self.__objects2,
            'abc,NULL,NULL,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringNULL_test2_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")
        builder.setNullString("NULL").build()

    def testWithSetNullStringNULL_test1_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("NULL")

    def testWithSetNullStringNULL_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()

    def testWithSetNullStringEmptyString_test29_decomposed(self) -> None:
        # Test case 1
        csv_format = CSVFormat.DEFAULT.builder().setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 6
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c",123',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test28_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setEscape0("?")
        builder.setNullString("").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 6
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC).build()
        )

    def testWithSetNullStringEmptyString_test27_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setEscape0("?")
        builder.setNullString("").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC)

    def testWithSetNullStringEmptyString_test26_decomposed(self) -> None:
        # Builder with default settings
        CSVFormat.DEFAULT.builder()

        # Builder with null string set to an empty string
        CSVFormat.DEFAULT.builder().setNullString("")

        # Build with null string set to an empty string
        CSVFormat.DEFAULT.builder().setNullString("").build()
        self.__every(
            CSVFormat.DEFAULT.builder().setNullString("").build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Builder with QuoteMode.ALL
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setNullString("")
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(
            QuoteMode.ALL
        ).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build(),
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Builder with QuoteMode.ALL_NON_NULL
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setNullString("")
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(
            QuoteMode.ALL_NON_NULL
        )
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(
            QuoteMode.ALL_NON_NULL
        ).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Builder with QuoteMode.MINIMAL
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setNullString("")
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(
            QuoteMode.MINIMAL
        ).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Builder with escape character and QuoteMode.NONE
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setNullString("")
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0("?")
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0("?").setQuoteMode(
            QuoteMode.NONE
        )
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0("?").setQuoteMode(
            QuoteMode.NONE
        ).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

        # Final builder with null string set to an empty string
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setNullString("")

    def testWithSetNullStringEmptyString_test25_decomposed(self) -> None:
        # Test case 1
        csv_format = CSVFormat.DEFAULT.builder().setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test24_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setEscape0("?")
        builder.setNullString("").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test23_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setEscape0("?")
        builder.setNullString("").setEscape0("?").setQuoteMode(QuoteMode.NONE)
        csv_format = (
            builder.setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )

    def testWithSetNullStringEmptyString_test22_decomposed(self) -> None:
        # Test case 1
        csv_format1 = CSVFormat.DEFAULT.builder().setNullString("").build()
        self.__every(
            csv_format1,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format2 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format2,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format3 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format3,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format4 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format4,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        csv_format5 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )
        # No `every` call for this case as per the Java code

    def testWithSetNullStringEmptyString_test21_decomposed(self) -> None:
        # Test case 1
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 5
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setEscape0("?")

    def testWithSetNullStringEmptyString_test20_decomposed(self) -> None:
        # Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test with default quote mode
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test with QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Final builder call
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

    def testWithSetNullStringEmptyString_test19_decomposed(self) -> None:
        # Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test with the first configuration
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test with QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test18_decomposed(self) -> None:
        # Test case 1
        csv_format_1 = CSVFormat.DEFAULT.builder().setNullString("").build()
        self.__every(
            csv_format_1,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        csv_format_2 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )
        self.__every(
            csv_format_2,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        csv_format_3 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )
        self.__every(
            csv_format_3,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        csv_format_4 = (
            CSVFormat.DEFAULT.builder()
            .setNullString("")
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )
        self.__every(
            csv_format_4,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test17_decomposed(self) -> None:
        # Test case 1
        builder1 = CSVFormat.DEFAULT.builder()
        builder1.setNullString("")
        csvFormat1 = builder1.setNullString("").build()
        self.__every(
            csvFormat1,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 2
        builder2 = CSVFormat.DEFAULT.builder()
        builder2.setNullString("")
        builder2.setNullString("").setQuoteMode(QuoteMode.ALL)
        csvFormat2 = builder2.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csvFormat2,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test case 3
        builder3 = CSVFormat.DEFAULT.builder()
        builder3.setNullString("")
        builder3.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csvFormat3 = (
            builder3.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csvFormat3,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test case 4
        builder4 = CSVFormat.DEFAULT.builder()
        builder4.setNullString("")
        builder4.setNullString("").setQuoteMode(QuoteMode.MINIMAL)
        csvFormat4 = builder4.setNullString("").setQuoteMode(QuoteMode.MINIMAL).build()

    def testWithSetNullStringEmptyString_test16_decomposed(self) -> None:
        # Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test with default quote mode
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Test with QuoteMode.ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Test with QuoteMode.MINIMAL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.MINIMAL)

    def testWithSetNullStringEmptyString_test15_decomposed(self) -> None:
        # First case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Second case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Third case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

        # Final builder call
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

    def testWithSetNullStringEmptyString_test14_decomposed(self) -> None:
        # Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test with the first configuration
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set null string, and set quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

        # Test with the second configuration
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder, set null string, and set quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

        # Test with the third configuration
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test13_decomposed(self) -> None:
        # First case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Second case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Third case
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test12_decomposed(self) -> None:
        # Step 1: Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Step 2: Test with the first configuration
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 3: Create a builder, set null string, and set quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

        # Step 4: Test with the second configuration
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 5: Create a builder, set null string, and set quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        )

    def testWithSetNullStringEmptyString_test11_decomposed(self) -> None:
        # Step 1: Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Step 2: Test with the first configuration
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 3: Create a builder, set null string, and set quote mode to ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

        # Step 4: Test with the second configuration
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 5: Create a builder, set null string, and set quote mode to ALL_NON_NULL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL)

    def testWithSetNullStringEmptyString_test10_decomposed(self) -> None:
        # Create a builder and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set null string to an empty string with QuoteMode.ALL
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

        # Test the second case
        self.__every(
            csv_format,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create a builder and set null string to an empty string again
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

    def testWithSetNullStringEmptyString_test9_decomposed(self) -> None:
        # Step 1: Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Step 2: Set the null string to an empty string and build the format
        csv_format1 = builder.setNullString("").build()

        # Step 3: Test the first case
        self.__every(
            csv_format1,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Step 4: Create another builder and set the null string and quote mode
        builder = CSVFormat.DEFAULT.builder()
        csv_format2 = builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

        # Step 5: Test the second case
        self.__every(
            csv_format2,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test8_decomposed(self) -> None:
        # Create a builder instance and set null string to an empty string
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()

        # Test the first case
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create another builder instance and set null string and quote mode
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        csv_format_with_quote_mode = (
            builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()
        )

        # Test the second case
        self.__every(
            csv_format_with_quote_mode,
            self.__objects1,
            '"abc","","","a,b,c","123"',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test7_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to an empty string
        builder.setNullString("")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Additional builder configurations
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)
        builder.setNullString("").setQuoteMode(QuoteMode.ALL).build()

    def testWithSetNullStringEmptyString_test6_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to an empty string
        builder.setNullString("")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create another builder and set the null string again
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

        # Set the quote mode to QuoteMode.ALL
        builder.setNullString("").setQuoteMode(QuoteMode.ALL)

    def testWithSetNullStringEmptyString_test5_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to an empty string
        builder.setNullString("")

        # Build the CSVFormat with the null string set
        csv_format = builder.setNullString("").build()

        # Call the __every method with the appropriate arguments
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Recreate the builder and set the null string again
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

    def testWithSetNullStringEmptyString_test4_decomposed(self) -> None:
        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set the null string to an empty string
        builder.setNullString("")

        # Build the CSVFormat with the updated null string
        csv_format = builder.setNullString("").build()

        # Call the __every method with the required parameters
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

        # Create another builder (not strictly necessary, but matches the Java code)
        CSVFormat.DEFAULT.builder()

    def testWithSetNullStringEmptyString_test3_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        csv_format = builder.setNullString("").build()
        self.__every(
            csv_format,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", None, None, "a,b,c", "123"],
        )

    def testWithSetNullStringEmptyString_test2_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")
        builder.build()

    def testWithSetNullStringEmptyString_test1_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setNullString("")

    def testWithSetNullStringEmptyString_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()

    def testWithNotSetNullString_test21_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build(),
            self.__objects1,
            '"abc","",,"a,b,c",123',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithNotSetNullString_test20_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build()

    def testWithNotSetNullString_test19_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC)

    def testWithNotSetNullString_test18_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()

    def testWithNotSetNullString_test17_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()
        self.__every(
            CSVFormat.DEFAULT.builder()
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NONE)
            .build(),
            self.__objects1,
            "abc,,,a?,b?,c,123",
            ["abc", "", "", "a,b,c", "123"],
        )

    def testWithNotSetNullString_test16_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE).build()

    def testWithNotSetNullString_test15_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")
        CSVFormat.DEFAULT.builder().setEscape0("?").setQuoteMode(QuoteMode.NONE)

    def testWithNotSetNullString_test14_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setEscape0("?")

    def testWithNotSetNullString_test13_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        self.__every(
            builder.setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        self.__every(
            builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.MINIMAL)
        self.__every(
            builder.setQuoteMode(QuoteMode.MINIMAL).build(),
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )

    def testWithNotSetNullString_test12_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        csvFormatAll = builder.setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csvFormatAll,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csvFormatAllNonNull = builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            csvFormatAllNonNull,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.MINIMAL)
        csvFormatMinimal = builder.setQuoteMode(QuoteMode.MINIMAL).build()
        self.__every(
            csvFormatMinimal,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )

    def testWithNotSetNullString_test11_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build()

    def testWithNotSetNullString_test10_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        builder.build()
        self.__every(
            builder.setQuoteMode(QuoteMode.ALL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        builder.build()
        self.__every(
            builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.MINIMAL)

    def testWithNotSetNullString_test9_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format_all = builder.setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format_all,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csv_format_all_non_null = builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            csv_format_all_non_null,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithNotSetNullString_test8_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        csvFormatAll = builder.setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csvFormatAll,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        csvFormatAllNonNull = builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build()
        self.__every(
            csvFormatAllNonNull,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", None, "a,b,c", "123"],
        )

    def testWithNotSetNullString_test7_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format_all = builder.setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format_all,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL).build()

    def testWithNotSetNullString_test6_decomposed(self) -> None:
        # Test with default CSVFormat
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )

        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set QuoteMode to ALL and build the CSVFormat
        csv_format_with_all_quotes = builder.setQuoteMode(QuoteMode.ALL).build()

        # Test with the modified CSVFormat
        self.__every(
            csv_format_with_all_quotes,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )

        # Create another builder and set QuoteMode to ALL_NON_NULL
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)

    def testWithNotSetNullString_test5_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        csv_format_with_quote_mode = builder.setQuoteMode(QuoteMode.ALL).build()
        self.__every(
            csv_format_with_quote_mode,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()

    def testWithNotSetNullString_test4_decomposed(self) -> None:
        # Test with default CSVFormat
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )

        # Create a builder from the default CSVFormat
        builder = CSVFormat.DEFAULT.builder()

        # Set QuoteMode to ALL and build a new CSVFormat
        csv_format_with_quote_mode = builder.setQuoteMode(QuoteMode.ALL).build()

        # Test with the new CSVFormat
        self.__every(
            csv_format_with_quote_mode,
            self.__objects1,
            '"abc","",,"a,b,c","123"',
            ["abc", "", "", "a,b,c", "123"],
        )

    def testWithNotSetNullString_test3_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build()

    def testWithNotSetNullString_test2_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)

    def testWithNotSetNullString_test1_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )
        CSVFormat.DEFAULT.builder()

    def testWithNotSetNullString_test0_decomposed(self) -> None:
        self.__every(
            CSVFormat.DEFAULT,
            self.__objects1,
            'abc,,,"a,b,c",123',
            ["abc", "", "", "a,b,c", "123"],
        )

    def __every(
        self,
        csvFormat: CSVFormat,
        objects: typing.List[typing.Any],
        format_: str,
        data: typing.List[str],
    ) -> None:
        source = csvFormat.format_(objects)
        self.assertEqual(format_, csvFormat.format_(objects))
        with io.StringIO(source) as reader:
            csvParser = csvFormat.parse(reader)
            csvRecord = next(csvParser.iterator())
            for i in range(len(data)):
                self.assertEqual(csvRecord.get1(i), data[i])
