from __future__ import annotations
import re
import pickle
import unittest
import pytest
import pathlib
import io
from io import BytesIO
import typing
from typing import *
import os


class DiskFileItemSerializeTest:

    __threshold: int = 16
    __textContentType: str = "text/plain"
    __REPO: pathlib.Path = (
        pathlib.Path(os.getenv("TMPDIR", "/tmp")) / "diskfileitemrepo"
    )

    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> typing.Any:
        result = None
        bais = io.BytesIO(baos.getvalue() if isinstance(baos, io.BytesIO) else baos)
        ois = pickle.Unpickler(bais)
        result = ois.load()
        bais.close()

        return result

    def __serialize(self, target: typing.Any) -> typing.Union[io.BytesIO, bytearray]:
        baos = io.BytesIO()
        oos = pickle.Pickler(baos)
        oos.dump(target)
        baos.seek(0)  # Reset the stream position to the beginning
        return baos

    def __createContentBytes(self, size: int) -> typing.List[int]:
        buffer = []
        count = 0
        for i in range(size):
            buffer.append(str(count))
            count += 1
            if count > 9:
                count = 0
        return "".join(buffer).encode()

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:
        self.assertIsNotNone(origBytes, "origBytes must not be null")
        self.assertIsNotNone(newBytes, "newBytes must not be null")
        self.assertEqual(len(origBytes), len(newBytes), f"{text} byte[] length")
        for i in range(len(origBytes)):
            self.assertEqual(origBytes[i], newBytes[i], f"{text} byte[{i}]")
