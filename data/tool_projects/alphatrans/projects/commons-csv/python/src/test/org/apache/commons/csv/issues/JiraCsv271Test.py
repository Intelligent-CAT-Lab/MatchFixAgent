from __future__ import annotations
import re
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.csv.CSVFormat import *
from src.main.org.apache.commons.csv.CSVPrinter import *


class JiraCsv271Test(unittest.TestCase):

    def testJiraCsv271_withList_test1_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print_("a")
            printer.printRecord0(["b", "c"])
        self.assertEqual("a,b,c\r\n", string_writer.getvalue())

    def testJiraCsv271_withList_test0_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print_("a")
            printer.printRecord0(["b", "c"])

    def testJiraCsv271_withArray_test1_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print_("a")
            printer.printRecord1("b", "c")
        self.assertEqual("a,b,c\r\n", string_writer.getvalue())

    def testJiraCsv271_withArray_test0_decomposed(self) -> None:
        csv_format = CSVFormat.DEFAULT
        string_writer = io.StringIO()
        with CSVPrinter(string_writer, csv_format) as printer:
            printer.print_("a")
            printer.printRecord1("b", "c")
