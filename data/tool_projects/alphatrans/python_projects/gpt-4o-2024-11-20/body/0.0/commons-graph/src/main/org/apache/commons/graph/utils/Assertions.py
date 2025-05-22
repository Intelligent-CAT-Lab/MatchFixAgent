from __future__ import annotations
import time
import re
import io
import typing
from typing import *


class Assertions:

    @staticmethod
    def checkState(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise RuntimeError(errorMessageTemplate.format(*errorMessageArgs))

    @staticmethod
    def checkNotNull(
        reference: typing.Any,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> typing.Any:
        if reference is None:
            errorMessage = errorMessageTemplate.format(*errorMessageArgs)
            raise RuntimeError(errorMessage)
        return reference

    @staticmethod
    def checkArgument(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise ValueError(errorMessageTemplate.format(*errorMessageArgs))

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated")
