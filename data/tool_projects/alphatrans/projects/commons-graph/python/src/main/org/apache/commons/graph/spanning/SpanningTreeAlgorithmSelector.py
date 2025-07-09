from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class SpanningTreeAlgorithmSelector(ABC):

    def applyingPrimAlgorithm(
        self, weightOperations: OrderedMonoid[W]
    ) -> SpanningTree[V, WE, W]:
        pass

    def applyingKruskalAlgorithm(
        self, weightOperations: OrderedMonoid
    ) -> SpanningTree[Any, Any, Any]:
        pass

    def applyingBoruvkaAlgorithm(
        self, weightOperations: OrderedMonoid[W]
    ) -> SpanningTree[V, WE, W]:
        pass
