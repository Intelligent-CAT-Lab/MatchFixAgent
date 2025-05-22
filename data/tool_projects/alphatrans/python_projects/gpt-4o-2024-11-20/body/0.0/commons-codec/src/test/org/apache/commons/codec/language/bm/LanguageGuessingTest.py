from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *


class LanguageGuessingTest(unittest.TestCase):

    __name: str = ""

    __language: str = ""

    __lang: Lang = Lang.instance(NameType.GENERIC)

    def testLanguageGuessing_test1_decomposed(self) -> None:
        guesses = self.__lang.guessLanguages(self.__name)
        self.assertTrue(
            f"language predicted for name '{self.__name}' is wrong: {guesses} should contain '{self.__language}'",
            guesses.contains(self.__language),
        )

    def testLanguageGuessing_test0_decomposed(self) -> None:
        guesses: LanguageSet = self.__lang.guessLanguages(self.__name)

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:
        return [
            ["Renault", "french"],
            ["Mickiewicz", "polish"],
            ["Thompson", "english"],  # this also hits german and greeklatin
            ["Nuñez", "spanish"],  # Nuñez
            ["Carvalho", "portuguese"],
            ["Čapek", "czech"],  # Čapek
            ["Sjneijder", "dutch"],
            ["Klausewitz", "german"],
            ["Küçük", "turkish"],  # Küçük
            ["Giacometti", "italian"],
            ["Nagy", "hungarian"],
            ["Ceaușescu", "romanian"],  # Ceaușescu
            ["Angelopoulos", "greeklatin"],
            ["Αγγελόπουλος", "greek"],  # Αγγελόπουλος
            ["Пушкин", "cyrillic"],  # Пушкин
            ["כהן", "hebrew"],  # כהן
            ["ácz", "any"],  # ácz
            ["átz", "any"],  # átz
        ]
