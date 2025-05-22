from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class HeadVertexConnector(ABC):

    def from_(self, head: H) -> TailVertexConnector[V, E]:
        pass
