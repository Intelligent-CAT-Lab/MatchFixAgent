from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI265Test(unittest.TestCase):

    __options: Options = None

    __parser: DefaultParser = None

    def testshouldParseShortOptionWithValue_test2_decomposed(self) -> None:
        short_option_with_value = ["-t1", "path/to/my/db"]
        command_line = self.__parser.parse0(self.__options, short_option_with_value)
        self.assertEqual("path/to/my/db", command_line.getOptionValue4("t1"))
        self.assertFalse(command_line.hasOption2("last"))

    def testshouldParseShortOptionWithValue_test1_decomposed(self) -> None:
        short_option_with_value = ["-t1", "path/to/my/db"]
        command_line = self.__parser.parse0(self.__options, short_option_with_value)
        self.assertEqual("path/to/my/db", command_line.getOptionValue4("t1"))

    def testshouldParseShortOptionWithValue_test0_decomposed(self) -> None:
        short_option_with_value = ["-t1", "path/to/my/db"]
        command_line = self.__parser.parse0(self.__options, short_option_with_value)

    def testshouldParseShortOptionWithoutValue_test3_decomposed(self) -> None:
        two_short_options = ["-t1", "-last"]
        command_line = self.__parser.parse0(self.__options, two_short_options)

        self.assertTrue(command_line.hasOption2("t1"))
        self.assertNotEqual(
            "-last",
            command_line.getOptionValue4("t1"),
            "Second option has been used as value for first option",
        )
        self.assertTrue(
            command_line.hasOption2("last"), "Second option has not been detected"
        )

    def testshouldParseShortOptionWithoutValue_test2_decomposed(self) -> None:
        two_short_options = ["-t1", "-last"]
        command_line = self.__parser.parse0(self.__options, two_short_options)
        self.assertTrue(command_line.hasOption2("t1"))
        self.assertNotEqual(
            "-last",
            command_line.getOptionValue4("t1"),
            "Second option has been used as value for first option",
        )

    def testshouldParseShortOptionWithoutValue_test1_decomposed(self) -> None:
        two_short_options = ["-t1", "-last"]
        command_line = self.__parser.parse0(self.__options, two_short_options)
        self.assertTrue(command_line.hasOption2("t1"))

    def testshouldParseShortOptionWithoutValue_test0_decomposed(self) -> None:
        two_short_options = ["-t1", "-last"]
        command_line = self.__parser.parse0(self.__options, two_short_options)

    def testshouldParseConcatenatedShortOptions_test3_decomposed(self) -> None:
        concatenated_short_options = ["-t1", "-ab"]
        command_line = self.__parser.parse0(self.__options, concatenated_short_options)

        self.assertTrue(command_line.hasOption2("t1"))
        self.assertIsNone(command_line.getOptionValue4("t1"))
        self.assertTrue(command_line.hasOption2("a"))
        self.assertTrue(command_line.hasOption2("b"))
        self.assertFalse(command_line.hasOption2("last"))

    def testshouldParseConcatenatedShortOptions_test2_decomposed(self) -> None:
        concatenated_short_options = ["-t1", "-ab"]
        command_line = self.__parser.parse0(self.__options, concatenated_short_options)
        self.assertTrue(command_line.hasOption2("t1"))
        self.assertIsNone(command_line.getOptionValue4("t1"))

    def testshouldParseConcatenatedShortOptions_test1_decomposed(self) -> None:
        concatenated_short_options = ["-t1", "-ab"]
        command_line = self.__parser.parse0(self.__options, concatenated_short_options)
        self.assertTrue(command_line.hasOption2("t1"))

    def testshouldParseConcatenatedShortOptions_test0_decomposed(self) -> None:
        concatenated_short_options = ["-t1", "-ab"]
        command_line = self.__parser.parse0(self.__options, concatenated_short_options)

    def setUp(self) -> None:
        self.__parser = DefaultParser(2, False, None)

        option_t1 = (
            Builder.builder1("t1")
            .hasArg0()
            .numberOfArgs(1)
            .optionalArg(True)
            .argName("t1_path")
            .build()
        )

        option_a = Builder.builder1("a").hasArg1(False).build()
        option_b = Builder.builder1("b").hasArg1(False).build()
        option_last = Builder.builder1("last").hasArg1(False).build()

        self.__options = (
            Options()
            .addOption0(option_t1)
            .addOption0(option_a)
            .addOption0(option_b)
            .addOption0(option_last)
        )
