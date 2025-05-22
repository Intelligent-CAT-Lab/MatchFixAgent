from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.validator.util.Flags import *


class FlagsTest(unittest.TestCase):

    __INT_FLAG: int = 4
    __LONG_FLAG_2: int = 2
    __LONG_FLAG: int = 1

    def testToString_test4_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with constructorId=1 and flags=0
        s = f.toString()  # Get the string representation of the Flags object
        self.assertEqual(64, len(s))  # Assert that the length of the string is 64
        f.turnOn(self.__INT_FLAG)  # Turn on the flag with value 4
        s = f.toString()  # Get the updated string representation
        self.assertEqual(64, len(s))  # Assert that the length of the string is still 64
        self.assertEqual(
            "0000000000000000000000000000000000000000000000000000000000000100", s
        )  # Assert the expected binary string

    def testToString_test3_decomposed(self) -> None:
        f = Flags(0, 0)  # Create a Flags object with initial values 0, 0
        s = f.toString()  # Call the toString method
        self.assertEqual(64, len(s))  # Assert that the length of the string is 64
        f.turnOn(self.__INT_FLAG)  # Turn on the flag with the value of __INT_FLAG
        s = f.toString()  # Call the toString method again

    def testToString_test2_decomposed(self) -> None:
        f = Flags(1, 0)
        s = f.toString()
        self.assertEqual(
            64, len(s), "String length does not match expected length of 64"
        )
        f.turnOn(self.__INT_FLAG)

    def testToString_test1_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with constructorId=1 and flags=0
        s = f.toString()  # Call the toString method
        self.assertEqual(
            s, "0" * 64
        )  # Assert that the result is a 64-bit string of zeros

    def testToString_test0_decomposed(self) -> None:
        f = Flags(1, 0)

    def testIsOn_isTrueWhenHighOrderBitIsSetAndQueried_test1_decomposed(self) -> None:
        all_on = Flags(1, ~0)
        high_order_bit = 0x8000000000000000
        self.assertTrue(all_on.isOn(high_order_bit))

    def testIsOn_isTrueWhenHighOrderBitIsSetAndQueried_test0_decomposed(self) -> None:
        all_on = Flags(1, ~0)

    def testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn_test1_decomposed(self) -> None:
        first = Flags(1, 1)
        first_and_second = 3
        self.assertFalse(first.isOn(first_and_second))

    def testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn_test0_decomposed(self) -> None:
        first = Flags(1, 1)

    def testTurnOnAll_test2_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with constructorId=1 and flags=0
        f.turnOnAll()  # Call the turnOnAll method to set all flags
        self.assertEqual(
            0xFFFFFFFFFFFFFFFF,
            f.getFlags(),
            "Flags were not set to all 1s (0xFFFFFFFFFFFFFFFF)",
        )

    def testTurnOnAll_test1_decomposed(self) -> None:
        f = Flags(1, 0)
        f.turnOnAll()

    def testTurnOnAll_test0_decomposed(self) -> None:
        f = Flags(0, 0)

    def testClear_test2_decomposed(self) -> None:
        f = Flags(1, 98432)
        f.clear()
        self.assertEqual(0, f.getFlags())

    def testClear_test1_decomposed(self) -> None:
        f = Flags(1, 98432)
        f.clear()
        self.assertEqual(f._Flags__flags, 0)

    def testClear_test0_decomposed(self) -> None:
        f = Flags(1, 98432)

    def testTurnOffAll_test2_decomposed(self) -> None:
        f = Flags(
            1, 98432
        )  # Create a Flags object with constructorId=1 and flags=98432
        f.turnOffAll()  # Call the turnOffAll method to set flags to 0
        self.assertEqual(0, f.getFlags())  # Assert that the flags are now 0

    def testTurnOffAll_test1_decomposed(self) -> None:
        f = Flags(1, 98432)
        f.turnOffAll()
        self.assertEqual(f._Flags__flags, 0)

    def testTurnOffAll_test0_decomposed(self) -> None:
        f = Flags(1, 98432)

    def testIsOnOff_test5_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with constructorId=1 and flags=0
        f.turnOn(self.__LONG_FLAG)  # Turn on LONG_FLAG
        f.turnOn(self.__INT_FLAG)  # Turn on INT_FLAG
        self.assertTrue(f.isOn(self.__LONG_FLAG))  # Assert LONG_FLAG is on
        self.assertTrue(not f.isOff(self.__LONG_FLAG))  # Assert LONG_FLAG is not off
        self.assertTrue(f.isOn(self.__INT_FLAG))  # Assert INT_FLAG is on
        self.assertTrue(not f.isOff(self.__INT_FLAG))  # Assert INT_FLAG is not off
        self.assertTrue(f.isOff(self.__LONG_FLAG_2))  # Assert LONG_FLAG_2 is off

    def testIsOnOff_test4_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with initial flags set to 0
        f.turnOn(self.__LONG_FLAG)  # Turn on the LONG_FLAG
        f.turnOn(self.__INT_FLAG)  # Turn on the INT_FLAG
        self.assertTrue(f.isOn(self.__LONG_FLAG))  # Assert that LONG_FLAG is on
        self.assertTrue(
            not f.isOff(self.__LONG_FLAG)
        )  # Assert that LONG_FLAG is not off
        self.assertTrue(f.isOn(self.__INT_FLAG))  # Assert that INT_FLAG is on

    def testIsOnOff_test3_decomposed(self) -> None:
        f = Flags(0, 0)
        f.turnOn(self.__LONG_FLAG)
        f.turnOn(self.__INT_FLAG)
        self.assertTrue(f.isOn(self.__LONG_FLAG))
        self.assertTrue(not f.isOff(self.__LONG_FLAG))

    def testIsOnOff_test2_decomposed(self) -> None:
        f = Flags(1, 0)  # Create a Flags object with constructorId=1 and flags=0
        f.turnOn(self.__LONG_FLAG)  # Turn on the LONG_FLAG
        f.turnOn(self.__INT_FLAG)  # Turn on the INT_FLAG
        self.assertTrue(f.isOn(self.__LONG_FLAG))  # Assert that LONG_FLAG is on

    def testIsOnOff_test1_decomposed(self) -> None:
        f = Flags(0, 0)
        f.turnOn(self.__LONG_FLAG)
        f.turnOn(self.__INT_FLAG)

    def testIsOnOff_test0_decomposed(self) -> None:
        f = Flags(0, 0)

    def testGetFlags_test1_decomposed(self) -> None:
        f = Flags(1, 45)
        self.assertEqual(f.getFlags(), 45)

    def testGetFlags_test0_decomposed(self) -> None:
        f = Flags(1, 45)

    def testHashCode_test1_decomposed(self) -> None:
        f = Flags(1, 45)
        self.assertEqual(f.hashCode(), 45)

    def testHashCode_test0_decomposed(self) -> None:
        f = Flags(1, 45)
