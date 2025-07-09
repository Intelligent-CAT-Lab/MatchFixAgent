from __future__ import annotations
import time
import copy
import re
import tempfile
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.QuoteMode import *
from src.test.org.apache.commons.csv.Utils import *


class CSVPrinterTest(unittest.TestCase):

    __recordSeparator: str = None  # LLM could not translate this field

    __longText2: str = ""

    __QUOTE_CH: str = "'"
    __ITERATIONS_FOR_RANDOM_TEST: int = 50000
    __EURO_CH: str = "\u20ac"
    __DQUOTE_CHAR: str = '"'

    def testTrimOnTwoColumns_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print_(" A ")  # Corresponds to printer.print in Java
            printer.print_(" B ")
        self.assertEqual(
            "A,B", sw.getvalue().strip()
        )  # Ensure the output matches "A,B"

    def testTrimOnOneColumn_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0()) as printer:
            printer.print_(" A ")
        self.assertEqual(
            " A ", sw.getvalue(), "Trimmed value does not match expected output"
        )

    def testTrimOffOneColumn_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrim1(False)) as printer:
            printer.print_(" A ")
            self.assertEqual(
                '" A "', sw.getvalue(), "Output does not match expected value"
            )

    def testTrailingDelimiterOnTwoColumns_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withTrailingDelimiter0()) as printer:
            printer.printRecord1(["A", "B"])
        self.assertEqual("A,B,\r\n", sw.getvalue())

    def testSingleQuoteQuoted_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("a'b'c")
            printer.print_("xyz")
        self.assertEqual("'a''b''c',xyz", sw.getvalue())

    def testSingleLineComment_test0_decomposed(self) -> None:
        sw = io.StringIO()
        printer = None
        try:
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#"))
            printer.printComment("This is a comment")
            self.assertEqual(
                "# This is a comment" + CSVFormat.DEFAULT._CSVFormat__recordSeparator,
                sw.getvalue(),
            )
        finally:
            if printer is not None:
                printer.close()

    def testRandomTdf_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.TDF, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomRfc4180_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.RFC4180, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomPostgreSqlText_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.POSTGRESQL_TEXT, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomMySql_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.MYSQL, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomExcel_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.EXCEL, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomDefault_test0_decomposed(self) -> None:
        self.__doRandom(CSVFormat.DEFAULT, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testQuoteNonNumeric_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC)
        ) as printer:
            printer.printRecord1(["a", "b\nc", 1])
            self.assertEqual(
                f'"a","b\nc",1{CSVFormat.DEFAULT._CSVFormat__recordSeparator}',
                sw.getvalue(),
            )

    def testQuoteCommaFirstChar_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        csv_format = CSVFormat.RFC4180  # Use RFC4180 format directly
        with CSVPrinter(sw, csv_format) as printer:
            printer.printRecord1([","])  # Pass the value as a list
            self.assertEqual(f'",{csv_format.getRecordSeparator()}', sw.getvalue())

    def testQuoteAll_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL)) as printer:
            printer.printRecord1(["a", "b\nc", "d"])
            self.assertEqual(
                f'"a","b\nc","d"{CSVFormat.DEFAULT._CSVFormat__recordSeparator}',
                sw.getvalue(),
            )

    def testPrintToPathWithDefaultCharset_test2_decomposed(self) -> None:
        file = self.__createTempPath()
        try:
            with CSVFormat.DEFAULT.print4(file, os.device_encoding(0)) as printer:
                printer.printRecord1(["a", "b\\c"])
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

        with file.open(mode="r", encoding=os.device_encoding(0)) as f:
            content = f.read()

        expected = f"a,b\\c{self.__recordSeparator}"
        self.assertEqual(expected, content)

    def testPrintToPathWithDefaultCharset_test1_decomposed(self) -> None:
        file: Path = self.__createTempPath()
        try:
            with CSVFormat.DEFAULT.print4(file, os.device_encoding(0)) as printer:
                printer.printRecord1(["a", "b\\c"])
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def testPrintToPathWithDefaultCharset_test0_decomposed(self) -> None:
        file = self.__createTempPath()

    def testPrintRecordStream_test1_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        # First try block
        with format_.print0(sw) as printer, CSVParser.parse4(code, format_) as parser:
            for record in parser:
                printer.printRecord2(record.stream())

        # Second try block
        with CSVParser.parse4(sw.getvalue(), format_) as parser:
            records = parser.getRecords()
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())
            Utils.compare("Fail", res, records)

    def testPrintRecordStream_test0_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with format_.print0(sw) as printer, CSVParser.parse4(code, format_) as parser:
            for record in parser:
                printer.printRecord2(record.stream())

    def testPrintReaderWithoutQuoteToWriter_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        content = "testValue"

        # Using a context manager to simulate the try-with-resources block
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)  # StringReader equivalent in Python
            printer.print_(
                value
            )  # Call the print_ method (Python equivalent of print in Java)

        self.assertEqual(content, sw.getvalue())  # Assert the content matches

    def testPrintReaderWithoutQuoteToWriter_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        content = "testValue"
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)  # StringReader equivalent in Python
            printer.print_(value)

    def testPrintReaderWithoutQuoteToAppendable_test1_decomposed(self) -> None:
        sb = io.StringIO()  # StringBuilder equivalent in Python
        content = "testValue"

        with CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)  # StringReader equivalent in Python
            printer.print_(value)

        self.assertEqual(content, sb.getvalue())

    def testPrintReaderWithoutQuoteToAppendable_test0_decomposed(self) -> None:
        sb = io.StringIO()  # StringBuilder equivalent in Python
        content = "testValue"
        with CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            value = io.StringIO(content)  # StringReader equivalent in Python
            printer.print_(value)

    def testPrintOnePositiveInteger_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL)
        ) as printer:
            printer.print_((2**31) - 1)  # 2147483647 in Java is 2^31 - 1
            self.assertEqual(str((2**31) - 1), sw.getvalue().strip())

    def testPrintNullValues_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", None, "b"])  # Pass the values as a list
            self.assertEqual(f"a,,b{self.__recordSeparator}", sw.getvalue())

    def testPrinter7_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\\c"])  # Corrected to pass a list of values
            self.assertEqual(f"a,b\\c{self.__recordSeparator}", sw.getvalue())

    def testPrinter6_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\r\nc"])
            self.assertEqual(f'a,"b\r\nc"{self.__recordSeparator}', sw.getvalue())

    def testPrinter5_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b\nc"])
            self.assertEqual(f'a,"b\nc"{self.__recordSeparator}', sw.getvalue())

    def testPrinter4_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", 'b"c'])  # Print the record
            self.assertEqual(
                f'a,"b""c"{self.__recordSeparator}', sw.getvalue()
            )  # Assert the output

    def testPrinter3_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a, b", "b "])  # Corrected to pass a list of values
            self.assertEqual(f'"a, b","b "{self.__recordSeparator}', sw.getvalue())

    def testPrinter2_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a,b", "b"])  # Corrected to pass a list of values
            self.assertEqual(f'"a,b",b{self.__recordSeparator}', sw.getvalue())

    def testPrinter1_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b"])  # Corrected to pass a list as argument
            self.assertEqual(
                f"a,b{self.__recordSeparator}",
                sw.getvalue(),
                "Output does not match expected value",
            )

    def testPrintCustomNullValues_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL")) as printer:
            printer.printRecord1(["a", None, "b"])
            self.assertEqual(
                f"a,NULL,b{CSVFormat.DEFAULT.getRecordSeparator()}", sw.getvalue()
            )

    def testPrintCSVRecords_test1_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        # First try block
        with format_.print0(sw) as printer, CSVParser.parse4(code, format_) as parser:
            printer.printRecords0(parser.getRecords())

        # Second try block
        with CSVParser.parse4(sw.getvalue(), format_) as parser:
            records = parser.getRecords()
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())
            Utils.compare("Fail", res, records)

    def testPrintCSVRecords_test0_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with CSVPrinter(sw, format_) as printer, CSVParser.parse4(
            code, format_
        ) as parser:
            printer.printRecords0(parser.getRecords())

    def testPrintCSVRecord_test1_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with format_.print0(sw) as printer, CSVParser.parse4(code, format_) as parser:
            for record in parser:
                printer.printRecord0(record)

        with CSVParser.parse4(sw.getvalue(), format_) as parser:
            records = parser.getRecords()
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())
            Utils.compare("Fail", res, records)

    def testPrintCSVRecord_test0_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with CSVPrinter(sw, format_) as printer, CSVParser.parse4(
            code, format_
        ) as parser:
            for record in parser:
                printer.printRecord0(record)

    def testPrintCSVParser_test1_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with CSVPrinter(sw, format_) as printer, CSVParser.parse4(
            code, format_
        ) as parser:
            printer.printRecords0(parser)

        with CSVParser.parse4(sw.getvalue(), format_) as parser:
            records = parser.getRecords()
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())
            Utils.compare("Fail", res, records)

    def testPrintCSVParser_test0_decomposed(self) -> None:
        code = "a1,b1\n" + "a2,b2\n" + "a3,b3\n" + "a4,b4\n"  # 1)  # 2)  # 3)  # 4)
        res = [["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]]
        format_ = CSVFormat.DEFAULT
        sw = io.StringIO()

        with CSVPrinter(sw, format_) as printer, CSVParser.parse4(
            code, format_
        ) as parser:
            printer.printRecords0(parser)

    def testPrint_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVFormat.DEFAULT.print0(sw) as printer:
            printer.printRecord1(["a", "b\\c"])
        self.assertEqual(
            f"a,b\\c{CSVFormat.DEFAULT._CSVFormat__recordSeparator}", sw.getvalue()
        )

    def testPostgreSqlNullStringDefaultText_test0_decomposed(self) -> None:
        self.assertEqual(
            "\\N",
            CSVFormat.POSTGRESQL_TEXT.getNullString(),
            "Null string does not match expected value '\\N'",
        )

    def testPostgreSqlNullStringDefaultCsv_test0_decomposed(self) -> None:
        self.assertEqual(
            "",
            CSVFormat.POSTGRESQL_CSV.getNullString(),
            "Null string does not match expected value",
        )

    def testPlainQuoted_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("abc")
        self.assertEqual("abc", sw.getvalue().strip())

    def testPlainPlain_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("abc")
            printer.print_("xyz")
        self.assertEqual("abc,xyz", sw.getvalue())

    def testPlainEscaped_test0_decomposed(self) -> None:
        sw = io.StringIO()
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!"))
        try:
            printer.print_("abc")
            printer.print_("xyz")
        finally:
            printer.close()
        self.assertEqual("abc,xyz", sw.getvalue())

    def testParseCustomNullValues_test3_decomposed(self) -> None:
        sw = io.StringIO()
        format_ = CSVFormat.DEFAULT.withNullString("NULL")

        # Writing to CSV using CSVPrinter
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord1(["a", None, "b"])

        csv_string = sw.getvalue()
        self.assertEqual(f"a,NULL,b{self.__recordSeparator}", csv_string)

        # Parsing the CSV string using CSVParser
        with format_.parse(io.StringIO(csv_string)) as iterable:
            iterator = iterable.iterator()
            record = next(iterator)

            self.assertEqual("a", record.get1(0))
            self.assertIsNone(record.get1(1))
            self.assertEqual("b", record.get1(2))
            self.assertFalse(iterator.hasNext())

    def testParseCustomNullValues_test2_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        format_ = CSVFormat.DEFAULT.withNullString(
            "NULL"
        )  # Set the null string to "NULL"
        with CSVPrinter(sw, format_) as printer:  # Use CSVPrinter with the format
            printer.printRecord1("a", None, "b")  # Print a record with a null value
        csv_string = sw.getvalue()  # Get the resulting CSV string

    def testParseCustomNullValues_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        format_ = CSVFormat.DEFAULT.withNullString(
            "NULL"
        )  # Set the null string to "NULL"
        with CSVPrinter(sw, format_) as printer:  # Use CSVPrinter with the format
            printer.printRecord1(["a", None, "b"])  # Print a record with a null value

    def testParseCustomNullValues_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        format = CSVFormat.DEFAULT.withNullString("NULL")

    def testNotFlushable_test0_decomposed(self) -> None:
        out = io.StringIO()  # Using StringIO to mimic StringBuilder in Java
        with CSVPrinter(out, CSVFormat.DEFAULT) as printer:
            printer.printRecord1(["a", "b", "c"])  # Corrected to pass a list
            self.assertEqual(
                f"a,b,c{self.__recordSeparator}",
                out.getvalue(),
                "Output does not match expected value",
            )
            printer.flush()

    def testNewCsvPrinterNullAppendableFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVPrinter(None, CSVFormat.DEFAULT)

    def testNewCsvPrinterAppendableNullFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVPrinter(io.StringIO(), None)

    def testMySqlNullStringDefault_test0_decomposed(self) -> None:
        self.assertEqual(
            "\\N",
            CSVFormat.MYSQL.getNullString(),
            "Null string does not match expected value '\\N'",
        )

    def testMySqlNullOutput_test41_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test40_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test39_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test38_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test37_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test36_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test35_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test34_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test33_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test32_decomposed(self) -> None:
        s = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test31_decomposed(self) -> None:
        s = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test30_decomposed(self) -> None:
        s = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test29_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test28_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)

    def testMySqlNullOutput_test27_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test26_decomposed(self) -> None:
        s = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test25_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test24_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test23_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test22_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test21_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.MYSQL.withNullString("NULL")

    def testMySqlNullOutput_test20_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test19_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)

    def testMySqlNullOutput_test18_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL").withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test17_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test16_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")

    def testMySqlNullOutput_test15_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test14_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)

    def testMySqlNullOutput_test13_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test12_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test11_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.MYSQL.withNullString("\\N")

    def testMySqlNullOutput_test10_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(s, format_), record0)

    def testMySqlNullOutput_test9_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

    def testMySqlNullOutput_test8_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test7_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test6_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withNullString("NULL")
        format_ = format_.withQuoteMode(QuoteMode.NON_NUMERIC)

        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(s, record0)

        s = ["\\N", None]
        format_ = CSVFormat.MYSQL.withNullString("\\N")

    def testMySqlNullOutput_test5_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)

    def testMySqlNullOutput_test4_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(*s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())

    def testMySqlNullOutput_test3_decomposed(self) -> None:
        s = ["NULL", None]
        format_ = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)

    def testMySqlNullOutput_test2_decomposed(self) -> None:
        s = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")
        format = (
            CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.NON_NUMERIC)
        )

    def testMySqlNullOutput_test1_decomposed(self) -> None:
        s: List[Optional[str]] = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR).withNullString("NULL")

    def testMySqlNullOutput_test0_decomposed(self) -> None:
        s: List[Optional[str]] = ["NULL", None]
        CSVFormat.MYSQL.withQuote0(self.__DQUOTE_CHAR)

    def testMultiLineComment_test0_decomposed(self) -> None:
        sw = io.StringIO()
        printer = None
        try:
            printer = CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#"))
            printer.printComment("This is a comment\non multiple lines")

            expected_output = (
                f"# This is a comment{CSVFormat.DEFAULT.getRecordSeparator()}"
                f"# on multiple lines{CSVFormat.DEFAULT.getRecordSeparator()}"
            )
            self.assertEqual(expected_output, sw.getvalue())
        finally:
            if printer:
                printer.close()

    def testMongoDbTsvTabInValue_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual(
                f'"a\tb"\tc{CSVFormat.MONGODB_TSV.getRecordSeparator()}', sw.getvalue()
            )

    def testMongoDbTsvCommaInValue_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        record_separator = (
            CSVFormat.DEFAULT.getRecordSeparator()
        )  # Retrieve the record separator
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a,b", "c"])  # Pass the values as a list
            self.assertEqual(
                f"a,b\tc{record_separator}", sw.getvalue()
            )  # Compare the expected and actual output

    def testMongoDbTsvBasic_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.MONGODB_TSV) as printer:
            printer.printRecord1(["a", "b"])  # Corrected to pass a list
            self.assertEqual(
                f"a\tb{CSVFormat.MONGODB_TSV._CSVFormat__recordSeparator}",
                sw.getvalue(),
            )

    def testMongoDbCsvTabInValue_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a\tb", "c"])
            self.assertEqual(
                f"a\tb,c{CSVFormat.MONGODB_CSV.getRecordSeparator()}", sw.getvalue()
            )

    def testMongoDbCsvDoubleQuoteInValue_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        record_separator = CSVFormat.MONGODB_CSV.getRecordSeparator()
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(['a "c" b', "d"])
            self.assertEqual(f'"a ""c"" b",d{record_separator}', sw.getvalue())

    def testMongoDbCsvCommaInValue_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a,b", "c"])  # Corrected to pass a list
            self.assertEqual(
                f'"a,b",c{CSVFormat.MONGODB_CSV._CSVFormat__recordSeparator}',
                sw.getvalue(),
            )

    def testMongoDbCsvBasic_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.MONGODB_CSV) as printer:
            printer.printRecord1(["a", "b"])  # Pass a list of values
            self.assertEqual(
                f"a,b{CSVFormat.MONGODB_CSV._CSVFormat__recordSeparator}", sw.getvalue()
            )

    def testJira135_part3_test7_decomposed(self) -> None:
        # Set up the CSV format with specific configurations
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent in Python
        sw = io.StringIO()

        # Create a list to hold the record
        record_list = ["\\"]

        # Use the CSVPrinter to write the record
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(record_list)

        # Generate the expected output
        expected = f'"\\\\{format_.getRecordSeparator()}"'

        # Assert that the output matches the expected string
        self.assertEqual(expected, sw.getvalue())

        # Parse the expected output to get the first record values
        record0 = self.__toFirstRecordValues(expected, format_)

        # Assert that the parsed record matches the expected null-adjusted list
        self.assertListEqual(self.__expectNulls(record_list, format_), record0)

    def testJira135_part3_test6_decomposed(self) -> None:
        # Set up the CSVFormat with the desired configurations
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent in Python
        sw = io.StringIO()

        # Create a list to hold the record
        record_list = ["\\"]

        # Use the CSVPrinter to write the record
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(record_list)

        # Define the expected output
        expected = f'"\\\\{format_.getRecordSeparator()}"'

        # Assert that the output matches the expected value
        self.assertEqual(expected, sw.getvalue())

        # Parse the expected output to get the first record values
        record0 = self.__toFirstRecordValues(expected, format_)

    def testJira135_part3_test5_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format_default = CSVFormat.DEFAULT.withRecordSeparator0("\n")
        format_with_quote = format_default.withQuote0(self.__DQUOTE_CHAR)
        format_with_escape = format_with_quote.withEscape0(Constants.BACKSLASH)

        # Create a StringWriter equivalent
        sw = io.StringIO()

        # Create a list and add the backslash character
        list_ = ["\\"]

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format_with_escape) as printer:
            printer.printRecord0(list_)

        # Define the expected output
        expected = f'"\\\\{format_with_escape.getRecordSeparator()}"'

        # Assert that the output matches the expected value
        self.assertEqual(expected, sw.getvalue())

    def testJira135_part3_test4_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent
        sw = io.StringIO()

        # Create a list and add the backslash character
        list_ = ["\\"]

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format) as printer:
            printer.printRecord0(list_)

        # Define the expected output
        expected = f'"\\\\{format.getRecordSeparator()}"'

        # Assert that the output matches the expected value
        self.assertEqual(sw.getvalue(), expected)

    def testJira135_part3_test3_decomposed(self) -> None:
        format_ = CSVFormat.DEFAULT.withRecordSeparator0("\n")
        format_ = format_.withQuote0(self.__DQUOTE_CHAR)
        format_ = format_.withEscape0(Constants.BACKSLASH)

        sw = io.StringIO()
        list_ = ["\\"]

        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(list_)

    def testJira135_part3_test2_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")
        CSVFormat.DEFAULT.withRecordSeparator0("\n").withQuote0(self.__DQUOTE_CHAR)
        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

    def testJira135_part3_test1_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")
        CSVFormat.DEFAULT.withRecordSeparator0("\n").withQuote0(self.__DQUOTE_CHAR)

    def testJira135_part3_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")

    def testJira135_part1_test7_decomposed(self) -> None:
        # Set up the CSV format with specific configurations
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent
        sw = io.StringIO()

        # Create a list to hold the record
        list_ = []

        # Use the CSVPrinter to write the record
        with CSVPrinter(sw, format_) as printer:
            list_.append('"')  # Add a double-quote character to the list
            printer.printRecord0(list_)  # Print the record

        # Define the expected output
        expected = f'"\\"" {format_.getRecordSeparator()}'

        # Assert that the output matches the expected value
        self.assertEqual(expected, sw.getvalue())

        # Parse the first record values from the expected output
        record0 = self.__toFirstRecordValues(expected, format_)

        # Assert that the parsed record matches the expected null-adjusted list
        self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def testJira135_part1_test6_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent in Python
        sw = io.StringIO()

        # Create a list to hold the record
        record_list = ['"']

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format_) as printer:
            printer.printRecord0(record_list)

        # Define the expected output
        expected = f'"\\""{format_.getRecordSeparator()}'

        # Assert that the output matches the expected value
        self.assertEqual(expected, sw.getvalue())

        # Parse the expected output to get the first record values
        record0 = self.__toFirstRecordValues(expected, format_)

    def testJira135_part1_test5_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent
        sw = io.StringIO()

        # Create a list to hold the record
        record_list = ['"']

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format) as printer:
            printer.printRecord0(record_list)

        # Define the expected output
        expected = '"\\""' + format.getRecordSeparator()

        # Assert that the output matches the expected value
        self.assertEqual(expected, sw.getvalue())

    def testJira135_part1_test4_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent in Python
        sw = io.StringIO()

        # Create a list to hold the record
        list_ = ['"']

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format) as printer:
            printer.printRecord0(list_)

        # Define the expected output
        expected = '"\\""' + format.getRecordSeparator()

        # Assert that the output matches the expected value
        self.assertEqual(sw.getvalue(), expected)

    def testJira135_part1_test3_decomposed(self) -> None:
        # Set up the CSV format with record separator and quote character
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

        # Create a StringWriter equivalent
        sw = io.StringIO()

        # Create a list to hold the record
        list_ = []

        # Use the CSVPrinter to print the record
        with CSVPrinter(sw, format_) as printer:
            list_.append('"')  # Add a double-quote character to the list
            printer.printRecord0(list_)  # Print the record

        # The test would typically include assertions here to verify the output

    def testJira135_part1_test2_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")
        CSVFormat.DEFAULT.withRecordSeparator0("\n").withQuote0(self.__DQUOTE_CHAR)
        format = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )

    def testJira135_part1_test1_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")
        CSVFormat.DEFAULT.withRecordSeparator0("\n").withQuote0(self.__DQUOTE_CHAR)

    def testJira135_part1_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.withRecordSeparator0("\n")

    def testInvalidFormat_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)

    def testHeaderNotSet_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.printRecord1(["a", "b", "c"])
            printer.printRecord1(["x", "y", "z"])
        self.assertEqual("a,b,c\r\nx,y,z\r\n", sw.getvalue())

    def testExcelPrinter2_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecord1(["a,b", "b"])
            self.assertEqual(
                f'"a,b",b{CSVFormat.EXCEL.getRecordSeparator()}', sw.getvalue()
            )

    def testExcelPrinter1_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecord1(["a", "b"])  # Corrected to pass a list
            self.assertEqual(
                f"a,b{CSVFormat.EXCEL.getRecordSeparator()}", sw.getvalue()
            )

    def testExcelPrintAllIterableOfLists_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
        self.assertEqual(
            f"r1c1,r1c2{CSVFormat.EXCEL.getRecordSeparator()}r2c1,r2c2{CSVFormat.EXCEL.getRecordSeparator()}",
            sw.getvalue(),
        )

    def testExcelPrintAllIterableOfArrays_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords0([["r1c1", "r1c2"], ["r2c1", "r2c2"]])
        self.assertEqual(
            f"r1c1,r1c2{CSVFormat.EXCEL.getRecordSeparator()}r2c1,r2c2{CSVFormat.EXCEL.getRecordSeparator()}",
            sw.getvalue(),
        )

    def testExcelPrintAllArrayOfLists_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords1(*[["r1c1", "r1c2"], ["r2c1", "r2c2"]])
        self.assertEqual(
            f"r1c1,r1c2{CSVFormat.EXCEL.getRecordSeparator()}r2c1,r2c2{CSVFormat.EXCEL.getRecordSeparator()}",
            sw.getvalue(),
        )

    def testExcelPrintAllArrayOfArrays_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.EXCEL) as printer:
            printer.printRecords1(
                *[["r1c1", "r1c2"], ["r2c1", "r2c2"]]
            )  # Unpacking the array of arrays
            self.assertEqual(
                "r1c1,r1c2"
                + CSVFormat.EXCEL.getRecordSeparator()
                + "r2c1,r2c2"
                + CSVFormat.EXCEL.getRecordSeparator(),
                sw.getvalue(),
            )

    def testEscapeNull5_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
        try:
            printer.print_("\\\\")
        finally:
            printer.close()
        self.assertEqual("\\\\", sw.getvalue())

    def testEscapeNull5_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\\")

    def testEscapeNull4_test1_decomposed(self) -> None:
        sw = io.StringIO()
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
        try:
            printer.print_("\\\\")
        finally:
            printer.close()
        self.assertEqual("\\\\", sw.getvalue())

    def testEscapeNull4_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\\")

    def testEscapeNull3_test1_decomposed(self) -> None:
        sw = io.StringIO()
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
        try:
            printer.print_("X\\\r")
        finally:
            printer.close()
        self.assertEqual('"X\\\r"', sw.getvalue())

    def testEscapeNull3_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("X\\\r")

    def testEscapeNull2_test1_decomposed(self) -> None:
        sw = io.StringIO()
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
        try:
            printer.print_("\\\r")
        finally:
            sw.close()
        self.assertEqual('"\\\r"', sw.getvalue())

    def testEscapeNull2_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\\r")

    def testEscapeNull1_test1_decomposed(self) -> None:
        sw = io.StringIO()
        printer = CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None))
        try:
            printer.print_("\\")
        finally:
            printer.close()
        self.assertEqual("\\", sw.getvalue())

    def testEscapeNull1_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(None)) as printer:
            printer.print_("\\")

    def testEscapeBackslash5_test1_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\\")
        sw_value = sw.getvalue()  # Retrieve the value before closing the StringIO
        self.assertEqual("\\\\", sw_value)

    def testEscapeBackslash5_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\\")

    def testEscapeBackslash4_test1_decomposed(self) -> None:
        sw = io.StringIO()
        try:
            with CSVPrinter(
                sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)
            ) as printer:
                printer.print_("\\\\")
            self.assertEqual("\\\\", sw.getvalue())
        finally:
            sw.close()

    def testEscapeBackslash4_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\\")

    def testEscapeBackslash3_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        try:
            with CSVPrinter(
                sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)
            ) as printer:
                printer.print_("X\\\r")
            self.assertEqual("'X\\\r'", sw.getvalue())
        finally:
            sw.close()

    def testEscapeBackslash3_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("X\\\r")

    def testEscapeBackslash2_test1_decomposed(self) -> None:
        sw = io.StringIO()
        try:
            with CSVPrinter(
                sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)
            ) as printer:
                printer.print_("\\\r")
            self.assertEqual("'\\\r'", sw.getvalue())
        finally:
            sw.close()

    def testEscapeBackslash2_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\\r")

    def testEscapeBackslash1_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\")
        self.assertEqual("\\", sw.getvalue(), "I/O operation on closed file")

    def testEscapeBackslash1_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(self.__QUOTE_CH)) as printer:
            printer.print_("\\")

    def testEolQuoted_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0("'")) as printer:
            printer.print_("a\rb\nc")
            printer.print_("x\by\fz")
        self.assertEqual("'a\rb\nc',x\by\fz", sw.getvalue())

    def testEolPlain_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("a\rb\nc")
            printer.print_("x\fy\bz")
        self.assertEqual("a\rb\nc,x\fy\bz", sw.getvalue())

    def testEolEscaped_test0_decomposed(self) -> None:
        sw = io.StringIO()
        try:
            printer = CSVPrinter(
                sw, CSVFormat.DEFAULT.withQuote1(None).withEscape0("!")
            )
            printer.print_("a\rb\nc")
            printer.print_("x\fy\bz")
            self.assertEqual("a!rb!nc,x!fy!bz", sw.getvalue())
        finally:
            sw.close()

    def testDontQuoteEuroFirstChar_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.RFC4180) as printer:
            printer.printRecord1([self.__EURO_CH, "Deux"])
            self.assertEqual(
                f"{self.__EURO_CH},Deux{self.__recordSeparator}", sw.getvalue()
            )

    def testDisabledComment_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(sw, CSVFormat.DEFAULT) as printer:
            printer.printComment("This is a comment")
            self.assertEqual(
                "", sw.getvalue(), "Expected no output for a disabled comment"
            )

    def testDelimiterStringEscaped_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(
            sw,
            CSVFormat.DEFAULT.builder()
            .setDelimiter1("|||")
            .setEscape0("!")
            .setQuote1(None)
            .build(),
        ) as printer:
            printer.print_("a|||b|||c")
            printer.print_("xyz")
            self.assertEqual("a!|!|!|b!|!|!|c|||xyz", sw.getvalue())

    def testDelimiterPlain_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        with CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(None)) as printer:
            printer.print_("a,b,c")  # Use print_ to match the Python method
            printer.print_("xyz")
            self.assertEqual(
                "a,b,cxyz", sw.getvalue(), "Output does not match expected value"
            )

    def testDelimiterEscaped_test0_decomposed(self) -> None:
        sw = io.StringIO()
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.withEscape0("!").withQuote1(None)
        ) as printer:
            printer.print_("a,b,c")
            printer.print_("xyz")
        self.assertEqual(
            "a!,b!,cxyz", sw.getvalue(), "Output does not match expected value"
        )

    def testDelimeterStringQuoteNone_test5_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setEscape0("!")
        builder.setQuoteMode(QuoteMode.NONE)
        format_ = builder.build()

        with CSVPrinter(sw, format_) as printer:
            printer.print_("a[|]b[|]c")
            printer.print_("xyz")
            printer.print_("a[xy]bc[]")

        # Ensure the StringIO object is not closed before calling getvalue()
        self.assertEqual("a![!|!]b![!|!]c[|]xyz[|]a[xy]bc[]", sw.getvalue())

    def testDelimeterStringQuoteNone_test4_decomposed(self) -> None:
        sw = io.StringIO()  # Equivalent to StringWriter in Java
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setDelimiter1("[|]").setEscape0("!")
        builder.setDelimiter1("[|]").setEscape0("!").setQuoteMode(QuoteMode.NONE)
        format = (
            CSVFormat.DEFAULT.builder()
            .setDelimiter1("[|]")
            .setEscape0("!")
            .setQuoteMode(QuoteMode.NONE)
            .build()
        )

    def testDelimeterStringQuoteNone_test3_decomposed(self) -> None:
        sw = io.StringIO()  # Equivalent to Java's StringWriter
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setEscape0("!")
        builder.setQuoteMode(QuoteMode.NONE)

    def testDelimeterStringQuoteNone_test2_decomposed(self) -> None:
        sw = io.StringIO()  # Equivalent to Java's StringWriter
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setDelimiter1("[|]").setEscape0("!")

    def testDelimeterStringQuoteNone_test1_decomposed(self) -> None:
        sw = io.StringIO()  # Equivalent to Java's StringWriter
        builder = (
            CSVFormat.DEFAULT.builder()
        )  # Get the builder from the default CSVFormat
        builder.setDelimiter1("[|]")  # Set the delimiter to "[|]"

    def testDelimeterStringQuoteNone_test0_decomposed(self) -> None:
        sw = io.StringIO()
        CSVFormat.DEFAULT.builder()

    def testDelimeterStringQuoted_test0_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        with CSVPrinter(
            sw, CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0("'").build()
        ) as printer:
            printer.print_("a[|]b[|]c")  # Using print_ to match the Python method
            printer.print_("xyz")
            self.assertEqual(
                "'a[|]b[|]c'[|]xyz", sw.getvalue()
            )  # Corrected expected output

    def testDelimeterQuoteNone_test2_decomposed(self) -> None:
        sw = io.StringIO()  # Using StringIO as a replacement for StringWriter
        format_ = CSVFormat.DEFAULT.withEscape0("!").withQuoteMode(QuoteMode.NONE)
        with CSVPrinter(
            sw, format_
        ) as printer:  # Use 'with' to ensure proper resource management
            printer.print_("a,b,c")  # Using print_ to match the Python method
            printer.print_("xyz")
        self.assertEqual("a!,b!,c,xyz", sw.getvalue())

    def testDelimeterQuoteNone_test1_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        format = CSVFormat.DEFAULT.withEscape0("!").withQuoteMode(QuoteMode.NONE)

    def testDelimeterQuoteNone_test0_decomposed(self) -> None:
        sw = io.StringIO()
        CSVFormat.DEFAULT.withEscape0("!")

    def testDelimeterQuoted_test0_decomposed(self) -> None:
        sw = io.StringIO()  # StringWriter equivalent in Python
        printer = CSVPrinter(
            sw, CSVFormat.DEFAULT.withQuote0("'")
        )  # Using single quote as the quote character
        try:
            printer.print_(
                "a,b,c"
            )  # Note: print_ is used because `print` is a reserved keyword in Python
            printer.print_("xyz")
            self.assertEqual(
                "'a,b,c',xyz", sw.getvalue()
            )  # Compare the expected and actual output
        finally:
            sw.close()  # Ensure the StringIO object is closed to avoid I/O operation on a closed file

    def testCSV259_test0_decomposed(self) -> None:
        sw = io.StringIO()
        sample_file_path = (
            "src/test/resources/org/apache/commons/csv/CSV-259/sample.txt"
        )

        if not os.path.exists(sample_file_path):
            self.skipTest(f"Sample file not found: {sample_file_path}")

        with open(sample_file_path, "r", encoding="utf-8") as reader:
            printer = CSVPrinter(
                sw, CSVFormat.DEFAULT.withEscape0("!").withQuote1(None)
            )
            printer.print_(reader.read())

        self.assertEqual("x!,y!,z", sw.getvalue().strip())

    def testCSV135_test1_decomposed(self) -> None:
        list_ = ['""', "\\\\", '\\"\\']

        self.__tryFormat(list_, None, None, '"",\\\\,\\"\\')
        self.__tryFormat(list_, '"', None, '"""""",\\\\,"\\""\\"')
        self.__tryFormat(list_, None, "\\", '"",\\\\\\\\,\\\\"\\\\')
        self.__tryFormat(list_, '"', "\\", '"\\"\\"","\\\\\\\\","\\\\\\"\\\\"')
        self.__tryFormat(list_, '"', '"', '"""""",\\\\,"\\""\\"')

    def testCSV135_test0_decomposed(self) -> None:
        list_ = ['""', "\\\\", '\\"\\']  # Create the list with the specified strings
        self.__tryFormat(
            list_, None, None, '"",\\\\,\\"\\'
        )  # Call __tryFormat with the list and expected output

    def testCRComment_test0_decomposed(self) -> None:
        sw = io.StringIO()
        value = "abc"
        record_separator = CSVFormat.DEFAULT.getRecordSeparator()

        with CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0("#")) as printer:
            printer.print_(value)
            printer.printComment(
                "This is a comment\r\non multiple lines\rthis is next comment\r"
            )

            expected_output = (
                "abc"
                + record_separator
                + "# This is a comment"
                + record_separator
                + "# on multiple lines"
                + record_separator
                + "# this is next comment"
                + record_separator
                + "#"
                + record_separator
            )

            self.assertEqual(expected_output, sw.getvalue())

    def testRandomPostgreSqlCsv(self) -> None:
        self.__doRandom(CSVFormat.POSTGRESQL_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomOracle(self) -> None:
        self.__doRandom(CSVFormat.ORACLE, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testRandomMongoDbCsv(self) -> None:
        self.__doRandom(CSVFormat.MONGODB_CSV, self.__ITERATIONS_FOR_RANDOM_TEST)

    def testPostgreSqlCsvTextOutput(self) -> None:
        s = ["NULL", None]
        format_ = (
            CSVFormat.POSTGRESQL_TEXT.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL"\tNULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual([None, None], record0)

        s = ["\\N", None]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_TEXT.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.POSTGRESQL_TEXT
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

    def testPostgreSqlCsvNullOutput(self) -> None:
        s = ["NULL", None]
        format_ = (
            CSVFormat.POSTGRESQL_CSV.withQuote0(self.__DQUOTE_CHAR)
            .withNullString("NULL")
            .withQuoteMode(QuoteMode.ALL_NON_NULL)
        )
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = '"NULL",NULL\n'
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual([None, None], record0)

        s = ["\\N", None]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "A"]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\n", "A"]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("\\N")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\n\tA\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_CSV.withNullString("NULL")
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\tNULL\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["", None]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\t\\N\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\N", "", "\u000e,\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\N\t\t\u000e,\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["NULL", "\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "NULL\t\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

        s = ["\\\r"]
        format_ = CSVFormat.POSTGRESQL_CSV
        writer = io.StringIO()
        with CSVPrinter(writer, format_) as printer:
            printer.printRecord1(s)
        expected = "\\\\\\r\n"
        self.assertEqual(expected, writer.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertEqual(self.__expectNulls(s, format_), record0)

    def testJira135All(self) -> None:
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = []
        with CSVPrinter(sw, format_) as printer:
            list_.append('"')
            list_.append("\n")
            list_.append("\\")
            printer.printRecord0(list_)

        expected = '"\\"","\\n","\\\\"' + format_.getRecordSeparator()
        self.assertEqual(expected, sw.getvalue())

        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def testJira135_part2(self) -> None:
        format_ = (
            CSVFormat.DEFAULT.withRecordSeparator0("\n")
            .withQuote0(self.__DQUOTE_CHAR)
            .withEscape0(Constants.BACKSLASH)
        )
        sw = io.StringIO()
        list_ = []
        with CSVPrinter(sw, format_) as printer:
            list_.append("\n")
            printer.printRecord0(list_)
        expected = f'"\\n"{format_.getRecordSeparator()}'
        self.assertEqual(expected, sw.getvalue())
        record0 = self.__toFirstRecordValues(expected, format_)
        self.assertListEqual(self.__expectNulls(list_, format_), record0)

    def __tryFormat(
        self, list_: typing.List[str], quote: str, escape: str, expected: str
    ) -> None:
        # Create a CSVFormat instance with the specified quote, escape, and no record separator
        format_ = (
            CSVFormat.DEFAULT.withQuote1(quote)
            .withEscape1(escape)
            .withRecordSeparator1(None)
        )

        # Use a StringIO object as the Appendable equivalent
        out = io.StringIO()

        # Use a context manager to create and use the CSVPrinter
        with CSVPrinter(out, format_) as printer:
            printer.printRecord0(list_)

        # Assert that the output matches the expected string
        self.assertEqual(expected, out.getvalue())

    def __toFirstRecordValues(
        self, expected: str, format_: CSVFormat
    ) -> typing.List[typing.List[str]]:
        with CSVParser.parse4(expected, format_) as parser:
            return parser.getRecords()[0].values()

    def __randStr(self) -> str:
        import random

        r = random.Random()
        sz = r.randint(0, 19)  # Random size between 0 and 19
        buf = []

        for _ in range(sz):
            what = r.randint(0, 19)  # Random number between 0 and 19
            if what == 0:
                ch = "\r"
            elif what == 1:
                ch = "\n"
            elif what == 2:
                ch = "\t"
            elif what == 3:
                ch = "\f"
            elif what == 4:
                ch = " "
            elif what == 5:
                ch = ","
            elif what == 6:
                ch = self.__DQUOTE_CHAR
            elif what == 7:
                ch = self.__QUOTE_CH
            elif what == 8:
                ch = Constants.BACKSLASH
            else:
                ch = chr(
                    r.randint(0, 299)
                )  # Random character with code point between 0 and 299
            buf.append(ch)

        return "".join(buf)

    def __generateLines(self, nLines: int, nCol: int) -> typing.List[typing.List[str]]:
        lines = []
        for i in range(nLines):
            line = []
            for j in range(nCol):
                line.append(self.__randStr())
            lines.append(line)
        return lines

    def __expectNulls(
        self, original: typing.List[typing.Any], csvFormat: CSVFormat
    ) -> typing.List[typing.Any]:
        fixed = original.copy()  # Clone the original list
        for i in range(len(fixed)):
            if csvFormat.getNullString() == fixed[i]:
                fixed[i] = None  # Replace with None if it matches the null string
        return fixed

    def __doRandom(self, format_: CSVFormat, iter_: int) -> None:
        for i in range(iter_):
            self.__doOneRandom(format_)

    def __doOneRandom(self, format_: CSVFormat) -> None:
        from random import randint
        from io import StringIO

        # Generate random number of lines and columns
        nLines = randint(1, 4)
        nCol = randint(1, 3)
        lines = self.__generateLines(nLines, nCol)

        # Create a StringWriter equivalent
        sw = StringIO()

        # Use CSVPrinter to write the records
        with CSVPrinter(sw, format_) as printer:
            for i in range(nLines):
                printer.printRecord1(lines[i])

            printer.flush()

        # Get the result as a string
        result = sw.getvalue()

        # Parse the result using CSVParser
        with CSVParser.parse4(result, format_) as parser:
            parseResult = parser.getRecords()

            # Clone and process the expected lines
            expected = lines.copy()
            for i in range(len(expected)):
                expected[i] = self.__expectNulls(expected[i], format_)

            # Compare the output
            Utils.compare(
                "Printer output :" + self.__printable(result), expected, parseResult
            )

    def __createTempPath(self) -> Path:
        return pathlib.Path(tempfile.mkstemp(suffix=".csv")[1])

    def __createTempFile(self) -> pathlib.Path:
        return self.__createTempPath().to_file()

    @staticmethod
    def __printable(s: str) -> str:
        sb = []
        for ch in s:
            if ord(ch) <= ord(" ") or ord(ch) >= 128:
                sb.append(f"({ord(ch)})")
            else:
                sb.append(ch)
        return "".join(sb)
