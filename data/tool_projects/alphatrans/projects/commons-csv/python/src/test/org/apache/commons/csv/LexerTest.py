from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *
from src.main.org.apache.commons.csv.Lexer import *
from src.main.org.apache.commons.csv.Token import *


class LexerTest(unittest.TestCase):

    __formatWithEscaping: CSVFormat = None

    def testReadEscapeFF_test0_decomposed(self) -> None:
        with self.__createLexer(
            "f", CSVFormat.DEFAULT.withEscape0(Constants.FF)
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(Constants.FF, chr(ch))

    def testReadEscapeBackspace_test0_decomposed(self) -> None:
        with self.__createLexer("b", CSVFormat.DEFAULT.withEscape0("\b")) as lexer:
            ch = lexer.readEscape()
            self.assertEqual(Constants.BACKSPACE, ch)

    def testIsMetaCharCommentStart_test0_decomposed(self) -> None:
        with self.__createLexer(
            "#", CSVFormat.DEFAULT.withCommentMarker0("#")
        ) as lexer:
            ch = lexer.readEscape()
            self.assertEqual("#", chr(ch))

    def testEscapingAtEOF_test0_decomposed(self) -> None:
        code = "escaping at EOF is evil\\"
        with self.__createLexer(code, self.__formatWithEscaping) as lexer:
            with self.assertRaises(io.OSError):
                lexer.nextToken(Token())

    def setUp(self) -> None:
        self.__formatWithEscaping = CSVFormat.DEFAULT.withEscape0("\\")

    def __createLexer(self, input_: str, format_: CSVFormat) -> Lexer:
        return Lexer(format_, ExtendedBufferedReader(io.StringIO(input_)))
