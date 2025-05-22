from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import numbers
import os
import unittest
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *


class OptionBuilderTest(unittest.TestCase):

    def testTwoCompleteOptions_test24_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(str, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertFalse(simple.isRequired())
        self.assertFalse(simple.hasArgs())

    def testTwoCompleteOptions_test23_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(str, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertFalse(simple.isRequired())

    def testTwoCompleteOptions_test22_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(str, simple.getType())
        self.assertTrue(simple.hasArg())

    def testTwoCompleteOptions_test21_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(str, simple.getType())

    def testTwoCompleteOptions_test20_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())

    def testTwoCompleteOptions_test19_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())

    def testTwoCompleteOptions_test18_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())

    def testTwoCompleteOptions_test17_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())
        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )

    def testTwoCompleteOptions_test16_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())
        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()
        OptionBuilder.withLongOpt("dimple option").hasArg0().withDescription(
            "this is a dimple option"
        )

    def testTwoCompleteOptions_test15_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())
        OptionBuilder.withLongOpt("dimple option")
        OptionBuilder.withLongOpt("dimple option").hasArg0()

    def testTwoCompleteOptions_test14_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())
        OptionBuilder.withLongOpt("dimple option")

    def testTwoCompleteOptions_test13_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

    def testTwoCompleteOptions_test12_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())

    def testTwoCompleteOptions_test11_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())

    def testTwoCompleteOptions_test10_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)

    def testTwoCompleteOptions_test9_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())

    def testTwoCompleteOptions_test8_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())

    def testTwoCompleteOptions_test7_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())

    def testTwoCompleteOptions_test6_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

    def testTwoCompleteOptions_test5_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

    def testTwoCompleteOptions_test4_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)

    def testTwoCompleteOptions_test3_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()

    def testTwoCompleteOptions_test2_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()

    def testTwoCompleteOptions_test1_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()

    def testTwoCompleteOptions_test0_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")

    def testSpecialOptChars_test6_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())

        OptionBuilder.withDescription("read from stdin")
        opt2 = OptionBuilder.withDescription("read from stdin").create1("@")
        self.assertEqual("@", opt2.getOpt())

        with pytest.raises(ValueError):
            OptionBuilder.create1(" ")

    def testSpecialOptChars_test5_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())

        OptionBuilder.withDescription("read from stdin")
        opt2 = OptionBuilder.withDescription("read from stdin").create1("@")
        self.assertEqual("@", opt2.getOpt())

    def testSpecialOptChars_test4_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())
        OptionBuilder.withDescription("read from stdin")
        opt2 = OptionBuilder.withDescription("read from stdin").create1("@")

    def testSpecialOptChars_test3_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())
        OptionBuilder.withDescription("read from stdin")

    def testSpecialOptChars_test2_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())

    def testSpecialOptChars_test1_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")
        opt1 = OptionBuilder.create1("?")

    def testSpecialOptChars_test0_decomposed(self) -> None:
        OptionBuilder.withDescription("help options")

    def testOptionArgNumbers_test3_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        OptionBuilder.withDescription("option description").hasArgs1(2)
        opt = (
            OptionBuilder.withDescription("option description").hasArgs1(2).create1("o")
        )
        self.assertEqual(2, opt.getArgs())

    def testOptionArgNumbers_test2_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        OptionBuilder.withDescription("option description").hasArgs1(2)
        opt = (
            OptionBuilder.withDescription("option description").hasArgs1(2).create1("o")
        )

    def testOptionArgNumbers_test1_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        OptionBuilder.withDescription("option description").hasArgs1(2)

    def testOptionArgNumbers_test0_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")

    def testIllegalOptions_test1_decomposed(self) -> None:
        with pytest.raises(ValueError):
            OptionBuilder.withDescription("option description").create1('"')

        with pytest.raises(ValueError):
            OptionBuilder.create2("opt`")

        try:
            OptionBuilder.create2("opt")
        except ValueError:
            pytest.fail("ValueError caught")

    def testIllegalOptions_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError, msg="ValueError not caught"):
            OptionBuilder.withDescription("option description").create1('"')

    def testCreateIncompleteOption_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError, msg="must specify longopt"):
            OptionBuilder.hasArg0().create0()

        # The following line should not execute if the exception is raised
        OptionBuilder.create2("opt")

    def testCompleteOption_test13_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

    def testCompleteOption_test12_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())

    def testCompleteOption_test11_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())
        self.assertTrue(simple.hasArg())

    def testCompleteOption_test10_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(float, simple.getType())

    def testCompleteOption_test9_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())

    def testCompleteOption_test8_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())

    def testCompleteOption_test7_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())

    def testCompleteOption_test6_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )
        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

    def testCompleteOption_test5_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float).withDescription(
            "this is a simple option"
        )

    def testCompleteOption_test4_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()
        OptionBuilder.withLongOpt(
            "simple option"
        ).hasArg0().isRequired0().hasArgs0().withType0(float)

    def testCompleteOption_test3_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0().hasArgs0()

    def testCompleteOption_test2_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()
        OptionBuilder.withLongOpt("simple option").hasArg0().isRequired0()

    def testCompleteOption_test1_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")
        OptionBuilder.withLongOpt("simple option").hasArg0()

    def testCompleteOption_test0_decomposed(self) -> None:
        OptionBuilder.withLongOpt("simple option")

    def testBuilderIsResettedAlways_test5_decomposed(self) -> None:
        # Test case 1: OptionBuilder.withDescription("JUnit").create1('"')
        with pytest.raises(ValueError, match="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create1('"')

        # Test case 2: OptionBuilder.create1('x')
        OptionBuilder.create1("x")
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )

        # Test case 3: OptionBuilder.withDescription("JUnit").create0()
        with pytest.raises(ValueError, match="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create0()

        # Test case 4: OptionBuilder.create1('x')
        OptionBuilder.create1("x")
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )

    def testBuilderIsResettedAlways_test4_decomposed(self) -> None:
        # Test case 1: Expecting an exception when calling create1 with invalid input
        with pytest.raises(ValueError, match="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create1('"')

        # Test case 2: Ensure description is reset after calling create1
        OptionBuilder.create1("x")
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )

        # Test case 3: Expecting an exception when calling create0 without proper setup
        with pytest.raises(ValueError, match="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create0()

        # Test case 4: Ensure description is reset again after calling create1
        OptionBuilder.create1("x")

    def testBuilderIsResettedAlways_test3_decomposed(self) -> None:
        # Test case 1: Expecting an exception when calling create1 with invalid input
        with self.assertRaises(ValueError, msg="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create1('"')

        # Test case 2: Ensure description is reset after calling create1
        option = OptionBuilder.create1("x")
        self.assertIsNone(option.getDescription(), "we inherited a description")

        # Test case 3: Expecting an exception when calling create0 without proper setup
        with self.assertRaises(ValueError, msg="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create0()

    def testBuilderIsResettedAlways_test2_decomposed(self) -> None:
        with pytest.raises(ValueError):
            OptionBuilder.withDescription("JUnit").create1('"')
            pytest.fail("ValueError expected")

        option = OptionBuilder.create1("x")
        self.assertIsNone(option.getDescription(), "we inherited a description")

    def testBuilderIsResettedAlways_test1_decomposed(self) -> None:
        with pytest.raises(ValueError):
            OptionBuilder.withDescription("JUnit").create1('"')

        # No exception expected here
        OptionBuilder.create1("x")

    def testBuilderIsResettedAlways_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError, msg="ValueError expected"):
            OptionBuilder.withDescription("JUnit").create1('"')

    def testBaseOptionStringOpt_test4_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create2("o")
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    def testBaseOptionStringOpt_test3_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create2("o")
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())

    def testBaseOptionStringOpt_test2_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create2("o")
        self.assertEqual("o", base.getOpt())

    def testBaseOptionStringOpt_test1_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create2("o")

    def testBaseOptionStringOpt_test0_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")

    def testBaseOptionCharOpt_test4_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create1("o")
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    def testBaseOptionCharOpt_test3_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create1("o")
        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())

    def testBaseOptionCharOpt_test2_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.withDescription("option description").create1("o")
        self.assertEqual("o", base.getOpt())

    def testBaseOptionCharOpt_test1_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
        base = OptionBuilder.create1("o")

    def testBaseOptionCharOpt_test0_decomposed(self) -> None:
        OptionBuilder.withDescription("option description")
