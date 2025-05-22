from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI71Test(unittest.TestCase):

    __parser: CommandLineParser = None

    __options: Options = None

    def testMistakenArgument_test2_decomposed(self) -> None:
        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)
        args = ["-a", "Caesar", "-k", "a"]
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue4("k"))

    def testMistakenArgument_test1_decomposed(self) -> None:
        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)
        args = ["-a", "Caesar", "-k", "a"]
        line = self.__parser.parse0(self.__options, args)

    def testMistakenArgument_test0_decomposed(self) -> None:
        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)

    def testLackOfError_test0_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        with pytest.raises(MissingArgumentException) as excinfo:
            self.__parser.parse0(self.__options, args)
        self.assertEqual("k", excinfo.value.getOption().getOpt())

    def testGetsDefaultIfOptional_test4_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k")
        self.__options.getOption("k").setOptionalArg(True)
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("a", line.getOptionValue1("k", "a"))

    def testGetsDefaultIfOptional_test3_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k").setOptionalArg(True)
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))

    def testGetsDefaultIfOptional_test2_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k").setOptionalArg(True)
        line = self.__parser.parse0(self.__options, args)

    def testGetsDefaultIfOptional_test1_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k")
        self.__options.getOption("k").setOptionalArg(True)

    def testGetsDefaultIfOptional_test0_decomposed(self) -> None:
        args = ["-k", "-a", "Caesar"]
        self.__options.getOption("k")

    def testBasic_test1_decomposed(self) -> None:
        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)
        self.assertEqual("Caesar", line.getOptionValue4("a"))
        self.assertEqual("A", line.getOptionValue4("k"))

    def testBasic_test0_decomposed(self) -> None:
        args = ["-a", "Caesar", "-k", "A"]
        line = self.__parser.parse0(self.__options, args)

    def setUp(self) -> None:
        self.__options = Options()

        algorithm = Option(
            0, "a", "algo", "the algorithm which it to perform executing", True, None
        )
        algorithm.setArgName("algorithm name")
        self.__options.addOption0(algorithm)

        key = Option(
            0, "k", "key", "the key the setted algorithm uses to process", True, None
        )
        key.setArgName("value")
        self.__options.addOption0(key)

        self.__parser = PosixParser()
