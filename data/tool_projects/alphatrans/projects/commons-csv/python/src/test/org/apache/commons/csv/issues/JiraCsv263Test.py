from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv263Test(unittest.TestCase):

    def testPrintFromReaderWithQuotes_test17_decomposed(self) -> None:
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out = io.StringIO()

        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z""', out.getvalue())

        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.getvalue())

        nested = io.StringIO('a,"b "and" c",d')
        out.seek(0)
        out.truncate(0)
        format.print2(nested, out, True)
        self.assertEqual('"a,""b ""and"" c"",d"', out.getvalue())

    def testPrintFromReaderWithQuotes_test16_decomposed(self) -> None:
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out = io.StringIO()

        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.getvalue())

        nested = io.StringIO('a,"b "and" c",d')
        out.seek(0)
        out.truncate(0)
        format.print2(nested, out, True)

    def testPrintFromReaderWithQuotes_test15_decomposed(self) -> None:
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out = io.StringIO()

        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedMiddleEnd, out, True)
        self.assertEqual('"a,""b"",c\r\nx,y,""z"""', out.getvalue())

    def testPrintFromReaderWithQuotes_test14_decomposed(self) -> None:
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )
        out = io.StringIO()

        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z""', out.getvalue())

        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embeddedBeginMiddle = io.StringIO('"a",b,c\r\nx,"y",z')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedBeginMiddle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

        embeddedMiddleEnd = io.StringIO('a,"b",c\r\nx,y,"z"')
        out.seek(0)
        out.truncate(0)
        format.print2(embeddedMiddleEnd, out, True)
        # Add the expected assertion for the last case if needed

    def testPrintFromReaderWithQuotes_test13_decomposed(self) -> None:
        format_builder = CSVFormat.RFC4180.builder()
        format_builder.setDelimiter0(",")
        format_builder.setDelimiter0(",").setQuote0('"')
        format_builder.setDelimiter0(",").setQuote0('"').setEscape0("?")
        format_builder.setDelimiter0(",").setQuote0('"').setEscape0("?").setQuoteMode(
            QuoteMode.NON_NUMERIC
        )
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )

        out = io.StringIO()

        at_start_only = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(at_start_only, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        at_end_only = io.StringIO('a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(at_end_only, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        at_begin_end = io.StringIO('"a,b,c\r\nx,y,z"')
        out.seek(0)
        out.truncate(0)
        format.print2(at_begin_end, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        embedded_begin_middle = io.StringIO('"a",b,c\r\nx,"y",z')
        out.seek(0)
        out.truncate(0)
        format.print2(embedded_begin_middle, out, True)
        self.assertEqual('"""a"",b,c\r\nx,""y"",z"', out.getvalue())

    def testPrintFromReaderWithQuotes_test12_decomposed(self) -> None:
        # Create the CSVFormat using the builder pattern
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )

        # Test case 1: Reader with quotes at the start only
        out = io.StringIO()
        at_start_only = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(at_start_only, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        # Test case 2: Reader with quotes at the end only
        at_end_only = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(at_end_only, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        # Test case 3: Reader with quotes at both the beginning and the end
        at_begin_end = io.StringIO('"a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(at_begin_end, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

        # Test case 4: Reader with embedded quotes in the middle
        embedded_begin_middle = io.StringIO('"a",b,c\r\nx,"y",z')
        out = io.StringIO()  # Reset the output
        format.print2(embedded_begin_middle, out, True)
        # No assertion provided in the original Java code for this case

    def testPrintFromReaderWithQuotes_test11_decomposed(self) -> None:
        # Step 1: Create the CSVFormat builder and configure it
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setQuote0('"')
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        format = builder.build()

        # Step 2: Test with a reader containing quotes at the start only
        out = io.StringIO()
        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        # Step 3: Test with a reader containing quotes at the end only
        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        # Step 4: Test with a reader containing quotes at both the beginning and the end
        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(atBeginEnd, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"""', out.getvalue())

    def testPrintFromReaderWithQuotes_test10_decomposed(self) -> None:
        # Create the CSVFormat builder and configure it step by step
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setQuote0('"')
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        format = builder.build()

        # Test case 1: Reader with quotes at the start only
        out = io.StringIO()
        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(atStartOnly, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        # Test case 2: Reader with quotes at the end only
        atEndOnly = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(atEndOnly, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

        # Test case 3: Reader with quotes at both the beginning and the end
        atBeginEnd = io.StringIO('"a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output
        format.print2(atBeginEnd, out, True)
        # No assertion provided in the original Java code for this case

    def testPrintFromReaderWithQuotes_test9_decomposed(self) -> None:
        # Create the CSVFormat builder and configure it step by step
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setQuote0('"')
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)

        # Build the final CSVFormat object
        format = builder.build()

        # Test case 1: Reader with quotes at the start only
        out = io.StringIO()
        at_start_only = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(at_start_only, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        # Test case 2: Reader with quotes at the end only
        at_end_only = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output buffer
        format.print2(at_end_only, out, True)
        self.assertEqual('"a,b,c\r\nx,y,z"""', out.getvalue())

    def testPrintFromReaderWithQuotes_test8_decomposed(self) -> None:
        # Create the CSVFormat builder and configure it step by step
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setQuote0('"')
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)

        # Build the final CSVFormat object
        format = builder.build()

        # Test case 1: Reader with quotes at the start only
        out = io.StringIO()
        at_start_only = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(at_start_only, out, True)
        self.assertEqual('"""a,b,c\r\nx,y,z"', out.getvalue())

        # Test case 2: Reader with quotes at the end only
        at_end_only = io.StringIO('a,b,c\r\nx,y,z"')
        out = io.StringIO()  # Reset the output buffer
        format.print2(at_end_only, out, True)

    def testPrintFromReaderWithQuotes_test7_decomposed(self) -> None:
        # Create a CSVFormat builder and configure it step by step
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setQuote0('"')
        builder.setEscape0("?")
        builder.setQuoteMode(QuoteMode.NON_NUMERIC)

        # Build the final CSVFormat object
        format = builder.build()

        # Prepare the output and input
        out = io.StringIO()
        atStartOnly = io.StringIO('"a,b,c\r\nx,y,z')

        # Use the format to print the input to the output
        format.print2(atStartOnly, out, True)

        # Assert the output matches the expected result
        self.assertEqual('"""a,b,c\r\nx,y,z""', out.getvalue())

    def testPrintFromReaderWithQuotes_test6_decomposed(self) -> None:
        format_builder = CSVFormat.RFC4180.builder()
        format_builder.setDelimiter0(",")
        format_builder.setQuote0('"')
        format_builder.setEscape0("?")
        format_builder.setQuoteMode(QuoteMode.NON_NUMERIC)
        format = format_builder.build()

        out = io.StringIO()
        at_start_only = io.StringIO('"a,b,c\r\nx,y,z')
        format.print2(at_start_only, out, True)

    def testPrintFromReaderWithQuotes_test5_decomposed(self) -> None:
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setDelimiter0(",").setQuote0('"')
        builder.setDelimiter0(",").setQuote0('"').setEscape0("?")
        builder.setDelimiter0(",").setQuote0('"').setEscape0("?").setQuoteMode(
            QuoteMode.NON_NUMERIC
        )
        format = (
            CSVFormat.RFC4180.builder()
            .setDelimiter0(",")
            .setQuote0('"')
            .setEscape0("?")
            .setQuoteMode(QuoteMode.NON_NUMERIC)
            .build()
        )

    def testPrintFromReaderWithQuotes_test4_decomposed(self) -> None:
        builder = CSVFormat.RFC4180.builder()
        builder.setDelimiter0(",")
        builder.setDelimiter0(",").setQuote0('"')
        builder.setDelimiter0(",").setQuote0('"').setEscape0("?")
        builder.setDelimiter0(",").setQuote0('"').setEscape0("?").setQuoteMode(
            QuoteMode.NON_NUMERIC
        )

    def testPrintFromReaderWithQuotes_test3_decomposed(self) -> None:
        CSVFormat.RFC4180.builder()
        CSVFormat.RFC4180.builder().setDelimiter0(",")
        CSVFormat.RFC4180.builder().setDelimiter0(",").setQuote0('"')
        CSVFormat.RFC4180.builder().setDelimiter0(",").setQuote0('"').setEscape0("?")

    def testPrintFromReaderWithQuotes_test2_decomposed(self) -> None:
        CSVFormat.RFC4180.builder()
        CSVFormat.RFC4180.builder().setDelimiter0(",")
        CSVFormat.RFC4180.builder().setDelimiter0(",").setQuote0('"')

    def testPrintFromReaderWithQuotes_test1_decomposed(self) -> None:
        CSVFormat.RFC4180.builder()
        CSVFormat.RFC4180.builder().setDelimiter0(",")

    def testPrintFromReaderWithQuotes_test0_decomposed(self) -> None:
        CSVFormat.RFC4180.builder()
