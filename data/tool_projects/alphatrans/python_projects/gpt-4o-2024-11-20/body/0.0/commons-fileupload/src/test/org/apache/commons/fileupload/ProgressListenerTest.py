from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.ProgressListener import *


class ProgressListenerTest:

    pass


class ProgressListenerImpl(ProgressListener):

    __items: int = 0

    __bytesRead: int = 0

    __expectedItems: int = 0

    __expectedContentLength: int = 0

    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
        self.assertTrue(0 <= pBytesRead <= self.__expectedContentLength)
        self.assertTrue(
            pContentLength == -1 or pContentLength == self.__expectedContentLength
        )
        self.assertTrue(0 <= pItems <= self.__expectedItems)

        self.assertTrue(self.__bytesRead is None or pBytesRead >= self.__bytesRead)
        self.__bytesRead = pBytesRead
        self.assertTrue(self.__items is None or pItems >= self.__items)
        self.__items = pItems

    def checkFinished(self) -> None:
        self.assertEqual(self.__expectedContentLength, self.__bytesRead)
        self.assertEqual(self.__expectedItems, self.__items)

    def __init__(self, pContentLength: int, pItems: int) -> None:
        self.__expectedContentLength = pContentLength
        self.__expectedItems = pItems
