from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugCLI13Test(unittest.TestCase):

    def testCLI13_test11_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()
        options.addOption0(debug)

        command_line = PosixParser().parse0(options, ["-d", "true"])

        self.assertEqual("true", command_line.getOptionValue4(debug_opt))
        self.assertEqual("true", command_line.getOptionValue0("d"))
        self.assertTrue(command_line.hasOption0("d"))
        self.assertTrue(command_line.hasOption2(debug_opt))

    def testCLI13_test10_decomposed(self) -> None:
        debug_opt = "debug"

        # Create the debug option using OptionBuilder
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        # Create options and add the debug option
        options = Options()
        options.addOption0(debug)

        # Parse the command line arguments
        command_line = PosixParser().parse0(options, ["-d", "true"])

        # Assertions
        self.assertEqual("true", command_line.getOptionValue4(debug_opt))
        self.assertEqual("true", command_line.getOptionValue0("d"))
        self.assertTrue(command_line.hasOption0("d"))

    def testCLI13_test9_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()
        options.addOption0(debug)

        command_line = PosixParser().parse0(options, ["-d", "true"])

        self.assertEqual("true", command_line.getOptionValue4(debug_opt))
        self.assertEqual("true", command_line.getOptionValue0("d"))

    def testCLI13_test8_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()
        options.addOption0(debug)

        command_line = PosixParser().parse0(options, ["-d", "true"])

        self.assertEqual("true", command_line.getOptionValue4(debug_opt))

    def testCLI13_test7_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()
        options.addOption0(debug)

        command_line = PosixParser().parse0(options, ["-d", "true"])

    def testCLI13_test6_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()
        options.addOption0(debug)

    def testCLI13_test5_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt).hasArg0()

        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

        options = Options()

    def testCLI13_test4_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withDescription("turn on debugging")
        OptionBuilder.withLongOpt(debug_opt)
        OptionBuilder.hasArg0()
        debug = (
            OptionBuilder.withArgName(debug_opt)
            .withDescription("turn on debugging")
            .withLongOpt(debug_opt)
            .hasArg0()
            .create1("d")
        )

    def testCLI13_test3_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withDescription("turn on debugging")
        OptionBuilder.withLongOpt(debug_opt)
        OptionBuilder.hasArg0()

    def testCLI13_test2_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")
        OptionBuilder.withArgName(debug_opt).withDescription(
            "turn on debugging"
        ).withLongOpt(debug_opt)

    def testCLI13_test1_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
        OptionBuilder.withArgName(debug_opt).withDescription("turn on debugging")

    def testCLI13_test0_decomposed(self) -> None:
        debug_opt = "debug"
        OptionBuilder.withArgName(debug_opt)
