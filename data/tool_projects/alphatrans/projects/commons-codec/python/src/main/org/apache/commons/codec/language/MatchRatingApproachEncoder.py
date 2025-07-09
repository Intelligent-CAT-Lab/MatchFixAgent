from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class MatchRatingApproachEncoder(StringEncoder):

    __DOUBLE_CONSONANT: List[str] = [
        "BB",
        "CC",
        "DD",
        "FF",
        "GG",
        "HH",
        "JJ",
        "KK",
        "LL",
        "MM",
        "NN",
        "PP",
        "QQ",
        "RR",
        "SS",
        "TT",
        "VV",
        "WW",
        "XX",
        "YY",
        "ZZ",
    ]
    __UNICODE: str = (
        "\u00c0\u00e0\u00c8\u00e8\u00cc\u00ec\u00d2\u00f2\u00d9\u00f9"
        "\u00c1\u00e1\u00c9\u00e9\u00cd\u00ed\u00d3\u00f3\u00da\u00fa\u00dd\u00fd"
        "\u00c2\u00e2\u00ca\u00ea\u00ce\u00ee\u00d4\u00f4\u00db\u00fb\u0176\u0177"
        "\u00c3\u00e3\u00d5\u00f5\u00d1\u00f1"
        "\u00c4\u00e4\u00cb\u00eb\u00cf\u00ef\u00d6\u00f6\u00dc\u00fc\u0178\u00ff"
        "\u00c5\u00e5"
        "\u00c7\u00e7"
        "\u0150\u0151\u0170\u0171"
    )
    __PLAIN_ASCII: str = (
        "AaEeIiOoUu"
        + "AaEeIiOoUuYy"
        + "AaEeIiOoUuYy"
        + "AaOoNn"
        + "AaEeIiOoUuYy"
        + "Aa"
        + "Cc"
        + "OoUu"
    )
    __EMPTY: str = ""
    __SPACE: str = " "

    def isEncodeEquals(self, name1: str, name2: str) -> bool:
        if (
            name1 is None
            or name1.strip() == self.__EMPTY
            or name1.strip() == self.__SPACE
        ):
            return False
        if (
            name2 is None
            or name2.strip() == self.__EMPTY
            or name2.strip() == self.__SPACE
        ):
            return False
        if len(name1) == 1 or len(name2) == 1:
            return False
        if name1.lower() == name2.lower():
            return True

        name1 = self.cleanName(name1)
        name2 = self.cleanName(name2)

        name1 = self.removeVowels(name1)
        name2 = self.removeVowels(name2)

        name1 = self.removeDoubleConsonants(name1)
        name2 = self.removeDoubleConsonants(name2)

        name1 = self.getFirst3Last3(name1)
        name2 = self.getFirst3Last3(name2)

        if abs(len(name1) - len(name2)) >= 3:
            return False

        sumLength = abs(len(name1) + len(name2))
        minRating = self.getMinRating(sumLength)

        count = self.leftToRightThenRightToLeftProcessing(name1, name2)

        return count >= minRating

    def encode1(self, name: str) -> str:
        if (
            name is None
            or name.upper() == self.__EMPTY
            or name.upper() == self.__SPACE
            or len(name) == 1
        ):
            return self.__EMPTY

        name = self.cleanName(name)
        name = self.removeVowels(name)
        name = self.removeDoubleConsonants(name)
        name = self.getFirst3Last3(name)

        return name

    def encode0(self, pObject: typing.Any) -> typing.Any:
        if not isinstance(pObject, str):
            raise EncoderException(
                "Parameter supplied to Match Rating Approach encoder is not of type"
                " java.lang.String",
                None,
            )
        return self.encode1(pObject)

    def removeVowels(self, name: str) -> str:
        first_letter = name[0]

        name = name.replace("A", self.__EMPTY)
        name = name.replace("E", self.__EMPTY)
        name = name.replace("I", self.__EMPTY)
        name = name.replace("O", self.__EMPTY)
        name = name.replace("U", self.__EMPTY)

        name = " ".join(name.split())  # Replaces multiple spaces with a single space

        if self.isVowel(first_letter):
            return first_letter + name
        return name

    def removeDoubleConsonants(self, name: str) -> str:
        replaced_name = name.upper()
        for dc in self.__DOUBLE_CONSONANT:
            if dc in replaced_name:
                single_letter = dc[0]
                replaced_name = replaced_name.replace(dc, single_letter)
        return replaced_name

    def removeAccents(self, accentedWord: str) -> str:
        if accentedWord is None:
            return None

        sb = []
        n = len(accentedWord)

        for i in range(n):
            c = accentedWord[i]
            pos = self.__UNICODE.find(c)
            if pos > -1:
                sb.append(self.__PLAIN_ASCII[pos])
            else:
                sb.append(c)

        return "".join(sb)

    def leftToRightThenRightToLeftProcessing(self, name1: str, name2: str) -> int:
        name1_char = list(name1)
        name2_char = list(name2)

        name1_size = len(name1) - 1
        name2_size = len(name2) - 1

        name1_lt_r_start = self.__EMPTY
        name1_lt_r_end = self.__EMPTY

        name2_rt_l_start = self.__EMPTY
        name2_rt_l_end = self.__EMPTY

        for i in range(len(name1_char)):
            if i > name2_size:
                break

            name1_lt_r_start = name1[i : i + 1]
            name1_lt_r_end = name1[name1_size - i : name1_size - i + 1]

            name2_rt_l_start = name2[i : i + 1]
            name2_rt_l_end = name2[name2_size - i : name2_size - i + 1]

            if name1_lt_r_start == name2_rt_l_start:
                name1_char[i] = " "
                name2_char[i] = " "

            if name1_lt_r_end == name2_rt_l_end:
                name1_char[name1_size - i] = " "
                name2_char[name2_size - i] = " "

        str_a = "".join(name1_char).replace(" ", self.__EMPTY)
        str_b = "".join(name2_char).replace(" ", self.__EMPTY)

        if len(str_a) > len(str_b):
            return abs(6 - len(str_a))
        return abs(6 - len(str_b))

    def isVowel(self, letter: str) -> bool:
        return letter.upper() in {"E", "A", "O", "I", "U"}

    def getMinRating(self, sumLength: int) -> int:
        minRating = 0

        if sumLength <= 4:
            minRating = 5
        elif sumLength <= 7:  # already know it is at least 5
            minRating = 4
        elif sumLength <= 11:  # already know it is at least 8
            minRating = 3
        elif sumLength == 12:
            minRating = 2
        else:
            minRating = 1  # docs said little here.

        return minRating

    def getFirst3Last3(self, name: str) -> str:
        name_length = len(name)

        if name_length > 6:
            first_three = name[:3]
            last_three = name[-3:]
            return first_three + last_three
        return name

    def cleanName(self, name: str) -> str:
        upperName = name.upper()

        charsToTrim = ["\\-", "[&]", "\\'", "\\.", "[\\,]"]
        for str_ in charsToTrim:
            upperName = re.sub(str_, self.__EMPTY, upperName)

        upperName = self.removeAccents(upperName)
        upperName = re.sub("\\s+", self.__EMPTY, upperName)

        return upperName
