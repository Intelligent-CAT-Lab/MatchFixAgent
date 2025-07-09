from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.util.StringUtils import *


class CommandLineTest(unittest.TestCase):

    def testToStringTroubleshooting_test3_decomposed(self) -> None:
        print("testToStringTroubleshooting")
        CommandLine(2, None, None, "sh").addArgument0("-c")
        cmd1 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("echo 1", False)
        )
        cmd2 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument0("echo")
            .addArgument0("1")
        )
        print("cmd1: " + cmd1.toString())
        print("cmd2: " + cmd2.toString())
        self.assertTrue(
            cmd1.toString() != cmd2.toString(),
            "toString() is useful for troubleshooting",
        )

    def testToStringTroubleshooting_test2_decomposed(self) -> None:
        print("testToStringTroubleshooting")
        CommandLine(2, None, None, "sh").addArgument0("-c")
        cmd1 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("echo 1", False)
        )
        cmd2 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument0("echo")
            .addArgument0("1")
        )

    def testToStringTroubleshooting_test1_decomposed(self) -> None:
        print("testToStringTroubleshooting")
        CommandLine(2, None, None, "sh").addArgument0("-c")
        cmd1 = (
            CommandLine(2, None, None, "sh")
            .addArgument0("-c")
            .addArgument1("echo 1", False)
        )

    def testToStringTroubleshooting_test0_decomposed(self) -> None:
        print("testToStringTroubleshooting")
        CommandLine(2, None, None, "sh").addArgument0("-c")

    def testToString_test5_decomposed(self) -> None:
        cmdl = None
        params = {}

        # Test case 1
        cmdl = CommandLine.parse1("AcroRd32.exe", params)
        self.assertEqual("[AcroRd32.exe]", cmdl.toString())

        # Test case 2
        params["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)
        self.assertEqual(
            '[AcroRd32.exe, /p, /h, "C:\\Document And Settings\\documents\\432432.pdf"]',
            cmdl.toString(),
        )

        # Test case 3
        params["file"] = "C:\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)
        self.assertEqual(
            "[AcroRd32.exe, /p, /h, C:\\documents\\432432.pdf]", cmdl.toString()
        )

    def testToString_test4_decomposed(self) -> None:
        cmdl: CommandLine
        params: dict[str, str] = {}

        # First test case
        cmdl = CommandLine.parse1("AcroRd32.exe", params)
        self.assertEqual("[AcroRd32.exe]", cmdl.toString())

        # Second test case
        params["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)
        self.assertEqual(
            '[AcroRd32.exe, /p, /h, "C:\\Document And Settings\\documents\\432432.pdf"]',
            cmdl.toString(),
        )

        # Third test case
        params["file"] = "C:\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)

    def testToString_test3_decomposed(self) -> None:
        cmdl = None
        params = {}

        # First test case
        cmdl = CommandLine.parse1("AcroRd32.exe", params)
        self.assertEqual("[AcroRd32.exe]", cmdl.toString())

        # Second test case
        params["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)
        self.assertEqual(
            '[AcroRd32.exe, /p, /h, "C:\\Document And Settings\\documents\\432432.pdf"]',
            cmdl.toString(),
        )

    def testToString_test2_decomposed(self) -> None:
        cmdl = None
        params = {}
        cmdl = CommandLine.parse1("AcroRd32.exe", params)
        self.assertEqual("[AcroRd32.exe]", cmdl.toString())
        params["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params)

    def testToString_test1_decomposed(self) -> None:
        params = {}
        cmdl = CommandLine.parse1("AcroRd32.exe", params)
        self.assertEqual("[AcroRd32.exe]", cmdl.toString())

    def testToString_test0_decomposed(self) -> None:
        cmdl: CommandLine
        params: dict[str, str] = {}
        cmdl = CommandLine.parse1("AcroRd32.exe", params)

    def testParseRealLifeCommandLine_1_test2_decomposed(self) -> None:
        commandline = (
            'cmd.exe /C "c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat"'
        )
        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()
        self.assertEqual("/C", args[0])
        self.assertEqual(
            '"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat"', args[1]
        )

    def testParseRealLifeCommandLine_1_test1_decomposed(self) -> None:
        commandline = r'cmd.exe /C "c:\was51\Web Sphere\AppServer\bin\versionInfo.bat"'
        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()

    def testParseRealLifeCommandLine_1_test0_decomposed(self) -> None:
        commandline = (
            r'cmd.exe /C "c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat"'
        )
        cmdl = CommandLine.parse0(commandline)

    def testParseComplexCommandLine2_test3_decomposed(self) -> None:
        commandline = (
            "./script/jrake cruise:publish_installers "
            + "INSTALLER_VERSION=unstable_2_1 "
            + 'INSTALLER_PATH="/var/lib/ cruise-agent/installers" '
            + "INSTALLER_DOWNLOAD_SERVER='something' "
            + "WITHOUT_HELP_DOC=true"
        )
        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()
        self.assertEqual(args[0], "cruise:publish_installers")
        self.assertEqual(args[1], "INSTALLER_VERSION=unstable_2_1")
        self.assertEqual(args[4], "WITHOUT_HELP_DOC=true")

    def testParseComplexCommandLine2_test2_decomposed(self) -> None:
        commandline = (
            "./script/jrake cruise:publish_installers "
            + "INSTALLER_VERSION=unstable_2_1 "
            + 'INSTALLER_PATH="/var/lib/ cruise-agent/installers" '
            + "INSTALLER_DOWNLOAD_SERVER='something' "
            + "WITHOUT_HELP_DOC=true"
        )
        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()
        self.assertEqual(args[0], "cruise:publish_installers")
        self.assertEqual(args[1], "INSTALLER_VERSION=unstable_2_1")

    def testParseComplexCommandLine2_test1_decomposed(self) -> None:
        commandline = (
            "./script/jrake cruise:publish_installers "
            + "INSTALLER_VERSION=unstable_2_1 "
            + 'INSTALLER_PATH="/var/lib/ cruise-agent/installers" '
            + "INSTALLER_DOWNLOAD_SERVER='something' "
            + "WITHOUT_HELP_DOC=true"
        )
        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()

    def testParseComplexCommandLine2_test0_decomposed(self) -> None:
        commandline = (
            "./script/jrake cruise:publish_installers "
            + "INSTALLER_VERSION=unstable_2_1 "
            + 'INSTALLER_PATH="/var/lib/ cruise-agent/installers" '
            + "INSTALLER_DOWNLOAD_SERVER='something' "
            + "WITHOUT_HELP_DOC=true"
        )
        cmdl = CommandLine.parse0(commandline)

    def testParseComplexCommandLine1_test1_decomposed(self) -> None:
        substitution_map = {"in": "source.jpg", "out": "target.jpg"}
        cmdl = CommandLine.parse1(
            "cmd /C convert ${in} -resize \"'500x> '\" ${out}", substitution_map
        )
        self.assertEqual(
            '[cmd, /C, convert, source.jpg, -resize, "500x> ", target.jpg]',
            cmdl.toString(),
        )

    def testParseComplexCommandLine1_test0_decomposed(self) -> None:
        substitution_map = {"in": "source.jpg", "out": "target.jpg"}
        cmdl = CommandLine.parse1(
            "cmd /C convert ${in} -resize \"'500x> '\" ${out}", substitution_map
        )

    def testParseCommandLineWithUnevenQuotes_test0_decomposed(self) -> None:
        with self.assertRaises(
            ValueError, msg="ValueError must be thrown due to uneven quotes"
        ):
            CommandLine.parse0('test "foo bar')

    def testParseCommandLineWithQuotes_test2_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test \"foo\" 'ba r'")
        self.assertEqual('[test, foo, "ba r"]', cmdl.toString())
        self.assertEqual(["test", "foo", '"ba r"'], cmdl.toStrings())

    def testParseCommandLineWithQuotes_test1_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test \"foo\" 'ba r'")
        self.assertEqual('[test, foo, "ba r"]', cmdl.toString())

    def testParseCommandLineWithQuotes_test0_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test \"foo\" 'ba r'")

    def testParseCommandLineWithOnlyWhitespace_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            CommandLine.parse0("  ")

    def testParseCommandLineWithNull_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            CommandLine.parse0(None)

    def testParseCommandLine_test2_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test foo bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())
        self.assertEqual(["test", "foo", "bar"], cmdl.toStrings())

    def testParseCommandLine_test1_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test foo bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())

    def testParseCommandLine_test0_decomposed(self) -> None:
        cmdl = CommandLine.parse0("test foo bar")

    def testNullExecutable_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommandLine(2, None, None, None)

    def testExecutableZeroLengthString_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            CommandLine(2, None, None, "")

    def testExecutableWhitespaceString_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            CommandLine(2, None, None, "   ")

    def testExecutable_test4_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        self.assertEqual("[test]", cmdl.toString())
        self.assertEqual(["test"], cmdl.toStrings())
        self.assertEqual("test", cmdl.getExecutable())
        self.assertTrue(len(cmdl.getArguments()) == 0)

    def testExecutable_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        self.assertEqual("[test]", cmdl.toString())
        self.assertEqual(["test"], cmdl.toStrings())
        self.assertEqual("test", cmdl.getExecutable())

    def testExecutable_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        self.assertEqual("[test]", cmdl.toString())
        self.assertListEqual(["test"], cmdl.toStrings())

    def testExecutable_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        self.assertEqual("[test]", cmdl.toString())

    def testExecutable_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testCopyConstructor_test7_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)
        cmdl = CommandLine(0, other, None, None)

        self.assertEqual(other.getExecutable(), cmdl.getExecutable())
        self.assertEqual(other.getArguments(), cmdl.getArguments())
        self.assertEqual(other.isFile(), cmdl.isFile())
        self.assertEqual(other.getSubstitutionMap(), cmdl.getSubstitutionMap())

    def testCopyConstructor_test6_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)
        cmdl = CommandLine(0, other, None, None)

        self.assertEqual(other.getExecutable(), cmdl.getExecutable())
        self.assertEqual(other.getArguments(), cmdl.getArguments())
        self.assertEqual(other.isFile(), cmdl.isFile())

    def testCopyConstructor_test5_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)
        cmdl = CommandLine(0, other, None, None)
        self.assertEqual(other.getExecutable(), cmdl.getExecutable())
        self.assertEqual(other.getArguments(), cmdl.getArguments())

    def testCopyConstructor_test4_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)
        cmdl = CommandLine(0, other, None, None)
        self.assertEqual(other.getExecutable(), cmdl.getExecutable())

    def testCopyConstructor_test3_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)
        cmdl = CommandLine(0, other, None, None)

    def testCopyConstructor_test2_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")
        other.setSubstitutionMap(map)

    def testCopyConstructor_test1_decomposed(self) -> None:
        map: dict[str, str] = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")
        other.addArgument0("foo")

    def testCopyConstructor_test0_decomposed(self) -> None:
        map = {"bar": "bar"}
        other = CommandLine(2, None, None, "test")

    def testComplexAddArguments2_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")
        cmdl.addArguments1(
            "10 30 -XX:+UseParallelGC '\"-XX:ParallelGCThreads=2\"'", False
        )
        self.assertEqual(
            [
                "runMemorySud.cmd",
                "10",
                "30",
                "-XX:+UseParallelGC",
                '"-XX:ParallelGCThreads=2"',
            ],
            cmdl.toStrings(),
        )

    def testComplexAddArguments2_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, executableString="runMemorySud.cmd")
        cmdl.addArguments1(
            "10 30 -XX:+UseParallelGC '\"-XX:ParallelGCThreads=2\"'", False
        )

    def testComplexAddArguments2_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")

    def testComplexAddArguments1_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")
        cmdl.addArguments3(
            ["10", "30", "-XX:+UseParallelGC", '"-XX:ParallelGCThreads=2"'], False
        )
        self.assertEqual(
            [
                "runMemorySud.cmd",
                "10",
                "30",
                "-XX:+UseParallelGC",
                '"-XX:ParallelGCThreads=2"',
            ],
            cmdl.toStrings(),
        )

    def testComplexAddArguments1_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")
        cmdl.addArguments3(
            ["10", "30", "-XX:+UseParallelGC", '"-XX:ParallelGCThreads=2"'], False
        )

    def testComplexAddArguments1_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")

    def testComplexAddArgument_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")
        cmdl.addArgument1("10", False)
        cmdl.addArgument1("30", False)
        cmdl.addArgument1("-XX:+UseParallelGC", False)
        cmdl.addArgument1('"-XX:ParallelGCThreads=2"', False)
        self.assertEqual(
            [
                "runMemorySud.cmd",
                "10",
                "30",
                "-XX:+UseParallelGC",
                '"-XX:ParallelGCThreads=2"',
            ],
            cmdl.toStrings(),
        )

    def testComplexAddArgument_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")
        cmdl.addArgument1("10", False)
        cmdl.addArgument1("30", False)
        cmdl.addArgument1("-XX:+UseParallelGC", False)
        cmdl.addArgument1('"-XX:ParallelGCThreads=2"', False)

    def testComplexAddArgument_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "runMemorySud.cmd")

    def testCommandLineParsingWithExpansion3_test6_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")
        cmdl.addArgument1("${file}", False)

        params = {"file": "C:\\Document And Settings\\documents\\432432.pdf"}
        cmdl.setSubstitutionMap(params)

        result = cmdl.toStrings()

        self.assertEqual("AcroRd32.exe", result[0])
        self.assertEqual("/p", result[1])
        self.assertEqual("/h", result[2])
        self.assertEqual("C:\\Document And Settings\\documents\\432432.pdf", result[3])

    def testCommandLineParsingWithExpansion3_test5_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")
        cmdl.addArgument1("${file}", False)

        params = {"file": "C:\\Document And Settings\\documents\\432432.pdf"}
        cmdl.setSubstitutionMap(params)

        result = cmdl.toStrings()
        self.assertEqual("AcroRd32.exe", result[0])
        self.assertEqual("/p", result[1])

    def testCommandLineParsingWithExpansion3_test4_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")
        cmdl.addArgument1("${file}", False)
        params = {"file": "C:\\Document And Settings\\documents\\432432.pdf"}
        cmdl.setSubstitutionMap(params)
        result = cmdl.toStrings()

    def testCommandLineParsingWithExpansion3_test3_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")
        cmdl.addArgument1("${file}", False)
        params = {"file": "C:\\Document And Settings\\documents\\432432.pdf"}
        cmdl.setSubstitutionMap(params)

    def testCommandLineParsingWithExpansion3_test2_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")
        cmdl.addArgument1("${file}", False)

    def testCommandLineParsingWithExpansion3_test1_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")
        cmdl.addArgument0("/p")
        cmdl.addArgument0("/h")

    def testCommandLineParsingWithExpansion3_test0_decomposed(self) -> None:
        cmdl = CommandLine.parse0("AcroRd32.exe")

    def testCommandLineParsingWithExpansion2_test13_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )
        self.assertEqual("-class", arguments[0])
        self.assertEqual("foo.bar.Main", arguments[1])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', arguments[2]
        )

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432432.pdf"', result[3]
        )

    def testCommandLineParsingWithExpansion2_test12_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }

        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )
        self.assertEqual("-class", arguments[0])
        self.assertEqual("foo.bar.Main", arguments[1])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', arguments[2]
        )

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])

    def testCommandLineParsingWithExpansion2_test11_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )
        self.assertEqual("-class", arguments[0])
        self.assertEqual("foo.bar.Main", arguments[1])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', arguments[2]
        )

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )

    def testCommandLineParsingWithExpansion2_test10_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }

        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )
        self.assertEqual("-class", arguments[0])
        self.assertEqual("foo.bar.Main", arguments[1])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', arguments[2]
        )

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432432.pdf"
        result = cmdl.toStrings()

    def testCommandLineParsingWithExpansion2_test9_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }

        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )
        self.assertEqual("-class", arguments[0])
        self.assertEqual("foo.bar.Main", arguments[1])

    def testCommandLineParsingWithExpansion2_test8_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )
        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            executable,
        )

    def testCommandLineParsingWithExpansion2_test7_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)
        result = cmdl.toStrings()

        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )

        executable = cmdl.getExecutable()
        arguments = cmdl.getArguments()

    def testCommandLineParsingWithExpansion2_test6_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])
        self.assertEqual(
            '"C:\\Document And Settings\\documents\\432431.pdf"', result[3]
        )
        executable = cmdl.getExecutable()

    def testCommandLineParsingWithExpansion2_test5_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)
        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )
        self.assertEqual("-class", result[1])
        self.assertEqual("foo.bar.Main", result[2])

    def testCommandLineParsingWithExpansion2_test4_decomposed(self) -> None:
        cmdl: CommandLine
        result: List[str]
        substitution_map: Dict[str, str] = {}
        substitution_map["JAVA_HOME"] = "C:\\Programme\\jdk1.5.0_12"
        substitution_map["appMainClass"] = "foo.bar.Main"

        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")

        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

        result = cmdl.toStrings()
        self.assertEqual(
            StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"),
            result[0],
        )

    def testCommandLineParsingWithExpansion2_test3_decomposed(self) -> None:
        cmdl: CommandLine
        result: List[str]
        substitution_map: Dict[str, str] = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)
        result = cmdl.toStrings()

    def testCommandLineParsingWithExpansion2_test2_decomposed(self) -> None:
        cmdl: CommandLine
        result: list[str]
        substitution_map: dict[str, str] = {}
        substitution_map["JAVA_HOME"] = "C:\\Programme\\jdk1.5.0_12"
        substitution_map["appMainClass"] = "foo.bar.Main"
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")
        substitution_map["file"] = "C:\\Document And Settings\\documents\\432431.pdf"
        cmdl.setSubstitutionMap(substitution_map)

    def testCommandLineParsingWithExpansion2_test1_decomposed(self) -> None:
        substitution_map = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")
        cmdl.addArgument0("-class")
        cmdl.addArgument0("${appMainClass}")
        cmdl.addArgument0("${file}")

    def testCommandLineParsingWithExpansion2_test0_decomposed(self) -> None:
        cmdl: CommandLine
        result: list[str]
        substitution_map: dict[str, str] = {
            "JAVA_HOME": "C:\\Programme\\jdk1.5.0_12",
            "appMainClass": "foo.bar.Main",
        }
        cmdl = CommandLine(2, None, None, "${JAVA_HOME}\\bin\\java")

    def testCommandLineParsingWithExpansion1_test13_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

        # Test parse1 with incomplete substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", incomplete_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with multiple substitutions
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass} ${file1} ${file2}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().index("${file}") < 0)

    def testCommandLineParsingWithExpansion1_test12_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

        # Test parse1 with incomplete substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", incomplete_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with multiple arguments in substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass} ${file1} ${file2}", substitution_map
        )

    def testCommandLineParsingWithExpansion1_test11_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().find("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

        # Test parse1 with incomplete substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", incomplete_map
        )
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().find("local") > 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

    def testCommandLineParsingWithExpansion1_test10_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

        # Test parse1 with incomplete substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", incomplete_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)

    def testCommandLineParsingWithExpansion1_test9_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().find("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

        # Test parse1 with incomplete substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", incomplete_map
        )

    def testCommandLineParsingWithExpansion1_test8_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with an empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with a populated substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().index("local") > 0)
        self.assertEqual(["foo.bar.Main"], cmdl.getArguments())

    def testCommandLineParsingWithExpansion1_test7_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with an empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with a populated substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )
        self.assertTrue(cmdl.getExecutable().find("${JAVA_HOME}") < 0)
        self.assertTrue(cmdl.getExecutable().find("local") > 0)

    def testCommandLineParsingWithExpansion1_test6_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with empty substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1 with substitution map
        cmdl = CommandLine.parse1(
            "${JAVA_HOME}/bin/java ${appMainClass}", substitution_map
        )

    def testCommandLineParsingWithExpansion1_test5_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Test parse0
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().startswith("${JAVA_HOME}"))
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        # Test parse1
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().startswith("${JAVA_HOME}"))
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

    def testCommandLineParsingWithExpansion1_test4_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)

    def testCommandLineParsingWithExpansion1_test3_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map: dict[str, object] = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }
        incomplete_map: dict[str, str] = {"JAVA_HOME": "/usr/local/java"}

        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", {})

    def testCommandLineParsingWithExpansion1_test2_decomposed(self) -> None:
        # Create substitution map
        substitution_map = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": "./pom.xml",
            "file2": ".\\temp\\READ ME.txt",
        }

        # Create incomplete map
        incomplete_map = {"JAVA_HOME": "/usr/local/java"}

        # Parse the command line
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")

        # Assert that the executable starts with "${JAVA_HOME}"
        self.assertTrue(cmdl.getExecutable().startswith("${JAVA_HOME}"))

        # Assert that the arguments match the expected array
        self.assertEqual(["${appMainClass}"], cmdl.getArguments())

    def testCommandLineParsingWithExpansion1_test1_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map: dict[str, object] = {
            "JAVA_HOME": "/usr/local/java",
            "appMainClass": "foo.bar.Main",
            "file1": File("./pom.xml"),
            "file2": File(".\\temp\\READ ME.txt"),
        }
        incomplete_map: dict[str, str] = {
            "JAVA_HOME": "/usr/local/java",
        }
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")
        self.assertTrue(cmdl.getExecutable().index("${JAVA_HOME}") == 0)

    def testCommandLineParsingWithExpansion1_test0_decomposed(self) -> None:
        cmdl: CommandLine
        substitution_map: dict[str, object] = {}
        substitution_map["JAVA_HOME"] = "/usr/local/java"
        substitution_map["appMainClass"] = "foo.bar.Main"
        substitution_map["file1"] = File("./pom.xml")
        substitution_map["file2"] = File(".\\temp\\READ ME.txt")

        incomplete_map: dict[str, str] = {}
        incomplete_map["JAVA_HOME"] = "/usr/local/java"

        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}")

    def testAddTwoArguments_test4_decomposed(self) -> None:
        userAddCL1 = CommandLine(2, None, None, "useradd")
        userAddCL1.addArgument0("-g")
        userAddCL1.addArgument0("tomcat")
        userAddCL1.addArgument0("foo")

        userAddCL2 = CommandLine(2, None, None, "useradd")
        userAddCL2.addArgument0("-g").addArgument0("tomcat")
        userAddCL2.addArgument0("foo")

        self.assertEqual(userAddCL1.toString(), userAddCL2.toString())

    def testAddTwoArguments_test3_decomposed(self) -> None:
        userAddCL1 = CommandLine(2, None, None, "useradd")
        userAddCL1.addArgument0("-g")
        userAddCL1.addArgument0("tomcat")
        userAddCL1.addArgument0("foo")

        userAddCL2 = CommandLine(2, None, None, "useradd")
        userAddCL2.addArgument0("-g").addArgument0("tomcat")
        userAddCL2.addArgument0("foo")

    def testAddTwoArguments_test2_decomposed(self) -> None:
        userAddCL1 = CommandLine(2, None, None, "useradd")
        userAddCL1.addArgument0("-g")
        userAddCL1.addArgument0("tomcat")
        userAddCL1.addArgument0("foo")
        userAddCL2 = CommandLine(2, None, None, "useradd")

    def testAddTwoArguments_test1_decomposed(self) -> None:
        userAddCL1 = CommandLine(2, None, None, "useradd")
        userAddCL1.addArgument0("-g")
        userAddCL1.addArgument0("tomcat")
        userAddCL1.addArgument0("foo")

    def testAddTwoArguments_test0_decomposed(self) -> None:
        user_add_cl1 = CommandLine(2, None, None, "useradd")

    def testAddNullArgument_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0(None)
        self.assertEqual("[test]", cmdl.toString())
        self.assertEqual(["test"], cmdl.toStrings())

    def testAddNullArgument_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0(None)
        self.assertEqual("[test]", cmdl.toString())

    def testAddNullArgument_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, executableString="test")
        cmdl.addArgument0(None)

    def testAddNullArgument_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentWithSpace_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba r")
        self.assertEqual('[test, foo, "ba r"]', cmdl.toString())
        self.assertEqual(["test", "foo", '"ba r"'], cmdl.toStrings())

    def testAddArgumentWithSpace_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba r")
        self.assertEqual('[test, foo, "ba r"]', cmdl.toString())

    def testAddArgumentWithSpace_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba r")

    def testAddArgumentWithSpace_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentWithSingleQuote_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba'r")
        self.assertEqual('[test, foo, "ba\'r"]', cmdl.toString())
        self.assertEqual(["test", "foo", '"ba\'r"'], cmdl.toStrings())

    def testAddArgumentWithSingleQuote_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba'r")
        self.assertEqual('[test, foo, "ba\'r"]', cmdl.toString())

    def testAddArgumentWithSingleQuote_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("ba'r")

    def testAddArgumentWithSingleQuote_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentWithQuotesAround_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("'foo'")
        cmdl.addArgument0('"bar"')
        cmdl.addArgument0('"fe z"')
        self.assertEqual('[test, foo, bar, "fe z"]', cmdl.toString())
        self.assertEqual(["test", "foo", "bar", '"fe z"'], cmdl.toStrings())

    def testAddArgumentWithQuotesAround_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("'foo'")
        cmdl.addArgument0('"bar"')
        cmdl.addArgument0('"fe z"')
        self.assertEqual('[test, foo, bar, "fe z"]', cmdl.toString())

    def testAddArgumentWithQuotesAround_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("'foo'")
        cmdl.addArgument0('"bar"')
        cmdl.addArgument0('"fe z"')

    def testAddArgumentWithQuotesAround_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentWithQuote_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0('ba"r')
        self.assertEqual("[test, foo, 'ba\"r']", cmdl.toString())
        self.assertListEqual(["test", "foo", "'ba\"r'"], cmdl.toStrings())

    def testAddArgumentWithQuote_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0('ba"r')
        self.assertEqual("[test, foo, 'ba\"r']", cmdl.toString())

    def testAddArgumentWithQuote_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0('ba"r')

    def testAddArgumentWithQuote_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentWithBothQuotes_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        with self.assertRaises(ValueError):
            cmdl.addArgument0("b\"a'r")

    def testAddArgumentWithBothQuotes_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentsWithQuotesAndSpaces_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'fo o' \"ba r\"")
        self.assertEqual('[test, "fo o", "ba r"]', cmdl.toString())
        self.assertEqual(["test", '"fo o"', '"ba r"'], cmdl.toStrings())

    def testAddArgumentsWithQuotesAndSpaces_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'fo o' \"ba r\"")
        self.assertEqual('[test, "fo o", "ba r"]', cmdl.toString())

    def testAddArgumentsWithQuotesAndSpaces_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'fo o' \"ba r\"")

    def testAddArgumentsWithQuotesAndSpaces_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentsWithQuotes_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'foo' \"bar\"")
        self.assertEqual("[test, foo, bar]", cmdl.toString())
        self.assertEqual(["test", "foo", "bar"], cmdl.toStrings())

    def testAddArgumentsWithQuotes_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'foo' \"bar\"")
        self.assertEqual("[test, foo, bar]", cmdl.toString())

    def testAddArgumentsWithQuotes_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("'foo' \"bar\"")

    def testAddArgumentsWithQuotes_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentsArrayNull_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(None)
        self.assertEqual("[test]", cmdl.toString())
        self.assertEqual(["test"], cmdl.toStrings())

    def testAddArgumentsArrayNull_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(None)
        self.assertEqual("[test]", cmdl.toString())

    def testAddArgumentsArrayNull_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(None)

    def testAddArgumentsArrayNull_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgumentsArray_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(["foo", "bar"])
        self.assertEqual("[test, foo, bar]", cmdl.toString())
        self.assertEqual(["test", "foo", "bar"], cmdl.toStrings())

    def testAddArgumentsArray_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(["foo", "bar"])
        self.assertEqual("[test, foo, bar]", cmdl.toString())

    def testAddArgumentsArray_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments2(["foo", "bar"])

    def testAddArgumentsArray_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArguments_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("foo bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())
        self.assertEqual(["test", "foo", "bar"], cmdl.toStrings())

    def testAddArguments_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("foo bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())

    def testAddArguments_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArguments0("foo bar")

    def testAddArguments_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")

    def testAddArgument_test3_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())
        self.assertEqual(["test", "foo", "bar"], cmdl.toStrings())

    def testAddArgument_test2_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("bar")
        self.assertEqual("[test, foo, bar]", cmdl.toString())

    def testAddArgument_test1_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
        cmdl.addArgument0("foo")
        cmdl.addArgument0("bar")

    def testAddArgument_test0_decomposed(self) -> None:
        cmdl = CommandLine(2, None, None, "test")
