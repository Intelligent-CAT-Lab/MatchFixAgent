from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv288Test(unittest.TestCase):

    def testParseWithTwoCharDelimiterEndsWithDelimiter_test0_decomposed(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~|")
        string_builder = io.StringIO()

        csv_format = CSVFormat.Builder.create0().setDelimiter1("~|").build()

        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(in_, csv_format) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithTwoCharDelimiter4_test0_decomposed(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~~||g")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Used to collect the output

        # Create CSVPrinter and CSVParser instances
        csv_printer = CSVPrinter(string_builder, CSVFormat.EXCEL)
        csv_parser = CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("~|").build()
        )

        # Iterate through the parsed records
        for csv_record in csv_parser:
            self.__print_(csv_record, csv_printer)  # Call the helper print method
            self.assertEqual("a,b,c,d,,f~,|g", string_builder.getvalue())

    def testParseWithTwoCharDelimiter3_test0_decomposed(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f|")  # Simulates the Java StringReader
        string_builder = io.StringIO()  # Simulates the Java StringBuilder

        # Create CSVPrinter and CSVParser instances
        csv_printer = CSVPrinter(string_builder, CSVFormat.EXCEL)
        csv_parser = CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("~|").build()
        )

        # Iterate through CSV records
        for csv_record in csv_parser:
            self.__print_(csv_record, csv_printer)
            self.assertEqual("a,b,c,d,,f|", string_builder.getvalue())

    def testParseWithTwoCharDelimiter2_test0_decomposed(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f~")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Acts as a StringBuilder in Python

        # Using a context manager to handle resources
        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("~|").build()
        ) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)  # Call the helper print method
                self.assertEqual(
                    "a,b,c,d,,f~", string_builder.getvalue()
                )  # Validate the output

    def testParseWithTwoCharDelimiter1_test0_decomposed(self) -> None:
        in_ = io.StringIO("a~|b~|c~|d~|~|f")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Acts as a StringBuilder in Python

        csv_format = CSVFormat.Builder.create0().setDelimiter1("~|").build()
        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(in_, csv_format) as csv_parser:
            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def testParseWithTriplePipeDelimiter_test0_decomposed(self) -> None:
        in_ = io.StringIO("a|||b|||c|||d||||||f")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Acts as a StringBuilder in Python

        csv_format = CSVFormat.Builder.create0().setDelimiter1("|||").build()

        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(in_, csv_format) as csv_parser:
            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def testParseWithSinglePipeDelimiterEndsWithDelimiter_test0_decomposed(
        self,
    ) -> None:
        in_ = io.StringIO("a|b|c|d||f|")
        string_builder = io.StringIO()

        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("|").build()
        ) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithDoublePipeDelimiterQuoted_test0_decomposed(self) -> None:
        in_ = io.StringIO('a||"b||c"||d||||f')  # Simulates the Java StringReader
        string_builder = io.StringIO()  # Simulates the Java StringBuilder

        # Create CSVPrinter and CSVParser with the appropriate configurations
        csv_printer = CSVPrinter(string_builder, CSVFormat.EXCEL)
        csv_parser = CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("||").build()
        )

        try:
            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b||c,d,,f", string_builder.getvalue())
        finally:
            in_.close()

    def testParseWithDoublePipeDelimiterEndsWithDelimiter_test0_decomposed(
        self,
    ) -> None:
        in_ = io.StringIO("a||b||c||d||||f||")
        string_builder = io.StringIO()

        csv_format = CSVFormat.Builder.create0().setDelimiter1("||").build()

        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(in_, csv_format) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f,", string_builder.getvalue())

    def testParseWithDoublePipeDelimiterDoubleCharValue_test0_decomposed(self) -> None:
        in_ = io.StringIO("a||bb||cc||dd||f")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Acts as a StringBuilder in Python

        # Using a context manager to handle resources
        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(
            in_, Builder.create0().setDelimiter1("||").build()
        ) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(
                    csv_record, csv_printer
                )  # Call the helper method to print the record
                self.assertEqual(
                    "a,bb,cc,dd,f", string_builder.getvalue()
                )  # Validate the output

    def testParseWithDoublePipeDelimiter_test0_decomposed(self) -> None:
        in_ = io.StringIO("a||b||c||d||||f")  # Equivalent to Java's StringReader
        string_builder = io.StringIO()  # Acts as a StringBuilder in Python

        # Create CSVPrinter and CSVParser with the specified format
        csv_format = CSVFormat.Builder.create0().setDelimiter1("||").build()
        with CSVPrinter(
            string_builder, CSVFormat.EXCEL
        ) as csv_printer, CSVParser.parse3(in_, csv_format) as csv_parser:

            for csv_record in csv_parser:
                self.__print_(csv_record, csv_printer)
                self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def testParseWithABADelimiter_test0_decomposed(self) -> None:
        in_ = io.StringIO("a|~|b|~|c|~|d|~||~|f")  # Simulates the Java StringReader
        string_builder = io.StringIO()  # Simulates the Java StringBuilder

        # Create CSVPrinter and CSVParser
        csv_printer = CSVPrinter(string_builder, CSVFormat.EXCEL)
        parser = CSVParser.parse3(in_, Builder.create0().setDelimiter1("|~|").build())

        # Iterate through the parsed records
        for csv_record in parser:
            self.__print_(csv_record, csv_printer)
            self.assertEqual("a,b,c,d,,f", string_builder.getvalue())

    def __print_(self, csvRecord: CSVRecord, csvPrinter: CSVPrinter) -> None:
        for value in csvRecord:
            csvPrinter.print_(value)
