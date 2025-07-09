from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.QuoteMode import *


class JiraCsv148Test(unittest.TestCase):

    def testWithTrimEmpty_test4_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        builder.setQuoteMode(QuoteMode.ALL).setTrim(True)
        format_ = builder.setQuoteMode(QuoteMode.ALL).setTrim(True).build()
        self.assertEqual(
            '"","","Single space on the left","Single space on the right",'
            + '"Single spaces on both sides","Multiple spaces on the left",'
            + '"Multiple spaces on the right","Multiple spaces on both sides"',
            format_.format_(
                [
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     ",
                ]
            ),
        )

    def testWithTrimEmpty_test3_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).setTrim(True)
        format = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setTrim(True)
            .build()
        )

    def testWithTrimEmpty_test2_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).setTrim(True)

    def testWithTrimEmpty_test1_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)

    def testWithTrimEmpty_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()

    def testWithIgnoreSurroundingSpacesEmpty_test4_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        builder.setQuoteMode(QuoteMode.ALL).setIgnoreSurroundingSpaces(True)
        format_ = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setIgnoreSurroundingSpaces(True)
            .build()
        )
        self.assertEqual(
            '""," "," Single space on the left","Single space on the right "," Single'
            + ' spaces on both sides ","   Multiple spaces on the left","Multiple'
            + ' spaces on the right   ","  Multiple spaces on both sides     "',
            format_.format_(
                [
                    "",
                    " ",
                    " Single space on the left",
                    "Single space on the right ",
                    " Single spaces on both sides ",
                    "   Multiple spaces on the left",
                    "Multiple spaces on the right   ",
                    "  Multiple spaces on both sides     ",
                ]
            ),
        )

    def testWithIgnoreSurroundingSpacesEmpty_test3_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)
        builder.setQuoteMode(QuoteMode.ALL).setIgnoreSurroundingSpaces(True)
        format = (
            CSVFormat.DEFAULT.builder()
            .setQuoteMode(QuoteMode.ALL)
            .setIgnoreSurroundingSpaces(True)
            .build()
        )

    def testWithIgnoreSurroundingSpacesEmpty_test2_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL)
        CSVFormat.DEFAULT.builder().setQuoteMode(
            QuoteMode.ALL
        ).setIgnoreSurroundingSpaces(True)

    def testWithIgnoreSurroundingSpacesEmpty_test1_decomposed(self) -> None:
        builder = CSVFormat.DEFAULT.builder()
        builder.setQuoteMode(QuoteMode.ALL)

    def testWithIgnoreSurroundingSpacesEmpty_test0_decomposed(self) -> None:
        CSVFormat.DEFAULT.builder()
