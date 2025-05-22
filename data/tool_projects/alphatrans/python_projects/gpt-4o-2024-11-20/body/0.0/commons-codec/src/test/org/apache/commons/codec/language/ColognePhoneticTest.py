from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.ColognePhonetic import *


class ColognePhoneticTest(StringEncoderAbstractTest, unittest.TestCase):

    __MATCHES: typing.List[str] = [
        ".*[AEIOUJY].*",  # A, E, I, J, O, U, Y
        ".*H.*",  # H
        ".*B.*",  # B
        ".*P[^H].*",  # P not before H
        ".*[DT][^CSZ].*",  # D, T not before C, S, Z
        ".*[FVW].*",  # F, V, W
        ".*PH.*",  # P before H
        ".*[GKQ].*",  # G, K, Q
        "C[AHKLOQRUX].*",  # Initial C before A, H, K, L, O, Q, R, U, X
        ".*[^SZ]C[AHKLOQRUX].*",  # C before A, H, K, L, O, Q, R, U, X but not after S, Z
        ".*[^CKQ]X.*",  # X not after C, K, Q
        ".*L.*",  # L
        ".*[MN].*",  # M, N
        ".*R.*",  # R
        ".*[SZ].*",  # S, Z
        ".*[SZ]C.*",  # C after S, Z
        "C[^AHKLOQRUX].*",  # Initial C except before A, H, K, L, O, Q, R, U, X
        ".+C[^AHKLOQRUX].*",  # C except before A, H, K, L, O, Q, R, U, X
        ".*[DT][CSZ].*",  # D, T before C, S, Z
        ".*[CKQ]X.*",  # X after C, K, Q
    ]
    __TESTSET: typing.Set[str] = set()

    def testSpecialCharsBetweenSameLetters_test0_decomposed(self) -> None:
        data = ["Test test", "Testtest", "Test-test", "TesT#Test", "TesT?test"]
        self.checkEncodingVariations("28282", data)

    def testVariationsMeyer_test0_decomposed(self) -> None:
        data = ["Meier", "Maier", "Mair", "Meyer", "Meyr", "Mejer", "Major"]
        self.checkEncodingVariations("67", data)

    def testVariationsMella_test0_decomposed(self) -> None:
        data = ["mella", "milah", "moulla", "mellah", "muehle", "mule"]
        self.checkEncodingVariations("65", data)

    def testIsEncodeEquals_test0_decomposed(self) -> None:
        data = [
            ["Muller", "Müller"],  # Müller
            ["Meyer", "Mayr"],
            ["house", "house"],
            ["House", "house"],
            ["Haus", "house"],
            ["ganz", "Gans"],
            ["ganz", "Gänse"],  # Gänse
            ["Miyagi", "Miyako"],
        ]
        for element in data:
            encode_equal = ColognePhonetic().isEncodeEqual(element[1], element[0])
            self.assertTrue(encode_equal, f"{element[1]} != {element[0]}")

    def testHyphen_test0_decomposed(self) -> None:
        data = [("bergisch-gladbach", "174845214"), ("Müller-Lüdenscheidt", "65752682")]
        self.check_encodings(data)

    def testExamples_test0_decomposed(self) -> None:
        data = [
            ["mÜller", "657"],  # mÜller - why upper case U-umlaut?
            ["müller", "657"],  # müller - add equivalent lower-case
            ["schmidt", "862"],
            ["schneider", "8627"],
            ["fischer", "387"],
            ["weber", "317"],
            ["wagner", "3467"],
            ["becker", "147"],
            ["hoffmann", "0366"],
            ["schÄfer", "837"],  # schÄfer - why upper case A-umlaut ?
            ["schäfer", "837"],  # schäfer - add equivalent lower-case
            ["Breschnew", "17863"],
            ["Wikipedia", "3412"],
            ["peter", "127"],
            ["pharma", "376"],
            ["mönchengladbach", "664645214"],  # mönchengladbach
            ["deutsch", "28"],
            ["deutz", "28"],
            ["hamburg", "06174"],
            ["hannover", "0637"],
            ["christstollen", "478256"],
            ["Xanthippe", "48621"],
            ["Zacharias", "8478"],
            ["Holzbau", "0581"],
            ["matsch", "68"],
            ["matz", "68"],
            ["Arbeitsamt", "071862"],
            ["Eberhard", "01772"],
            ["Eberhardt", "01772"],
            ["Celsius", "8588"],
            ["Ace", "08"],
            ["shch", "84"],  # CODEC-254
            ["xch", "484"],  # CODEC-255
            ["heithabu", "021"],
        ]
        self.checkEncodings(data)

    def testEdgeCases_test0_decomposed(self) -> None:
        data = [
            ["a", "0"],
            ["e", "0"],
            ["i", "0"],
            ["o", "0"],
            ["u", "0"],
            ["\u00e4", "0"],  # a-umlaut
            ["\u00f6", "0"],  # o-umlaut
            ["\u00fc", "0"],  # u-umlaut
            ["\u00df", "8"],  # small sharp s
            ["aa", "0"],
            ["ha", "0"],
            ["h", ""],
            ["aha", "0"],
            ["b", "1"],
            ["p", "1"],
            ["ph", "3"],
            ["f", "3"],
            ["v", "3"],
            ["w", "3"],
            ["g", "4"],
            ["k", "4"],
            ["q", "4"],
            ["x", "48"],
            ["ax", "048"],
            ["cx", "48"],
            ["l", "5"],
            ["cl", "45"],
            ["acl", "085"],
            ["mn", "6"],
            ["{mn}", "6"],  # test chars above Z
            ["r", "7"],
        ]
        self.checkEncodings(data)

    def testAychlmajrForCodec122_test0_decomposed(self) -> None:
        self.checkEncoding("04567", "Aychlmajr")

    def testAaclan_test0_decomposed(self) -> None:
        self.checkEncoding("0856", "Aaclan")

    def testAabjoe_test0_decomposed(self) -> None:
        self.checkEncoding("01", "Aabjoe")

    def testCanFail_test0_decomposed(self) -> None:
        with self.assertRaises(ComparisonFailure):  # Correct exception type
            self.checkEncoding("/", "Fehler")

    def _createStringEncoder(self) -> ColognePhonetic:
        return ColognePhonetic()

    def checkEncoding(self, expected: str, source: str) -> None:
        self.__TESTSET.add(
            source.upper().replace("Ä", "A").replace("Ö", "O").replace("Ü", "U")
        )
        super().checkEncoding(expected, source)

    @staticmethod
    def finishTests() -> None:
        errors = 0
        for m in ColognePhoneticTest.__MATCHES:
            if not ColognePhoneticTest.__hasTestCase(m):
                print(f"{m} has no test case")
                errors += 1
        assert errors == 0, "Not expecting any missing test cases"

    @staticmethod
    def main(args: typing.List[str]) -> None:
        coder = ColognePhonetic()
        for arg in args:
            code = coder.encode1(arg)
            print(f"'{arg}' = '{code}'")

    @staticmethod
    def __hasTestCase(re: str) -> bool:
        for s in ColognePhoneticTest.__TESTSET:
            if re.match(s):  # Using re.match for regex matching
                return True
        return False
