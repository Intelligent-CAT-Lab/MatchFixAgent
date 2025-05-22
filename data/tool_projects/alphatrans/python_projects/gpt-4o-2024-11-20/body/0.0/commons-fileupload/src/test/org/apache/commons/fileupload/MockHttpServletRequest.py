from __future__ import annotations
import time
import re
import unittest
import pytest
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.FileUploadBase import *


class MockHttpServletRequest:

    __m_headers: typing.Dict[str, str] = {}
    __readLimit: int = -1
    __m_strContentType: str = ""

    __length: int = 0

    __m_requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    def getRealPath(self, arg0: str) -> str:
        return None

    def getLocalAddr(self) -> str:
        return None

    def getRemotePort(self) -> int:
        return 0

    def getLocalPort(self) -> int:
        return 0

    def getLocalName(self) -> str:
        return None

    def isRequestedSessionIdFromUrl(self) -> bool:
        return False

    def isSecure(self) -> bool:
        return False

    def getLocales(self) -> typing.Union[typing.Iterator[Locale], None]:
        return None

    def getLocale(self) -> typing.Any:
        return None

    def removeAttribute(self, arg0: str) -> None:
        pass

    def setAttribute(self, arg0: str, arg1: typing.Any) -> None:
        pass

    def getRemoteHost(self) -> str:
        return None

    def getRemoteAddr(self) -> str:
        return None

    def getReader(self) -> io.BufferedReader:
        return None

    def getServerPort(self) -> int:
        return 0

    def getServerName(self) -> str:
        return None

    def getScheme(self) -> str:
        return None

    def getProtocol(self) -> str:
        return None

    def getParameterMap(self) -> typing.Dict[str, typing.List[str]]:
        return None

    def getParameterValues(self, arg0: str) -> typing.Optional[typing.List[str]]:
        return None

    def getParameterNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        return iter([])

    def getParameter(self, arg0: str) -> str:
        return None

    def setReadLimit(self, readLimit: int) -> None:
        self.__readLimit = readLimit

    def getContentType(self) -> str:
        return self.__m_strContentType

    def setContentLength(self, length: int) -> None:
        self.__length = length

    def getContentLength(self) -> int:
        iLength = 0

        if self.__m_requestData is None:
            iLength = -1
        else:
            if self.__length > (2**31 - 1):  # 2147483647 in Java is 2^31 - 1
                raise RuntimeError(
                    f"Value '{self.__length}' is too large to be converted to int"
                )
            iLength = int(self.__length)

        return iLength

    def setCharacterEncoding(self, arg0: str) -> None:
        # In Python, this method would typically not throw an exception like ValueError.
        # However, you can raise a ValueError if the encoding is invalid.
        try:
            # Validate the encoding by attempting to use it
            "".encode(arg0)
        except LookupError:
            raise ValueError(f"Unsupported encoding: {arg0}")

    def getCharacterEncoding(self) -> str:
        return None

    def getAttributeNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        return iter([])

    def getAttribute(self, arg0: str) -> typing.Any:
        return None

    def isRequestedSessionIdFromURL(self) -> bool:
        return False

    def isRequestedSessionIdFromCookie(self) -> bool:
        return False

    def isRequestedSessionIdValid(self) -> bool:
        return False

    def getServletPath(self) -> str:
        return None

    def getRequestURL(self) -> io.StringIO:
        return io.StringIO()

    def getRequestURI(self) -> str:
        return None

    def getRequestedSessionId(self) -> str:
        return None

    def isUserInRole(self, arg0: str) -> bool:
        return False

    def getRemoteUser(self) -> str:
        return None

    def getQueryString(self) -> str:
        return None

    def getContextPath(self) -> str:
        return None

    def getPathTranslated(self) -> str:
        return None

    def getPathInfo(self) -> str:
        return None

    def getMethod(self) -> str:
        return None

    def getHeaderNames(
        self,
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        return None

    def getHeaders(
        self, arg0: str
    ) -> typing.Union[
        typing.Iterator[typing.Any], typing.Generator[str, typing.Any, typing.Any]
    ]:
        return iter([])

    def getHeader(self, headerName: str) -> str:
        return self.__m_headers.get(headerName)

    def getDateHeader(self, arg0: str) -> int:
        return 0

    def getAuthType(self) -> str:
        return None

    @staticmethod
    def MockHttpServletRequest1(
        requestData: typing.List[int], strContentType: str
    ) -> MockHttpServletRequest:
        return MockHttpServletRequest(
            0, io.BytesIO(bytes(requestData)), strContentType, len(requestData)
        )

    def __init__(
        self,
        constructorId: int,
        requestData: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        strContentType: str,
        requestLength: int,
    ) -> None:
        if constructorId == 0:
            self.__m_requestData = requestData
            self.__length = requestLength
            self.__m_strContentType = strContentType
            self.__m_headers[FileUploadBase.CONTENT_TYPE] = strContentType
        else:
            self.__m_requestData = requestData
            self.__length = requestLength
            self.__m_strContentType = strContentType
            self.__m_headers[FileUploadBase.CONTENT_TYPE] = strContentType


class MyServletInputStream:

    __readLimit: int = 0

    __in: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        if self.__readLimit > 0:
            return self.__in.readinto(
                memoryview(b)[off : off + min(self.__readLimit, len_)]
            )
        return self.__in.readinto(memoryview(b)[off : off + len_])

    def read0(self) -> int:
        return self.__in.read(1)

    def __init__(
        self,
        pStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        readLimit: int,
    ) -> None:
        self.__in = pStream
        self.__readLimit = readLimit
