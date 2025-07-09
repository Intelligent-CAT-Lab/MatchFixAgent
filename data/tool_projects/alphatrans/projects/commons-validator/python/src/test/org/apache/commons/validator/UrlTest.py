from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
from src.test.org.apache.commons.validator.ResultPair import *
from src.main.org.apache.commons.validator.UrlValidator import *


class UrlTest(unittest.TestCase):

    __printIndex: bool = False
    __printStatus: bool = False
    testScheme: typing.List[ResultPair] = [
        ResultPair("http", True),
        ResultPair("ftp", False),
        ResultPair("httpd", False),
        ResultPair("telnet", False),
    ]
    testPartsIndex: typing.List[int] = [0, 0, 0, 0, 0]
    testUrlQuery: typing.List[ResultPair] = [
        ResultPair("?action=view", True),
        ResultPair("?action=edit&mode=up", True),
        ResultPair("", True),
    ]
    testUrlPathOptions: typing.List[ResultPair] = [
        ResultPair("/test1", True),
        ResultPair("/t123", True),
        ResultPair("/$23", True),
        ResultPair("/..", False),
        ResultPair("/../", False),
        ResultPair("/test1/", True),
        ResultPair("/#", False),
        ResultPair("", True),
        ResultPair("/test1/file", True),
        ResultPair("/t123/file", True),
        ResultPair("/$23/file", True),
        ResultPair("/../file", False),
        ResultPair("/..//file", False),
        ResultPair("/test1//file", True),
        ResultPair("/#/file", False),
    ]
    testPath: typing.List[ResultPair] = [
        ResultPair("/test1", True),
        ResultPair("/t123", True),
        ResultPair("/$23", True),
        ResultPair("/..", False),
        ResultPair("/../", False),
        ResultPair("/test1/", True),
        ResultPair("", True),
        ResultPair("/test1/file", True),
        ResultPair("/..//file", False),
        ResultPair("/test1//file", False),
    ]
    testUrlPort: typing.List[ResultPair] = [
        ResultPair(":80", True),
        ResultPair(":65535", True),
        ResultPair(":0", True),
        ResultPair("", True),
        ResultPair(":-1", False),
        ResultPair(":65636", True),
        ResultPair(":65a", False),
    ]
    testUrlAuthority: typing.List[ResultPair] = [
        ResultPair("www.google.com", True),
        ResultPair("go.com", True),
        ResultPair("go.au", True),
        ResultPair("0.0.0.0", True),
        ResultPair("255.255.255.255", True),
        ResultPair("256.256.256.256", False),
        ResultPair("255.com", True),
        ResultPair("1.2.3.4.5", False),
        ResultPair("1.2.3.4.", False),
        ResultPair("1.2.3", False),
        ResultPair(".1.2.3.4", False),
        ResultPair("go.a", False),
        ResultPair("go.a1a", True),
        ResultPair("go.1aa", False),
        ResultPair("aaa.", False),
        ResultPair(".aaa", False),
        ResultPair("aaa", False),
        ResultPair("", False),
    ]
    testUrlScheme: typing.List[ResultPair] = [
        ResultPair("http://", True),
        ResultPair("ftp://", True),
        ResultPair("h3t://", True),
        ResultPair("3ht://", False),
        ResultPair("http:/", False),
        ResultPair("http:", False),
        ResultPair("http/", False),
        ResultPair("://", False),
        ResultPair("", True),
    ]
    testUrlPartsOptions: typing.List[typing.Any] = [
        testUrlScheme,
        testUrlAuthority,
        testUrlPort,
        testUrlPathOptions,
        testUrlQuery,
    ]
    testUrlParts: typing.List[typing.Any] = [
        testUrlScheme,
        testUrlAuthority,
        testUrlPort,
        testPath,
        testUrlQuery,
    ]

    def testValidateUrl_test0_decomposed(self) -> None:
        self.assertTrue(True)

    def testValidator204_test1_decomposed(self) -> None:
        schemes = ["http", "https"]
        url_validator = UrlValidator.UrlValidator2(schemes)
        self.assertTrue(
            url_validator.isValid(
                "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"
            )
        )

    def testValidator204_test0_decomposed(self) -> None:
        schemes = ["http", "https"]
        url_validator = UrlValidator.UrlValidator2(schemes)

    def testValidator202_test1_decomposed(self) -> None:
        schemes = ["http", "https"]
        url_validator = UrlValidator(schemes, UrlValidator.NO_FRAGMENTS)
        result = url_validator.isValid(
            "http://www.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.logoworks.comwww.log"
        )
        # You can add assertions here if needed, for example:
        # self.assertFalse(result)

    def testValidator202_test0_decomposed(self) -> None:
        schemes = ["http", "https"]
        url_validator = UrlValidator(schemes, UrlValidator.NO_FRAGMENTS)

    def testIsValidScheme_test2_decomposed(self) -> None:
        if self.__printStatus:
            print("\n testIsValidScheme() ")

        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)

        for testPair in self.testScheme:
            result = urlVal._isValidScheme(testPair.item)
            self.assertEqual(
                testPair.valid, result, f"Failed for scheme: {testPair.item}"
            )

            if self.__printStatus:
                if result == testPair.valid:
                    print(".", end="")
                else:
                    print("X", end="")

        if self.__printStatus:
            print()

    def testIsValidScheme_test1_decomposed(self) -> None:
        if self.__printStatus:
            print("\n testIsValidScheme() ")

        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)

        for testPair in self.testScheme:
            result = urlVal._isValidScheme(testPair.item)
            self.assertEqual(
                testPair.valid, result, f"Failed for scheme: {testPair.item}"
            )

            if self.__printStatus:
                if result == testPair.valid:
                    print(".", end="")
                else:
                    print("X", end="")

    def testIsValidScheme_test0_decomposed(self) -> None:
        if self.__printStatus:
            print("\n testIsValidScheme() ")
        schemes = ["http", "gopher"]
        urlVal = UrlValidator(schemes, 0)

    def testIsValid0_test2_decomposed(self) -> None:
        self.testIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()
        options = (
            UrlValidator.ALLOW_2_SLASHES
            + UrlValidator.ALLOW_ALL_SCHEMES
            + UrlValidator.NO_FRAGMENTS
        )
        self.testIsValid1(self.testUrlPartsOptions, options)

    def testIsValid0_test1_decomposed(self) -> None:
        self.testIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)
        self.setUp()

    def testIsValid0_test0_decomposed(self) -> None:
        self.testIsValid1(self.testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES)

    def setUp(self) -> None:
        for index in range(len(self.testPartsIndex) - 1):
            self.testPartsIndex[index] = 0

    @staticmethod
    def main(argv: typing.List[str]) -> None:
        fct = UrlTest("url test")
        fct.setUp()
        fct.testIsValid0_test2_decomposed()
        fct.testIsValidScheme_test2_decomposed()

    @staticmethod
    def incrementTestPartsIndex(
        testPartsIndex: typing.List[int], testParts: typing.List[typing.Any]
    ) -> bool:
        carry = True  # Add 1 to the lowest order part
        maxIndex = True

        for testPartsIndexIndex in range(
            len(testPartsIndex) - 1, -1, -1
        ):  # Iterate in reverse
            index = testPartsIndex[testPartsIndexIndex]
            part = testParts[
                testPartsIndexIndex
            ]  # Assuming testParts contains lists or similar iterable objects

            if carry:
                if index < len(part) - 1:
                    index += 1
                    testPartsIndex[testPartsIndexIndex] = index
                    carry = False
                else:
                    testPartsIndex[testPartsIndexIndex] = 0
                    carry = True

            maxIndex &= index == (len(part) - 1)

        return not maxIndex

    def testIsValid1(self, testObjects: typing.List[typing.Any], options: int) -> None:
        urlVal = UrlValidator(None, options)
        self.assertTrue(urlVal.isValid("http://www.google.com"))
        self.assertTrue(urlVal.isValid("http://www.google.com/"))

        statusPerLine = 60
        printed = 0
        if self.__printIndex:
            statusPerLine = 6

        while True:
            testBuffer = []
            expected = True
            for testPartsIndexIndex in range(len(self.testPartsIndex)):
                index = self.testPartsIndex[testPartsIndexIndex]
                part = testObjects[testPartsIndexIndex]
                testBuffer.append(part[index].item)
                expected = expected and part[index].valid

            url = "".join(testBuffer)
            result = urlVal.isValid(url)
            self.assertEqual(expected, result, url)

            if self.__printStatus:
                if self.__printIndex:
                    print(self.__testPartsIndextoString(), end="")
                else:
                    if result == expected:
                        print(".", end="")
                    else:
                        print("X", end="")

                printed += 1
                if printed == statusPerLine:
                    print()
                    printed = 0

            if not self.incrementTestPartsIndex(self.testPartsIndex, testObjects):
                break

        if self.__printStatus:
            print()

    def __testPartsIndextoString(self) -> str:
        carry_msg = "{"
        for test_parts_index_index in range(len(self.testPartsIndex)):
            carry_msg += str(self.testPartsIndex[test_parts_index_index])
            if test_parts_index_index < len(self.testPartsIndex) - 1:
                carry_msg += ","
            else:
                carry_msg += "}"
        return carry_msg
