from __future__ import annotations
import time
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.NegativeWeightedCycleException import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultTargetSourceSelector(TargetSourceSelector):

    __source: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def to(
        self, target: typing.Any
    ) -> ShortestPathAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        target = Assertions.checkNotNull(
            target, "Shortest path can not be calculated to a null target", []
        )
        return DefaultShortestPathAlgorithmSelector(
            self.__graph, self.__weightedEdges, self.__source, target
        )

    def applyingBelmannFord(
        self, weightOperations: OrderedMonoid
    ) -> AllVertexPairsShortestPath:
        # Ensure weightOperations is not null
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "Belmann-Ford algorithm cannot be applied using null weight operations",
            [],
        )

        # Initialize shortest distances and set the source weight to the identity element
        shortestDistances = ShortestDistances(weightOperations)
        shortestDistances.setWeight(self.__source, weightOperations.identity())

        # Initialize predecessors list
        predecessors = PredecessorsList(
            self.__graph, weightOperations, self.__weightedEdges
        )

        # Relax edges |V| - 1 times
        for _ in range(self.__graph.getOrder()):
            for edge in self.__graph.getEdges():
                vertexPair = self.__graph.getVertices1(edge)
                u = vertexPair.getHead()
                v = vertexPair.getTail()

                if shortestDistances.alreadyVisited(u):
                    shortDist = weightOperations.append(
                        shortestDistances.getWeight(u), self.__weightedEdges.map(edge)
                    )

                    if (
                        not shortestDistances.alreadyVisited(v)
                        or weightOperations.compare(
                            shortDist, shortestDistances.getWeight(v)
                        )
                        < 0
                    ):
                        shortestDistances.setWeight(v, shortDist)
                        predecessors.addPredecessor(v, u)

        # Check for negative-weight cycles
        for edge in self.__graph.getEdges():
            vertexPair = self.__graph.getVertices1(edge)
            u = vertexPair.getHead()
            v = vertexPair.getTail()

            if shortestDistances.alreadyVisited(u):
                shortDist = weightOperations.append(
                    shortestDistances.getWeight(u), self.__weightedEdges.map(edge)
                )

                if (
                    not shortestDistances.alreadyVisited(v)
                    or weightOperations.compare(
                        shortDist, shortestDistances.getWeight(v)
                    )
                    < 0
                ):
                    raise NegativeWeightedCycleException(
                        "Graph contains a negative-weight cycle in vertex %s", None, [v]
                    )

        # Build the AllVertexPairsShortestPath result
        allVertexPairsShortestPath = AllVertexPairsShortestPath(weightOperations)

        for target in self.__graph.getVertices0():
            if self.__source != target:
                try:
                    weightedPath = predecessors.buildPath0(self.__source, target)
                    allVertexPairsShortestPath.addShortestPath(
                        self.__source, target, weightedPath
                    )
                except PathNotFoundException:
                    continue

        return allVertexPairsShortestPath

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
