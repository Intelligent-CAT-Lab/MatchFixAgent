from __future__ import annotations
import re
import io


class IntWrapper:

    __value: int = 0

    __serialVersionUID: int = 1

    def toString(self) -> str:
        return str(self.__value)

    def longValue(self) -> int:
        return self.__value

    def intValue(self) -> int:
        return self.__value

    def floatValue(self) -> float:
        return float(self.__value)

    def doubleValue(self) -> float:
        return float(self.__value)

    def set_(self, value: int) -> None:
        self.__value = value

    def increment(self) -> None:
        self.__value += 1

    def get(self) -> int:
        return self.__value

    def add(self, v: int) -> None:
        self.__value += v

    @staticmethod
    def IntWrapper1() -> IntWrapper:
        return IntWrapper(0)

    def __init__(self, v: int) -> None:
        self.__value = v
