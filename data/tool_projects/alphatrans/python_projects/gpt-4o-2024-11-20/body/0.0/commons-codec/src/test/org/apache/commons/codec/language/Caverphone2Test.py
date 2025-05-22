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
from src.main.org.apache.commons.codec.language.Caverphone2 import *


class Caverphone2Test(StringEncoderAbstractTest, unittest.TestCase):

    def testSpecificationExamples_test0_decomposed(self) -> None:
        data = [
            ("Peter", "PTA1111111"),
            ("ready", "RTA1111111"),
            ("social", "SSA1111111"),
            ("able", "APA1111111"),
            ("Tedder", "TTA1111111"),
            ("Karleen", "KLN1111111"),
            ("Dyun", "TN11111111"),
        ]
        self.checkEncodings(data)

    def testIsCaverphoneEquals_test1_decomposed(self) -> None:
        caverphone = Caverphone2()
        self.assertFalse(
            caverphone.isEncodeEqual("Peter", "Stevenson"),
            "Caverphone encodings should not be equal",
        )
        self.assertTrue(
            caverphone.isEncodeEqual("Peter", "Peady"),
            "Caverphone encodings should be equal",
        )

    def testIsCaverphoneEquals_test0_decomposed(self) -> None:
        caverphone = Caverphone2()

    def testEndMb_test0_decomposed(self) -> None:
        data = [["mb", "M111111111"], ["mbmb", "MPM1111111"]]
        self.check_encodings(data)

    def testCaverphoneRevisitedRandomWords_test2_decomposed(self) -> None:
        self.check_encoding_variations("RTA1111111", ["rather", "ready", "writer"])
        self.check_encoding("SSA1111111", "social")
        self.check_encoding_variations("APA1111111", ["able", "appear"])

    def testCaverphoneRevisitedRandomWords_test1_decomposed(self) -> None:
        self.checkEncodingVariations("RTA1111111", ["rather", "ready", "writer"])
        self.checkEncoding("SSA1111111", "social")

    def testCaverphoneRevisitedRandomWords_test0_decomposed(self) -> None:
        self.checkEncodingVariations("RTA1111111", ["rather", "ready", "writer"])

    def testCaverphoneRevisitedRandomNameTTA1111111_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "TTA1111111",
            [
                "Darda",
                "Datha",
                "Dedie",
                "Deedee",
                "Deerdre",
                "Deidre",
                "Deirdre",
                "Detta",
                "Didi",
                "Didier",
                "Dido",
                "Dierdre",
                "Dieter",
                "Dita",
                "Ditter",
                "Dodi",
                "Dodie",
                "Dody",
                "Doherty",
                "Dorthea",
                "Dorthy",
                "Doti",
                "Dotti",
                "Dottie",
                "Dotty",
                "Doty",
                "Doughty",
                "Douty",
                "Dowdell",
                "Duthie",
                "Tada",
                "Taddeo",
                "Tadeo",
                "Tadio",
                "Tati",
                "Teador",
                "Tedda",
                "Tedder",
                "Teddi",
                "Teddie",
                "Teddy",
                "Tedi",
                "Tedie",
                "Teeter",
                "Teodoor",
                "Teodor",
                "Terti",
                "Theda",
                "Theodor",
                "Theodore",
                "Theta",
                "Thilda",
                "Thordia",
                "Tilda",
                "Tildi",
                "Tildie",
                "Tildy",
                "Tita",
                "Tito",
                "Tjader",
                "Toddie",
                "Toddy",
                "Torto",
                "Tuddor",
                "Tudor",
                "Turtle",
                "Tuttle",
                "Tutto",
            ],
        )

    def testCaverphoneRevisitedRandomNameTN11111111_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "TN11111111",
            [
                "Dan",
                "Dane",
                "Dann",
                "Darn",
                "Daune",
                "Dawn",
                "Ddene",
                "Dean",
                "Deane",
                "Deanne",
                "DeeAnn",
                "Deeann",
                "Deeanne",
                "Deeyn",
                "Den",
                "Dene",
                "Denn",
                "Deonne",
                "Diahann",
                "Dian",
                "Diane",
                "Diann",
                "Dianne",
                "Diannne",
                "Dine",
                "Dion",
                "Dione",
                "Dionne",
                "Doane",
                "Doehne",
                "Don",
                "Donn",
                "Doone",
                "Dorn",
                "Down",
                "Downe",
                "Duane",
                "Dun",
                "Dunn",
                "Duyne",
                "Dyan",
                "Dyane",
                "Dyann",
                "Dyanne",
                "Dyun",
                "Tan",
                "Tann",
                "Teahan",
                "Ten",
                "Tenn",
                "Terhune",
                "Thain",
                "Thaine",
                "Thane",
                "Thanh",
                "Thayne",
                "Theone",
                "Thin",
                "Thorn",
                "Thorne",
                "Thun",
                "Thynne",
                "Tien",
                "Tine",
                "Tjon",
                "Town",
                "Towne",
                "Turne",
                "Tyne",
            ],
        )

    def testCaverphoneRevisitedRandomNameKLN1111111_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "KLN1111111",
            [
                "Cailean",
                "Calan",
                "Calen",
                "Callahan",
                "Callan",
                "Callean",
                "Carleen",
                "Carlen",
                "Carlene",
                "Carlin",
                "Carline",
                "Carlyn",
                "Carlynn",
                "Carlynne",
                "Charlean",
                "Charleen",
                "Charlene",
                "Charline",
                "Cherlyn",
                "Chirlin",
                "Clein",
                "Cleon",
                "Cline",
                "Cohleen",
                "Colan",
                "Coleen",
                "Colene",
                "Colin",
                "Colleen",
                "Collen",
                "Collin",
                "Colline",
                "Colon",
                "Cullan",
                "Cullen",
                "Cullin",
                "Gaelan",
                "Galan",
                "Galen",
                "Garlan",
                "Garlen",
                "Gaulin",
                "Gayleen",
                "Gaylene",
                "Giliane",
                "Gillan",
                "Gillian",
                "Glen",
                "Glenn",
                "Glyn",
                "Glynn",
                "Gollin",
                "Gorlin",
                "Kalin",
                "Karlan",
                "Karleen",
                "Karlen",
                "Karlene",
                "Karlin",
                "Karlyn",
                "Kaylyn",
                "Keelin",
                "Kellen",
                "Kellene",
                "Kellyann",
                "Kellyn",
                "Khalin",
                "Kilan",
                "Kilian",
                "Killen",
                "Killian",
                "Killion",
                "Klein",
                "Kleon",
                "Kline",
                "Koerlin",
                "Kylen",
                "Kylynn",
                "Quillan",
                "Quillon",
                "Qulllon",
                "Xylon",
            ],
        )

    def testCaverphoneRevisitedExamples_test0_decomposed(self) -> None:
        data = [["Stevenson", "STFNSN1111"], ["Peter", "PTA1111111"]]
        self.check_encodings(data)

    def testCaverphoneRevisitedCommonCodeAT11111111_test0_decomposed(self) -> None:
        self.check_encoding_variations(
            "AT11111111",
            [
                "add",
                "aid",
                "at",
                "art",
                "eat",
                "earth",
                "head",
                "hit",
                "hot",
                "hold",
                "hard",
                "heart",
                "it",
                "out",
                "old",
            ],
        )

    def _createStringEncoder(self) -> Caverphone2:
        return Caverphone2()
