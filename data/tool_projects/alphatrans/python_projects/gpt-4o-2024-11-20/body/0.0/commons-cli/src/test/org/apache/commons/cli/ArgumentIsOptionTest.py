from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.PosixParser import *


class ArgumentIsOptionTest(unittest.TestCase):

    __parser: CommandLineParser = None

    __options: Options = None

    def testOptionWithArgument_test3_decomposed(self) -> None:
        args = ["-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
        self.assertEqual(cl.getOptionValue4("attr"), "p", "Confirm arg of -attr")
        self.assertEqual(len(cl.getArgs()), 0, "Confirm all arguments recognized")

    def testOptionWithArgument_test2_decomposed(self) -> None:
        args = ["-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
        self.assertEqual(cl.getOptionValue4("attr"), "p", "Confirm arg of -attr")

    def testOptionWithArgument_test1_decomposed(self) -> None:
        args = ["-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")

    def testOptionWithArgument_test0_decomposed(self) -> None:
        args = ["-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)

    def testOptionAndOptionWithArgument_test3_decomposed(self) -> None:
        args = ["-p", "-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
        self.assertEqual(cl.getOptionValue4("attr"), "p", "Confirm arg of -attr")
        self.assertEqual(len(cl.getArgs()), 0, "Confirm all arguments recognized")

    def testOptionAndOptionWithArgument_test2_decomposed(self) -> None:
        args = ["-p", "-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")
        self.assertEqual(cl.getOptionValue4("attr"), "p", "Confirm arg of -attr")

    def testOptionAndOptionWithArgument_test1_decomposed(self) -> None:
        args = ["-p", "-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
        self.assertTrue(cl.hasOption2("attr"), "Confirm -attr is set")

    def testOptionAndOptionWithArgument_test0_decomposed(self) -> None:
        args = ["-p", "-attr", "p"]
        cl = self.__parser.parse0(self.__options, args)

    def testOption_test2_decomposed(self) -> None:
        args = ["-p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
        self.assertFalse(cl.hasOption2("attr"), "Confirm -attr is not set")
        self.assertEqual(len(cl.getArgs()), 0, "Confirm all arguments recognized")

    def testOption_test1_decomposed(self) -> None:
        args = ["-p"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("p"), "Confirm -p is set")
        self.assertFalse(cl.hasOption2("attr"), "Confirm -attr is not set")

    def testOption_test0_decomposed(self) -> None:
        args = ["-p"]
        cl = self.__parser.parse0(self.__options, args)

    def setUp(self) -> None:
        self.__options = (
            Options()
            .addOption1("p", False, "Option p")
            .addOption1("attr", True, "Option accepts argument")
        )
        self.__parser = PosixParser()
