from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI148Test(unittest.TestCase):

    __options: Options = None

    def testWorkaround2_test2_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-t", '"-something"']
        command_line = parser.parse0(self.options, args)
        self.assertEqual("-something", command_line.getOptionValue0("t"))

    def testWorkaround2_test1_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-t", '"-something"']
        command_line = parser.parse0(self.options, args)

    def testWorkaround2_test0_decomposed(self) -> None:
        parser = PosixParser()

    def testWorkaround1_test2_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-t-something"]
        command_line = parser.parse0(self.options, args)
        self.assertEqual("-something", command_line.getOptionValue0("t"))

    def testWorkaround1_test1_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-t-something"]
        command_line = parser.parse0(self.options, args)

    def testWorkaround1_test0_decomposed(self) -> None:
        parser = PosixParser()

    def setUp(self) -> None:
        self.options = Options()
        self.options.addOption0(OptionBuilder.hasArg0().create1("t"))
        self.options.addOption0(OptionBuilder.hasArg0().create1("s"))
