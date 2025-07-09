from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.exec.util.StringUtils import *


class StringUtilTest(unittest.TestCase):

    def testNoStringSubstitution_test1_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}
        result = StringUtils.stringSubstitution("This is a FOO & BAR test", vars_, True)
        self.assertEqual("This is a FOO & BAR test", result.getvalue())

    def testNoStringSubstitution_test0_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}
        result = StringUtils.stringSubstitution("This is a FOO & BAR test", vars_, True)
        self.assertEqual(result.getvalue(), "This is a FOO & BAR test")

    def testIncompleteSubstitution_test1_decomposed(self) -> None:
        vars_ = {"foo": "FOO"}

        # Test lenient substitution
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        ).getvalue()
        self.assertEqual("This is a FOO & ${bar} test", result)

        # Test strict substitution
        with pytest.raises(
            RuntimeError
        ):  # Assuming RuntimeError in Java maps to RuntimeError in Python
            StringUtils.stringSubstitution(
                "This is a ${foo} & ${bar} test", vars_, False
            ).getvalue()

    def testIncompleteSubstitution_test0_decomposed(self) -> None:
        vars_ = {"foo": "FOO"}
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        )
        self.assertEqual(result.getvalue(), "This is a FOO & ${bar} test")

    def testErroneousTemplate_test1_decomposed(self) -> None:
        vars_ = {"foo": "FOO"}
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${}} test", vars_, True
        )
        self.assertEqual("This is a FOO & ${}} test", result.getvalue())

    def testErroneousTemplate_test0_decomposed(self) -> None:
        vars_ = {"foo": "FOO"}
        with self.assertRaises(ValueError):
            StringUtils.stringSubstitution("This is a ${foo} & ${}} test", vars_, False)

    def testDefaultStringSubstitution_test3_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}

        # Test with isLenient=True
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        ).getvalue()
        self.assertEqual("This is a FOO & BAR test", result)

        # Test with isLenient=False
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, False
        ).getvalue()
        self.assertEqual("This is a FOO & BAR test", result)

    def testDefaultStringSubstitution_test2_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        ).getvalue()
        self.assertEqual("This is a FOO & BAR test", result)
        StringUtils.stringSubstitution("This is a ${foo} & ${bar} test", vars_, False)

    def testDefaultStringSubstitution_test1_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        ).getvalue()
        self.assertEqual("This is a FOO & BAR test", result)

    def testDefaultStringSubstitution_test0_decomposed(self) -> None:
        vars_ = {"foo": "FOO", "bar": "BAR"}
        result = StringUtils.stringSubstitution(
            "This is a ${foo} & ${bar} test", vars_, True
        )
        self.assertEqual(result.getvalue(), "This is a FOO & BAR test")
