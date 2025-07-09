from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *


class BugCLI266Test(unittest.TestCase):

    __sortOrder: typing.List[str] = ["d", "f", "h", "o", "p", "s", "t", "w", "x"]
    __insertedOrder: typing.List[str] = ["h", "d", "f", "x", "s", "p", "t", "w", "o"]

    def testOptionComparatorInsertedOrder_test1_decomposed(self) -> None:
        options = self.__getOptions().getOptions()
        i = 0
        for o in options:
            self.assertEqual(o.getOpt(), self.__insertedOrder[i])
            i += 1

    def testOptionComparatorInsertedOrder_test0_decomposed(self) -> None:
        options: Collection[Option] = self.__getOptions().getOptions()

    def testOptionComparatorDefaultOrder_test3_decomposed(self) -> None:
        formatter = HelpFormatter()
        options = list(self.__getOptions().getOptions())
        options.sort(key=formatter.getOptionComparator())

        i = 0
        for option in options:
            self.assertEqual(option.getOpt(), self.__sortOrder[i])
            i += 1

    def testOptionComparatorDefaultOrder_test2_decomposed(self) -> None:
        formatter = HelpFormatter()
        options = list(self.__getOptions().getOptions())
        options.sort(key=formatter.getOptionComparator())

    def testOptionComparatorDefaultOrder_test1_decomposed(self) -> None:
        formatter = HelpFormatter()
        options = list(self.__getOptions().getOptions())

    def testOptionComparatorDefaultOrder_test0_decomposed(self) -> None:
        formatter = HelpFormatter()

    def __getOptions(self) -> Options:
        options = Options()

        help_option = (
            Builder.builder1("h")
            .longOpt("help")
            .desc("Prints this help message")
            .build()
        )
        options.addOption0(help_option)

        self.__buildOptionsGroup(options)

        t_option = Builder.builder1("t").required0().hasArg0().argName("file").build()
        w_option = Builder.builder1("w").required0().hasArg0().argName("word").build()
        o_option = Builder.builder1("o").hasArg0().argName("directory").build()

        options.addOption0(t_option)
        options.addOption0(w_option)
        options.addOption0(o_option)

        return options

    def __buildOptionsGroup(self, options: Options) -> None:
        first_group = OptionGroup()
        second_group = OptionGroup()
        first_group.setRequired(True)
        second_group.setRequired(True)

        first_group.addOption(
            Builder.builder1("d").longOpt("db").hasArg0().argName("table-name").build()
        )
        first_group.addOption(
            Builder.builder1("f")
            .longOpt("flat-file")
            .hasArg0()
            .argName("input.csv")
            .build()
        )
        options.addOptionGroup(first_group)

        second_group.addOption(Builder.builder1("x").hasArg0().argName("arg1").build())
        second_group.addOption(Builder.builder1("s").build())
        second_group.addOption(Builder.builder1("p").hasArg0().argName("arg1").build())
        options.addOptionGroup(second_group)
