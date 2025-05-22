from __future__ import annotations
import time
import re
import numbers
import unittest
import pytest
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVParser import *
from src.main.org.apache.commons.csv.CSVRecord import *


class JiraCsv248Test(unittest.TestCase):

    def testJiraCsv248_test0_decomposed(self) -> None:
        try:
            with self.__getTestInput() as in_stream, ObjectInputStream(
                in_stream
            ) as ois:
                obj = ois.readObject()
                self.assertTrue(isinstance(obj, CSVRecord))

                rec: CSVRecord = obj
                self.assertEqual(1, rec.getRecordNumber())
                self.assertEqual("One", rec.get1(0))
                self.assertEqual("Two", rec.get1(1))
                self.assertEqual(2, rec.size())
                self.assertEqual(4, rec.getCharacterPosition())
                self.assertEqual("my comment", rec.getComment())
                self.assertIsNone(rec.getParser())
                self.assertTrue(rec.isConsistent())
                self.assertFalse(rec.isMapped("A"))
                self.assertFalse(rec.isSet1("A"))
                self.assertEqual(0, len(rec.toMap()))

                with pytest.raises(RuntimeError):
                    rec.get2("A")
        except Exception as e:
            pytest.fail(f"Test failed with exception: {e}")

    @staticmethod
    def __getTestInput() -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        resource_path = os.path.join(
            "org", "apache", "commons", "csv", "CSV-248", "csvRecord.bin"
        )
        return open(resource_path, "rb")
