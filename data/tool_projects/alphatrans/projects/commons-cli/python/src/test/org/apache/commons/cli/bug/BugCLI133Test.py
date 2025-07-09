from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI133Test(unittest.TestCase):

    def testOrder_test5_decomposed(self) -> None:
        optionA = Option.Option1("a", "first")
        opts = Options()
        opts.addOption0(optionA)
        posixParser = PosixParser()
        line = posixParser.parse0(opts, None)
        self.assertFalse(line.hasOption2(None))

    def testOrder_test4_decomposed(self) -> None:
        option_a = Option.Option1("a", "first")
        opts = Options()
        opts.addOption0(option_a)
        posix_parser = PosixParser()
        line = posix_parser.parse0(opts, None)

    def testOrder_test3_decomposed(self) -> None:
        option_a = Option.Option1("a", "first")
        opts = Options()
        opts.addOption0(option_a)
        posix_parser = PosixParser()

    def testOrder_test2_decomposed(self) -> None:
        option_a = Option.Option1("a", "first")
        opts = Options()
        opts.addOption0(option_a)

    def testOrder_test1_decomposed(self) -> None:
        option_a = Option.Option1("a", "first")
        opts = Options()

    def testOrder_test0_decomposed(self) -> None:
        option_a = Option.Option1("a", "first")
