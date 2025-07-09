from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.DefaultParser import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.Options import *


class DisablePartialMatchingTest(unittest.TestCase):

    def testRegularPartialMatching_test6_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

        line = parser.parse0(options, ["-de", "--option=foobar"])

        self.assertTrue(
            line.hasOption2("debug"), "There should be an option debug in any case..."
        )
        self.assertFalse(
            line.hasOption2("extract"),
            "There should not be an extract option because partial matching only selects debug",
        )
        self.assertTrue(
            line.hasOption2("option"),
            "There should be an option option with a argument value",
        )

    def testRegularPartialMatching_test5_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )
        line = parser.parse0(options, ["-de", "--option=foobar"])

    def testRegularPartialMatching_test4_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

    def testRegularPartialMatching_test3_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))

    def testRegularPartialMatching_test2_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))

    def testRegularPartialMatching_test1_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)
        options = Options()

    def testRegularPartialMatching_test0_decomposed(self) -> None:
        parser = DefaultParser(2, False, None)

    def testDisablePartialMatching_test6_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

        line = parser.parse0(options, ["-de", "--option=foobar"])

        self.assertTrue(
            line.hasOption2("debug"), "There should be an option debug in any case..."
        )
        self.assertTrue(
            line.hasOption2("extract"),
            "There should be an extract option because partial matching is off",
        )
        self.assertTrue(
            line.hasOption2("option"),
            "There should be an option option with a argument value",
        )

    def testDisablePartialMatching_test5_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )
        line = parser.parse0(options, ["-de", "--option=foobar"])

    def testDisablePartialMatching_test4_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))
        options.addOption0(
            Option(0, "o", "option", "Turn on option with argument.", True, None)
        )

    def testDisablePartialMatching_test3_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))
        options.addOption0(Option(0, "e", "extract", "Turn on extract.", False, None))

    def testDisablePartialMatching_test2_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()
        options.addOption0(Option(0, "d", "debug", "Turn on debug.", False, None))

    def testDisablePartialMatching_test1_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
        options = Options()

    def testDisablePartialMatching_test0_decomposed(self) -> None:
        parser = DefaultParser(0, False, None)
