from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class PathSourceSelector(ABC):

    def from_(self, source: H) -> TargetSourceSelector[V, WE, W]:
        pass

    def applyingFloydWarshall(
        self, weightOperations: OrderedMonoid[typing.Any]
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        return AllVertexPairsShortestPath(weightOperations)
