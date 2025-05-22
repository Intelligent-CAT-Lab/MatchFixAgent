from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
from io import BytesIO
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.exec.CommandLine import *
from src.main.org.apache.commons.exec.DefaultExecutor import *
from src.main.org.apache.commons.exec.ExecuteStreamHandler import *
from src.main.org.apache.commons.exec.Executor import *
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.PumpStreamHandler import *
from src.test.org.apache.commons.exec.TestUtil import *


class Exec36Test(unittest.TestCase):

    __baos: typing.Union[io.BytesIO, bytearray] = None

    __testDir: pathlib.Path = pathlib.Path("src/test/scripts")

    __exec: Executor = None  # LLM could not translate this field

    __printArgsScript: pathlib.Path = None  # LLM could not translate this field

    def testExec36_2_test7_decomposed(self) -> None:
        # Determine the expected output based on the OS
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS: {os.name}"
            )
            return

        # Create the command line
        file = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map = {"FILE": file}
        cmdl = CommandLine(1, executable=self.__printArgsScript)
        cmdl.setSubstitutionMap(substitution_map)
        cmdl.addArgument1("dotnetfx.exe", False)
        cmdl.addArgument1("/q:a", False)
        cmdl.addArgument1('/c:"install.exe /l ""${FILE}"" /q"', False)

        # Execute the command
        exit_value = self.__exec.execute0(cmdl)
        result = self.__baos.getvalue().decode().strip()

        # Assertions
        self.assertFalse(self.__exec.isFailure(exit_value))
        if OS.isFamilyUnix():
            # The parameters fall apart literally under Windows - need to disable the check for Win32
            self.assertEqual(expected, result)

    def testExec36_2_test6_decomposed(self) -> None:
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS: {os.name}"
            )
            return

        file = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map = {"FILE": file}

        cmdl = CommandLine(1, executable=self.__printArgsScript)
        cmdl.setSubstitutionMap(substitution_map)
        cmdl.addArgument1("dotnetfx.exe", False)
        cmdl.addArgument1("/q:a", False)
        cmdl.addArgument1('/c:"install.exe /l ""${FILE}"" /q"', False)

        exit_value = self.__exec.execute0(cmdl)
        result = self.__baos.getvalue().decode().strip()

        self.assertFalse(self.__exec.isFailure(exit_value))

    def testExec36_2_test5_decomposed(self) -> None:
        expected: str
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS : {os.name}"
            )
            return

        file = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map: Dict[str, pathlib.Path] = {"FILE": file}

        cmdl = CommandLine(1, executable=self.__printArgsScript)
        cmdl.setSubstitutionMap(substitution_map)
        cmdl.addArgument1("dotnetfx.exe", False)
        cmdl.addArgument1("/q:a", False)
        cmdl.addArgument1('/c:"install.exe /l ""${FILE}"" /q"', False)

        exit_value: int = self.__exec.execute0(cmdl)
        result: str = self.__baos.getvalue().decode().strip()

    def testExec36_2_test4_decomposed(self) -> None:
        expected: str
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS: {os.name}"
            )
            return

        file = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map: Dict[str, pathlib.Path] = {"FILE": file}

        cmdl = CommandLine(1, executable=self.__printArgsScript)
        cmdl.setSubstitutionMap(substitution_map)
        cmdl.addArgument1("dotnetfx.exe", False)
        cmdl.addArgument1("/q:a", False)
        cmdl.addArgument1('/c:"install.exe /l ""${FILE}"" /q"', False)

        exit_value: int = self.__exec.execute0(cmdl)

    def testExec36_2_test3_decomposed(self) -> None:
        expected: str
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS: {os.name}"
            )
            return

        cmdl: CommandLine
        file: pathlib.Path = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map: Dict[str, pathlib.Path] = {"FILE": file}

        cmdl = CommandLine(1, None, self.__printArgsScript, None)
        cmdl.setSubstitutionMap(substitution_map)
        cmdl.addArgument1("dotnetfx.exe", False)
        cmdl.addArgument1("/q:a", False)
        cmdl.addArgument1('/c:"install.exe /l ""${FILE}"" /q"', False)

    def testExec36_2_test2_decomposed(self) -> None:
        expected: str
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS : {os.name}"
            )
            return

        cmdl: CommandLine
        file: pathlib.Path = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        substitution_map: Dict[str, pathlib.Path] = {"FILE": file}
        cmdl = CommandLine(1, executable=self.__printArgsScript)
        cmdl.setSubstitutionMap(substitution_map)

    def testExec36_2_test1_decomposed(self) -> None:
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_3' does not support the following OS : {os.name}"
            )
            return

        file = pathlib.Path(
            "/Documents and Settings/myusername/Local Settings/Temp/netfx.log"
        )
        map_ = {"FILE": file}
        cmdl = CommandLine(1, executable=self.__printArgsScript)

    def testExec36_2_test0_decomposed(self) -> None:
        expected: str
        if OS.isFamilyWindows():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
            )
        elif OS.isFamilyUnix():
            expected = (
                "dotnetfx.exe\n"
                "/q:a\n"
                '/c:"install.exe /l ""/Documents and Settings/myusername/Local Settings/Temp/netfx.log"" /q"'
            )
        else:
            print(
                f"The test 'testExec36_2_test0_decomposed' does not support the following OS : {os.name}"
            )
            return

    def testExec36_1_test0_decomposed(self) -> None:
        if OS.isFamilyUnix():
            # Define the expected output
            expected = (
                "./script/jrake\n"
                "cruise:publish_installers\n"
                "INSTALLER_VERSION=unstable_2_1\n"
                'INSTALLER_PATH="/var/lib/ cruise-agent/installers"\n'
                "INSTALLER_DOWNLOAD_SERVER='something'\n"
                "WITHOUT_HELP_DOC=true"
            )

            # Create the command line object
            cmdl = CommandLine(1, executable=self.__printArgsScript)
            cmdl.addArgument1("./script/jrake", False)
            cmdl.addArgument1("cruise:publish_installers", False)
            cmdl.addArgument1("INSTALLER_VERSION=unstable_2_1", False)
            cmdl.addArgument1(
                'INSTALLER_PATH="/var/lib/ cruise-agent/installers"', False
            )
            cmdl.addArgument1("INSTALLER_DOWNLOAD_SERVER='something'", False)
            cmdl.addArgument1("WITHOUT_HELP_DOC=true", False)

            # Execute the command
            exit_value = self.__exec.execute0(cmdl)
            result = self.__baos.getvalue().decode().strip()

            # Assertions
            self.assertFalse(self.__exec.isFailure(exit_value))
            self.assertEqual(expected, result)
        else:
            print(
                f"The test 'testExec36_1' does not support the following OS: {os.name}"
            )

    def tearDown(self) -> None:
        if self.__baos is not None:
            self.__baos.close()

    def setUp(self) -> None:
        # prepare a ready to Executor
        self.__baos = io.BytesIO()
        self.__exec.setStreamHandler(
            PumpStreamHandler.PumpStreamHandler2(self.__baos, self.__baos)
        )

    def test_testExec36_6(self) -> None:
        commandline = r"C:\CVS_DB\WeightsEngine /f WeightsEngine.mak CFG=\"WeightsEngine - Win32Release\""

        cmdl = CommandLine.parse0(commandline)
        args = cmdl.getArguments()
        self.assertEqual("/f", args[0])
        self.assertEqual("WeightsEngine.mak", args[1])
        self.assertEqual('CFG="WeightsEngine - Win32Release"', args[2])

    def test_testExec36_5(self) -> None:
        line = (
            "dotnetfx.exe"
            + " /q:a "
            + '/c:"install.exe /l ""c:\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"'
        )

        cmdl = CommandLine.parse0(line)
        args = cmdl.toStrings()
        self.assertEqual("dotnetfx.exe", args[0])
        self.assertEqual("/q:a", args[1])
        self.assertEqual(
            '/c:"install.exe /l ""c:\\Documents and Settings\\myusername\\Local Settings\\Temp\\netfx.log"" /q"',
            args[2],
        )

    def test_testExec36_4(self) -> None:
        line = (
            "./script/jrake "
            + "cruise:publish_installers "
            + "INSTALLER_VERSION=unstable_2_1 "
            + 'INSTALLER_PATH="/var/lib/cruise-agent/installers" '
            + "INSTALLER_DOWNLOAD_SERVER='something'"
            + "WITHOUT_HELP_DOC=true"
        )

        cmdl = CommandLine.parse0(line)
        args = cmdl.toStrings()

        self.assertEqual("./script/jrake", args[0])
        self.assertEqual("cruise:publish_installers", args[1])
        self.assertEqual("INSTALLER_VERSION=unstable_2_1", args[2])
        self.assertEqual('INSTALLER_PATH="/var/lib/cruise-agent/installers"', args[3])
        self.assertEqual("INSTALLER_DOWNLOAD_SERVER='something'", args[4])
        self.assertEqual("WITHOUT_HELP_DOC=true", args[5])
