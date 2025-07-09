from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.DaitchMokotoffSoundex import *


class DaitchMokotoffSoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSpecialRomanianCharacters_test0_decomposed(self) -> None:
        self.assertEqual(
            "364000|464000",
            self.__soundex("ţamas"),
            "Soundex encoding for 'ţamas' did not match expected value",
        )
        self.assertEqual(
            "364000|464000",
            self.__soundex("țamas"),
            "Soundex encoding for 'țamas' did not match expected value",
        )

    def testSoundexBasic3_test0_decomposed(self) -> None:
        self.assertEqual(
            "734000|739400",
            self.__soundex("Peters"),
            "Soundex for 'Peters' did not match expected value",
        )
        self.assertEqual(
            "734600|739460",
            self.__soundex("Peterson"),
            "Soundex for 'Peterson' did not match expected value",
        )
        self.assertEqual(
            "645740",
            self.__soundex("Moskowitz"),
            "Soundex for 'Moskowitz' did not match expected value",
        )
        self.assertEqual(
            "645740",
            self.__soundex("Moskovitz"),
            "Soundex for 'Moskovitz' did not match expected value",
        )
        self.assertEqual(
            "154600|145460|454600|445460",
            self.__soundex("Jackson"),
            "Soundex for 'Jackson' did not match expected value",
        )
        self.assertEqual(
            "154654|154645|154644|145465|145464|454654|454645|454644|445465|445464",
            self.__soundex("Jackson-Jackson"),
            "Soundex for 'Jackson-Jackson' did not match expected value",
        )

    def testSoundexBasic2_test0_decomposed(self) -> None:
        self.assertEqual(
            "467000|567000", self.__soundex("Ceniow"), "Soundex mismatch for 'Ceniow'"
        )
        self.assertEqual(
            "467000", self.__soundex("Tsenyuv"), "Soundex mismatch for 'Tsenyuv'"
        )
        self.assertEqual(
            "587400|587500",
            self.__soundex("Holubica"),
            "Soundex mismatch for 'Holubica'",
        )
        self.assertEqual(
            "587400", self.__soundex("Golubitsa"), "Soundex mismatch for 'Golubitsa'"
        )
        self.assertEqual(
            "746480|794648",
            self.__soundex("Przemysl"),
            "Soundex mismatch for 'Przemysl'",
        )
        self.assertEqual(
            "746480", self.__soundex("Pshemeshil"), "Soundex mismatch for 'Pshemeshil'"
        )
        self.assertEqual(
            "944744|944745|944754|944755|945744|945745|945754|945755",
            self.__soundex("Rosochowaciec"),
            "Soundex mismatch for 'Rosochowaciec'",
        )
        self.assertEqual(
            "945744",
            self.__soundex("Rosokhovatsets"),
            "Soundex mismatch for 'Rosokhovatsets'",
        )

    def testSoundexBasic_test0_decomposed(self) -> None:
        self.assertEqual(
            "583600", self.__soundex("GOLDEN"), "Soundex for 'GOLDEN' did not match"
        )
        self.assertEqual(
            "087930", self.__soundex("Alpert"), "Soundex for 'Alpert' did not match"
        )
        self.assertEqual(
            "791900", self.__soundex("Breuer"), "Soundex for 'Breuer' did not match"
        )
        self.assertEqual(
            "579000", self.__soundex("Haber"), "Soundex for 'Haber' did not match"
        )
        self.assertEqual(
            "665600", self.__soundex("Mannheim"), "Soundex for 'Mannheim' did not match"
        )
        self.assertEqual(
            "664000", self.__soundex("Mintz"), "Soundex for 'Mintz' did not match"
        )
        self.assertEqual(
            "370000", self.__soundex("Topf"), "Soundex for 'Topf' did not match"
        )
        self.assertEqual(
            "586660",
            self.__soundex("Kleinmann"),
            "Soundex for 'Kleinmann' did not match",
        )
        self.assertEqual(
            "769600", self.__soundex("Ben Aron"), "Soundex for 'Ben Aron' did not match"
        )
        self.assertEqual(
            "097400|097500",
            self.__soundex("AUERBACH"),
            "Soundex for 'AUERBACH' did not match",
        )
        self.assertEqual(
            "097400|097500",
            self.__soundex("OHRBACH"),
            "Soundex for 'OHRBACH' did not match",
        )
        self.assertEqual(
            "874400", self.__soundex("LIPSHITZ"), "Soundex for 'LIPSHITZ' did not match"
        )
        self.assertEqual(
            "874400|874500",
            self.__soundex("LIPPSZYC"),
            "Soundex for 'LIPPSZYC' did not match",
        )
        self.assertEqual(
            "876450", self.__soundex("LEWINSKY"), "Soundex for 'LEWINSKY' did not match"
        )
        self.assertEqual(
            "876450", self.__soundex("LEVINSKI"), "Soundex for 'LEVINSKI' did not match"
        )
        self.assertEqual(
            "486740",
            self.__soundex("SZLAMAWICZ"),
            "Soundex for 'SZLAMAWICZ' did not match",
        )
        self.assertEqual(
            "486740",
            self.__soundex("SHLAMOVITZ"),
            "Soundex for 'SHLAMOVITZ' did not match",
        )

    def testEncodeIgnoreTrimmable_test0_decomposed(self) -> None:
        self.assertEqual(
            "746536",
            self.__encode(" \t\n\r Washington \t\n\r "),
            "Encoded value does not match for input with trimmable characters",
        )
        self.assertEqual(
            "746536",
            self.__encode("Washington"),
            "Encoded value does not match for input without trimmable characters",
        )

    def testEncodeIgnoreHyphens_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "565463",
            [
                "KINGSMITH",
                "-KINGSMITH",
                "K-INGSMITH",
                "KI-NGSMITH",
                "KIN-GSMITH",
                "KING-SMITH",
                "KINGS-MITH",
                "KINGSM-ITH",
                "KINGSMI-TH",
                "KINGSMIT-H",
                "KINGSMITH-",
            ],
        )

    def testEncodeIgnoreApostrophes_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "079600",
            [
                "OBrien",
                "'OBrien",
                "O'Brien",
                "OB'rien",
                "OBr'ien",
                "OBri'en",
                "OBrie'n",
                "OBrien'",
            ],
        )

    def testAdjacentCodes_test0_decomposed(self) -> None:
        self.assertEqual(
            "054800",
            self.__soundex("AKSSOL"),
            "Soundex code for 'AKSSOL' does not match expected value",
        )
        self.assertEqual(
            "547830|545783|594783|594578",
            self.__soundex("GERSCHFELD"),
            "Soundex code for 'GERSCHFELD' does not match expected value",
        )

    def testAccentedCharacterFolding_test0_decomposed(self) -> None:
        self.assertEqual(
            "294795",
            self.__soundex("Straßburg"),
            "Soundex code for 'Straßburg' does not match expected value",
        )
        self.assertEqual(
            "294795",
            self.__soundex("Strasburg"),
            "Soundex code for 'Strasburg' does not match expected value",
        )
        self.assertEqual(
            "095600",
            self.__soundex("Éregon"),
            "Soundex code for 'Éregon' does not match expected value",
        )
        self.assertEqual(
            "095600",
            self.__soundex("Eregon"),
            "Soundex code for 'Eregon' does not match expected value",
        )

    def _createStringEncoder(self) -> DaitchMokotoffSoundex:
        return DaitchMokotoffSoundex.DaitchMokotoffSoundex1()

    def testEncodeBasic(self) -> None:
        self.assertEqual("097400", self.__encode("AUERBACH"))
        self.assertEqual("097400", self.__encode("OHRBACH"))
        self.assertEqual("874400", self.__encode("LIPSHITZ"))
        self.assertEqual("874400", self.__encode("LIPPSZYC"))
        self.assertEqual("876450", self.__encode("LEWINSKY"))
        self.assertEqual("876450", self.__encode("LEVINSKI"))
        self.assertEqual("486740", self.__encode("SZLAMAWICZ"))
        self.assertEqual("486740", self.__encode("SHLAMOVITZ"))

    def __encode(self, source: str) -> str:
        return DaitchMokotoffSoundex().encode1(source)

    def __soundex(self, source: str) -> str:
        return self.getStringEncoder().soundex0(source)
