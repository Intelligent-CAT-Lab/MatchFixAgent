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


class PrimTestCase(unittest.TestCase):

    def testVerifyWikipediaMinimumSpanningTree_test11_decomposed(self) -> None:
        input_ = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        input_.add_vertex(a)
        input_.add_vertex(b)
        input_.add_vertex(c)
        input_.add_vertex(d)
        input_.add_vertex(e)
        input_.add_vertex(f)
        input_.add_vertex(g)
        input_.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input_.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input_.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input_.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input_.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input_.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input_.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input_.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input_.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_.get_vertices0():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        self.__internalPrimAssertion(input_, d, expected)

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
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

    def testVerifyWikipediaMinimumSpanningTree_test9_decomposed(self) -> None:
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
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)
        input.addVertex(g)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        input.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        input.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)

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
        input_graph.addVertex(a)
        input_graph.addVertex(b)
        input_graph.addVertex(c)
        input_graph.addVertex(d)
        input_graph.addVertex(e)
        input_graph.addVertex(f)
        input_graph.addVertex(g)

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

    def testVerifyMinimumSpanningTree2_test11_decomposed(self) -> None:
        input_ = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")
        input_.add_vertex(a)
        input_.add_vertex(b)
        input_.add_vertex(c)
        input_.add_vertex(d)
        input_.add_vertex(e)
        input_.add_vertex(f)
        input_.add_vertex(g)
        input_.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        input_.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 30.0), d)
        input_.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        input_.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        input_.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        input_.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        for vertex in input_.get_vertices0():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        expected.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        self.__internalPrimAssertion(input_, a, expected)

    def testVerifyMinimumSpanningTree2_test10_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 30.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        expected.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

    def testVerifyMinimumSpanningTree2_test9_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 30.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input_graph.get_vertices():
            expected.add_vertex(vertex)

    def testVerifyMinimumSpanningTree2_test8_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        input_graph.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> d", 30.0), d)
        input_graph.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        input_graph.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        input_graph.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)
        input_graph.add_edge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

    def testVerifyMinimumSpanningTree2_test7_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input_graph.add_vertex(a)
        input_graph.add_vertex(b)
        input_graph.add_vertex(c)
        input_graph.add_vertex(d)
        input_graph.add_vertex(e)
        input_graph.add_vertex(f)
        input_graph.add_vertex(g)

    def testVerifyMinimumSpanningTree2_test6_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

    def testVerifyMinimumSpanningTree2_test5_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

    def testVerifyMinimumSpanningTree2_test4_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

    def testVerifyMinimumSpanningTree2_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")

    def testVerifyMinimumSpanningTree2_test2_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyMinimumSpanningTree2_test1_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyMinimumSpanningTree2_test0_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testNullVertex_test3_decomposed(self) -> None:
        input_graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph)

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).fromSource(None).applyingPrimAlgorithm(DoubleWeightBaseOperations())

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
            ).fromSource(a).applyingBoruvkaAlgorithm(None)

    def testNullMonoid_test3_decomposed(self) -> None:
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

        CommonsGraph.minimumSpanningTree(input_graph)
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.minimumSpanningTree(input_graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).fromSource(a)

    def testNullMonoid_test2_decomposed(self) -> None:
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

    def testNullMonoid_test1_decomposed(self) -> None:
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
                BaseWeightedEdge()
            )
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource()
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

    def testNullGraph_test2_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None)
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource()

    def testNullGraph_test1_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
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
            ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

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

    @staticmethod
    def __internalPrimAssertion(
        input_: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ],
        source: BaseLabeledVertex,
        expected: MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ],
    ) -> None:

        pass  # LLM could not translate this method
