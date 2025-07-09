from __future__ import annotations
import re
import typing
from typing import *
from io import BytesIO
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.fileupload.MultipartStream import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class MultipartStreamTest(unittest.TestCase):

    __BOUNDARY_TEXT: str = "myboundary"

    def testTwoParamConstructor_test1_decomposed(self) -> None:
        str_data = "foobar"
        contents = str_data.encode()  # Convert string to bytes
        input_stream = io.BytesIO(contents)  # Create a ByteArrayInputStream equivalent
        boundary = self.__BOUNDARY_TEXT.encode()  # Convert boundary text to bytes
        ms = MultipartStream.MultipartStream2(
            input_stream,
            boundary,
            MultipartStream.ProgressNotifier(None, len(contents)),
        )
        self.assertIsNotNone(ms)  # Assert that ms is not None

    def testTwoParamConstructor_test0_decomposed(self) -> None:
        str_data = "foobar"
        contents = str_data.encode()  # Convert string to bytes
        input_stream = io.BytesIO(contents)  # Create a ByteArrayInputStream equivalent
        boundary = self.__BOUNDARY_TEXT.encode()  # Convert boundary text to bytes
        ms = MultipartStream.MultipartStream2(
            input_stream, boundary, ProgressNotifier(None, len(contents))
        )

    def testSmallBuffer_test0_decomposed(self) -> None:
        str_data = "foobar"
        contents = str_data.encode()  # Convert string to bytes
        input_stream = io.BytesIO(contents)  # Create a ByteArrayInputStream equivalent
        boundary = self.__BOUNDARY_TEXT.encode()  # Convert boundary string to bytes
        buf_size = 1

        with pytest.raises(
            ValueError
        ):  # Expecting an exception (ValueError in Java maps to ValueError in Python)
            MultipartStream(
                input_stream, boundary, buf_size, ProgressNotifier(None, len(contents))
            )

    def testThreeParamConstructor_test1_decomposed(self) -> None:
        str_data = "foobar"
        contents = str_data.encode()  # Convert string to bytes
        input_stream = io.BytesIO(contents)  # Create a ByteArrayInputStream equivalent
        boundary = self.__BOUNDARY_TEXT.encode()  # Convert boundary text to bytes
        buf_size = len(boundary) + len(MultipartStream._BOUNDARY_PREFIX) + 1
        ms = MultipartStream(
            input_=input_stream,
            boundary=list(boundary),  # Convert bytes to a list of integers
            bufSize=buf_size,
            pNotifier=ProgressNotifier(None, len(contents)),
        )
        self.assertIsNotNone(ms)

    def testThreeParamConstructor_test0_decomposed(self) -> None:
        str_data = "foobar"
        contents = str_data.encode()  # Convert string to bytes
        input_stream = io.BytesIO(contents)  # Create a ByteArrayInputStream equivalent
        boundary = self.__BOUNDARY_TEXT.encode()  # Convert boundary text to bytes
        i_buf_size = len(boundary) + len(MultipartStream._BOUNDARY_PREFIX) + 1
        ms = MultipartStream(
            input_=input_stream,
            boundary=list(boundary),  # Convert bytes to a list of integers
            bufSize=i_buf_size,
            pNotifier=ProgressNotifier(None, len(contents)),
        )
