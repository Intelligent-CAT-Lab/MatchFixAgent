from __future__ import annotations
import copy
import re
import io
import typing
from typing import *


class MapUtils:

    @staticmethod
    def prefix(
        source: typing.Dict[typing.Any, typing.Any], prefix: str
    ) -> typing.Dict[str, typing.Any]:
        if source is None:
            return None
        result: typing.Dict[str, typing.Any] = {}
        for key, value in source.items():
            result[f"{prefix}.{str(key)}"] = value
        return result

    @staticmethod
    def merge(
        lhs: typing.Dict[typing.Any, typing.Any],
        rhs: typing.Dict[typing.Any, typing.Any],
    ) -> typing.Dict[typing.Any, typing.Any]:
        if lhs is None or not lhs:
            return MapUtils.copy(rhs)
        elif rhs is None or not rhs:
            return MapUtils.copy(lhs)
        else:
            result = MapUtils.copy(lhs)
            result.update(rhs)
            return result

    @staticmethod
    def copy(
        source: typing.Dict[typing.Any, typing.Any],
    ) -> typing.Dict[typing.Any, typing.Any]:
        return None if source is None else dict(source)
