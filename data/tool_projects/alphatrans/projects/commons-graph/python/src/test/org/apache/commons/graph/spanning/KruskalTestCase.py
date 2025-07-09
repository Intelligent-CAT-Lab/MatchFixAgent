from __future__ import annotations
import time
import re
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
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class KruskalTestCase(unittest.TestCase):

    def testVerifyWikipediaMinimumSpanningTree_test15_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)
        input_graph.addVertex(g)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 9.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        # Compute the actual spanning tree using Kruskal's algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testVerifyWikipediaMinimumSpanningTree_test14_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)
        input_graph.addVertex(g)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input_graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input_graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 9.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Add assertions here to compare `expected` and `actual` if needed

    def testVerifyWikipediaMinimumSpanningTree_test13_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 8.0), c)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> d", 9.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 15.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 8.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 9.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        minimum_spanning_tree = CommonsGraph.minimumSpanningTree(input_graph)
        minimum_spanning_tree.where_edges_have_weights(BaseWeightedEdge[float]())
        minimum_spanning_tree.where_edges_have_weights(
            BaseWeightedEdge[float]()
        ).from_arbitrary_source()

    def testVerifyWikipediaMinimumSpanningTree_test12_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 9.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        result = CommonsGraph.minimumSpanningTree(input_graph)
        result.where_edges_have_weights(BaseWeightedEdge[float]())

    def testVerifyWikipediaMinimumSpanningTree_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 8.0), c)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> d", 9.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 15.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 8.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 9.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyWikipediaMinimumSpanningTree_test10_decomposed(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        input.add_vertex(a)
        input.add_vertex(b)
        input.add_vertex(c)
        input.add_vertex(d)
        input.add_vertex(e)
        input.add_vertex(f)
        input.add_vertex(g)
        input.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input.get_vertices():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 9.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

    def testVerifyWikipediaMinimumSpanningTree_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

    def testVerifyWikipediaMinimumSpanningTree_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 8.0), c)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> d", 9.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 15.0), e)
        input_graph.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 8.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 11.0), g)

    def testVerifyWikipediaMinimumSpanningTree_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

    def testVerifyWikipediaMinimumSpanningTree_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

    def testVerifyWikipediaMinimumSpanningTree_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")

    def testVerifyWikipediaMinimumSpanningTree_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")

    def testVerifyWikipediaMinimumSpanningTree_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testVerifyWikipediaMinimumSpanningTree_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testVerifyWikipediaMinimumSpanningTree_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testVerifyWikipediaMinimumSpanningTree_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")

    def testVerifyNotConnectedMinimumSpanningTree_test12_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Generate the actual spanning tree using Kruskal's algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testVerifyNotConnectedMinimumSpanningTree_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add an edge between vertices
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add the same edge to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Perform the minimum spanning tree operation
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assertions can be added here to compare `expected` and `actual` if needed

    def testVerifyNotConnectedMinimumSpanningTree_test10_decomposed(self) -> None:
        # Create an undirected mutable graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add an edge between vertices 'a' and 'b'
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Create an expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add the same edge to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        # Perform the minimum spanning tree operation
        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).fromArbitrarySource()

    def testVerifyNotConnectedMinimumSpanningTree_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyNotConnectedMinimumSpanningTree_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testVerifyNotConnectedMinimumSpanningTree_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices0():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

    def testVerifyNotConnectedMinimumSpanningTree_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

    def testVerifyNotConnectedMinimumSpanningTree_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)

    def testVerifyNotConnectedMinimumSpanningTree_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

    def testVerifyNotConnectedMinimumSpanningTree_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testVerifyNotConnectedMinimumSpanningTree_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testVerifyNotConnectedMinimumSpanningTree_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testVerifyNotConnectedMinimumSpanningTree_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")

    @pytest.mark.skip(reason="Ignore")
    def testP4UniformWeightsMinimumSpanningTree_test0_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 1.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 1.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 1.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 1.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 1.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 1.0), d)

        # Compute the actual spanning tree using Kruskal's algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testP4NonUniformWeightsMinimumSpanningTree_test12_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

        # Compute the actual spanning tree using Kruskal's algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testP4NonUniformWeightsMinimumSpanningTree_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Compute the actual minimum spanning tree
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assertions can be added here to compare `expected` and `actual`

    def testP4NonUniformWeightsMinimumSpanningTree_test10_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add edges with weights to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Perform the minimum spanning tree operation
        mst = CommonsGraph.minimumSpanningTree(input_graph)
        mst.whereEdgesHaveWeights(BaseWeightedEdge[float]())
        mst.whereEdgesHaveWeights(BaseWeightedEdge[float]()).fromArbitrarySource()

    def testP4NonUniformWeightsMinimumSpanningTree_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Perform the minimum spanning tree operation
        result = CommonsGraph.minimumSpanningTree(input_graph)
        result.whereEdgesHaveWeights(BaseWeightedEdge[float]())

    def testP4NonUniformWeightsMinimumSpanningTree_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        # Create vertices
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        # Add vertices to the graph
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        # Add edges to the graph
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        # Add vertices to the expected spanning tree
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        # Add edges to the expected spanning tree
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Call the minimum spanning tree function
        CommonsGraph.minimumSpanningTree(input_graph)

    def testP4NonUniformWeightsMinimumSpanningTree_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

    def testP4NonUniformWeightsMinimumSpanningTree_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

    def testP4NonUniformWeightsMinimumSpanningTree_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        input_graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

    def testP4NonUniformWeightsMinimumSpanningTree_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

    def testP4NonUniformWeightsMinimumSpanningTree_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testP4NonUniformWeightsMinimumSpanningTree_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testP4NonUniformWeightsMinimumSpanningTree_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testP4NonUniformWeightsMinimumSpanningTree_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")

    def testNullVertex_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(None)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(None).applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    def testNullVertex_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(None)

    def testNullVertex_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullVertex_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)

    def testNullMonoid_test4_decomposed(self) -> None:
        input_graph = None
        a = None
        try:
            input_graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("A")
            input_graph.addVertex(a)
        except RuntimeError as e:
            pytest.fail(e.getMessage())

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(a)

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(a).applyingKruskalAlgorithm(None)

    def testNullMonoid_test3_decomposed(self) -> None:
        input_graph = None
        vertex_a = None
        try:
            input_graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            vertex_a = BaseLabeledVertex("A")
            input_graph.addVertex(vertex_a)
        except RuntimeError as e:
            pytest.fail(e.getMessage())

        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).fromSource(vertex_a)

    def testNullMonoid_test2_decomposed(self) -> None:
        input_graph = None
        a = None
        try:
            input_graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("A")
            input_graph.addVertex(a)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullMonoid_test1_decomposed(self) -> None:
        input_graph = None
        vertex_a = None
        try:
            input_graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            vertex_a = BaseLabeledVertex("A")
            input_graph.addVertex(vertex_a)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.minimumSpanningTree(input_graph)

    def testNullMonoid_test0_decomposed(self) -> None:
        input_graph = None
        a = None
        try:
            input_graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("A")
            input_graph.addVertex(a)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

    def testNullGraph_test3_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource()
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource().applyingKruskalAlgorithm(
                DoubleWeightBaseOperations()
            )

    def testNullGraph_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource()

    def testNullGraph_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )

    def testNullGraph_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)

    def testNotExistVertex_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(BaseLabeledVertex("NOT EXIST"))

    def testNotExistVertex_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNotExistVertex_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.minimumSpanningTree(input_graph)

    def testEmptyGraph_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource()
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource().applyingKruskalAlgorithm(
                DoubleWeightBaseOperations()
            )

    def testEmptyGraph_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromArbitrarySource()

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

    def testDisconnectedMinimumSpanningTree_test12_decomposed(self) -> None:
        # Create the input graph
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Create the expected spanning tree
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        # Compute the actual spanning tree using Kruskal's algorithm
        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assert that the expected and actual spanning trees are equal
        self.assertEqual(expected, actual)

    def testDisconnectedMinimumSpanningTree_test11_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input_graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        # Assertions can be added here to compare `expected` and `actual`

    def testDisconnectedMinimumSpanningTree_test10_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).fromArbitrarySource()

    def testDisconnectedMinimumSpanningTree_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        minimumSpanningTree(input_graph)
        minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testDisconnectedMinimumSpanningTree_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

        input_graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        CommonsGraph.minimumSpanningTree(input_graph)

    def testDisconnectedMinimumSpanningTree_test7_decomposed(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

    def testDisconnectedMinimumSpanningTree_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 4.0), b)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

    def testDisconnectedMinimumSpanningTree_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)

        input_graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        input_graph.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

    def testDisconnectedMinimumSpanningTree_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)

    def testDisconnectedMinimumSpanningTree_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testDisconnectedMinimumSpanningTree_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testDisconnectedMinimumSpanningTree_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testDisconnectedMinimumSpanningTree_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
