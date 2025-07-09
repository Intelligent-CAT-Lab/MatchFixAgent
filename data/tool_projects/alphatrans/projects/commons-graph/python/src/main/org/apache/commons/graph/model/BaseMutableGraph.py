from __future__ import annotations
import re
import os
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.BaseGraph import *


class BaseMutableGraph(MutableGraph, BaseGraph, ABC):

    __serialVersionUID: int = 1549113549446254183

    def removeVertex(self, v: typing.Any) -> None:
        self._checkGraphCondition(
            v is not None, "Impossible to remove a null Vertex from the Graph"
        )
        self._checkGraphCondition(
            v in self._adjacencyList, f"Vertex '{v}' not present in the Graph"
        )

        for tail in self._adjacencyList[v]:
            self._indexedEdges.pop(VertexPair(v, tail), None)
        self._adjacencyList.pop(v, None)

        self._decorateRemoveVertex(v)

    def removeEdge(self, e: typing.Any) -> None:
        self._checkGraphCondition(
            e is not None, "Impossible to remove a null Edge from the Graph", []
        )
        self._checkGraphCondition(
            self.containsEdge(e), f"Edge '{e}' not present in the Graph", [e]
        )
        vertex_pair = self.getVertices1(e)
        self._decorateRemoveEdge(e)
        self._internalRemoveEdge(vertex_pair.getHead(), e, vertex_pair.getTail())
        self.getAllEdges().remove(e)

    def _internalRemoveEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        vertex_pair = VertexPair(head, tail)
        self.getIndexedVertices().remove(e)
        self.getIndexedEdges().remove(vertex_pair)
        self.getAdjacencyList()[vertex_pair.head].remove(vertex_pair.tail)

    def _internalAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        self.getAdjacencyList()[head].add(tail)

        vertex_pair = VertexPair(head, tail)
        self.getIndexedEdges()[vertex_pair] = e

        if e not in self.getIndexedVertices():
            self.getIndexedVertices()[e] = vertex_pair

    def addVertex(self, v: typing.Any) -> None:
        self._checkGraphCondition(
            v is not None, "Impossible to add a null Vertex to the Graph", []
        )
        self._checkGraphCondition(
            not self.containsVertex(v),
            f"Vertex '{v}' already present in the Graph",
            [v],
        )

        self.__adjacencyList[v] = set()

        self._decorateAddVertex(v)

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:
        self._checkGraphCondition(head is not None, "Null head Vertex not admitted", [])
        self._checkGraphCondition(
            e is not None, "Impossible to add a null Edge in the Graph", []
        )
        self._checkGraphCondition(tail is not None, "Null tail Vertex not admitted", [])
        self._checkGraphCondition(
            self.containsVertex(head),
            f"Head Vertex '{head}' not present in the Graph",
            [head],
        )
        self._checkGraphCondition(
            self.containsVertex(tail),
            f"Tail Vertex '{tail}' not present in the Graph",
            [tail],
        )
        self._checkGraphCondition(
            self.getEdge(head, tail) is None,
            f"Edge {e} is already present in the Graph",
            [e],
        )

        self.getAllEdges().add(e)

        self._internalAddEdge(head, e, tail)

        self._decorateAddEdge(head, e, tail)

    def _decorateRemoveVertex(self, v: typing.Any) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    def _decorateRemoveEdge(self, e: typing.Any) -> None:
        # Abstract method placeholder
        # Implement this method in a subclass
        pass

    def _decorateAddVertex(self, v: typing.Any) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        # This method is abstract in Java, so it should remain unimplemented here.
        # You can raise a NotImplementedError to indicate it must be overridden in subclasses.
        raise NotImplementedError("Subclasses must implement this method")
