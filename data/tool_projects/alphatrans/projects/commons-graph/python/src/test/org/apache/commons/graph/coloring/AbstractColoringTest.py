from __future__ import annotations
import re
import random
import unittest
import pytest
from abc import ABC
import io
import numbers
import typing
from typing import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *


class AbstractColoringTest(ABC):

    def _createColorsList(self, colorNumber: int) -> typing.Set[int]:
        colors = set()
        for j in range(colorNumber):
            colors.add(j)
        return colors

    def _createColorMap(self, numColor: int) -> typing.Dict[int, str]:
        colorCodes: typing.Dict[int, str] = {}
        for i in range(100):
            rnd = random.Random(i)
            colorCodes[i] = (
                f"#{rnd.randint(0, 255):02x}{rnd.randint(0, 255):02x}{rnd.randint(0, 255):02x}"
            )
        return colorCodes

    def _checkColoring(
        self,
        g: UndirectedMutableGraph[typing.Any, typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> None:
        for e in g.getEdges():
            vp = g.getVertices1(e)
            h = coloredVertices.getColor(vp.getHead())
            t = coloredVertices.getColor(vp.getTail())

            self.assertIsNotNone(h)
            self.assertIsNotNone(t)
            self.assertTrue(h != t)

    def __init__(self) -> None:
        pass
