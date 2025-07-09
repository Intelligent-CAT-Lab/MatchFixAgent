from __future__ import annotations
import time
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest


class CacheSubSequencePerformanceTest(unittest.TestCase):

    def test0_test5_decomposed(self) -> None:
        times = 10000000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1(io.StringIO("Angelo"), times)
        print("Test with cached String : ", end="")
        self.__cacheSubSequence("Angelo")
        self.__test1(self.__cacheSubSequence("Angelo"), times)
        print("Test with cached StringBuilder : ", end="")
        self.__cacheSubSequence(io.StringIO("Angelo"))
        self.__test1(self.__cacheSubSequence(io.StringIO("Angelo")), times)

    def test0_test4_decomposed(self) -> None:
        times = 10_000_000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1(
            "Angelo", times
        )  # Python strings are immutable, so StringBuilder is not needed
        print("Test with cached String : ", end="")
        cached_string = self.__cacheSubSequence("Angelo")
        self.__test1(cached_string, times)
        print("Test with cached StringBuilder : ", end="")
        cached_string_builder = self.__cacheSubSequence("Angelo")
        self.__test1(cached_string_builder, times)

    def test0_test3_decomposed(self) -> None:
        times = 10000000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1(
            "Angelo", times
        )  # In Python, strings are mutable, so StringBuilder is not needed
        print("Test with cached String : ", end="")
        cached = self.__cacheSubSequence("Angelo")
        self.__test1(cached.subSequence(0, len("Angelo")), times)

    def test0_test2_decomposed(self) -> None:
        times = 10_000_000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1(
            "Angelo", times
        )  # In Python, we use strings directly instead of StringBuilder
        print("Test with cached String : ", end="")
        self.__cacheSubSequence("Angelo")

    def test0_test1_decomposed(self) -> None:
        times = 10000000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)
        print("Test with StringBuilder : ", end="")
        self.__test1("Angelo", times)

    def test0_test0_decomposed(self) -> None:
        times = 10000000
        print("Test with String : ", end="")
        self.__test1("Angelo", times)

    def __cacheSubSequence(self, cached: str) -> str:
        cache = [[None for _ in range(len(cached))] for _ in range(len(cached))]

        class CachedCharSequence:
            def __init__(self, cached: str):
                self.cached = cached

            def charAt(self, index: int) -> str:
                return self.cached[index]

            def length(self) -> int:
                return len(self.cached)

            def subSequence(self, start: int, end: int) -> str:
                if start == end:
                    return ""
                if cache[start][end - 1] is None:
                    cache[start][end - 1] = self.cached[start:end]
                return cache[start][end - 1]

        return CachedCharSequence(cached)

    def __test2(self, input_: str) -> None:
        for i in range(len(input_)):
            for j in range(i, len(input_) + 1):
                input_[i:j]

    def __test1(self, input_: str, times: int) -> None:
        begin_time_millis = int(round(time.time() * 1000))
        for _ in range(times):
            self.__test2(input_)
        print(f"{int(round(time.time() * 1000)) - begin_time_millis} millis")
