from __future__ import annotations
import re
from abc import ABC
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class ShortestPathAlgorithmSelector(ABC):

    def applyingDijkstra(
        self, weightOperations: OrderedMonoid[W]
    ) -> WeightedPath[V, WE, W]:
        # Implementation would go here
        pass

    def applyingBidirectionalDijkstra(
        self, weightOperations: OrderedMonoid
    ) -> WeightedPath[V, WE, W]:
        pass

    def applyingAStar(
        self, weightOperations: OrderedMonoid
    ) -> HeuristicBuilder[V, WE, W]:
        pass
