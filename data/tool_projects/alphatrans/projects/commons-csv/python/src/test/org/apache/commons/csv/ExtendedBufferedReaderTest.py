from __future__ import annotations
import re
import numbers
from io import StringIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.csv.Constants import *
from src.main.org.apache.commons.csv.ExtendedBufferedReader import *


class ExtendedBufferedReaderTest(unittest.TestCase):

    def testReadLookahead2_test0_decomposed(self) -> None:
        ref = ["\0"] * 5  # Initialize a list of 5 null characters
        res = ["\0"] * 5  # Initialize a list of 5 null characters
        with self.__createBufferedReader("abcdefg") as br:
            ref[0] = "a"
            ref[1] = "b"
            ref[2] = "c"
            self.assertEqual(
                3, br.read1(res, 0, 3)
            )  # Read 3 characters into res starting at index 0
            self.assertEqual(ref, res)  # Assert that ref and res are equal
            self.assertEqual(
                "c", chr(br.getLastChar())
            )  # Assert the last character read is 'c'

            self.assertEqual(
                "d", chr(br.lookAhead0())
            )  # Assert the next character to be read is 'd'
            ref[4] = "d"
            self.assertEqual(
                1, br.read1(res, 4, 1)
            )  # Read 1 character into res at index 4
            self.assertEqual(ref, res)  # Assert that ref and res are equal
            self.assertEqual(
                "d", chr(br.getLastChar())
            )  # Assert the last character read is 'd'

    def testReadLookahead1_test0_decomposed(self) -> None:
        with self.__createBufferedReader("1\n2\r3\n") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.lookAhead0())
            self.assertEqual(Constants.UNDEFINED, br.getLastChar())
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.read0())  # Start line 1
            self.assertEqual(ord("1"), br.getLastChar())

            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("1"), br.getLastChar())
            self.assertEqual(ord("\n"), br.read0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())

            self.assertEqual(ord("2"), br.lookAhead0())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.read0())  # Start line 2
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.getLastChar())

            self.assertEqual(ord("\r"), br.lookAhead0())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("2"), br.getLastChar())
            self.assertEqual(ord("\r"), br.read0())
            self.assertEqual(ord("\r"), br.getLastChar())
            self.assertEqual(2, br.getCurrentLineNumber())

            self.assertEqual(ord("3"), br.lookAhead0())
            self.assertEqual(ord("\r"), br.getLastChar())
            self.assertEqual(ord("3"), br.read0())  # Start line 3
            self.assertEqual(ord("3"), br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual(ord("3"), br.getLastChar())
            self.assertEqual(ord("\n"), br.read0())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(3, br.getCurrentLineNumber())

            self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
            self.assertEqual(ord("\n"), br.getLastChar())
            self.assertEqual(Constants.END_OF_STREAM, br.read0())
            self.assertEqual(Constants.END_OF_STREAM, br.getLastChar())
            self.assertEqual(Constants.END_OF_STREAM, br.read0())
            self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
            self.assertEqual(3, br.getCurrentLineNumber())

    def testReadLine_test3_decomposed(self) -> None:
        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("foo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("hello", br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(ord("f"), br.read0())
            self.assertEqual(ord("o"), br.lookAhead0())
            self.assertEqual("oo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("h"), br.lookAhead0())
            self.assertEqual("hello", br.readLine())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

        with self.__createBufferedReader("foo\rbaar\r\nfoo") as br:
            self.assertEqual("foo", br.readLine())
            self.assertEqual(ord("b"), br.lookAhead0())
            self.assertEqual("baar", br.readLine())
            self.assertEqual(ord("f"), br.lookAhead0())
            self.assertEqual("foo", br.readLine())
            self.assertIsNone(br.readLine())

    def testReadLine_test2_decomposed(self) -> None:
        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("foo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("hello", br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(ord("f"), br.read0())
            self.assertEqual(ord("o"), br.lookAhead0())
            self.assertEqual("oo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual(ord("\n"), br.lookAhead0())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual(ord("h"), br.lookAhead0())
            self.assertEqual("hello", br.readLine())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

    def testReadLine_test1_decomposed(self) -> None:
        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("foo\n\nhello") as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            self.assertEqual("foo", br.readLine())
            self.assertEqual(1, br.getCurrentLineNumber())
            self.assertEqual("", br.readLine())
            self.assertEqual(2, br.getCurrentLineNumber())
            self.assertEqual("hello", br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())
            self.assertIsNone(br.readLine())
            self.assertEqual(3, br.getCurrentLineNumber())

    def testReadLine_test0_decomposed(self) -> None:
        with self.__createBufferedReader("") as br:
            self.assertIsNone(br.readLine())

        with self.__createBufferedReader("\n") as br:
            self.assertEqual("", br.readLine())
            self.assertIsNone(br.readLine())

    def testReadingInDifferentBuffer_test0_decomposed(self) -> None:
        tmp1 = [""] * 2  # Create a buffer of size 2
        tmp2 = [""] * 4  # Create a buffer of size 4
        with self.__createBufferedReader("1\r\n2\r\n") as reader:
            reader.read1(tmp1, 0, 2)  # Read 2 characters into tmp1 starting at index 0
            reader.read1(tmp2, 2, 2)  # Read 2 characters into tmp2 starting at index 2
            self.assertEqual(
                2, reader.getCurrentLineNumber()
            )  # Assert the current line number is 2

    def testReadChar_test2_decomposed(self) -> None:
        LF = "\n"
        CR = "\r"
        CRLF = CR + LF
        LFCR = LF + CR
        test = (
            "a"
            + LF
            + "b"
            + CR
            + "c"
            + LF
            + LF
            + "d"
            + CR
            + CR
            + "e"
            + LFCR
            + "f "
            + CRLF
        )
        EOLeolct = 9

        # First test case
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.readLine() is not None:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

        # Second test case
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.read0() != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

        # Third test case
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            buff = [""] * 10  # Create a buffer of size 10
            while br.read1(buff, 0, 3) != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

    def testReadChar_test1_decomposed(self) -> None:
        LF = "\n"
        CR = "\r"
        CRLF = CR + LF
        LFCR = LF + CR
        test = (
            "a"
            + LF
            + "b"
            + CR
            + "c"
            + LF
            + LF
            + "d"
            + CR
            + CR
            + "e"
            + LFCR
            + "f "
            + CRLF
        )
        EOLeolct = 9

        # First test block
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.readLine() is not None:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

        # Second test block
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.read0() != -1:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

    def testReadChar_test0_decomposed(self) -> None:
        LF = "\n"
        CR = "\r"
        CRLF = CR + LF
        LFCR = LF + CR
        test = (
            "a"
            + LF
            + "b"
            + CR
            + "c"
            + LF
            + LF
            + "d"
            + CR
            + CR
            + "e"
            + LFCR
            + "f "
            + CRLF
        )
        EOLeolct = 9
        with self.__createBufferedReader(test) as br:
            self.assertEqual(0, br.getCurrentLineNumber())
            while br.readLine() is not None:
                pass
            self.assertEqual(EOLeolct, br.getCurrentLineNumber())

    def testEmptyInput_test0_decomposed(self) -> None:
        with self.__createBufferedReader("") as br:
            self.assertEqual(Constants.END_OF_STREAM, br.read0())
            self.assertEqual(Constants.END_OF_STREAM, br.lookAhead0())
            self.assertEqual(Constants.END_OF_STREAM, br.getLastChar())
            self.assertIsNone(br.readLine())
            self.assertEqual(0, br.read1([""] * 10, 0, 0))

    def __createBufferedReader(self, s: str) -> ExtendedBufferedReader:
        return ExtendedBufferedReader(io.StringIO(s))
