from __future__ import annotations
import inspect
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.UsageTracking import *
from src.main.org.apache.commons.pool2.proxy.BaseProxyHandler import *


class JdkProxyHandler(BaseProxyHandler):

    def invoke(
        self,
        proxy: typing.Any,
        method: typing.Union[inspect.Signature, typing.Callable],
        args: typing.List[typing.Any],
    ) -> typing.Any:
        return self.do_invoke(method, args)

    def __init__(
        self, pooledObject: typing.Any, usageTracking: UsageTracking[typing.Any]
    ) -> None:
        super().__init__(pooledObject, usageTracking)
