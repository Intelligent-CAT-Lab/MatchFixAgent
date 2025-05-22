from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.flow.FlowNetworkHandler import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class DefaultMaxFlowAlgorithmSelector(MaxFlowAlgorithmSelector):

    __target: typing.Any = None

    __source: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def applyingFordFulkerson(self, weightOperations: typing.Any) -> typing.Any:
        # Ensure weightOperations is not null
        checkedWeightOperations = Assertions.checkNotNull(
            weightOperations,
            "Weight operations can not be null to find the max flow in the graph",
            [],
        )

        # Create a new flow network
        flowNetwork = self.__newFlowNetwok(self.__graph, checkedWeightOperations)

        # Initialize the flow network handler
        flowNetworkHandler = FlowNetworkHandler(
            flowNetwork,
            self.__source,
            self.__target,
            checkedWeightOperations,
            MapperWrapper(checkedWeightOperations, self.__weightedEdges),
        )

        # Perform an initial depth-first search
        CommonsGraph.visit(flowNetwork).from_(self.__source).applyingDepthFirstSearch1(
            flowNetworkHandler
        )

        # While there is an augmenting path, update the residual network
        while flowNetworkHandler.hasAugmentingPath():
            flowNetworkHandler.updateResidualNetworkWithCurrentAugmentingPath()
            CommonsGraph.visit(flowNetwork).from_(
                self.__source
            ).applyingDepthFirstSearch1(flowNetworkHandler)

        # Return the result of the max flow computation
        return flowNetworkHandler.onCompleted()

    def applyingEdmondsKarp(
        self, weightOperations: OrderedMonoid[typing.Any]
    ) -> typing.Any:
        # Ensure weightOperations is not null
        checkedWeightOperations = Assertions.checkNotNull(
            weightOperations,
            "Weight operations can not be null to find the max flow in the graph",
            [],
        )

        # Create a new flow network
        flowNetwork = self.__newFlowNetwok(self.__graph, checkedWeightOperations)

        # Initialize the flow network handler
        flowNetworkHandler = FlowNetworkHandler(
            flowNetwork,
            self.__source,
            self.__target,
            checkedWeightOperations,
            MapperWrapper(checkedWeightOperations, self.__weightedEdges),
        )

        # Perform the initial BFS visit
        CommonsGraph.visit(flowNetwork).from_(
            self.__source
        ).applyingBreadthFirstSearch1(flowNetworkHandler)

        # While there is an augmenting path, update the residual network
        while flowNetworkHandler.hasAugmentingPath():
            flowNetworkHandler.updateResidualNetworkWithCurrentAugmentingPath()
            CommonsGraph.visit(flowNetwork).from_(
                self.__source
            ).applyingBreadthFirstSearch1(flowNetworkHandler)

        # Return the result after completing the max flow computation
        return flowNetworkHandler.onCompleted()

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
        self.__target = target

    def __newFlowNetwok(
        self, graph: DirectedGraph[typing.Any, typing.Any], weightOperations: typing.Any
    ) -> DirectedGraph[typing.Any, EdgeWrapper[typing.Any]]:
        return CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[typing.Any, EdgeWrapper[typing.Any]](
                connect0=lambda: (
                    [self.addVertex(vertex) for vertex in graph.getVertices0()]
                    + [
                        (
                            (
                                self.addEdge(EdgeWrapper(edge))
                                .from_(edgeVertices.getHead())
                                .to(edgeVertices.getTail()),
                                self.addEdge(EdgeWrapper.EdgeWrapper1())
                                .from_(edgeVertices.getTail())
                                .to(edgeVertices.getHead()),
                            )[0]
                            if graph.getEdge(
                                edgeVertices.getTail(), edgeVertices.getHead()
                            )
                            is None
                            else self.addEdge(EdgeWrapper(edge))
                            .from_(edgeVertices.getHead())
                            .to(edgeVertices.getTail())
                        )
                        for edge in graph.getEdges()
                        for edgeVertices in [graph.getVertices1(edge)]
                    ]
                )
            )
        )


class MapperWrapper(Mapper):

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: typing.Any = None

    def map_(self, input_: EdgeWrapper[typing.Any]) -> typing.Any:
        if input_.get_wrapped() is None:
            return self.__weightOperations.identity()
        return self.__weightedEdges.map(input_.get_wrapped())

    def __init__(
        self,
        weightOperations: typing.Any,
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges


class EdgeWrapper:

    __wrapped: typing.Any = None

    def getWrapped(self) -> typing.Any:
        return self.__wrapped

    @staticmethod
    def EdgeWrapper1() -> EdgeWrapper[typing.Any]:
        return EdgeWrapper(None)

    def __init__(self, wrapped: typing.Any) -> None:
        self.__wrapped = wrapped
