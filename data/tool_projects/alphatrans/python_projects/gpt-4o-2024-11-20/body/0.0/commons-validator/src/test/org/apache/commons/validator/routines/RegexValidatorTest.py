from __future__ import annotations
import re
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.routines.RegexValidator import *


class RegexValidatorTest(unittest.TestCase):

    __SEPARATOR_2: str = r"(?:\s)"
    __SEPARATOR_1: str = r"(?:\-)"
    __COMPONENT_3: str = "([123]{3})"
    __COMPONENT_2: str = "([DEF]{3})"
    __COMPONENT_1: str = "([abc]{3})"
    __REGEX: str = r"^([abc]*)(?:\-)([DEF]*)(?:\-)([123]*)$"
    __REGEX_3: str = None
    __REGEX_2: str = None
    __REGEX_1: str = None
    __MULTIPLE_REGEX: List[str] = [__REGEX_1, __REGEX_2, __REGEX_3]

    @staticmethod
    def initialize_fields() -> None:
        RegexValidatorTest.__REGEX_3: str = (
            f"^{RegexValidatorTest.__COMPONENT_1}{RegexValidatorTest.__COMPONENT_2}{RegexValidatorTest.__COMPONENT_3}$"
        )

        RegexValidatorTest.__REGEX_2: str = (
            f"^{RegexValidatorTest.__COMPONENT_1}{RegexValidatorTest.__SEPARATOR_2}{RegexValidatorTest.__COMPONENT_2}{RegexValidatorTest.__SEPARATOR_2}{RegexValidatorTest.__COMPONENT_3}$"
        )

        RegexValidatorTest.__REGEX_1: str = (
            f"^{RegexValidatorTest.__COMPONENT_1}{RegexValidatorTest.__SEPARATOR_1}{RegexValidatorTest.__COMPONENT_2}{RegexValidatorTest.__SEPARATOR_1}{RegexValidatorTest.__COMPONENT_3}$"
        )

    def testToString_test3_decomposed(self) -> None:
        single = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(
            f"RegexValidator{{{self.__REGEX}}}", single.toString(), "Single"
        )

        multiple = RegexValidator.RegexValidator1([self.__REGEX, self.__REGEX])
        self.assertEqual(
            f"RegexValidator{{{self.__REGEX},{self.__REGEX}}}",
            multiple.toString(),
            "Multiple",
        )

    def testToString_test2_decomposed(self) -> None:
        single = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(
            f"RegexValidator{{{self.__REGEX}}}", single.toString(), "Single"
        )

        multiple = RegexValidator.RegexValidator1([self.__REGEX, self.__REGEX])

    def testToString_test1_decomposed(self) -> None:
        single = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(
            f"RegexValidator{{{self.__REGEX}}}", single.toString(), "Single"
        )

    def testToString_test0_decomposed(self) -> None:
        single = RegexValidator.RegexValidator3(self.__REGEX)

    def testExceptions_test0_decomposed(self) -> None:
        invalid_regex = "^([abCD12]*$"
        with self.assertRaises(
            re.error
        ):  # re.error is raised for invalid regex patterns in Python
            RegexValidator.RegexValidator3(invalid_regex)

    def testMissingRegex_test3_decomposed(self) -> None:
        with pytest.raises(ValueError, match="Regular expression\\[0\\] is missing"):
            RegexValidator.RegexValidator3(None)

        with pytest.raises(ValueError, match="Regular expression\\[0\\] is missing"):
            RegexValidator.RegexValidator3("")

        with pytest.raises(ValueError, match="Regular expressions are missing"):
            RegexValidator.RegexValidator1(None)

        with pytest.raises(ValueError, match="Regular expressions are missing"):
            RegexValidator.RegexValidator1([])

        expressions = ["ABC", None]
        with pytest.raises(ValueError, match="Regular expression\\[1\\] is missing"):
            RegexValidator.RegexValidator1(expressions)

        expressions = ["", "ABC"]
        with pytest.raises(ValueError, match="Regular expression\\[0\\] is missing"):
            RegexValidator.RegexValidator1(expressions)

    def testMissingRegex_test2_decomposed(self) -> None:
        with pytest.raises(
            ValueError, match="Regular expression\\[0\\] is missing"
        ) as excinfo:
            RegexValidator.RegexValidator3(None)
        assert str(excinfo.value) == "Regular expression[0] is missing"

        with pytest.raises(
            ValueError, match="Regular expression\\[0\\] is missing"
        ) as excinfo:
            RegexValidator.RegexValidator3("")
        assert str(excinfo.value) == "Regular expression[0] is missing"

        with pytest.raises(
            ValueError, match="Regular expressions are missing"
        ) as excinfo:
            RegexValidator.RegexValidator1(None)
        assert str(excinfo.value) == "Regular expressions are missing"

        with pytest.raises(
            ValueError, match="Regular expressions are missing"
        ) as excinfo:
            RegexValidator.RegexValidator1([])
        assert str(excinfo.value) == "Regular expressions are missing"

        expressions = ["ABC", None]
        with pytest.raises(
            ValueError, match="Regular expression\\[1\\] is missing"
        ) as excinfo:
            RegexValidator.RegexValidator1(expressions)
        assert str(excinfo.value) == "Regular expression[1] is missing"

    def testMissingRegex_test1_decomposed(self) -> None:
        with pytest.raises(ValueError) as excinfo:
            RegexValidator.RegexValidator3(None)
        self.assertEqual("Regular expression[0] is missing", str(excinfo.value))

        with pytest.raises(ValueError) as excinfo:
            RegexValidator.RegexValidator3("")
        self.assertEqual("Regular expression[0] is missing", str(excinfo.value))

        with pytest.raises(ValueError) as excinfo:
            RegexValidator.RegexValidator1(None)
        self.assertEqual("Regular expressions are missing", str(excinfo.value))

        with pytest.raises(ValueError) as excinfo:
            RegexValidator.RegexValidator1([])
        self.assertEqual("Regular expressions are missing", str(excinfo.value))

    def testMissingRegex_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator3(None)
        self.assertEqual(
            "Regular expression[0] is missing", str(context.exception), "Single Null"
        )

        with self.assertRaises(ValueError) as context:
            RegexValidator.RegexValidator3("")
        self.assertEqual(
            "Regular expression[0] is missing",
            str(context.exception),
            "Single Zero Length",
        )

    def testNullValue_test3_decomposed(self) -> None:
        validator = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(False, validator.isValid(None), "Instance isValid()")
        self.assertEqual(None, validator.validate(None), "Instance validate()")
        self.assertEqual(None, validator.match(None), "Instance match()")

    def testNullValue_test2_decomposed(self) -> None:
        validator = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(False, validator.isValid(None), "Instance isValid()")
        self.assertEqual(None, validator.validate(None), "Instance validate()")

    def testNullValue_test1_decomposed(self) -> None:
        validator = RegexValidator.RegexValidator3(self.__REGEX)
        self.assertEqual(False, validator.isValid(None))

    def testNullValue_test0_decomposed(self) -> None:
        validator = RegexValidator.RegexValidator3(self.__REGEX)

    def testMultipleInsensitive_test15_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)

        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual(False, multiple.isValid(value), "isValid() Invalid")
        self.assertEqual(None, multiple.validate(value), "validate() Invalid")
        self.__checkArray("match() Multiple", None, multiple.match(value))

    def testMultipleInsensitive_test14_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)

        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual(False, multiple.isValid(value), "isValid() Invalid")
        self.assertEqual(None, multiple.validate(value), "validate() Invalid")

    def testMultipleInsensitive_test13_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)

        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "isValid() 3rd")

        self.assertEqual(multiple.validate(value), expect, "validate() Multiple")
        self.assertEqual(single1.validate(value), None, "validate() 1st")
        self.assertEqual(single2.validate(value), expect, "validate() 2nd")
        self.assertEqual(single3.validate(value), None, "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual(multiple.isValid(value), False, "isValid() Invalid")

    def testMultipleInsensitive_test12_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

    def testMultipleInsensitive_test11_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        # Assertions for match()
        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

    def testMultipleInsensitive_test10_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))

    def testMultipleInsensitive_test9_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        # Assertions for match()
        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))
        self.__checkArray("match() 2nd", array, single2.match(value))
        self.__checkArray("match() 3rd", None, single3.match(value))

    def testMultipleInsensitive_test8_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))

    def testMultipleInsensitive_test7_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))
        self.__checkArray("match() 1st", None, single1.match(value))

    def testMultipleInsensitive_test6_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "isValid() 3rd")

        self.assertEqual(expect, multiple.validate(value), "validate() Multiple")
        self.assertEqual(None, single1.validate(value), "validate() 1st")
        self.assertEqual(expect, single2.validate(value), "validate() 2nd")
        self.assertEqual(None, single3.validate(value), "validate() 3rd")

        self.__checkArray("match() Multiple", array, multiple.match(value))

    def testMultipleInsensitive_test5_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "isValid() 3rd")
        self.assertEqual(multiple.validate(value), expect, "validate() Multiple")
        self.assertEqual(single1.validate(value), None, "validate() 1st")
        self.assertEqual(single2.validate(value), expect, "validate() 2nd")
        self.assertEqual(single3.validate(value), None, "validate() 3rd")
        multiple.match(value)

    def testMultipleInsensitive_test4_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"

        # Simulating the array from Java, though it's not directly used in assertions
        array = ["AAC", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "isValid() 3rd")
        self.assertEqual(multiple.validate(value), expect, "validate() Multiple")
        self.assertEqual(single1.validate(value), None, "validate() 1st")
        self.assertEqual(single2.validate(value), expect, "validate() 2nd")
        self.assertEqual(single3.validate(value), None, "validate() 3rd")

    def testMultipleInsensitive_test3_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "isValid() 3rd")

    def testMultipleInsensitive_test2_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)
        value = "AAC FDE 321"
        expect = "AACFDE321"
        array = ["AAC", "FDE", "321"]
        self.assertEqual(multiple.isValid(value), True, "isValid() Multiple")

    def testMultipleInsensitive_test1_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)
        single1 = RegexValidator.RegexValidator2(self.__REGEX_1, False)
        single2 = RegexValidator.RegexValidator2(self.__REGEX_2, False)
        single3 = RegexValidator.RegexValidator2(self.__REGEX_3, False)

    def testMultipleInsensitive_test0_decomposed(self) -> None:
        multiple = RegexValidator(self.__MULTIPLE_REGEX, False)

    def testMultipleSensitive_test15_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)

        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "Sensitive isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "Sensitive isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "Sensitive isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "Sensitive isValid() 3rd")

        self.assertEqual(
            multiple.validate(value), expect, "Sensitive validate() Multiple"
        )
        self.assertEqual(single1.validate(value), None, "Sensitive validate() 1st")
        self.assertEqual(single2.validate(value), expect, "Sensitive validate() 2nd")
        self.assertEqual(single3.validate(value), None, "Sensitive validate() 3rd")

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual(multiple.isValid(value), False, "isValid() Invalid")
        self.assertEqual(multiple.validate(value), None, "validate() Invalid")
        self.__checkArray("match() Multiple", None, multiple.match(value))

    def testMultipleSensitive_test14_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "Sensitive isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "Sensitive isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "Sensitive isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "Sensitive isValid() 3rd")

        self.assertEqual(
            multiple.validate(value), expect, "Sensitive validate() Multiple"
        )
        self.assertEqual(single1.validate(value), None, "Sensitive validate() 1st")
        self.assertEqual(single2.validate(value), expect, "Sensitive validate() 2nd")
        self.assertEqual(single3.validate(value), None, "Sensitive validate() 3rd")

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

        value = "AAC*FDE*321"
        self.assertEqual(multiple.isValid(value), False, "isValid() Invalid")
        self.assertEqual(multiple.validate(value), None, "validate() Invalid")

    def testMultipleSensitive_test13_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        # Assertions for match()
        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

        # Test with an invalid value
        value = "AAC*FDE*321"
        self.assertEqual(False, multiple.isValid(value), "isValid() Invalid")

    def testMultipleSensitive_test12_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

    def testMultipleSensitive_test11_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        # Assertions for match()
        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))
        self.__checkArray("Sensitive match() 3rd", None, single3.match(value))

    def testMultipleSensitive_test10_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertIsNone(single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertIsNone(single3.validate(value), "Sensitive validate() 3rd")

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))

    def testMultipleSensitive_test9_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))
        self.__checkArray("Sensitive match() 2nd", array, single2.match(value))

    def testMultipleSensitive_test8_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        # Assertions for match()
        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        self.__checkArray("Sensitive match() 1st", None, single1.match(value))

    def testMultipleSensitive_test7_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        # Assertions for match()
        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))
        single1.match(value)  # This line is included but does not perform any assertion

    def testMultipleSensitive_test6_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        # Assertions for isValid()
        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")

        # Assertions for validate()
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

        # Assertions for match()
        self.__checkArray("Sensitive match() Multiple", array, multiple.match(value))

    def testMultipleSensitive_test5_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "Sensitive isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "Sensitive isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "Sensitive isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "Sensitive isValid() 3rd")

        self.assertEqual(
            multiple.validate(value), expect, "Sensitive validate() Multiple"
        )
        self.assertEqual(single1.validate(value), None, "Sensitive validate() 1st")
        self.assertEqual(single2.validate(value), expect, "Sensitive validate() 2nd")
        self.assertEqual(single3.validate(value), None, "Sensitive validate() 3rd")

        multiple.match(value)

    def testMultipleSensitive_test4_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(True, multiple.isValid(value), "Sensitive isValid() Multiple")
        self.assertEqual(False, single1.isValid(value), "Sensitive isValid() 1st")
        self.assertEqual(True, single2.isValid(value), "Sensitive isValid() 2nd")
        self.assertEqual(False, single3.isValid(value), "Sensitive isValid() 3rd")
        self.assertEqual(
            expect, multiple.validate(value), "Sensitive validate() Multiple"
        )
        self.assertEqual(None, single1.validate(value), "Sensitive validate() 1st")
        self.assertEqual(expect, single2.validate(value), "Sensitive validate() 2nd")
        self.assertEqual(None, single3.validate(value), "Sensitive validate() 3rd")

    def testMultipleSensitive_test3_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]

        self.assertEqual(multiple.isValid(value), True, "Sensitive isValid() Multiple")
        self.assertEqual(single1.isValid(value), False, "Sensitive isValid() 1st")
        self.assertEqual(single2.isValid(value), True, "Sensitive isValid() 2nd")
        self.assertEqual(single3.isValid(value), False, "Sensitive isValid() 3rd")

    def testMultipleSensitive_test2_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)
        value = "aac FDE 321"
        expect = "aacFDE321"
        array = ["aac", "FDE", "321"]
        self.assertEqual(multiple.isValid(value), True, "Sensitive isValid() Multiple")

    def testMultipleSensitive_test1_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)
        single1 = RegexValidator.RegexValidator3(self.__REGEX_1)
        single2 = RegexValidator.RegexValidator3(self.__REGEX_2)
        single3 = RegexValidator.RegexValidator3(self.__REGEX_3)

    def testMultipleSensitive_test0_decomposed(self) -> None:
        multiple = RegexValidator.RegexValidator1(self.__MULTIPLE_REGEX)

    def testSingle_test16_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

        # Additional RegexValidator3 tests
        validator = RegexValidator.RegexValidator3(r"^([A-Z]*)$")
        self.assertEqual("ABC", validator.validate("ABC"), "validate one")
        self.__checkArray("match one", ["ABC"], validator.match("ABC"))

    def testSingle_test15_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

        # Additional RegexValidator3 tests
        validator = RegexValidator.RegexValidator3(r"^([A-Z]*)$")
        self.assertEqual("ABC", validator.validate("ABC"), "validate one")
        self.__checkArray("match one", ["ABC"], validator.match("ABC"))

    def testSingle_test14_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

        # Additional RegexValidator3 test
        validator = RegexValidator.RegexValidator3(r"^([A-Z]*)$")
        self.assertEqual("ABC", validator.validate("ABC"), "validate one")

    def testSingle_test13_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

        # Additional RegexValidator3 test
        validator = RegexValidator.RegexValidator3(r"^([A-Z]*)$")
        self.assertEqual("ABC", validator.validate("ABC"), "validate one")

    def testSingle_test12_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

        # Additional test for RegexValidator3
        RegexValidator.RegexValidator3(r"^([A-Z]*)$")

    def testSingle_test11_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

    def testSingle_test10_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )
        self.__checkArray(
            "Insensitive match() invalid", None, insensitive.match("ABd-de-1")
        )

    def testSingle_test9_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )

    def testSingle_test8_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))
        self.__checkArray(
            "Insensitive match() valid", ["AB", "de", "1"], insensitive.match("AB-de-1")
        )

    def testSingle_test7_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))

    def testSingle_test6_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        # Testing isValid() method
        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        # Testing validate() method
        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

        # Testing match() method
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )
        self.__checkArray("Sensitive match() invalid", None, sensitive.match("AB-de-1"))

    def testSingle_test5_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        sensitive.match("ac-DE-1")
        self.__checkArray(
            "Sensitive match() valid", ["ac", "DE", "1"], sensitive.match("ac-DE-1")
        )

    def testSingle_test4_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

        self.assertEqual(
            "acDE1", sensitive.validate("ac-DE-1"), "Sensitive validate() valid"
        )
        self.assertEqual(
            None, sensitive.validate("AB-de-1"), "Sensitive validate() invalid"
        )
        self.assertEqual(
            "ABde1", insensitive.validate("AB-de-1"), "Insensitive validate() valid"
        )
        self.assertEqual(
            None, insensitive.validate("ABd-de-1"), "Insensitive validate() invalid"
        )

        sensitive.match("ac-DE-1")

    def testSingle_test3_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        self.assertEqual(
            sensitive.isValid("ac-DE-1"), True, "Sensitive isValid() valid"
        )
        self.assertEqual(
            sensitive.isValid("AB-de-1"), False, "Sensitive isValid() invalid"
        )
        self.assertEqual(
            insensitive.isValid("AB-de-1"), True, "Insensitive isValid() valid"
        )
        self.assertEqual(
            insensitive.isValid("ABd-de-1"), False, "Insensitive isValid() invalid"
        )

        self.assertEqual(
            sensitive.validate("ac-DE-1"), "acDE1", "Sensitive validate() valid"
        )
        self.assertEqual(
            sensitive.validate("AB-de-1"), None, "Sensitive validate() invalid"
        )
        self.assertEqual(
            insensitive.validate("AB-de-1"), "ABde1", "Insensitive validate() valid"
        )
        self.assertEqual(
            insensitive.validate("ABd-de-1"), None, "Insensitive validate() invalid"
        )

    def testSingle_test2_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

        self.assertEqual(
            True, sensitive.isValid("ac-DE-1"), "Sensitive isValid() valid"
        )
        self.assertEqual(
            False, sensitive.isValid("AB-de-1"), "Sensitive isValid() invalid"
        )
        self.assertEqual(
            True, insensitive.isValid("AB-de-1"), "Insensitive isValid() valid"
        )
        self.assertEqual(
            False, insensitive.isValid("ABd-de-1"), "Insensitive isValid() invalid"
        )

    def testSingle_test1_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)
        insensitive = RegexValidator.RegexValidator2(self.__REGEX, False)

    def testSingle_test0_decomposed(self) -> None:
        sensitive = RegexValidator.RegexValidator3(self.__REGEX)

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:
        super().setUp()

    def __checkArray(
        self, label: str, expect: Optional[List[str]], result: Optional[List[str]]
    ) -> None:
        if expect is None or result is None:
            if expect is None and result is None:
                return  # valid, both are None
            else:
                pytest.fail(f"{label} Null expect={expect} result={result}")
            return  # not strictly necessary, but prevents possible issues below

        if len(expect) != len(result):
            pytest.fail(f"{label} Length expect={len(expect)} result={len(result)}")

        for i in range(len(expect)):
            self.assertEqual(expect[i], result[i], f"{label} value[{i}]")


RegexValidatorTest.initialize_fields()
