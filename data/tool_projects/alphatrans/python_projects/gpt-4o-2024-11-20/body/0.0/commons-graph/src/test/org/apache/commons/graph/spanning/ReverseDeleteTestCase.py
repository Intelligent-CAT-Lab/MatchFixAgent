from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class ReverseDeleteTestCase(unittest.TestCase):

    def testVerifyNotConnectGraph3_test13_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)
        expected.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        # Compute the actual spanning tree using the reverse-delete algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph3_test12_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)
        expected.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

    def testVerifyNotConnectGraph3_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)
        expected.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        # Perform the minimum spanning tree operation
        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyNotConnectGraph3_test10_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 7.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 21.0), f)
        input_graph.add_edge(f, BaseLabeledWeightedEdge("f <-> d", 4.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        expected.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)
        expected.add_edge(f, BaseLabeledWeightedEdge("f <-> d", 4.0), d)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyNotConnectGraph3_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)
        expected.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

    def testVerifyNotConnectGraph3_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

    def testVerifyNotConnectGraph3_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 7.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 21.0), f)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> d", 4.0), d)

    def testVerifyNotConnectGraph3_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)

    def testVerifyNotConnectGraph3_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

    def testVerifyNotConnectGraph3_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

    def testVerifyNotConnectGraph3_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")

    def testVerifyNotConnectGraph3_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyNotConnectGraph3_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyNotConnectGraph3_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testVerifyNotConnectGraph2_test12_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)

        # Compute the actual spanning tree using the reverse-delete algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph2_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

    def testVerifyNotConnectGraph2_test10_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyNotConnectGraph2_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyNotConnectGraph2_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

    def testVerifyNotConnectGraph2_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

    def testVerifyNotConnectGraph2_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 4.0), e)

    def testVerifyNotConnectGraph2_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)

    def testVerifyNotConnectGraph2_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

    def testVerifyNotConnectGraph2_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")

    def testVerifyNotConnectGraph2_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyNotConnectGraph2_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyNotConnectGraph2_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testVerifyNotConnectGraph_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        actual = (
            minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

    def testVerifyNotConnectGraph_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyNotConnectGraph_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyNotConnectGraph_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

    def testVerifyNotConnectGraph_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

    def testVerifyNotConnectGraph_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyNotConnectGraph_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyNotConnectGraph_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testVerifyMinimumSpanningTree_test10_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        # Compute the actual spanning tree using the reverse-delete algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testVerifyMinimumSpanningTree_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

    def testVerifyMinimumSpanningTree_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyMinimumSpanningTree_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyMinimumSpanningTree_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

    def testVerifyMinimumSpanningTree_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

    def testVerifyMinimumSpanningTree_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> a", 4.0), a)

    def testVerifyMinimumSpanningTree_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)

    def testVerifyMinimumSpanningTree_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyMinimumSpanningTree_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyMinimumSpanningTree_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testNullMonoid_test2_decomposed(self) -> None:
        input_graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).applyingReverseDeleteAlgorithm(None)

    def testNullMonoid_test1_decomposed(self) -> None:
        input_graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )

    def testNullMonoid_test0_decomposed(self) -> None:
        input_graph = None
        with self.assertRaises(
            TypeError
        ):  # Python raises TypeError for NoneType operations
            CommonsGraph.minimumSpanningTree(input_graph)

    def testNullGraph_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())

    def testNullGraph_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )

    def testNullGraph_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)

    def testEmptyGraph_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        tree = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(0, tree.getOrder())
        self.assertEqual(0, tree.getSize())

    def testEmptyGraph_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        tree = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(0, tree.getOrder())

    def testEmptyGraph_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        tree = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

    def testEmptyGraph_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testEmptyGraph_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)
