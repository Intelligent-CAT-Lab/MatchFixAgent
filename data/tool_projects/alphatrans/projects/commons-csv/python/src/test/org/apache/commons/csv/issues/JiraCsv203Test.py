from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv203Test(unittest.TestCase):

    def testWithoutQuoteMode_test5_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)

        # Build the CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to print records
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    def testWithoutQuoteMode_test4_decomposed(self) -> None:
        format_builder = CSVFormat.EXCEL.builder()
        format_builder = format_builder.setNullString("N/A")
        format_builder = format_builder.setIgnoreSurroundingSpaces(True)
        format_ = format_builder.build()
        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testWithoutQuoteMode_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .build()
        )

    def testWithoutQuoteMode_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testWithoutQuoteMode_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")

    def testWithoutQuoteMode_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testWithoutNullString_test5_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it
        builder = CSVFormat.EXCEL.builder()
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.ALL)

        # Build the final CSVFormat
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to print the record
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output
        self.assertEqual(',"Hello",,"World"\r\n', buffer.getvalue())

    def testWithoutNullString_test4_decomposed(self) -> None:
        # Create a CSVFormat builder based on EXCEL
        builder = CSVFormat.EXCEL.builder()

        # Set ignore surrounding spaces to True
        builder.setIgnoreSurroundingSpaces(True)

        # Set quote mode to ALL
        builder.setQuoteMode(QuoteMode.ALL)

        # Build the final CSVFormat
        format_ = builder.build()

        # Create a StringBuilder equivalent (using io.StringIO in Python)
        buffer = io.StringIO()

        # Use a CSVPrinter to print records
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testWithoutNullString_test3_decomposed(self) -> None:
        # Create a builder for the EXCEL format
        CSVFormat.EXCEL.builder()

        # Set the builder to ignore surrounding spaces
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(True)

        # Set the builder to ignore surrounding spaces and set the quote mode to ALL
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(True).setQuoteMode(
            QuoteMode.ALL
        )

        # Build the final CSVFormat object with the specified configurations
        format = (
            CSVFormat.EXCEL.builder()
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

    def testWithoutNullString_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(True).setQuoteMode(
            QuoteMode.ALL
        )

    def testWithoutNullString_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(True)

    def testWithoutNullString_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testWithEmptyValues_test6_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.ALL)

        # Build the final CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to write records to the buffer
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1("", "Hello", "", "World")

        # Assert the expected output
        self.assertEqual('"","Hello","","World"\r\n', buffer.getvalue())

    def testWithEmptyValues_test5_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.EXCEL.builder()
        builder = builder.setNullString("N/A")
        builder = builder.setIgnoreSurroundingSpaces(True)
        builder = builder.setQuoteMode(QuoteMode.ALL)

        # Build the final CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (using io.StringIO in Python)
        buffer = io.StringIO()

        # Use the CSVPrinter to print a record
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(["", "Hello", "", "World"])

    def testWithEmptyValues_test4_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.ALL)
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

    def testWithEmptyValues_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.ALL)

    def testWithEmptyValues_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testWithEmptyValues_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")

    def testWithEmptyValues_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testQuoteModeNonNumeric_test6_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)

        # Build the final CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (using io.StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to write the record
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output matches the expected result
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    def testQuoteModeNonNumeric_test5_decomposed(self) -> None:
        format_builder = CSVFormat.EXCEL.builder()
        format_builder = format_builder.setNullString("N/A")
        format_builder = format_builder.setIgnoreSurroundingSpaces(True)
        format_builder = format_builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        format_ = format_builder.build()

        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testQuoteModeNonNumeric_test4_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.NON_NUMERIC)
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )

    def testQuoteModeNonNumeric_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.NON_NUMERIC)

    def testQuoteModeNonNumeric_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testQuoteModeNonNumeric_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")

    def testQuoteModeNonNumeric_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testQuoteModeMinimal_test6_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.MINIMAL)

        # Build the final CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use the CSVPrinter to write records to the buffer
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output matches the expected result
        self.assertEqual("N/A,Hello,N/A,World\r\n", buffer.getvalue())

    def testQuoteModeMinimal_test5_decomposed(self) -> None:
        format_builder = CSVFormat.EXCEL.builder()
        format_builder = format_builder.setNullString("N/A")
        format_builder = format_builder.setIgnoreSurroundingSpaces(True)
        format_builder = format_builder.setQuoteMode(QuoteMode.MINIMAL)
        format_ = format_builder.build()

        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testQuoteModeMinimal_test4_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.MINIMAL)
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.MINIMAL)
            .build()
        )

    def testQuoteModeMinimal_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.MINIMAL)

    def testQuoteModeMinimal_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testQuoteModeMinimal_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")

    def testQuoteModeMinimal_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testQuoteModeAllNonNull_test6_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.ALL_NON_NULL)

        # Build the CSVFormat
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to print the record
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output
        self.assertEqual('N/A,"Hello",N/A,"World"\r\n', buffer.getvalue())

    def testQuoteModeAllNonNull_test5_decomposed(self) -> None:
        format_builder = CSVFormat.EXCEL.builder()
        format_builder = format_builder.setNullString("N/A")
        format_builder = format_builder.setIgnoreSurroundingSpaces(True)
        format_builder = format_builder.setQuoteMode(QuoteMode.ALL_NON_NULL)
        format_ = format_builder.build()

        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testQuoteModeAllNonNull_test4_decomposed(self) -> None:
        # Create a builder for the EXCEL format
        builder = CSVFormat.EXCEL.builder()

        # Set the null string to "N/A"
        builder.setNullString("N/A")

        # Set the null string to "N/A" and ignore surrounding spaces
        builder.setNullString("N/A").setIgnoreSurroundingSpaces(True)

        # Set the null string to "N/A", ignore surrounding spaces, and set the quote mode to ALL_NON_NULL
        builder.setNullString("N/A").setIgnoreSurroundingSpaces(True).setQuoteMode(
            QuoteMode.ALL_NON_NULL
        )

        # Build the final CSVFormat object
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL_NON_NULL)
            .build()
        )

    def testQuoteModeAllNonNull_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.ALL_NON_NULL)

    def testQuoteModeAllNonNull_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testQuoteModeAllNonNull_test1_decomposed(self) -> None:
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")

    def testQuoteModeAllNonNull_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()

    def testQuoteModeAll_test6_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.EXCEL.builder()
        builder.setNullString("N/A")
        builder.setIgnoreSurroundingSpaces(True)
        builder.setQuoteMode(QuoteMode.ALL)

        # Build the final CSVFormat object
        format_ = builder.build()

        # Create a StringBuilder equivalent (StringIO in Python)
        buffer = io.StringIO()

        # Use CSVPrinter to print records
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1(None, "Hello", None, "World")

        # Assert the output matches the expected result
        self.assertEqual('"N/A","Hello","N/A","World"\r\n', buffer.getvalue())

    def testQuoteModeAll_test5_decomposed(self) -> None:
        format_builder = CSVFormat.EXCEL.builder()
        format_builder = format_builder.setNullString("N/A")
        format_builder = format_builder.setIgnoreSurroundingSpaces(True)
        format_builder = format_builder.setQuoteMode(QuoteMode.ALL)
        format_ = format_builder.build()

        buffer = io.StringIO()
        with CSVPrinter(buffer, format_) as printer:
            printer.printRecord1([None, "Hello", None, "World"])

    def testQuoteModeAll_test4_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.ALL)
        format = (
            CSVFormat.EXCEL.builder()
            .setNullString("N/A")
            .setIgnoreSurroundingSpaces(True)
            .setQuoteMode(QuoteMode.ALL)
            .build()
        )

    def testQuoteModeAll_test3_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(
            True
        ).setQuoteMode(QuoteMode.ALL)

    def testQuoteModeAll_test2_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(True)

    def testQuoteModeAll_test1_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
        CSVFormat.EXCEL.builder().setNullString("N/A")

    def testQuoteModeAll_test0_decomposed(self) -> None:
        CSVFormat.EXCEL.builder()
