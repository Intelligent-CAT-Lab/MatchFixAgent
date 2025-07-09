from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *


class ColoringAlgorithmsSelector(ABC):

    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:
        # Implementation of the greedy algorithm goes here
        # This is a placeholder for the actual logic
        pass

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:
        return partialColoredVertex

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:
        # Implementation of the backtracking algorithm goes here
        pass
