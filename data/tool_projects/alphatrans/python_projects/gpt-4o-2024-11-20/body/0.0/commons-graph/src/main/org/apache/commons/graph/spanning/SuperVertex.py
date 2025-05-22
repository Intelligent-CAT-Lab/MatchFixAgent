from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *


class SuperVertex:

    __orderedEdges: typing.Set[typing.Any] = None

    __vertices: typing.Set[typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def merge(self, other: SuperVertex) -> None:
        for v in other.__vertices:
            self.__vertices.add(v)

        for edge in other.__orderedEdges:
            pair = self.__graph.getVertices1(edge)
            if not (
                pair.getHead() in self.__vertices and pair.getTail() in self.__vertices
            ):
                self.__orderedEdges.add(edge)

    def iterator(self) -> typing.Iterator[typing.Any]:
        return iter(self.__vertices)

    def getMinimumWeightEdge(self) -> typing.Any:
        found = False
        edge = None
        while not found and self.__orderedEdges:
            edge = self.__orderedEdges.pop(
                0
            )  # Assuming __orderedEdges is a sorted list
            pair = self.__graph.getVertices1(edge)
            if not (
                pair.getHead() in self.__vertices and pair.getTail() in self.__vertices
            ):
                found = True
        return edge

    def __init__(
        self,
        source: typing.Any,
        graph: Graph[typing.Any, typing.Any],
        weightComparator: WeightedEdgesComparator[typing.Any, typing.Any],
    ) -> None:
        self.__graph = graph

        self.__vertices = set()
        self.__vertices.add(source)

        self.__orderedEdges = sorted(
            (graph.getEdge(source, w) for w in graph.getConnectedVertices(source)),
            key=weightComparator,
        )
