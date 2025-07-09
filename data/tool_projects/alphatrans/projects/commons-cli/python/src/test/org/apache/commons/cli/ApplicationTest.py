from __future__ import annotations
import time
import locale
import re
import logging
import sys
import numbers
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.GnuParser import *
from src.main.org.apache.commons.cli.HelpFormatter import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class ApplicationTest(unittest.TestCase):

    def testNLT_test34_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

        parser = PosixParser()
        args = ["-v", "-l", "10", "-age", "5", "-file", "filename"]
        line = parser.parse0(options, args)

        self.assertTrue(line.hasOption2("v"))
        self.assertEqual(line.getOptionValue4("l"), "10")
        self.assertEqual(line.getOptionValue4("limit"), "10")
        self.assertEqual(line.getOptionValue4("a"), "5")
        self.assertEqual(line.getOptionValue4("age"), "5")
        self.assertEqual(line.getOptionValue4("file"), "filename")

    def testNLT_test33_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

        parser = PosixParser()
        args = ["-v", "-l", "10", "-age", "5", "-file", "filename"]
        line = parser.parse0(options, args)

        self.assertTrue(line.hasOption2("v"))

    def testNLT_test32_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

        parser = PosixParser()
        args = ["-v", "-l", "10", "-age", "5", "-file", "filename"]
        line = parser.parse0(options, args)

    def testNLT_test31_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

        parser = PosixParser()

    def testNLT_test30_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()
        options.addOption0(help_option)
        options.addOption0(version_option)
        options.addOption0(new_run_option)
        options.addOption0(tracker_run_option)
        options.addOption0(time_limit_option)
        options.addOption0(age_option)
        options.addOption0(server_option)
        options.addOption0(num_results_option)
        options.addOption0(config_file_option)

    def testNLT_test29_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

        options = Options()

    def testNLT_test28_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        OptionBuilder.withLongOpt("file")
        OptionBuilder.withLongOpt("file").hasArg0()
        OptionBuilder.withLongOpt("file").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "file"
        ).hasArg0().withValueSeparator0().withDescription(
            "Use the specified configuration file"
        )
        config_file_option = (
            OptionBuilder.withLongOpt("file")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Use the specified configuration file")
            .create0()
        )

    def testNLT_test27_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        OptionBuilder.withLongOpt("file")
        OptionBuilder.withLongOpt("file").hasArg0()
        OptionBuilder.withLongOpt("file").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "file"
        ).hasArg0().withValueSeparator0().withDescription(
            "Use the specified configuration file"
        )

    def testNLT_test26_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        OptionBuilder.withLongOpt("file")
        OptionBuilder.withLongOpt("file").hasArg0()
        OptionBuilder.withLongOpt("file").hasArg0().withValueSeparator0()

    def testNLT_test25_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        OptionBuilder.withLongOpt("file")
        OptionBuilder.withLongOpt("file").hasArg0()

    def testNLT_test24_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

        OptionBuilder.withLongOpt("file")

    def testNLT_test23_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")
        num_results_option = (
            OptionBuilder.withLongOpt("results")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Number of results per item")
            .create2("r")
        )

    def testNLT_test22_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "results"
        ).hasArg0().withValueSeparator0().withDescription("Number of results per item")

    def testNLT_test21_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()
        OptionBuilder.withLongOpt("results").hasArg0().withValueSeparator0()

    def testNLT_test20_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")
        OptionBuilder.withLongOpt("results").hasArg0()

    def testNLT_test19_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

        OptionBuilder.withLongOpt("results")

    def testNLT_test18_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")
        server_option = (
            OptionBuilder.withLongOpt("server")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("The NLT server address")
            .create2("s")
        )

    def testNLT_test17_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "server"
        ).hasArg0().withValueSeparator0().withDescription("The NLT server address")

    def testNLT_test16_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()
        OptionBuilder.withLongOpt("server").hasArg0().withValueSeparator0()

    def testNLT_test15_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")
        OptionBuilder.withLongOpt("server").hasArg0()

    def testNLT_test14_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

        OptionBuilder.withLongOpt("server")

    def testNLT_test13_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )
        age_option = (
            OptionBuilder.withLongOpt("age")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Age (in days) of cache item before being recomputed")
            .create2("a")
        )

    def testNLT_test12_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "age"
        ).hasArg0().withValueSeparator0().withDescription(
            "Age (in days) of cache item before being recomputed"
        )

    def testNLT_test11_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()
        OptionBuilder.withLongOpt("age").hasArg0().withValueSeparator0()

    def testNLT_test10_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")
        OptionBuilder.withLongOpt("age").hasArg0()

    def testNLT_test9_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )
        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

        OptionBuilder.withLongOpt("age")

    def testNLT_test8_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )

        time_limit_option = (
            OptionBuilder.withLongOpt("limit")
            .hasArg0()
            .withValueSeparator0()
            .withDescription("Set time limit for execution, in minutes")
            .create2("l")
        )

    def testNLT_test7_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()
        OptionBuilder.withLongOpt(
            "limit"
        ).hasArg0().withValueSeparator0().withDescription(
            "Set time limit for execution, in minutes"
        )

    def testNLT_test6_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()
        OptionBuilder.withLongOpt("limit").hasArg0().withValueSeparator0()

    def testNLT_test5_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

        OptionBuilder.withLongOpt("limit")
        OptionBuilder.withLongOpt("limit").hasArg0()

    def testNLT_test4_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )
        OptionBuilder.withLongOpt("limit")

    def testNLT_test3_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )
        tracker_run_option = Option(
            0,
            "t",
            "tracker",
            "Create NLT cache entries only for tracker items",
            False,
            None,
        )

    def testNLT_test2_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )
        new_run_option = Option(
            0, "n", "new", "Create NLT cache entries only for new items", False, None
        )

    def testNLT_test1_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)
        version_option = Option(
            0, "v", "version", "print version information", False, None
        )

    def testNLT_test0_decomposed(self) -> None:
        help_option = Option(0, "h", "help", "print this message", False, None)

    def testMan_test3_decomposed(self) -> None:
        cmd_line = (
            "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem]"
            " [-pstring] [-Llocale] [-eextension] [section] page ..."
        )
        options = (
            Options()
            .addOption3("a", "all", False, "find all matching manual pages.")
            .addOption3("d", "debug", False, "emit debugging messages.")
            .addOption3(
                "e", "extension", False, "limit search to extension type 'extension'."
            )
            .addOption3("f", "whatis", False, "equivalent to whatis.")
            .addOption3("k", "apropos", False, "equivalent to apropos.")
            .addOption3(
                "w", "location", False, "print physical location of man page(s)."
            )
            .addOption3(
                "l",
                "local-file",
                False,
                "interpret 'page' argument(s) as local filename(s)",
            )
            .addOption3("u", "update", False, "force a cache consistency check.")
            .addOption3("r", "prompt", True, "provide 'less' pager with prompt.")
            .addOption3(
                "c",
                "catman",
                False,
                "used by catman to reformat out of date cat pages.",
            )
            .addOption3(
                "7",
                "ascii",
                False,
                "display ASCII translation or certain latin1 chars.",
            )
            .addOption3("t", "troff", False, "use troff format pages.")
            .addOption3("T", "troff-device", True, "use groff with selected device.")
            .addOption3("Z", "ditroff", False, "use groff with selected device.")
            .addOption3(
                "D", "default", False, "reset all options to their default values."
            )
            .addOption3(
                "M", "manpath", True, "set search path for manual pages to 'path'."
            )
            .addOption3("P", "pager", True, "use program 'pager' to display output.")
            .addOption3("S", "sections", True, "use colon separated section list.")
            .addOption3(
                "m", "systems", True, "search for man pages from other unix system(s)."
            )
            .addOption3(
                "L", "locale", True, "define the locale for this particular man search."
            )
            .addOption3(
                "p",
                "preprocessor",
                True,
                "string indicates which preprocessor to run.\n"
                " e - [n]eqn  p - pic     t - tbl\n"
                " g - grap    r - refer   v - vgrind",
            )
            .addOption3("V", "version", False, "show version.")
            .addOption3("h", "help", False, "show this usage message.")
        )
        hf = HelpFormatter()
        eol = os.linesep
        out = io.StringIO()
        hf.printHelp3(
            out,
            60,
            cmd_line,
            None,
            options,
            HelpFormatter.DEFAULT_LEFT_PAD,
            HelpFormatter.DEFAULT_DESC_PAD,
            None,
            False,
        )
        self.assertEqual(
            "usage: man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath]"
            + eol
            + "           [-Ppager] [-Slist] [-msystem] [-pstring]"
            + eol
            + "           [-Llocale] [-eextension] [section] page ..."
            + eol
            + " -7,--ascii                display ASCII translation or"
            + eol
            + "                           certain latin1 chars."
            + eol
            + " -a,--all                  find all matching manual pages."
            + eol
            + " -c,--catman               used by catman to reformat out of"
            + eol
            + "                           date cat pages."
            + eol
            + " -d,--debug                emit debugging messages."
            + eol
            + " -D,--default              reset all options to their"
            + eol
            + "                           default values."
            + eol
            + " -e,--extension            limit search to extension type"
            + eol
            + "                           'extension'."
            + eol
            + " -f,--whatis               equivalent to whatis."
            + eol
            + " -h,--help                 show this usage message."
            + eol
            + " -k,--apropos              equivalent to apropos."
            + eol
            + " -l,--local-file           interpret 'page' argument(s) as"
            + eol
            + "                           local filename(s)"
            + eol
            + " -L,--locale <arg>         define the locale for this"
            + eol
            + "                           particular man search."
            + eol
            + " -M,--manpath <arg>        set search path for manual pages"
            + eol
            + "                           to 'path'."
            + eol
            + " -m,--systems <arg>        search for man pages from other"
            + eol
            + "                           unix system(s)."
            + eol
            + " -P,--pager <arg>          use program 'pager' to display"
            + eol
            + "                           output."
            + eol
            + " -p,--preprocessor <arg>   string indicates which"
            + eol
            + "                           preprocessor to run."
            + eol
            + "                           e - [n]eqn  p - pic     t - tbl"
            + eol
            + "                           g - grap    r - refer   v -"
            + eol
            + "                           vgrind"
            + eol
            + " -r,--prompt <arg>         provide 'less' pager with prompt."
            + eol
            + " -S,--sections <arg>       use colon separated section list."
            + eol
            + " -t,--troff                use troff format pages."
            + eol
            + " -T,--troff-device <arg>   use groff with selected device."
            + eol
            + " -u,--update               force a cache consistency check."
            + eol
            + " -V,--version              show version."
            + eol
            + " -w,--location             print physical location of man"
            + eol
            + "                           page(s)."
            + eol
            + " -Z,--ditroff              use groff with selected device."
            + eol,
            out.getvalue(),
        )

    def testMan_test2_decomposed(self) -> None:
        cmd_line = (
            "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem]"
            " [-pstring] [-Llocale] [-eextension] [section] page ..."
        )
        options = (
            Options()
            .addOption3("a", "all", False, "find all matching manual pages.")
            .addOption3("d", "debug", False, "emit debugging messages.")
            .addOption3(
                "e", "extension", False, "limit search to extension type 'extension'."
            )
            .addOption3("f", "whatis", False, "equivalent to whatis.")
            .addOption3("k", "apropos", False, "equivalent to apropos.")
            .addOption3(
                "w", "location", False, "print physical location of man page(s)."
            )
            .addOption3(
                "l",
                "local-file",
                False,
                "interpret 'page' argument(s) as local filename(s)",
            )
            .addOption3("u", "update", False, "force a cache consistency check.")
            .addOption3("r", "prompt", True, "provide 'less' pager with prompt.")
            .addOption3(
                "c",
                "catman",
                False,
                "used by catman to reformat out of date cat pages.",
            )
            .addOption3(
                "7",
                "ascii",
                False,
                "display ASCII translation or certain latin1 chars.",
            )
            .addOption3("t", "troff", False, "use troff format pages.")
            .addOption3("T", "troff-device", True, "use groff with selected device.")
            .addOption3("Z", "ditroff", False, "use groff with selected device.")
            .addOption3(
                "D", "default", False, "reset all options to their default values."
            )
            .addOption3(
                "M", "manpath", True, "set search path for manual pages to 'path'."
            )
            .addOption3("P", "pager", True, "use program 'pager' to display output.")
            .addOption3("S", "sections", True, "use colon separated section list.")
            .addOption3(
                "m", "systems", True, "search for man pages from other unix system(s)."
            )
            .addOption3(
                "L", "locale", True, "define the locale for this particular man search."
            )
            .addOption3(
                "p",
                "preprocessor",
                True,
                "string indicates which preprocessor to run.\n"
                + " e - [n]eqn  p - pic     t - tbl\n"
                + " g - grap    r - refer   v - vgrind",
            )
            .addOption3("V", "version", False, "show version.")
            .addOption3("h", "help", False, "show this usage message.")
        )
        hf = HelpFormatter()
        eol = os.linesep
        out = io.StringIO()
        hf.printHelp3(
            out,
            60,
            cmd_line,
            None,
            options,
            HelpFormatter.DEFAULT_LEFT_PAD,
            HelpFormatter.DEFAULT_DESC_PAD,
            None,
            False,
        )

    def testMan_test1_decomposed(self) -> None:
        cmd_line = (
            "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem]"
            " [-pstring] [-Llocale] [-eextension] [section] page ..."
        )
        options = (
            Options()
            .addOption3("a", "all", False, "find all matching manual pages.")
            .addOption3("d", "debug", False, "emit debugging messages.")
            .addOption3(
                "e", "extension", False, "limit search to extension type 'extension'."
            )
            .addOption3("f", "whatis", False, "equivalent to whatis.")
            .addOption3("k", "apropos", False, "equivalent to apropos.")
            .addOption3(
                "w", "location", False, "print physical location of man page(s)."
            )
            .addOption3(
                "l",
                "local-file",
                False,
                "interpret 'page' argument(s) as local filename(s)",
            )
            .addOption3("u", "update", False, "force a cache consistency check.")
            .addOption3("r", "prompt", True, "provide 'less' pager with prompt.")
            .addOption3(
                "c",
                "catman",
                False,
                "used by catman to reformat out of date cat pages.",
            )
            .addOption3(
                "7",
                "ascii",
                False,
                "display ASCII translation or certain latin1 chars.",
            )
            .addOption3("t", "troff", False, "use troff format pages.")
            .addOption3("T", "troff-device", True, "use groff with selected device.")
            .addOption3("Z", "ditroff", False, "use groff with selected device.")
            .addOption3(
                "D", "default", False, "reset all options to their default values."
            )
            .addOption3(
                "M", "manpath", True, "set search path for manual pages to 'path'."
            )
            .addOption3("P", "pager", True, "use program 'pager' to display output.")
            .addOption3("S", "sections", True, "use colon separated section list.")
            .addOption3(
                "m", "systems", True, "search for man pages from other unix system(s)."
            )
            .addOption3(
                "L", "locale", True, "define the locale for this particular man search."
            )
            .addOption3(
                "p",
                "preprocessor",
                True,
                "string indicates which preprocessor to run.\n"
                " e - [n]eqn  p - pic     t - tbl\n"
                " g - grap    r - refer   v - vgrind",
            )
            .addOption3("V", "version", False, "show version.")
            .addOption3("h", "help", False, "show this usage message.")
        )
        hf = HelpFormatter()

    def testMan_test0_decomposed(self) -> None:
        cmd_line = (
            "man [-c|-f|-k|-w|-tZT device] [-adlhu7V] [-Mpath] [-Ppager] [-Slist] [-msystem]"
            " [-pstring] [-Llocale] [-eextension] [section] page ..."
        )
        options = (
            Options()
            .addOption3("a", "all", False, "find all matching manual pages.")
            .addOption3("d", "debug", False, "emit debugging messages.")
            .addOption3(
                "e", "extension", False, "limit search to extension type 'extension'."
            )
            .addOption3("f", "whatis", False, "equivalent to whatis.")
            .addOption3("k", "apropos", False, "equivalent to apropos.")
            .addOption3(
                "w", "location", False, "print physical location of man page(s)."
            )
            .addOption3(
                "l",
                "local-file",
                False,
                "interpret 'page' argument(s) as local filename(s)",
            )
            .addOption3("u", "update", False, "force a cache consistency check.")
            .addOption3("r", "prompt", True, "provide 'less' pager with prompt.")
            .addOption3(
                "c",
                "catman",
                False,
                "used by catman to reformat out of date cat pages.",
            )
            .addOption3(
                "7",
                "ascii",
                False,
                "display ASCII translation or certain latin1 chars.",
            )
            .addOption3("t", "troff", False, "use troff format pages.")
            .addOption3("T", "troff-device", True, "use groff with selected device.")
            .addOption3("Z", "ditroff", False, "use groff with selected device.")
            .addOption3(
                "D", "default", False, "reset all options to their default values."
            )
            .addOption3(
                "M", "manpath", True, "set search path for manual pages to 'path'."
            )
            .addOption3("P", "pager", True, "use program 'pager' to display output.")
            .addOption3("S", "sections", True, "use colon separated section list.")
            .addOption3(
                "m", "systems", True, "search for man pages from other unix system(s)."
            )
            .addOption3(
                "L", "locale", True, "define the locale for this particular man search."
            )
            .addOption3(
                "p",
                "preprocessor",
                True,
                "string indicates which preprocessor to run.\n"
                " e - [n]eqn  p - pic     t - tbl\n"
                " g - grap    r - refer   v - vgrind",
            )
            .addOption3("V", "version", False, "show version.")
            .addOption3("h", "help", False, "show this usage message.")
        )

    def testLs_test13_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()

        # Adding options to the Options object
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )
        options.addOption0(block_size_option)

        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entried ending with ~"
        )
        options.addOption1(
            "c",
            False,
            "with -lt: sort by, and show, ctime (time of last modification of file status "
            "information) with -l:show ctime and sort by name otherwise: sort by ctime",
        )
        options.addOption1("C", False, "list entries by columns")

        # Parsing command-line arguments
        args = ["--block-size=10"]
        line = parser.parse0(options, args)

        # Assertions
        self.assertTrue(line.hasOption2("block-size"))
        self.assertEqual(line.getOptionValue4("block-size"), "10")

    def testLs_test12_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )

        options.addOption0(block_size_option)
        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entries ending with ~"
        )
        options.addOption1(
            "c",
            False,
            "with -lt: sort by, and show, ctime (time of last modification of file status "
            "information) with -l:show ctime and sort by name otherwise: sort by ctime",
        )
        options.addOption1("C", False, "list entries by columns")

        args = ["--block-size=10"]
        line = parser.parse0(options, args)
        self.assertTrue(line.hasOption2("block-size"))

    def testLs_test11_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )
        options.addOption0(block_size_option)

        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entried ending with ~"
        )
        options.addOption1(
            "c",
            False,
            "with -lt: sort by, and show, ctime (time of last modification of file status "
            "information) with -l:show ctime and sort by name otherwise: sort by ctime",
        )
        options.addOption1("C", False, "list entries by columns")

        args = ["--block-size=10"]
        line = parser.parse0(options, args)

    def testLs_test10_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )
        options.addOption0(block_size_option)

        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entries ending with ~"
        )
        options.addOption1(
            "c",
            False,
            "with -lt: sort by, and show, ctime (time of last modification of file status "
            "information) with -l:show ctime and sort by name otherwise: sort by ctime",
        )
        options.addOption1("C", False, "list entries by columns")

    def testLs_test9_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )
        options.addOption0(block_size_option)

        options.addOption3(
            "B", "ignore-backups", False, "do not list implied entries ending with ~"
        )

    def testLs_test8_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        block_size_option = (
            OptionBuilder.withLongOpt("block-size")
            .withDescription("use SIZE-byte blocks")
            .hasArg0()
            .withArgName("SIZE")
            .create0()
        )

        options.addOption0(block_size_option)

    def testLs_test7_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE").create0()

    def testLs_test6_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )
        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0().withArgName("SIZE")

    def testLs_test5_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )
        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")
        OptionBuilder.withLongOpt("block-size").withDescription(
            "use SIZE-byte blocks"
        ).hasArg0()

    def testLs_test4_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )
        OptionBuilder.withLongOpt("block-size")
        OptionBuilder.withLongOpt("block-size").withDescription("use SIZE-byte blocks")

    def testLs_test3_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )
        OptionBuilder.withLongOpt("block-size")

    def testLs_test2_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()
        options.addOption3("a", "all", False, "do not hide entries starting with .")
        options.addOption3("A", "almost-all", False, "do not list implied . and ..")
        options.addOption3(
            "b", "escape", False, "print octal escapes for nongraphic characters"
        )

    def testLs_test1_decomposed(self) -> None:
        parser = PosixParser()
        options = Options()

    def testLs_test0_decomposed(self) -> None:
        parser = PosixParser()

    def testGroovy_test60_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        # Define the "line" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        line_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(line_option)

        # Define the "print" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        print_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(print_option)

        # Define the "port" option
        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        port_option = (
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )
        options.addOption0(port_option)

        # Define the "autosplit" option
        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")
        autosplit_option = (
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )
        options.addOption0(autosplit_option)

        # Parse the command line
        parser = PosixParser()
        line = parser.parse1(options, ["-e", "println 'hello'"], True)

        # Assertions
        self.assertTrue(line.hasOption0("e"))
        self.assertEqual("println 'hello'", line.getOptionValue0("e"))

    def testGroovy_test59_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        # Define the "line" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        line_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(line_option)

        # Define the "print result" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        print_result_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(print_result_option)

        # Define the "port" option
        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        port_option = (
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )
        options.addOption0(port_option)

        # Define the "autosplit" option
        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")
        autosplit_option = (
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )
        options.addOption0(autosplit_option)

        # Parse the command line
        parser = PosixParser()
        line = parser.parse1(options, ["-e", "println 'hello'"], True)

        # Assert that the "e" option is present
        self.assertTrue(line.hasOption0("e"))

    def testGroovy_test58_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit").create1("a")
        options.addOption0(
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )

        parser = PosixParser()
        line = parser.parse1(options, ["-e", "println 'hello'"], True)

    def testGroovy_test57_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit").create1("a")
        options.addOption0(
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )

        parser = PosixParser()

    def testGroovy_test56_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")
        options.addOption0(
            OptionBuilder.withArgName("splitPattern")
            .hasOptionalArg()
            .withDescription(
                "split lines using splitPattern (default '\\s') using implicit 'split' variable"
            )
            .withLongOpt("autosplit")
            .create1("a")
        )

    def testGroovy_test55_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        # Define the "help" option
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        # Define the "debug" option
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        # Define the "version" option
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        # Define the "encoding" option
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        # Define the "script" option
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        # Define the "extension" option
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        # Define the "line" option
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        # Define the "print result" option
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        # Define the "port" option
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        # Define the "autosplit" option
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit").create1("a")

    def testGroovy_test54_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        ).withLongOpt("autosplit")

    def testGroovy_test53_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()
        OptionBuilder.withArgName("splitPattern").hasOptionalArg().withDescription(
            "split lines using splitPattern (default '\\s') using implicit 'split' variable"
        )

    def testGroovy_test52_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")
        OptionBuilder.withArgName("splitPattern").hasOptionalArg()

    def testGroovy_test51_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

        OptionBuilder.withArgName("splitPattern")

    def testGroovy_test50_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")
        options.addOption0(
            OptionBuilder.withArgName("port")
            .hasOptionalArg()
            .withDescription("listen on a port and process inbound lines")
            .create1("l")
        )

    def testGroovy_test49_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        ).create1("l")

    def testGroovy_test48_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        # Define the "line" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        line_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(line_option)

        # Define the "print" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        print_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(print_option)

        # Define the "port" option
        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()
        OptionBuilder.withArgName("port").hasOptionalArg().withDescription(
            "listen on a port and process inbound lines"
        )

    def testGroovy_test47_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        ).create1("p")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

        OptionBuilder.withArgName("port")
        OptionBuilder.withArgName("port").hasOptionalArg()

    def testGroovy_test46_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        # Define the "line" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        line_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(line_option)

        # Define the "print" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        print_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(print_option)

        # Define the "port" option (not fully implemented in the Java code)
        OptionBuilder.withArgName("port")

    def testGroovy_test45_decomposed(self) -> None:
        options = Options()

        # Define "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        # Define "line" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        line_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )
        options.addOption0(line_option)

        # Define "print result" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        print_result_option = (
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )
        options.addOption0(print_result_option)

    def testGroovy_test44_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line and print result (see also -n)"
            )
            .create1("p")
        )

    def testGroovy_test43_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line and print result (see also -n)"
        )

    def testGroovy_test42_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

    def testGroovy_test41_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription(
                "process files line by line using implicit 'line' variable"
            )
            .create1("n")
        )

    def testGroovy_test40_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        ).create1("n")

    def testGroovy_test39_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "process files line by line using implicit 'line' variable"
        )

    def testGroovy_test38_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )
        options.addOption0(extension_option)

        OptionBuilder.hasArg1(False)

    def testGroovy_test37_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        ).create1("i")
        options.addOption0(
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

    def testGroovy_test36_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )
        extension_option = (
            OptionBuilder.withArgName("extension")
            .hasOptionalArg()
            .withDescription(
                "modify files in place; create backup if extension is given (e.g. '.bak')"
            )
            .create1("i")
        )

    def testGroovy_test35_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        # Define the "encoding" option
        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        # Define the "script" option
        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )
        options.addOption0(script_option)

        # Define the "extension" option
        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()
        OptionBuilder.withArgName("extension").hasOptionalArg().withDescription(
            "modify files in place; create backup if extension is given (e.g. '.bak')"
        )

    def testGroovy_test34_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")
        OptionBuilder.withArgName("extension").hasOptionalArg()

    def testGroovy_test33_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

        OptionBuilder.withArgName("extension")

    def testGroovy_test32_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding").create1("c")
        options.addOption0(
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        ).create1("e")
        options.addOption0(
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

    def testGroovy_test31_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )
        script_option = (
            OptionBuilder.withArgName("script")
            .hasArg0()
            .withDescription("specify a command line script")
            .create1("e")
        )

    def testGroovy_test30_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()
        OptionBuilder.withArgName("script").hasArg0().withDescription(
            "specify a command line script"
        )

    def testGroovy_test29_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        OptionBuilder.withArgName("script")
        OptionBuilder.withArgName("script").hasArg0()

    def testGroovy_test28_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

        OptionBuilder.withArgName("script")

    def testGroovy_test27_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

    def testGroovy_test26_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")
        encoding_option = (
            OptionBuilder.withArgName("charset")
            .hasArg0()
            .withDescription("specify the encoding of the files")
            .withLongOpt("encoding")
            .create1("c")
        )
        options.addOption0(encoding_option)

    def testGroovy_test25_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        ).withLongOpt("encoding")

    def testGroovy_test24_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()
        OptionBuilder.withArgName("charset").hasArg0().withDescription(
            "specify the encoding of the files"
        )

    def testGroovy_test23_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")
        options.addOption0(
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        ).create1("h")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug").create1("d")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version").create1("v")
        options.addOption0(
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )

        OptionBuilder.withArgName("charset")
        OptionBuilder.withArgName("charset").hasArg0()

    def testGroovy_test22_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

        OptionBuilder.withArgName("charset")

    def testGroovy_test21_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

    def testGroovy_test20_decomposed(self) -> None:
        options = Options()

        # Define the "define" option
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        # Define the "help" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        # Define the "debug" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        # Define the "version" option
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")
        version_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("display the Groovy and JVM versions")
            .withLongOpt("version")
            .create1("v")
        )
        options.addOption0(version_option)

    def testGroovy_test19_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        ).withLongOpt("version")

    def testGroovy_test18_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "display the Groovy and JVM versions"
        )

    def testGroovy_test17_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

        OptionBuilder.hasArg1(False)

    def testGroovy_test16_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )
        options.addOption0(debug_option)

    def testGroovy_test15_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")
        debug_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("debug mode will print out full stack traces")
            .withLongOpt("debug")
            .create1("d")
        )

    def testGroovy_test14_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        ).withLongOpt("debug")

    def testGroovy_test13_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription(
            "debug mode will print out full stack traces"
        )

    def testGroovy_test12_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

        OptionBuilder.hasArg1(False)

    def testGroovy_test11_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        define_option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(define_option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        help_option = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )
        options.addOption0(help_option)

    def testGroovy_test10_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        option_define = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(option_define)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )
        option_help = (
            OptionBuilder.hasArg1(False)
            .withDescription("usage information")
            .withLongOpt("help")
            .create1("h")
        )

    def testGroovy_test9_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(option)

        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")
        OptionBuilder.hasArg1(False).withDescription("usage information").withLongOpt(
            "help"
        )

    def testGroovy_test8_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(option)
        OptionBuilder.hasArg1(False)
        OptionBuilder.hasArg1(False).withDescription("usage information")

    def testGroovy_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(option)
        OptionBuilder.hasArg1(False)

    def testGroovy_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")
        option = (
            OptionBuilder.withLongOpt("define")
            .withDescription("define a system property")
            .hasArg1(True)
            .withArgName("name=value")
            .create1("D")
        )
        options.addOption0(option)

    def testGroovy_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value").create1("D")

    def testGroovy_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True).withArgName("name=value")

    def testGroovy_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")
        OptionBuilder.withLongOpt("define").withDescription(
            "define a system property"
        ).hasArg1(True)

    def testGroovy_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")
        OptionBuilder.withLongOpt("define").withDescription("define a system property")

    def testGroovy_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("define")

    def testGroovy_test0_decomposed(self) -> None:
        options = Options()

    def testAnt_test14_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        option_d = (
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption0(option_d)
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )

        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)
        opts = line.getOptionValues2("D")

        self.assertEqual("property", opts[0])
        self.assertEqual("value", opts[1])
        self.assertEqual("property1", opts[2])
        self.assertEqual("value1", opts[3])
        self.assertEqual("mybuild.xml", line.getOptionValue4("buildfile"))
        self.assertTrue(line.hasOption2("projecthelp"))

    def testAnt_test13_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        options.addOption0(
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )
        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)
        opts = line.getOptionValues2("D")
        self.assertEqual("property", opts[0])
        self.assertEqual("value", opts[1])
        self.assertEqual("property1", opts[2])
        self.assertEqual("value1", opts[3])
        self.assertEqual("mybuild.xml", line.getOptionValue4("buildfile"))

    def testAnt_test12_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        options.addOption0(
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )
        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)
        opts = line.getOptionValues2("D")
        self.assertEqual("property", opts[0])
        self.assertEqual("value", opts[1])
        self.assertEqual("property1", opts[2])
        self.assertEqual("value1", opts[3])

    def testAnt_test11_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        options.addOption0(
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )
        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)
        opts = line.getOptionValues2("D")
        self.assertEqual("property", opts[0])
        self.assertEqual("value", opts[1])

    def testAnt_test10_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        option_d = (
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption0(option_d)
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )

        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)
        opts = line.getOptionValues2("D")

    def testAnt_test9_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        option_d = (
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption0(option_d)
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )
        args = [
            "-buildfile",
            "mybuild.xml",
            "-Dproperty=value",
            "-Dproperty1=value1",
            "-projecthelp",
        ]
        line = parser.parse0(options, args)

    def testAnt_test8_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        option_d = (
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption0(option_d)
        options.addOption1(
            "find",
            True,
            "search for buildfile towards the root of the filesystem and use it",
        )

    def testAnt_test7_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        option = (
            OptionBuilder.withDescription("use value for given property")
            .hasArgs0()
            .withValueSeparator0()
            .create1("D")
        )
        options.addOption0(option)

    def testAnt_test6_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0().create1("D")

    def testAnt_test5_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()
        OptionBuilder.withDescription(
            "use value for given property"
        ).hasArgs0().withValueSeparator0()

    def testAnt_test4_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")
        OptionBuilder.withDescription("use value for given property").hasArgs0()

    def testAnt_test3_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")
        OptionBuilder.withDescription("use value for given property")

    def testAnt_test2_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()
        options.addOption1("help", False, "print this message")
        options.addOption1("projecthelp", False, "print project help information")
        options.addOption1("version", False, "print the version information and exit")
        options.addOption1("quiet", False, "be extra quiet")
        options.addOption1("verbose", False, "be extra verbose")
        options.addOption1("debug", False, "print debug information")
        options.addOption1("logfile", True, "use given file for log")
        options.addOption1("logger", True, "the class which is to perform the logging")
        options.addOption1(
            "listener", True, "add an instance of a class as a project listener"
        )
        options.addOption1("buildfile", True, "use given buildfile")

    def testAnt_test1_decomposed(self) -> None:
        parser = GnuParser()
        options = Options()

    def testAnt_test0_decomposed(self) -> None:
        parser = GnuParser()
