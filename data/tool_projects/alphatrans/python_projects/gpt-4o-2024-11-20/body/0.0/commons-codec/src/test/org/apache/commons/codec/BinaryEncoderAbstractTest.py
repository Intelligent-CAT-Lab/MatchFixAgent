from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import os
import unittest
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class BinaryEncoderAbstractTest(ABC, unittest.TestCase):

    def testEncodeNull_test1_decomposed(self) -> None:
        encoder = self._makeEncoder()
        with pytest.raises(EncoderException):
            encoder.encode(None)

    def testEncodeNull_test0_decomposed(self) -> None:
        encoder = self._makeEncoder()

    def testEncodeEmpty_test1_decomposed(self) -> None:
        encoder = self._makeEncoder()
        encoder.encode([])

    def testEncodeEmpty_test0_decomposed(self) -> None:
        encoder = self._makeEncoder()

    def _makeEncoder(self) -> BinaryEncoder:
        raise NotImplementedError("Subclasses must implement this method")
