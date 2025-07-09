from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.cli.Option import *


class OptionTest(unittest.TestCase):

    def testSubclass_test3_decomposed(self) -> None:
        option = DefaultOption("f", "file", "myfile.txt")
        clone = option.clone()
        self.assertEqual("myfile.txt", clone.getValue0())
        self.assertEqual(DefaultOption, clone.__class__)

    def testSubclass_test2_decomposed(self) -> None:
        option = DefaultOption("f", "file", "myfile.txt")
        clone = option.clone()
        self.assertEqual("myfile.txt", clone.getValue0())

    def testSubclass_test1_decomposed(self) -> None:
        option = DefaultOption("f", "file", "myfile.txt")
        clone = option.clone()

    def testSubclass_test0_decomposed(self) -> None:
        option = DefaultOption("f", "file", "myfile.txt")

    def testHashCode_test15_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder1("test").build().hashCode()
        Option.builder1("test").longOpt("long test")
        Option.builder1("test").longOpt("long test").build()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test").longOpt("long test").build().hashCode(),
        )

    def testHashCode_test14_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder1("test").build().hashCode()
        Option.builder1("test").longOpt("long test")
        Option.builder1("test").longOpt("long test").build()

    def testHashCode_test13_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder1("test").build().hashCode()
        Option.builder1("test").longOpt("long test")

    def testHashCode_test12_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder1("test").build().hashCode()

    def testHashCode_test11_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")
        Option.builder1("test").build()

    def testHashCode_test10_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        Option.builder1("test")

    def testHashCode_test9_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )

    def testHashCode_test8_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()
        Option.builder1("test").build().hashCode()

    def testHashCode_test7_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")
        Option.builder0().longOpt("test").build()

    def testHashCode_test6_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()
        Option.builder0().longOpt("test")

    def testHashCode_test5_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")
        Option.builder1("test").build()

    def testHashCode_test4_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        Option.builder0()
        Option.builder1("test")

    def testHashCode_test3_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
            "Hash codes for different options should not be equal",
        )
        Option.builder0()

    def testHashCode_test2_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()
        Option.builder1("test").build().hashCode()
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )

    def testHashCode_test1_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")
        Option.builder1("test").build()
        Option.builder1("test2").build()

    def testHashCode_test0_decomposed(self) -> None:
        Option.builder1("test")
        Option.builder1("test2")

    def testHasArgs_test10_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNINITIALIZED)
        self.assertFalse(option.hasArgs())

    def testHasArgs_test9_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNINITIALIZED)

    def testHasArgs_test8_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertTrue(option.hasArgs())

    def testHasArgs_test7_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)
        self.assertTrue(option.hasArgs())
        option.setArgs(Option.UNLIMITED_VALUES)

    def testHasArgs_test6_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)
        self.assertTrue(option.hasArgs())

    def testHasArgs_test5_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())
        option.setArgs(10)

    def testHasArgs_test4_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)
        self.assertFalse(option.hasArgs())

    def testHasArgs_test3_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())
        option.setArgs(1)

    def testHasArgs_test2_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgs(0)
        self.assertFalse(option.hasArgs())

    def testHasArgs_test1_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(0)

    def testHasArgs_test0_decomposed(self) -> None:
        option = Option.Option1("f", None)

    def testHasArgName_test6_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgName(None)
        self.assertFalse(option.hasArgName())
        option.setArgName("")
        self.assertFalse(option.hasArgName())
        option.setArgName("file")
        self.assertTrue(option.hasArgName())

    def testHasArgName_test5_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgName(None)
        self.assertFalse(option.hasArgName())
        option.setArgName("")
        self.assertFalse(option.hasArgName())
        option.setArgName("file")

    def testHasArgName_test4_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgName(None)
        self.assertFalse(option.hasArgName())
        option.setArgName("")
        self.assertFalse(option.hasArgName())

    def testHasArgName_test3_decomposed(self) -> None:
        option = Option("f", None)  # Create an Option instance with "f" and None
        option.setArgName(None)  # Set the argument name to None
        self.assertFalse(option.hasArgName())  # Assert that hasArgName() returns False
        option.setArgName("")  # Set the argument name to an empty string

    def testHasArgName_test2_decomposed(self) -> None:
        option = Option("f", None)
        option.setArgName(None)
        self.assertFalse(option.hasArgName())

    def testHasArgName_test1_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgName(None)

    def testHasArgName_test0_decomposed(self) -> None:
        option = Option.Option1("f", None)

    def testGetValue_test7_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))
        option.addValueForProcessing("foo")
        self.assertEqual("foo", option.getValue0())
        self.assertEqual("foo", option.getValue1(0))
        self.assertEqual("foo", option.getValue2("default"))

    def testGetValue_test6_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))
        option.addValueForProcessing("foo")
        self.assertEqual("foo", option.getValue0())
        self.assertEqual("foo", option.getValue1(0))

    def testGetValue_test5_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))
        option.addValueForProcessing("foo")
        self.assertEqual("foo", option.getValue0())

    def testGetValue_test4_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))
        option.addValueForProcessing("foo")

    def testGetValue_test3_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))

    def testGetValue_test2_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertEqual("default", option.getValue2("default"))

    def testGetValue_test1_decomposed(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)

    def testGetValue_test0_decomposed(self) -> None:
        option = Option.Option1("f", None)

    def testClone_test9_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        self.assertEqual(1, a.getArgs())
        self.assertEqual(0, len(a.getValuesList()))
        self.assertEqual(2, len(b.getValues()))

    def testClone_test8_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        self.assertEqual(1, a.getArgs())
        self.assertEqual(0, len(a.getValuesList()))

    def testClone_test7_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        self.assertEqual(1, a.getArgs())

    def testClone_test6_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")

    def testClone_test5_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)

    def testClone_test4_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())

    def testClone_test3_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")

    def testClone_test2_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)

    def testClone_test1_decomposed(self) -> None:
        a = TestOption("a", True, "")
        b = a.clone()

    def testClone_test0_decomposed(self) -> None:
        a = TestOption("a", True, "")

    def testClear_test5_decomposed(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))
        option.addValue("a")
        self.assertEqual(1, len(option.getValuesList()))
        option.clearValues()
        self.assertEqual(0, len(option.getValuesList()))

    def testClear_test4_decomposed(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))
        option.addValue("a")
        self.assertEqual(1, len(option.getValuesList()))
        option.clearValues()
        self.assertEqual(0, len(option.getValuesList()))

    def testClear_test3_decomposed(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))
        option.addValue("a")
        self.assertEqual(1, len(option.getValuesList()))

    def testClear_test2_decomposed(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))
        option.addValue("a")

    def testClear_test1_decomposed(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))

    def testClear_test0_decomposed(self) -> None:
        option = TestOption("x", True, "")

    def testBuilderMethods_test73_decomposed(self) -> None:
        default_separator = "\u0000"

        # Test case 1
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 2
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 3
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 4
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 5
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 6
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        # Test case 7
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 8
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        # Test case 9
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 10
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        # Test case 11
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        # Test case 12
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        # Test case 13
        Option.builder0()
        Option.builder0().option("a")
        Option.builder0().option("a").desc("desc")
        Option.builder0().option("a").desc("desc").type_(int)
        Option.builder0().option("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder0().option("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

    def testBuilderMethods_test72_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        Option.builder0()
        Option.builder0().option("a")
        Option.builder0().option("a").desc("desc")
        Option.builder0().option("a").desc("desc").type_(int)
        Option.builder0().option("a").desc("desc").type_(int).build()

    def testBuilderMethods_test71_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        Option.builder0()
        Option.builder0().option("a")
        Option.builder0().option("a").desc("desc")
        Option.builder0().option("a").desc("desc").type_(int)

    def testBuilderMethods_test70_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        Option.builder0()
        Option.builder0().option("a")
        Option.builder0().option("a").desc("desc")

    def testBuilderMethods_test69_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        Option.builder0()
        Option.builder0().option("a")

    def testBuilderMethods_test68_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

        Option.builder0()

    def testBuilderMethods_test67_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").type_(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            int,
        )

    def testBuilderMethods_test66_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)
        Option.builder1("a").desc("desc").type_(int).build()

    def testBuilderMethods_test65_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").type_(int)

    def testBuilderMethods_test64_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test63_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test62_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )

    def testBuilderMethods_test61_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")
        Option.builder1("a").desc("desc").valueSeparator1(":").build()

    def testBuilderMethods_test60_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").valueSeparator1(":")

    def testBuilderMethods_test59_decomposed(self) -> None:
        default_separator = "\u0000"

        # Test case 1
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 2
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 3
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 4
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 5
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 6
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 7
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        # Test case 8
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 9
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        # Test case 10
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test case 11
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

    def testBuilderMethods_test58_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test57_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            default_separator,
            str,
        )

    def testBuilderMethods_test56_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)
        Option.builder1("a").desc("desc").optionalArg(True).build()

    def testBuilderMethods_test55_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(True)

    def testBuilderMethods_test54_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test53_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test52_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test51_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)
        Option.builder1("a").desc("desc").optionalArg(False).build()

    def testBuilderMethods_test50_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").optionalArg(False)

    def testBuilderMethods_test49_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test48_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test47_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test46_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")
        Option.builder1("a").desc("desc").argName("arg1").build()

    def testBuilderMethods_test45_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").argName("arg1")

    def testBuilderMethods_test44_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test43_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test42_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test41_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)
        Option.builder1("a").desc("desc").required1(False).build()

    def testBuilderMethods_test40_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(False)

    def testBuilderMethods_test39_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test38_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test37_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test36_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)
        Option.builder1("a").desc("desc").required1(True).build()

    def testBuilderMethods_test35_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").required1(True)

    def testBuilderMethods_test34_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test33_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test32_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test31_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)
        Option.builder1("a").desc("desc").numberOfArgs(3).build()

    def testBuilderMethods_test30_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").numberOfArgs(3)

    def testBuilderMethods_test29_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test28_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test27_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test26_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()

    def testBuilderMethods_test25_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)

    def testBuilderMethods_test24_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test23_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test22_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test21_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)
        Option.builder1("a").desc("desc").hasArg1(False).build()

    def testBuilderMethods_test20_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(False)

    def testBuilderMethods_test19_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test18_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")

    def testBuilderMethods_test17_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test16_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)
        Option.builder1("a").desc("desc").hasArg1(True).build()

    def testBuilderMethods_test15_decomposed(self) -> None:
        default_separator = "\u0000"

        # Test 1
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test 2
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test 3
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Test 4
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").hasArg1(True)

    def testBuilderMethods_test14_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test13_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test12_decomposed(self) -> None:
        default_separator = "\u0000"

        # First set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Second set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Third set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test11_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")
        Option.builder1("a").desc("desc").longOpt("aaa").build()

    def testBuilderMethods_test10_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").longOpt("aaa")

    def testBuilderMethods_test9_decomposed(self) -> None:
        default_separator = "\u0000"

        # First set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Second set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Third set of operations
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test8_decomposed(self) -> None:
        default_separator = "\u0000"

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        Option.builder1("a")

    def testBuilderMethods_test7_decomposed(self) -> None:
        default_separator = "\u0000"

        # Test Option.builder1("a")
        Option.builder1("a")

        # Test Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc")

        # Test Option.builder1("a").desc("desc").build()
        Option.builder1("a").desc("desc").build()

        # Test checkOption with built Option
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Repeat the same sequence of tests
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test6_decomposed(self) -> None:
        default_separator: str = "\u0000"

        # Create Option instances using the builder
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

        # Check the created Option instance
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

        # Repeat the same steps as in the Java code
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

    def testBuilderMethods_test5_decomposed(self) -> None:
        default_separator = "\u0000"
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test4_decomposed(self) -> None:
        default_separator = "\u0000"
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )
        Option.builder1("a")

    def testBuilderMethods_test3_decomposed(self) -> None:
        default_separator = "\u0000"  # Equivalent to (char) 0 in Java
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            default_separator,
            str,
        )

    def testBuilderMethods_test2_decomposed(self) -> None:
        default_separator: str = "\u0000"
        Option.builder1("a")
        Option.builder1("a").desc("desc")
        Option.builder1("a").desc("desc").build()

    def testBuilderMethods_test1_decomposed(self) -> None:
        default_separator: str = "\u0000"
        Option.builder1("a")
        Option.builder1("a").desc("desc")

    def testBuilderMethods_test0_decomposed(self) -> None:
        default_separator: str = "\u0000"
        Option.builder1("a")

    def testBuilderInvalidOptionName4_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid@")

    def testBuilderInvalidOptionName3_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid?")

    def testBuilderInvalidOptionName2_test1_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0()
            Option.builder0().option("invalid@")

    def testBuilderInvalidOptionName2_test0_decomposed(self) -> None:
        Option.builder0()

    def testBuilderInvalidOptionName1_test1_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0()
            Option.builder0().option("invalid?")

    def testBuilderInvalidOptionName1_test0_decomposed(self) -> None:
        Option.builder0()

    def testBuilderInsufficientParams2_test2_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1(None)

        with self.assertRaises(ValueError):
            Option.builder1(None).desc("desc")

        with self.assertRaises(ValueError):
            Option.builder1(None).desc("desc").build()

    def testBuilderInsufficientParams2_test1_decomposed(self) -> None:
        Option.builder1(None)
        Option.builder1(None).desc("desc")

    def testBuilderInsufficientParams2_test0_decomposed(self) -> None:
        Option.builder1(None)

    def testBuilderInsufficientParams1_test2_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().build()
        with self.assertRaises(ValueError):
            Option.builder0().desc("desc").build()

    def testBuilderInsufficientParams1_test1_decomposed(self) -> None:
        Option.builder0()
        Option.builder0().desc("desc")

    def testBuilderInsufficientParams1_test0_decomposed(self) -> None:
        Option.builder0()

    @staticmethod
    def __checkOption(
        option: Option,
        opt: str,
        description: str,
        longOpt: str,
        numArgs: int,
        argName: str,
        required: bool,
        optionalArg: bool,
        valueSeparator: str,
        cls: typing.Type[typing.Any],
    ) -> None:
        assert option.getOpt() == opt
        assert option.getDescription() == description
        assert option.getLongOpt() == longOpt
        assert option.getArgs() == numArgs
        assert option.getArgName() == argName
        assert option.isRequired() == required
        assert option.hasOptionalArg() == optionalArg
        assert option.getValueSeparator() == valueSeparator
        assert option.getType() == cls


class TestOption(Option):

    __serialVersionUID: int = 1

    def addValue(self, value: str) -> bool:
        self.addValueForProcessing(value)
        return True

    def __init__(self, opt: str, hasArg: bool, description: str) -> None:
        super().__init__(-1, opt, None, description, hasArg, None)


class DefaultOption(Option):

    __defaultValue: str = ""

    __serialVersionUID: int = 1

    def getValue0(self) -> str:
        return (
            super().getValue0()
            if super().getValue0() is not None
            else self.__defaultValue
        )

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:
        super().__init__(-1, None, None, None, False, None)
        self.__defaultValue = defaultValue
