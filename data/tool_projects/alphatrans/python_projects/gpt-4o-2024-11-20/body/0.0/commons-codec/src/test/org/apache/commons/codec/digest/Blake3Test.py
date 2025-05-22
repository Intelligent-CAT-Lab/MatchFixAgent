from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3Test(unittest.TestCase):

    def shouldThrowValueErrorWhenIncorrectKeySize_test0_decomposed(self) -> None:
        for i in range(32):
            self.__assertThrowsProperExceptionWithKeySize(i)
        self.__assertThrowsProperExceptionWithKeySize(33)

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:
        with pytest.raises(ValueError) as excinfo:
            Blake3.initKeyedHash([0] * keySize)
        assert str(excinfo.value) == "Blake3 keys must be 32 bytes"
