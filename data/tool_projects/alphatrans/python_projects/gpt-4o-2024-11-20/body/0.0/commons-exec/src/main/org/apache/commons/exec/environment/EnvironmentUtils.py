from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.exec.environment.DefaultProcessingEnvironment import *


class EnvironmentUtils:

    __ENVIRONMENT: DefaultProcessingEnvironment = None

    @staticmethod
    def run_static_init():
        EnvironmentUtils.__ENVIRONMENT = DefaultProcessingEnvironment()

    @staticmethod
    def toStrings(
        environment: typing.Optional[typing.Dict[str, str]],
    ) -> typing.Optional[typing.List[str]]:
        if environment is None:
            return None
        return [f"{str(key)}={str(value)}" for key, value in environment.items()]

    @staticmethod
    def getProcEnvironment() -> typing.Dict[str, str]:
        return EnvironmentUtils.__ENVIRONMENT.getProcEnvironment()

    @staticmethod
    def addVariableToEnvironment(
        environment: typing.Dict[str, str], keyAndValue: str
    ) -> None:
        parsedVariable = EnvironmentUtils.__parseEnvironmentVariable(keyAndValue)
        environment[parsedVariable[0]] = parsedVariable[1]

    def __init__(self) -> None:
        pass

    @staticmethod
    def __toString(value: str) -> str:
        return str(value) if value is not None else ""

    @staticmethod
    def __parseEnvironmentVariable(keyAndValue: str) -> List[str]:
        index = keyAndValue.find("=")
        if index == -1:
            raise ValueError(
                "Environment variable for this platform must contain an equals sign ('=')"
            )
        result = [keyAndValue[:index], keyAndValue[index + 1 :]]
        return result


EnvironmentUtils.run_static_init()
