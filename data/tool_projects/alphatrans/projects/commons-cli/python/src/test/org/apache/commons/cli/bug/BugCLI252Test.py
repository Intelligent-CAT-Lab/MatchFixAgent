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
from src.main.org.apache.commons.cli.ParseException import *


class BugCLI252Test(unittest.TestCase):

    def testExactOptionNameMatch_test1_decomposed(self) -> None:
        options = self.__getOptions()
        parser = DefaultParser(2, False, None)
        parser.parse0(options, ["--prefix"])

    def testExactOptionNameMatch_test0_decomposed(self) -> None:
        self.__getOptions()

    def testAmbiquousOptionName_test1_decomposed(self) -> None:
        with pytest.raises(AmbiguousOptionException):
            options = self.__getOptions()
            parser = DefaultParser(2, False, None)
            parser.parse0(options, ["--pref"])

    def testAmbiquousOptionName_test0_decomposed(self) -> None:
        self.__getOptions()

    def __getOptions(self) -> Options:
        options = Options()
        options.addOption0(Builder.builder0().longOpt("prefix").build())
        options.addOption0(Builder.builder0().longOpt("prefixplusplus").build())
        return options
