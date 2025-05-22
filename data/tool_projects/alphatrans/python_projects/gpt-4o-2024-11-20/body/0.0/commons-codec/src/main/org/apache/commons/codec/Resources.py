from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class Resources:

    @staticmethod
    def getInputStream(
        name: str,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        input_stream = Resources.__class__.__module__.get_resource_stream(name)
        if input_stream is None:
            raise ValueError(f"Unable to resolve required resource: {name}")
        return input_stream
