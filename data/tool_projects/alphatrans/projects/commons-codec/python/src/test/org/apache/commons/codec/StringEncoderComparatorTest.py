from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringEncoderComparator import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.main.org.apache.commons.codec.language.Soundex import *


class StringEncoderComparatorTest(unittest.TestCase):

    def testComparatorWithDoubleMetaphoneAndInvalidInput_test2_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, DoubleMetaphone())
        compare = s_compare.compare(3.0, 3)
        self.assertEqual(
            0,
            compare,
            "Trying to compare objects that make no sense to the underlying encoder should"
            + " return a zero compare code",
        )

    def testComparatorWithDoubleMetaphoneAndInvalidInput_test1_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, DoubleMetaphone())
        with self.assertRaises(EncoderException) as context:
            s_compare.compare(3.0, 3)
        self.assertEqual(str(context.exception), "Method not implemented")

    def testComparatorWithDoubleMetaphoneAndInvalidInput_test0_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, DoubleMetaphone())

    def testComparatorWithDoubleMetaphone_test1_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, DoubleMetaphone())
        test_array = ["Jordan", "Sosa", "Prior", "Pryor"]
        test_list = list(test_array)
        control_array = ["Jordan", "Prior", "Pryor", "Sosa"]

        # Sorting the test_list using the comparator
        test_list.sort(
            key=lambda x: s_compare._StringEncoderComparator__stringEncoder.encode(x)
        )

        result_array = test_list

        for i in range(len(result_array)):
            self.assertEqual(
                control_array[i],
                result_array[i],
                f"Result Array not Equal to Control Array at index: {i}",
            )

    def testComparatorWithDoubleMetaphone_test0_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, DoubleMetaphone())

    def testComparatorWithSoundex_test1_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, Soundex(3, False, None, None))
        self.assertEqual(
            0,
            s_compare.compare("O'Brien", "O'Brian"),
            "O'Brien and O'Brian didn't come out with the same Soundex, something must be wrong here",
        )

    def testComparatorWithSoundex_test0_decomposed(self) -> None:
        s_compare = StringEncoderComparator(0, Soundex(3, False, None, None))
