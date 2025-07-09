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
from src.main.org.apache.commons.codec.language.Nysiis import *


class NysiisTest(StringEncoderAbstractTest, unittest.TestCase):

    __fullNysiis: Nysiis = Nysiis(False)

    def testTrueVariant_test3_decomposed(self) -> None:
        encoder = Nysiis(True)
        encoded = encoder.encode1("WESTERLUND")
        self.assertTrue(len(encoded) <= 6)
        self.assertEqual("WASTAR", encoded)

    def testTrueVariant_test2_decomposed(self) -> None:
        encoder = Nysiis(True)
        encoded = encoder.encode1("WESTERLUND")
        self.assertTrue(len(encoded) <= 6)

    def testTrueVariant_test1_decomposed(self) -> None:
        encoder = Nysiis(True)
        encoded = encoder.encode1("WESTERLUND")

    def testTrueVariant_test0_decomposed(self) -> None:
        encoder = Nysiis(True)

    def testTranan_test0_decomposed(self) -> None:
        self.__encodeAll(["Trueman", "Truman"], "TRANAN")

    def testSpecialBranches_test0_decomposed(self) -> None:
        self.__encodeAll(["Kobwick"], "CABWAC")
        self.__encodeAll(["Kocher"], "CACAR")
        self.__encodeAll(["Fesca"], "FASC")
        self.__encodeAll(["Shom"], "SAN")
        self.__encodeAll(["Ohlo"], "OL")
        self.__encodeAll(["Uhu"], "UH")
        self.__encodeAll(["Um"], "UN")

    def testSnat_test0_decomposed(self) -> None:
        self.__encodeAll(["Smith", "Schmit"], "SNAT")

    def testSnad_test0_decomposed(self) -> None:
        self.__encodeAll(["Schmidt"], "SNAD")

    def testRule7_test0_decomposed(self) -> None:
        self.__assertEncodings([["XA", "X"], ["XAS", "X"]])

    def testRule6_test0_decomposed(self) -> None:
        self.__assertEncodings([["XAY", "XY"], ["XY", "XY"]])

    def testRule5_test0_decomposed(self) -> None:
        self.__assertEncodings([["XS", "X"], ["XSS", "X"]])

    def testRule4Dot2_test0_decomposed(self) -> None:
        self.__assertEncodings([["XQ", "XG"], ["XZ", "X"], ["XM", "XN"]])

    def testRule4Dot1_test0_decomposed(self) -> None:
        self.__assertEncodings(
            [
                ["XEV", "XAF"],
                ["XAX", "XAX"],
                ["XEX", "XAX"],
                ["XIX", "XAX"],
                ["XOX", "XAX"],
                ["XUX", "XAX"],
            ]
        )

    def testRule2_test0_decomposed(self) -> None:
        self.__assertEncodings(
            [
                ["XEE", "XY"],
                ["XIE", "XY"],
                ["XDT", "XD"],
                ["XRT", "XD"],
                ["XRD", "XD"],
                ["XNT", "XD"],
                ["XND", "XD"],
            ]
        )

    def testRule1_test0_decomposed(self) -> None:
        self.__assertEncodings(
            [
                ["MACX", "MCX"],
                ["KNX", "NX"],
                ["KX", "CX"],
                ["PHX", "FX"],
                ["PFX", "FX"],
                ["SCHX", "SX"],
            ]
        )

    def testOthers_test0_decomposed(self) -> None:
        self.__assertEncodings(
            [
                ["O'Daniel", "ODANAL"],
                ["O'Donnel", "ODANAL"],
                ["Cory", "CARY"],
                ["Corey", "CARY"],
                ["Kory", "CARY"],
                ["FUZZY", "FASY"],
            ]
        )

    def testFal_test0_decomposed(self) -> None:
        self.__encodeAll(["Phil"], "FAL")

    def testDropBy_test0_decomposed(self) -> None:
        self.__assertEncodings(
            [
                ["MACINTOSH", "MCANT"],
                ["KNUTH", "NAT"],  # Original: NNAT; modified: NATH
                ["KOEHN", "CAN"],  # Original: C
                ["PHILLIPSON", "FALAPSAN"],  # Original: FFALAP[SAN]
                ["PFEISTER", "FASTAR"],  # Original: FFASTA[R]
                ["SCHOENHOEFT", "SANAFT"],  # Original: SSANAF[T]
                ["MCKEE", "MCY"],
                ["MACKIE", "MCY"],
                ["HEITSCHMIDT", "HATSNAD"],
                ["BART", "BAD"],
                ["HURD", "HAD"],
                ["HUNT", "HAD"],
                ["WESTERLUND", "WASTARLAD"],
                ["CASSTEVENS", "CASTAFAN"],
                ["VASQUEZ", "VASG"],
                ["FRAZIER", "FRASAR"],
                ["BOWMAN", "BANAN"],
                ["MCKNIGHT", "MCNAGT"],
                ["RICKERT", "RACAD"],
                ["DEUTSCH", "DAT"],  # Original: DATS
                ["WESTPHAL", "WASTFAL"],
                ["SHRIVER", "SRAVAR"],  # Original: SHRAVA[R]
                ["KUHL", "CAL"],  # Original: C
                ["RAWSON", "RASAN"],
                ["JILES", "JAL"],
                ["CARRAWAY", "CARY"],  # Original: CARAY
                ["YAMADA", "YANAD"],
            ]
        )

    def testDan_test0_decomposed(self) -> None:
        self.__encodeAll(["Dane", "Dean", "Dionne"], "DAN")

    def testDad_test0_decomposed(self) -> None:
        self.__encodeAll(["Dent"], "DAD")

    def testCap_test0_decomposed(self) -> None:
        self.__encodeAll(["Capp", "Cope", "Copp", "Kipp"], "CAP")

    def testBran_test0_decomposed(self) -> None:
        self.__encodeAll(["Brian", "Brown", "Brun"], "BRAN")

    def _createStringEncoder(self) -> Nysiis:
        return Nysiis.Nysiis1()

    def __encodeAll(self, strings: List[str], expectedEncoding: str) -> None:
        for string in strings:
            self.assertEqual(
                expectedEncoding,
                self.getStringEncoder().encode1(string),
                f"Problem with {string}",
            )

    def __assertEncodings(self, testValues: typing.List[typing.List[str]]) -> None:
        for arr in testValues:
            self.assertEqual(
                arr[1], self.__fullNysiis.encode1(arr[0]), msg=f"Problem with {arr[0]}"
            )
