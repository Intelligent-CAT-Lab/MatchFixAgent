from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class OptionsTest(unittest.TestCase):

    def testToString_test4_decomposed(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")
        s = options.toString()
        self.assertIsNotNone(s, "null string returned")
        self.assertTrue("foo" in s.lower(), "foo option missing")
        self.assertTrue("bar" in s.lower(), "bar option missing")

    def testToString_test3_decomposed(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")
        s = options.toString()
        self.assertIsNotNone(s, "null string returned")
        self.assertTrue("foo" in s.lower(), "foo option missing")

    def testToString_test2_decomposed(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")
        s = options.toString()

    def testToString_test1_decomposed(self) -> None:
        options = Options()
        options.addOption3("f", "foo", True, "Foo")
        options.addOption3("b", "bar", False, "Bar")

    def testToString_test0_decomposed(self) -> None:
        options = Options()

    def testSimple_test2_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("b", True, "toggle -b")
        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))

    def testSimple_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("b", True, "toggle -b")

    def testSimple_test0_decomposed(self) -> None:
        opts = Options()

    def testMissingOptionsException_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        option_f = OptionBuilder.isRequired0().create2("f")
        options.addOption0(option_f)
        OptionBuilder.isRequired0()
        option_x = OptionBuilder.isRequired0().create2("x")
        options.addOption0(option_x)

        try:
            PosixParser().parse0(options, [])
            pytest.fail("Expected MissingOptionException to be thrown")
        except MissingOptionException as e:
            self.assertEqual("Missing required options: f, x", e.getMessage())

    def testMissingOptionsException_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("x")
        options.addOption0(OptionBuilder.isRequired0().create2("x"))

    def testMissingOptionsException_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("x")

    def testMissingOptionsException_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")
        options.addOption0(OptionBuilder.isRequired0().create2("f"))
        OptionBuilder.isRequired0()

    def testMissingOptionsException_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")
        options.addOption0(OptionBuilder.isRequired0().create2("f"))

    def testMissingOptionsException_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")

    def testMissingOptionsException_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()

    def testMissingOptionsException_test0_decomposed(self) -> None:
        options = Options()

    def testMissingOptionException_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        option = OptionBuilder.isRequired0().create2("f")
        options.addOption0(option)

        with pytest.raises(MissingOptionException) as excinfo:
            PosixParser().parse0(options, [])

        assert str(excinfo.value) == "Missing required option: f"

    def testMissingOptionException_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        option = OptionBuilder.isRequired0().create2("f")
        options.addOption0(option)

    def testMissingOptionException_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().create2("f")

    def testMissingOptionException_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.isRequired0()

    def testMissingOptionException_test0_decomposed(self) -> None:
        options = Options()

    def testLong_test2_decomposed(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("b", "--b", True, "set -b")
        self.assertTrue(opts.hasOption("a"))
        self.assertTrue(opts.hasOption("b"))

    def testLong_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("b", "--b", True, "set -b")

    def testLong_test0_decomposed(self) -> None:
        opts = Options()

    def testHelpOptions_test14_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        longOnly1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        longOnly2 = OptionBuilder.withLongOpt("long-only2").create0()
        shortOnly1 = OptionBuilder.create2("1")
        shortOnly2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        bothA = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        bothB = OptionBuilder.withLongOpt("bothB").create2("b")

        options = Options()
        options.addOption0(longOnly1)
        options.addOption0(longOnly2)
        options.addOption0(shortOnly1)
        options.addOption0(shortOnly2)
        options.addOption0(bothA)
        options.addOption0(bothB)

        allOptions = []
        allOptions.append(longOnly1)
        allOptions.append(longOnly2)
        allOptions.append(shortOnly1)
        allOptions.append(shortOnly2)
        allOptions.append(bothA)
        allOptions.append(bothB)

        helpOptions = options.helpOptions()

        self.assertTrue(
            all(option in helpOptions for option in allOptions),
            "Everything in all should be in help",
        )
        self.assertTrue(
            all(option in allOptions for option in helpOptions),
            "Everything in help should be in all",
        )

    def testHelpOptions_test13_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")

        options = Options()
        options.addOption0(long_only1)
        options.addOption0(long_only2)
        options.addOption0(short_only1)
        options.addOption0(short_only2)
        options.addOption0(both_a)
        options.addOption0(both_b)

        all_options = []
        all_options.append(long_only1)
        all_options.append(long_only2)
        all_options.append(short_only1)
        all_options.append(short_only2)
        all_options.append(both_a)
        all_options.append(both_b)

        help_options = options.helpOptions()
        self.assertEqual(set(help_options), set(options.__shortOpts.values()))

    def testHelpOptions_test12_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")

        options = Options()
        options.addOption0(long_only1)
        options.addOption0(long_only2)
        options.addOption0(short_only1)
        options.addOption0(short_only2)
        options.addOption0(both_a)
        options.addOption0(both_b)

        all_options = []
        all_options.append(long_only1)
        all_options.append(long_only2)
        all_options.append(short_only1)
        all_options.append(short_only2)
        all_options.append(both_a)
        all_options.append(both_b)

    def testHelpOptions_test11_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")
        options = Options()
        options.addOption0(long_only1)
        options.addOption0(long_only2)
        options.addOption0(short_only1)
        options.addOption0(short_only2)
        options.addOption0(both_a)
        options.addOption0(both_b)
        all_options = []
        all_options.append(long_only1)

    def testHelpOptions_test10_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")
        options = Options()
        options.addOption0(long_only1)
        options.addOption0(long_only2)
        options.addOption0(short_only1)
        options.addOption0(short_only2)
        options.addOption0(both_a)
        options.addOption0(both_b)

    def testHelpOptions_test9_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")
        options = Options()

    def testHelpOptions_test8_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")
        both_b = OptionBuilder.withLongOpt("bothB").create2("b")

    def testHelpOptions_test7_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")
        OptionBuilder.withLongOpt("bothB")

    def testHelpOptions_test6_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")
        both_a = OptionBuilder.withLongOpt("bothA").create2("a")

    def testHelpOptions_test5_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")
        OptionBuilder.withLongOpt("bothA")

    def testHelpOptions_test4_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()
        short_only1 = OptionBuilder.create2("1")
        short_only2 = OptionBuilder.create2("2")

    def testHelpOptions_test3_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")
        long_only2 = OptionBuilder.withLongOpt("long-only2").create0()

    def testHelpOptions_test2_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()
        OptionBuilder.withLongOpt("long-only2")

    def testHelpOptions_test1_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")
        long_only1 = OptionBuilder.withLongOpt("long-only1").create0()

    def testHelpOptions_test0_decomposed(self) -> None:
        OptionBuilder.withLongOpt("long-only1")

    def testGetOptionsGroups_test12_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))
        group2.addOption(OptionBuilder.create1("y"))
        options.addOptionGroup(group1)
        options.addOptionGroup(group2)
        self.assertIsNotNone(
            options.getOptionGroups(), "Option groups should not be None"
        )
        self.assertEqual(2, len(options.getOptionGroups()), "Expected 2 option groups")

    def testGetOptionsGroups_test11_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))
        group2.addOption(OptionBuilder.create1("y"))
        options.addOptionGroup(group1)
        options.addOptionGroup(group2)

    def testGetOptionsGroups_test10_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))

        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))
        group2.addOption(OptionBuilder.create1("y"))

    def testGetOptionsGroups_test9_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))
        group2.addOption(OptionBuilder.create1("y"))

    def testGetOptionsGroups_test8_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()
        group2.addOption(OptionBuilder.create1("x"))

    def testGetOptionsGroups_test7_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        OptionBuilder.create1("a")
        group1.addOption(OptionBuilder.create1("a"))
        OptionBuilder.create1("b")
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()
        OptionBuilder.create1("x")

    def testGetOptionsGroups_test6_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))
        group2 = OptionGroup()

    def testGetOptionsGroups_test5_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        group1.addOption(OptionBuilder.create1("a"))
        group1.addOption(OptionBuilder.create1("b"))

    def testGetOptionsGroups_test4_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        OptionBuilder.create1("a")
        group1.addOption(OptionBuilder.create1("a"))
        OptionBuilder.create1("b")

    def testGetOptionsGroups_test3_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        option_a = OptionBuilder.create1("a")
        group1.addOption(option_a)

    def testGetOptionsGroups_test2_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()
        OptionBuilder.create1("a")

    def testGetOptionsGroups_test1_decomposed(self) -> None:
        options = Options()
        group1 = OptionGroup()

    def testGetOptionsGroups_test0_decomposed(self) -> None:
        options = Options()

    def testGetMatchingOpts_test7_decomposed(self) -> None:
        options = Options()

        # Adding the "version" option
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())

        # Adding the "verbose" option
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

        # Assertions
        self.assertTrue(len(options.getMatchingOptions("foo")) == 0)
        self.assertEqual(1, len(options.getMatchingOptions("version")))
        self.assertEqual(2, len(options.getMatchingOptions("ver")))

    def testGetMatchingOpts_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

    def testGetMatchingOpts_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()

    def testGetMatchingOpts_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()
        options.addOption0(OptionBuilder.withLongOpt("version").create0())
        OptionBuilder.withLongOpt("verbose")

    def testGetMatchingOpts_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")
        option = OptionBuilder.withLongOpt("version").create0()
        options.addOption0(option)

    def testGetMatchingOpts_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")
        OptionBuilder.withLongOpt("version").create0()

    def testGetMatchingOpts_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("version")

    def testGetMatchingOpts_test0_decomposed(self) -> None:
        options = Options()

    def testDuplicateSimple_test3_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")
        option = opts.getOption("a")
        self.assertEqual("toggle -a*", option.getDescription(), "last one in wins")

    def testDuplicateSimple_test2_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")
        opts.getOption("a")

    def testDuplicateSimple_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption1("a", False, "toggle -a")
        opts.addOption1("a", True, "toggle -a*")

    def testDuplicateSimple_test0_decomposed(self) -> None:
        opts = Options()

    def testDuplicateLong_test3_decomposed(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")
        option = opts.getOption("a")
        self.assertEqual("toggle -a*", option.getDescription(), "last one in wins")

    def testDuplicateLong_test2_decomposed(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")
        opts.getOption("a")

    def testDuplicateLong_test1_decomposed(self) -> None:
        opts = Options()
        opts.addOption3("a", "--a", False, "toggle -a")
        opts.addOption3("a", "--a", False, "toggle -a*")

    def testDuplicateLong_test0_decomposed(self) -> None:
        opts = Options()
