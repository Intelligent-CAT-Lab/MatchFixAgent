from __future__ import annotations
import time
import re
import enum
import io
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.pool2.PooledObjectFactory import *


class PoolImplUtils:

    @staticmethod
    def getFactoryType(
        factoryClass: typing.Type[PooledObjectFactory[typing.Any]],
    ) -> typing.Type[typing.Any]:
        type_ = PooledObjectFactory
        genericType = PoolImplUtils.__getGenericType(type_, factoryClass)

        if isinstance(genericType, int):
            parameterizedType = PoolImplUtils.__getParameterizedType(
                type_, factoryClass
            )
            if parameterizedType is not None:
                typeArguments = parameterizedType.__args__
                if isinstance(typeArguments[genericType], typing.TypeVar):
                    bounds = typeArguments[genericType].__bound__
                    if bounds is not None:
                        if isinstance(bounds, type):
                            return bounds
            return object
        return genericType

    @staticmethod
    def toDuration(amount: int, timeUnit: datetime.timedelta) -> datetime.timedelta:
        if timeUnit is None:
            raise ValueError("timeUnit cannot be None")
        return amount * timeUnit

    @staticmethod
    def nonNull(
        value: datetime.timedelta, defaultValue: datetime.timedelta
    ) -> datetime.timedelta:
        return value if value is not None else defaultValue

    @staticmethod
    def toChronoUnit(timeUnit: str) -> datetime.timedelta:
        if timeUnit is None:
            raise ValueError("timeUnit cannot be None")

        match timeUnit:
            case "NANOSECONDS":
                return datetime.timedelta(microseconds=1) / 1000
            case "MICROSECONDS":
                return datetime.timedelta(microseconds=1)
            case "MILLISECONDS":
                return datetime.timedelta(milliseconds=1)
            case "SECONDS":
                return datetime.timedelta(seconds=1)
            case "MINUTES":
                return datetime.timedelta(minutes=1)
            case "HOURS":
                return datetime.timedelta(hours=1)
            case "DAYS":
                return datetime.timedelta(days=1)
            case _:
                raise ValueError(f"Invalid timeUnit: {timeUnit}")

    return a if a < b else b
    return a if a > b else b

    @staticmethod
    def isPositive(delay: datetime.timedelta) -> bool:
        return delay is not None and delay.total_seconds() > 0

    @staticmethod
    def __getTypeParameter(
        clazz: typing.Type[typing.Any], argType: typing.Type
    ) -> typing.Any:
        if isinstance(
            argType, type
        ):  # Equivalent to Java's `argType instanceof Class<?>`
            return argType
        type_vars = clazz.__parameters__ if hasattr(clazz, "__parameters__") else []
        for i, tv in enumerate(type_vars):
            if tv == argType:
                return i
        return None

    @staticmethod
    def __getParameterizedType(
        type_: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Optional[typing.ParameterizedType]:
        for iface in getattr(clazz, "__orig_bases__", []):
            if isinstance(
                iface, typing._GenericAlias
            ):  # Check if iface is a parameterized type
                raw_type = iface.__origin__
                if isinstance(raw_type, type) and issubclass(raw_type, type_):
                    return iface
        return None

    @staticmethod
    def __getGenericType(
        type_: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Any:
        if type_ is None or clazz is None:
            return None

        # Attempt to get the parameterized type
        parameterized_type = PoolImplUtils.__getParameterizedType(type_, clazz)
        if parameterized_type is not None:
            return PoolImplUtils.__getTypeParameter(
                clazz, parameterized_type.__args__[0]
            )

        # Get the superclass of the current class
        super_class = getattr(clazz, "__base__", None)
        if super_class is None:
            return None

        # Recursively call __getGenericType on the superclass
        result = PoolImplUtils.__getGenericType(type_, super_class)
        if isinstance(result, type):
            return result
        if isinstance(result, int):
            # Get the generic superclass and its type arguments
            generic_superclass = getattr(clazz, "__orig_bases__", None)
            if generic_superclass:
                for base in generic_superclass:
                    if (
                        isinstance(base, typing._GenericAlias)
                        and base.__origin__ == super_class
                    ):
                        return PoolImplUtils.__getTypeParameter(
                            clazz, base.__args__[result]
                        )
        return None
