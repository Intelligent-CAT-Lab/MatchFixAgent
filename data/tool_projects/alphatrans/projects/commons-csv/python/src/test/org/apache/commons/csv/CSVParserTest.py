from __future__ import annotations
import time
import re
from io import StringIO
import unittest
import pytest
import pathlib
import io
import numbers
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVPrinter import *
from src.main.org.apache.commons.csv.CSVRecord import *
from src.main.org.apache.commons.csv.Constants import *
from src.test.org.apache.commons.csv.Utils import *


class CSVParserTest(unittest.TestCase):

    __CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT: str = (
        "# multi-line"
        + Constants.CRLF
        + "# header comment"
        + Constants.CRLF
        + "A,B"
        + Constants.CRLF
        + "1,2"
        + Constants.CRLF
        + "# multi-line"
        + Constants.CRLF
        + "# comment"
        if Constants.CRLF is not None
        else ""
    )

    __CSV_INPUT_HEADER_TRAILER_COMMENT: str = None  # LLM could not translate this field

    __CSV_INPUT_HEADER_COMMENT: str = None  # LLM could not translate this field

    __CSV_INPUT_NO_COMMENT: str = "A,B" + "\r\n" + "1,2" + "\r\n"
    __RESULT: typing.List[typing.List[str]] = [
        ["a", "b", "c", "d"],
        ["a", "b", "1 2"],
        ["foo baar", "b", ""],
        ['foo\n,,\n",,\n"', "d", "e"],
    ]
    __CSV_INPUT_2: str = "a,b,1 2"
    __CSV_INPUT_1: str = "a,b,c,d"
    __CSV_INPUT: str = (
        "a,b,c,d\n" " a , b , 1 2 \n" '"foo baar", b,\n' '   "foo\n,,\n"",,\n""",d,e\n'
    )
    __UTF_8: str = "utf-8"

    def testStream_test0_decomposed(self) -> None:
        in_reader = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        with CSVFormat.DEFAULT.parse(in_reader) as parser:
            record_list = list(parser.stream())
            self.assertFalse(len(record_list) == 0)  # Check that the list is not empty
            self.assertEqual(
                ["a", "b", "c"], record_list[0].values()
            )  # Check first record
            self.assertEqual(
                ["1", "2", "3"], record_list[1].values()
            )  # Check second record
            self.assertEqual(
                ["x", "y", "z"], record_list[2].values()
            )  # Check third record

    def testRoundtrip_test0_decomposed(self) -> None:
        out = io.StringIO()
        data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n"
        with CSVPrinter(out, CSVFormat.DEFAULT) as printer, CSVParser.parse4(
            data, CSVFormat.DEFAULT
        ) as parse:
            for record in parse:
                printer.printRecord0(record)
            self.assertEqual(data, out.getvalue())

    def testParseWithQuoteWithEscape_test2_decomposed(self) -> None:
        source = "'a?,b?,c?d',xyz"
        csv_format = CSVFormat.DEFAULT.withQuote0("'").withEscape0("?")
        with io.StringIO(source) as reader:
            csv_parser = csv_format.parse(reader)
            csv_record = csv_parser.nextRecord()
            self.assertEqual("a,b,c?d", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

    def testParseWithQuoteWithEscape_test1_decomposed(self) -> None:
        source = "'a?,b?,c?d',xyz"
        csv_format = CSVFormat.DEFAULT.withQuote0("'").withEscape0("?")

    def testParseWithQuoteWithEscape_test0_decomposed(self) -> None:
        source = "'a?,b?,c?d',xyz"
        CSVFormat.DEFAULT.withQuote0("'")

    def testParseWithQuoteThrowsException_test1_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT.withQuote0("'")

        with self.assertRaises(IOError):
            csv_format.parse(io.StringIO("'a,b,c','")).next()

        with self.assertRaises(IOError):
            csv_format.parse(io.StringIO("'a,b,c'abc,xyz")).next()

        with self.assertRaises(IOError):
            csv_format.parse(io.StringIO("'abc'a,b,c',xyz")).next()

    def testParseWithQuoteThrowsException_test0_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT.withQuote0("'")

    def testParseWithDelimiterWithQuote_test1_decomposed(self) -> None:
        source = "'a,b,c',xyz"
        csv_format = CSVFormat.DEFAULT.withQuote0("'")
        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertEqual("a,b,c", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

    def testParseWithDelimiterWithQuote_test0_decomposed(self) -> None:
        source = "'a,b,c',xyz"
        csv_format = CSVFormat.DEFAULT.withQuote0("'")

    def testParseWithDelimiterWithEscape_test1_decomposed(self) -> None:
        source = "a!,b!,c,xyz"
        csv_format = CSVFormat.DEFAULT.withEscape0("!")
        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertEqual("a,b,c", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

    def testParseWithDelimiterWithEscape_test0_decomposed(self) -> None:
        source = "a!,b!,c,xyz"
        csv_format = CSVFormat.DEFAULT.withEscape0("!")

    def testParseWithDelimiterStringWithQuote_test4_decomposed(self) -> None:
        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setQuote0("'")
        csv_format = builder.build()

        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertEqual("a[|]b[|]c", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

            csv_record = csv_parser.nextRecord()
            self.assertEqual("abc[abc]", csv_record.get1(0))
            self.assertEqual("xyz", csv_record.get1(1))

    def testParseWithDelimiterStringWithQuote_test3_decomposed(self) -> None:
        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setDelimiter1("[|]").setQuote0("'")
        csv_format = builder.setDelimiter1("[|]").setQuote0("'").build()

    def testParseWithDelimiterStringWithQuote_test2_decomposed(self) -> None:
        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setDelimiter1("[|]").setQuote0("'")

    def testParseWithDelimiterStringWithQuote_test1_decomposed(self) -> None:
        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")

    def testParseWithDelimiterStringWithQuote_test0_decomposed(self) -> None:
        source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz"
        CSVFormat.DEFAULT.builder()

    def testParseWithDelimiterStringWithEscape_test4_decomposed(self) -> None:
        source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setEscape0("!")
        csvFormat = builder.build()

        with csvFormat.parse(io.StringIO(source)) as csvParser:
            csvRecord = csvParser.nextRecord()
            self.assertEqual("a[|]b![|]c", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

            csvRecord = csvParser.nextRecord()
            self.assertEqual("abc[abc]", csvRecord.get1(0))
            self.assertEqual("xyz", csvRecord.get1(1))

    def testParseWithDelimiterStringWithEscape_test3_decomposed(self) -> None:
        source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setEscape0("!")
        csv_format = builder.setDelimiter1("[|]").setEscape0("!").build()

    def testParseWithDelimiterStringWithEscape_test2_decomposed(self) -> None:
        source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")
        builder.setDelimiter1("[|]").setEscape0("!")

    def testParseWithDelimiterStringWithEscape_test1_decomposed(self) -> None:
        source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        builder = CSVFormat.DEFAULT.builder()
        builder.setDelimiter1("[|]")

    def testParseWithDelimiterStringWithEscape_test0_decomposed(self) -> None:
        source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz"
        CSVFormat.DEFAULT.builder()

    def testParseUrlCharsetNullFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(
                URL("https://commons.apache.org"), Charset.defaultCharset(), None
            )

    def testParseStringNullFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse4("csv data", None)

    def testParserUrlNullCharsetFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(URL("https://commons.apache.org"), None, CSVFormat.DEFAULT)

    def testParseNullUrlCharsetFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse5(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullStringFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse4(None, CSVFormat.DEFAULT)

    def testParseNullPathFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse2(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseNullFileFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse0(None, Charset.defaultCharset(), CSVFormat.DEFAULT)

    def testParseFileNullFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.parse0(
                pathlib.Path("CSVFileParser/test.csv"),
                os.fsdecode(os.path.getdefaultencoding()),
                None,
            )

    def testNotValueCSV_test1_decomposed(self) -> None:
        source = "#"
        csv_format = CSVFormat.DEFAULT.withCommentMarker0("#")
        with csv_format.parse(io.StringIO(source)) as csv_parser:
            csv_record = csv_parser.nextRecord()
            self.assertIsNone(csv_record)

    def testNotValueCSV_test0_decomposed(self) -> None:
        source: str = "#"
        csv_format: CSVFormat = CSVFormat.DEFAULT.withCommentMarker0("#")

    def testNoHeaderMap_test0_decomposed(self) -> None:
        with CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.getHeaderMap())

    def testNewCSVParserReaderNullFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.CSVParser1(io.StringIO(""), None)

    def testNewCSVParserNullReaderFormat_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CSVParser.CSVParser1(None, CSVFormat.DEFAULT)

    def testMultipleIterators_test0_decomposed(self) -> None:
        with CSVParser.parse4(
            "a,b,c" + Constants.CRLF + "d,e,f", CSVFormat.DEFAULT
        ) as parser:
            itr1 = parser.iterator()

            first = next(itr1)
            self.assertEqual("a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = next(itr1)
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    def testLineFeedEndings_test0_decomposed(self) -> None:
        code = "foo\nbaar,\nhello,world\n,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testIteratorSequenceBreaking_test2_decomposed(self) -> None:
        five_rows = "1\n2\n3\n4\n5\n"

        # First try block
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            iter = parser.iterator()
            record_number = 0
            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break
            iter.hasNext()
            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

        # Second try block
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

        # Third try block
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break
            parser.iterator().hasNext()
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

    def testIteratorSequenceBreaking_test1_decomposed(self) -> None:
        five_rows = "1\n2\n3\n4\n5\n"

        # First try block equivalent
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            iter = parser.iterator()
            record_number = 0
            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break

            iter.hasNext()  # This is just a call, no assertion or effect

            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

        # Second try block equivalent
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            record_number = 0
            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break

            for record in parser:
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

    def testIteratorSequenceBreaking_test0_decomposed(self) -> None:
        five_rows = "1\n2\n3\n4\n5\n"
        with CSVFormat.DEFAULT.parse(io.StringIO(five_rows)) as parser:
            iter = parser.iterator()
            record_number = 0
            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))
                if record_number >= 2:
                    break
            iter.hasNext()
            while iter.hasNext():
                record = iter.next()
                record_number += 1
                self.assertEqual(str(record_number), record.get1(0))

    def testIterator_test0_decomposed(self) -> None:
        in_reader = io.StringIO("a,b,c\n1,2,3\nx,y,z")
        with CSVFormat.DEFAULT.parse(in_reader) as parser:
            iterator = parser.iterator()

            self.assertTrue(iterator.hasNext())
            with self.assertRaises(NotImplementedError):
                iterator.remove()
            self.assertEqual(["a", "b", "c"], iterator.next().values())
            self.assertEqual(["1", "2", "3"], iterator.next().values())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertTrue(iterator.hasNext())
            self.assertEqual(["x", "y", "z"], iterator.next().values())
            self.assertFalse(iterator.hasNext())

            with self.assertRaises(RuntimeError):
                iterator.next()

    def testInvalidFormat_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):  # Equivalent to ValueError in Java
            CSVFormat.DEFAULT.withDelimiter(Constants.CR)

    def testIgnoreEmptyLines_test0_decomposed(self) -> None:
        code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(3, len(records))

    def testGetRecordWithMultiLineValues_test0_decomposed(self) -> None:
        with CSVParser.parse4(
            '"a\r\n1","a\r\n2"'
            + Constants.CRLF
            + '"b\r\n1","b\r\n2"'
            + Constants.CRLF
            + '"c\r\n1","c\r\n2"',
            CSVFormat.DEFAULT.withRecordSeparator1(Constants.CRLF),
        ) as parser:
            record = None
            self.assertEqual(0, parser.getRecordNumber())
            self.assertEqual(0, parser.getCurrentLineNumber())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(3, parser.getCurrentLineNumber())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(6, parser.getCurrentLineNumber())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())

            record = parser.nextRecord()
            self.assertIsNotNone(record)
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())

            record = parser.nextRecord()
            self.assertIsNone(record)
            self.assertEqual(9, parser.getCurrentLineNumber())
            self.assertEqual(3, parser.getRecordNumber())

    def testGetRecords_test0_decomposed(self) -> None:
        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            records = parser.getRecords()
            self.assertEqual(len(self.__RESULT), len(records))
            self.assertFalse(
                len(records) == 0
            )  # Equivalent to assertFalse(records.isEmpty())
            for i in range(len(self.__RESULT)):
                self.assertEqual(self.__RESULT[i], records[i].values())

    def testGetRecordPositionWithLF_test1_decomposed(self) -> None:
        self.__validateRecordPosition(Constants.LF)

    def testGetRecordPositionWithLF_test0_decomposed(self) -> None:
        str(Constants.LF)

    def testGetRecordPositionWithCRLF_test0_decomposed(self) -> None:
        self.__validateRecordPosition(Constants.CRLF)

    def testGetRecordNumberWithLF_test1_decomposed(self) -> None:
        self.__validateRecordNumbers(Constants.LF)

    def testGetRecordNumberWithLF_test0_decomposed(self) -> None:
        str(Constants.LF)

    def testGetRecordNumberWithCRLF_test0_decomposed(self) -> None:
        self.__validateRecordNumbers(Constants.CRLF)

    def testGetRecordNumberWithCR_test1_decomposed(self) -> None:
        str(Constants.CR)  # Equivalent to String.valueOf(CR) in Java
        self.__validateRecordNumbers(
            str(Constants.CR)
        )  # Call the validateRecordNumbers method

    def testGetRecordNumberWithCR_test0_decomposed(self) -> None:
        str(Constants.CR)

    def testGetOneLineOneParser_test0_decomposed(self) -> None:
        format_ = CSVFormat.DEFAULT
        with io.StringIO() as writer:
            # Write the first CSV input
            writer.write(self.__CSV_INPUT_1)
            writer.seek(0)  # Reset the writer's position to the beginning

            # Create a CSVParser instance using the writer as input
            parser = CSVRecord.CSVParser1(writer, format_)

            # Process the first record
            record1 = parser.nextRecord()
            self.assertEqual(self.__RESULT[0], record1.values())

            # Write the second CSV input
            writer.seek(0)
            writer.truncate(0)  # Clear the writer
            writer.write(self.__CSV_INPUT_2)
            writer.seek(0)  # Reset the writer's position to the beginning

            # Process the second record
            record2 = parser.nextRecord()
            self.assertEqual(self.__RESULT[1], record2.values())

    def testGetOneLine_test0_decomposed(self) -> None:
        with CSVParser.parse4(self.__CSV_INPUT_1, CSVFormat.DEFAULT) as parser:
            record = parser.getRecords()[0]
            self.assertEqual(self.__RESULT[0], record.values())

    def testGetLineNumberWithLF_test1_decomposed(self) -> None:
        str(Constants.LF)  # Equivalent to String.valueOf(LF) in Java
        self.__validateLineNumbers(
            str(Constants.LF)
        )  # Call the validateLineNumbers method

    def testGetLineNumberWithLF_test0_decomposed(self) -> None:
        str(Constants.LF)

    def testGetLineNumberWithCRLF_test0_decomposed(self) -> None:
        self.__validateLineNumbers(Constants.CRLF)

    def testGetLineNumberWithCR_test1_decomposed(self) -> None:
        self.__validateLineNumbers(Constants.CR)

    def testGetLineNumberWithCR_test0_decomposed(self) -> None:
        str(Constants.CR)

    def testGetLine_test0_decomposed(self) -> None:
        with CSVParser.parse4(
            self.__CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0()
        ) as parser:
            for expected_row in self.__RESULT:
                self.assertEqual(expected_row, parser.nextRecord().values())

            self.assertIsNone(parser.nextRecord())

    def testForEach_test0_decomposed(self) -> None:
        with io.StringIO("a,b,c\n1,2,3\nx,y,z") as in_stream:
            parser = CSVFormat.DEFAULT.parse(in_stream)
            records = []
            for record in parser:
                records.append(record)

            self.assertEqual(3, len(records))
            self.assertEqual(["a", "b", "c"], records[0].values())
            self.assertEqual(["1", "2", "3"], records[1].values())
            self.assertEqual(["x", "y", "z"], records[2].values())

    def testFirstEndOfLineLf_test0_decomposed(self) -> None:
        data = "foo\nbaar,\nhello,world\n,kanu"
        parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
        try:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\n", parser.getFirstEndOfLine())
        finally:
            parser.close()

    def testFirstEndOfLineCrLf_test0_decomposed(self) -> None:
        data = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
        with parser:  # Using the parser as a context manager
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r\n", parser.getFirstEndOfLine())

    def testFirstEndOfLineCr_test0_decomposed(self) -> None:
        data = "foo\rbaar,\rhello,world\r,kanu"
        parser = CSVParser.parse4(data, CSVFormat.DEFAULT)
        try:
            records = parser.getRecords()
            self.assertEqual(4, len(records))
            self.assertEqual("\r", parser.getFirstEndOfLine())
        finally:
            parser.close()

    def testExcelFormat2_test0_decomposed(self) -> None:
        code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n"
        res = [["foo", "baar"], [""], ["hello", ""], [""], ["world", ""]]

        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())

            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testExcelFormat1_test0_decomposed(self) -> None:
        code = (
            "value1,value2,value3,value4\r\na,b,c,d\r\n  x,,,"
            + '\r\n\r\n"""hello""","  ""world""","abc\ndef",\r\n'
        )
        res = [
            ["value1", "value2", "value3", "value4"],
            ["a", "b", "c", "d"],
            ["  x", "", "", ""],
            [""],
            ['"hello"', '  "world"', "abc\ndef", ""],
        ]

        with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(
                len(records) == 0
            )  # Equivalent to assertFalse(records.isEmpty())
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def testEndOfFileBehaviorExcel_test0_decomposed(self) -> None:
        codes = [
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\r\n',
            'hello,\r\n\r\nworld,""',
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\n',
            'hello,\r\n\r\nworld,""',
        ]
        res = [
            ["hello", ""],
            [""],  # Excel format does not ignore empty lines
            ["world", ""],
        ]
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(
                    not records
                )  # Equivalent to assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

    def testEndOfFileBehaviorCSV_test0_decomposed(self) -> None:
        codes = [
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\r\n',
            'hello,\r\n\r\nworld,""',
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            'hello,\r\n\r\nworld,""\n',
            'hello,\r\n\r\nworld,""',
        ]
        res = [["hello", ""], ["world", ""]]  # CSV format ignores empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(
                    not records
                )  # Equivalent to assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

    def testEmptyString_test0_decomposed(self) -> None:
        with CSVParser.parse4("", CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.nextRecord())

    def testEmptyLineBehaviorExcel_test0_decomposed(self) -> None:
        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(
                    not records
                )  # Equivalent to assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

    def testEmptyLineBehaviorCSV_test0_decomposed(self) -> None:
        codes = [
            "hello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""]]  # CSV format ignores empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(
                    not records
                )  # Equivalent to assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

    def testEmptyFile_test0_decomposed(self) -> None:
        path = pathlib.Path("src/test/resources/org/apache/commons/csv/empty.txt")
        with CSVParser.parse2(path, self.__UTF_8, CSVFormat.DEFAULT) as parser:
            self.assertIsNone(parser.nextRecord())

    def testDefaultFormat_test2_decomposed(self) -> None:
        code = (
            "a,b#\n"  # 1)
            + '"\n"," ",#\n'  # 2)
            + '#,""\n'  # 3)
            + "# Final comment\n"  # 4)
        )
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]
        format_ = CSVFormat.DEFAULT
        self.assertFalse(format_.isCommentMarkerSet())
        res_comments = [
            ["a", "b#"],
            ["\n", " ", "#"],
        ]

        # Parsing without comments
        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            self.assertFalse(len(records) == 0)  # Check records are not empty
            Utils.compare("Failed to parse without comments", res, records)

            # Update format to include comment marker
            format_ = CSVFormat.DEFAULT.withCommentMarker0("#")

        # Parsing with comments
        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            Utils.compare("Failed to parse with comments", res_comments, records)

    def testDefaultFormat_test1_decomposed(self) -> None:
        code = (
            "a,b#\n"  # 1)
            + '"\n"," ",#\n'  # 2)
            + '#,""\n'  # 3)
            + "# Final comment\n"  # 4)
        )
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]
        format_ = CSVFormat.DEFAULT
        self.assertFalse(format_.isCommentMarkerSet())
        res_comments = [
            ["a", "b#"],
            ["\n", " ", "#"],
        ]
        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            self.assertFalse(
                not records
            )  # Equivalent to assertFalse(records.isEmpty())

            Utils.compare("Failed to parse without comments", res, records)

            format_ = CSVFormat.DEFAULT.withCommentMarker0("#")

    def testDefaultFormat_test0_decomposed(self) -> None:
        code = (
            "a,b#\n"  # 1)
            + '"\n"," ",#\n'  # 2)
            + '#,""\n'  # 3)
            + "# Final comment\n"  # 4)
        )
        res = [["a", "b#"], ["\n", " ", "#"], ["#", ""], ["# Final comment"]]
        format = CSVFormat.DEFAULT
        self.assertFalse(
            format.isCommentMarkerSet(), "Expected comment marker to not be set"
        )

    def testCSV57_test0_decomposed(self) -> None:
        with CSVParser.parse4("", CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertIsNotNone(records)
            self.assertEqual(0, len(records))

    def testCSV235_test0_decomposed(self) -> None:
        dq_string = '"aaa","b""bb","ccc"'
        with CSVFormat.RFC4180.parse(io.StringIO(dq_string)) as parser:
            records = parser.iterator()
            record = next(records)
            self.assertFalse(next(records, None))  # Check if there are no more records
            self.assertEqual(3, record.size())
            self.assertEqual("aaa", record.get1(0))
            self.assertEqual('b"bb', record.get1(1))
            self.assertEqual("ccc", record.get1(2))

    def testCSV141RFC4180_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.RFC4180, 3)

    def testCSV141CSVFormat_POSTGRESQL_CSV_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.POSTGRESQL_CSV, 3)

    def testCSV141CSVFormat_ORACLE_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.ORACLE, 2)

    def testCSV141CSVFormat_INFORMIX_UNLOAD_CSV_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3)

    def testCSV141CSVFormat_INFORMIX_UNLOAD_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1)

    def testCSV141CSVFormat_DEFAULT_test0_decomposed(self) -> None:
        self.__testCSV141Failure(CSVFormat.DEFAULT, 3)

    def testCarriageReturnLineFeedEndings_test0_decomposed(self) -> None:
        code = "foo\r\nbaar,\r\nhello,world\r\n,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testCarriageReturnEndings_test0_decomposed(self) -> None:
        code = "foo\rbaar,\rhello,world\r,kanu"
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(4, len(records))

    def testBackslashEscaping2_test4_decomposed(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]

        # Create the CSVFormat object with the specified configurations
        format_ = (
            CSVFormat.newFormat(",")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        # Parse the code using the format
        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            self.assertFalse(not records)  # Assert that records is not empty

            # Compare the parsed records with the expected result
            Utils.compare("", res, records)

    def testBackslashEscaping2_test3_decomposed(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]
        format = (
            CSVFormat.newFormat(",")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

    def testBackslashEscaping2_test2_decomposed(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]
        CSVFormat.newFormat(",")
        CSVFormat.newFormat(",").withRecordSeparator1(Constants.CRLF)
        CSVFormat.newFormat(",").withRecordSeparator1(Constants.CRLF).withEscape0("/")

    def testBackslashEscaping2_test1_decomposed(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]
        format = CSVFormat.newFormat(",")
        format = format.withRecordSeparator1(Constants.CRLF)

    def testBackslashEscaping2_test0_decomposed(self) -> None:
        code = (
            " , , \n"  # 1)
            " \t ,  , \n"  # 2)
            " // , /, , /,\n"  # 3)
        )
        res = [
            [" ", " ", " "],  # 1
            [" \t ", "  ", " "],  # 2
            [" / ", " , ", " ,"],  # 3
        ]
        CSVFormat.newFormat(",")

    def testBackslashEscaping_test5_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]

        # Create the CSVFormat with the specified options
        format_ = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

        # Parse the CSV data
        with CSVParser.parse4(code, format_) as parser:
            records = parser.getRecords()
            self.assertFalse(not records, "Records should not be empty")

            # Compare the parsed records with the expected result
            Utils.compare("Records do not match expected result", res, records)

    def testBackslashEscaping_test4_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]
        CSVFormat.newFormat(",")
        CSVFormat.newFormat(",").withQuote0("'")
        CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(Constants.CRLF)
        format = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
            .withIgnoreEmptyLines0()
        )

    def testBackslashEscaping_test3_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]
        format = (
            CSVFormat.newFormat(",")
            .withQuote0("'")
            .withRecordSeparator1(Constants.CRLF)
            .withEscape0("/")
        )
        parser = CSVParser(code, format)
        records = list(parser)
        self.assertEqual(len(records), len(res))
        for record, expected in zip(records, res):
            self.assertEqual(record, expected)

    def testBackslashEscaping_test2_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]
        CSVFormat.newFormat(",")
        CSVFormat.newFormat(",").withQuote0("'")
        CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(Constants.CRLF)

    def testBackslashEscaping_test1_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]
        csv_format = CSVFormat.newFormat(",")
        csv_format = csv_format.withQuote0("'")

    def testBackslashEscaping_test0_decomposed(self) -> None:
        code = (
            "one,two,three\n"  # 0
            + "'',''\n"  # 1) empty encapsulators
            + "/',/'\n"  # 2) single encapsulators
            + "'/'','/''\n"  # 3) single encapsulators encapsulated via escape
            + "'''',''''\n"  # 4) single encapsulators encapsulated via doubling
            + "/,,/,\n"  # 5) separator escaped
            + "//,//\n"  # 6) escape escaped
            + "'//','//'\n"  # 7) escape escaped in encapsulation
            + '   8   ,   "quoted "" /" // string"   \n'  # don't eat spaces
            + "9,   /\n   \n"  # escaped newline
        )
        res = [
            ["one", "two", "three"],  # 0
            ["", ""],  # 1
            ["'", "'"],  # 2
            ["'", "'"],  # 3
            ["'", "'"],  # 4
            [",", ","],  # 5
            ["/", "/"],  # 6
            ["/", "/"],  # 7
            ["   8   ", '   "quoted "" /" / string"   '],
            ["9", "   \n   "],
        ]
        CSVFormat.newFormat(",")

    def testStartWithEmptyLinesThenHeaders(self) -> None:
        codes = [
            "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            'hello,""\r\n\r\n\r\n',
            'hello,""\n\n\n',
        ]
        res = [["hello", ""], [""], [""]]  # Excel format does not ignore empty lines
        for code in codes:
            with CSVParser.parse4(code, CSVFormat.EXCEL) as parser:
                records = parser.getRecords()
                self.assertEqual(len(res), len(records))
                self.assertFalse(
                    not records
                )  # Equivalent to assertFalse(records.isEmpty())
                for i in range(len(res)):
                    self.assertEqual(res[i], records[i].values())

    def testMongoDbCsv(self) -> None:
        with CSVParser.parse4(
            '"a a",b,c' + Constants.LF + "d,e,f", CSVFormat.MONGODB_CSV
        ) as parser:
            itr1 = parser.iterator()
            itr2 = parser.iterator()

            first = next(itr1)
            self.assertEqual("a a", first.get1(0))
            self.assertEqual("b", first.get1(1))
            self.assertEqual("c", first.get1(2))

            second = next(itr2)
            self.assertEqual("d", second.get1(0))
            self.assertEqual("e", second.get1(1))
            self.assertEqual("f", second.get1(2))

    def testCSV141Excel(self) -> None:
        self.__testCSV141Ok(CSVFormat.EXCEL)

    def testBackslashEscapingOld(self) -> None:
        code = (
            "one,two,three\n"
            'on\\"e,two\n'
            'on"e,two\n'
            'one,"tw\\"o"\n'
            'one,"t\\,wo"\n'
            'one,two,"th,ree"\n'
            '"a\\\\"\n'
            "a\\,b\n"
            '"a\\\\,b"'
        )
        res = [
            ["one", "two", "three"],
            ['on\\"e', "two"],
            ['on"e', "two"],
            ["one", 'tw"o'],
            ["one", "t\\,wo"],  # backslash in quotes only
            ["one", "two", "th,ree"],
            ["a\\\\"],  # backslash in quotes only escapes a delimiter (",")
            ["a\\", "b"],  # a backslash must be returned
            ["a\\\\,b"],  # backslash in quotes only escapes a delimiter (",")
        ]
        with CSVParser.parse4(code, CSVFormat.DEFAULT) as parser:
            records = parser.getRecords()
            self.assertEqual(len(res), len(records))
            self.assertFalse(len(records) == 0)
            for i in range(len(res)):
                self.assertEqual(res[i], records[i].values())

    def __validateRecordPosition(self, lineSeparator: str) -> None:
        nl = lineSeparator  # used as linebreak in values for better distinction

        code = (
            "a,b,c"
            + lineSeparator
            + "1,2,3"
            + lineSeparator
            + "'A"
            + nl
            + "A','B"
            + nl
            + "B',CC"
            + lineSeparator
            + "\u00c4,\u00d6,\u00dc"
            + lineSeparator
            + "EOF,EOF,EOF"
        )

        format_ = (
            CSVFormat.newFormat(",").withQuote0("'").withRecordSeparator1(lineSeparator)
        )
        parser = CSVFormat.parse4(code, format_)

        record = None
        self.assertEqual(0, parser.getRecordNumber())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(1, record.getRecordNumber())
        self.assertEqual(code.index("a"), record.getCharacterPosition())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(2, record.getRecordNumber())
        self.assertEqual(code.index("1"), record.getCharacterPosition())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        positionRecord3 = record.getCharacterPosition()
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + lineSeparator + "A", record.get1(0))
        self.assertEqual("B" + lineSeparator + "B", record.get1(1))
        self.assertEqual("CC", record.get1(2))

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(4, record.getRecordNumber())
        self.assertEqual(code.index("\u00c4"), record.getCharacterPosition())

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(5, record.getRecordNumber())
        self.assertEqual(code.index("EOF"), record.getCharacterPosition())

        parser.close()

        parser = CSVParser(
            io.StringIO(code[positionRecord3:]), format_, positionRecord3, 3
        )

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(3, record.getRecordNumber())
        self.assertEqual(code.index("'A"), record.getCharacterPosition())
        self.assertEqual("A" + lineSeparator + "A", record.get1(0))
        self.assertEqual("B" + lineSeparator + "B", record.get1(1))
        self.assertEqual("CC", record.get1(2))

        record = parser.nextRecord()
        self.assertIsNotNone(record)
        self.assertEqual(4, record.getRecordNumber())
        self.assertEqual(code.index("\u00c4"), record.getCharacterPosition())
        self.assertEqual("\u00c4", record.get1(0))

        parser.close()

    def __validateRecordNumbers(self, lineSeparator: str) -> None:
        with CSVParser.parse4(
            f"a{lineSeparator}b{lineSeparator}c",
            CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
        ) as parser:
            record = None
            self.assertEqual(0, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(1, record.getRecordNumber())
            self.assertEqual(1, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(2, record.getRecordNumber())
            self.assertEqual(2, parser.getRecordNumber())
            self.assertIsNotNone(record := parser.nextRecord())
            self.assertEqual(3, record.getRecordNumber())
            self.assertEqual(3, parser.getRecordNumber())
            self.assertIsNone(record := parser.nextRecord())
            self.assertEqual(3, parser.getRecordNumber())

    def __validateLineNumbers(self, lineSeparator: str) -> None:
        with CSVParser.parse4(
            f"a{lineSeparator}b{lineSeparator}c",
            CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator),
        ) as parser:
            self.assertEqual(0, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(1, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(2, parser.getCurrentLineNumber())
            self.assertIsNotNone(parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())
            self.assertIsNone(parser.nextRecord())
            self.assertEqual(3, parser.getCurrentLineNumber())

    def __testCSV141Ok(self, format_: CSVFormat) -> None:
        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format_) as parser:
            record = parser.nextRecord()
            self.assertEqual("1414770317901", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _8", record.get1(4))
            self.assertEqual(5, record.size())

            record = parser.nextRecord()
            self.assertEqual("1414770318470", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84:|", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _84:\\", record.get1(4))
            self.assertEqual(5, record.size())

            record = parser.nextRecord()
            self.assertEqual("1414770318327", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1", record.get1(2))
            self.assertEqual(3, record.size())

            record = parser.nextRecord()
            self.assertEqual("1414770318628", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1", record.get1(4))
            self.assertEqual(5, record.size())

    def __testCSV141Failure(self, format_: CSVFormat, failParseRecordNo: int) -> None:
        path = pathlib.Path(
            "src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv"
        )
        with CSVParser.parse2(path, self.__UTF_8, format_) as parser:
            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure

            self.assertEqual("1414770317901", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84*|*", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _8", record.get1(4))
            self.assertEqual(5, record.size())

            record = self.parse(parser, failParseRecordNo)
            if record is None:
                return  # expected failure

            self.assertEqual("1414770318470", record.get1(0))
            self.assertEqual("android.widget.EditText", record.get1(1))
            self.assertEqual("pass sem1 _84:|", record.get1(2))
            self.assertEqual("0", record.get1(3))
            self.assertEqual("pass sem1 _84:\\", record.get1(4))
            self.assertEqual(5, record.size())

            with pytest.raises(OSError):
                parser.nextRecord()

    def __parseFully(self, parser: CSVParser) -> None:
        for record in parser:
            self.assertIsNotNone(record)

    def parse(self, parser: CSVParser, failParseRecordNo: int) -> CSVRecord:
        if parser.getRecordNumber() + 1 == failParseRecordNo:
            with pytest.raises(IOError):
                parser.nextRecord()
            return None
        return parser.nextRecord()
