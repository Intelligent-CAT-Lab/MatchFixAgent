from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEnginePerformanceTest(unittest.TestCase):

    __LOOP: int = 80000

    def test_test2_decomposed(self) -> None:
        engine = PhoneticEngine.PhoneticEngine0(NameType.GENERIC, RuleType.APPROX, True)
        input_ = "Angelo"
        start_millis = int(round(time.time() * 1000))
        for _ in range(self.__LOOP):
            engine.encode0(input_)
        total_millis = int(round(time.time() * 1000)) - start_millis
        print(
            f"Time for encoding {self.__LOOP:,} times the input '{input_}': {total_millis:,} millis."
        )

    def test_test1_decomposed(self) -> None:
        engine = PhoneticEngine.PhoneticEngine0(NameType.GENERIC, RuleType.APPROX, True)
        input_ = "Angelo"
        start_millis = int(round(time.time() * 1000))
        for _ in range(self.__LOOP):
            engine.encode0(input_)

    def test_test0_decomposed(self) -> None:
        engine = PhoneticEngine.PhoneticEngine0(NameType.GENERIC, RuleType.APPROX, True)
