from __future__ import annotations
import time
import re
import sys
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
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class BugsTest(unittest.TestCase):

    def test31148_test7_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()
        options.addOption0(multi_arg_option)
        parser = PosixParser()
        args = []
        props = {"o": "ovalue"}
        cl = parser.parse2(options, args, props)
        self.assertTrue(cl.hasOption0("o"))
        self.assertEqual("ovalue", cl.getOptionValue0("o"))

    def test31148_test6_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()
        options.addOption0(multi_arg_option)
        parser = PosixParser()
        args = []
        props = {"o": "ovalue"}
        cl = parser.parse2(options, args, props)
        self.assertTrue(cl.hasOption0("o"))

    def test31148_test5_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()
        options.addOption0(multi_arg_option)
        parser = PosixParser()
        args = []
        props = {"o": "ovalue"}
        cl = parser.parse2(options, args, props)

    def test31148_test4_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()
        options.addOption0(multi_arg_option)
        parser = PosixParser()

    def test31148_test3_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()
        options.addOption0(multi_arg_option)

    def test31148_test2_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)
        options = Options()

    def test31148_test1_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")
        multi_arg_option.setArgs(1)

    def test31148_test0_decomposed(self) -> None:
        multi_arg_option = Option.Option1("o", "option with multiple args")

    def test15648_test6_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()
        m = OptionBuilder.hasArgs0().create2("m")
        options = Options()
        options.addOption0(m)
        line = parser.parse0(options, args)
        self.assertEqual("Two Words", line.getOptionValue4("m"))

    def test15648_test5_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()
        m = OptionBuilder.hasArgs0().create2("m")
        options = Options()
        options.addOption0(m)
        line = parser.parse0(options, args)

    def test15648_test4_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()
        m = OptionBuilder.hasArgs0().create2("m")
        options = Options()
        options.addOption0(m)

    def test15648_test3_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()
        m = OptionBuilder.hasArgs0().create2("m")
        options = Options()

    def test15648_test2_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()
        m = OptionBuilder.hasArgs0().create2("m")

    def test15648_test1_decomposed(self) -> None:
        parser = PosixParser()
        args = ["-m", '"Two Words"']
        OptionBuilder.hasArgs0()

    def test15648_test0_decomposed(self) -> None:
        parser = PosixParser()

    def test15046_test7_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))
        parser.parse0(options, cli_args)
        options.addOption3("c", "conflict", True, "conflict option")
        line = parser.parse0(options, cli_args)
        self.assertEqual(line.getOptionValue0("z"), "c")
        self.assertFalse(line.hasOption2("c"))

    def test15046_test6_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))
        parser.parse0(options, cli_args)
        options.addOption3("c", "conflict", True, "conflict option")
        line = parser.parse0(options, cli_args)
        self.assertEqual(line.getOptionValue0("z"), "c")

    def test15046_test5_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))
        parser.parse0(options, cli_args)
        options.addOption3("c", "conflict", True, "conflict option")
        line = parser.parse0(options, cli_args)

    def test15046_test4_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))
        parser.parse0(options, cli_args)
        options.addOption3("c", "conflict", True, "conflict option")

    def test15046_test3_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))
        parser.parse0(options, cli_args)

    def test15046_test2_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()
        options.addOption0(Option(0, "z", "timezone", "affected option", True, None))

    def test15046_test1_decomposed(self) -> None:
        parser = PosixParser()
        cli_args = ["-z", "c"]
        options = Options()

    def test15046_test0_decomposed(self) -> None:
        parser = PosixParser()

    def test14786_test7_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()
        opts.addOption0(o)
        opts.addOption0(o)
        parser = GnuParser()
        args = ["-test"]
        line = parser.parse0(opts, args)
        self.assertTrue(line.hasOption2("test"))

    def test14786_test6_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()
        opts.addOption0(o)
        opts.addOption0(o)
        parser = GnuParser()
        args = ["-test"]
        line = parser.parse0(opts, args)

    def test14786_test5_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()
        opts.addOption0(o)
        opts.addOption0(o)
        parser = GnuParser()

    def test14786_test4_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()
        opts.addOption0(o)
        opts.addOption0(o)

    def test14786_test3_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")
        opts = Options()

    def test14786_test2_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")
        o = OptionBuilder.isRequired0().withDescription("test").create2("test")

    def test14786_test1_decomposed(self) -> None:
        OptionBuilder.isRequired0()
        OptionBuilder.isRequired0().withDescription("test")

    def test14786_test0_decomposed(self) -> None:
        OptionBuilder.isRequired0()

    def test13935_test17_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s"]
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s", "-l"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)
        opts.addOption0(forward)
        args = ["-s", "-l", "-f"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)

    def test13935_test16_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s"]
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s", "-l"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)
        opts.addOption0(forward)
        args = ["-s", "-l", "-f"]
        line = parser.parse0(opts, args)

    def test13935_test15_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        with pytest.raises(ParseException):
            parser.parse0(opts, args)
        args = ["-s"]
        with pytest.raises(ParseException):
            parser.parse0(opts, args)
        args = ["-s", "-l"]
        line = parser.parse0(opts, args)
        self.assertIsNotNone(line)
        opts.addOption0(forward)

    def test13935_test14_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s"]
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass
        args = ["-s", "-l"]
        line = parser.parse0(opts, args)

    def test13935_test13_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        with pytest.raises(ParseException):
            parser.parse0(opts, args)
        args = ["-s"]
        with pytest.raises(ParseException):
            parser.parse0(opts, args)

    def test13935_test12_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()
        args = []
        try:
            parser.parse0(opts, args)
            pytest.fail("Expected ParseException")
        except ParseException:
            pass

    def test13935_test11_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)
        parser = PosixParser()

    def test13935_test10_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)
        opts.addOption0(straight)

    def test13935_test9_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.addOption(straight)
        directions.addOption(forward)
        directions.setRequired(True)
        opts = Options()
        opts.addOptionGroup(directions)

    def test13935_test8_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)
        opts = Options()

    def test13935_test7_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)
        directions.setRequired(True)

    def test13935_test6_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)
        directions.addOption(left)
        directions.addOption(right)

    def test13935_test5_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)
        forward.setRequired(True)

    def test13935_test4_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)
        forward = Option(0, "f", "forward", "go forward", False, None)

    def test13935_test3_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)
        straight = Option(0, "s", "straight", "go straight", False, None)

    def test13935_test2_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)
        right = Option(0, "r", "right", "go right", False, None)

    def test13935_test1_decomposed(self) -> None:
        directions = OptionGroup()
        left = Option(0, "l", "left", "go left", False, None)

    def test13935_test0_decomposed(self) -> None:
        directions = OptionGroup()

    def test13666_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withDescription("dir")
        OptionBuilder.withDescription("dir").hasArg0()
        dir_option = OptionBuilder.withDescription("dir").hasArg0().create1("d")
        options.addOption0(dir_option)

        old_system_out = sys.stdout
        try:
            bytes_io = io.StringIO()
            sys.stdout = bytes_io

            print()  # Print a blank line
            eol = bytes_io.getvalue()
            bytes_io.truncate(0)
            bytes_io.seek(0)

            formatter = HelpFormatter()
            formatter.printHelp4("dir", options)

            self.assertEqual(
                f"usage: dir{eol} -d <arg>   dir{eol}", bytes_io.getvalue()
            )
        finally:
            sys.stdout = old_system_out

    def test13666_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withDescription("dir")
        OptionBuilder.withDescription("dir").hasArg0()
        dir_option = OptionBuilder.withDescription("dir").hasArg0().create1("d")
        options.addOption0(dir_option)

    def test13666_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withDescription("dir")
        OptionBuilder.withDescription("dir").hasArg0()
        dir_option = OptionBuilder.withDescription("dir").hasArg0().create1("d")

    def test13666_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withDescription("dir")
        OptionBuilder.withDescription("dir").hasArg0()

    def test13666_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withDescription("dir")

    def test13666_test0_decomposed(self) -> None:
        options = Options()

    def test13425_test12_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

        args = ["-o", "-n", "newpassword"]
        options.addOption0(oldpass)
        options.addOption0(newpass)

        parser = PosixParser()
        try:
            parser.parse0(options, args)
            pytest.fail("MissingArgumentException not caught.")
        except MissingArgumentException:
            pass

    def test13425_test11_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

        args = ["-o", "-n", "newpassword"]
        options.addOption0(oldpass)
        options.addOption0(newpass)

        parser = PosixParser()

    def test13425_test10_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

        args = ["-o", "-n", "newpassword"]
        options.addOption0(oldpass)
        options.addOption0(newpass)

    def test13425_test9_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

        args = ["-o", "-n", "newpassword"]
        options.addOption0(oldpass)

    def test13425_test8_decomposed(self) -> None:
        options = Options()

        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()
        newpass = (
            OptionBuilder.withLongOpt("new-password")
            .withDescription("Use this option to specify the new password")
            .hasArg0()
            .create1("n")
        )

    def test13425_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )
        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        ).hasArg0()

    def test13425_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )
        OptionBuilder.withLongOpt("new-password")
        OptionBuilder.withLongOpt("new-password").withDescription(
            "Use this option to specify the new password"
        )

    def test13425_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )
        OptionBuilder.withLongOpt("new-password")

    def test13425_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()
        oldpass = (
            OptionBuilder.withLongOpt("old-password")
            .withDescription("Use this option to specify the old password")
            .hasArg0()
            .create1("o")
        )

    def test13425_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        ).hasArg0()

    def test13425_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")
        OptionBuilder.withLongOpt("old-password").withDescription(
            "Use this option to specify the old password"
        )

    def test13425_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("old-password")

    def test13425_test0_decomposed(self) -> None:
        options = Options()

    def test12210_test14_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]

        grp = OptionGroup()
        grp.addOption(Parser.Option2("exec", False, "description for this option"))
        grp.addOption(Parser.Option2("rep", False, "description for this option"))
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, "desc")
        exec_options.addOption1("exec_opt2", False, "desc")

        rep_options = Options()
        rep_options.addOption1("repopto", False, "desc")
        rep_options.addOption1("repoptt", False, "desc")

        parser = GnuParser()
        cmd = parser.parse1(main_options, argv, True)
        argv = cmd.getArgs()

        if cmd.hasOption2("exec"):
            cmd = parser.parse1(exec_options, argv, False)
            self.assertTrue(cmd.hasOption2("exec_opt1"))
            self.assertTrue(cmd.hasOption2("exec_opt2"))
        elif cmd.hasOption2("rep"):
            cmd = parser.parse1(rep_options, argv, False)
        else:
            pytest.fail("exec option not found")

    def test12210_test13_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]

        grp = OptionGroup()
        grp.addOption(Parser.Option2("exec", False, "description for this option"))
        grp.addOption(Parser.Option2("rep", False, "description for this option"))
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, "desc")
        exec_options.addOption1("exec_opt2", False, "desc")

        rep_options = Options()
        rep_options.addOption1("repopto", False, "desc")
        rep_options.addOption1("repoptt", False, "desc")

        parser = GnuParser()
        cmd = parser.parse1(main_options, argv, True)
        argv = cmd.getArgs()

    def test12210_test12_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]

        grp = OptionGroup()
        grp.addOption(Parser.Option2("exec", False, "description for this option"))
        grp.addOption(Parser.Option2("rep", False, "description for this option"))
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, "desc")
        exec_options.addOption1("exec_opt2", False, "desc")

        rep_options = Options()
        rep_options.addOption1("repopto", False, "desc")
        rep_options.addOption1("repoptt", False, "desc")

        parser = GnuParser()
        cmd = parser.parse1(main_options, argv, True)

    def test12210_test11_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, "desc")
        exec_options.addOption1("exec_opt2", False, "desc")

        rep_options = Options()
        rep_options.addOption1("repopto", False, "desc")
        rep_options.addOption1("repoptt", False, "desc")

        parser = GnuParser()

    def test12210_test10_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, "desc")
        exec_options.addOption1("exec_opt2", False, "desc")

        rep_options = Options()
        rep_options.addOption1("repopto", False, "desc")
        rep_options.addOption1("repoptt", False, "desc")

    def test12210_test9_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, " desc")
        exec_options.addOption1("exec_opt2", False, " desc")

        rep_options = Options()

    def test12210_test8_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )
        main_options.addOptionGroup(grp)

        exec_options = Options()
        exec_options.addOption1("exec_opt1", False, " desc")
        exec_options.addOption1("exec_opt2", False, " desc")

    def test12210_test7_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()

        # Adding "exec" option to the group
        exec_option = OptionBuilder.Option2(
            "exec", False, "description for this option"
        )
        grp.addOption(exec_option)

        # Adding "rep" option to the group
        rep_option = OptionBuilder.Option2("rep", False, "description for this option")
        grp.addOption(rep_option)

        # Adding the group to main options
        main_options.addOptionGroup(grp)

        # Creating execOptions
        exec_options = Options()

    def test12210_test6_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )
        main_options.addOptionGroup(grp)

    def test12210_test5_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        grp.addOption(
            OptionBuilder.Option2("rep", False, "description for this option")
        )

    def test12210_test4_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        grp.addOption(
            OptionBuilder.Option2("exec", False, "description for this option")
        )
        OptionBuilder.Option2("rep", False, "description for this option")

    def test12210_test3_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        option = OptionBuilder.Option2("exec", False, "description for this option")
        grp.addOption(option)

    def test12210_test2_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()
        option = OptionBuilder.Option2("exec", False, "description for this option")

    def test12210_test1_decomposed(self) -> None:
        main_options = Options()
        argv = ["-exec", "-exec_opt1", "-exec_opt2"]
        grp = OptionGroup()

    def test12210_test0_decomposed(self) -> None:
        main_options = Options()

    def test11680_test4_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "foobar")
        options.addOption1("m", True, "missing")
        args = ["-f", "foo"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        cmd.getOptionValue5("f", "default f")
        cmd.getOptionValue5("m", "default m")

    def test11680_test3_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "foobar")
        options.addOption1("m", True, "missing")
        args = ["-f", "foo"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

    def test11680_test2_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "foobar")
        options.addOption1("m", True, "missing")
        args = ["-f", "foo"]
        parser = PosixParser()

    def test11680_test1_decomposed(self) -> None:
        options = Options()
        options.addOption1("f", True, "foobar")
        options.addOption1("m", True, "missing")

    def test11680_test0_decomposed(self) -> None:
        options = Options()

    def test11458_test16_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse arguments
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Validate 'D' option values
        values = cmd.getOptionValues0("D")
        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

        # Validate 'p' option values
        values = cmd.getOptionValues0("p")
        self.assertEqual(values[0], "file1")
        self.assertEqual(values[1], "file2")
        self.assertEqual(values[2], "file3")

        # Iterate through options and validate
        iter = cmd.iterator()
        for opt in iter:
            if opt.getId() == ord("D"):
                self.assertEqual(opt.getValue1(0), "JAVA_HOME")
                self.assertEqual(opt.getValue1(1), "/opt/java")
            elif opt.getId() == ord("p"):
                self.assertEqual(opt.getValue1(0), "file1")
                self.assertEqual(opt.getValue1(1), "file2")
                self.assertEqual(opt.getValue1(2), "file3")
            else:
                pytest.fail("-D option not found")

    def test11458_test15_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse arguments
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Validate 'D' option values
        values = cmd.getOptionValues0("D")
        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

        # Validate 'p' option values
        values = cmd.getOptionValues0("p")
        self.assertEqual(values[0], "file1")
        self.assertEqual(values[1], "file2")
        self.assertEqual(values[2], "file3")

        # Iterate over options (not used further in the test)
        iter_options = cmd.iterator()

    def test11458_test14_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse arguments
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Validate 'D' option values
        values = cmd.getOptionValues0("D")
        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

        # Validate 'p' option values
        values = cmd.getOptionValues0("p")
        self.assertEqual(values[0], "file1")
        self.assertEqual(values[1], "file2")

    def test11458_test13_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        option_d = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(option_d)

        # Configure OptionBuilder for 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        option_p = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(option_p)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse the arguments
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Validate 'D' option values
        values = cmd.getOptionValues0("D")
        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

        # Validate 'p' option values
        values = cmd.getOptionValues0("p")

    def test11458_test12_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for '=' separator and add 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for ':' separator and add 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse arguments
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Retrieve and validate 'D' option values
        values = cmd.getOptionValues0("D")
        self.assertEqual(values[0], "JAVA_HOME")
        self.assertEqual(values[1], "/opt/java")

    def test11458_test11_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for '=' separator and add 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for ':' separator and add 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse arguments using PosixParser
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Retrieve option values for 'D'
        values = cmd.getOptionValues0("D")

    def test11458_test10_decomposed(self) -> None:
        options = Options()

        # Configure OptionBuilder for '=' separator and add 'D' option
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        d_option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(d_option)

        # Configure OptionBuilder for ':' separator and add 'p' option
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        p_option = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(p_option)

        # Define arguments
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]

        # Parse the arguments using PosixParser
        parser = PosixParser()
        cmd = parser.parse0(options, args)

    def test11458_test9_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        option_d = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(option_d)
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        option_p = OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(option_p)
        args = ["-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"]
        parser = PosixParser()

    def test11458_test8_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        )
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        options.addOption0(
            OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")
        )

    def test11458_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        )
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()
        OptionBuilder.withValueSeparator1(":").hasArgs0().create1("p")

    def test11458_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(
            OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        )
        OptionBuilder.withValueSeparator1(":")
        OptionBuilder.withValueSeparator1(":").hasArgs0()

    def test11458_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(option)
        OptionBuilder.withValueSeparator1(":")

    def test11458_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        option = OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")
        options.addOption0(option)

    def test11458_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()
        OptionBuilder.withValueSeparator1("=").hasArgs0().create1("D")

    def test11458_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")
        OptionBuilder.withValueSeparator1("=").hasArgs0()

    def test11458_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withValueSeparator1("=")

    def test11458_test0_decomposed(self) -> None:
        options = Options()

    def test11457_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        verbose_option = OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(verbose_option)

        args = ["--verbose"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        self.assertTrue(cmd.hasOption2("verbose"))

    def test11457_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())
        args = ["--verbose"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

    def test11457_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())
        args = ["--verbose"]
        parser = PosixParser()

    def test11457_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0())

    def test11457_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")
        OptionBuilder.withLongOpt("verbose").create0()

    def test11457_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.withLongOpt("verbose")

    def test11457_test0_decomposed(self) -> None:
        options = Options()

    def test11456_test19_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-b", "value"]
        parser = GnuParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

    def test11456_test18_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-b", "value"]
        parser = GnuParser()
        cmd = parser.parse0(options, args)

    def test11456_test17_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-b", "value"]
        parser = GnuParser()

    def test11456_test16_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        self.assertEqual(cmd.getOptionValue0("b"), "value")

        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

    def test11456_test15_decomposed(self) -> None:
        options = Options()

        # Adding option 'a' with optional argument
        OptionBuilder.hasOptionalArg()
        option_a = OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(option_a)

        # Adding option 'b' with required argument
        OptionBuilder.hasArg0()
        option_b = OptionBuilder.hasArg0().create1("b")
        options.addOption0(option_b)

        # Parsing command line arguments
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

        # Asserting the value of option 'b'
        self.assertEqual(cmd.getOptionValue0("b"), "value")

        # Reinitializing options for further testing
        options = Options()

        # Adding option 'a' with optional argument again
        OptionBuilder.hasOptionalArg()
        option_a = OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(option_a)

        # Adding option 'b' with required argument again
        OptionBuilder.hasArg0()
        option_b = OptionBuilder.hasArg0().create1("b")

    def test11456_test14_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()

    def test11456_test13_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))

    def test11456_test12_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")

    def test11456_test11_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
        options = Options()
        OptionBuilder.hasOptionalArg()

    def test11456_test10_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")
        options = Options()

    def test11456_test9_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)
        self.assertEqual(cmd.getOptionValue0("b"), "value")

    def test11456_test8_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()
        cmd = parser.parse0(options, args)

    def test11456_test7_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))
        args = ["-a", "-bvalue"]
        parser = PosixParser()

    def test11456_test6_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")
        options.addOption0(OptionBuilder.hasArg0().create1("b"))

    def test11456_test5_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()
        OptionBuilder.hasArg0().create1("b")

    def test11456_test4_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))
        OptionBuilder.hasArg0()

    def test11456_test3_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")
        options.addOption0(OptionBuilder.hasOptionalArg().create1("a"))

    def test11456_test2_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()
        OptionBuilder.hasOptionalArg().create1("a")

    def test11456_test1_decomposed(self) -> None:
        options = Options()
        OptionBuilder.hasOptionalArg()

    def test11456_test0_decomposed(self) -> None:
        options = Options()
