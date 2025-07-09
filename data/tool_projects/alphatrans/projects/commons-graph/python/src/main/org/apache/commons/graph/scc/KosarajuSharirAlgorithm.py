from __future__ import annotations
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class KosarajuSharirAlgorithm(SccAlgorithm):

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform1(self, source: typing.Any) -> typing.Set[typing.Any]:
        # Check that the source is not null
        Assertions.checkNotNull(
            source,
            "Kosaraju Sharir algorithm cannot be calculated without expressing the source vertex",
            [],
        )

        # Check that the source vertex exists in the graph
        Assertions.checkState(
            self.__graph.containsVertex(source),
            "Vertex {} does not exist in the Graph".format(source),
            [],
        )

        # Initialize visited vertices set
        visitedVertices: typing.Set[typing.Any] = set()

        # Get the expanded vertex list starting from the source
        expandedVertexList: typing.List[typing.Any] = self.__getExpandedVertexList(
            source, visitedVertices
        )

        # Create a reverted graph
        reverted: DirectedGraph[typing.Any, typing.Any] = RevertedGraph(self.__graph)

        # Remove the last vertex from the expanded vertex list
        v: typing.Any = expandedVertexList.pop()

        # Initialize the strongly connected component (SCC) set
        sccSet: typing.Set[typing.Any] = set()

        # Perform a recursive search on the reverted graph
        self.__searchRecursive(reverted, v, sccSet, visitedVertices, False)

        # Return the SCC set
        return sccSet

    def perform0(self) -> typing.Set[typing.Set[typing.Any]]:
        visited_vertices: typing.Set[typing.Any] = set()
        expanded_vertex_list: typing.List[typing.Any] = self.__getExpandedVertexList(
            None, visited_vertices
        )
        reverted: DirectedGraph[typing.Any, typing.Any] = RevertedGraph(self.__graph)

        sccs: typing.Set[typing.Set[typing.Any]] = set()

        stack: typing.List[typing.Any] = []
        for i in range(len(expanded_vertex_list) - 1, -1, -1):
            stack.append(expanded_vertex_list[i])

        while stack:
            v = stack.pop(0)  # Get the first element from the stack
            scc_set: typing.Set[typing.Any] = set()
            self.__searchRecursive(reverted, v, scc_set, visited_vertices, False)

            stack = [
                x for x in stack if x not in scc_set
            ]  # Remove all elements in scc_set from stack
            sccs.add(frozenset(scc_set))  # Use frozenset to make the set hashable

        return sccs

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        return self.perform0()

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph

    def __searchRecursive(
        self,
        g: DirectedGraph[typing.Any, typing.Any],
        source: typing.Any,
        coll: typing.Collection[typing.Any],
        visited: typing.Set[typing.Any],
        forward: bool,
    ) -> None:
        stack: typing.List[typing.Any] = []
        stack.append(source)

        while stack:
            v = stack.pop()

            if not (forward ^ (v in visited)):
                coll.add(v)
                continue

            stack.append(v)
            if forward:
                visited.add(v)
            else:
                visited.remove(v)

            for w in g.getOutbound(v):
                if not (forward ^ (w not in visited)):
                    stack.append(w)

    def __getExpandedVertexList(
        self, source: typing.Any, visitedVertices: typing.Set[typing.Any]
    ) -> typing.List[typing.Any]:
        size = 13 if source is not None else self.__graph.getOrder()
        vertices: typing.Set[typing.Any] = set()

        if source is not None:
            vertices.add(source)
        else:
            for vertex in self.__graph.getVertices0():
                vertices.add(vertex)

        expandedVertexList: typing.List[typing.Any] = []
        idx = 0

        while vertices:
            v = next(iter(vertices))  # Get an arbitrary element from the set
            self.__searchRecursive(
                self.__graph, v, expandedVertexList, visitedVertices, True
            )
            vertices.difference_update(
                expandedVertexList[idx:]
            )  # Remove processed vertices
            idx = len(expandedVertexList)

        return expandedVertexList
