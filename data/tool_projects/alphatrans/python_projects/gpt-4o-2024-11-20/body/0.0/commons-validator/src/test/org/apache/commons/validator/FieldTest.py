from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.Field import *


class FieldTest(unittest.TestCase):

    _field: typing.Any = None

    def testOverrideSomePosition_test35_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverrideSomePosition(11) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg0(1).getKey(),
            "testOverrideSomePosition(12) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg0(2).getKey(),
            "testOverrideSomePosition(13) ",
        )
        self.assertIsNone(self._field.getArg0(3), "testOverrideSomePosition(14) ")

    def testOverrideSomePosition_test34_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverrideSomePosition(11) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg0(1).getKey(),
            "testOverrideSomePosition(12) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg0(2).getKey(),
            "testOverrideSomePosition(13) ",
        )

    def testOverrideSomePosition_test33_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverrideSomePosition(11) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg0(1).getKey(),
            "testOverrideSomePosition(12) ",
        )

    def testOverrideSomePosition_test32_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverrideSomePosition(11) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg0(1).getKey(),
            "testOverrideSomePosition(12) ",
        )

    def testOverrideSomePosition_test31_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

        # Assertions for default arguments
        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverrideSomePosition(11) ",
        )

    def testOverrideSomePosition_test30_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideSomePosition(3) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverrideSomePosition(4) ",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")), 4, "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(7) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideSomePosition(8) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideSomePosition(9) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 3).getKey(),
            "mask-position-3",
            "testOverrideSomePosition(10) ",
        )

        self.assertEqual(
            self._field.getArg0(0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(11) ",
        )

    def testOverrideSomePosition_test29_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideSomePosition(3) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverrideSomePosition(4) ",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            len(self._field.getArgs("mask")), 4, "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(7) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideSomePosition(8) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideSomePosition(9) ",
        )

        self.assertEqual(
            self._field.getArg1("mask", 3).getKey(),
            "mask-position-3",
            "testOverrideSomePosition(10) ",
        )

        self._field.getArg0(0)

    def testOverrideSomePosition_test28_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9) ",
        )
        self.assertEqual(
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
            "testOverrideSomePosition(10) ",
        )

    def testOverrideSomePosition_test27_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideSomePosition(1)"
        )

        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(2)",
        )

        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideSomePosition(3)",
        )

        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverrideSomePosition(4)",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        self.assertEqual(
            len(self._field.getArgs("mask")), 4, "testOverrideSomePosition(6)"
        )

        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(7)",
        )

        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideSomePosition(8)",
        )

        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideSomePosition(9)",
        )

    def testOverrideSomePosition_test26_decomposed(self) -> None:
        self._field = Field()

        # Adding arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3)",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4)",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7)",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8)",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideSomePosition(9)",
        )

    def testOverrideSomePosition_test25_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2)",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3)",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4)",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7)",
        )

        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8)",
        )

    def testOverrideSomePosition_test24_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3)",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4)",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7)",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideSomePosition(8)",
        )

    def testOverrideSomePosition_test23_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )

    def testOverrideSomePosition_test22_decomposed(self) -> None:
        self._field = Field()

        # Adding arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideSomePosition(7) ",
        )

    def testOverrideSomePosition_test21_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2)",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3)",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4)",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6)"
        )

        self._field.getArg1("mask", 0)

    def testOverrideSomePosition_test20_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3)",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4)",
        )
        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5)"
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideSomePosition(6)"
        )

    def testOverrideSomePosition_test19_decomposed(self) -> None:
        self._field = Field()

        # Adding arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions
        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideSomePosition(3) ",
        )

        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "required-position-2",
            "testOverrideSomePosition(4) ",
        )

        self.assertIsNone(
            self._field.getArg1("required", 3), "testOverrideSomePosition(5) "
        )

    def testOverrideSomePosition_test18_decomposed(self) -> None:
        self._field = Field()

        # Adding default-position arguments
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Adding required-position arguments
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))

        # Adding mask-position argument
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideSomePosition(4) ",
        )

    def testOverrideSomePosition_test17_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        # Assert the key of the first argument with the key "required"
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

        # Assert the key of the second argument with the key "required"
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )

    def testOverrideSomePosition_test16_decomposed(self) -> None:
        self._field = Field()

        # Create and add arguments
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assertions
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideSomePosition(3) ",
        )

    def testOverrideSomePosition_test15_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assert the number of required arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        # Assert the key of the first required argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

    def testOverrideSomePosition_test14_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add arguments with required positions
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))

        # Create and add arguments with mask positions
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assert the number of required arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        # Assert the key of the first required argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideSomePosition(2) ",
        )

    def testOverrideSomePosition_test13_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add arguments with specific positions and names
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        # Assert the number of arguments with the "required" key
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

        # Retrieve the first argument with the "required" key
        self._field.getArg1("required", 0)

    def testOverrideSomePosition_test12_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideSomePosition(1) "
        )

    def testOverrideSomePosition_test11_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

    def testOverrideSomePosition_test10_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self.__createArg2("mask-position-3", "mask")

    def testOverrideSomePosition_test9_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))

    def testOverrideSomePosition_test8_decomposed(self) -> None:
        self._field = Field()

        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

        arg3_1 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_1)

        arg2_2 = self.__createArg2("required-position-2", "required")

    def testOverrideSomePosition_test7_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

    def testOverrideSomePosition_test6_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

        self.__createArg3("required-position-1", "required", 1)

    def testOverrideSomePosition_test5_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

    def testOverrideSomePosition_test4_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)
        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)
        arg0_2 = self.__createArg0("default-position-2")

    def testOverrideSomePosition_test3_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)
        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

    def testOverrideSomePosition_test2_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        self.__createArg0("default-position-1")

    def testOverrideSomePosition_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testOverrideSomePosition_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testOverridePositionImplied_test23_decomposed(self) -> None:
        self._field = Field()

        # Create and add arguments
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3)",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6)",
        )
        self.assertEqual(
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverridePositionImplied(7)",
        )
        self.assertIsNone(
            self._field.getArg1("mask", 2), "testOverridePositionImplied(8)"
        )

        # Assertions for default arguments
        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverridePositionImplied(9)",
        )
        self.assertIsNone(self._field.getArg0(1), "testOverridePositionImplied(10)")
        self.assertIsNone(self._field.getArg0(2), "testOverridePositionImplied(11)")

    def testOverridePositionImplied_test22_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4) ",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6) ",
        )
        self.assertEqual(
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverridePositionImplied(7) ",
        )
        self.assertIsNone(
            self._field.getArg1("mask", 2), "testOverridePositionImplied(8) "
        )

        # Assertions for default arguments
        self.assertEqual(
            "default-position-0",
            self._field.getArg0(0).getKey(),
            "testOverridePositionImplied(9) ",
        )

    def testOverridePositionImplied_test21_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2)",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3)",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6)",
        )

        self.assertEqual(
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverridePositionImplied(7)",
        )

        self.assertIsNone(
            self._field.getArg1("mask", 2), "testOverridePositionImplied(8)"
        )

        # Access the first argument (position 0)
        self._field.getArg0(0)

    def testOverridePositionImplied_test20_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3)",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6)",
        )
        self.assertEqual(
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverridePositionImplied(7)",
        )
        self.assertIsNone(
            self._field.getArg1("mask", 2), "testOverridePositionImplied(8)"
        )

    def testOverridePositionImplied_test19_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2)",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3)",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6)",
        )

        self.assertEqual(
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverridePositionImplied(7)",
        )

    def testOverridePositionImplied_test18_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        arg_required_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            arg_required_0.getKey(),
            "testOverridePositionImplied(2) ",
        )

        arg_required_1 = self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            arg_required_1.getKey(),
            "testOverridePositionImplied(3) ",
        )

        arg_required_2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "required-position-2",
            arg_required_2.getKey(),
            "testOverridePositionImplied(4) ",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5) "
        )

        arg_mask_0 = self._field.getArg1("mask", 0)
        self.assertEqual(
            "default-position-0", arg_mask_0.getKey(), "testOverridePositionImplied(6) "
        )

    def testOverridePositionImplied_test17_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3) ",
        )
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4) ",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverridePositionImplied(6) ",
        )

    def testOverridePositionImplied_test16_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        arg_required_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            arg_required_0.getKey(),
            "testOverridePositionImplied(2) ",
        )

        arg_required_1 = self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            arg_required_1.getKey(),
            "testOverridePositionImplied(3) ",
        )

        arg_required_2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "required-position-2",
            arg_required_2.getKey(),
            "testOverridePositionImplied(4) ",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5) "
        )

        arg_mask_0 = self._field.getArg1("mask", 0)

    def testOverridePositionImplied_test15_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assertions for "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1)"
        )

        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2)",
        )

        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3)",
        )

        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverridePositionImplied(5)"
        )

    def testOverridePositionImplied_test14_decomposed(self) -> None:
        # Create and add the first argument
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the second argument
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the third argument
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the fourth argument
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert the number of "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        # Assert the key of the first "required" argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2) ",
        )

        # Assert the key of the second "required" argument
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3) ",
        )

        # Assert the key of the third "required" argument
        self.assertEqual(
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverridePositionImplied(4) ",
        )

    def testOverridePositionImplied_test13_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert the number of required arguments
        self.assertEqual(
            len(self._field.getArgs("required")), 3, "testOverridePositionImplied(1) "
        )

        # Assert the key of the first required argument
        arg_at_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            arg_at_0.getKey(), "default-position-0", "testOverridePositionImplied(2) "
        )

        # Assert the key of the second required argument
        arg_at_1 = self._field.getArg1("required", 1)
        self.assertEqual(
            arg_at_1.getKey(), "required-position-1", "testOverridePositionImplied(3) "
        )

        # Access the third required argument (no assertion needed as per the original code)
        self._field.getArg1("required", 2)

    def testOverridePositionImplied_test12_decomposed(self) -> None:
        # Create and add the first argument with key "default-position-0"
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the second argument with key "required-position-1" and name "required"
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the third argument with key "required-position-2" and name "required"
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the fourth argument with key "mask-position-1" and name "mask"
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert that there are 3 arguments with the name "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        # Assert the key of the first "required" argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverridePositionImplied(2) ",
        )

        # Assert the key of the second "required" argument
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverridePositionImplied(3) ",
        )

    def testOverridePositionImplied_test11_decomposed(self) -> None:
        # Create and add the first argument with "default-position-0"
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the first "required" argument with "required-position-1"
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the second "required" argument with "required-position-2"
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the "mask" argument with "mask-position-1"
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert that there are 3 "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        # Retrieve the first "required" argument and assert its key
        first_required_arg = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            first_required_arg.getKey(),
            "testOverridePositionImplied(2) ",
        )

        # Retrieve the second "required" argument (no assertion needed here)
        self._field.getArg1("required", 1)

    def testOverridePositionImplied_test10_decomposed(self) -> None:
        # Create and add the first argument with "default-position-0"
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the first "required" argument with "required-position-1"
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the second "required" argument with "required-position-2"
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the "mask" argument with "mask-position-1"
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert that there are 3 "required" arguments
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        # Retrieve the first "required" argument and assert its key
        first_required_arg = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            first_required_arg.getKey(),
            "testOverridePositionImplied(2) ",
        )

    def testOverridePositionImplied_test9_decomposed(self) -> None:
        # Create and add the first argument
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the second argument
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the third argument
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the fourth argument
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

        # Retrieve the first argument with the key "required" and position 0
        self._field.getArg1("required", 0)

    def testOverridePositionImplied_test8_decomposed(self) -> None:
        self._field = Field()

        # Create and add the first argument
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        # Create and add the second argument
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        # Create and add the third argument
        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        # Create and add the fourth argument
        arg3 = self.__createArg2("mask-position-1", "mask")
        self._field.addArg(arg3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverridePositionImplied(1) "
        )

    def testOverridePositionImplied_test7_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

    def testOverridePositionImplied_test6_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

        arg3 = self.__createArg2("mask-position-1", "mask")

    def testOverridePositionImplied_test5_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)

        arg2 = self.__createArg2("required-position-2", "required")
        self._field.addArg(arg2)

    def testOverridePositionImplied_test4_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg1)
        arg2 = self.__createArg2("required-position-2", "required")

    def testOverridePositionImplied_test3_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg2 = self.__createArg2("required-position-1", "required")
        self._field.addArg(arg2)

    def testOverridePositionImplied_test2_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        self.__createArg2("required-position-1", "required")

    def testOverridePositionImplied_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testOverridePositionImplied_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testOverrideUsingPositionB_test26_decomposed(self) -> None:
        self._field = Field()

        # Adding arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assertions for "required" key
        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideUsingPositionB(1)"
        )
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(2)",
        )
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionB(3)",
        )
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(4)",
        )
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "required-position-3",
            "testOverrideUsingPositionB(5)",
        )

        # Assertions for "mask" key
        self.assertEqual(
            len(self._field.getArgs("mask")), 4, "testOverrideUsingPositionB(6)"
        )
        self.assertEqual(
            self._field.getArg1("mask", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(6)",
        )
        self.assertEqual(
            self._field.getArg1("mask", 1).getKey(),
            "default-position-1",
            "testOverrideUsingPositionB(7)",
        )
        self.assertEqual(
            self._field.getArg1("mask", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(8)",
        )
        self.assertIsNone(
            self._field.getArg1("mask", 3), "testOverrideUsingPositionB(9)"
        )

    def testOverrideUsingPositionB_test25_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2)",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3)",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4)",
        )
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5)",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6)"
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideUsingPositionB(6)",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionB(7)",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
            "testOverrideUsingPositionB(8)",
        )

    def testOverrideUsingPositionB_test24_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1)"
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2)",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3)",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4)",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5)",
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6)"
        )

        self._field.getArg1("mask", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideUsingPositionB(6)",
        )

        self._field.getArg1("mask", 1)
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionB(7)",
        )

        self._field.getArg1("mask", 2)

    def testOverrideUsingPositionB_test23_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1)"
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2)",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3)",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4)",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5)",
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6)"
        )

        self._field.getArg1("mask", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideUsingPositionB(6)",
        )

        self._field.getArg1("mask", 1)
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionB(7)",
        )

    def testOverrideUsingPositionB_test22_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1)"
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2)",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3)",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4)",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5)",
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6)"
        )

        self._field.getArg1("mask", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideUsingPositionB(6)",
        )

        self._field.getArg1("mask", 1)

    def testOverrideUsingPositionB_test21_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2) ",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3) ",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4) ",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5) ",
        )

        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6) "
        )

        self._field.getArg1("mask", 0)
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
            "testOverrideUsingPositionB(6) ",
        )

    def testOverrideUsingPositionB_test20_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assertions for "required" arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2) ",
        )
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4) ",
        )
        self.assertEqual(
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testOverrideUsingPositionB(5) ",
        )

        # Assertions for "mask" arguments
        self.assertEqual(
            4, len(self._field.getArgs("mask")), "testOverrideUsingPositionB(6) "
        )
        self._field.getArg1("mask", 0)

    def testOverrideUsingPositionB_test19_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideUsingPositionB(1) "
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(2) ",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionB(3) ",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(4) ",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "required-position-3",
            "testOverrideUsingPositionB(5) ",
        )

        self.assertEqual(
            len(self._field.getArgs("mask")), 4, "testOverrideUsingPositionB(6) "
        )

    def testOverrideUsingPositionB_test18_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideUsingPositionB(1) "
        )

        self._field.getArg1("required", 0)
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(2) ",
        )

        self._field.getArg1("required", 1)
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionB(3) ",
        )

        self._field.getArg1("required", 2)
        self.assertEqual(
            self._field.getArg1("required", 2).getKey(),
            "default-position-2",
            "testOverrideUsingPositionB(4) ",
        )

        self._field.getArg1("required", 3)
        self.assertEqual(
            self._field.getArg1("required", 3).getKey(),
            "required-position-3",
            "testOverrideUsingPositionB(5) ",
        )

    def testOverrideUsingPositionB_test17_decomposed(self) -> None:
        # Create and add arguments with specific positions
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        # Validate the key of the argument at position 0
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2) ",
        )

        # Validate the key of the argument at position 1
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3) ",
        )

        # Validate the key of the argument at position 2
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4) ",
        )

        # Access the argument at position 3 (no assertion needed as per the original code)
        self._field.getArg1("required", 3)

    def testOverrideUsingPositionB_test16_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assert the number of required arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        # Assert the key of the first required argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2) ",
        )

        # Assert the key of the second required argument
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3) ",
        )

        # Assert the key of the third required argument
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testOverrideUsingPositionB(4) ",
        )

    def testOverrideUsingPositionB_test15_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        # Validate the first argument's key
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testOverrideUsingPositionB(2) ",
        )

        # Validate the second argument's key
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionB(3) ",
        )

        # Access the third argument (no assertion needed as per the original Java code)
        self._field.getArg1("required", 2)

    def testOverrideUsingPositionB_test14_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideUsingPositionB(1) "
        )

        # Assert the key of the first argument
        self.assertEqual(
            self._field.getArg1("required", 0).getKey(),
            "default-position-0",
            "testOverrideUsingPositionB(2) ",
        )

        # Assert the key of the second argument
        self.assertEqual(
            self._field.getArg1("required", 1).getKey(),
            "required-position-1",
            "testOverrideUsingPositionB(3) ",
        )

    def testOverrideUsingPositionB_test13_decomposed(self) -> None:
        # Create and add arguments with position 3
        arg3_1 = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(arg3_1)

        # Create and add arguments with position 1
        arg3_2 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_2)

        # Create and add arguments with default positions
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

        arg0_3 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        # Retrieve and assert the first argument with the key "required"
        arg1_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg1_0.getKey(), "testOverrideUsingPositionB(2) "
        )

        # Retrieve the second argument with the key "required"
        arg1_1 = self._field.getArg1("required", 1)

    def testOverrideUsingPositionB_test12_decomposed(self) -> None:
        # Create and add arguments with specific positions and keys
        arg3_1 = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(arg3_1)

        arg3_2 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_2)

        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

        arg0_3 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            len(self._field.getArgs("required")), 4, "testOverrideUsingPositionB(1) "
        )

        # Retrieve the first argument with the key "required" and assert its key
        arg1 = self._field.getArg1("required", 0)
        self.assertEqual(
            arg1.getKey(), "default-position-0", "testOverrideUsingPositionB(2) "
        )

    def testOverrideUsingPositionB_test11_decomposed(self) -> None:
        # Create and add arguments with position 3
        arg3_1 = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(arg3_1)

        # Create and add arguments with position 1
        arg3_2 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_2)

        # Create and add default arguments with positions 0, 1, and 2
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

        arg0_3 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_3)

        # Assert the number of required arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testOverrideUsingPositionB(1) "
        )

        # Retrieve the first required argument
        self._field.getArg1("required", 0)

    def testOverrideUsingPositionB_test10_decomposed(self) -> None:
        self._field = Field()

        # Create and add arguments with position 3
        arg3_1 = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(arg3_1)

        # Create and add arguments with position 1
        arg3_2 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_2)

        # Create and add arguments with default positions
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

        arg0_3 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(4, len(self._field.getArgs("required")))

    def testOverrideUsingPositionB_test9_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")
        self._field.addArg(self.__createArg0("default-position-2"))

    def testOverrideUsingPositionB_test8_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")

    def testOverrideUsingPositionB_test7_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))

    def testOverrideUsingPositionB_test6_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")

    def testOverrideUsingPositionB_test5_decomposed(self) -> None:
        self._field = Field()
        arg3_1 = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(arg3_1)
        arg3_2 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_2)
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testOverrideUsingPositionB_test4_decomposed(self) -> None:
        self._field = Field()
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self.__createArg0("default-position-0")

    def testOverrideUsingPositionB_test3_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

    def testOverrideUsingPositionB_test2_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self.__createArg3("required-position-1", "required", 1)

    def testOverrideUsingPositionB_test1_decomposed(self) -> None:
        arg = self.__createArg3("required-position-3", "required", 3)
        self._field.addArg(self.__createArg3("required-position-3", "required", 3))

    def testOverrideUsingPositionB_test0_decomposed(self) -> None:
        self.__createArg3("required-position-3", "required", 3)

    def testOverrideUsingPositionA_test15_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the "required" key
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1)"
        )

        # Assert the key of the argument at position 1 with the "required" key
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2)",
        )

        # Assert the number of arguments with the "mask" key
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverrideUsingPositionA(3)"
        )

        # Assert the key of the argument at position 1 with the "mask" key
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionA(4)",
        )

        # Assert the key of the argument at position 1 with the default key
        self.assertEqual(
            "default-position-1",
            self._field.getArg0(1).getKey(),
            "testOverrideUsingPositionA(5)",
        )

    def testOverrideUsingPositionA_test14_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the "required" key
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1)"
        )

        # Assert the key of the argument at position 1 with the "required" key
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2)",
        )

        # Assert the number of arguments with the "mask" key
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverrideUsingPositionA(3)"
        )

        # Assert the key of the argument at position 1 with the "mask" key
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionA(4)",
        )

        # Retrieve the argument at position 1 with the default key
        self._field.getArg0(1)

    def testOverrideUsingPositionA_test13_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the "required" key
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1) "
        )

        # Assert the key of the argument at position 1 with the "required" key
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2) ",
        )

        # Assert the number of arguments with the "mask" key
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverrideUsingPositionA(3) "
        )

        # Assert the key of the argument at position 1 with the "mask" key
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
            "testOverrideUsingPositionA(4) ",
        )

    def testOverrideUsingPositionA_test12_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the "required" key
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1) "
        )

        # Assert the key of the argument at position 1 with the "required" key
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2) ",
        )

        # Assert the number of arguments with the "mask" key
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverrideUsingPositionA(3) "
        )

        # Access the argument at position 1 with the "mask" key
        self._field.getArg1("mask", 1)

    def testOverrideUsingPositionA_test11_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1) "
        )

        # Assert the key of the argument at position 1 with the key "required"
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2) ",
        )

        # Assert the number of arguments with the key "mask"
        self.assertEqual(
            3, len(self._field.getArgs("mask")), "testOverrideUsingPositionA(3) "
        )

    def testOverrideUsingPositionA_test10_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add an argument with a required position
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1) "
        )

        # Assert the key of the argument at position 1 with the key "required"
        self.assertEqual(
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testOverrideUsingPositionA(2) ",
        )

    def testOverrideUsingPositionA_test9_decomposed(self) -> None:
        # Create and add arguments with default positions
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

        # Create and add an argument with a required position
        arg3_1 = self.__createArg3("required-position-1", "required", 1)
        self._field.addArg(arg3_1)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testOverrideUsingPositionA(1) "
        )

        # Retrieve an argument at position 1 with the key "required"
        self._field.getArg1("required", 1)

    def testOverrideUsingPositionA_test8_decomposed(self) -> None:
        # Create and add arguments with default positions
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        # Create and add arguments with specific positions
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            len(self._field.getArgs("required")), 3, "testOverrideUsingPositionA(1) "
        )

    def testOverrideUsingPositionA_test7_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

    def testOverrideUsingPositionA_test6_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self.__createArg3("required-position-1", "required", 1)

    def testOverrideUsingPositionA_test5_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

    def testOverrideUsingPositionA_test4_decomposed(self) -> None:
        self.__createArg0("default-position-0")
        self._field.addArg(self.__createArg0("default-position-0"))
        self.__createArg0("default-position-1")
        self._field.addArg(self.__createArg0("default-position-1"))
        self.__createArg0("default-position-2")

    def testOverrideUsingPositionA_test3_decomposed(self) -> None:
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)
        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

    def testOverrideUsingPositionA_test2_decomposed(self) -> None:
        self._field = Field()  # Ensure _field is initialized
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        self.__createArg0("default-position-1")

    def testOverrideUsingPositionA_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testOverrideUsingPositionA_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testDefaultSomePositions_test16_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Assert the key of each argument in the required order
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultSomePositions(2) ",
        )

        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultSomePositions(3) ",
        )

        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testDefaultSomePositions(4) ",
        )

        self.assertEqual(
            "default-position-3",
            self._field.getArg1("required", 3).getKey(),
            "testDefaultSomePositions(5) ",
        )

    def testDefaultSomePositions_test15_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Assert the key of each argument in the required order
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultSomePositions(2) ",
        )

        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultSomePositions(3) ",
        )

        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testDefaultSomePositions(4) ",
        )

        # Ensure the last argument is accessed (no assertion needed here)
        self._field.getArg1("required", 3)

    def testDefaultSomePositions_test14_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Assert the key of each argument in the correct order
        arg0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg0.getKey(), "testDefaultSomePositions(2) "
        )

        arg1 = self._field.getArg1("required", 1)
        self.assertEqual(
            "default-position-1", arg1.getKey(), "testDefaultSomePositions(3) "
        )

        arg2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2", arg2.getKey(), "testDefaultSomePositions(4) "
        )

    def testDefaultSomePositions_test13_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))
        self._field.addArg(self.__createArg1("default-position-1", 1))

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Assert the key of the first argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultSomePositions(2) ",
        )

        # Assert the key of the second argument
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultSomePositions(3) ",
        )

        # Access the third argument (no assertion needed as per the original code)
        self._field.getArg1("required", 2)

    def testDefaultSomePositions_test12_decomposed(self) -> None:
        # Create and add arguments to the field
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))
        self._field.addArg(self.__createArg1("default-position-1", 1))

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Assert the key of the first argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultSomePositions(2) ",
        )

        # Assert the key of the second argument
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultSomePositions(3) ",
        )

    def testDefaultSomePositions_test11_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Retrieve and assert the first argument's key
        arg0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg0.getKey(), "testDefaultSomePositions(2) "
        )

        # Retrieve the second argument (no assertion needed as per the original code)
        self._field.getArg1("required", 1)

    def testDefaultSomePositions_test10_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments in the field
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Retrieve and assert the key of the first argument
        arg = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg.getKey(), "testDefaultSomePositions(2) "
        )

    def testDefaultSomePositions_test9_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        # Create and add the third argument
        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        # Create and add the fourth argument
        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

        # Assert the number of arguments added
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

        # Retrieve the first argument at position 0
        self._field.getArg1("required", 0)

    def testDefaultSomePositions_test8_decomposed(self) -> None:
        self._field = Field()

        # Create and add arguments
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg1_1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_1)

        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        arg1_2 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_2)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultSomePositions(1) "
        )

    def testDefaultSomePositions_test7_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg1_2 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1_2)

        arg0_3 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_3)

        arg1_1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1_1)

    def testDefaultSomePositions_test6_decomposed(self) -> None:
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))
        self._field.addArg(self.__createArg1("default-position-1", 1))

    def testDefaultSomePositions_test5_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        arg2 = self.__createArg0("default-position-3")
        self._field.addArg(arg2)

    def testDefaultSomePositions_test4_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)
        self.__createArg0("default-position-3")

    def testDefaultSomePositions_test3_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

    def testDefaultSomePositions_test2_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        self.__createArg1("default-position-2", 2)

    def testDefaultSomePositions_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testDefaultSomePositions_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testDefaultOnePosition_test12_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument with position 2
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments in the "required" key
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Assert the first argument's key
        arg1_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg1_0.getKey(), "testDefaultOnePosition(2) "
        )

        # Assert the second argument is None
        self.assertIsNone(
            self._field.getArg1("required", 1), "testDefaultOnePosition(3) "
        )

        # Assert the third argument's key
        arg1_2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2", arg1_2.getKey(), "testDefaultOnePosition(4) "
        )

        # Assert the fourth argument's key
        arg1_3 = self._field.getArg1("required", 3)
        self.assertEqual(
            "default-position-3", arg1_3.getKey(), "testDefaultOnePosition(5) "
        )

    def testDefaultOnePosition_test11_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Retrieve and assert the first argument
        arg1_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg1_0.getKey(), "testDefaultOnePosition(2) "
        )

        # Assert the second argument is None
        self.assertIsNone(
            self._field.getArg1("required", 1), "testDefaultOnePosition(3) "
        )

        # Retrieve and assert the third argument
        arg1_2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2", arg1_2.getKey(), "testDefaultOnePosition(4) "
        )

        # Retrieve the fourth argument (no assertion needed as per the original code)
        self._field.getArg1("required", 3)

    def testDefaultOnePosition_test10_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments in the "required" key
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Retrieve and assert the first argument
        arg1_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg1_0.getKey(), "testDefaultOnePosition(2) "
        )

        # Assert the second argument is None
        self.assertIsNone(
            self._field.getArg1("required", 1), "testDefaultOnePosition(3) "
        )

        # Retrieve and assert the third argument
        arg1_2 = self._field.getArg1("required", 2)
        self.assertEqual(
            "default-position-2", arg1_2.getKey(), "testDefaultOnePosition(4) "
        )

    def testDefaultOnePosition_test9_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments in the "required" key
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Retrieve and assert the first argument's key
        arg1_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg1_0.getKey(), "testDefaultOnePosition(2) "
        )

        # Assert that the second argument is None
        self.assertIsNone(
            self._field.getArg1("required", 1), "testDefaultOnePosition(3) "
        )

        # Retrieve the third argument (no assertion needed as per the original code)
        self._field.getArg1("required", 2)

    def testDefaultOnePosition_test8_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Retrieve and assert the key of the first argument
        arg = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg.getKey(), "testDefaultOnePosition(2) "
        )

    def testDefaultOnePosition_test7_decomposed(self) -> None:
        # Create and add the first argument
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        # Create and add the second argument
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        # Create and add the third argument
        arg0_2 = self.__createArg0("default-position-3")
        self._field.addArg(arg0_2)

        # Assert the number of arguments in the "required" category
        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

        # Retrieve the first argument in the "required" category
        self._field.getArg1("required", 0)

    def testDefaultOnePosition_test6_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        arg2 = self.__createArg0("default-position-3")
        self._field.addArg(arg2)

        self.assertEqual(
            4, len(self._field.getArgs("required")), "testDefaultOnePosition(1) "
        )

    def testDefaultOnePosition_test5_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

        arg2 = self.__createArg0("default-position-3")
        self._field.addArg(arg2)

    def testDefaultOnePosition_test4_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)
        self.__createArg0("default-position-3")

    def testDefaultOnePosition_test3_decomposed(self) -> None:
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg1)

    def testDefaultOnePosition_test2_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg1("default-position-2", 2)

    def testDefaultOnePosition_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testDefaultOnePosition_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testDefaultUsingPositions_test12_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)
        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)
        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments in the field
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

        # Assert the key of the first argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultUsingPositions(2) ",
        )

        # Assert the key of the second argument
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultUsingPositions(3) ",
        )

        # Assert the key of the third argument
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testDefaultUsingPositions(4) ",
        )

    def testDefaultUsingPositions_test11_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)
        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)
        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments added
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

        # Validate the key of the first argument
        arg_at_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg_at_0.getKey(), "testDefaultUsingPositions(2) "
        )

        # Validate the key of the second argument
        arg_at_1 = self._field.getArg1("required", 1)
        self.assertEqual(
            "default-position-1", arg_at_1.getKey(), "testDefaultUsingPositions(3) "
        )

        # Validate the third argument exists (no assertion needed in Java code)
        arg_at_2 = self._field.getArg1("required", 2)

    def testDefaultUsingPositions_test10_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments in the field
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

        # Assert the key of the first argument
        arg_at_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", arg_at_0.getKey(), "testDefaultUsingPositions(2) "
        )

        # Assert the key of the second argument
        arg_at_1 = self._field.getArg1("required", 1)
        self.assertEqual(
            "default-position-1", arg_at_1.getKey(), "testDefaultUsingPositions(3) "
        )

    def testDefaultUsingPositions_test9_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments added
        self.assertEqual(
            len(self._field.getArgs("required")), 3, "testDefaultUsingPositions(1) "
        )

        # Assert the key of the argument at position 0
        arg_at_position_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            arg_at_position_0.getKey(),
            "default-position-0",
            "testDefaultUsingPositions(2) ",
        )

        # Retrieve the argument at position 1 (no assertion here, just retrieval)
        self._field.getArg1("required", 1)

    def testDefaultUsingPositions_test8_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments in the field
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

        # Assert the key of the first argument
        first_arg = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0", first_arg.getKey(), "testDefaultUsingPositions(2) "
        )

    def testDefaultUsingPositions_test7_decomposed(self) -> None:
        # Create and add arguments to the field
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        # Assert the number of arguments with the key "required"
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

        # Retrieve an argument by key and position
        self._field.getArg1("required", 0)

    def testDefaultUsingPositions_test6_decomposed(self) -> None:
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultUsingPositions(1) "
        )

    def testDefaultUsingPositions_test5_decomposed(self) -> None:
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)
        self._field.addArg(arg3)

    def testDefaultUsingPositions_test4_decomposed(self) -> None:
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)

        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

        arg3 = self.__createArg1("default-position-2", 2)

    def testDefaultUsingPositions_test3_decomposed(self) -> None:
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)
        arg2 = self.__createArg1("default-position-0", 0)
        self._field.addArg(arg2)

    def testDefaultUsingPositions_test2_decomposed(self) -> None:
        arg1 = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg1)
        self.__createArg1("default-position-0", 0)

    def testDefaultUsingPositions_test1_decomposed(self) -> None:
        self._field = Field()
        arg = self.__createArg1("default-position-1", 1)
        self._field.addArg(arg)

    def testDefaultUsingPositions_test0_decomposed(self) -> None:
        self.__createArg1("default-position-1", 1)

    def testDefaultPositionImplied_test12_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg0("default-position-1")
        self._field.addArg(arg1)
        arg2 = self.__createArg0("default-position-2")
        self._field.addArg(arg2)

        # Assert the number of arguments added
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

        # Assert the key of each argument
        self.assertEqual(
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
            "testDefaultPositionImplied(2) ",
        )
        self.assertEqual(
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
            "testDefaultPositionImplied(3) ",
        )
        self.assertEqual(
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
            "testDefaultPositionImplied(4) ",
        )

    def testDefaultPositionImplied_test11_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg0("default-position-1")
        self._field.addArg(arg1)
        arg2 = self.__createArg0("default-position-2")
        self._field.addArg(arg2)

        # Assert the number of arguments added
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

        # Assert the key of the first argument
        arg0_key = self._field.getArg1("required", 0).getKey()
        self.assertEqual(
            "default-position-0", arg0_key, "testDefaultPositionImplied(2) "
        )

        # Assert the key of the second argument
        arg1_key = self._field.getArg1("required", 1).getKey()
        self.assertEqual(
            "default-position-1", arg1_key, "testDefaultPositionImplied(3) "
        )

        # Access the third argument (no assertion needed as per the original code)
        self._field.getArg1("required", 2)

    def testDefaultPositionImplied_test10_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg0("default-position-1")
        self._field.addArg(arg1)
        arg2 = self.__createArg0("default-position-2")
        self._field.addArg(arg2)

        # Assert the number of arguments added
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

        # Assert the key of the first argument
        arg0_key = self._field.getArg1("required", 0).getKey()
        self.assertEqual(
            "default-position-0", arg0_key, "testDefaultPositionImplied(2) "
        )

        # Assert the key of the second argument
        arg1_key = self._field.getArg1("required", 1).getKey()
        self.assertEqual(
            "default-position-1", arg1_key, "testDefaultPositionImplied(3) "
        )

    def testDefaultPositionImplied_test9_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

        arg1 = self.__createArg0("default-position-1")
        self._field.addArg(arg1)

        arg2 = self.__createArg0("default-position-2")
        self._field.addArg(arg2)

        # Assert the number of arguments added
        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

        # Assert the key of the first argument
        arg_at_position_0 = self._field.getArg1("required", 0)
        self.assertEqual(
            "default-position-0",
            arg_at_position_0.getKey(),
            "testDefaultPositionImplied(2) ",
        )

        # Access the second argument (no assertion here, just accessing)
        self._field.getArg1("required", 1)

    def testDefaultPositionImplied_test8_decomposed(self) -> None:
        # Create and add arguments to the field
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        arg1 = self.__createArg0("default-position-1")
        self._field.addArg(arg1)
        arg2 = self.__createArg0("default-position-2")
        self._field.addArg(arg2)

        # Assert the number of arguments added
        self.assertEqual(
            len(self._field.getArgs("required")), 3, "testDefaultPositionImplied(1) "
        )

        # Assert the key of the first argument
        first_arg = self._field.getArg1("required", 0)
        self.assertEqual(
            first_arg.getKey(), "default-position-0", "testDefaultPositionImplied(2) "
        )

    def testDefaultPositionImplied_test7_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

        self._field.getArg1("required", 0)

    def testDefaultPositionImplied_test6_decomposed(self) -> None:
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

        arg0_3 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_3)

        self.assertEqual(
            3, len(self._field.getArgs("required")), "testDefaultPositionImplied(1) "
        )

    def testDefaultPositionImplied_test5_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)

        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)

        arg0_2 = self.__createArg0("default-position-2")
        self._field.addArg(arg0_2)

    def testDefaultPositionImplied_test4_decomposed(self) -> None:
        arg0_0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_0)
        arg0_1 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_1)
        arg0_2 = self.__createArg0("default-position-2")

    def testDefaultPositionImplied_test3_decomposed(self) -> None:
        arg0_1 = self.__createArg0("default-position-0")
        self._field.addArg(arg0_1)
        arg0_2 = self.__createArg0("default-position-1")
        self._field.addArg(arg0_2)

    def testDefaultPositionImplied_test2_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)
        self.__createArg0("default-position-1")

    def testDefaultPositionImplied_test1_decomposed(self) -> None:
        self._field = Field()
        arg0 = self.__createArg0("default-position-0")
        self._field.addArg(arg0)

    def testDefaultPositionImplied_test0_decomposed(self) -> None:
        self.__createArg0("default-position-0")

    def testEmptyArgs_test0_decomposed(self) -> None:
        self._field = Field()  # Initialize the Field object
        self.assertEqual(0, len(self._field.getArgs("required")), "Empty Args(1) ")

    def tearDown(self) -> None:
        self._field = None

    def setUp(self) -> None:
        self._field = Field()

    @staticmethod
    def FieldTest1() -> FieldTest:
        return FieldTest(None)

    def __createArg3(self, key: str, name: str, position: int) -> Arg:
        arg = self.__createArg2(key, name)
        arg.setPosition(position)
        return arg

    def __createArg2(self, key: str, name: str) -> Arg:
        arg = self.__createArg0(key)
        arg.setName(name)
        return arg

    def __createArg1(self, key: str, position: int) -> Arg:
        arg = self.__createArg0(key)
        arg.setPosition(position)
        return arg

    def __createArg0(self, key: str) -> Arg:
        arg = Arg()
        arg.setKey(key)
        return arg
