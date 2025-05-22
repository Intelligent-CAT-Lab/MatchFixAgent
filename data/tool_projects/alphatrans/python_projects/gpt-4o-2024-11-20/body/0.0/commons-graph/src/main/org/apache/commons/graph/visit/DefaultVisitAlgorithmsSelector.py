from __future__ import annotations
import re
import collections
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitGraphBuilder import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class DefaultVisitAlgorithmsSelector(VisitAlgorithmsSelector):

    __source: typing.Any = None

    __graph: typing.Any = None

    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        return self.__applyingSearch(handler, False)

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        return self.applyingDepthFirstSearch1(
            VisitGraphBuilder[typing.Any, typing.Any, typing.Any]()
        )

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        return self.__applyingSearch(handler, True)

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        return self.applyingBreadthFirstSearch1(
            VisitGraphBuilder[typing.Any, typing.Any, Graph[typing.Any, typing.Any]]()
        )

    def __init__(self, graph: typing.Any, source: typing.Any) -> None:
        self.__graph = graph
        self.__source = source

    def __applyingSearch(
        self,
        handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any],
        enqueue: bool,
    ) -> typing.Any:
        handler = Assertions.checkNotNull(
            handler, "Graph visitor handler can not be null.", []
        )

        handler.discoverGraph(self.__graph)

        vertex_list = collections.deque()
        vertex_list.append(VertexPair(self.__source, self.__source))

        visited_vertices = set()
        visited_vertices.add(self.__source)

        visiting_graph = True

        while visiting_graph and vertex_list:
            pair = vertex_list.popleft() if enqueue else vertex_list.pop()
            v = pair.getHead()
            prev_head = pair.getTail()
            e = None if prev_head == v else self.__graph.getEdge(prev_head, v)

            skip_vertex = False

            if e is not None:
                if v in visited_vertices:
                    skip_vertex = True
                else:
                    state_after_edge_discovery = handler.discoverEdge(prev_head, e, v)
                    if VisitState.CONTINUE != state_after_edge_discovery:
                        skip_vertex = True
                        if VisitState.ABORT == state_after_edge_discovery:
                            visiting_graph = False

                    if VisitState.ABORT == handler.finishEdge(prev_head, e, v):
                        skip_vertex = True
                        visiting_graph = False

            vertex_was_discovered = False
            if not skip_vertex:
                visited_vertices.add(v)
                state_after_vertex_discovery = handler.discoverVertex(v)
                vertex_was_discovered = True
                if VisitState.CONTINUE != state_after_vertex_discovery:
                    skip_vertex = True
                    if VisitState.ABORT == state_after_vertex_discovery:
                        visiting_graph = False

            if not skip_vertex:
                connected = (
                    self.__graph.getOutbound(v)
                    if isinstance(self.__graph, DirectedGraph)
                    else self.__graph.getConnectedVertices(v)
                )

                for w in connected:
                    if w not in visited_vertices:
                        vertex_list.append(VertexPair(w, v))

            if vertex_was_discovered and VisitState.ABORT == handler.finishVertex(v):
                visiting_graph = False

        handler.finishGraph(self.__graph)

        return handler.onCompleted()
