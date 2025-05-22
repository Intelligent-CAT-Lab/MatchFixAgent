from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class PhoneticEngine:

    __maxPhonemes: int = 0

    __concat: bool = False

    __ruleType: RuleType = None

    __nameType: NameType = None

    __lang: Lang = None

    __DEFAULT_MAX_PHONEMES: int = 20
    __NAME_PREFIXES: typing.Dict[NameType, typing.Set[str]] = {}

    @staticmethod
    def run_static_init():
        PhoneticEngine.__NAME_PREFIXES[NameType.ASHKENAZI] = frozenset(
            {"bar", "ben", "da", "de", "van", "von"}
        )
        PhoneticEngine.__NAME_PREFIXES[NameType.SEPHARDIC] = frozenset(
            {
                "al",
                "el",
                "da",
                "dal",
                "de",
                "del",
                "dela",
                "de la",
                "della",
                "des",
                "di",
                "do",
                "dos",
                "du",
                "van",
                "von",
            }
        )
        PhoneticEngine.__NAME_PREFIXES[NameType.GENERIC] = frozenset(
            {
                "da",
                "dal",
                "de",
                "del",
                "dela",
                "de la",
                "della",
                "des",
                "di",
                "do",
                "dos",
                "du",
                "van",
                "von",
            }
        )

    def getMaxPhonemes(self) -> int:
        return self.__maxPhonemes

    def isConcat(self) -> bool:
        return self.__concat

    def getRuleType(self) -> RuleType:
        return self.__ruleType

    def getNameType(self) -> NameType:
        return self.__nameType

    def getLang(self) -> Lang:
        return self.__lang

    def encode1(self, input_: str, languageSet: LanguageSet) -> str:
        rules = Rule.getInstanceMap0(self.__nameType, RuleType.RULES, languageSet)
        finalRules1 = Rule.getInstanceMap1(self.__nameType, self.__ruleType, "common")
        finalRules2 = Rule.getInstanceMap0(
            self.__nameType, self.__ruleType, languageSet
        )

        input_ = input_.lower().replace("-", " ").strip()

        if self.__nameType == NameType.GENERIC:
            if len(input_) >= 2 and input_[:2] == "d'":
                remainder = input_[2:]
                combined = "d" + remainder
                return f"({self.encode0(remainder)})-({self.encode0(combined)})"
            for l in self.__NAME_PREFIXES.get(self.__nameType, set()):
                if input_.startswith(l + " "):
                    remainder = input_[len(l) + 1 :]
                    combined = l + remainder
                    return f"({self.encode0(remainder)})-({self.encode0(combined)})"

        words = input_.split()
        words2 = []

        if self.__nameType == NameType.SEPHARDIC:
            for aWord in words:
                parts = aWord.split("'")
                lastPart = parts[-1]
                words2.append(lastPart)
            words2 = [
                w
                for w in words2
                if w not in self.__NAME_PREFIXES.get(self.__nameType, set())
            ]
        elif self.__nameType == NameType.ASHKENAZI:
            words2.extend(words)
            words2 = [
                w
                for w in words2
                if w not in self.__NAME_PREFIXES.get(self.__nameType, set())
            ]
        elif self.__nameType == NameType.GENERIC:
            words2.extend(words)
        else:
            raise ValueError(f"Unreachable case: {self.__nameType}")

        if self.__concat:
            input_ = self.__join(words2, " ")
        elif len(words2) == 1:
            input_ = words2[0]
        else:
            result = []
            for word in words2:
                result.append("-" + self.encode0(word))
            return "".join(result)[1:]

        phonemeBuilder = PhonemeBuilder.empty(languageSet)

        i = 0
        while i < len(input_):
            rulesApplication = RulesApplication(
                rules, input_, phonemeBuilder, i, self.__maxPhonemes
            ).invoke()
            i = rulesApplication.getI()
            phonemeBuilder = rulesApplication.getPhonemeBuilder()

        phonemeBuilder = self.__applyFinalRules(phonemeBuilder, finalRules1)
        phonemeBuilder = self.__applyFinalRules(phonemeBuilder, finalRules2)

        return phonemeBuilder.makeString()

    def encode0(self, input_: str) -> str:
        languageSet = self.__lang.guessLanguages(input_)
        return self.encode1(input_, languageSet)

    def __init__(
        self, nameType: NameType, ruleType: RuleType, concat: bool, maxPhonemes: int
    ) -> None:
        if ruleType == RuleType.RULES:
            raise ValueError(f"ruleType must not be {RuleType.RULES}")
        self.__nameType = nameType
        self.__ruleType = ruleType
        self.__concat = concat
        self.__lang = Lang.instance(nameType)
        self.__maxPhonemes = maxPhonemes

    @staticmethod
    def PhoneticEngine0(
        nameType: NameType, ruleType: RuleType, concat: bool
    ) -> PhoneticEngine:
        return PhoneticEngine(
            nameType,
            ruleType,
            concat,
            PhoneticEngine._PhoneticEngine__DEFAULT_MAX_PHONEMES,
        )

    def __applyFinalRules(
        self,
        phonemeBuilder: PhonemeBuilder,
        finalRules: typing.Dict[str, typing.List[Rule]],
    ) -> PhonemeBuilder:
        if finalRules is None:
            raise ValueError("finalRules cannot be None")
        if not finalRules:
            return phonemeBuilder

        phonemes = {}

        for phoneme in phonemeBuilder.getPhonemes():
            subBuilder = PhonemeBuilder.empty(phoneme.getLanguages())
            phonemeText = phoneme.getPhonemeText()

            i = 0
            while i < len(phonemeText):
                rulesApplication = RulesApplication(
                    finalRules, phonemeText, subBuilder, i, self.__maxPhonemes
                ).invoke()
                found = rulesApplication.isFound()
                subBuilder = rulesApplication.getPhonemeBuilder()

                if not found:
                    subBuilder.append(phonemeText[i : i + 1])

                i = rulesApplication.getI()

            for newPhoneme in subBuilder.getPhonemes():
                if newPhoneme in phonemes:
                    oldPhoneme = phonemes.pop(newPhoneme)
                    mergedPhoneme = oldPhoneme.mergeWithLanguage(
                        newPhoneme.getLanguages()
                    )
                    phonemes[mergedPhoneme] = mergedPhoneme
                else:
                    phonemes[newPhoneme] = newPhoneme

        return PhonemeBuilder(0, set(phonemes.keys()), None)

    @staticmethod
    def __join(strings: typing.Iterable[str], sep: str) -> str:
        iterator = iter(strings)
        try:
            result = next(iterator)
        except StopIteration:
            return ""
        for s in iterator:
            result += sep + s
        return result


