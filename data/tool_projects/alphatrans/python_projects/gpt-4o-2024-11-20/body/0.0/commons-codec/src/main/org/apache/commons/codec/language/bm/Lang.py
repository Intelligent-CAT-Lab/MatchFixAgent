from __future__ import annotations
import time
import copy
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *


class Lang:

    __rules: typing.List[LangRule] = None

    __languages: Languages = None

    __LANGUAGE_RULES_RN: str = "org/apache/commons/codec/language/bm/%s_lang.txt"
    __Langs: typing.Dict[NameType, Lang] = {}

    def run_static_init():
        pass  # LLM could not translate this static initializer

    def guessLanguages(self, input_: str) -> LanguageSet:
        text = input_.lower()  # Convert input to lowercase

        langs = set(self.__languages.getLanguages())  # Get the set of languages
        for rule in self.__rules:
            if rule.matches(text):  # Check if the rule matches the text
                if (
                    rule._LangRule__acceptOnMatch
                ):  # If the rule is an accept-on-match rule
                    langs.intersection_update(
                        rule._LangRule__languages
                    )  # Retain only matching languages
                else:  # If the rule is a reject-on-match rule
                    langs.difference_update(
                        rule._LangRule__languages
                    )  # Remove matching languages

        ls = LanguageSet.from_(
            langs
        )  # Create a LanguageSet from the resulting languages
        return Languages.ANY_LANGUAGE if ls == Languages.NO_LANGUAGES else ls

    def guessLanguage(self, text: str) -> str:
        ls = self.guessLanguages(text)
        return ls.getAny() if ls.isSingleton() else Languages.ANY

    @staticmethod
    def loadFromResource(languageRulesResourceName: str, languages: Languages) -> Lang:
        rules: List[LangRule] = []
        try:
            with Resources.getInputStream(languageRulesResourceName) as input_stream:
                scanner = io.TextIOWrapper(
                    input_stream, encoding=ResourceConstants.ENCODING
                )
                in_extended_comment = False
                for raw_line in scanner:
                    line = raw_line.strip()
                    if in_extended_comment:
                        if line.endswith(ResourceConstants.EXT_CMT_END):
                            in_extended_comment = False
                        continue
                    elif line.startswith(ResourceConstants.EXT_CMT_START):
                        in_extended_comment = True
                        continue
                    else:
                        cmt_index = line.find(ResourceConstants.CMT)
                        if cmt_index >= 0:
                            line = line[:cmt_index].strip()

                        if not line:
                            continue  # Skip empty lines

                        parts = line.split()
                        if len(parts) != 3:
                            raise ValueError(
                                f"Malformed line '{raw_line.strip()}' in language resource '{languageRulesResourceName}'"
                            )

                        pattern = re.compile(parts[0])
                        langs = set(parts[1].split("+"))
                        accept = parts[2].lower() == "true"

                        rules.append(LangRule(pattern, langs, accept))
        except Exception as e:
            raise RuntimeError(
                f"Error loading resource '{languageRulesResourceName}': {e}"
            )

        return Lang(rules, languages)

    @staticmethod
    def instance(nameType: NameType) -> Lang:
        return Lang.__Langs.get(nameType)

    def __init__(self, rules: typing.List[LangRule], languages: Languages) -> None:
        self.__rules = list(rules)  # Create an immutable copy of the list
        self.__languages = languages


class LangRule:

    __pattern: re.Pattern = None

    __languages: typing.Set[str] = None

    __acceptOnMatch: bool = False

    def matches(self, txt: str) -> bool:
        return self.__pattern.search(txt) is not None

    def __init__(
        self, pattern: re.Pattern, languages: typing.Set[str], acceptOnMatch: bool
    ) -> None:
        self.__pattern = pattern
        self.__languages = languages
        self.__acceptOnMatch = acceptOnMatch


Lang.run_static_init()
