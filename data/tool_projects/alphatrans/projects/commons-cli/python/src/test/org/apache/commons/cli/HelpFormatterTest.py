from __future__ import annotations
import time
import re
import numbers
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class HelpFormatterTest(unittest.TestCase):

    __EOL: str = os.linesep

    def testUsageWithLongOptSeparator_test18_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        # Building the "size" option
        size_option = (
            Options.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )
        options.addOption0(size_option)

        # Building the "age" option
        age_option = Options.builder0().longOpt("age").desc("the age").hasArg0().build()
        options.addOption0(age_option)

        # Setting up the HelpFormatter
        formatter = HelpFormatter()
        formatter.setLongOptSeparator("=")

        # Capturing the output
        out = io.StringIO()
        formatter.printUsage1(out, 80, "create", options)

        # Asserting the expected output
        self.assertEqual(
            "usage: create [--age=<arg>] [-f <arg>] [-s <SIZE>]", out.getvalue().strip()
        )

    def testUsageWithLongOptSeparator_test17_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Option.builder1("s")
        builder_s = builder_s.longOpt("size")
        builder_s = builder_s.desc("the size")
        builder_s = builder_s.hasArg0()
        builder_s = builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Option.builder0()
        builder_age = builder_age.longOpt("age")
        builder_age = builder_age.desc("the age")
        builder_age = builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        formatter.setLongOptSeparator("=")

        out = io.StringIO()
        formatter.printUsage1(out, 80, "create", options)
        out_value = out.getvalue()
        self.assertIn("create", out_value)
        self.assertIn("--size=SIZE", out_value)
        self.assertIn("--age", out_value)

    def testUsageWithLongOptSeparator_test16_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        formatter.setLongOptSeparator("=")

    def testUsageWithLongOptSeparator_test15_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        Option.builder1("s")
        Option.builder1("s").longOpt("size")
        Option.builder1("s").longOpt("size").desc("the size")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0()
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName(
            "SIZE"
        ).build()

        options.addOption0(
            Option.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )

        Option.builder0()
        Option.builder0().longOpt("age")
        Option.builder0().longOpt("age").desc("the age")
        Option.builder0().longOpt("age").desc("the age").hasArg0()
        Option.builder0().longOpt("age").desc("the age").hasArg0().build()

        options.addOption0(
            Option.builder0().longOpt("age").desc("the age").hasArg0().build()
        )

        formatter = HelpFormatter()

    def testUsageWithLongOptSeparator_test14_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.longOpt("size").desc("the size")
        builder_s.longOpt("size").desc("the size").hasArg0()
        builder_s.longOpt("size").desc("the size").hasArg0().argName("SIZE")
        option_s = (
            builder_s.longOpt("size").desc("the size").hasArg0().argName("SIZE").build()
        )
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.longOpt("age").desc("the age")
        builder_age.longOpt("age").desc("the age").hasArg0()
        option_age = builder_age.longOpt("age").desc("the age").hasArg0().build()
        options.addOption0(option_age)

    def testUsageWithLongOptSeparator_test13_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        Option.builder1("s")
        Option.builder1("s").longOpt("size")
        Option.builder1("s").longOpt("size").desc("the size")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0()
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName(
            "SIZE"
        ).build()

        options.addOption0(
            Option.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )

        Option.builder0()
        Option.builder0().longOpt("age")
        Option.builder0().longOpt("age").desc("the age")
        Option.builder0().longOpt("age").desc("the age").hasArg0()
        Option.builder0().longOpt("age").desc("the age").hasArg0().build()

    def testUsageWithLongOptSeparator_test12_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        size_option = builder.build()

        options.addOption0(size_option)

        builder = Options.builder0()
        builder.longOpt("age")
        builder.desc("the age")
        builder.hasArg0()

    def testUsageWithLongOptSeparator_test11_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        size_option = builder.build()

        options.addOption0(size_option)

        builder = Options.builder0()
        builder.longOpt("age")
        builder.desc("the age")

    def testUsageWithLongOptSeparator_test10_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Option.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)

        Option.builder0()
        Option.builder0().longOpt("age")

    def testUsageWithLongOptSeparator_test9_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)
        Options.builder0()

    def testUsageWithLongOptSeparator_test8_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)

    def testUsageWithLongOptSeparator_test7_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Options.builder1("s")
        builder = builder.longOpt("size")
        builder = builder.desc("the size")
        builder = builder.hasArg0()
        builder = builder.argName("SIZE")
        option = builder.build()

    def testUsageWithLongOptSeparator_test6_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")
        Option.builder1("s").longOpt("size")
        Option.builder1("s").longOpt("size").desc("the size")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0()
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE")

    def testUsageWithLongOptSeparator_test5_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Options.builder1("s")
        builder = builder.longOpt("size")
        builder = builder.desc("the size")
        builder = builder.hasArg0()

    def testUsageWithLongOptSeparator_test4_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")
        Option.builder1("s").longOpt("size")
        Option.builder1("s").longOpt("size").desc("the size")

    def testUsageWithLongOptSeparator_test3_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")
        Option.builder1("s").longOpt("size")

    def testUsageWithLongOptSeparator_test2_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")

    def testUsageWithLongOptSeparator_test1_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

    def testUsageWithLongOptSeparator_test0_decomposed(self) -> None:
        options = Options()

    def testRtrim_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        self.assertIsNone(formatter._rtrim(None))
        self.assertEqual("", formatter._rtrim(""))
        self.assertEqual("  foo", formatter._rtrim("  foo  "))

    def testRtrim_test0_decomposed(self) -> None:
        formatter = HelpFormatter()

    def testRenderWrappedTextWordCut_test1_decomposed(self) -> None:
        width = 7
        padding = 0
        text = "Thisisatest."
        expected = "Thisisa" + self.__EOL + "test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "cut and wrap")

    def testRenderWrappedTextWordCut_test0_decomposed(self) -> None:
        width = 7
        padding = 0
        text = "Thisisatest."
        expected = "Thisisa" + self.__EOL + "test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(sb.getvalue(), expected)

    def testRenderWrappedTextSingleLinePadded2_test1_decomposed(self) -> None:
        width = 53
        padding = 24
        text = (
            "  -p,--period <PERIOD>  PERIOD is time duration of form "
            "DATE[-DATE] where DATE has form YYYY[MM[DD]]"
        )
        expected = (
            "  -p,--period <PERIOD>  PERIOD is time duration of"
            + self.__EOL
            + "                        form DATE[-DATE] where DATE"
            + self.__EOL
            + "                        has form YYYY[MM[DD]]"
        )
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line padded text 2")

    def testRenderWrappedTextSingleLinePadded2_test0_decomposed(self) -> None:
        width = 53
        padding = 24
        text = (
            "  -p,--period <PERIOD>  PERIOD is time duration of form "
            "DATE[-DATE] where DATE has form YYYY[MM[DD]]"
        )
        expected = (
            "  -p,--period <PERIOD>  PERIOD is time duration of"
            + self.__EOL
            + "                        form DATE[-DATE] where DATE"
            + self.__EOL
            + "                        has form YYYY[MM[DD]]"
        )
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(sb.getvalue(), expected)

    def testRenderWrappedTextSingleLinePadded_test1_decomposed(self) -> None:
        width = 12
        padding = 4
        text = "This is a test."
        expected = f"This is a{self.__EOL}    test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line padded text")

    def testRenderWrappedTextSingleLinePadded_test0_decomposed(self) -> None:
        width = 12
        padding = 4
        text = "This is a test."
        expected = f"This is a{self.__EOL}    test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(sb.getvalue(), expected)

    def testRenderWrappedTextSingleLine_test1_decomposed(self) -> None:
        width = 12
        padding = 0
        text = "This is a test."
        expected = "This is a" + self.__EOL + "test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "single line text")

    def testRenderWrappedTextSingleLine_test0_decomposed(self) -> None:
        width = 12
        padding = 0
        text = "This is a test."
        expected = "This is a" + self.__EOL + "test."
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(sb.getvalue(), expected)

    def testRenderWrappedTextMultiLinePadded_test1_decomposed(self) -> None:
        width = 16
        padding = 4
        text = "aaaa aaaa aaaa" + self.__EOL + "aaaaaa" + self.__EOL + "aaaaa"
        expected = (
            "aaaa aaaa aaaa" + self.__EOL + "    aaaaaa" + self.__EOL + "    aaaaa"
        )
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(expected, sb.getvalue(), "multi-line padded text")

    def testRenderWrappedTextMultiLinePadded_test0_decomposed(self) -> None:
        width = 16
        padding = 4
        text = f"aaaa aaaa aaaa{self.__EOL}aaaaaa{self.__EOL}aaaaa"
        expected = f"aaaa aaaa aaaa{self.__EOL}    aaaaaa{self.__EOL}    aaaaa"
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, text)
        self.assertEqual(sb.getvalue(), expected)

    def testRenderWrappedTextMultiLine_test1_decomposed(self) -> None:
        width = 16
        padding = 0
        expected = f"aaaa aaaa aaaa{self.__EOL}aaaaaa{self.__EOL}aaaaa"
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(
            sb, width, padding, "aaaa aaaa aaaa aaaaaa aaaaa"
        )
        self.assertEqual(expected, sb.getvalue().strip(), "multi line text")

    def testRenderWrappedTextMultiLine_test0_decomposed(self) -> None:
        width = 16
        padding = 0
        expected = f"aaaa aaaa aaaa{self.__EOL}aaaaaa{self.__EOL}aaaaa"
        sb = io.StringIO()
        HelpFormatter()._renderWrappedText(sb, width, padding, expected)

    def testPrintUsage_test5_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)
        helpFormatter = HelpFormatter()
        bytesOut = io.StringIO()
        with io.StringIO() as printWriter:
            helpFormatter.printUsage1(printWriter, 80, "app", opts)
            output = printWriter.getvalue()
        self.assertEqual(f"usage: app [-a] [-b] [-c]{self.__EOL}", output)

    def testPrintUsage_test4_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)
        helpFormatter = HelpFormatter()
        bytesOut = io.StringIO()
        with io.StringIO() as printWriter:
            helpFormatter.printUsage1(printWriter, 80, "app", opts)

    def testPrintUsage_test3_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)
        helpFormatter = HelpFormatter()

    def testPrintUsage_test2_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()
        opts.addOption0(optionA)
        opts.addOption0(optionB)
        opts.addOption0(optionC)

    def testPrintUsage_test1_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")
        opts = Options()

    def testPrintUsage_test0_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        optionB = Option.Option1("b", "second")
        optionC = Option.Option1("c", "third")

    def testPrintSortedUsageWithNullComparator_test10_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))

        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(None)

        out = io.StringIO()
        help_formatter.printUsage1(out, 80, "app", opts)

        self.assertEqual(f"usage: app [-c] [-b] [-a]{self.__EOL}", out.getvalue())

    def testPrintSortedUsageWithNullComparator_test9_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))

        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(None)

        out = io.StringIO()
        help_formatter.printUsage1(out, 80, "app", opts)

    def testPrintSortedUsageWithNullComparator_test8_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))
        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(None)

    def testPrintSortedUsageWithNullComparator_test7_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option("c", "first"))
        opts.addOption0(Option("b", "second"))
        opts.addOption0(Option("a", "third"))
        help_formatter = HelpFormatter()

    def testPrintSortedUsageWithNullComparator_test6_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("a", "third"))

    def testPrintSortedUsageWithNullComparator_test5_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option("c", "first"))
        opts.addOption0(Option("b", "second"))
        opts.addOption0(Option("a", "third"))

    def testPrintSortedUsageWithNullComparator_test4_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("c", "first"))
        opts.addOption0(Option.Option1("b", "second"))

    def testPrintSortedUsageWithNullComparator_test3_decomposed(self) -> None:
        opts = Options()
        opt1 = Option("c", "first")
        opts.addOption0(opt1)
        opt2 = Option("b", "second")

    def testPrintSortedUsageWithNullComparator_test2_decomposed(self) -> None:
        opts = Options()
        opt = Option.Option1("c", "first")
        opts.addOption0(opt)

    def testPrintSortedUsageWithNullComparator_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption(Option("c", "first"))

    def testPrintSortedUsageWithNullComparator_test0_decomposed(self) -> None:
        opts = Options()

    def testPrintSortedUsage_test10_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("a", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("c", "third"))

        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(
            lambda opt1, opt2: opt2.getKey().lower() > opt1.getKey().lower()
        )

        out = io.StringIO()
        help_formatter.printUsage1(out, 80, "app", opts)

        self.assertEqual(f"usage: app [-c] [-b] [-a]{self.__EOL}", out.getvalue())

    def testPrintSortedUsage_test9_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option.Option1("a", "first"))
        opts.addOption0(Option.Option1("b", "second"))
        opts.addOption0(Option.Option1("c", "third"))

        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(
            lambda opt1, opt2: (
                -1
                if opt2.getKey().lower() > opt1.getKey().lower()
                else (1 if opt2.getKey().lower() < opt1.getKey().lower() else 0)
            )
        )

        out = io.StringIO()
        help_formatter.printUsage1(out, 80, "app", opts)

    def testPrintSortedUsage_test8_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option("a", "first"))
        opts.addOption0(Option("b", "second"))
        opts.addOption0(Option("c", "third"))

        help_formatter = HelpFormatter()
        help_formatter.setOptionComparator(
            lambda opt1, opt2: opt2.getKey().lower().compare(opt1.getKey().lower())
        )

    def testPrintSortedUsage_test7_decomposed(self) -> None:
        opts = Options()
        opts.addOption0(Option("a", "first"))
        opts.addOption0(Option("b", "second"))
        opts.addOption0(Option("c", "third"))
        help_formatter = HelpFormatter()

    def testPrintSortedUsage_test6_decomposed(self) -> None:
        opts = Options()
        opt1 = Option("a", "first")
        opts.addOption0(opt1)
        opt2 = Option("b", "second")
        opts.addOption0(opt2)
        opt3 = Option("c", "third")
        opts.addOption0(opt3)

    def testPrintSortedUsage_test5_decomposed(self) -> None:
        opts = Options()
        opt_a = Option("a", "first")
        opts.addOption0(opt_a)
        opt_b = Option("b", "second")
        opts.addOption0(opt_b)
        opt_c = Option("c", "third")

    def testPrintSortedUsage_test4_decomposed(self) -> None:
        opts = Options()
        opt1 = Option("a", "first")
        opts.addOption0(opt1)
        opt2 = Option("b", "second")
        opts.addOption0(opt2)

    def testPrintSortedUsage_test3_decomposed(self) -> None:
        opts = Options()
        opt1 = Option("a", "first")
        opts.addOption0(opt1)
        opt2 = Option("b", "second")

    def testPrintSortedUsage_test2_decomposed(self) -> None:
        opts = Options()
        option1 = Option("a", "first")
        opts.addOption0(option1)

    def testPrintSortedUsage_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption(Option("a", "first"))

    def testPrintSortedUsage_test0_decomposed(self) -> None:
        opts = Options()

    def testPrintRequiredOptionGroupUsage_test15_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual(f"usage: app -a | -b | -c{self.__EOL}", out.getvalue())

    def testPrintRequiredOptionGroupUsage_test14_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

    def testPrintRequiredOptionGroupUsage_test13_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()

    def testPrintRequiredOptionGroupUsage_test12_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

    def testPrintRequiredOptionGroupUsage_test11_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)
        options = Options()

    def testPrintRequiredOptionGroupUsage_test10_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())
        group.setRequired(True)

    def testPrintRequiredOptionGroupUsage_test9_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()
        group.addOption(Option.builder1("c").build())

    def testPrintRequiredOptionGroupUsage_test8_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()

    def testPrintRequiredOptionGroupUsage_test7_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")

    def testPrintRequiredOptionGroupUsage_test6_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())

    def testPrintRequiredOptionGroupUsage_test5_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()

    def testPrintRequiredOptionGroupUsage_test4_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")

    def testPrintRequiredOptionGroupUsage_test3_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())

    def testPrintRequiredOptionGroupUsage_test2_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()

    def testPrintRequiredOptionGroupUsage_test1_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")

    def testPrintRequiredOptionGroupUsage_test0_decomposed(self) -> None:
        group = OptionGroup()

    def testPrintOptionWithEmptyArgNameUsage_test7_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)

        options = Options()
        options.addOption0(option)

        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual(f"usage: app -f{self.__EOL}", out.getvalue())

    def testPrintOptionWithEmptyArgNameUsage_test6_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

    def testPrintOptionWithEmptyArgNameUsage_test5_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()

    def testPrintOptionWithEmptyArgNameUsage_test4_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)
        options = Options()
        options.addOption0(option)

    def testPrintOptionWithEmptyArgNameUsage_test3_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)
        options = Options()

    def testPrintOptionWithEmptyArgNameUsage_test2_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")
        option.setRequired(True)

    def testPrintOptionWithEmptyArgNameUsage_test1_decomposed(self) -> None:
        option = Option.Option2("f", True, None)
        option.setArgName("")

    def testPrintOptionWithEmptyArgNameUsage_test0_decomposed(self) -> None:
        option = Option.Option2("f", True, None)

    def testPrintOptions_test19_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = None
        expected = None

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

        # Test case 3: Multiple wrapped options
        options = (
            Options()
            .addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            .addOption1("b", False, "feeee eeee eeee eeee")
        )
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
            + self.__EOL
            + lpad
            + "-b      "
            + dpad
            + "feeee eeee"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "eeee eeee"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("multiple wrapped options", expected, sb.getvalue())

    def testPrintOptions_test18_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = None
        expected = None

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            f"{lpad}-a{dpad}aaaa aaaa aaaa{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}aaaa aaaa"
        )
        sb = io.StringIO()
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = f"{lpad}-a,--aaa{dpad}dddd dddd dddd dddd"
        sb = io.StringIO()
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            f"{lpad}-a,--aaa{dpad}dddd dddd{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}dddd dddd"
        )
        sb = io.StringIO()
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

        # Test case 3: Multiple options
        options = (
            Options()
            .addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            .addOption1("b", False, "feeee eeee eeee eeee")
        )
        expected = (
            f"{lpad}-a,--aaa{dpad}dddd dddd{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}dddd dddd{self.__EOL}"
            f"{lpad}-b      {dpad}feeee eeee{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}eeee eeee"
        )
        sb = io.StringIO()
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("multiple options", expected, sb.getvalue())

    def testPrintOptions_test17_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            f"{lpad}-a{dpad}aaaa aaaa aaaa{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = f"{lpad}-a,--aaa{dpad}dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            f"{lpad}-a,--aaa{dpad}dddd dddd{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

        # Test case 3: Multiple options
        options = (
            Options()
            .addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            .addOption1("b", False, "feeee eeee eeee eeee")
        )
        expected = (
            f"{lpad}-a,--aaa{dpad}dddd dddd{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}dddd dddd{self.__EOL}"
            f"{lpad}-b      {dpad}feeee eeee{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}eeee eeee"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("multiple options", expected, sb.getvalue())

    def testPrintOptions_test16_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = None
        expected = None

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

        # Test case 3: Multiple options
        options = (
            Options()
            .addOption3("a", "aaa", False, "dddd dddd dddd dddd")
            .addOption1("b", False, "feeee eeee eeee eeee")
        )

    def testPrintOptions_test15_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

    def testPrintOptions_test14_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options()
        expected = ""

        # Test case 1: Simple non-wrapped option
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

    def testPrintOptions_test13_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options()
        expected = ""

        # Test case 1: Simple non-wrapped option
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            f"{lpad}-a{dpad}aaaa aaaa aaaa{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = f"{lpad}-a,--aaa{dpad}dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            f"{lpad}-a,--aaa{dpad}dddd dddd{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 25, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

    def testPrintOptions_test12_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options()
        expected = ""

        # Test case 1: Simple non-wrapped option
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a,--aaa")
        expected = (
            lpad
            + "-a,--aaa"
            + dpad
            + "dddd dddd"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "dddd dddd"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("long wrapped option", expected, sb.getvalue())

    def testPrintOptions_test11_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Long non-wrapped option
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("long non-wrapped option", expected, sb.getvalue())

    def testPrintOptions_test10_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options()
        expected = ""

        # Test case 1: Simple non-wrapped option
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Test case 2: Option with long name
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd"
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("option with long name", expected, sb.getvalue())

    def testPrintOptions_test9_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        # Test case 1: Simple non-wrapped option
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        # Test case 2: Simple wrapped option
        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

        # Additional test case
        options = Options().addOption3("a", "aaa", False, "dddd dddd dddd dddd")

    def testPrintOptions_test8_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )
        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual("simple wrapped option", expected, sb.getvalue())

    def testPrintOptions_test7_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa"

        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            lpad
            + "-a"
            + dpad
            + "aaaa aaaa aaaa"
            + self.__EOL
            + hf._createPadding(next_line_tab_stop)
            + "aaaa aaaa"
        )

        sb = io.StringIO()  # Reset the StringIO buffer
        hf._renderOptions(sb, next_line_tab_stop + 17, options, left_pad, desc_pad)
        self.assertEqual(expected, sb.getvalue())

    def testPrintOptions_test6_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"

        hf._renderOptions(sb, 60, options, left_pad, desc_pad)
        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

        next_line_tab_stop = left_pad + desc_pad + len("-a")
        expected = (
            f"{lpad}-a{dpad}aaaa aaaa aaaa{self.__EOL}"
            f"{hf._createPadding(next_line_tab_stop)}aaaa aaaa"
        )

    def testPrintOptions_test5_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"

        hf._renderOptions(sb, 60, options, left_pad, desc_pad)

        self.assertEqual("simple non-wrapped option", expected, sb.getvalue())

    def testPrintOptions_test4_decomposed(self) -> None:
        sb = io.StringIO()
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = f"{lpad}-a{dpad}aaaa aaaa aaaa aaaa aaaa"
        hf._renderOptions(sb, 60, options, left_pad, desc_pad)

    def testPrintOptions_test3_decomposed(self) -> None:
        sb = io.StringIO()  # Using StringIO as a replacement for StringBuffer
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = None  # Placeholder for expected value, as it is not defined in the Java code

    def testPrintOptions_test2_decomposed(self) -> None:
        sb = io.StringIO()  # Using StringIO as a replacement for StringBuffer
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)
        dpad = hf._createPadding(desc_pad)

    def testPrintOptions_test1_decomposed(self) -> None:
        sb = io.StringIO()  # Equivalent to Java's StringBuffer
        hf = HelpFormatter()
        left_pad = 1
        desc_pad = 3
        lpad = hf._createPadding(left_pad)

    def testPrintOptions_test0_decomposed(self) -> None:
        sb = io.StringIO()  # Using StringIO as a replacement for StringBuffer
        hf = HelpFormatter()  # Creating an instance of HelpFormatter

    def testPrintOptionGroupUsage_test14_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

        self.assertEqual(f"usage: app [-a | -b | -c]{self.__EOL}", out.getvalue())

    def testPrintOptionGroupUsage_test13_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.printUsage1(out, 80, "app", options)

    def testPrintOptionGroupUsage_test12_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()
        group.addOption(Option.builder1("c").build())

        options = Options()
        options.addOptionGroup(group)

        out = io.StringIO()
        formatter = HelpFormatter()

    def testPrintOptionGroupUsage_test11_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(Option.builder1("a").build())
        group.addOption(Option.builder1("b").build())
        group.addOption(Option.builder1("c").build())

        options = Options()
        options.addOptionGroup(group)

    def testPrintOptionGroupUsage_test10_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()
        group.addOption(Option.builder1("c").build())
        options = Options()

    def testPrintOptionGroupUsage_test9_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()
        group.addOption(Option.builder1("c").build())

    def testPrintOptionGroupUsage_test8_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")
        Option.builder1("c").build()

    def testPrintOptionGroupUsage_test7_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())
        Option.builder1("c")

    def testPrintOptionGroupUsage_test6_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()
        group.addOption(Option.builder1("b").build())

    def testPrintOptionGroupUsage_test5_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")
        Option.builder1("b").build()

    def testPrintOptionGroupUsage_test4_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()
        group.addOption(Option.builder1("a").build())
        Option.builder1("b")

    def testPrintOptionGroupUsage_test3_decomposed(self) -> None:
        group = OptionGroup()
        builder = Option.builder1("a")
        option = builder.build()
        group.addOption(option)

    def testPrintOptionGroupUsage_test2_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")
        Option.builder1("a").build()

    def testPrintOptionGroupUsage_test1_decomposed(self) -> None:
        group = OptionGroup()
        Option.builder1("a")

    def testPrintOptionGroupUsage_test0_decomposed(self) -> None:
        group = OptionGroup()

    def testPrintHelpWithEmptySyntax_test2_decomposed(self) -> None:
        formatter = HelpFormatter()
        with pytest.raises(ValueError):
            formatter.printHelp4(None, Options())
        with pytest.raises(ValueError):
            formatter.printHelp4("", Options())

    def testPrintHelpWithEmptySyntax_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        with self.assertRaises(
            ValueError, msg="null command line syntax should be rejected"
        ):
            formatter.printHelp4(None, Options())

    def testPrintHelpWithEmptySyntax_test0_decomposed(self) -> None:
        formatter = HelpFormatter()

    def testPrintHelpNewlineHeader_test4_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.StringIO()
        pw = out
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(
            pw,
            80,
            "test" + self.__EOL,
            self.__EOL,
            options,
            0,
            0,
            "footer" + self.__EOL,
        )
        expected = (
            "usage: test"
            + self.__EOL
            + self.__EOL
            + "-ab"
            + self.__EOL
            + "footer"
            + self.__EOL
        )
        pw.seek(0)  # Reset the StringIO cursor to the beginning
        self.assertEqual("header newline", expected, out.getvalue())

    def testPrintHelpNewlineHeader_test3_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.StringIO()
        pw = out
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(
            pw,
            80,
            "test" + self.__EOL,
            self.__EOL,
            options,
            0,
            0,
            "footer" + self.__EOL,
        )

    def testPrintHelpNewlineHeader_test2_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, encoding="utf-8")
        options = Options()
        options.addOption2("a", "b")

    def testPrintHelpNewlineHeader_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, encoding="utf-8")
        options = Options()

    def testPrintHelpNewlineHeader_test0_decomposed(self) -> None:
        formatter = HelpFormatter()

    def testPrintHelpNewlineFooter_test4_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.StringIO()
        pw = out
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(
            pw,
            80,
            "test" + self.__EOL,
            "header" + self.__EOL,
            options,
            0,
            0,
            self.__EOL,
        )
        expected = (
            "usage: test"
            + self.__EOL
            + "header"
            + self.__EOL
            + "-ab"
            + self.__EOL
            + self.__EOL
        )
        pw.flush()
        self.assertEqual("footer newline", expected, out.getvalue())

    def testPrintHelpNewlineFooter_test3_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.StringIO()
        pw = out
        options = Options()
        options.addOption2("a", "b")
        formatter.printHelp2(
            pw,
            80,
            "test" + self.__EOL,
            "header" + self.__EOL,
            options,
            0,
            0,
            self.__EOL,
        )

    def testPrintHelpNewlineFooter_test2_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, encoding="utf-8")
        options = Options()
        options.addOption2("a", "b")

    def testPrintHelpNewlineFooter_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        out = io.BytesIO()
        pw = io.TextIOWrapper(out, encoding="utf-8")
        options = Options()

    def testPrintHelpNewlineFooter_test0_decomposed(self) -> None:
        formatter = HelpFormatter()

    def testOptionWithoutShortFormat2_test38_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

        formatter = HelpFormatter()
        eol = os.getenv("line.separator", "\n")
        out = io.StringIO()

        formatter.printHelp3(
            out,
            80,
            "commandline",
            "header",
            options,
            2,
            2,
            "footer",
            True,
        )

        expected_output = (
            "usage: commandline [-a <arg>] [--config <arg>] [-h] [-l <arg>] [-n] [-r <arg>]"
            + eol
            + "       [-s <arg>] [-t] [-v]"
            + eol
            + "header"
            + eol
            + "  -a,--age <arg>      Age (in days) of cache item before being recomputed"
            + eol
            + "     --config <arg>   Use the specified configuration file"
            + eol
            + "  -h,--help           print this message"
            + eol
            + "  -l,--limit <arg>    Set time limit for execution, in mintues"
            + eol
            + "  -n,--new            Create NLT cache entries only for new items"
            + eol
            + "  -r,--results <arg>  Number of results per item"
            + eol
            + "  -s,--server <arg>   The NLT server address"
            + eol
            + "  -t,--tracker        Create NLT cache entries only for tracker items"
            + eol
            + "  -v,--version        print version information"
            + eol
            + "footer"
            + eol
        )

        self.assertEqual(expected_output, out.getvalue())

    def testOptionWithoutShortFormat2_test37_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

        m_options = Options()
        m_options.addOption0(help_option)
        m_options.addOption0(version_option)
        m_options.addOption0(new_run_option)
        m_options.addOption0(tracker_run_option)
        m_options.addOption0(time_limit_option)
        m_options.addOption0(age_option)
        m_options.addOption0(server_option)
        m_options.addOption0(num_results_option)
        m_options.addOption0(config_file_option)

        formatter = HelpFormatter()
        eol = os.getenv("line.separator", "\n")
        out = io.StringIO()
        formatter.printHelp3(
            out, 80, "commandline", "header", m_options, 2, 2, "footer", True
        )

    def testOptionWithoutShortFormat2_test36_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

        m_options = Options()
        m_options.addOption0(help_option)
        m_options.addOption0(version_option)
        m_options.addOption0(new_run_option)
        m_options.addOption0(tracker_run_option)
        m_options.addOption0(time_limit_option)
        m_options.addOption0(age_option)
        m_options.addOption0(server_option)
        m_options.addOption0(num_results_option)
        m_options.addOption0(config_file_option)

        formatter = HelpFormatter()

    def testOptionWithoutShortFormat2_test35_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

        m_options = Options()
        m_options.addOption0(help_option)
        m_options.addOption0(version_option)
        m_options.addOption0(new_run_option)
        m_options.addOption0(tracker_run_option)
        m_options.addOption0(time_limit_option)
        m_options.addOption0(age_option)
        m_options.addOption0(server_option)
        m_options.addOption0(num_results_option)
        m_options.addOption0(config_file_option)

    def testOptionWithoutShortFormat2_test34_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

        m_options = Options()

    def testOptionWithoutShortFormat2_test33_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_file_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

    def testOptionWithoutShortFormat2_test32_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_option = (
            Builder.builder0()
            .longOpt("config")
            .hasArg0()
            .valueSeparator0()
            .desc("Use the specified configuration file")
            .build()
        )

    def testOptionWithoutShortFormat2_test31_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        config_option = Builder.builder0().longOpt("config").hasArg0().valueSeparator0()

    def testOptionWithoutShortFormat2_test30_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")
        Builder.builder1("r").longOpt("results").hasArg0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc(
            "Number of results per item"
        )
        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        Builder.builder0()
        Builder.builder0().longOpt("config")
        Builder.builder0().longOpt("config").hasArg0()

    def testOptionWithoutShortFormat2_test29_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")
        Builder.builder1("r").longOpt("results").hasArg0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc(
            "Number of results per item"
        )
        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        Builder.builder0()
        Builder.builder0().longOpt("config")

    def testOptionWithoutShortFormat2_test28_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

        Builder.builder0()

    def testOptionWithoutShortFormat2_test27_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        num_results_option = (
            Builder.builder1("r")
            .longOpt("results")
            .hasArg0()
            .valueSeparator0()
            .desc("Number of results per item")
            .build()
        )

    def testOptionWithoutShortFormat2_test26_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")
        Builder.builder1("r").longOpt("results").hasArg0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc(
            "Number of results per item"
        )

    def testOptionWithoutShortFormat2_test25_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")
        Builder.builder1("r").longOpt("results").hasArg0()
        Builder.builder1("r").longOpt("results").hasArg0().valueSeparator0()

    def testOptionWithoutShortFormat2_test24_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")
        Builder.builder1("r").longOpt("results").hasArg0()

    def testOptionWithoutShortFormat2_test23_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        Builder.builder1("r")
        Builder.builder1("r").longOpt("results")

    def testOptionWithoutShortFormat2_test22_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        # Building the timeLimit option
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        # Building the age option
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        # Building the server option
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

        # Example of creating an unused option (like "r" in the Java code)
        unused_option = Builder.builder1("r")

    def testOptionWithoutShortFormat2_test21_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc(
            "The NLT server address"
        )
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
            .build()
        )

    def testOptionWithoutShortFormat2_test20_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        # Building the timeLimit option
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in mintues")
            .build()
        )

        # Building the age option
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        # Building the server option
        server_option = (
            Builder.builder1("s")
            .longOpt("server")
            .hasArg0()
            .valueSeparator0()
            .desc("The NLT server address")
        )

    def testOptionWithoutShortFormat2_test19_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()
        Builder.builder1("s").longOpt("server").hasArg0().valueSeparator0()

    def testOptionWithoutShortFormat2_test18_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")
        Builder.builder1("s").longOpt("server").hasArg0()

    def testOptionWithoutShortFormat2_test17_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")
        Builder.builder1("s").longOpt("server")

    def testOptionWithoutShortFormat2_test16_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

        Builder.builder1("s")

    def testOptionWithoutShortFormat2_test15_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            Builder.builder1("a")
            .longOpt("age")
            .hasArg0()
            .valueSeparator0()
            .desc("Age (in days) of cache item before being recomputed")
            .build()
        )

    def testOptionWithoutShortFormat2_test14_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc(
            "Age (in days) of cache item before being recomputed"
        )

    def testOptionWithoutShortFormat2_test13_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()
        Builder.builder1("a").longOpt("age").hasArg0().valueSeparator0()

    def testOptionWithoutShortFormat2_test12_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")
        Builder.builder1("a").longOpt("age").hasArg0()

    def testOptionWithoutShortFormat2_test11_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")
        Builder.builder1("a").longOpt("age")

    def testOptionWithoutShortFormat2_test10_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        Builder.builder1("l")
        Builder.builder1("l").longOpt("limit")
        Builder.builder1("l").longOpt("limit").hasArg0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0()
        Builder.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc(
            "Set time limit for execution, in minutes"
        )

        time_limit_option = (
            Builder.builder1("l")
            .longOpt("limit")
            .hasArg0()
            .valueSeparator0()
            .desc("Set time limit for execution, in minutes")
            .build()
        )

        Builder.builder1("a")

    def testOptionWithoutShortFormat2_test9_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        builder = Builder.builder1("l")
        builder = builder.longOpt("limit")
        builder = builder.hasArg0()
        builder = builder.valueSeparator0()
        builder = builder.desc("Set time limit for execution, in minutes")
        time_limit_option = builder.build()

    def testOptionWithoutShortFormat2_test8_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        builder = Option.builder1("l")
        builder = builder.longOpt("limit")
        builder = builder.hasArg0()
        builder = builder.valueSeparator0()
        builder = builder.desc("Set time limit for execution, in minutes")

    def testOptionWithoutShortFormat2_test7_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        builder = Option.builder1("l")
        builder.longOpt("limit")
        builder.hasArg0()
        builder.valueSeparator0()

    def testOptionWithoutShortFormat2_test6_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        builder = Option.builder1("l")
        builder.longOpt("limit")
        builder.hasArg0()

    def testOptionWithoutShortFormat2_test5_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )
        Option.builder1("l")
        Option.builder1("l").longOpt("limit")

    def testOptionWithoutShortFormat2_test4_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )
        Option.builder1("l")

    def testOptionWithoutShortFormat2_test3_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

    def testOptionWithoutShortFormat2_test2_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )

    def testOptionWithoutShortFormat2_test1_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )

    def testOptionWithoutShortFormat2_test0_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)

    def testOptionWithoutShortFormat_test6_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

        formatter = HelpFormatter()
        out = io.StringIO()
        formatter.printHelp3(
            io.StringIO(out), 80, "foobar", "", options, 2, 2, "", True
        )

        expected_output = (
            "usage: foobar [-a] [--bbb] [-c]"
            + self.__EOL
            + "  -a,--aaa  aaaaaaa"
            + self.__EOL
            + "     --bbb  bbbbbbb"
            + self.__EOL
            + "  -c        ccccccc"
            + self.__EOL
        )

        self.assertEqual(expected_output, out.getvalue())

    def testOptionWithoutShortFormat_test5_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

        formatter = HelpFormatter()
        out = io.StringIO()
        formatter.printHelp3(out, 80, "foobar", "", options, 2, 2, "", True)

    def testOptionWithoutShortFormat_test4_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))
        formatter = HelpFormatter()

    def testOptionWithoutShortFormat_test3_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))
        options.addOption0(Option(0, "c", None, "ccccccc", False, None))

    def testOptionWithoutShortFormat_test2_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))
        options.addOption0(Option(0, None, "bbb", "bbbbbbb", False, None))

    def testOptionWithoutShortFormat_test1_decomposed(self) -> None:
        options = Options()
        options.addOption0(Option(0, "a", "aaa", "aaaaaaa", False, None))

    def testOptionWithoutShortFormat_test0_decomposed(self) -> None:
        options = Options()

    def testIndentedHeaderAndFooter_test3_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = "  Header1\n  Header2"
        footer = "  Footer1\n  Footer2"
        out = io.StringIO()

        formatter.printHelp3(out, 80, "foobar", header, options, 2, 2, footer, True)

        expected_output = (
            "usage: foobar"
            + self.__EOL
            + "  Header1"
            + self.__EOL
            + "  Header2"
            + self.__EOL
            + ""
            + self.__EOL
            + "  Footer1"
            + self.__EOL
            + "  Footer2"
            + self.__EOL
        )

        self.assertEqual(expected_output, out.getvalue())

    def testIndentedHeaderAndFooter_test2_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = "  Header1\n  Header2"
        footer = "  Footer1\n  Footer2"
        out = io.StringIO()
        formatter.printHelp3(out, 80, "foobar", header, options, 2, 2, footer, True)

    def testIndentedHeaderAndFooter_test1_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()

    def testIndentedHeaderAndFooter_test0_decomposed(self) -> None:
        options = Options()

    def testHelpWithLongOptSeparator_test20_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Option.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Option.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )

        formatter.setLongOptSeparator("=")
        self.assertEqual("=", formatter.getLongOptSeparator())

        out = io.StringIO()
        formatter.printHelp2(out, 80, "create", "header", options, 2, 2, "footer")

        expected_output = (
            "usage: create"
            + self.__EOL
            + "header"
            + self.__EOL
            + "     --age=<arg>    the age"
            + self.__EOL
            + "  -f <arg>          the file"
            + self.__EOL
            + "  -s,--size=<SIZE>  the size"
            + self.__EOL
            + "footer"
            + self.__EOL
        )
        self.assertEqual(expected_output, out.getvalue())

    def testHelpWithLongOptSeparator_test19_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Option.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Option.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )

        formatter.setLongOptSeparator("=")
        self.assertEqual("=", formatter.getLongOptSeparator())

        out = io.StringIO()
        formatter.printHelp2(out, 80, "create", "header", options, 2, 2, "footer")

    def testHelpWithLongOptSeparator_test18_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )
        formatter.setLongOptSeparator("=")
        self.assertEqual("=", formatter.getLongOptSeparator())

    def testHelpWithLongOptSeparator_test17_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )
        formatter.setLongOptSeparator("=")

    def testHelpWithLongOptSeparator_test16_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

        formatter = HelpFormatter()
        self.assertEqual(
            HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator()
        )

    def testHelpWithLongOptSeparator_test15_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        Option.builder1("s")
        Option.builder1("s").longOpt("size")
        Option.builder1("s").longOpt("size").desc("the size")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0()
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE")
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName(
            "SIZE"
        ).build()

        options.addOption0(
            Option.builder1("s")
            .longOpt("size")
            .desc("the size")
            .hasArg0()
            .argName("SIZE")
            .build()
        )

        Option.builder0()
        Option.builder0().longOpt("age")
        Option.builder0().longOpt("age").desc("the age")
        Option.builder0().longOpt("age").desc("the age").hasArg0()
        Option.builder0().longOpt("age").desc("the age").hasArg0().build()

        options.addOption0(
            Option.builder0().longOpt("age").desc("the age").hasArg0().build()
        )

        formatter = HelpFormatter()

    def testHelpWithLongOptSeparator_test14_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.desc("the size")
        builder_s.hasArg0()
        builder_s.argName("SIZE")
        option_s = builder_s.build()
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.desc("the age")
        builder_age.hasArg0()
        option_age = builder_age.build()
        options.addOption0(option_age)

    def testHelpWithLongOptSeparator_test13_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder_s = Options.builder1("s")
        builder_s.longOpt("size")
        builder_s.longOpt("size").desc("the size")
        builder_s.longOpt("size").desc("the size").hasArg0()
        builder_s.longOpt("size").desc("the size").hasArg0().argName("SIZE")
        option_s = (
            builder_s.longOpt("size").desc("the size").hasArg0().argName("SIZE").build()
        )
        options.addOption0(option_s)

        builder_age = Options.builder0()
        builder_age.longOpt("age")
        builder_age.longOpt("age").desc("the age")
        builder_age.longOpt("age").desc("the age").hasArg0()
        option_age = builder_age.longOpt("age").desc("the age").hasArg0().build()

    def testHelpWithLongOptSeparator_test12_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        size_option = builder.build()

        options.addOption0(size_option)

        builder = Options.builder0()
        builder.longOpt("age")
        builder.desc("the age")
        builder.hasArg0()

    def testHelpWithLongOptSeparator_test11_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)

        builder = Options.builder0()
        builder.longOpt("age")
        builder.desc("the age")

    def testHelpWithLongOptSeparator_test10_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Option.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)

        Option.builder0()
        Option.builder0().longOpt("age")

    def testHelpWithLongOptSeparator_test9_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)
        Options.builder0()

    def testHelpWithLongOptSeparator_test8_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

        builder = Options.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()
        builder.argName("SIZE")
        option = builder.build()

        options.addOption0(option)

    def testHelpWithLongOptSeparator_test7_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Options.builder1("s")
        builder = builder.longOpt("size")
        builder = builder.desc("the size")
        builder = builder.hasArg0()
        builder = builder.argName("SIZE")
        option = builder.build()

    def testHelpWithLongOptSeparator_test6_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Options.builder1("s")
        builder = builder.longOpt("size")
        builder = builder.desc("the size")
        builder = builder.hasArg0()
        builder = builder.argName("SIZE")

    def testHelpWithLongOptSeparator_test5_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Option.builder1("s")
        builder.longOpt("size")
        builder.desc("the size")
        builder.hasArg0()

    def testHelpWithLongOptSeparator_test4_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        builder = Options.builder1("s")
        builder = builder.longOpt("size")
        builder = builder.desc("the size")

    def testHelpWithLongOptSeparator_test3_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")
        Option.builder1("s").longOpt("size")

    def testHelpWithLongOptSeparator_test2_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")
        Option.builder1("s")

    def testHelpWithLongOptSeparator_test1_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "the file")

    def testHelpWithLongOptSeparator_test0_decomposed(self) -> None:
        options = Options()

    def testHeaderStartingWithLineSeparator_test3_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = self.__EOL + "Header"
        footer = "Footer"
        out = io.StringIO()

        formatter.printHelp3(out, 80, "foobar", header, options, 2, 2, footer, True)

        expected_output = (
            "usage: foobar"
            + self.__EOL
            + ""
            + self.__EOL
            + "Header"
            + self.__EOL
            + ""
            + self.__EOL
            + "Footer"
            + self.__EOL
        )

        self.assertEqual(expected_output, out.getvalue())

    def testHeaderStartingWithLineSeparator_test2_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()
        header = self.__EOL + "Header"
        footer = "Footer"
        out = io.StringIO()
        formatter.printHelp3(out, 80, "foobar", header, options, 2, 2, footer, True)

    def testHeaderStartingWithLineSeparator_test1_decomposed(self) -> None:
        options = Options()
        formatter = HelpFormatter()

    def testHeaderStartingWithLineSeparator_test0_decomposed(self) -> None:
        options = Options()

    def testFindWrapPos_test7_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")

        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")

        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf._findWrapPos(text, 6, 0), "wrap position 4")
        self.assertEqual(-1, hf._findWrapPos(text, 6, 7), "wrap position 4")

        text = "aaaaaa\n aaaaaa"
        self.assertEqual(7, hf._findWrapPos(text, 6, 0), "wrap position 5")

        text = "aaaaaa\t aaaaaa"
        self.assertEqual(7, hf._findWrapPos(text, 6, 0), "wrap position 6")

    def testFindWrapPos_test6_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")

        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")

        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf._findWrapPos(text, 6, 0), "wrap position 4")
        self.assertEqual(-1, hf._findWrapPos(text, 6, 7), "wrap position 4")

        text = "aaaaaa\n aaaaaa"
        self.assertEqual(7, hf._findWrapPos(text, 6, 0), "wrap position 5")

    def testFindWrapPos_test5_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")
        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")
        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf._findWrapPos(text, 6, 0), "wrap position 4")
        self.assertEqual(-1, hf._findWrapPos(text, 6, 7), "wrap position 4")

    def testFindWrapPos_test4_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")
        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")
        text = "aaaaaa aaaaaa"
        self.assertEqual(6, hf._findWrapPos(text, 6, 0), "wrap position 4")

    def testFindWrapPos_test3_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")
        text = "aaaa aa"
        self.assertEqual(3, hf._findWrapPos(text, 3, 0), "wrap position 3")

    def testFindWrapPos_test2_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")
        self.assertEqual(-1, hf._findWrapPos(text, 8, 8), "wrap position 2")

    def testFindWrapPos_test1_decomposed(self) -> None:
        hf = HelpFormatter()
        text = "This is a test."
        self.assertEqual(7, hf._findWrapPos(text, 8, 0), "wrap position")

    def testFindWrapPos_test0_decomposed(self) -> None:
        hf = HelpFormatter()

    def testDefaultArgName_test9_decomposed(self) -> None:
        option = Builder.builder1("f").hasArg0().required1(True).build()
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.setArgName("argument")
        formatter.printUsage1(out, 80, "app", options)
        self.assertEqual(f"usage: app -f <argument>{self.__EOL}", out.getvalue())

    def testDefaultArgName_test8_decomposed(self) -> None:
        option = Builder.builder1("f").hasArg0().required1(True).build()
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.setArgName("argument")
        formatter.printUsage1(out, 80, "app", options)

    def testDefaultArgName_test7_decomposed(self) -> None:
        option = Builder.builder1("f").hasArg0().required1(True).build()
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()
        formatter.setArgName("argument")

    def testDefaultArgName_test6_decomposed(self) -> None:
        builder = Builder.builder1("f")
        builder.hasArg0()
        builder.hasArg0().required1(True)
        option = builder.hasArg0().required1(True).build()
        options = Options()
        options.addOption0(option)
        out = io.StringIO()
        formatter = HelpFormatter()

    def testDefaultArgName_test5_decomposed(self) -> None:
        option = Builder.builder1("f").hasArg0().required1(True).build()
        options = Options()
        options.addOption0(option)

    def testDefaultArgName_test4_decomposed(self) -> None:
        builder = Builder.builder1("f")
        builder.hasArg0()
        builder.required1(True)
        option = builder.hasArg0().required1(True).build()
        options = Options()

    def testDefaultArgName_test3_decomposed(self) -> None:
        Builder.builder1("f")
        Builder.builder1("f").hasArg0()
        Builder.builder1("f").hasArg0().required1(True)
        option = Builder.builder1("f").hasArg0().required1(True).build()

    def testDefaultArgName_test2_decomposed(self) -> None:
        Option.builder1("f")
        Option.builder1("f").hasArg0()
        Option.builder1("f").hasArg0().required1(True)

    def testDefaultArgName_test1_decomposed(self) -> None:
        Option.builder1("f")
        Option.builder1("f").hasArg0()

    def testDefaultArgName_test0_decomposed(self) -> None:
        Option.builder1("f")

    def testAutomaticUsage_test8_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)

        # First test case
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())
        out.seek(0)
        out.truncate(0)

        # Second test case
        expected = "usage: app [-a] [-b]"
        options = (
            Options()
            .addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            .addOption1("b", False, "bbb")
        )
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())
        out.seek(0)
        out.truncate(0)

    def testAutomaticUsage_test7_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = out

        # First test case
        options = options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.seek(0)  # Reset the pointer to the beginning of the stream
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())
        out.truncate(0)  # Clear the stream
        out.seek(0)

        # Second test case
        expected = "usage: app [-a] [-b]"
        options = (
            Options()
            .addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            .addOption1("b", False, "bbb")
        )
        hf.printUsage1(pw, 60, "app", options)
        pw.seek(0)  # Reset the pointer to the beginning of the stream
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())

    def testAutomaticUsage_test6_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)

        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())

        out.seek(0)
        out.truncate(0)

        expected = "usage: app [-a] [-b]"
        options = (
            Options()
            .addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            .addOption1("b", False, "bbb")
        )
        hf.printUsage1(pw, 60, "app", options)

    def testAutomaticUsage_test5_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)

        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())

        out.seek(0)
        out.truncate(0)

        expected = "usage: app [-a] [-b]"
        options = (
            Options()
            .addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
            .addOption1("b", False, "bbb")
        )

    def testAutomaticUsage_test4_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        pw.flush()
        self.assertEqual("simple auto usage", expected, out.getvalue().strip())
        out.close()

    def testAutomaticUsage_test3_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options().addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        expected = "usage: app [-a]"

        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)

        hf.printUsage1(pw, 60, "app", options)
        pw.flush()

        self.assertEqual("simple auto usage", expected, out.getvalue().strip())

    def testAutomaticUsage_test2_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = out
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")
        hf.printUsage1(pw, 60, "app", options)
        self.assertEqual(out.getvalue().strip(), expected)

    def testAutomaticUsage_test1_decomposed(self) -> None:
        hf = HelpFormatter()
        options = Options()
        expected = "usage: app [-a]"
        out = io.StringIO()
        pw = io.TextIOWrapper(out, write_through=True)
        options.addOption1("a", False, "aaaa aaaa aaaa aaaa aaaa")

    def testAutomaticUsage_test0_decomposed(self) -> None:
        hf = HelpFormatter()

    def testAccessors_test16_decomposed(self) -> None:
        formatter = HelpFormatter()

        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")

        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")

        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")

        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")

        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")

        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")

        formatter.setSyntaxPrefix("-> ")
        self.assertEqual("-> ", formatter.getSyntaxPrefix(), "syntax prefix")

        formatter.setWidth(80)
        self.assertEqual(80, formatter.getWidth(), "width")

    def testAccessors_test15_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")

        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")

        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")

        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")

        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")

        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")

        formatter.setSyntaxPrefix("-> ")
        self.assertEqual("-> ", formatter.getSyntaxPrefix(), "syntax prefix")

        formatter.setWidth(80)

    def testAccessors_test14_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")
        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")
        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")
        formatter.setSyntaxPrefix("-> ")
        self.assertEqual("-> ", formatter.getSyntaxPrefix(), "syntax prefix")

    def testAccessors_test13_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")

        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")

        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")

        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")

        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")

        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")

        formatter.setSyntaxPrefix("-> ")
        # No assertion for setSyntaxPrefix as in the original Java code

    def testAccessors_test12_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")
        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")
        formatter.setOptPrefix("~")
        self.assertEqual("~", formatter.getOptPrefix(), "opt prefix")

    def testAccessors_test11_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")
        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")
        formatter.setOptPrefix("~")

    def testAccessors_test10_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")
        formatter.setNewLine("\n")
        self.assertEqual("\n", formatter.getNewLine(), "new line")

    def testAccessors_test9_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")
        formatter.setNewLine("\n")

    def testAccessors_test8_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")
        self.assertEqual("~~", formatter.getLongOptPrefix(), "long opt prefix")

    def testAccessors_test7_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")
        formatter.setLongOptPrefix("~~")

    def testAccessors_test6_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)
        self.assertEqual(7, formatter.getLeftPadding(), "left padding")

    def testAccessors_test5_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")
        formatter.setLeftPadding(7)

    def testAccessors_test4_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)
        self.assertEqual(3, formatter.getDescPadding(), "desc padding")

    def testAccessors_test3_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")
        formatter.setDescPadding(3)

    def testAccessors_test2_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")
        self.assertEqual("argname", formatter.getArgName(), "arg name")

    def testAccessors_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        formatter.setArgName("argname")

    def testAccessors_test0_decomposed(self) -> None:
        formatter = HelpFormatter()