class PhonemeBuilder:

    __phonemes: typing.Set[Phoneme] = None

    def makeString(self) -> str:
        sb = []

        for ph in self.__phonemes:
            if len(sb) > 0:
                sb.append("|")
            sb.append(ph.getPhonemeText())

        return "".join(sb)

    def getPhonemes(self) -> typing.Set[Phoneme]:
        return self.__phonemes

    def apply(self, phonemeExpr: PhonemeExpr, maxPhonemes: int) -> None:
        newPhonemes: Set[Phoneme] = set()

        for left in self.__phonemes:
            for right in phonemeExpr.getPhonemes():
                languages = left.getLanguages().restrictTo(right.getLanguages())
                if not languages.isEmpty():
                    join = Phoneme(left, right, languages)
                    if len(newPhonemes) < maxPhonemes:
                        newPhonemes.add(join)
                        if len(newPhonemes) >= maxPhonemes:
                            break

        self.__phonemes.clear()
        self.__phonemes.update(newPhonemes)

    def append(self, str_: str) -> None:
        for ph in self.__phonemes:
            ph.append(str_)

    def __init__(
        self, constructorId: int, phonemes: typing.Set[Phoneme], phoneme: Phoneme
    ) -> None:
        if constructorId == 0:
            self.__phonemes = phonemes
        else:
            self.__phonemes = set()
            self.__phonemes.add(phoneme)

    @staticmethod
    def empty(languages: LanguageSet) -> PhonemeBuilder:
        return PhonemeBuilder(3, None, Rule.Phoneme(2, "", languages, None))


class RulesApplication:

    __found: bool = False

    __maxPhonemes: int = 0

    __i: int = 0

    __phonemeBuilder: PhonemeBuilder = None

    __input: str = ""

    __finalRules: typing.Dict[str, typing.List[Rule]] = None

    def isFound(self) -> bool:
        return self.__found

    def invoke(self) -> RulesApplication:
        self.__found = False
        pattern_length = 1
        rules = self.__finalRules.get(
            self.__input[self.__i : self.__i + pattern_length]
        )

        if rules is not None:
            for rule in rules:
                pattern = rule.getPattern()
                pattern_length = len(pattern)

                if rule.patternAndContextMatches(self.__input, self.__i):
                    self.__phonemeBuilder.apply(rule.getPhoneme(), self.__maxPhonemes)
                    self.__found = True
                    break

        if not self.__found:
            pattern_length = 1

        self.__i += pattern_length
        return self

    def getPhonemeBuilder(self) -> PhonemeBuilder:
        return self.__phonemeBuilder

    def getI(self) -> int:
        return self.__i

    def __init__(
        self,
        finalRules: typing.Dict[str, typing.List[Rule]],
        input_: str,
        phonemeBuilder: PhonemeBuilder,
        i: int,
        maxPhonemes: int,
    ) -> None:
        if finalRules is None:
            raise ValueError("finalRules cannot be None")
        self.__finalRules = finalRules
        self.__phonemeBuilder = phonemeBuilder
        self.__input = input_
        self.__i = i
        self.__maxPhonemes = maxPhonemes


PhoneticEngine.run_static_init()
