from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class Mapper(ABC):

    def map_(self, input_: typing.Any) -> typing.Any:
        return input_
