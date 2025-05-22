from __future__ import annotations
import time
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
from src.main.org.apache.commons.codec.language.bm.BeiderMorseEncoder import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class BeiderMorseEncoderTest(StringEncoderAbstractTest, unittest.TestCase):

    __TEST_CHARS: typing.List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "o", "u"]

    def testSpeedCheck3_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        phrase = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[:i])

    def testSpeedCheck3_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testSpeedCheck2_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        phrase = "ItstheendoftheworldasweknowitandIfeelfine"
        for i in range(1, len(phrase) + 1):
            bmpm.encode0(phrase[:i])

    def testSpeedCheck2_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testSpeedCheck_test2_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        string_buffer = [
            self.__TEST_CHARS[0]
        ]  # Using a list to mimic StringBuilder behavior
        for i in range(40):
            j = (i + 1) % len(self.__TEST_CHARS)  # Calculate the index for TEST_CHARS
            bmpm.encode1("".join(string_buffer))  # Join the list to form a string
            string_buffer.append(self.__TEST_CHARS[j])  # Append the next character

    def testSpeedCheck_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        string_buffer = []
        string_buffer.append(self.__TEST_CHARS[0])

    def testSpeedCheck_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testSetRuleTypeToRulesValueError_test1_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        with self.assertRaises(ValueError):
            bmpm.setRuleType(RuleType.RULES)

    def testSetRuleTypeToRulesValueError_test0_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()

    def testSetRuleTypeExact_test2_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setRuleType(RuleType.EXACT)
        self.assertEqual(
            RuleType.EXACT,
            bmpm.getRuleType(),
            "Rule type should have been set to exact",
        )

    def testSetRuleTypeExact_test1_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setRuleType(RuleType.EXACT)

    def testSetRuleTypeExact_test0_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()

    def testSetNameTypeAsh_test2_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setNameType(NameType.ASHKENAZI)
        self.assertEqual(
            NameType.ASHKENAZI,
            bmpm.getNameType(),
            "Name type should have been set to ash",
        )

    def testSetNameTypeAsh_test1_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setNameType(NameType.ASHKENAZI)

    def testSetNameTypeAsh_test0_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()

    def testSetConcat_test2_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setConcat(False)
        self.assertFalse(bmpm.isConcat(), "Should be able to set concat to false")

    def testSetConcat_test1_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()
        bmpm.setConcat(False)

    def testSetConcat_test0_decomposed(self) -> None:
        bmpm = BeiderMorseEncoder()

    def testOOM_test6_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)
        phonemes = encoder.encode1(phrase)
        self.assertFalse(phonemes == "")
        phoneme_arr = phonemes.split("|")
        self.assertTrue(len(phoneme_arr) <= 10)

    def testOOM_test5_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)
        phonemes = encoder.encode1(phrase)
        self.assertFalse(phonemes == "")

    def testOOM_test4_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)
        phonemes = encoder.encode1(phrase)

    def testOOM_test3_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)
        encoder.setMaxPhonemes(10)

    def testOOM_test2_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.EXACT)

    def testOOM_test1_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)

    def testOOM_test0_decomposed(self) -> None:
        phrase = (
            "200697900'-->&#1913348150;</  bceaeef"
            + " >aadaabcf\"aedfbff<!--'-->?>caecfaaa><?&#<!--</script>&lang&fc;aadeaf?>>&bdquo<"
            + '    cc ="abff"    /></   afe  ><script><!-- f(\';<    cf aefbeef ='
            + ' "bfabadcf" ebbfeedd = fccabeb >'
        )
        encoder = BeiderMorseEncoder()

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException_test1_decomposed(
        self,
    ) -> None:
        r = Rule("a", "", "", Phoneme(2, "", Languages.ANY_LANGUAGE, None))
        with self.assertRaises(IndexError):
            r.patternAndContextMatches("bob", -1)

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException_test0_decomposed(
        self,
    ) -> None:
        r = Rule("a", "", "", Phoneme(2, "", Languages.ANY_LANGUAGE, None))

    def testLongestEnglishSurname_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        bmpm.encode1("MacGhilleseatheanaich")

    def testLongestEnglishSurname_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testInvalidLanguageValueError_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Languages.getInstance1("thereIsNoSuchLanguage")

    def testInvalidLangRuntimeError_test1_decomposed(self) -> None:
        with self.assertRaises(
            ValueError
        ):  # Assuming ValueError maps to ValueError in Python
            Languages.getInstance0(NameType.GENERIC)
            Lang.loadFromResource(
                "thisIsAMadeUpResourceName", Languages.getInstance0(NameType.GENERIC)
            )

    def testInvalidLangRuntimeError_test0_decomposed(self) -> None:
        Languages.getInstance0(NameType.GENERIC)

    def testInvalidLangValueError_test0_decomposed(self) -> None:
        with self.assertRaises(ValueError):
            Rule.getInstance1(NameType.GENERIC, RuleType.APPROX, "noSuchLanguage")

    def testEncodeGna_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        result = bmpm.encode1("gna")
        # Add assertions here if needed, e.g., to check the result

    def testEncodeGna_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testEncodeAtzNotEmpty_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        names = ["\u00e1cz", "\u00e1tz", "Ign\u00e1cz", "Ign\u00e1tz", "Ign\u00e1c"]
        for name in names:
            self.__assertNotEmpty(bmpm, name)

    def testEncodeAtzNotEmpty_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testAsciiEncodeNotEmpty2Letters_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        for c1 in range(ord("a"), ord("z") + 1):
            for c2 in range(ord("a"), ord("z") + 1):
                value = chr(c1) + chr(c2)
                valueU = value.upper()
                self.__assertNotEmpty(bmpm, value)
                self.__assertNotEmpty(bmpm, valueU)

    def testAsciiEncodeNotEmpty2Letters_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testAsciiEncodeNotEmpty1Letter_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        for c in range(ord("a"), ord("z") + 1):
            value = chr(c)
            valueU = value.upper()
            self.__assertNotEmpty(bmpm, value)
            self.__assertNotEmpty(bmpm, valueU)

    def testAsciiEncodeNotEmpty1Letter_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def testAllChars_test1_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()
        for c in range(0, 0xFFFF):  # 0 to 65535 in Java
            bmpm.encode1(chr(c))

    def testAllChars_test0_decomposed(self) -> None:
        bmpm = self.__createGenericApproxEncoder()

    def _createStringEncoder(self) -> StringEncoder:
        return BeiderMorseEncoder()

    def __createGenericApproxEncoder(self) -> BeiderMorseEncoder:
        encoder = BeiderMorseEncoder()
        encoder.setNameType(NameType.GENERIC)
        encoder.setRuleType(RuleType.APPROX)
        return encoder

    def __assertNotEmpty(self, bmpm: BeiderMorseEncoder, value: str) -> None:
        self.assertNotEqual(value, "", bmpm.encode1(value))
