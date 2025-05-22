from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *


class FromHeadBuilder(ABC):

    def from_(self, head: H) -> ToTailBuilder[V, WE, W]:
        pass
