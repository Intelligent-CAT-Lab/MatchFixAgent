from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.AlreadySelectedException import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class OptionGroupTest(unittest.TestCase):

    __parser: Parser = PosixParser()
    __options: Options = None

    def testValidLongOnlyOptions_test3_decomposed(self) -> None:
        cl1 = self.__parser.parse0(self.__options, ["--export"])
        self.assertTrue(cl1.hasOption2("export"), "Confirm --export is set")

        cl2 = self.__parser.parse0(self.__options, ["--import"])
        self.assertTrue(cl2.hasOption2("import"), "Confirm --import is set")

    def testValidLongOnlyOptions_test2_decomposed(self) -> None:
        cl1 = self.__parser.parse0(self.__options, ["--export"])
        self.assertTrue(cl1.hasOption2("export"), "Confirm --export is set")
        cl2 = self.__parser.parse0(self.__options, ["--import"])

    def testValidLongOnlyOptions_test1_decomposed(self) -> None:
        cl1 = self.__parser.parse0(self.__options, ["--export"])
        self.assertTrue(cl1.hasOption2("export"), "Confirm --export is set")

    def testValidLongOnlyOptions_test0_decomposed(self) -> None:
        cl1 = self.__parser.parse0(self.__options, ["--export"])

    def testTwoValidOptions_test2_decomposed(self) -> None:
        args = ["-r", "-f"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(cl.getArgList() == [], "Confirm no extra args")

    def testTwoValidOptions_test1_decomposed(self) -> None:
        args = ["-r", "-f"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testTwoValidOptions_test0_decomposed(self) -> None:
        args = ["-r", "-f"]
        cl = self.__parser.parse0(self.__options, args)

    def testTwoValidLongOptions_test2_decomposed(self) -> None:
        args = ["--revision", "--file"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(len(cl.getArgList()) == 0, "Confirm no extra args")

    def testTwoValidLongOptions_test1_decomposed(self) -> None:
        args = ["--revision", "--file"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testTwoValidLongOptions_test0_decomposed(self) -> None:
        args = ["--revision", "--file"]
        cl = self.__parser.parse0(self.__options, args)

    def testTwoOptionsFromGroupWithProperties_test1_decomposed(self) -> None:
        args = ["-f"]
        properties = {"d": "true"}
        cl = self.__parser.parse2(self.__options, args, properties)
        self.assertTrue(cl.hasOption2("f"))
        self.assertFalse(cl.hasOption2("d"))

    def testTwoOptionsFromGroupWithProperties_test0_decomposed(self) -> None:
        args = ["-f"]
        properties = {"d": "true"}
        cl = self.__parser.parse2(self.__options, args, properties)

    def testTwoOptionsFromGroup_test0_decomposed(self) -> None:
        args = ["-f", "-d"]
        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone(e.getOptionGroup(), "null option group")
            self.assertEqual("f", e.getOptionGroup().getSelected(), "selected option")
            self.assertEqual("d", e.getOption().getOpt(), "option")

    def testTwoOptionsFromDifferentGroup_test2_decomposed(self) -> None:
        args = ["-f", "-s"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertTrue(cl.hasOption2("s"), "Confirm -s is set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(cl.getArgList().isEmpty(), "Confirm NO extra args")

    def testTwoOptionsFromDifferentGroup_test1_decomposed(self) -> None:
        args = ["-f", "-s"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertTrue(cl.hasOption2("s"), "Confirm -s is set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testTwoOptionsFromDifferentGroup_test0_decomposed(self) -> None:
        args = ["-f", "-s"]
        cl = self.__parser.parse0(self.__options, args)

    def testTwoLongOptionsFromGroup_test0_decomposed(self) -> None:
        args = ["--file", "--directory"]
        try:
            self.__parser.parse0(self.__options, args)
            pytest.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone(e.getOptionGroup(), "null option group")
            self.assertEqual("f", e.getOptionGroup().getSelected(), "selected option")
            self.assertEqual("d", e.getOption().getOpt(), "option")

    def testToString_test7_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

        if group2.toString() != "[-b Bar, -f Foo]":
            self.assertEqual("[-f Foo, -b Bar]", group2.toString())

    def testToString_test6_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

    def testToString_test5_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))

    def testToString_test4_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()

    def testToString_test3_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

    def testToString_test2_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

    def testToString_test1_decomposed(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))

    def testToString_test0_decomposed(self) -> None:
        group1 = OptionGroup()

    def testSingleOptionFromGroup_test2_decomposed(self) -> None:
        args = ["-f"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(len(cl.getArgList()) == 0, "Confirm no extra args")

    def testSingleOptionFromGroup_test1_decomposed(self) -> None:
        args = ["-f"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testSingleOptionFromGroup_test0_decomposed(self) -> None:
        args = ["-f"]
        cl = self.__parser.parse0(self.__options, args)

    def testSingleOption_test2_decomposed(self) -> None:
        args = ["-r"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(cl.getArgList() == [], "Confirm no extra args")

    def testSingleOption_test1_decomposed(self) -> None:
        args = ["-r"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
        self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testSingleOption_test0_decomposed(self) -> None:
        args = ["-r"]
        cl = self.__parser.parse0(self.__options, args)

    def testSingleLongOption_test2_decomposed(self) -> None:
        args = ["--file"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(len(cl.getArgList()) == 0, "Confirm no extra args")

    def testSingleLongOption_test1_decomposed(self) -> None:
        args = ["--file"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testSingleLongOption_test0_decomposed(self) -> None:
        args = ["--file"]
        cl = self.__parser.parse0(self.__options, args)

    def testNoOptionsExtraArgs_test2_decomposed(self) -> None:
        args = ["arg1", "arg2"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertEqual(len(cl.getArgList()), 2, "Confirm TWO extra args")

    def testNoOptionsExtraArgs_test1_decomposed(self) -> None:
        args = ["arg1", "arg2"]
        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")

    def testNoOptionsExtraArgs_test0_decomposed(self) -> None:
        args = ["arg1", "arg2"]
        cl = self.__parser.parse0(self.__options, args)

    def testGetNames_test5_decomposed(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create1("a"))
        group.addOption(OptionBuilder.create1("b"))

        self.assertIsNotNone(group.getNames(), "null names")
        self.assertEqual(2, len(group.getNames()))
        self.assertTrue("a" in group.getNames())
        self.assertTrue("b" in group.getNames())

    def testGetNames_test4_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create1("a")
        group.addOption(OptionBuilder.create1("a"))
        OptionBuilder.create1("b")
        group.addOption(OptionBuilder.create1("b"))

    def testGetNames_test3_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create1("a")
        group.addOption(OptionBuilder.create1("a"))
        OptionBuilder.create1("b")

    def testGetNames_test2_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create1("a")
        group.addOption(OptionBuilder.create1("a"))

    def testGetNames_test1_decomposed(self) -> None:
        group = OptionGroup()
        OptionBuilder.create1("a")

    def testGetNames_test0_decomposed(self) -> None:
        group = OptionGroup()

    def setUp(self) -> None:
        file = Option(0, "f", "file", "file to process", False, None)
        dir = Option(0, "d", "directory", "directory to process", False, None)
        group = OptionGroup()
        group.addOption(file)
        group.addOption(dir)
        self.__options = Options().addOptionGroup(group)

        section = Option(0, "s", "section", "section to process", False, None)
        chapter = Option(0, "c", "chapter", "chapter to process", False, None)
        group2 = OptionGroup()
        group2.addOption(section)
        group2.addOption(chapter)

        self.__options.addOptionGroup(group2)

        import_opt = Option(0, None, "import", "section to process", False, None)
        export_opt = Option(0, None, "export", "chapter to process", False, None)
        group3 = OptionGroup()
        group3.addOption(import_opt)
        group3.addOption(export_opt)
        self.__options.addOptionGroup(group3)

        self.__options.addOption3("r", "revision", False, "revision number")
