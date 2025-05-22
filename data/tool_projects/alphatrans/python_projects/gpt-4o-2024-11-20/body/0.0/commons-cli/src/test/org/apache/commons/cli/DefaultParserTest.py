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
from src.main.org.apache.commons.cli.Options import *
from src.test.org.apache.commons.cli.ParserTestCase import *


class DefaultParserTest(ParserTestCase, unittest.TestCase):

    def testShortOptionQuoteHandlingWithStrip_test4_decomposed(self) -> None:
        # Create a builder for DefaultParser
        builder = DefaultParser.builder()

        # Set the builder to strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(True)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ["-b", '"quoted string"']

        # Parse the arguments using the parser
        cl = parser.parse0(self._options, args)

        # Assert that the option value for "-b" is "quoted string"
        self.assertEqual(
            "quoted string", cl.getOptionValue4("b"), 'Confirm -b "arg" strips quotes'
        )

    def testShortOptionQuoteHandlingWithStrip_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )
        args = ["-b", '"quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testShortOptionQuoteHandlingWithStrip_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )

    def testShortOptionQuoteHandlingWithStrip_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)

    def testShortOptionQuoteHandlingWithStrip_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def testShortOptionQuoteHandlingWithoutStrip_test4_decomposed(self) -> None:
        # Create a DefaultParser builder
        builder = DefaultParser.builder()

        # Set the builder to not strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(False)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ["-b", '"quoted string"']

        # Parse the arguments using the parser
        cl = parser.parse0(self._options, args)

        # Assert that the option value retains the quotes
        self.assertEqual(
            '"quoted string"', cl.getOptionValue4("b"), 'Confirm -b "arg" keeps quotes'
        )

    def testShortOptionQuoteHandlingWithoutStrip_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )
        args = ["-b", '"quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testShortOptionQuoteHandlingWithoutStrip_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )

    def testShortOptionQuoteHandlingWithoutStrip_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)

    def testShortOptionQuoteHandlingWithoutStrip_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def testShortOptionConcatenatedQuoteHandling_test1_decomposed(self) -> None:
        args = ['-b"quoted string"']
        cl = self.parser.parse0(self._options, args)
        self.assertEqual(
            '"quoted string"', cl.getOptionValue4("b"), 'Confirm -b"arg" keeps quotes'
        )

    def testShortOptionConcatenatedQuoteHandling_test0_decomposed(self) -> None:
        args = ['-b"quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testLongOptionWithEqualsQuoteHandlingWithStrip_test4_decomposed(self) -> None:
        # Create a DefaultParser builder
        builder = DefaultParser.builder()

        # Set the builder to strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(True)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ['--bfile="quoted string"']

        # Parse the arguments with the options
        cl = parser.parse0(self._options, args)

        # Assert that the quotes are stripped correctly
        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" strips quotes',
        )

    def testLongOptionWithEqualsQuoteHandlingWithStrip_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        args = ['--bfile="quoted string"']
        cl = parser.parse0(self._options, args)

    def testLongOptionWithEqualsQuoteHandlingWithStrip_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )

    def testLongOptionWithEqualsQuoteHandlingWithStrip_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)

    def testLongOptionWithEqualsQuoteHandlingWithStrip_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip_test4_decomposed(
        self,
    ) -> None:
        # Create a DefaultParser builder
        builder = DefaultParser.builder()

        # Set the builder to not strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(False)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ['--bfile="quoted string"']

        # Parse the arguments with the options
        cl = parser.parse0(self._options, args)

        # Assert that the option value retains the quotes
        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" keeps quotes',
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip_test3_decomposed(
        self,
    ) -> None:
        builder = DefaultParser.builder()
        builder.setStripLeadingAndTrailingQuotes(False)
        parser = builder.setStripLeadingAndTrailingQuotes(False).build()
        args = ['--bfile="quoted string"']
        cl = parser.parse0(self._options, args)

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip_test2_decomposed(
        self,
    ) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip_test1_decomposed(
        self,
    ) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)

    def testLongOptionWithEqualsQuoteHandlingWithoutStrip_test0_decomposed(
        self,
    ) -> None:
        DefaultParser.builder()

    def testLongOptionWithEqualsQuoteHandling_test1_decomposed(self) -> None:
        args = ['--bfile="quoted string"']
        cl = self.parser.parse0(self._options, args)
        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile="arg" strips quotes',
        )

    def testLongOptionWithEqualsQuoteHandling_test0_decomposed(self) -> None:
        args = ['--bfile="quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testLongOptionQuoteHandlingWithStrip_test4_decomposed(self) -> None:
        # Create a DefaultParser builder
        builder = DefaultParser.builder()

        # Set the builder to strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(True)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ["--bfile", '"quoted string"']

        # Parse the arguments using the parser
        cl = parser.parse0(self._options, args)

        # Assert that the quotes are stripped from the option value
        self.assertEqual(
            "quoted string",
            cl.getOptionValue4("b"),
            'Confirm --bfile "arg" strips quotes',
        )

    def testLongOptionQuoteHandlingWithStrip_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )
        args = ["--bfile", '"quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testLongOptionQuoteHandlingWithStrip_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(True).build()
        )

    def testLongOptionQuoteHandlingWithStrip_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(True)

    def testLongOptionQuoteHandlingWithStrip_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def testLongOptionQuoteHandlingWithoutStrip_test4_decomposed(self) -> None:
        # Create a DefaultParser builder
        builder = DefaultParser.builder()

        # Set the builder to not strip leading and trailing quotes
        builder.setStripLeadingAndTrailingQuotes(False)

        # Build the parser
        parser = builder.build()

        # Define the arguments
        args = ["--bfile", '"quoted string"']

        # Parse the arguments with the options
        cl = parser.parse0(self._options, args)

        # Assert that the option value retains the quotes
        self.assertEqual(
            '"quoted string"',
            cl.getOptionValue4("b"),
            'Confirm --bfile "arg" keeps quotes',
        )

    def testLongOptionQuoteHandlingWithoutStrip_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )
        args = ["--bfile", '"quoted string"']
        cl = self.parser.parse0(self._options, args)

    def testLongOptionQuoteHandlingWithoutStrip_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        self.parser = (
            DefaultParser.builder().setStripLeadingAndTrailingQuotes(False).build()
        )

    def testLongOptionQuoteHandlingWithoutStrip_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)

    def testLongOptionQuoteHandlingWithoutStrip_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def testBuilder_test4_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(
            False
        ).setAllowPartialMatching(False)
        parser = (
            DefaultParser.builder()
            .setStripLeadingAndTrailingQuotes(False)
            .setAllowPartialMatching(False)
            .build()
        )
        self.assertEqual(DefaultParser, parser.__class__)

    def testBuilder_test3_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(
            False
        ).setAllowPartialMatching(False)
        self.parser = (
            DefaultParser.builder()
            .setStripLeadingAndTrailingQuotes(False)
            .setAllowPartialMatching(False)
            .build()
        )

    def testBuilder_test2_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(
            False
        ).setAllowPartialMatching(False)

    def testBuilder_test1_decomposed(self) -> None:
        DefaultParser.builder()
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(False)

    def testBuilder_test0_decomposed(self) -> None:
        DefaultParser.builder()

    def setUp(self) -> None:
        super().setUp()
        self.parser = DefaultParser(2, False, None)
