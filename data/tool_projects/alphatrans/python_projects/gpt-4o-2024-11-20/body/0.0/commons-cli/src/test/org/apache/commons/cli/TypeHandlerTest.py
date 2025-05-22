from __future__ import annotations
import re
import pathlib
import unittest
import pytest
import io
import numbers
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.cli.PatternOptionBuilder import *
from src.main.org.apache.commons.cli.TypeHandler import *


class TypeHandlerTest(unittest.TestCase):

    def testCreateValueURL_malformed_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0("malformed-url", PatternOptionBuilder.URL_VALUE)

    def testCreateValueURL_test1_decomposed(self) -> None:
        url_string = "https://commons.apache.org"
        result = TypeHandler.createValue0(url_string, PatternOptionBuilder.URL_VALUE)
        self.assertEqual(url_string, result.geturl())

    def testCreateValueURL_test0_decomposed(self) -> None:
        url_string = "https://commons.apache.org"
        result = TypeHandler.createValue0(url_string, PatternOptionBuilder.URL_VALUE)

    def testCreateValueString_test0_decomposed(self) -> None:
        self.assertEqual(
            "String",
            TypeHandler.createValue0("String", PatternOptionBuilder.STRING_VALUE),
            "Expected the returned value to match the input string 'String'",
        )

    def testCreateValueObject_unknownClass_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0("unknown", PatternOptionBuilder.OBJECT_VALUE)

    def testCreateValueObject_notInstantiableClass_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0(
                NotInstantiable.__name__, PatternOptionBuilder.OBJECT_VALUE
            )

    def testCreateValueObject_InstantiableClass_test1_decomposed(self) -> None:
        result = TypeHandler.createValue0(
            Instantiable.__name__, PatternOptionBuilder.OBJECT_VALUE
        )
        self.assertTrue(isinstance(result, Instantiable))

    def testCreateValueObject_InstantiableClass_test0_decomposed(self) -> None:
        result = TypeHandler.createValue0(
            "Instantiable", PatternOptionBuilder.OBJECT_VALUE
        )

    def testCreateValueNumber_noNumber_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0("not a number", PatternOptionBuilder.NUMBER_VALUE)

    def testCreateValueNumber_Long_test0_decomposed(self) -> None:
        self.assertEqual(
            15,  # Python's `int` is used instead of Java's `Long.valueOf`
            TypeHandler.createValue0("15", PatternOptionBuilder.NUMBER_VALUE),
        )

    def testCreateValueNumber_Double_test0_decomposed(self) -> None:
        self.assertEqual(
            1.5, TypeHandler.createValue0("1.5", PatternOptionBuilder.NUMBER_VALUE)
        )

    def testCreateValueInteger_failure_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0("just-a-string", int)

    def testCreateValueFiles_test0_decomposed(self) -> None:
        with self.assertRaises(NotImplementedError):
            TypeHandler.createValue0("some.files", PatternOptionBuilder.FILES_VALUE)

    def testCreateValueFile_test1_decomposed(self) -> None:
        result = TypeHandler.createValue0(
            "some-file.txt", PatternOptionBuilder.FILE_VALUE
        )
        self.assertEqual("some-file.txt", result.name)

    def testCreateValueFile_test0_decomposed(self) -> None:
        result = TypeHandler.createValue0(
            "some-file.txt", PatternOptionBuilder.FILE_VALUE
        )
        self.assertIsInstance(result, pathlib.Path)
        self.assertEqual(result.name, "some-file.txt")

    def testCreateValueExistingFile_nonExistingFile_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0(
                "non-existing.file", PatternOptionBuilder.EXISTING_FILE_VALUE
            )

    def testCreateValueExistingFile_test0_decomposed(self) -> None:
        file_path = "src/test/resources/org/apache/commons/cli/existing-readable.file"
        try:
            with TypeHandler.createValue0(
                file_path, PatternOptionBuilder.EXISTING_FILE_VALUE
            ) as result:
                self.assertIsNotNone(result)
        except Exception as e:
            self.fail(f"Exception occurred: {e}")

    def testCreateValueDate_test0_decomposed(self) -> None:
        with self.assertRaises(NotImplementedError):
            TypeHandler.createValue0("what ever", PatternOptionBuilder.DATE_VALUE)

    def testCreateValueClass_notFound_test0_decomposed(self) -> None:
        with self.assertRaises(ParseException):
            TypeHandler.createValue0("what ever", PatternOptionBuilder.CLASS_VALUE)

    def testCreateValueClass_test1_decomposed(self) -> None:
        clazz = TypeHandler.createValue0(
            Instantiable.__name__, PatternOptionBuilder.CLASS_VALUE
        )
        self.assertEqual(Instantiable, clazz)

    def testCreateValueClass_test0_decomposed(self) -> None:
        clazz = TypeHandler.createValue0(
            Instantiable.__name__, PatternOptionBuilder.CLASS_VALUE
        )


class Instantiable:

    pass


class NotInstantiable:

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")
