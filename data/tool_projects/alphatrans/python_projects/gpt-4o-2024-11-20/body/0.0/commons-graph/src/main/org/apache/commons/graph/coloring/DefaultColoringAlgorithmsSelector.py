from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.main.org.apache.commons.graph.coloring.UncoloredOrderedVertices import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultColoringAlgorithmsSelector:

    __colors: typing.Set[typing.Any] = None

    __g: UndirectedGraph[typing.Any, typing.Any] = None

    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:
        coloredVertices = ColoredVertices()

        uncoloredOrderedVertices = UncoloredOrderedVertices()
        for v in self.__g.getVertices0():
            uncoloredOrderedVertices.addVertexDegree(v, self.__g.getDegree(v))

        colorsIt = iter(self.__colors)
        while uncoloredOrderedVertices:
            try:
                color = next(colorsIt)
            except StopIteration:
                raise NotEnoughColorsException(self.__colors)

            currentColorVertices = []
            uncoloredVtxIterator = iter(uncoloredOrderedVertices)
            for uncoloredVtx in list(uncoloredOrderedVertices):
                foundAnAdjacentVertex = False
                for currentColoredVtx in currentColorVertices:
                    if self.__g.getEdge(currentColoredVtx, uncoloredVtx) is not None:
                        foundAnAdjacentVertex = True
                        break

                if not foundAnAdjacentVertex:
                    uncoloredOrderedVertices.remove(uncoloredVtx)
                    coloredVertices.addColor(uncoloredVtx, color)
                    currentColorVertices.append(uncoloredVtx)

        return coloredVertices

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:
        partialColoredVertex = Assertions.checkNotNull(
            partialColoredVertex, "PartialColoredVertex must be not null", []
        )

        verticesList: typing.List[typing.Any] = []

        for v in self.__g.getVertices0():
            if not partialColoredVertex.containsColoredVertex(v):
                verticesList.append(v)

        if self.__backtraking(-1, verticesList, partialColoredVertex):
            return partialColoredVertex

        raise NotEnoughColorsException(self.__colors)

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:
        return self.applyingBackTrackingAlgorithm1(ColoredVertices())

    def __init__(
        self, g: UndirectedGraph[typing.Any, typing.Any], colors: typing.Set[typing.Any]
    ) -> None:
        self.__g = g
        self.__colors = colors

    def __isThereColorConflict(
        self,
        currentVertex: typing.Any,
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:
        if currentVertex is None:
            return False

        nextVertexColor = coloredVertices.getColor(currentVertex)
        if nextVertexColor is None:
            return False

        for adj in self.__g.getConnectedVertices(currentVertex):
            adjColor = coloredVertices.getColor(adj)
            if adjColor is not None and nextVertexColor == adjColor:
                return True

        return False

    def __backtraking(
        self,
        currentVertexIndex: int,
        verticesList: typing.List[typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:
        if currentVertexIndex != -1 and self.__isThereColorConflict(
            verticesList[currentVertexIndex], coloredVertices
        ):
            return False

        if currentVertexIndex == len(verticesList) - 1:
            return True

        next_index = currentVertexIndex + 1
        next_vertex = verticesList[next_index]
        for color in self.__colors:
            coloredVertices.addColor(next_vertex, color)
            is_done = self.__backtraking(next_index, verticesList, coloredVertices)
            if is_done:
                return True
        coloredVertices.removeColor(next_vertex)
        return False
