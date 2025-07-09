from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *


class CharSequenceUtilsTest(unittest.TestCase):

    __TEST_DATA: typing.List[TestData] = None

    @staticmethod
    def initialize_fields() -> None:
        CharSequenceUtilsTest.__TEST_DATA: typing.List[TestData] = [
            TestData(1, True, 0, "a", None, 0, True, "abc", 0),
            TestData(1, True, 0, "a", None, 0, True, "abc", 1),
            TestData(1, True, 0, "Abc", None, 0, True, "abc", 3),
            TestData(1, False, 0, "Abc", None, 0, False, "abc", 3),
            TestData(1, True, 1, "Abc", None, 1, True, "abc", 2),
            TestData(1, True, 1, "Abc", None, 1, False, "abc", 2),
            TestData(1, True, 1, "Abcd", None, 1, True, "abcD", 2),
            TestData(1, True, 1, "Abcd", None, 1, False, "abcD", 2),
        ]

    def testConstructor_test0_decomposed(self) -> None:
        CharSequenceUtils()

    def testRegionMatches_test0_decomposed(self) -> None:
        for data in self.__TEST_DATA:

            class RunTestString(RunTest):
                def invoke(self) -> bool:
                    return (
                        data.source[data.toffset : data.toffset + data.len].lower()
                        == data.other[data.ooffset : data.ooffset + data.len].lower()
                        if data.ignoreCase
                        else data.source[data.toffset : data.toffset + data.len]
                        == data.other[data.ooffset : data.ooffset + data.len]
                    )

            RunTestString().run(data, "String")

            class RunTestCSString(RunTest):
                def invoke(self) -> bool:
                    return CharSequenceUtils.region_matches(
                        data.source,
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )

            RunTestCSString().run(data, "CSString")

            class RunTestCSNonString(RunTest):
                def invoke(self) -> bool:
                    return CharSequenceUtils.region_matches(
                        str(data.source),
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )

            RunTestCSNonString().run(data, "CSNonString")


class TestData:

    throwable: typing.Type[BaseException] = None

    expected: bool = False

    len: int = 0

    ooffset: int = 0

    other: str = ""

    toffset: int = 0

    ignoreCase: bool = False

    source: str = ""

    def toString(self) -> str:
        sb = []
        sb.append(f"{self.source}[{self.toffset}]")
        sb.append(" caseblind " if self.ignoreCase else " samecase ")
        sb.append(f"{self.other}[{self.ooffset}]")
        sb.append(f" {self.len} => ")
        if self.throwable is not None:
            sb.append(str(self.throwable))
        else:
            sb.append(str(self.expected))
        return "".join(sb)

    def __init__(
        self,
        constructorId: int,
        expected: bool,
        ooffset: int,
        source: str,
        throwable: typing.Type[BaseException],
        toffset: int,
        ignoreCase: bool,
        other: str,
        len_: int,
    ) -> None:
        if constructorId == 0:
            self.source = source
            self.ignoreCase = ignoreCase
            self.toffset = toffset
            self.other = other
            self.ooffset = ooffset
            self.len = len_
            self.expected = False
            self.throwable = throwable
        else:
            self.source = source
            self.ignoreCase = ignoreCase
            self.toffset = toffset
            self.other = other
            self.ooffset = ooffset
            self.len = len_
            self.expected = expected
            self.throwable = None


class RunTest(ABC):

    def run(self, data: TestData, id_: str) -> None:
        if data.throwable is not None:
            msg = f"{id_} Expected {data.throwable}"
            try:
                self.invoke()
                pytest.fail(f"{msg} but nothing was thrown.")
            except Exception as ex:
                assert issubclass(
                    ex.__class__, data.throwable
                ), f"{msg} but was {ex.__class__.__name__}"
        else:
            string_check = self.invoke()
            assert string_check == data.expected, f"{id_} Failed test {data}"

    def invoke(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")


CharSequenceUtilsTest.initialize_fields()
