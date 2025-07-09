from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.connectivity.ConnectedComponentHandler import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *


class DefaultConnectivityAlgorithmsSelector:

    __includedVertices: typing.Iterable[typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def applyingMinimumSpanningTreeAlgorithm(
        self,
    ) -> typing.Collection[typing.List[typing.Any]]:
        untouched_vertices: typing.List[typing.Any] = []

        for v in self.__includedVertices:
            Assertions.checkState(
                self.__graph.containsVertex(v),
                "Vertex {} does not exist in the Graph".format(v),
                [],
            )
            untouched_vertices.append(v)

        connected_vertices: typing.Collection[typing.List[typing.Any]] = []

        while len(untouched_vertices) > 0:
            source = untouched_vertices.pop(0)

            connected_vertices.append(
                CommonsGraph.visit(self.__graph)
                .from_(source)
                .applyingDepthFirstSearch1(
                    ConnectedComponentHandler(untouched_vertices)
                )
            )

        return connected_vertices

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        includedVertices: typing.Iterable[typing.Any],
    ) -> None:
        self.__graph = graph
        self.__includedVertices = includedVertices
