from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEngineRegressionTest(unittest.TestCase):

    def testCompatibilityWithOriginalVersion_test4_decomposed(self) -> None:
        args = {"nameType": "GENERIC", "ruleType": "APPROX"}
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom",
        )
        self.assertEqual(
            self.__encode(args, True, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn"
        )
        args["nameType"] = "ASHKENAZI"
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abrom|avram|avrom|imbram|imbrom|obram|obrom|ombram|ombrom|ovram|ovrom",
        )
        self.assertEqual(
            self.__encode(args, True, "Halpern"),
            "YlpYrn|Ylpirn|alpYrn|alpirn|olpYrn|olpirn|xalpirn|xolpirn",
        )

    def testCompatibilityWithOriginalVersion_test3_decomposed(self) -> None:
        args = {"nameType": "GENERIC", "ruleType": "APPROX"}
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom",
        )
        self.assertEqual(
            self.__encode(args, True, "Bendzin"), "bndzn|bntsn|bnzn|vndzn|vntsn"
        )
        args["nameType"] = "ASHKENAZI"
        args["ruleType"] = "APPROX"

    def testCompatibilityWithOriginalVersion_test2_decomposed(self) -> None:
        args = {"nameType": "GENERIC", "ruleType": "APPROX"}
        self.assertEqual(
            self.__encode(args, True, "abram"),
            "Ybram|Ybrom|abram|abran|abrom|abron|avram|avrom|obram|obran|obrom|obron|ovram|ovrom",
            "Encoding for 'abram' did not match the expected result",
        )
        self.assertEqual(
            self.__encode(args, True, "Bendzin"),
            "bndzn|bntsn|bnzn|vndzn|vntsn",
            "Encoding for 'Bendzin' did not match the expected result",
        )

    def testCompatibilityWithOriginalVersion_test1_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"
        args["ruleType"] = "APPROX"

    def testCompatibilityWithOriginalVersion_test0_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"

    def testSolrSEPHARDIC_test23_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrSEPHARDIC_test22_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrSEPHARDIC_test21_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "danhila|danhilu|danzila|danzilu|nhila|nhilu|nzila|nzilu",
        )

    def testSolrSEPHARDIC_test20_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"

    def testSolrSEPHARDIC_test19_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )

    def testSolrSEPHARDIC_test18_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"

    def testSolrSEPHARDIC_test17_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrSEPHARDIC_test16_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrSEPHARDIC_test15_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )

    def testSolrSEPHARDIC_test14_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "APPROX"

    def testSolrSEPHARDIC_test13_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )

    def testSolrSEPHARDIC_test12_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"

    def testSolrSEPHARDIC_test11_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrSEPHARDIC_test10_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrSEPHARDIC_test9_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, False, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "danZelo|dandZelo|danxelo"
        )

    def testSolrSEPHARDIC_test8_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"

    def testSolrSEPHARDIC_test7_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )

    def testSolrSEPHARDIC_test6_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "SEPHARDIC"

    def testSolrSEPHARDIC_test5_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrSEPHARDIC_test4_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")
        args["languageSet"] = "italian,greek,spanish"

    def testSolrSEPHARDIC_test3_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(self.__encode(args, True, "Angelo"), "anZelo|andZelo|anxelo")
        self.assertEqual(self.__encode(args, True, "D'Angelo"), "anZelo|andZelo|anxelo")

    def testSolrSEPHARDIC_test2_decomposed(self) -> None:
        args = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
        )
        args["ruleType"] = "EXACT"

    def testSolrSEPHARDIC_test1_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "SEPHARDIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anhila|anhilu|anzila|anzilu|nhila|nhilu|nzila|nzilu",
            "Encoded output does not match the expected result",
        )

    def testSolrSEPHARDIC_test0_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "SEPHARDIC"

    def testSolrASHKENAZI_test23_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrASHKENAZI_test22_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrASHKENAZI_test21_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )

    def testSolrASHKENAZI_test20_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"

    def testSolrASHKENAZI_test19_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )

    def testSolrASHKENAZI_test18_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"

    def testSolrASHKENAZI_test17_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "angilo|anxilo|ongilo|onxilo"
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrASHKENAZI_test16_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrASHKENAZI_test15_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "dYngYlo|dYngilo|dangYlo|dangilo|danilo|danxilo|danzilo|dongYlo|dongilo|donilo|donxilo|donzilo",
        )

    def testSolrASHKENAZI_test14_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"

    def testSolrASHKENAZI_test13_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )

    def testSolrASHKENAZI_test12_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"

    def testSolrASHKENAZI_test11_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrASHKENAZI_test10_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrASHKENAZI_test9_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )

    def testSolrASHKENAZI_test8_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"

    def testSolrASHKENAZI_test7_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )

    def testSolrASHKENAZI_test6_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        args["nameType"] = "ASHKENAZI"

    def testSolrASHKENAZI_test5_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrASHKENAZI_test4_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrASHKENAZI_test3_decomposed(self) -> None:
        args = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"), "andZelo|angelo|anhelo|anxelo"
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"), "dandZelo|dangelo|danhelo|danxelo"
        )

    def testSolrASHKENAZI_test2_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"

    def testSolrASHKENAZI_test1_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "ASHKENAZI"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|angYlo|angilo|anilo|anxilo|anzilo|ongYlo|ongilo|onilo|onxilo|onzilo",
        )

    def testSolrASHKENAZI_test0_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "ASHKENAZI"

    def testSolrGENERIC_test20_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrGENERIC_test19_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrGENERIC_test18_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )

    def testSolrGENERIC_test17_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"

    def testSolrGENERIC_test16_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )

    def testSolrGENERIC_test15_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "angilo|anxilo|anzilo|ongilo|onxilo|onzilo",
        )
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrGENERIC_test14_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrGENERIC_test13_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo)-(dYngYlo|dYngilo|dagilo|dangYlo|dangilo|daniilo|danilo|danxilo|danzilo|dogilo|dongYlo|dongilo|doniilo|donilo|donxilo|donzilo)",
        )

    def testSolrGENERIC_test12_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "APPROX"

    def testSolrGENERIC_test11_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )

    def testSolrGENERIC_test10_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, False, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, False, "1234"), "")

    def testSolrGENERIC_test9_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrGENERIC_test8_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, False, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )

    def testSolrGENERIC_test7_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"

    def testSolrGENERIC_test6_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")
        args = {}
        self.assertEqual(
            self.__encode(args, False, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )

    def testSolrGENERIC_test5_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"
        self.assertEqual(self.__encode(args, True, "Angelo"), "andZelo|angelo|anxelo")
        self.assertEqual(self.__encode(args, True, "1234"), "")

    def testSolrGENERIC_test4_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )
        args["languageSet"] = "italian,greek,spanish"

    def testSolrGENERIC_test3_decomposed(self) -> None:
        args = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "anZelo|andZelo|angelo|anhelo|anjelo|anxelo",
        )
        self.assertEqual(
            self.__encode(args, True, "D'Angelo"),
            "(anZelo|andZelo|angelo|anhelo|anjelo|anxelo)-(danZelo|dandZelo|dangelo|danhelo|danjelo|danxelo)",
        )

    def testSolrGENERIC_test2_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
        )
        args["ruleType"] = "EXACT"

    def testSolrGENERIC_test1_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"
        self.assertEqual(
            self.__encode(args, True, "Angelo"),
            "YngYlo|Yngilo|agilo|angYlo|angilo|aniilo|anilo|anxilo|anzilo|ogilo|ongYlo|ongilo|oniilo|onilo|onxilo|onzilo",
            "Encoded output does not match the expected result",
        )

    def testSolrGENERIC_test0_decomposed(self) -> None:
        args: Dict[str, str] = {}
        args["nameType"] = "GENERIC"

    @staticmethod
    def __encode(args: typing.Dict[str, str], concat: bool, input_: str) -> str:
        name_type_arg = args.get("nameType")
        name_type = (
            NameType.GENERIC if name_type_arg is None else NameType[name_type_arg]
        )

        rule_type_arg = args.get("ruleType")
        rule_type = (
            RuleType.APPROX if rule_type_arg is None else RuleType[rule_type_arg]
        )

        engine = PhoneticEngine.PhoneticEngine0(name_type, rule_type, concat)

        language_set_arg = args.get("languageSet")
        if language_set_arg is None or language_set_arg == "auto":
            language_set = None
        else:
            language_set = LanguageSet.from_(set(language_set_arg.split(",")))

        if language_set is None:
            return engine.encode0(input_)
        return engine.encode1(input_, language_set)
