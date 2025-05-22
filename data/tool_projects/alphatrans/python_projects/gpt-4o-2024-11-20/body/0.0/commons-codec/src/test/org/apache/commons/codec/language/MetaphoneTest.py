from __future__ import annotations
import re
import enum
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.Metaphone import *


class MetaphoneTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSetMaxLengthWithTruncation_test3_decomposed(self) -> None:
        encoder = Metaphone()
        encoder.setMaxCodeLen(6)
        result = encoder.metaphone("AXEAXEAXE")
        self.assertEqual("AKSKSK", result)

    def testSetMaxLengthWithTruncation_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.getStringEncoder().setMaxCodeLen(6)
        self.getStringEncoder()

    def testSetMaxLengthWithTruncation_test1_decomposed(self) -> None:
        encoder = Metaphone()
        encoder.setMaxCodeLen(6)

    def testSetMaxLengthWithTruncation_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testExceedLength_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("AKSK", encoder.metaphone("AXEAXE"))

    def testExceedLength_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testTCH_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("RX", self.getStringEncoder().metaphone("RETCH"))
        self.getStringEncoder()
        self.assertEqual("WX", self.getStringEncoder().metaphone("WATCH"))

    def testTCH_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("RX", encoder.metaphone("RETCH"))
        encoder = self.getStringEncoder()

    def testTCH_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("RX", encoder.metaphone("RETCH"))

    def testTCH_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testTIOAndTIAToX_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("OX", encoder.metaphone("OTIA"))
        encoder = self.getStringEncoder()
        self.assertEqual("PRXN", encoder.metaphone("PORTION"))

    def testTIOAndTIAToX_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("OX", encoder.metaphone("OTIA"))
        encoder = self.getStringEncoder()

    def testTIOAndTIAToX_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("OX", encoder.metaphone("OTIA"))

    def testTIOAndTIAToX_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testSHAndSIOAndSIAToX_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("XT", self.getStringEncoder().metaphone("SHOT"))
        self.getStringEncoder()
        self.assertEqual("OTXN", self.getStringEncoder().metaphone("ODSIAN"))
        self.getStringEncoder()
        self.assertEqual("PLXN", self.getStringEncoder().metaphone("PULSION"))

    def testSHAndSIOAndSIAToX_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("XT", self.getStringEncoder().metaphone("SHOT"))
        self.getStringEncoder()
        self.assertEqual("OTXN", self.getStringEncoder().metaphone("ODSIAN"))
        self.getStringEncoder()

    def testSHAndSIOAndSIAToX_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("XT", encoder.metaphone("SHOT"))
        encoder = self.getStringEncoder()
        self.assertEqual("OTXN", encoder.metaphone("ODSIAN"))

    def testSHAndSIOAndSIAToX_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("XT", self.getStringEncoder().metaphone("SHOT"))
        self.getStringEncoder()

    def testSHAndSIOAndSIAToX_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("XT", encoder.metaphone("SHOT"))

    def testSHAndSIOAndSIAToX_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testPHTOF_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("FX", encoder.metaphone("PHISH"))

    def testPHTOF_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testDiscardOfSilentGN_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("N", encoder.metaphone("GNU"))
        encoder = self.getStringEncoder()
        self.assertEqual("SNT", encoder.metaphone("SIGNED"))

    def testDiscardOfSilentGN_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("N", encoder.metaphone("GNU"))
        encoder = self.getStringEncoder()

    def testDiscardOfSilentGN_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("N", encoder.metaphone("GNU"))

    def testDiscardOfSilentGN_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testDiscardOfSilentHAfterG_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("KNT", self.getStringEncoder().metaphone("GHENT"))
        self.getStringEncoder()
        self.assertEqual("B", self.getStringEncoder().metaphone("BAUGH"))

    def testDiscardOfSilentHAfterG_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("KNT", self.getStringEncoder().metaphone("GHENT"))
        self.getStringEncoder()

    def testDiscardOfSilentHAfterG_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("KNT", encoder.metaphone("GHENT"))

    def testDiscardOfSilentHAfterG_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testTranslateToJOfDGEOrDGIOrDGY_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGY"))
        self.getStringEncoder()
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGE"))
        self.getStringEncoder()
        self.assertEqual("AJMT", self.getStringEncoder().metaphone("ADGIEMTI"))

    def testTranslateToJOfDGEOrDGIOrDGY_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGY"))
        self.getStringEncoder()
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGE"))
        self.getStringEncoder()

    def testTranslateToJOfDGEOrDGIOrDGY_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("TJ", encoder.metaphone("DODGY"))
        encoder = self.getStringEncoder()
        self.assertEqual("TJ", encoder.metaphone("DODGE"))

    def testTranslateToJOfDGEOrDGIOrDGY_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("TJ", self.getStringEncoder().metaphone("DODGY"))
        self.getStringEncoder()

    def testTranslateToJOfDGEOrDGIOrDGY_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("TJ", encoder.metaphone("DODGY"))

    def testTranslateToJOfDGEOrDGIOrDGY_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testTranslateOfSCHAndCH_test7_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SKTL", encoder.metaphone("SCHEDULE"))
        encoder = self.getStringEncoder()
        self.assertEqual("SKMT", encoder.metaphone("SCHEMATIC"))
        encoder = self.getStringEncoder()
        self.assertEqual("KRKT", encoder.metaphone("CHARACTER"))
        encoder = self.getStringEncoder()
        self.assertEqual("TX", encoder.metaphone("TEACH"))

    def testTranslateOfSCHAndCH_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("SKTL", self.getStringEncoder().metaphone("SCHEDULE"))
        self.getStringEncoder()
        self.assertEqual("SKMT", self.getStringEncoder().metaphone("SCHEMATIC"))
        self.getStringEncoder()
        self.assertEqual("KRKT", self.getStringEncoder().metaphone("CHARACTER"))
        self.getStringEncoder()

    def testTranslateOfSCHAndCH_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("SKTL", self.getStringEncoder().metaphone("SCHEDULE"))
        self.getStringEncoder()
        self.assertEqual("SKMT", self.getStringEncoder().metaphone("SCHEMATIC"))
        self.getStringEncoder()
        self.assertEqual("KRKT", self.getStringEncoder().metaphone("CHARACTER"))

    def testTranslateOfSCHAndCH_test4_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SKTL", encoder.metaphone("SCHEDULE"))
        encoder = self.getStringEncoder()
        self.assertEqual("SKMT", encoder.metaphone("SCHEMATIC"))
        encoder = self.getStringEncoder()

    def testTranslateOfSCHAndCH_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SKTL", encoder.metaphone("SCHEDULE"))
        encoder = self.getStringEncoder()
        self.assertEqual("SKMT", encoder.metaphone("SCHEMATIC"))

    def testTranslateOfSCHAndCH_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SKTL", encoder.metaphone("SCHEDULE"))
        encoder = self.getStringEncoder()

    def testTranslateOfSCHAndCH_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SKTL", encoder.metaphone("SCHEDULE"))

    def testTranslateOfSCHAndCH_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testWordsWithCIA_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("XP", encoder.metaphone("CIAPO"))

    def testWordsWithCIA_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testWhy_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("", encoder.metaphone("WHY"))

    def testWhy_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testDiscardOfSCEOrSCIOrSCY_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("SNS", self.getStringEncoder().metaphone("SCIENCE"))
        self.getStringEncoder()
        self.assertEqual("SN", self.getStringEncoder().metaphone("SCENE"))
        self.getStringEncoder()
        self.assertEqual("S", self.getStringEncoder().metaphone("SCY"))

    def testDiscardOfSCEOrSCIOrSCY_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("SNS", self.getStringEncoder().metaphone("SCIENCE"))
        self.getStringEncoder()
        self.assertEqual("SN", self.getStringEncoder().metaphone("SCENE"))
        self.getStringEncoder()

    def testDiscardOfSCEOrSCIOrSCY_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("SNS", self.getStringEncoder().metaphone("SCIENCE"))
        self.getStringEncoder()
        self.assertEqual("SN", self.getStringEncoder().metaphone("SCENE"))

    def testDiscardOfSCEOrSCIOrSCY_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("SNS", encoder.metaphone("SCIENCE"))
        encoder = self.getStringEncoder()

    def testDiscardOfSCEOrSCIOrSCY_test1_decomposed(self) -> None:
        string_encoder = self.getStringEncoder()
        self.assertEqual("SNS", string_encoder.metaphone("SCIENCE"))

    def testDiscardOfSCEOrSCIOrSCY_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testWordEndingInMB_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("KM", self.getStringEncoder().metaphone("COMB"))
        self.getStringEncoder()
        self.assertEqual("TM", self.getStringEncoder().metaphone("TOMB"))
        self.getStringEncoder()
        self.assertEqual("WM", self.getStringEncoder().metaphone("WOMB"))

    def testWordEndingInMB_test4_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("KM", encoder.metaphone("COMB"))
        encoder = self.getStringEncoder()
        self.assertEqual("TM", encoder.metaphone("TOMB"))
        encoder = self.getStringEncoder()

    def testWordEndingInMB_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("KM", encoder.metaphone("COMB"))
        encoder = self.getStringEncoder()
        self.assertEqual("TM", encoder.metaphone("TOMB"))

    def testWordEndingInMB_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("KM", self.getStringEncoder().metaphone("COMB"))
        self.getStringEncoder()

    def testWordEndingInMB_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("KM", encoder.metaphone("COMB"))

    def testWordEndingInMB_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testMetaphone_test21_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("the"))
        self.getStringEncoder()
        self.assertEqual("LS", self.getStringEncoder().metaphone("lazy"))
        self.getStringEncoder()
        self.assertEqual("TKS", self.getStringEncoder().metaphone("dogs"))

    def testMetaphone_test20_decomposed(self) -> None:
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.assertEqual("0", self.getStringEncoder().metaphone("the"))
        self.assertEqual("LS", self.getStringEncoder().metaphone("lazy"))

    def testMetaphone_test19_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("the"))
        self.getStringEncoder()
        self.assertEqual("LS", self.getStringEncoder().metaphone("lazy"))

    def testMetaphone_test18_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("the"))
        self.getStringEncoder()

    def testMetaphone_test17_decomposed(self) -> None:
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.assertEqual("0", self.getStringEncoder().metaphone("the"))

    def testMetaphone_test16_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))
        self.getStringEncoder()

    def testMetaphone_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()
        self.assertEqual("OFR", self.getStringEncoder().metaphone("over"))

    def testMetaphone_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))
        self.getStringEncoder()

    def testMetaphone_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()
        self.assertEqual("JMPT", self.getStringEncoder().metaphone("jumped"))

    def testMetaphone_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))
        self.getStringEncoder()

    def testMetaphone_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()
        self.assertEqual("FKS", self.getStringEncoder().metaphone("fox"))

    def testMetaphone_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))
        self.getStringEncoder()
        self.assertEqual("BRN", self.getStringEncoder().metaphone("brown"))
        self.getStringEncoder()

    def testMetaphone_test9_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))
        self.assertEqual("0", encoder.metaphone("The"))
        self.assertEqual("KK", encoder.metaphone("quick"))
        self.assertEqual("BRN", encoder.metaphone("brown"))

    def testMetaphone_test8_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))
        self.assertEqual("0", encoder.metaphone("The"))
        self.assertEqual("KK", encoder.metaphone("quick"))

    def testMetaphone_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("HL", self.getStringEncoder().metaphone("howl"))
        self.getStringEncoder()
        self.assertEqual("TSTN", self.getStringEncoder().metaphone("testing"))
        self.getStringEncoder()
        self.assertEqual("0", self.getStringEncoder().metaphone("The"))
        self.getStringEncoder()
        self.assertEqual("KK", self.getStringEncoder().metaphone("quick"))

    def testMetaphone_test6_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))
        self.assertEqual("0", encoder.metaphone("The"))

    def testMetaphone_test5_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))
        self.assertEqual("0", encoder.metaphone("The"))

    def testMetaphone_test4_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))

    def testMetaphone_test3_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        self.assertEqual("TSTN", encoder.metaphone("testing"))

    def testMetaphone_test2_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))
        encoder = self.getStringEncoder()

    def testMetaphone_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("HL", encoder.metaphone("howl"))

    def testMetaphone_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testIsMetaphoneEqualXalan_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Xalan",
            [
                "Celene",
                "Celina",
                "Celine",
                "Selena",
                "Selene",
                "Selina",
                "Seline",
                "Suellen",
                "Xylina",
            ],
        )

    def testIsMetaphoneEqualWright_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual("Wright", ["Rota", "Rudd", "Ryde"])

    def testIsMetaphoneEqualSusan_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Susan",
            [
                "Siusan",
                "Sosanna",
                "Susan",
                "Susana",
                "Susann",
                "Susanna",
                "Susannah",
                "Susanne",
                "Suzann",
                "Suzanna",
                "Suzanne",
                "Zuzana",
            ],
        )

    def testIsMetaphoneEqualRay_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual("Ray", ["Ray", "Rey", "Roi", "Roy", "Ruy"])

    def testIsMetaphoneEqualPeter_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Peter",
            [
                "Peadar",
                "Peder",
                "Pedro",
                "Peter",
                "Petr",
                "Peyter",
                "Pieter",
                "Pietro",
                "Piotr",
            ],
        )

    def testIsMetaphoneEqualParis_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Paris", ["Pearcy", "Perris", "Piercy", "Pierz", "Pryse"]
        )

    def testIsMetaphoneEqualMary_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Mary",
            [
                "Mair",
                "Maire",
                "Mara",
                "Mareah",
                "Mari",
                "Maria",
                "Marie",
                "Mary",
                "Maura",
                "Maure",
                "Meara",
                "Merrie",
                "Merry",
                "Mira",
                "Moira",
                "Mora",
                "Moria",
                "Moyra",
                "Muire",
                "Myra",
                "Myrah",
            ],
        )

    def testIsMetaphoneEqualKnight_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Knight",
            [
                "Hynda",
                "Nada",
                "Nadia",
                "Nady",
                "Nat",
                "Nata",
                "Natty",
                "Neda",
                "Nedda",
                "Nedi",
                "Netta",
                "Netti",
                "Nettie",
                "Netty",
                "Nita",
                "Nydia",
            ],
        )

    def testIsMetaphoneEqualJohn_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "John",
            [
                "Gena",
                "Gene",
                "Genia",
                "Genna",
                "Genni",
                "Gennie",
                "Genny",
                "Giana",
                "Gianna",
                "Gina",
                "Ginni",
                "Ginnie",
                "Ginny",
                "Jaine",
                "Jan",
                "Jana",
                "Jane",
                "Janey",
                "Jania",
                "Janie",
                "Janna",
                "Jany",
                "Jayne",
                "Jean",
                "Jeana",
                "Jeane",
                "Jeanie",
                "Jeanna",
                "Jeanne",
                "Jeannie",
                "Jen",
                "Jena",
                "Jeni",
                "Jenn",
                "Jenna",
                "Jennee",
                "Jenni",
                "Jennie",
                "Jenny",
                "Jinny",
                "Jo Ann",
                "Jo-Ann",
                "Jo-Anne",
                "Joan",
                "Joana",
                "Joane",
                "Joanie",
                "Joann",
                "Joanna",
                "Joanne",
                "Joeann",
                "Johna",
                "Johnna",
                "Joni",
                "Jonie",
                "Juana",
                "June",
                "Junia",
                "Junie",
            ],
        )

    def testIsMetaphoneEqualGary_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Gary",
            [
                "Cahra",
                "Cara",
                "Carey",
                "Cari",
                "Caria",
                "Carie",
                "Caro",
                "Carree",
                "Carri",
                "Carrie",
                "Carry",
                "Cary",
                "Cora",
                "Corey",
                "Cori",
                "Corie",
                "Correy",
                "Corri",
                "Corrie",
                "Corry",
                "Cory",
                "Gray",
                "Kara",
                "Kare",
                "Karee",
                "Kari",
                "Karia",
                "Karie",
                "Karrah",
                "Karrie",
                "Karry",
                "Kary",
                "Keri",
                "Kerri",
                "Kerrie",
                "Kerry",
                "Kira",
                "Kiri",
                "Kora",
                "Kore",
                "Kori",
                "Korie",
                "Korrie",
                "Korry",
            ],
        )

    def testIsMetaphoneEqualAlbert_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "Albert", ["Ailbert", "Alberik", "Albert", "Alberto", "Albrecht"]
        )

    def testIsMetaphoneEqualWhite_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual(
            "White",
            [
                "Wade",
                "Wait",
                "Waite",
                "Wat",
                "Whit",
                "Wiatt",
                "Wit",
                "Wittie",
                "Witty",
                "Wood",
                "Woodie",
                "Woody",
            ],
        )

    def testIsMetaphoneEqualAero_test0_decomposed(self) -> None:
        self.assertIsMetaphoneEqual("Aero", ["Eure"])

    def testIsMetaphoneEqual2_test0_decomposed(self) -> None:
        self.assertMetaphoneEqual(
            [
                ["Lawrence", "Lorenza"],
                ["Gary", "Cahra"],
            ]
        )

    def testIsMetaphoneEqual1_test0_decomposed(self) -> None:
        self.assertMetaphoneEqual(
            [["Case", "case"], ["CASE", "Case"], ["caSe", "cAsE"], ["quick", "cookie"]]
        )

    def _createStringEncoder(self) -> Metaphone:
        return Metaphone()

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        if len(pairs) == 0:
            pytest.fail("Test fixture is empty")
        for i, pair in enumerate(pairs):
            if len(pair) != 2:
                pytest.fail(f"Error in test fixture in the data array at index {i}")

    def assertMetaphoneEqual(self, pairs: typing.List[typing.List[str]]) -> None:
        self.validateFixture(pairs)
        for pair in pairs:
            name0 = pair[0]
            name1 = pair[1]
            fail_msg = f"Expected match between {name0} and {name1}"
            self.assertTrue(
                self.getStringEncoder().isMetaphoneEqual(name0, name1), fail_msg
            )
            self.assertTrue(
                self.getStringEncoder().isMetaphoneEqual(name1, name0), fail_msg
            )

    def assertIsMetaphoneEqual(self, source: str, matches: typing.List[str]) -> None:
        for matche in matches:
            self.assertTrue(
                self.getStringEncoder().isMetaphoneEqual(source, matche),
                f"Source: {source}, should have same Metaphone as: {matche}",
            )
        for matche in matches:
            for matche2 in matches:
                self.assertTrue(
                    self.getStringEncoder().isMetaphoneEqual(matche, matche2),
                    f"Matches: {matche} and {matche2} should have the same Metaphone",
                )
