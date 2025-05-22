from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import os
import unittest
import configparser
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *


class ParserTestCase(ABC, unittest.TestCase):

    _options: Options = None

    _parser: CommandLineParser = None

    def testWithRequiredOption_test10_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)
        cl = self._parser.parse0(options, args)

        self.assertFalse(cl.hasOption2("a"), "Confirm -a is NOT set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue4("b"), "file", "Confirm arg of -b")
        self.assertTrue(cl.getArgList().isEmpty(), "Confirm NO of extra args")

    def testWithRequiredOption_test9_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)
        cl = self._parser.parse0(options, args)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is NOT set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("file", cl.getOptionValue4("b"), "Confirm arg of -b")

    def testWithRequiredOption_test8_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)
        cl = self._parser.parse0(options, args)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is NOT set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testWithRequiredOption_test7_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)
        cl = self._parser.parse0(options, args)

    def testWithRequiredOption_test6_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)

    def testWithRequiredOption_test5_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")

    def testWithRequiredOption_test4_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()

    def testWithRequiredOption_test3_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()

    def testWithRequiredOption_test2_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")

    def testWithRequiredOption_test1_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

    def testWithRequiredOption_test0_decomposed(self) -> None:
        args = ["-b", "file"]
        options = Options()

    def testUnrecognizedOptionWithBursting_test0_decomposed(self) -> None:
        args = ["-adbtoast", "foo", "bar"]
        try:
            self._parser.parse0(self._options, args)
            pytest.fail("UnrecognizedOptionException wasn't thrown")
        except UnrecognizedOptionException as e:
            self.assertEqual("-adbtoast", e.getOption())

    def testUnrecognizedOption_test0_decomposed(self) -> None:
        args = ["-a", "-d", "-b", "toast", "foo", "bar"]
        with pytest.raises(UnrecognizedOptionException) as excinfo:
            self._parser.parse0(self._options, args)
        assert excinfo.value.getOption() == "-d"

    def testUnlimitedArgs_test11_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

        # Create and add option "e" with unlimited arguments
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

        # Create and add option "f" with unlimited arguments
        option_f = OptionBuilder.hasArgs0().create2("f")
        options.addOption0(option_f)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions for option "e"
        self.assertTrue(cl.hasOption2("e"), "Confirm -e is set")
        self.assertEqual(2, len(cl.getOptionValues2("e")), "number of arg for -e")

        # Assertions for option "f"
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertEqual(1, len(cl.getOptionValues2("f")), "number of arg for -f")

    def testUnlimitedArgs_test10_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

        # Create and add option "e" with unlimited arguments
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

        # Create and add option "f" with unlimited arguments
        option_f = OptionBuilder.hasArgs0().create2("f")
        options.addOption0(option_f)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("e"), "Confirm -e is set")
        self.assertEqual(2, len(cl.getOptionValues2("e")), "number of args for -e")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")

    def testUnlimitedArgs_test9_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

        # Create and add option "e" with unlimited arguments
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

        # Create and add option "f" with unlimited arguments
        option_f = OptionBuilder.hasArgs0().create2("f")
        options.addOption0(option_f)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("e"), "Confirm -e is set")
        self.assertEqual(2, len(cl.getOptionValues2("e")), "number of args for -e")

    def testUnlimitedArgs_test8_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

        # Create and add option "e"
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

        # Create and add option "f"
        option_f = OptionBuilder.hasArgs0().create2("f")
        options.addOption0(option_f)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assert that the "-e" option is set
        self.assertTrue(cl.hasOption2("e"), "Confirm -e is set")

    def testUnlimitedArgs_test7_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

        # Create and add option "e"
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

        # Create and add option "f"
        option_f = OptionBuilder.hasArgs0().create2("f")
        options.addOption0(option_f)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

    def testUnlimitedArgs_test6_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        OptionBuilder.hasArgs0()
        options.addOption0(OptionBuilder.hasArgs0().create2("e"))
        OptionBuilder.hasArgs0()
        options.addOption0(OptionBuilder.hasArgs0().create2("f"))

    def testUnlimitedArgs_test5_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        OptionBuilder.hasArgs0()
        e_option = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(e_option)
        OptionBuilder.hasArgs0()
        f_option = OptionBuilder.hasArgs0().create2("f")

    def testUnlimitedArgs_test4_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        OptionBuilder.hasArgs0()
        e_option = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(e_option)
        OptionBuilder.hasArgs0()

    def testUnlimitedArgs_test3_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        option_e = OptionBuilder.hasArgs0().create2("e")
        options.addOption0(option_e)

    def testUnlimitedArgs_test2_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        OptionBuilder.hasArgs0()
        OptionBuilder.hasArgs0().create2("e")

    def testUnlimitedArgs_test1_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()
        OptionBuilder.hasArgs0()

    def testUnlimitedArgs_test0_decomposed(self) -> None:
        args = ["-e", "one", "two", "-f", "alpha"]
        options = Options()

    def testUnambiguousPartialLongOption4_test10_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        # Define the "verbose" option with an optional argument
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Define the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set")
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption4_test9_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        # Define the "verbose" option with an optional argument
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Define the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assert that the "verbose" option is set
        self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set")

    def testUnambiguousPartialLongOption4_test8_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        cl = self._parser.parse0(options, args)

    def testUnambiguousPartialLongOption4_test7_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

    def testUnambiguousPartialLongOption4_test6_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()

    def testUnambiguousPartialLongOption4_test5_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        OptionBuilder.withLongOpt("help")

    def testUnambiguousPartialLongOption4_test4_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

    def testUnambiguousPartialLongOption4_test3_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()

    def testUnambiguousPartialLongOption4_test2_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()

    def testUnambiguousPartialLongOption4_test1_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")

    def testUnambiguousPartialLongOption4_test0_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

    def testUnambiguousPartialLongOption3_test10_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "verbose" option with an optional argument
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Define the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set")
        self.assertEqual("1", cl.getOptionValue4("verbose"))

    def testUnambiguousPartialLongOption3_test9_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "verbose" option with an optional argument
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Define the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assert that the "verbose" option is set
        self.assertTrue(cl.hasOption2("verbose"), "Confirm --verbose is set")

    def testUnambiguousPartialLongOption3_test8_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "verbose" option with an optional argument
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Define the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

    def testUnambiguousPartialLongOption3_test7_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Create and add the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        # Create and add the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

    def testUnambiguousPartialLongOption3_test6_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()

    def testUnambiguousPartialLongOption3_test5_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )
        OptionBuilder.withLongOpt("help")

    def testUnambiguousPartialLongOption3_test4_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

    def testUnambiguousPartialLongOption3_test3_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()

    def testUnambiguousPartialLongOption3_test2_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()

    def testUnambiguousPartialLongOption3_test1_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("verbose")

    def testUnambiguousPartialLongOption3_test0_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

    def testUnambiguousPartialLongOption2_test8_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Add the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Add the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assert that the "version" option is set
        self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")

    def testUnambiguousPartialLongOption2_test7_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Add "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Add "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

    def testUnambiguousPartialLongOption2_test6_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Create and add the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Create and add the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

    def testUnambiguousPartialLongOption2_test5_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()

    def testUnambiguousPartialLongOption2_test4_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("help")

    def testUnambiguousPartialLongOption2_test3_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

    def testUnambiguousPartialLongOption2_test2_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testUnambiguousPartialLongOption2_test1_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testUnambiguousPartialLongOption2_test0_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

    def testUnambiguousPartialLongOption1_test8_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

        # Add the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Add the "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assert that the "version" option is set
        self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")

    def testUnambiguousPartialLongOption1_test7_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

        # Add "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Add "help" option
        OptionBuilder.withLongOpt("help")
        help_option = OptionBuilder.withLongOpt("help").create0()
        options.addOption0(help_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

    def testUnambiguousPartialLongOption1_test6_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()
        options.addOption0(OptionBuilder.withLongOpt("help").create0())

    def testUnambiguousPartialLongOption1_test5_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("help")
        OptionBuilder.withLongOpt("help").create0()

    def testUnambiguousPartialLongOption1_test4_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("help")

    def testUnambiguousPartialLongOption1_test3_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(option)

    def testUnambiguousPartialLongOption1_test2_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testUnambiguousPartialLongOption1_test1_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testUnambiguousPartialLongOption1_test0_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

    def testStopBursting2_test7_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)

        # Confirm -c is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Confirm 2 extra args
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )

        # Get arguments and re-parse
        cl_args = cl.getArgs()
        cl = self._parser.parse0(self._options, cl_args)

        # Confirm -c is not set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Confirm -b is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

        # Confirm argument of -b
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")

        # Confirm 1 extra arg
        self.assertEqual(
            1, len(cl.getArgList()), f"Confirm 1 extra arg: {len(cl.getArgList())}"
        )

        # Confirm value of extra arg
        self.assertEqual(
            "foobar",
            cl.getArgList()[0],
            f"Confirm value of extra arg: {cl.getArgList()[0]}",
        )

    def testStopBursting2_test6_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")

    def testStopBursting2_test5_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)

        # Confirm -c is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Confirm 2 extra args
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )

        cl_args = cl.getArgs()
        cl = self._parser.parse0(self._options, cl_args)

        # Confirm -c is not set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Confirm -b is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testStopBursting2_test4_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())

    def testStopBursting2_test3_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()

    def testStopBursting2_test2_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )

    def testStopBursting2_test1_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

    def testStopBursting2_test0_decomposed(self) -> None:
        args = ["-c", "foobar", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)

    def testStopBursting_test2_decomposed(self) -> None:
        args = ["-azc"]
        cl = self._parser.parse1(self._options, args, True)

        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
        self.assertEqual(
            1, len(cl.getArgList()), f"Confirm 1 extra arg: {len(cl.getArgList())}"
        )
        self.assertIn("zc", cl.getArgList())

    def testStopBursting_test1_decomposed(self) -> None:
        args = ["-azc"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

    def testStopBursting_test0_decomposed(self) -> None:
        args = ["-azc"]
        cl = self._parser.parse1(self._options, args, True)

    def testStopAtUnexpectedArg_test2_decomposed(self) -> None:
        args = ["-c", "foober", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

    def testStopAtUnexpectedArg_test1_decomposed(self) -> None:
        args = ["-c", "foober", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

    def testStopAtUnexpectedArg_test0_decomposed(self) -> None:
        args = ["-c", "foober", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)

    def testStopAtNonOptionShort_test2_decomposed(self) -> None:
        args = ["-z", "-a", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

    def testStopAtNonOptionShort_test1_decomposed(self) -> None:
        args = ["-z", "-a", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")

    def testStopAtNonOptionShort_test0_decomposed(self) -> None:
        args = ["-z", "-a", "-btoast"]
        cl = self._parser.parse1(self._options, args, True)

    def testStopAtNonOptionLong_test2_decomposed(self) -> None:
        args = ["--zop==1", "-abtoast", "--b=bar"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
        self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

    def testStopAtNonOptionLong_test1_decomposed(self) -> None:
        args = ["--zop==1", "-abtoast", "--b=bar"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertFalse(cl.hasOption2("a"), "Confirm -a is not set")
        self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")

    def testStopAtNonOptionLong_test0_decomposed(self) -> None:
        args = ["--zop==1", "-abtoast", "--b=bar"]
        cl = self._parser.parse1(self._options, args, True)

    def testStopAtExpectedArg_test3_decomposed(self) -> None:
        args = ["-b", "foo"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption0("b"), "Confirm -b is set")
        self.assertEqual("foo", cl.getOptionValue0("b"), "Confirm -b is set")
        self.assertTrue(
            len(cl.getArgList()) == 0, f"Confirm no extra args: {len(cl.getArgList())}"
        )

    def testStopAtExpectedArg_test2_decomposed(self) -> None:
        args = ["-b", "foo"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption0("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue0("b"), "foo", "Confirm -b is set")

    def testStopAtExpectedArg_test1_decomposed(self) -> None:
        args = ["-b", "foo"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption0("b"), "Confirm -b is set")

    def testStopAtExpectedArg_test0_decomposed(self) -> None:
        args = ["-b", "foo"]
        cl = self._parser.parse1(self._options, args, True)

    def testSingleDash_test3_decomposed(self) -> None:
        args = ["--copt", "-b", "-", "-a", "-"]
        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("-", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertEqual(
            1, len(cl.getArgList()), f"Confirm 1 extra arg: {len(cl.getArgList())}"
        )
        self.assertEqual(
            "-", cl.getArgList()[0], f"Confirm value of extra arg: {cl.getArgList()[0]}"
        )

    def testSingleDash_test2_decomposed(self) -> None:
        args = ["--copt", "-b", "-", "-a", "-"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue4("b"), "-", "Confirm arg of -b")

    def testSingleDash_test1_decomposed(self) -> None:
        args = ["--copt", "-b", "-", "-a", "-"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testSingleDash_test0_decomposed(self) -> None:
        args = ["--copt", "-b", "-", "-a", "-"]
        cl = self._parser.parse0(self._options, args)

    def testSimpleShort_test3_decomposed(self) -> None:
        args = ["-a", "-b", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue4("b"), "toast", "Confirm arg of -b")
        self.assertEqual(len(cl.getArgList()), 2, "Confirm size of extra args")

    def testSimpleShort_test2_decomposed(self) -> None:
        args = ["-a", "-b", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue4("b"), "toast", "Confirm arg of -b")

    def testSimpleShort_test1_decomposed(self) -> None:
        args = ["-a", "-b", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testSimpleShort_test0_decomposed(self) -> None:
        args = ["-a", "-b", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)

    def testSimpleLong_test3_decomposed(self) -> None:
        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)

        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertEqual("toast", cl.getOptionValue4("bfile"), "Confirm arg of --bfile")
        self.assertEqual(2, len(cl.getArgList()), "Confirm size of extra args")

    def testSimpleLong_test2_decomposed(self) -> None:
        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertEqual("toast", cl.getOptionValue4("bfile"), "Confirm arg of --bfile")

    def testSimpleLong_test1_decomposed(self) -> None:
        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testSimpleLong_test0_decomposed(self) -> None:
        args = ["--enable-a", "--bfile", "toast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)

    def testShortWithUnexpectedArgument_test5_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-f=bar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testShortWithUnexpectedArgument_test4_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-f=bar", e.getOption())
            return

    def testShortWithUnexpectedArgument_test3_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

    def testShortWithUnexpectedArgument_test2_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")

    def testShortWithUnexpectedArgument_test1_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testShortWithUnexpectedArgument_test0_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()

    def testShortWithoutEqual_test6_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testShortWithoutEqual_test5_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)

    def testShortWithoutEqual_test4_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)

    def testShortWithoutEqual_test3_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testShortWithoutEqual_test2_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testShortWithoutEqual_test1_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testShortWithoutEqual_test0_decomposed(self) -> None:
        args = ["-fbar"]
        options = Options()

    def testShortWithEqual_test6_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testShortWithEqual_test5_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)

    def testShortWithEqual_test4_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)

    def testShortWithEqual_test3_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testShortWithEqual_test2_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testShortWithEqual_test1_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testShortWithEqual_test0_decomposed(self) -> None:
        args = ["-f=bar"]
        options = Options()

    def testShortOptionQuoteHandling_test1_decomposed(self) -> None:
        args = ["-b", '"quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            "quoted string", cl.getOptionValue4("b"), 'Confirm -b "arg" strips quotes'
        )

    def testShortOptionQuoteHandling_test0_decomposed(self) -> None:
        args = ["-b", '"quoted string"']
        cl = self._parser.parse0(self._options, args)

    def testShortOptionConcatenatedQuoteHandling_test1_decomposed(self) -> None:
        args = ['-b"quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            "quoted string", cl.getOptionValue4("b"), 'Confirm -b"arg" strips quotes'
        )

    def testShortOptionConcatenatedQuoteHandling_test0_decomposed(self) -> None:
        args = ['-b"quoted string"']
        cl = self._parser.parse0(self._options, args)

    def testReuseOptionsTwice_test4_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        v_option = OptionBuilder.isRequired0().create1("v")
        opts.addOption0(v_option)

        # First parse with the required option present
        self._parser.parse0(opts, ["-v"])

        # Second parse without the required option, expecting an exception
        with pytest.raises(MissingOptionException):
            self._parser.parse0(opts, [])

    def testReuseOptionsTwice_test3_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create1("v")
        opts.addOption0(OptionBuilder.isRequired0().create1("v"))

    def testReuseOptionsTwice_test2_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create1("v")

    def testReuseOptionsTwice_test1_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()

    def testReuseOptionsTwice_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOverrideValues_test12_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}

        cmd = self._ParserTestCase__parse(self._parser, opts, args, properties)

        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))
        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue4("i"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOverrideValues_test11_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}

        cmd = self._ParserTestCase__parse(self._parser, opts, args, properties)

        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))
        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue4("i"))

    def testPropertyOverrideValues_test10_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}

        cmd = self._ParserTestCase__parse(self._parser, opts, args, properties)

        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))
        self.assertTrue(cmd.hasOption2("i"))

    def testPropertyOverrideValues_test9_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}

        cmd = self._ParserTestCase__parse(self._parser, opts, args, properties)

        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("found", cmd.getOptionValue4("j"))

    def testPropertyOverrideValues_test8_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}

        cmd = self._parse(self._parser, opts, args, properties)
        self.assertTrue(cmd.hasOption2("j"))

    def testPropertyOverrideValues_test7_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))
        args = ["-j", "found", "-i", "ink"]
        properties = {"j": "seek"}
        cmd = self._ParserTestCase__parse(self._parser, opts, args, properties)

    def testPropertyOverrideValues_test6_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")
        opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

    def testPropertyOverrideValues_test5_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()
        OptionBuilder.hasOptionalArgs0().create1("j")

    def testPropertyOverrideValues_test4_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        OptionBuilder.hasOptionalArgs0()

    def testPropertyOverrideValues_test3_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))

    def testPropertyOverrideValues_test2_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).create1("i")

    def testPropertyOverrideValues_test1_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)

    def testPropertyOverrideValues_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionUnexpected_test1_decomposed(self) -> None:
        opts = Options()
        properties = {
            "f": "true"
        }  # Simulating Java's Properties with a Python dictionary
        try:
            self.__parse(self._parser, opts, None, properties)
            pytest.fail("UnrecognizedOptionException expected")
        except UnrecognizedOptionException:
            pass

    def testPropertyOptionUnexpected_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionSingularValue_test8_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")
        option = OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        opts.addOption0(option)

        properties = {"hide": "seek"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

        self.assertTrue(cmd.hasOption2("hide"))
        self.assertEqual("seek", cmd.getOptionValue4("hide"))
        self.assertFalse(cmd.hasOption2("fake"))

    def testPropertyOptionSingularValue_test7_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")
        option = OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        opts.addOption0(option)

        properties = {"hide": "seek"}

        cmd = self._parser.parse2(opts, None, properties)

        self.assertTrue(cmd.hasOption2("hide"))
        self.assertEqual("seek", cmd.getOptionValue4("hide"))

    def testPropertyOptionSingularValue_test6_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")
        option = OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        opts.addOption0(option)

        properties = {"hide": "seek"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("hide"))

    def testPropertyOptionSingularValue_test5_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        opts.addOption0(OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0())

        properties = {"hide": "seek"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionSingularValue_test4_decomposed(self) -> None:
        opts = Options()
        option = OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        opts.addOption0(option)

    def testPropertyOptionSingularValue_test3_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()

    def testPropertyOptionSingularValue_test2_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)
        OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide")

    def testPropertyOptionSingularValue_test1_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasOptionalArgs1(2)

    def testPropertyOptionSingularValue_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionRequired_test5_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        option_f = OptionBuilder.isRequired0().create2("f")
        opts.addOption0(option_f)

        properties = {"f": "true"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("f"))

    def testPropertyOptionRequired_test4_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")
        opts.addOption0(OptionBuilder.isRequired0().create2("f"))

        properties = {"f": "true"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionRequired_test3_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        option = OptionBuilder.isRequired0().create2("f")
        opts.addOption0(option)

    def testPropertyOptionRequired_test2_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")

    def testPropertyOptionRequired_test1_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.isRequired0()

    def testPropertyOptionRequired_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionMultipleValues_test7_decomposed(self) -> None:
        opts = Options()
        option = OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k")
        opts.addOption0(option)

        properties = {"k": "one,two"}
        values = ["one", "two"]

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

        self.assertTrue(cmd.hasOption2("k"))
        self.assertEqual(values, cmd.getOptionValues0("k"))

    def testPropertyOptionMultipleValues_test6_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasArgs0()
        OptionBuilder.hasArgs0().withValueSeparator1(",")
        option = OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k")
        opts.addOption0(option)

        properties = {"k": "one,two"}
        values = ["one", "two"]

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("k"))

    def testPropertyOptionMultipleValues_test5_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasArgs0()
        OptionBuilder.hasArgs0().withValueSeparator1(",")
        option = OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k")
        opts.addOption0(option)

        properties = {"k": "one,two"}
        values = ["one", "two"]

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionMultipleValues_test4_decomposed(self) -> None:
        opts = Options()
        option = OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k")
        opts.addOption0(option)

    def testPropertyOptionMultipleValues_test3_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasArgs0()
        OptionBuilder.hasArgs0().withValueSeparator1(",")
        OptionBuilder.hasArgs0().withValueSeparator1(",").create1("k")

    def testPropertyOptionMultipleValues_test2_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasArgs0()
        OptionBuilder.hasArgs0().withValueSeparator1(",")

    def testPropertyOptionMultipleValues_test1_decomposed(self) -> None:
        opts = Options()
        OptionBuilder.hasArgs0()

    def testPropertyOptionMultipleValues_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionGroup_test14_decomposed(self) -> None:
        opts = Options()

        # Create and configure the first option group
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        # Create and configure the second option group
        group2 = OptionGroup()
        group2.addOption(Option("x", None))
        group2.addOption(Option("y", None))
        opts.addOptionGroup(group2)

        # Define the arguments and properties
        args = ["-a"]
        properties = {"b": "true", "x": "true"}

        # Parse the command line
        cmd = self._parse(self._parser, opts, args, properties)

        # Assertions
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("b"))
        self.assertTrue(cmd.hasOption2("x"))
        self.assertFalse(cmd.hasOption2("y"))

    def testPropertyOptionGroup_test13_decomposed(self) -> None:
        opts = Options()

        # Create the first option group
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        # Create the second option group
        group2 = OptionGroup()
        group2.addOption(Option("x", None))
        group2.addOption(Option("y", None))
        opts.addOptionGroup(group2)

        # Define the arguments and properties
        args = ["-a"]
        properties = {"b": "true", "x": "true"}

        # Parse the command line
        cmd = self._parse(self._parser, opts, args, properties)

    def testPropertyOptionGroup_test12_decomposed(self) -> None:
        opts = Options()

        # Create the first option group
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        # Create the second option group
        group2 = OptionGroup()
        group2.addOption(Option("x", None))
        group2.addOption(Option("y", None))
        opts.addOptionGroup(group2)

    def testPropertyOptionGroup_test11_decomposed(self) -> None:
        opts = Options()

        # Create the first option group
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        # Create the second option group
        group2 = OptionGroup()
        group2.addOption(Option("x", None))
        group2.addOption(Option("y", None))
        opts.addOptionGroup(group2)

    def testPropertyOptionGroup_test10_decomposed(self) -> None:
        opts = Options()

        # Create the first option group
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        # Create the second option group
        group2 = OptionGroup()
        group2.addOption(Option("x", None))
        group2.addOption(Option("y", None))

    def testPropertyOptionGroup_test9_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

        group2 = OptionGroup()
        group2.addOption(Option("x", None))

    def testPropertyOptionGroup_test8_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)
        group2 = OptionGroup()
        group2.addOption(Option("x", None))

    def testPropertyOptionGroup_test7_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)
        group2 = OptionGroup()

    def testPropertyOptionGroup_test6_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))
        opts.addOptionGroup(group1)

    def testPropertyOptionGroup_test5_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))
        group1.addOption(Option("b", None))

    def testPropertyOptionGroup_test4_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        option_a = Option("a", None)
        group1.addOption(option_a)
        option_b = Option("b", None)

    def testPropertyOptionGroup_test3_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        option1 = Option("a", None)
        group1.addOption(option1)

    def testPropertyOptionGroup_test2_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()
        group1.addOption(Option("a", None))

    def testPropertyOptionGroup_test1_decomposed(self) -> None:
        opts = Options()
        group1 = OptionGroup()

    def testPropertyOptionGroup_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertyOptionFlags_test15_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "just a string", "e": ""}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "0", "c": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))

    def testPropertyOptionFlags_test14_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "just a string", "e": ""}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "0", "c": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionFlags_test13_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "just a string", "e": ""}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

    def testPropertyOptionFlags_test12_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "just a string", "e": ""}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionFlags_test11_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

    def testPropertyOptionFlags_test10_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "TRUE", "c": "nO", "e": "TrUe"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionFlags_test9_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        e_option = OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(e_option)

        properties = {"a": "true", "c": "yes", "e": "1"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}
        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertFalse(cmd.hasOption2("a"))
        self.assertFalse(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

    def testPropertyOptionFlags_test8_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)
        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

        properties = {"a": "false", "c": "no", "e": "0"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionFlags_test7_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        option_e = OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(option_e)

        properties = {"a": "true", "c": "yes", "e": "1"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

        self.assertTrue(cmd.hasOption2("a"))
        self.assertTrue(cmd.hasOption2("c"))
        self.assertTrue(cmd.hasOption2("e"))

    def testPropertyOptionFlags_test6_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))

        properties = {"a": "true", "c": "yes", "e": "1"}

        cmd = self._ParserTestCase__parse(self._parser, opts, None, properties)

    def testPropertyOptionFlags_test5_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        option_e = OptionBuilder.hasOptionalArg().create1("e")
        opts.addOption0(option_e)

    def testPropertyOptionFlags_test4_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("e")

    def testPropertyOptionFlags_test3_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")
        OptionBuilder.hasOptionalArg()

    def testPropertyOptionFlags_test2_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption3("c", "c", False, "toggle -c")

    def testPropertyOptionFlags_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")

    def testPropertyOptionFlags_test0_decomposed(self) -> None:
        opts = Options()

    def testPropertiesOption2_test10_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        props = cl.getOptionProperties1("D")

        self.assertIsNotNone(props, "null properties")
        self.assertEqual(2, len(props), f"number of properties in {props}")
        self.assertEqual("true", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")

        args_left = cl.getArgList()
        self.assertEqual(0, len(args_left), "Should be no arg left")

    def testPropertiesOption2_test9_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option_builder = OptionBuilder.withValueSeparator0()
        option_builder = option_builder.hasOptionalArgs1(2)
        option = option_builder.create1("D")
        options.addOption0(option)

        cl = self._parser.parse0(options, args)
        props = cl.getOptionProperties1("D")

        self.assertIsNotNone(props, "null properties")
        self.assertEqual(2, len(props), f"number of properties in {props}")
        self.assertEqual("true", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")

        args_left = cl.getArgList()

    def testPropertiesOption2_test8_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        props = cl.getOptionProperties1("D")

        self.assertIsNotNone(props, "null properties")
        self.assertEqual(2, len(props), f"number of properties in {props}")
        self.assertEqual("true", props.get("param1"), "property 1")
        self.assertEqual("value2", props.get("param2"), "property 2")

    def testPropertiesOption2_test7_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        props = cl.getOptionProperties1("D")
        self.assertIsNotNone(props, "null properties")
        self.assertEqual(2, len(props), f"number of properties in {props}")

    def testPropertiesOption2_test6_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        props = cl.getOptionProperties1("D")

    def testPropertiesOption2_test5_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option = OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)

    def testPropertiesOption2_test4_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        option_builder = OptionBuilder.withValueSeparator0()
        option_builder = option_builder.hasOptionalArgs1(2)
        option = option_builder.create1("D")
        options.addOption0(option)

    def testPropertiesOption2_test3_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2).create1("D")

    def testPropertiesOption2_test2_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasOptionalArgs1(2)

    def testPropertiesOption2_test1_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()
        OptionBuilder.withValueSeparator0()

    def testPropertiesOption2_test0_decomposed(self) -> None:
        args = ["-Dparam1", "-Dparam2=value2", "-D"]
        options = Options()

    def testPropertiesOption1_test11_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        values = cl.getOptionValues2("J")
        self.assertIsNotNone(values, "null values")
        self.assertEqual(len(values), 4, "number of values")
        self.assertEqual(values[0], "source", "value 1")
        self.assertEqual(values[1], "1.5", "value 2")
        self.assertEqual(values[2], "target", "value 3")
        self.assertEqual(values[3], "1.5", "value 4")
        args_left = cl.getArgList()
        self.assertEqual(len(args_left), 1, "Should be 1 arg left")
        self.assertEqual(args_left[0], "foo", "Expecting foo")

    def testPropertiesOption1_test10_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        option_builder = OptionBuilder.withValueSeparator0()
        option_builder = option_builder.hasArgs1(2)
        option = option_builder.create1("J")
        options.addOption0(option)

        cl = self._parser.parse0(options, args)
        values = cl.getOptionValues2("J")

        self.assertIsNotNone(values, "null values")
        self.assertEqual(len(values), 4, "number of values")
        self.assertEqual(values[0], "source", "value 1")
        self.assertEqual(values[1], "1.5", "value 2")
        self.assertEqual(values[2], "target", "value 3")
        self.assertEqual(values[3], "1.5", "value 4")

        args_left = cl.getArgList()

    def testPropertiesOption1_test9_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        values = cl.getOptionValues2("J")
        self.assertIsNotNone(values, "null values")
        self.assertEqual(len(values), 4, "number of values")
        self.assertEqual(values[0], "source", "value 1")
        self.assertEqual(values[1], "1.5", "value 2")
        self.assertEqual(values[2], "target", "value 3")
        self.assertEqual(values[3], "1.5", "value 4")

    def testPropertiesOption1_test8_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        values = cl.getOptionValues2("J")
        self.assertIsNotNone(values, "null values")
        self.assertEqual(len(values), 4, "number of values")
        self.assertEqual(values[0], "source", "value 1")
        self.assertEqual(values[1], "1.5", "value 2")

    def testPropertiesOption1_test7_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()

        # Configure the OptionBuilder and add the option to options
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Retrieve the option values
        values = cl.getOptionValues2("J")

        # Assertions
        self.assertIsNotNone(values, "null values")
        self.assertEqual(len(values), 4, "number of values")

    def testPropertiesOption1_test6_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)
        values = cl.getOptionValues2("J")

    def testPropertiesOption1_test5_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)

    def testPropertiesOption1_test4_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        option = OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")
        options.addOption0(option)

    def testPropertiesOption1_test3_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)
        OptionBuilder.withValueSeparator0().hasArgs1(2).create1("J")

    def testPropertiesOption1_test2_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()
        OptionBuilder.withValueSeparator0().hasArgs1(2)

    def testPropertiesOption1_test1_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()
        OptionBuilder.withValueSeparator0()

    def testPropertiesOption1_test0_decomposed(self) -> None:
        args = ["-Jsource=1.5", "-J", "target", "1.5", "foo"]
        options = Options()

    def testPartialLongOptionSingleDash_test8_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "-v" option with an argument
        OptionBuilder.hasArg0()
        v_option = OptionBuilder.hasArg0().create1("v")
        options.addOption0(v_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("version"), "Confirm --version is set")
        self.assertFalse(cl.hasOption2("v"), "Confirm -v is not set")

    def testPartialLongOptionSingleDash_test7_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Create an option with long option "version"
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Create an option with short option 'v' that accepts an argument
        OptionBuilder.hasArg0()
        v_option = OptionBuilder.hasArg0().create1("v")
        options.addOption0(v_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

    def testPartialLongOptionSingleDash_test6_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("v")
        options.addOption0(OptionBuilder.hasArg0().create1("v"))

    def testPartialLongOptionSingleDash_test5_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("v")

    def testPartialLongOptionSingleDash_test4_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.hasArg0()

    def testPartialLongOptionSingleDash_test3_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

    def testPartialLongOptionSingleDash_test2_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testPartialLongOptionSingleDash_test1_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testPartialLongOptionSingleDash_test0_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

    def testOptionGroupLong_test11_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

        options = Options()
        options.addOptionGroup(group)

        cl = self._parser.parse0(options, ["--bar"])

        self.assertTrue(cl.hasOption2("bar"))
        self.assertEqual("bar", group.getSelected(), "selected option")

    def testOptionGroupLong_test10_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

        options = Options()
        options.addOptionGroup(group)

        cl = self._parser.parse0(options, ["--bar"])
        self.assertTrue(cl.hasOption2("bar"))

    def testOptionGroupLong_test9_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

        options = Options()
        options.addOptionGroup(group)

        cl = self._parser.parse0(options, ["--bar"])

    def testOptionGroupLong_test8_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())
        options = Options()
        options.addOptionGroup(group)

    def testOptionGroupLong_test7_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())
        options = Options()

    def testOptionGroupLong_test6_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()
        group.addOption(OptionBuilder.withLongOpt("bar").create0())

    def testOptionGroupLong_test5_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").create0()

    def testOptionGroupLong_test4_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())
        OptionBuilder.withLongOpt("bar")

    def testOptionGroupLong_test3_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()
        group.addOption(OptionBuilder.withLongOpt("foo").create0())

    def testOptionGroupLong_test2_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create0()

    def testOptionGroupLong_test1_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.withLongOpt("foo")

    def testOptionGroupLong_test0_decomposed(self) -> None:
        group = OptionGroup()

    def testOptionGroup_test8_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

        options = Options()
        options.addOptionGroup(group)

        self._parser.parse0(options, ["-b"])

        self.assertEqual("b", group.getSelected(), "selected option")

    def testOptionGroup_test7_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

        options = Options()
        options.addOptionGroup(group)

        self._parser.parse0(options, ["-b"])

    def testOptionGroup_test6_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        options = Options()
        options.addOptionGroup(group)

    def testOptionGroup_test5_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        options = Options()

    def testOptionGroup_test4_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

    def testOptionGroup_test3_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create2("a")
        group.addOption(OptionBuilder.create2("a"))
        OptionBuilder.create2("b")

    def testOptionGroup_test2_decomposed(self) -> None:
        group = OptionGroup()
        option = OptionBuilder.create2("a")
        group.addOption(option)

    def testOptionGroup_test1_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create2("a")

    def testOptionGroup_test0_decomposed(self) -> None:
        group = OptionGroup()

    def testOptionAndRequiredOption_test10_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)
        cl = self._parser.parse0(options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("file", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertTrue(cl.getArgList().isEmpty(), "Confirm NO of extra args")

    def testOptionAndRequiredOption_test9_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)
        cl = self._parser.parse0(options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual(cl.getOptionValue4("b"), "file", "Confirm arg of -b")

    def testOptionAndRequiredOption_test8_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)
        cl = self._parser.parse0(options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testOptionAndRequiredOption_test7_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)
        cl = self._parser.parse0(options, args)

    def testOptionAndRequiredOption_test6_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)

    def testOptionAndRequiredOption_test5_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")

    def testOptionAndRequiredOption_test4_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()

    def testOptionAndRequiredOption_test3_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()

    def testOptionAndRequiredOption_test2_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")

    def testOptionAndRequiredOption_test1_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

    def testOptionAndRequiredOption_test0_decomposed(self) -> None:
        args = ["-a", "-b", "file"]
        options = Options()

    def testNegativeOption_test2_decomposed(self) -> None:
        args = ["-b", "-1"]
        self._options.addOption1("1", False, None)
        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-1", cl.getOptionValue4("b"))

    def testNegativeOption_test1_decomposed(self) -> None:
        args = ["-b", "-1"]
        self._options.addOption1("1", False, None)
        cl = self._parser.parse0(self._options, args)

    def testNegativeOption_test0_decomposed(self) -> None:
        args = ["-b", "-1"]
        self._options.addOption1("1", False, None)

    def testNegativeArgument_test1_decomposed(self) -> None:
        args = ["-b", "-1"]
        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-1", cl.getOptionValue4("b"))

    def testNegativeArgument_test0_decomposed(self) -> None:
        args = ["-b", "-1"]
        cl = self._parser.parse0(self._options, args)

    def testMultipleWithLong_test7_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)

        # Confirm -c is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Confirm 3 extra args
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        # Get arguments and re-parse
        cl = self._parser.parse0(self._options, cl.getArgs())

        # Confirm -c is not set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Confirm -b is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

        # Confirm arg of -b
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")

        # Confirm 1 extra arg
        self.assertEqual(
            1, len(cl.getArgList()), f"Confirm 1 extra arg: {len(cl.getArgList())}"
        )

        # Confirm value of extra arg
        self.assertEqual(
            "foobar",
            cl.getArgList()[0],
            f"Confirm value of extra arg: {cl.getArgList()[0]}",
        )

    def testMultipleWithLong_test6_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]

        # Parse the arguments with the parser
        cl = self._parser.parse1(self._options, args, True)

        # Assert that the "-c" option is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Assert that there are 3 extra arguments
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        # Get the remaining arguments
        remaining_args = cl.getArgs()

        # Parse the remaining arguments again
        cl = self._parser.parse0(self._options, remaining_args)

        # Assert that the "-c" option is no longer set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Assert that the "-b" option is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

        # Assert that the value of the "-b" option is "toast"
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")

    def testMultipleWithLong_test5_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]

        # Parse the arguments with the parser
        cl = self._parser.parse1(self._options, args, True)

        # Assert that the "-c" option is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Assert that there are 3 extra arguments
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        # Get the remaining arguments
        remaining_args = cl.getArgs()

        # Parse the remaining arguments again
        cl = self._parser.parse0(self._options, remaining_args)

        # Assert that the "-c" option is no longer set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Assert that the "-b" option is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testMultipleWithLong_test4_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            len(cl.getArgList()), 3, f"Confirm 3 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())

    def testMultipleWithLong_test3_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()

    def testMultipleWithLong_test2_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

    def testMultipleWithLong_test1_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

    def testMultipleWithLong_test0_decomposed(self) -> None:
        args = ["--copt", "foobar", "--bfile", "toast"]
        cl = self._parser.parse1(self._options, args, True)

    def testMultiple_test7_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)

        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())

        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertEqual(
            1, len(cl.getArgList()), f"Confirm 1 extra arg: {len(cl.getArgList())}"
        )
        self.assertEqual(
            "foobar",
            cl.getArgList()[0],
            f"Confirm value of extra arg: {cl.getArgList()[0]}",
        )

    def testMultiple_test6_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)

        # Confirm -c is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Confirm 3 extra args
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())

        # Confirm -c is not set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Confirm -b is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

        # Confirm arg of -b
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")

    def testMultiple_test5_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)

        # Assert that the "-c" option is set
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

        # Assert that there are 3 extra arguments
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

        # Get the arguments and re-parse
        cl = self._parser.parse0(self._options, cl.getArgs())

        # Assert that the "-c" option is no longer set
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is not set")

        # Assert that the "-b" option is set
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")

    def testMultiple_test4_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()
        cl = self._parser.parse0(self._options, cl.getArgs())

    def testMultiple_test3_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )
        cl.getArgs()

    def testMultiple_test2_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(
            3, len(cl.getArgList()), f"Confirm 3 extra args: {len(cl.getArgList())}"
        )

    def testMultiple_test1_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

    def testMultiple_test0_decomposed(self) -> None:
        args = ["-c", "foobar", "-b", "toast"]
        cl = self._parser.parse1(self._options, args, True)

    def testMissingRequiredOptions_test12_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        options.addOption0(
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        OptionBuilder.withLongOpt("cfile")
        OptionBuilder.withLongOpt("cfile").hasArg0()
        OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0()
        options.addOption0(
            OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0().create1("c")
        )

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Incorrect exception message",
                "Missing required options: b, c",
                e.getMessage(),
            )
            self.assertTrue("b" in e.getMissingOptions())
            self.assertTrue("c" in e.getMissingOptions())
        except ParseException:
            self.fail("expected to catch MissingOptionException")

    def testMissingRequiredOptions_test11_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)

        OptionBuilder.withLongOpt("cfile")
        OptionBuilder.withLongOpt("cfile").hasArg0()
        OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0()
        c_option = (
            OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0().create1("c")
        )
        options.addOption0(c_option)

    def testMissingRequiredOptions_test10_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)

        OptionBuilder.withLongOpt("cfile")
        OptionBuilder.withLongOpt("cfile").hasArg0()
        OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0()
        c_option = (
            OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0().create1("c")
        )

    def testMissingRequiredOptions_test9_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)

        OptionBuilder.withLongOpt("cfile")
        OptionBuilder.withLongOpt("cfile").hasArg0()
        OptionBuilder.withLongOpt("cfile").hasArg0().isRequired0()

    def testMissingRequiredOptions_test8_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)

        OptionBuilder.withLongOpt("cfile")
        OptionBuilder.withLongOpt("cfile").hasArg0()

    def testMissingRequiredOptions_test7_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        b_option = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(b_option)
        OptionBuilder.withLongOpt("cfile")

    def testMissingRequiredOptions_test6_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)

    def testMissingRequiredOptions_test5_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")

    def testMissingRequiredOptions_test4_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()

    def testMissingRequiredOptions_test3_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()

    def testMissingRequiredOptions_test2_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")

    def testMissingRequiredOptions_test1_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

    def testMissingRequiredOptions_test0_decomposed(self) -> None:
        args = ["-a"]
        options = Options()

    def testMissingRequiredOption_test7_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)

        try:
            self._parser.parse0(options, args)
            self.fail("exception should have been thrown")
        except MissingOptionException as e:
            self.assertEqual(
                "Missing required option: b",
                e.getMessage(),
                "Incorrect exception message",
            )
            self.assertTrue("b" in e.getMissingOptions())
        except ParseException:
            self.fail("expected to catch MissingOptionException")

    def testMissingRequiredOption_test6_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        option_b = (
            OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")
        )
        options.addOption0(option_b)

    def testMissingRequiredOption_test5_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0().create1("b")

    def testMissingRequiredOption_test4_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()
        OptionBuilder.withLongOpt("bfile").hasArg0().isRequired0()

    def testMissingRequiredOption_test3_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")
        OptionBuilder.withLongOpt("bfile").hasArg0()

    def testMissingRequiredOption_test2_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)
        OptionBuilder.withLongOpt("bfile")

    def testMissingRequiredOption_test1_decomposed(self) -> None:
        args = ["-a"]
        options = Options()
        options.addOption3("a", "enable-a", False, None)

    def testMissingRequiredOption_test0_decomposed(self) -> None:
        args = ["-a"]
        options = Options()

    def testMissingRequiredGroup_test11_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)
        options.addOption0(OptionBuilder.isRequired0().create2("c"))

        try:
            self._parser.parse0(options, ["-c"])
            self.fail("MissingOptionException not thrown")
        except MissingOptionException as e:
            self.assertEqual(1, len(e.getMissingOptions()))
            self.assertTrue(isinstance(e.getMissingOptions()[0], OptionGroup))
        except ParseException:
            self.fail("Expected to catch MissingOptionException")

    def testMissingRequiredGroup_test10_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)
        options.addOption0(OptionBuilder.isRequired0().create2("c"))

    def testMissingRequiredGroup_test9_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("c")

    def testMissingRequiredGroup_test8_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

        options = Options()
        options.addOptionGroup(group)

        OptionBuilder.isRequired0()

    def testMissingRequiredGroup_test7_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)
        options = Options()
        options.addOptionGroup(group)

    def testMissingRequiredGroup_test6_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)
        options = Options()

    def testMissingRequiredGroup_test5_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create2("a")
        group.addOption(OptionBuilder.create2("a"))
        OptionBuilder.create2("b")
        group.addOption(OptionBuilder.create2("b"))
        group.setRequired(True)

    def testMissingRequiredGroup_test4_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create2("a"))
        group.addOption(OptionBuilder.create2("b"))

    def testMissingRequiredGroup_test3_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create2("a")
        group.addOption(OptionBuilder.create2("a"))
        OptionBuilder.create2("b")

    def testMissingRequiredGroup_test2_decomposed(self) -> None:
        group = OptionGroup()
        option_a = OptionBuilder.create2("a")
        group.addOption(option_a)

    def testMissingRequiredGroup_test1_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create2("a")

    def testMissingRequiredGroup_test0_decomposed(self) -> None:
        group = OptionGroup()

    def testMissingArgWithBursting_test1_decomposed(self) -> None:
        args = ["-acb"]
        caught = False
        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")
        self.assertTrue(caught, "Confirm MissingArgumentException caught")

    def testMissingArgWithBursting_test0_decomposed(self) -> None:
        args = ["-acb"]
        caught = False
        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")

        self.assertTrue(caught, "Expected MissingArgumentException was not thrown")

    def testMissingArg_test1_decomposed(self) -> None:
        args = ["-b"]
        caught = False
        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")
        self.assertTrue(caught, "Confirm MissingArgumentException caught")

    def testMissingArg_test0_decomposed(self) -> None:
        args = ["-b"]
        caught = False
        try:
            self._parser.parse0(self._options, args)
        except MissingArgumentException as e:
            caught = True
            self.assertEqual("b", e.getOption().getOpt(), "option missing an argument")
        self.assertTrue(caught, "Expected MissingArgumentException was not thrown")

    def testLongWithUnexpectedArgument2_test5_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-foobar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testLongWithUnexpectedArgument2_test4_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("-foobar", e.getOption())
            return

    def testLongWithUnexpectedArgument2_test3_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").create1("f"))

    def testLongWithUnexpectedArgument2_test2_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")

    def testLongWithUnexpectedArgument2_test1_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithUnexpectedArgument2_test0_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()

    def testLongWithUnexpectedArgument1_test5_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("--foo=bar", e.getOption())
            return

        self.fail("UnrecognizedOptionException not thrown")

    def testLongWithUnexpectedArgument1_test4_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

        try:
            self._parser.parse0(options, args)
        except UnrecognizedOptionException as e:
            self.assertEqual("--foo=bar", e.getOption())
            return

    def testLongWithUnexpectedArgument1_test3_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        option = OptionBuilder.withLongOpt("foo").create1("f")
        options.addOption0(option)

    def testLongWithUnexpectedArgument1_test2_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").create1("f")

    def testLongWithUnexpectedArgument1_test1_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithUnexpectedArgument1_test0_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()

    def testLongWithoutEqualSingleDash_test6_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse0(options, args)
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithoutEqualSingleDash_test5_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse0(options, args)

    def testLongWithoutEqualSingleDash_test4_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

    def testLongWithoutEqualSingleDash_test3_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testLongWithoutEqualSingleDash_test2_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testLongWithoutEqualSingleDash_test1_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithoutEqualSingleDash_test0_decomposed(self) -> None:
        args = ["-foobar"]
        options = Options()

    def testLongWithoutEqualDoubleDash_test6_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse1(options, args, True)
        self.assertFalse(cl.hasOption2("foo"))

    def testLongWithoutEqualDoubleDash_test5_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse1(options, args, True)

    def testLongWithoutEqualDoubleDash_test4_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)

    def testLongWithoutEqualDoubleDash_test3_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testLongWithoutEqualDoubleDash_test2_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testLongWithoutEqualDoubleDash_test1_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithoutEqualDoubleDash_test0_decomposed(self) -> None:
        args = ["--foobar"]
        options = Options()

    def testLongWithEqualSingleDash_test6_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse0(options, args)
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithEqualSingleDash_test5_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)
        cl = self._parser.parse0(options, args)

    def testLongWithEqualSingleDash_test4_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        option = OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(option)

    def testLongWithEqualSingleDash_test3_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testLongWithEqualSingleDash_test2_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testLongWithEqualSingleDash_test1_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithEqualSingleDash_test0_decomposed(self) -> None:
        args = ["-foo=bar"]
        options = Options()

    def testLongWithEqualDoubleDash_test6_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse0(options, args)
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testLongWithEqualDoubleDash_test5_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))
        cl = self._parser.parse0(options, args)

    def testLongWithEqualDoubleDash_test4_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")
        options.addOption0(OptionBuilder.withLongOpt("foo").hasArg0().create1("f"))

    def testLongWithEqualDoubleDash_test3_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()
        OptionBuilder.withLongOpt("foo").hasArg0().create1("f")

    def testLongWithEqualDoubleDash_test2_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasArg0()

    def testLongWithEqualDoubleDash_test1_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testLongWithEqualDoubleDash_test0_decomposed(self) -> None:
        args = ["--foo=bar"]
        options = Options()

    def testLongOptionWithEqualsQuoteHandling_test1_decomposed(self) -> None:
        args = ['--bfile="quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" strips quotes',
        )

    def testLongOptionWithEqualsQuoteHandling_test0_decomposed(self) -> None:
        args = ['--bfile="quoted string"']
        cl = self._parser.parse0(self._options, args)

    def testLongOptionQuoteHandling_test1_decomposed(self) -> None:
        args = ["--bfile", '"quoted string"']
        cl = self._parser.parse0(self._options, args)
        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile "arg" strips quotes',
        )

    def testLongOptionQuoteHandling_test0_decomposed(self) -> None:
        args = ["--bfile", '"quoted string"']
        cl = self._parser.parse0(self._options, args)

    def testDoubleDash2_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("n")
        options.addOption0(OptionBuilder.hasArg0().create1("n"))
        OptionBuilder.create1("m")
        options.addOption0(OptionBuilder.create1("m"))

        try:
            self._parser.parse0(options, ["-n", "--", "-m"])
            pytest.fail("MissingArgumentException not thrown for option -n")
        except MissingArgumentException as e:
            self.assertIsNotNone(e.getOption(), "option null")
            self.assertEqual("n", e.getOption().getOpt())

    def testDoubleDash2_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("n")
        options.addOption0(OptionBuilder.hasArg0().create1("n"))
        OptionBuilder.create1("m")
        options.addOption0(OptionBuilder.create1("m"))

    def testDoubleDash2_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("n")
        options.addOption0(OptionBuilder.hasArg0().create1("n"))
        OptionBuilder.create1("m")

    def testDoubleDash2_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("n")
        options.addOption0(OptionBuilder.hasArg0().create1("n"))

    def testDoubleDash2_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("n")

    def testDoubleDash2_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasArg0()

    def testDoubleDash2_test0_decomposed(self) -> None:
        options = Options()

    def testDoubleDash1_test2_decomposed(self) -> None:
        args = ["--copt", "--", "-b", "toast"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")
        self.assertEqual(
            2, len(cl.getArgList()), f"Confirm 2 extra args: {len(cl.getArgList())}"
        )

    def testDoubleDash1_test1_decomposed(self) -> None:
        args = ["--copt", "--", "-b", "toast"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertFalse(cl.hasOption2("b"), "Confirm -b is not set")

    def testDoubleDash1_test0_decomposed(self) -> None:
        args = ["--copt", "--", "-b", "toast"]
        cl = self._parser.parse0(self._options, args)

    def testBursting_test3_decomposed(self) -> None:
        args = ["-acbtoast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual("toast", cl.getOptionValue4("b"), "Confirm arg of -b")
        self.assertEqual(2, len(cl.getArgList()), "Confirm size of extra args")

    def testBursting_test2_decomposed(self) -> None:
        args = ["-acbtoast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")
        self.assertEqual(cl.getOptionValue4("b"), "toast", "Confirm arg of -b")

    def testBursting_test1_decomposed(self) -> None:
        args = ["-acbtoast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)
        self.assertTrue(cl.hasOption2("a"), "Confirm -a is set")
        self.assertTrue(cl.hasOption2("b"), "Confirm -b is set")
        self.assertTrue(cl.hasOption2("c"), "Confirm -c is set")

    def testBursting_test0_decomposed(self) -> None:
        args = ["-acbtoast", "foo", "bar"]
        cl = self._parser.parse0(self._options, args)

    def testArgumentStartingWithHyphen_test1_decomposed(self) -> None:
        args = ["-b", "-foo"]
        cl = self._parser.parse0(self._options, args)
        self.assertEqual("-foo", cl.getOptionValue4("b"))

    def testArgumentStartingWithHyphen_test0_decomposed(self) -> None:
        args = ["-b", "-foo"]
        cl = self._parser.parse0(self._options, args)

    def testAmbiguousPartialLongOption4_test9_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Confirm AmbiguousOptionException caught")

    def testAmbiguousPartialLongOption4_test8_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Expected AmbiguousOptionException was not thrown")

    def testAmbiguousPartialLongOption4_test7_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(
            OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        )

    def testAmbiguousPartialLongOption4_test6_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()

    def testAmbiguousPartialLongOption4_test5_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()

    def testAmbiguousPartialLongOption4_test4_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")

    def testAmbiguousPartialLongOption4_test3_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

    def testAmbiguousPartialLongOption4_test2_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testAmbiguousPartialLongOption4_test1_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testAmbiguousPartialLongOption4_test0_decomposed(self) -> None:
        args = ["-ver=1"]
        options = Options()

    def testAmbiguousPartialLongOption3_test9_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("--ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Confirm MissingArgumentException caught")

    def testAmbiguousPartialLongOption3_test8_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("--ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "AmbiguousOptionException was not caught")

    def testAmbiguousPartialLongOption3_test7_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

        # Define the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Define the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        verbose_option = OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()
        options.addOption0(verbose_option)

    def testAmbiguousPartialLongOption3_test6_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()
        OptionBuilder.withLongOpt("verbose").hasOptionalArg().create0()

    def testAmbiguousPartialLongOption3_test5_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").hasOptionalArg()

    def testAmbiguousPartialLongOption3_test4_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")

    def testAmbiguousPartialLongOption3_test3_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

    def testAmbiguousPartialLongOption3_test2_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testAmbiguousPartialLongOption3_test1_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testAmbiguousPartialLongOption3_test0_decomposed(self) -> None:
        args = ["--ver=1"]
        options = Options()

    def testAmbiguousPartialLongOption2_test8_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Adding "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Adding "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Confirm AmbiguousOptionException caught")

    def testAmbiguousPartialLongOption2_test7_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Adding "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Adding "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("-ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Expected AmbiguousOptionException was not thrown")

    def testAmbiguousPartialLongOption2_test6_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

        # Create and add the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Create and add the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

    def testAmbiguousPartialLongOption2_test5_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()

    def testAmbiguousPartialLongOption2_test4_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")

    def testAmbiguousPartialLongOption2_test3_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(option)

    def testAmbiguousPartialLongOption2_test2_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testAmbiguousPartialLongOption2_test1_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testAmbiguousPartialLongOption2_test0_decomposed(self) -> None:
        args = ["-ver"]
        options = Options()

    def testAmbiguousPartialLongOption1_test8_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

        # Add "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Add "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("--ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Confirm MissingArgumentException caught")

    def testAmbiguousPartialLongOption1_test7_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

        # Adding "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Adding "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

        caught = False
        try:
            self._parser.parse0(options, args)
        except AmbiguousOptionException as e:
            caught = True
            self.assertEqual("--ver", e.getOption(), "Partial option")
            self.assertIsNotNone(e.getMatchingOptions(), "Matching options null")
            self.assertEqual(2, len(e.getMatchingOptions()), "Matching options size")

        self.assertTrue(caught, "Expected AmbiguousOptionException was not thrown")

    def testAmbiguousPartialLongOption1_test6_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

        # Create and add the "version" option
        OptionBuilder.withLongOpt("version")
        version_option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(version_option)

        # Create and add the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

    def testAmbiguousPartialLongOption1_test5_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()

    def testAmbiguousPartialLongOption1_test4_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")

    def testAmbiguousPartialLongOption1_test3_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

    def testAmbiguousPartialLongOption1_test2_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testAmbiguousPartialLongOption1_test1_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testAmbiguousPartialLongOption1_test0_decomposed(self) -> None:
        args = ["--ver"]
        options = Options()

    def testAmbiguousLongWithoutEqualSingleDash_test11_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

        # Define the "foo" option
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        foo_option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(foo_option)

        # Define the "bar" option
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()
        bar_option = OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        options.addOption0(bar_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("b"))
        self.assertTrue(cl.hasOption2("f"))
        self.assertEqual("bar", cl.getOptionValue4("foo"))

    def testAmbiguousLongWithoutEqualSingleDash_test10_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

        # Define the "foo" option
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        foo_option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(foo_option)

        # Define the "bar" option
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()
        bar_option = OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        options.addOption0(bar_option)

        # Parse the command line arguments
        cl = self._parser.parse0(options, args)

        # Assertions
        self.assertTrue(cl.hasOption2("b"))
        self.assertTrue(cl.hasOption2("f"))

    def testAmbiguousLongWithoutEqualSingleDash_test9_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

        # Adding "foo" option with optional argument
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        foo_option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(foo_option)

        # Adding "bar" option with optional argument
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()
        bar_option = OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        options.addOption0(bar_option)

        # Parsing the command line arguments
        cl = self._parser.parse0(options, args)

    def testAmbiguousLongWithoutEqualSingleDash_test8_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

        # Define "foo" option
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        foo_option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(foo_option)

        # Define "bar" option
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()
        bar_option = OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        options.addOption0(bar_option)

    def testAmbiguousLongWithoutEqualSingleDash_test7_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        foo_option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(foo_option)

        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()
        bar_option = OptionBuilder.withLongOpt("bar").hasOptionalArg().create1("b")
        options.addOption0(bar_option)

    def testAmbiguousLongWithoutEqualSingleDash_test6_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        options.addOption0(
            OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        )
        OptionBuilder.withLongOpt("bar")
        OptionBuilder.withLongOpt("bar").hasOptionalArg()

    def testAmbiguousLongWithoutEqualSingleDash_test5_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(
            OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        )
        OptionBuilder.withLongOpt("bar")

    def testAmbiguousLongWithoutEqualSingleDash_test4_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        option = OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")
        options.addOption0(option)

    def testAmbiguousLongWithoutEqualSingleDash_test3_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()
        OptionBuilder.withLongOpt("foo").hasOptionalArg().create1("f")

    def testAmbiguousLongWithoutEqualSingleDash_test2_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")
        OptionBuilder.withLongOpt("foo").hasOptionalArg()

    def testAmbiguousLongWithoutEqualSingleDash_test1_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()
        OptionBuilder.withLongOpt("foo")

    def testAmbiguousLongWithoutEqualSingleDash_test0_decomposed(self) -> None:
        args = ["-b", "-foobar"]
        options = Options()

    def setUp(self) -> None:
        self._options = (
            Options()
            .addOption3("a", "enable-a", False, "turn [a] on or off")
            .addOption3("b", "bfile", True, "set the value of [b]")
            .addOption3("c", "copt", False, "turn [c] on or off")
        )

    def __parse(
        self,
        parser: CommandLineParser,
        opts: Options,
        args: typing.List[str],
        properties: typing.Union[configparser.ConfigParser, typing.Dict],
    ) -> CommandLine:
        if isinstance(parser, Parser):
            return parser.parse2(opts, args, properties)
        if isinstance(parser, DefaultParser):
            return parser.parse2(opts, args, properties)
        raise NotImplementedError("Default options not supported by this parser")
