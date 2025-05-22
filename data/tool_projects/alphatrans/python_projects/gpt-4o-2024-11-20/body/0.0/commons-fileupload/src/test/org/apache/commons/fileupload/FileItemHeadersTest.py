from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.fileupload.util.FileItemHeadersImpl import *


class FileItemHeadersTest(unittest.TestCase):

    def testFileItemHeaders_test25_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue4")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader")
        self.assertFalse(any(headerValueEnumeration))

    def testFileItemHeaders_test24_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue4")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader")
        self.assertFalse(any(headerValueEnumeration))

    def testFileItemHeaders_test23_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue4")
        self.assertFalse(any(headerValueEnumeration))

    def testFileItemHeaders_test22_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue4")

    def testFileItemHeaders_test21_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")
        self.assertTrue(any(headerValueEnumeration))

    def testFileItemHeaders_test20_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue3")

    def testFileItemHeaders_test19_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")
        self.assertTrue(any(headerValueEnumeration))

    def testFileItemHeaders_test18_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue2")

    def testFileItemHeaders_test17_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")
        self.assertTrue(any(headerValueEnumeration))

    def testFileItemHeaders_test16_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "headerValue1")

    def testFileItemHeaders_test15_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        self.assertTrue(any(headerValueEnumeration))

    def testFileItemHeaders_test14_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Check if no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Check if no more values exist

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Check if no more values exist

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader")
        # Additional assertions can be added here if needed

    def testFileItemHeaders_test13_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Ensure no more values exist

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Ensure no more values exist

    def testFileItemHeaders_test12_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Ensure no more values exist

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")

    def testFileItemHeaders_test11_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # No more headers should exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # No more values should exist

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")
        self.assertTrue(any(headerValueEnumeration))

    def testFileItemHeaders_test10_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(
            any(headerNameEnumeration)
        )  # Check if there are no more elements

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))  # Check if there are elements
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(
            any(headerValueEnumeration)
        )  # Check if there are no more elements

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type")

    def testFileItemHeaders_test9_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))  # Ensure there are headers
        self.assertEqual(next(headerValueEnumeration), "text/plain")
        self.assertFalse(any(headerValueEnumeration))  # Ensure no more headers exist

    def testFileItemHeaders_test8_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(
            any(headerNameEnumeration)
        )  # Check if there are no more elements

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))  # Check if there are elements
        self.assertEqual(next(headerValueEnumeration), "text/plain")

    def testFileItemHeaders_test7_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        self.assertTrue(any(headerValueEnumeration))  # Ensure there are headers

    def testFileItemHeaders_test6_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type")
        # Additional assertions can be added here if needed

    def testFileItemHeaders_test5_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual(next(headerNameEnumeration), "content-disposition")
        self.assertEqual(next(headerNameEnumeration), "content-type")
        self.assertEqual(next(headerNameEnumeration), "testheader")
        self.assertFalse(any(headerNameEnumeration))  # Ensure no more headers exist

        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Disposition"),
            'form-data; name="FileItem"; filename="file1.txt"',
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("content-type"), "text/plain"
        )
        self.assertEqual(
            aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1"
        )
        self.assertIsNone(aMutableFileItemHeaders.getHeader("DummyHeader"))

    def testFileItemHeaders_test4_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual("content-disposition", next(headerNameEnumeration))
        self.assertEqual("content-type", next(headerNameEnumeration))
        self.assertEqual("testheader", next(headerNameEnumeration))
        self.assertFalse(any(headerNameEnumeration))

    def testFileItemHeaders_test3_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()
        self.assertEqual("content-disposition", next(headerNameEnumeration))
        self.assertEqual("content-type", next(headerNameEnumeration))
        self.assertEqual("testheader", next(headerNameEnumeration))

    def testFileItemHeaders_test2_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")
        headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames()

    def testFileItemHeaders_test1_decomposed(self) -> None:
        aMutableFileItemHeaders = FileItemHeadersImpl()
        aMutableFileItemHeaders.addHeader(
            "Content-Disposition", 'form-data; name="FileItem"; filename="file1.txt"'
        )
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2")
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3")
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4")

    def testFileItemHeaders_test0_decomposed(self) -> None:
        a_mutable_file_item_headers = FileItemHeadersImpl()
