from __future__ import annotations
import time
import re
import urllib
import datetime
import pathlib
import unittest
import pytest
import io
import numbers
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.PosixParser import *


class PatternOptionBuilderTest(unittest.TestCase):

    def testURLPattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("u/v/")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"],
        )
        self.assertEqual(
            "u value",
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("u"),
        )
        self.assertIsNone(line.getOptionObject1("v"), "v value")

    def testURLPattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("u/v/")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"],
        )

    def testURLPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("u/v/")
        parser = PosixParser()

    def testURLPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("u/v/")

    def testUntypedPattern_test8_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"), "value a")

        self.assertTrue(line.hasOption0("b"))
        self.assertIsNone(line.getOptionObject0("b"), "value b")

        self.assertTrue(line.hasOption0("c"))
        self.assertIsNone(line.getOptionObject0("c"), "value c")

    def testUntypedPattern_test7_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"), "value a")

        self.assertTrue(line.hasOption0("b"))
        self.assertIsNone(line.getOptionObject0("b"), "value b")

        self.assertTrue(line.hasOption0("c"))

    def testUntypedPattern_test6_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"), "value a")
        self.assertTrue(line.hasOption0("b"))
        self.assertIsNone(line.getOptionObject0("b"), "value b")

    def testUntypedPattern_test5_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])
        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"), "value a")
        self.assertTrue(line.hasOption0("b"))

    def testUntypedPattern_test4_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])
        self.assertTrue(line.hasOption0("a"))
        self.assertIsNone(line.getOptionObject0("a"), "value a")

    def testUntypedPattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])
        self.assertTrue(line.hasOption0("a"))

    def testUntypedPattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()
        line = parser.parse0(options, ["-abc"])

    def testUntypedPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")
        parser = PosixParser()

    def testUntypedPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("abc")

    def testSimplePattern_test10_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")
        self.assertEqual(
            pathlib.Path("build.xml"), line.getOptionObject1("e"), "file flag e"
        )
        self.assertEqual(
            Calendar, line.getOptionObject1("f"), "class flag f"
        )  # Assuming Calendar is imported
        self.assertEqual(4.5, line.getOptionObject1("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("t"),
            "url flag t",
        )
        self.assertEqual("foo", line.getOptionValue0("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject0("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject0("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption0("c"), "boolean true flag c")
        self.assertFalse(line.hasOption0("d"), "boolean false flag d")
        self.assertEqual(
            pathlib.Path("build.xml"), line.getOptionObject0("e"), "file flag e"
        )
        self.assertEqual(
            Calendar, line.getOptionObject0("f"), "class flag f"
        )  # Assuming Calendar is imported
        self.assertEqual(4.5, line.getOptionObject0("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject0("t"),
            "url flag t",
        )

        with pytest.raises(NotImplementedError):
            self.assertEqual([], line.getOptionObject0("m"), "files flag m")
            pytest.fail("Multiple files are not supported yet, should have failed")

        with pytest.raises(NotImplementedError):
            self.assertEqual(
                datetime.datetime(2002, 6, 6, 17, 48, 57),
                line.getOptionObject0("z"),
                "date flag z",
            )
            pytest.fail("Date is not supported yet, should have failed")

    def testSimplePattern_test9_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")
        self.assertEqual(
            os.path.abspath("build.xml"), str(line.getOptionObject1("e")), "file flag e"
        )
        self.assertEqual(
            "java.util.Calendar", line.getOptionObject1("f"), "class flag f"
        )
        self.assertEqual(4.5, line.getOptionObject1("n"), "number flag n")
        self.assertEqual(
            "https://commons.apache.org", str(line.getOptionObject1("t")), "url flag t"
        )
        self.assertEqual("foo", line.getOptionValue0("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject0("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject0("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption0("c"), "boolean true flag c")
        self.assertFalse(line.hasOption0("d"), "boolean false flag d")

    def testSimplePattern_test8_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")
        self.assertEqual(
            pathlib.Path("build.xml"), line.getOptionObject1("e"), "file flag e"
        )
        self.assertEqual(
            Calendar, line.getOptionObject1("f"), "class flag f"
        )  # Assuming Calendar is defined
        self.assertEqual(4.5, line.getOptionObject1("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("t"),
            "url flag t",
        )
        self.assertEqual("foo", line.getOptionValue0("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject0("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject0("b"), "object flag b"
        )  # Assuming empty list for Vector

    def testSimplePattern_test7_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming empty Vector translates to empty list
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")
        self.assertEqual(
            pathlib.Path("build.xml"), line.getOptionObject1("e"), "file flag e"
        )
        self.assertEqual(
            Calendar, line.getOptionObject1("f"), "class flag f"
        )  # Assuming Calendar is imported or defined
        self.assertEqual(4.5, line.getOptionObject1("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("t"),
            "url flag t",
        )
        self.assertEqual("foo", line.getOptionValue0("a"), "flag a")

    def testSimplePattern_test6_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming empty list for Vector
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")
        self.assertEqual(
            pathlib.Path("build.xml"), line.getOptionObject1("e"), "file flag e"
        )
        self.assertEqual(
            Calendar, line.getOptionObject1("f"), "class flag f"
        )  # Assuming Calendar is imported
        self.assertEqual(4.5, line.getOptionObject1("n"), "number flag n")
        self.assertEqual(
            urllib.parse.urlparse("https://commons.apache.org"),
            line.getOptionObject1("t"),
            "url flag t",
        )

    def testSimplePattern_test5_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)
        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual(
            [], line.getOptionObject1("b"), "object flag b"
        )  # Assuming `new Vector<>()` translates to an empty list
        self.assertTrue(line.hasOption2("c"), "boolean true flag c")
        self.assertFalse(line.hasOption2("d"), "boolean false flag d")

    def testSimplePattern_test4_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)
        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")
        self.assertEqual("foo", line.getOptionObject1("a"), "string flag a")
        self.assertEqual([], line.getOptionObject1("b"), "object flag b")

    def testSimplePattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)
        self.assertEqual("foo", line.getOptionValue4("a"), "flag a")

    def testSimplePattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()
        line = parser.parse0(options, args)

    def testSimplePattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")
        args = [
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*",
        ]
        parser = PosixParser()

    def testSimplePattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#")

    def testRequiredOption_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("!n%m%")
        parser = PosixParser()
        try:
            parser.parse0(options, [""])
            pytest.fail("MissingOptionException wasn't thrown")
        except MissingOptionException as e:
            self.assertEqual(1, len(e.getMissingOptions()))
            self.assertTrue("n" in e.getMissingOptions())

    def testRequiredOption_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("!n%m%")
        parser = PosixParser()

    def testRequiredOption_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("!n%m%")

    def testObjectPattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("o@i@n@")
        parser = PosixParser()
        line = parser.parse0(
            options,
            [
                "-o",
                "java.lang.String",
                "-i",
                "java.util.Calendar",
                "-n",
                "System.DateTime",
            ],
        )
        self.assertEqual("", line.getOptionObject1("o"), "o value")
        self.assertIsNone(line.getOptionObject1("i"), "i value")
        self.assertIsNone(line.getOptionObject1("n"), "n value")

    def testObjectPattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("o@i@n@")
        parser = PosixParser()
        line = parser.parse0(
            options,
            [
                "-o",
                "java.lang.String",
                "-i",
                "java.util.Calendar",
                "-n",
                "System.DateTime",
            ],
        )

    def testObjectPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("o@i@n@")
        parser = PosixParser()

    def testObjectPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("o@i@n@")

    def testNumberPattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()
        line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

        self.assertEqual(type(line.getOptionObject1("n")), int, "n object class")
        self.assertEqual(line.getOptionObject1("n"), 1, "n value")

        self.assertEqual(type(line.getOptionObject1("d")), float, "d object class")
        self.assertEqual(line.getOptionObject1("d"), 2.1, "d value")

        self.assertIsNone(line.getOptionObject1("x"), "x object")

    def testNumberPattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()
        line = parser.parse0(options, ["-n", "1", "-d", "2.1", "-x", "3,5"])

    def testNumberPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("n%d%x%")
        parser = PosixParser()

    def testNumberPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("n%d%x%")

    def testExistingFilePatternFileNotExist_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])
        self.assertIsNone(line.getOptionObject1("f"), "option f parsed")

    def testExistingFilePatternFileNotExist_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()
        line = parser.parse0(options, ["-f", "non-existing.file"])

    def testExistingFilePatternFileNotExist_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("f<")
        parser = PosixParser()

    def testExistingFilePatternFileNotExist_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("f<")

    def testExistingFilePattern_test4_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )
        parsed_readable_file_stream = line.getOptionObject1("g")
        self.assertIsNotNone(parsed_readable_file_stream, "option g not parsed")
        self.assertTrue(
            isinstance(parsed_readable_file_stream, io.FileIO),
            "option g not FileInputStream",
        )

    def testExistingFilePattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )
        parsed_readable_file_stream = line.getOptionObject1("g")

    def testExistingFilePattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()
        line = parser.parse0(
            options,
            ["-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"],
        )

    def testExistingFilePattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")
        parser = PosixParser()

    def testExistingFilePattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("g<")

    def testEmptyPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("")
        self.assertTrue(
            len(options.getOptions()) == 0,
            "Options should be empty for an empty pattern",
        )

    def testEmptyPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("")

    def testClassPattern_test3_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )
        self.assertEqual("c value", Calendar, line.getOptionObject1("c"))
        self.assertIsNone(line.getOptionObject1("d"), "d value")

    def testClassPattern_test2_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()
        line = parser.parse0(
            options, ["-c", "java.util.Calendar", "-d", "System.DateTime"]
        )

    def testClassPattern_test1_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("c+d+")
        parser = PosixParser()

    def testClassPattern_test0_decomposed(self) -> None:
        options = PatternOptionBuilder.parsePattern("c+d+")
