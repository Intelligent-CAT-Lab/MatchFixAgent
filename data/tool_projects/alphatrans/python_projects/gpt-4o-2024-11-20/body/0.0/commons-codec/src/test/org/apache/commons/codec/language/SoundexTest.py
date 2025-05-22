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
from src.main.org.apache.commons.codec.language.Soundex import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class SoundexTest(StringEncoderAbstractTest, unittest.TestCase):

    def testSimplifiedSoundex_test1_decomposed(self) -> None:
        s = Soundex.US_ENGLISH_SIMPLIFIED
        self.assertEqual("W452", s.encode1("WILLIAMS"))
        self.assertEqual("B625", s.encode1("BARAGWANATH"))
        self.assertEqual("D540", s.encode1("DONNELL"))
        self.assertEqual("L300", s.encode1("LLOYD"))
        self.assertEqual("W422", s.encode1("WOOLCOCK"))
        self.assertEqual("D320", s.encode1("Dodds"))
        self.assertEqual("D320", s.encode1("Dwdds"))
        self.assertEqual("D320", s.encode1("Dhdds"))

    def testSimplifiedSoundex_test0_decomposed(self) -> None:
        s = Soundex.US_ENGLISH_SIMPLIFIED
        self.assertEqual("W452", s.encode1("WILLIAMS"))

    def testGenealogy_test1_decomposed(self) -> None:
        s = Soundex.US_ENGLISH_GENEALOGY
        self.assertEqual("H251", s.encode1("Heggenburger"))
        self.assertEqual("B425", s.encode1("Blackman"))
        self.assertEqual("S530", s.encode1("Schmidt"))
        self.assertEqual("L150", s.encode1("Lippmann"))
        self.assertEqual("D200", s.encode1("Dodds"))
        self.assertEqual("D200", s.encode1("Dhdds"))
        self.assertEqual("D200", s.encode1("Dwdds"))

    def testGenealogy_test0_decomposed(self) -> None:
        s = Soundex.US_ENGLISH_GENEALOGY
        self.assertEqual("H251", s.encode1("Heggenburger"))

    def testWikipediaAmericanSoundex_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))

    def testWikipediaAmericanSoundex_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))
        self.getStringEncoder()

    def testWikipediaAmericanSoundex_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))

    def testWikipediaAmericanSoundex_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()

    def testWikipediaAmericanSoundex_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))

    def testWikipediaAmericanSoundex_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()

    def testWikipediaAmericanSoundex_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))

    def testWikipediaAmericanSoundex_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))
        self.getStringEncoder()

    def testWikipediaAmericanSoundex_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Rupert"))

    def testWikipediaAmericanSoundex_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()

    def testWikipediaAmericanSoundex_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))

    def testWikipediaAmericanSoundex_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testUsMappingOWithDiaeresis_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("O000", self.getStringEncoder().encode1("o"))

        if "\u00f6".isalpha():  # Check if 'ö' (o-umlaut) is a letter
            try:
                self.assertEqual("\u00d6000", self.getStringEncoder().encode1("\u00f6"))
                pytest.fail("Expected ValueError not thrown")
            except ValueError:
                pass  # Exception is expected, so we do nothing here
        else:
            self.assertEqual("", self.getStringEncoder().encode1("\u00f6"))

    def testUsMappingOWithDiaeresis_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testUsMappingEWithAcute_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("E000", self.getStringEncoder().encode1("e"))

        if "\u00e9".isalpha():  # e-acute
            with pytest.raises(ValueError):
                self.assertEqual("\u00c9000", self.getStringEncoder().encode1("\u00e9"))
        else:
            self.assertEqual("", self.getStringEncoder().encode1("\u00e9"))

    def testUsMappingEWithAcute_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testUsEnglishStatic_test0_decomposed(self) -> None:
        self.assertEqual("W452", Soundex.US_ENGLISH.soundex("Williams"))

    def testSoundexUtilsNullBehaviour_test1_decomposed(self) -> None:
        self.assertIsNone(SoundexUtils.clean(None))
        self.assertEqual("", SoundexUtils.clean(""))
        self.assertEqual(0, SoundexUtils.differenceEncoded(None, ""))
        self.assertEqual(0, SoundexUtils.differenceEncoded("", None))

    def testSoundexUtilsNullBehaviour_test0_decomposed(self) -> None:
        self.assertIsNone(SoundexUtils.clean(None))
        self.assertEqual("", SoundexUtils.clean(""))

    def testSoundexUtilsConstructable_test0_decomposed(self) -> None:
        SoundexUtils()

    def testNewInstance3_test0_decomposed(self) -> None:
        self.assertEqual(
            "W452",
            Soundex(1, False, Soundex.US_ENGLISH_MAPPING_STRING, None).soundex(
                "Williams"
            ),
        )

    def testNewInstance2_test0_decomposed(self) -> None:
        self.assertEqual(
            "W452",
            Soundex(2, False, None, list(Soundex.US_ENGLISH_MAPPING_STRING)).soundex(
                "Williams"
            ),
        )

    def testNewInstance_test0_decomposed(self) -> None:
        self.assertEqual("W452", Soundex(3, False, None, None).soundex("Williams"))

    def testMsSqlServer3_test17_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("L600", self.getStringEncoder().encode1("Laura"))
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Anne"))

    def testMsSqlServer3_test16_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("L600", self.getStringEncoder().encode1("Laura"))
        self.getStringEncoder()

    def testMsSqlServer3_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()
        self.assertEqual("L600", self.getStringEncoder().encode1("Laura"))

    def testMsSqlServer3_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))
        self.getStringEncoder()

    def testMsSqlServer3_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()
        self.assertEqual("R163", self.getStringEncoder().encode1("Robert"))

    def testMsSqlServer3_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))
        self.getStringEncoder()

    def testMsSqlServer3_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()
        self.assertEqual("M240", self.getStringEncoder().encode1("Michael"))

    def testMsSqlServer3_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))
        self.getStringEncoder()

    def testMsSqlServer3_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()
        self.assertEqual("S315", self.getStringEncoder().encode1("Steven"))

    def testMsSqlServer3_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))
        self.getStringEncoder()

    def testMsSqlServer3_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()
        self.assertEqual("M626", self.getStringEncoder().encode1("Margaret"))

    def testMsSqlServer3_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))
        self.getStringEncoder()

    def testMsSqlServer3_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()
        self.assertEqual("J530", self.getStringEncoder().encode1("Janet"))

    def testMsSqlServer3_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))
        self.getStringEncoder()

    def testMsSqlServer3_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()
        self.assertEqual("A536", self.getStringEncoder().encode1("Andrew"))

    def testMsSqlServer3_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))
        self.getStringEncoder()

    def testMsSqlServer3_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A500", self.getStringEncoder().encode1("Ann"))

    def testMsSqlServer3_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testMsSqlServer2_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "E625",
            ["Erickson", "Erickson", "Erikson", "Ericson", "Ericksen", "Ericsen"],
        )

    def testMsSqlServer1_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S530", self.getStringEncoder().encode1("Smith"))
        self.getStringEncoder()
        self.assertEqual("S530", self.getStringEncoder().encode1("Smythe"))

    def testMsSqlServer1_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S530", self.getStringEncoder().encode1("Smith"))
        self.getStringEncoder()

    def testMsSqlServer1_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S530", self.getStringEncoder().encode1("Smith"))

    def testMsSqlServer1_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testHWRuleEx3_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Sgler"))
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Swhgler"))
        self.checkEncodingVariations(
            "S460",
            [
                "SAILOR",
                "SALYER",
                "SAYLOR",
                "SCHALLER",
                "SCHELLER",
                "SCHILLER",
                "SCHOOLER",
                "SCHULER",
                "SCHUYLER",
                "SEILER",
                "SEYLER",
                "SHOLAR",
                "SHULER",
                "SILAR",
                "SILER",
                "SILLER",
            ],
        )

    def testHWRuleEx3_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Sgler"))
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Swhgler"))

    def testHWRuleEx3_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Sgler"))
        self.getStringEncoder()

    def testHWRuleEx3_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("S460", self.getStringEncoder().encode1("Sgler"))

    def testHWRuleEx3_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testHWRuleEx2_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTHDAVIS"))
        self.getStringEncoder()
        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTH-DAVIS"))

    def testHWRuleEx2_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTHDAVIS"))
        self.getStringEncoder()

    def testHWRuleEx2_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("B312", self.getStringEncoder().encode1("BOOTHDAVIS"))

    def testHWRuleEx2_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testHWRuleEx1_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("Y330", self.getStringEncoder().encode1("yehudit"))
        self.getStringEncoder()
        self.assertEqual("Y330", self.getStringEncoder().encode1("yhwdyt"))

    def testHWRuleEx1_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("Y330", self.getStringEncoder().encode1("yehudit"))
        self.getStringEncoder()

    def testHWRuleEx1_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()
        self.assertEqual("Y330", self.getStringEncoder().encode1("yehudit"))

    def testHWRuleEx1_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))
        self.getStringEncoder()

    def testHWRuleEx1_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcroft"))

    def testHWRuleEx1_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))
        self.getStringEncoder()

    def testHWRuleEx1_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A261", self.getStringEncoder().encode1("Ashcraft"))

    def testHWRuleEx1_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testEncodeIgnoreTrimmable_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("W252", encoder.encode1(" \t\n\r Washington \t\n\r "))

    def testEncodeIgnoreTrimmable_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testEncodeIgnoreHyphens_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "K525",
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
            "O165",
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

    def testEncodeBatch4_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))
        self.getStringEncoder()
        self.assertEqual("S545", self.getStringEncoder().encode1("SCANLON"))
        self.getStringEncoder()
        self.assertEqual("S532", self.getStringEncoder().encode1("SAINTJOHN"))

    def testEncodeBatch4_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))
        self.getStringEncoder()
        self.assertEqual("S545", self.getStringEncoder().encode1("SCANLON"))
        self.getStringEncoder()

    def testEncodeBatch4_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))
        self.getStringEncoder()
        self.assertEqual("S545", self.getStringEncoder().encode1("SCANLON"))

    def testEncodeBatch4_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))
        self.getStringEncoder()

    def testEncodeBatch4_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("JACKSON"))

    def testEncodeBatch4_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))
        self.getStringEncoder()

    def testEncodeBatch4_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()
        self.assertEqual("S000", self.getStringEncoder().encode1("SHAW"))

    def testEncodeBatch4_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))
        self.getStringEncoder()

    def testEncodeBatch4_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()
        self.assertEqual("B400", self.getStringEncoder().encode1("BALL"))

    def testEncodeBatch4_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))
        self.getStringEncoder()

    def testEncodeBatch4_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()
        self.assertEqual("V536", self.getStringEncoder().encode1("VONDERLEHR"))

    def testEncodeBatch4_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))
        self.getStringEncoder()

    def testEncodeBatch4_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()
        self.assertEqual("A355", self.getStringEncoder().encode1("ADOMOMI"))

    def testEncodeBatch4_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))
        self.getStringEncoder()

    def testEncodeBatch4_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOLMES"))

    def testEncodeBatch4_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testEncodeBatch3_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("Jackson"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))
        self.getStringEncoder()
        self.assertEqual("V532", self.getStringEncoder().encode1("VanDeusen"))

    def testEncodeBatch3_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("Jackson"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))
        self.getStringEncoder()

    def testEncodeBatch3_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("Jackson"))
        self.getStringEncoder()
        self.assertEqual("T522", self.getStringEncoder().encode1("Tymczak"))

    def testEncodeBatch3_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("Jackson"))
        self.getStringEncoder()

    def testEncodeBatch3_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()
        self.assertEqual("J250", self.getStringEncoder().encode1("Jackson"))

    def testEncodeBatch3_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))
        self.getStringEncoder()

    def testEncodeBatch3_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()
        self.assertEqual("P236", self.getStringEncoder().encode1("Pfister"))

    def testEncodeBatch3_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))
        self.getStringEncoder()

    def testEncodeBatch3_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()
        self.assertEqual("G362", self.getStringEncoder().encode1("Gutierrez"))

    def testEncodeBatch3_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))
        self.getStringEncoder()

    def testEncodeBatch3_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()
        self.assertEqual("L000", self.getStringEncoder().encode1("Lee"))

    def testEncodeBatch3_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))
        self.getStringEncoder()

    def testEncodeBatch3_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("W252", self.getStringEncoder().encode1("Washington"))

    def testEncodeBatch3_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testEncodeBatch2_test31_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.getStringEncoder()
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))
        self.getStringEncoder()
        self.assertEqual("Z300", self.getStringEncoder().encode1("Zita"))
        self.getStringEncoder()
        self.assertEqual("Z325", self.getStringEncoder().encode1("Zitzmeinn"))

    def testEncodeBatch2_test30_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.getStringEncoder()
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))
        self.getStringEncoder()
        self.assertEqual("Z300", self.getStringEncoder().encode1("Zita"))
        self.getStringEncoder()

    def testEncodeBatch2_test29_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.getStringEncoder()
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))
        self.getStringEncoder()
        self.assertEqual("Z300", self.getStringEncoder().encode1("Zita"))

    def testEncodeBatch2_test28_decomposed(self) -> None:
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))

    def testEncodeBatch2_test27_decomposed(self) -> None:
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.assertEqual("R355", self.getStringEncoder().encode1("Riedemanas"))

    def testEncodeBatch2_test26_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))
        self.getStringEncoder()

    def testEncodeBatch2_test25_decomposed(self) -> None:
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Oppenheimer"))

    def testEncodeBatch2_test24_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))
        self.getStringEncoder()

    def testEncodeBatch2_test23_decomposed(self) -> None:
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.assertEqual("O155", self.getStringEncoder().encode1("Opnian"))

    def testEncodeBatch2_test22_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))
        self.getStringEncoder()

    def testEncodeBatch2_test21_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()
        self.assertEqual("M200", self.getStringEncoder().encode1("McGee"))

    def testEncodeBatch2_test20_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))
        self.getStringEncoder()

    def testEncodeBatch2_test19_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()
        self.assertEqual("M235", self.getStringEncoder().encode1("McDonnell"))

    def testEncodeBatch2_test18_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))
        self.getStringEncoder()

    def testEncodeBatch2_test17_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()
        self.assertEqual("L222", self.getStringEncoder().encode1("Lukaschowsky"))

    def testEncodeBatch2_test16_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))
        self.getStringEncoder()

    def testEncodeBatch2_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()
        self.assertEqual("L530", self.getStringEncoder().encode1("Lind"))

    def testEncodeBatch2_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))
        self.getStringEncoder()

    def testEncodeBatch2_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()
        self.assertEqual("K152", self.getStringEncoder().encode1("Kavanagh"))

    def testEncodeBatch2_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))
        self.getStringEncoder()

    def testEncodeBatch2_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()
        self.assertEqual("H431", self.getStringEncoder().encode1("Hildebrand"))

    def testEncodeBatch2_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))
        self.getStringEncoder()

    def testEncodeBatch2_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()
        self.assertEqual("H524", self.getStringEncoder().encode1("Hanselmann"))

    def testEncodeBatch2_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))
        self.getStringEncoder()

    def testEncodeBatch2_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()
        self.assertEqual("H512", self.getStringEncoder().encode1("Heimbach"))

    def testEncodeBatch2_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))
        self.getStringEncoder()

    def testEncodeBatch2_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()
        self.assertEqual("E521", self.getStringEncoder().encode1("Engebrethson"))

    def testEncodeBatch2_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))
        self.getStringEncoder()

    def testEncodeBatch2_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()
        self.assertEqual("E166", self.getStringEncoder().encode1("Eberhard"))

    def testEncodeBatch2_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))
        self.getStringEncoder()

    def testEncodeBatch2_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("A462", self.getStringEncoder().encode1("Allricht"))

    def testEncodeBatch2_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testEncodeBasic_test19_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))
        self.getStringEncoder()
        self.assertEqual("L200", self.getStringEncoder().encode1("lazy"))
        self.getStringEncoder()
        self.assertEqual("D200", self.getStringEncoder().encode1("dogs"))

    def testEncodeBasic_test18_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))
        self.getStringEncoder()
        self.assertEqual("L200", self.getStringEncoder().encode1("lazy"))
        self.getStringEncoder()

    def testEncodeBasic_test17_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))
        self.getStringEncoder()
        self.assertEqual("L200", self.getStringEncoder().encode1("lazy"))

    def testEncodeBasic_test16_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))
        self.getStringEncoder()

    def testEncodeBasic_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("the"))

    def testEncodeBasic_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))
        self.getStringEncoder()

    def testEncodeBasic_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()
        self.assertEqual("O160", self.getStringEncoder().encode1("over"))

    def testEncodeBasic_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))
        self.getStringEncoder()

    def testEncodeBasic_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()
        self.assertEqual("J513", self.getStringEncoder().encode1("jumped"))

    def testEncodeBasic_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))
        self.getStringEncoder()

    def testEncodeBasic_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()
        self.assertEqual("F200", self.getStringEncoder().encode1("fox"))

    def testEncodeBasic_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))
        self.getStringEncoder()

    def testEncodeBasic_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()
        self.assertEqual("B650", self.getStringEncoder().encode1("brown"))

    def testEncodeBasic_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))
        self.getStringEncoder()

    def testEncodeBasic_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()
        self.assertEqual("Q200", self.getStringEncoder().encode1("quick"))

    def testEncodeBasic_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))
        self.getStringEncoder()

    def testEncodeBasic_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()
        self.assertEqual("T000", self.getStringEncoder().encode1("The"))

    def testEncodeBasic_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("T235", self.getStringEncoder().encode1("testing"))
        self.getStringEncoder()

    def testEncodeBasic_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertEqual("T235", encoder.encode1("testing"))

    def testEncodeBasic_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testDifference_test23_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smithers", "Smythers"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Anothers", "Brothers"))

    def testDifference_test22_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smithers", "Smythers"))
        self.getStringEncoder()

    def testDifference_test21_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smithers", "Smythers"))

    def testDifference_test20_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()

    def testDifference_test19_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))

    def testDifference_test18_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )
        self.getStringEncoder()

    def testDifference_test17_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()
        self.assertEqual(
            0, self.getStringEncoder().difference("Blotchet-Halls", "Greene")
        )

    def testDifference_test16_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))
        self.getStringEncoder()

    def testDifference_test15_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Green", "Greene"))

    def testDifference_test14_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))
        self.getStringEncoder()

    def testDifference_test13_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("Janet", "Margaret"))

    def testDifference_test12_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))
        self.getStringEncoder()

    def testDifference_test11_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()
        self.assertEqual(1, self.getStringEncoder().difference("Margaret", "Andrew"))

    def testDifference_test10_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))
        self.getStringEncoder()

    def testDifference_test9_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()
        self.assertEqual(2, self.getStringEncoder().difference("Ann", "Andrew"))

    def testDifference_test8_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))
        self.getStringEncoder()

    def testDifference_test7_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()
        self.assertEqual(4, self.getStringEncoder().difference("Smith", "Smythe"))

    def testDifference_test6_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))
        self.getStringEncoder()

    def testDifference_test5_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(" ", " "))

    def testDifference_test4_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))
        self.getStringEncoder()

    def testDifference_test3_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference("", ""))

    def testDifference_test2_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual(0, self.getStringEncoder().difference(None, None))
        self.getStringEncoder()

    def testDifference_test1_decomposed(self) -> None:
        encoder = self.getStringEncoder()
        self.assertIsNotNone(encoder, "Encoder instance is None")
        self.assertEqual(0, encoder.difference(None, None))

    def testDifference_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testBadCharacters_test1_decomposed(self) -> None:
        self.getStringEncoder()
        self.assertEqual("H452", self.getStringEncoder().encode1("HOL>MES"))

    def testBadCharacters_test0_decomposed(self) -> None:
        self.getStringEncoder()

    def testB650_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "B650",
            [
                "BARHAM",
                "BARONE",
                "BARRON",
                "BERNA",
                "BIRNEY",
                "BIRNIE",
                "BOOROM",
                "BOREN",
                "BORN",
                "BOURN",
                "BOURNE",
                "BOWRON",
                "BRAIN",
                "BRAME",
                "BRANN",
                "BRAUN",
                "BREEN",
                "BRIEN",
                "BRIM",
                "BRIMM",
                "BRINN",
                "BRION",
                "BROOM",
                "BROOME",
                "BROWN",
                "BROWNE",
                "BRUEN",
                "BRUHN",
                "BRUIN",
                "BRUMM",
                "BRUN",
                "BRUNO",
                "BRYAN",
                "BURIAN",
                "BURN",
                "BURNEY",
                "BYRAM",
                "BYRNE",
                "BYRON",
                "BYRUM",
            ],
        )

    def _createStringEncoder(self) -> Soundex:
        return Soundex(3, False, None, None)
