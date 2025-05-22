from __future__ import annotations
import time
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.Resources import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.Rule1 import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class DaitchMokotoffSoundex(StringEncoder):

    __folding: bool = False

    __FOLDINGS: typing.Dict[str, str] = {}

    __RULES: typing.Dict[str, typing.List[Rule]] = {}

    __MAX_LENGTH: int = 6
    __RESOURCE_FILE: str = "org/apache/commons/codec/language/dmrules.txt"
    __MULTILINE_COMMENT_START: str = "/*"
    __MULTILINE_COMMENT_END: str = "*/"
    __DOUBLE_QUOTE: str = '"'
    __COMMENT: str = "//"

    def run_static_init():
        pass  # LLM could not translate this static initializer

    def soundex0(self, source: str) -> str:
        branches = self.__soundex1(source, True)
        sb = []
        index = 0
        for branch in branches:
            sb.append(branch)
            if index + 1 < len(branches):
                sb.append("|")
            index += 1
        return "".join(sb)

    def encode1(self, source: str) -> Optional[str]:
        if source is None:
            return None
        return self.__soundex1(source, False)[0]

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to DaitchMokotoffSoundex encode is not of type java.lang.String",
                None,
            )
        return self.encode1(obj)

    @staticmethod
    def DaitchMokotoffSoundex1() -> DaitchMokotoffSoundex:
        return DaitchMokotoffSoundex(True)

    def __init__(self, folding: bool) -> None:
        self.__folding = folding

    def __soundex1(
        self, source: str, branching: bool
    ) -> typing.Optional[typing.List[str]]:
        if source is None:
            return None

        input_ = self.__cleanup(source)

        current_branches: typing.Set[Branch] = set()
        current_branches.add(Branch())

        last_char = "\0"
        index = 0
        while index < len(input_):
            ch = input_[index]

            if ch.isspace():
                index += 1
                continue

            input_context = input_[index:]
            rules = self.__RULES.get(ch)
            if rules is None:
                index += 1
                continue

            next_branches = [] if branching else []

            for rule in rules:
                if rule.matches(input_context):
                    if branching:
                        next_branches.clear()

                    replacements = rule.getReplacements(
                        input_context, last_char == "\0"
                    )
                    branching_required = len(replacements) > 1 and branching

                    for branch in current_branches:
                        for next_replacement in replacements:
                            next_branch = (
                                branch.createBranch() if branching_required else branch
                            )

                            force = (last_char == "m" and ch == "n") or (
                                last_char == "n" and ch == "m"
                            )

                            next_branch.processNextReplacement(next_replacement, force)

                            if not branching:
                                break
                            next_branches.append(next_branch)

                    if branching:
                        current_branches.clear()
                        current_branches.update(next_branches)

                    index += rule.getPatternLength() - 1
                    break

            last_char = ch
            index += 1

        result = []
        for branch in current_branches:
            branch.finish()
            result.append(branch.toString())

        return result

    def __cleanup(self, input_: str) -> str:
        sb = []
        for ch in input_:
            if ch.isspace():
                continue

            ch = ch.lower()
            if self.__folding and ch in self.__FOLDINGS:
                ch = self.__FOLDINGS[ch]
            sb.append(ch)
        return "".join(sb)

    @staticmethod
    def __stripQuotes(str_: str) -> str:
        if str_.startswith(DaitchMokotoffSoundex.__DOUBLE_QUOTE):
            str_ = str_[1:]

        if str_.endswith(DaitchMokotoffSoundex.__DOUBLE_QUOTE):
            str_ = str_[:-1]

        return str_

    @staticmethod
    def __parseRules(
        scanner: typing.Any,
        location: str,
        ruleMapping: typing.Dict[str, typing.List[Rule]],
        asciiFoldings: typing.Dict[str, str],
    ) -> None:
        currentLine = 0
        inMultilineComment = False

        while scanner.has_next_line():
            currentLine += 1
            rawLine = scanner.next_line()
            line = rawLine

            if inMultilineComment:
                if line.endswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_END):
                    inMultilineComment = False
                continue

            if line.startswith(DaitchMokotoffSoundex.__MULTILINE_COMMENT_START):
                inMultilineComment = True
            else:
                cmtI = line.find(DaitchMokotoffSoundex.__COMMENT)
                if cmtI >= 0:
                    line = line[:cmtI]

                line = line.strip()

                if not line:
                    continue  # empty lines can be safely skipped

                if "=" in line:
                    parts = line.split("=")
                    if len(parts) != 2:
                        raise ValueError(
                            f"Malformed folding statement split into {len(parts)} parts: {rawLine} in {location}"
                        )
                    leftCharacter = parts[0]
                    rightCharacter = parts[1]

                    if len(leftCharacter) != 1 or len(rightCharacter) != 1:
                        raise ValueError(
                            f"Malformed folding statement - patterns are not single characters: {rawLine} in {location}"
                        )

                    asciiFoldings[leftCharacter[0]] = rightCharacter[0]
                else:
                    parts = line.split()
                    if len(parts) != 4:
                        raise ValueError(
                            f"Malformed rule statement split into {len(parts)} parts: {rawLine} in {location}"
                        )
                    try:
                        pattern = DaitchMokotoffSoundex.__stripQuotes(parts[0])
                        replacement1 = DaitchMokotoffSoundex.__stripQuotes(parts[1])
                        replacement2 = DaitchMokotoffSoundex.__stripQuotes(parts[2])
                        replacement3 = DaitchMokotoffSoundex.__stripQuotes(parts[3])

                        r = Rule(pattern, replacement1, replacement2, replacement3)
                        patternKey = r._Rule__pattern[0]
                        rules = ruleMapping.get(patternKey)
                        if rules is None:
                            rules = []
                            ruleMapping[patternKey] = rules
                        rules.append(r)
                    except ValueError as e:
                        raise RuntimeError(
                            f"Problem parsing line '{currentLine}' in {location}"
                        ) from e


