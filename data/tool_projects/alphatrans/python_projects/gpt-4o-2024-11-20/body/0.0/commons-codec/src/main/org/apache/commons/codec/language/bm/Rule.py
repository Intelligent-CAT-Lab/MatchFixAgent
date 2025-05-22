from __future__ import annotations
import time
import re
import enum
from abc import ABC
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class Rule:

    ALL: str = "ALL"

    ALL_STRINGS_RMATCHER: RPattern = None  # LLM could not translate this field

    __rContext: RPattern = None

    __phoneme: PhonemeExpr = None

    __pattern: str = ""

    __lContext: RPattern = None

    __RULES: typing.Dict[
        NameType,
        typing.Dict[RuleType, typing.Dict[str, typing.Dict[str, typing.List[Rule]]]],
    ] = {}

    __HASH_INCLUDE: str = "#include"
    __DOUBLE_QUOTE: str = '"'

    def run_static_init():
        pass  # LLM could not translate this static initializer

    def patternAndContextMatches(self, input_: str, i: int) -> bool:
        if i < 0:
            raise IndexError("Cannot match pattern at negative indexes")

        pattern_length = len(self.__pattern)
        ipl = i + pattern_length

        if ipl > len(input_):
            return False

        if input_[i:ipl] != self.__pattern:
            return False

        if not self.__rContext.isMatch(input_[ipl:]):
            return False

        return self.__lContext.isMatch(input_[:i])

    def getRContext(self) -> RPattern:
        return self.__rContext

    def getPhoneme(self) -> PhonemeExpr:
        return self.__phoneme

    def getPattern(self) -> str:
        return self.__pattern

    def getLContext(self) -> RPattern:
        return self.__lContext

    def __init__(
        self, pattern: str, lContext: str, rContext: str, phoneme: PhonemeExpr
    ) -> None:
        self.__pattern = pattern
        self.__lContext = self.__pattern(lContext + "$")
        self.__rContext = self.__pattern("^" + rContext)
        self.__phoneme = phoneme

    @staticmethod
    def getInstanceMap1(
        nameType: NameType, rt: RuleType, lang: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        rules = Rule.__RULES.get(nameType, {}).get(rt, {}).get(lang)

        if rules is None:
            raise ValueError(
                f"No rules found for {nameType.getName()}, {rt.getName()}, {lang}."
            )

        return rules

    @staticmethod
    def getInstanceMap0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.Dict[str, typing.List[Rule]]:
        return Rule.getInstanceMap1(
            nameType, rt, langs.getAny() if langs.isSingleton() else Languages.ANY
        )

    @staticmethod
    def getInstance1(nameType: NameType, rt: RuleType, lang: str) -> typing.List[Rule]:
        return Rule.getInstance0(nameType, rt, LanguageSet.from_({lang}))

    @staticmethod
    def getInstance0(
        nameType: NameType, rt: RuleType, langs: LanguageSet
    ) -> typing.List[Rule]:
        rule_map = Rule.getInstanceMap0(nameType, rt, langs)
        all_rules = []
        for rules in rule_map.values():
            all_rules.extend(rules)
        return all_rules

    @staticmethod
    def __stripQuotes(str_: str) -> str:
        if str_.startswith(Rule.__DOUBLE_QUOTE):
            str_ = str_[1:]

        if str_.endswith(Rule.__DOUBLE_QUOTE):
            str_ = str_[:-1]

        return str_

    @staticmethod
    def __startsWith(input_: str, prefix: str) -> bool:
        if len(prefix) > len(input_):
            return False
        for i in range(len(prefix)):
            if input_[i] != prefix[i]:
                return False
        return True

    @staticmethod
    def __pattern(regex: str) -> RPattern:
        starts_with = regex.startswith("^")
        ends_with = regex.endswith("$")
        content = regex[1 if starts_with else 0 : -1 if ends_with else len(regex)]
        boxes = "[" in content

        if not boxes:
            if starts_with and ends_with:
                if not content:
                    return RPattern(lambda input: len(input) == 0)
                return RPattern(lambda input: input == content)
            if (starts_with or ends_with) and not content:
                return Rule.ALL_STRINGS_RMATCHER
            if starts_with:
                return RPattern(lambda input: input.startswith(content))
            if ends_with:
                return RPattern(lambda input: input.endswith(content))
        else:
            starts_with_box = content.startswith("[")
            ends_with_box = content.endswith("]")

            if starts_with_box and ends_with_box:
                box_content = content[1:-1]
                if "[" not in box_content:
                    negate = box_content.startswith("^")
                    if negate:
                        box_content = box_content[1:]
                    b_content = box_content
                    should_match = not negate

                    if starts_with and ends_with:
                        return RPattern(
                            lambda input: len(input) == 1
                            and (input[0] in b_content) == should_match
                        )
                    if starts_with:
                        return RPattern(
                            lambda input: len(input) > 0
                            and (input[0] in b_content) == should_match
                        )
                    if ends_with:
                        return RPattern(
                            lambda input: len(input) > 0
                            and (input[-1] in b_content) == should_match
                        )

        return RPattern(lambda input: bool(re.search(regex, input)))

    @staticmethod
    def __parseRules(
        scanner: typing.Any, location: str
    ) -> typing.Dict[str, typing.List[Rule]]:
        lines: Dict[str, List[Rule]] = {}
        current_line = 0
        in_multiline_comment = False

        while scanner.hasNextLine():
            current_line += 1
            raw_line = scanner.nextLine()
            line = raw_line

            if in_multiline_comment:
                if line.endswith(ResourceConstants.EXT_CMT_END):
                    in_multiline_comment = False
            elif line.startswith(ResourceConstants.EXT_CMT_START):
                in_multiline_comment = True
            else:
                cmt_index = line.find(ResourceConstants.CMT)
                if cmt_index >= 0:
                    line = line[:cmt_index]

                line = line.strip()

                if not line:
                    continue  # Skip empty lines

                if line.startswith(Rule.__HASH_INCLUDE):
                    incl = line[Rule.__HASH_INCLUDE_LENGTH :].strip()
                    if " " in incl:
                        raise ValueError(
                            f"Malformed import statement '{raw_line}' in {location}"
                        )
                    with Rule.__createScanner1(incl) as hash_include_scanner:
                        lines.update(
                            Rule.__parseRules(
                                hash_include_scanner, f"{location}->{incl}"
                            )
                        )
                else:
                    parts = line.split()
                    if len(parts) != 4:
                        raise ValueError(
                            f"Malformed rule statement split into {len(parts)} parts: {raw_line} in {location}"
                        )
                    try:
                        pat = Rule.__stripQuotes(parts[0])
                        l_con = Rule.__stripQuotes(parts[1])
                        r_con = Rule.__stripQuotes(parts[2])
                        ph = Rule.__parsePhonemeExpr(Rule.__stripQuotes(parts[3]))
                        rule = Rule1(pat, l_con, r_con, ph, current_line, location)
                        pattern_key = rule.pattern[0]
                        if pattern_key not in lines:
                            lines[pattern_key] = []
                        lines[pattern_key].append(rule)
                    except ValueError as e:
                        raise RuntimeError(
                            f"Problem parsing line '{current_line}' in {location}"
                        ) from e

        return lines

    @staticmethod
    def __parsePhonemeExpr(ph: str) -> PhonemeExpr:
        if ph.startswith("("):  # we have a bracketed list of options
            if not ph.endswith(")"):
                raise ValueError("Phoneme starts with '(' so must end with ')'")

            phs: List[Phoneme] = []
            body = ph[1:-1]  # Remove the surrounding parentheses
            for part in body.split("|"):
                phs.append(Rule.__parsePhoneme(part))

            if body.startswith("|") or body.endswith("|"):
                phs.append(Phoneme(2, "", Languages.ANY_LANGUAGE, None))

            return PhonemeList(phs)

        return Rule.__parsePhoneme(ph)

    @staticmethod
    def __parsePhoneme(ph: str) -> Phoneme:
        open_index = ph.find("[")
        if open_index >= 0:
            if not ph.endswith("]"):
                raise ValueError(
                    "Phoneme expression contains a '[' but does not end in ']'"
                )

            before = ph[:open_index]
            in_brackets = ph[open_index + 1 : -1]
            langs = set(in_brackets.split("+"))

            return Phoneme(2, before, Languages.LanguageSet.from_(langs), None)

        return Phoneme(2, ph, Languages.ANY_LANGUAGE, None)

    @staticmethod
    def __endsWith(input_: str, suffix: str) -> bool:
        suffix_length = len(suffix)
        input_length = len(input_)

        if suffix_length > input_length:
            return False

        for i, j in zip(
            range(input_length - 1, input_length - suffix_length - 1, -1),
            range(suffix_length - 1, -1, -1),
        ):
            if input_[i] != suffix[j]:
                return False

        return True

    @staticmethod
    def __createScanner1(lang: str) -> typing.Any:
        res_name = f"org/apache/commons/codec/language/bm/{lang}.txt"
        return Resources.getInputStream(res_name), ResourceConstants.ENCODING

    @staticmethod
    def __createScanner0(nameType: NameType, rt: RuleType, lang: str) -> typing.Any:
        resName = Rule.__createResourceName(nameType, rt, lang)
        return io.TextIOWrapper(
            Resources.getInputStream(resName), encoding=ResourceConstants.ENCODING
        )

    @staticmethod
    def __createResourceName(nameType: NameType, rt: RuleType, lang: str) -> str:
        return f"org/apache/commons/codec/language/bm/{nameType.getName()}_{rt.getName()}_{lang}.txt"

    @staticmethod
    def __contains(chars: str, input_: str) -> bool:
        for char in chars:
            if char == input_:
                return True
        return False


class PhonemeExpr(ABC):

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        return []


class PhonemeList(PhonemeExpr):

    __phonemes: typing.List[Phoneme] = None

    def getPhonemes(self) -> typing.List[Phoneme]:
        return self.__phonemes

    def __init__(self, phonemes: typing.List[Phoneme]) -> None:
        self.__phonemes = phonemes


class Phoneme(PhonemeExpr):

    __languages: LanguageSet = None

    __phonemeText: typing.Union[typing.List[str], io.StringIO] = None

    COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = None

    @staticmethod
    def initialize_fields() -> None:
        Phoneme.COMPARATOR: typing.Callable[[Phoneme, Phoneme], int] = lambda o1, o2: (
            (
                lambda o1Length, o2Length: (
                    next(
                        (
                            c
                            for i, c in enumerate(
                                (
                                    o1.__phonemeText[i] - o2.__phonemeText[i]
                                    for i in range(min(o1Length, o2Length))
                                )
                            )
                            if c != 0
                        ),
                        +1 if o1Length > o2Length else -1 if o1Length < o2Length else 0,
                    )
                )
            )(len(o1.__phonemeText), len(o2.__phonemeText))
        )

    def toString(self) -> str:
        return f"{self.__phonemeText}{[self.__languages]}"

    def join(self, right: Phoneme) -> Phoneme:
        return Phoneme(
            2,
            self.__phonemeText.getvalue() + right.__phonemeText.getvalue(),
            self.__languages.restrictTo(right.__languages),
            None,
        )

    def getPhonemes(self) -> typing.Iterable[Phoneme]:
        return {self}

    def mergeWithLanguage(self, lang: LanguageSet) -> Phoneme:
        return Phoneme(
            2, self.__phonemeText.getvalue(), self.__languages.merge(lang), None
        )

    def getPhonemeText(self) -> str:
        return (
            "".join(self.__phonemeText)
            if isinstance(self.__phonemeText, list)
            else self.__phonemeText.getvalue()
        )

    def getLanguages(self) -> LanguageSet:
        return self._Phoneme__languages

    def append(self, str_: str) -> Phoneme:
        if isinstance(self.__phonemeText, StringIO):
            self.__phonemeText.write(str_)
        elif isinstance(self.__phonemeText, list):
            self.__phonemeText.append(str_)
        return self

    return Phoneme(1, phonemeLeft.__phonemeText.getvalue(), languages, phonemeRight)

    @staticmethod
    def Phoneme0(phonemeLeft: Phoneme, phonemeRight: Phoneme) -> Phoneme:
        return Phoneme(
            0,
            phonemeLeft.__phonemeText.getvalue(),
            phonemeLeft.__languages,
            phonemeRight,
        )

    def __init__(
        self,
        constructorId: int,
        phonemeText: str,
        languages: LanguageSet,
        phonemeRight: Phoneme,
    ) -> None:
        if constructorId == 0 or constructorId == 1:
            self.__languages = languages
            self.__phonemeText = StringIO(phonemeText)
            self.__phonemeText.write(phonemeRight.__phonemeText.getvalue())
        else:
            self.__phonemeText = StringIO(phonemeText)
            self.__languages = languages


class RPattern(ABC):

    def isMatch(self, input_: str) -> bool:
        # Implement the logic here
        pass


Rule.run_static_init()

Phoneme.initialize_fields()
