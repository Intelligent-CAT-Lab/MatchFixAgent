from __future__ import annotations
import re
import enum
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.exec.OS import *
from src.main.org.apache.commons.exec.environment.EnvironmentUtils import *


class EnvironmentUtilsTest(unittest.TestCase):

    def testToStringWithNullValue_test1_decomposed(self) -> None:
        env = {"key": None}
        strings = EnvironmentUtils.toStrings(env)
        self.assertEqual(1, len(strings))
        self.assertEqual("key=", strings[0])

    def testToStringWithNullValue_test0_decomposed(self) -> None:
        env = {"key": None}
        strings = EnvironmentUtils.toStrings(env)

    def testToStringWithNullKey_test1_decomposed(self) -> None:
        env = {None: "TheNullKey"}  # Create a dictionary with a null key
        strings = EnvironmentUtils.toStrings(env)  # Call the toStrings method
        self.assertEqual(
            1, len(strings)
        )  # Assert that the length of the strings list is 1
        self.assertEqual(
            "=TheNullKey", strings[0]
        )  # Assert that the first string is "=TheNullKey"

    def testToStringWithNullKey_test0_decomposed(self) -> None:
        env = {None: "TheNullKey"}
        strings = EnvironmentUtils.toStrings(env)
        # Add assertions if needed, depending on the expected behavior

    def testToStrings_test3_decomposed(self) -> None:
        self.assertIsNone(EnvironmentUtils.toStrings(None))

        env = {}
        self.assertEqual([], EnvironmentUtils.toStrings(env))

        env["foo2"] = "bar2"
        env["foo"] = "bar"

        envStrings = EnvironmentUtils.toStrings(env)
        expected = ["foo2=bar2", "foo=bar"]

        expected.sort()
        envStrings.sort()

        self.assertEqual(expected, envStrings)

    def testToStrings_test2_decomposed(self) -> None:
        self.assertIsNone(EnvironmentUtils.toStrings(None))

        env = {}
        self.assertEqual([], EnvironmentUtils.toStrings(env))

        env["foo2"] = "bar2"
        env["foo"] = "bar"
        envStrings = EnvironmentUtils.toStrings(env)
        self.assertEqual(["foo2=bar2", "foo=bar"], envStrings)

    def testToStrings_test1_decomposed(self) -> None:
        self.assertIsNone(EnvironmentUtils.toStrings(None))
        env = {}
        self.assertEqual([], EnvironmentUtils.toStrings(env))

    def testToStrings_test0_decomposed(self) -> None:
        self.assertIsNone(EnvironmentUtils.toStrings(None))

    def testGetProcEnvironmentCaseInsensitiveLookup_test4_decomposed(self) -> None:
        if not OS.isFamilyWindows():
            return

        proc_environment = EnvironmentUtils.getProcEnvironment()
        for key, value in proc_environment.items():
            self.assertEqual(value, proc_environment.get(key.lower()))
            self.assertEqual(value, proc_environment.get(key.upper()))

        EnvironmentUtils.addVariableToEnvironment(proc_environment, "foo=bar")
        self.assertEqual("bar", proc_environment.get("FOO"))
        self.assertEqual("bar", proc_environment.get("Foo"))
        self.assertEqual("bar", proc_environment.get("foo"))

    def testGetProcEnvironmentCaseInsensitiveLookup_test3_decomposed(self) -> None:
        if not OS.isFamilyWindows():
            return

        proc_environment = EnvironmentUtils.getProcEnvironment()
        for key, value in proc_environment.items():
            self.assertEqual(value, proc_environment.get(key.lower()))
            self.assertEqual(value, proc_environment.get(key.upper()))

        EnvironmentUtils.addVariableToEnvironment(proc_environment, "foo=bar")

    def testGetProcEnvironmentCaseInsensitiveLookup_test2_decomposed(self) -> None:
        if not OS.isFamilyWindows():
            return

        proc_environment = EnvironmentUtils.getProcEnvironment()
        for key, value in proc_environment.items():
            self.assertEqual(value, proc_environment.get(key.lower()))
            self.assertEqual(value, proc_environment.get(key.upper()))

    def testGetProcEnvironmentCaseInsensitiveLookup_test1_decomposed(self) -> None:
        if not OS.isFamilyWindows():
            return
        proc_environment = EnvironmentUtils.getProcEnvironment()

    def testGetProcEnvironmentCaseInsensitiveLookup_test0_decomposed(self) -> None:
        if not OS.isFamilyWindows():
            return

    def testGetProcEnvironment_test3_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        self.assertFalse(
            len(proc_environment) == 0, "Expecting non-zero environment size"
        )

        env_args = EnvironmentUtils.toStrings(proc_environment)
        for i, entry in enumerate(env_args):
            self.assertIsNotNone(entry, f"Entry {i} should not be null")
            self.assertFalse(entry == "", f"Entry {i} should not be empty")
            # print(entry)  # Uncomment this line if you want to print the entries for debugging

    def testGetProcEnvironment_test2_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        self.assertFalse(not proc_environment, "Expecting non-zero environment size")
        env_args = EnvironmentUtils.toStrings(proc_environment)

    def testGetProcEnvironment_test1_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        self.assertFalse(
            len(proc_environment) == 0, "Expecting non-zero environment size"
        )

    def testGetProcEnvironment_test0_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()

    def testCaseInsensitiveVariableLookup_test2_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        EnvironmentUtils.addVariableToEnvironment(proc_environment, "foo=bAr")
        self.assertEqual("bAr", proc_environment.get("foo"))

    def testCaseInsensitiveVariableLookup_test1_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        EnvironmentUtils.addVariableToEnvironment(proc_environment, "foo=bAr")

    def testCaseInsensitiveVariableLookup_test0_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