class Rule:

    __replacementDefault: typing.List[typing.List[str]] = None

    __replacementBeforeVowel: typing.List[typing.List[str]] = None

    __replacementAtStart: typing.List[typing.List[str]] = None

    __pattern: str = ""

    def toString(self) -> str:
        return f"{self.__pattern}=({self.__replacementAtStart},{self.__replacementBeforeVowel},{self.__replacementDefault})"

    def matches(self, context: str) -> bool:
        return context.startswith(self.__pattern)

    def getReplacements(
        self, context: str, atStart: bool
    ) -> typing.List[typing.List[str]]:
        if atStart:
            return self.__replacementAtStart

        next_index = self.getPatternLength()
        next_char_is_vowel = next_index < len(context) and self.__isVowel(
            context[next_index]
        )
        if next_char_is_vowel:
            return self.__replacementBeforeVowel

        return self.__replacementDefault

    def getPatternLength(self) -> int:
        return len(self.__pattern)

    def __init__(
        self,
        pattern: str,
        replacementAtStart: str,
        replacementBeforeVowel: str,
        replacementDefault: str,
    ) -> None:
        self.__pattern = pattern
        self.__replacementAtStart = replacementAtStart.split("|")
        self.__replacementBeforeVowel = replacementBeforeVowel.split("|")
        self.__replacementDefault = replacementDefault.split("|")

    def __isVowel(self, ch: str) -> bool:
        return ch in {"a", "e", "i", "o", "u"}


class Branch:

    __lastReplacement: str = ""

    __cachedString: str = ""

    __builder: typing.Union[typing.List[str], io.StringIO] = None

    def toString(self) -> str:
        if self.__cachedString == "":
            self.__cachedString = (
                self.__builder.getvalue()
                if isinstance(self.__builder, io.StringIO)
                else "".join(self.__builder)
            )
        return self.__cachedString

    def hashCode(self) -> int:
        return hash(self.toString())

    def equals(self, other: typing.Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, Branch):
            return False
        return self.toString() == other.toString()

    def processNextReplacement(self, replacement: str, forceAppend: bool) -> None:
        append = (
            self.__lastReplacement is None
            or not self.__lastReplacement.endswith(replacement)
            or forceAppend
        )

        if append and len(self.__builder.getvalue()) < self.__MAX_LENGTH:
            self.__builder.write(replacement)
            if len(self.__builder.getvalue()) > self.__MAX_LENGTH:
                self.__builder = io.StringIO(
                    self.__builder.getvalue()[: self.__MAX_LENGTH]
                )
            self.__cachedString = None

        self.__lastReplacement = replacement

    def finish(self) -> None:
        while len(self.__builder.getvalue()) < DaitchMokotoffSoundex.__MAX_LENGTH:
            self.__builder.write("0")
            self.__cachedString = None

    def createBranch(self) -> Branch:
        branch = Branch()
        branch.__builder.write(self.toString())
        branch.__lastReplacement = self.__lastReplacement
        return branch

    def __init__(self) -> None:
        self.__builder = io.StringIO()
        self.__lastReplacement = None
        self.__cachedString = None


DaitchMokotoffSoundex.run_static_init()
