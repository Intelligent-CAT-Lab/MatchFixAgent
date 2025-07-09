from __future__ import annotations
import copy
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.exec.environment.EnvironmentUtils import *
from src.main.org.apache.commons.exec.util.MapUtils import *


class MapUtilTest(unittest.TestCase):

    def testPrefixMap_test2_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.prefix(proc_environment, "env")
        self.assertEqual(len(proc_environment), len(result))
        self.assertEqual("/usr/opt/java", result.get("env.JAVA_HOME"))

    def testPrefixMap_test1_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.prefix(proc_environment, "env")
        self.assertEqual(len(proc_environment), len(result))

    def testPrefixMap_test0_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.prefix(proc_environment, "env")
        # You can add assertions here if needed, e.g.:
        # self.assertEqual(result, {"env.JAVA_HOME": "/usr/opt/java"})

    def testMergeMap_test3_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        application_environment = {"appMainClass": "foo.bar.Main"}
        result = MapUtils.merge(proc_environment, application_environment)

        self.assertEqual(
            len(proc_environment) + len(application_environment), len(result)
        )
        self.assertEqual("foo.bar.Main", result.get("appMainClass"))

    def testMergeMap_test2_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        application_environment = {"appMainClass": "foo.bar.Main"}
        result = MapUtils.merge(proc_environment, application_environment)
        self.assertEqual(
            len(proc_environment) + len(application_environment), len(result)
        )

    def testMergeMap_test1_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()
        application_environment = {"appMainClass": "foo.bar.Main"}
        result = MapUtils.merge(proc_environment, application_environment)

    def testMergeMap_test0_decomposed(self) -> None:
        proc_environment = EnvironmentUtils.getProcEnvironment()

    def testCopyMap_test5_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)

        self.assertEqual(1, len(result))
        self.assertEqual(1, len(proc_environment))
        self.assertEqual("/usr/opt/java", result.get("JAVA_HOME"))

        result.pop("JAVA_HOME")
        self.assertTrue(len(result) == 0)
        self.assertEqual(1, len(proc_environment))

    def testCopyMap_test4_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)
        self.assertEqual(1, len(result))
        self.assertEqual(1, len(proc_environment))
        self.assertEqual("/usr/opt/java", result.get("JAVA_HOME"))
        result.pop("JAVA_HOME")
        self.assertTrue(len(result) == 0)

    def testCopyMap_test3_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)
        self.assertEqual(1, len(result))
        self.assertEqual(1, len(proc_environment))
        self.assertEqual("/usr/opt/java", result.get("JAVA_HOME"))
        result.pop("JAVA_HOME")

    def testCopyMap_test2_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)
        self.assertEqual(1, len(result))
        self.assertEqual(1, len(proc_environment))
        self.assertEqual("/usr/opt/java", result.get("JAVA_HOME"))

    def testCopyMap_test1_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)
        self.assertEqual(1, len(result))
        self.assertEqual(1, len(proc_environment))

    def testCopyMap_test0_decomposed(self) -> None:
        proc_environment = {"JAVA_HOME": "/usr/opt/java"}
        result = MapUtils.copy(proc_environment)
        self.assertEqual(result, proc_environment)
