from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class GraphBuilderTestCase(unittest.TestCase):

    def testVerifyProducedGraphesAreEquals_test10_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        expected.addVertex(start)
        expected.addVertex(a)
        expected.addVertex(b)
        expected.addVertex(c)
        expected.addVertex(d)
        expected.addVertex(e)
        expected.addVertex(goal)

        expected.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        expected.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]](
                lambda: self._connect_graph()
            )
        )

        self.assertEqual(expected, actual)

    def _connect_graph(self) -> None:
        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))
        e = self.addVertex(BaseLabeledVertex("e"))
        goal = self.addVertex(BaseLabeledVertex("goal"))

        self.addEdge(BaseLabeledWeightedEdge[float]("start <-> a", 1.5)).from_(
            start
        ).to(a)
        self.addEdge(BaseLabeledWeightedEdge[float]("start <-> d", 2.0)).from_(
            start
        ).to(d)
        self.addEdge(BaseLabeledWeightedEdge[float]("a <-> b", 2.0)).from_(a).to(b)
        self.addEdge(BaseLabeledWeightedEdge[float]("b <-> c", 3.0)).from_(b).to(c)
        self.addEdge(BaseLabeledWeightedEdge[float]("c <-> goal", 3.0)).from_(c).to(
            goal
        )
        self.addEdge(BaseLabeledWeightedEdge[float]("d <-> e", 3.0)).from_(d).to(e)
        self.addEdge(BaseLabeledWeightedEdge[float]("e <-> goal", 2.0)).from_(e).to(
            goal
        )

    def testVerifyProducedGraphesAreEquals_test9_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        expected.addVertex(start)
        expected.addVertex(a)
        expected.addVertex(b)
        expected.addVertex(c)
        expected.addVertex(d)
        expected.addVertex(e)
        expected.addVertex(goal)

        expected.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        expected.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]](
                lambda: self._connect_graph()
            )
        )

        self.assertEqual(expected, actual)

    def _connect_graph(self) -> None:
        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))
        e = self.addVertex(BaseLabeledVertex("e"))
        goal = self.addVertex(BaseLabeledVertex("goal"))

        self.addEdge(BaseLabeledWeightedEdge[float]("start <-> a", 1.5)).from_(
            start
        ).to(a)
        self.addEdge(BaseLabeledWeightedEdge[float]("start <-> d", 2.0)).from_(
            start
        ).to(d)
        self.addEdge(BaseLabeledWeightedEdge[float]("a <-> b", 2.0)).from_(a).to(b)
        self.addEdge(BaseLabeledWeightedEdge[float]("b <-> c", 3.0)).from_(b).to(c)
        self.addEdge(BaseLabeledWeightedEdge[float]("c <-> goal", 3.0)).from_(c).to(
            goal
        )
        self.addEdge(BaseLabeledWeightedEdge[float]("d <-> e", 3.0)).from_(d).to(e)
        self.addEdge(BaseLabeledWeightedEdge[float]("e <-> goal", 2.0)).from_(e).to(
            goal
        )

    def testVerifyProducedGraphesAreEquals_test8_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        expected.add_vertex(start)
        expected.add_vertex(a)
        expected.add_vertex(b)
        expected.add_vertex(c)
        expected.add_vertex(d)
        expected.add_vertex(e)
        expected.add_vertex(goal)

        expected.add_edge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        expected.add_edge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        expected.add_edge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        expected.add_edge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        expected.add_edge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        expected.add_edge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

    def testVerifyProducedGraphesAreEquals_test7_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")
        expected.add_vertex(start)
        expected.add_vertex(a)
        expected.add_vertex(b)
        expected.add_vertex(c)
        expected.add_vertex(d)
        expected.add_vertex(e)
        expected.add_vertex(goal)

    def testVerifyProducedGraphesAreEquals_test6_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

    def testVerifyProducedGraphesAreEquals_test5_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

    def testVerifyProducedGraphesAreEquals_test4_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")

    def testVerifyProducedGraphesAreEquals_test3_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyProducedGraphesAreEquals_test2_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyProducedGraphesAreEquals_test1_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")

    def testVerifyProducedGraphesAreEquals_test0_decomposed(self) -> None:
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
