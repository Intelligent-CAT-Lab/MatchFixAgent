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
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.test.org.apache.commons.graph.visit.NodeSequenceVisitor import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class VisitTestCase(unittest.TestCase):

    def testVerifyDepthFirstSearch_test4_decomposed(self) -> None:
        expected = [
            BaseLabeledVertex("S"),
            BaseLabeledVertex("B"),
            BaseLabeledVertex("F"),
            BaseLabeledVertex("E"),
            BaseLabeledVertex("G"),
            BaseLabeledVertex("H"),
            BaseLabeledVertex("A"),
            BaseLabeledVertex("D"),
            BaseLabeledVertex("C"),
        ]

        def connect0():
            a = graph.addVertex(BaseLabeledVertex("A"))
            b = graph.addVertex(BaseLabeledVertex("B"))
            c = graph.addVertex(BaseLabeledVertex("C"))
            d = graph.addVertex(BaseLabeledVertex("D"))
            e = graph.addVertex(BaseLabeledVertex("E"))
            f = graph.addVertex(BaseLabeledVertex("F"))
            g = graph.addVertex(BaseLabeledVertex("G"))
            h = graph.addVertex(BaseLabeledVertex("H"))
            s = graph.addVertex(BaseLabeledVertex("S"))

            graph.addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a)
            graph.addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b)

            graph.addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c)
            graph.addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d)

            graph.addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e)
            graph.addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f)

            graph.addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h)
            graph.addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )
        CommonsGraph.visit(graph)
        CommonsGraph.visit(graph).from_(BaseLabeledVertex("S"))
        actual = (
            CommonsGraph.visit(graph)
            .from_(BaseLabeledVertex("S"))
            .applyingDepthFirstSearch1(NodeSequenceVisitor())
        )

        self.assertEqual(expected, actual)

    def testVerifyDepthFirstSearch_test3_decomposed(self) -> None:
        expected = []

        def connect0():
            a = addVertex(BaseLabeledVertex("A"))
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            g = addVertex(BaseLabeledVertex("G"))
            h = addVertex(BaseLabeledVertex("H"))
            s = addVertex(BaseLabeledVertex("S"))

            addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a)
            addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b)

            addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c)
            addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d)

            addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e)
            addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f)

            addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h)
            addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g)

            expected.extend([s, b, f, e, g, h, a, d, c])

        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.visit(input_graph)
        CommonsGraph.visit(input_graph).from_(BaseLabeledVertex("S"))
        actual = (
            CommonsGraph.visit(input_graph)
            .from_(BaseLabeledVertex("S"))
            .applyingDepthFirstSearch1(NodeSequenceVisitor())
        )

        self.assertEqual(expected, actual)

    def testVerifyDepthFirstSearch_test2_decomposed(self) -> None:
        expected = []

        def connect0():
            a = input.add_vertex(BaseLabeledVertex("A"))
            b = input.add_vertex(BaseLabeledVertex("B"))
            c = input.add_vertex(BaseLabeledVertex("C"))
            d = input.add_vertex(BaseLabeledVertex("D"))
            e = input.add_vertex(BaseLabeledVertex("E"))
            f = input.add_vertex(BaseLabeledVertex("F"))
            g = input.add_vertex(BaseLabeledVertex("G"))
            h = input.add_vertex(BaseLabeledVertex("H"))
            s = input.add_vertex(BaseLabeledVertex("S"))

            input.add_edge(BaseLabeledEdge("S <-> A")).from_vertex(s).to_vertex(a)
            input.add_edge(BaseLabeledEdge("S <-> B")).from_vertex(s).to_vertex(b)

            input.add_edge(BaseLabeledEdge("A <-> C")).from_vertex(a).to_vertex(c)
            input.add_edge(BaseLabeledEdge("A <-> D")).from_vertex(a).to_vertex(d)

            input.add_edge(BaseLabeledEdge("B <-> E")).from_vertex(b).to_vertex(e)
            input.add_edge(BaseLabeledEdge("B <-> F")).from_vertex(b).to_vertex(f)

            input.add_edge(BaseLabeledEdge("E <-> H")).from_vertex(e).to_vertex(h)
            input.add_edge(BaseLabeledEdge("E <-> G")).from_vertex(e).to_vertex(g)

            expected.extend([s, b, f, e, g, h, a, d, c])

        input = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )
        CommonsGraph.visit(input)
        CommonsGraph.visit(input).from_vertex(BaseLabeledVertex("S"))

    def testVerifyDepthFirstSearch_test1_decomposed(self) -> None:
        expected = []

        def connect0():
            a = addVertex(BaseLabeledVertex("A"))
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            g = addVertex(BaseLabeledVertex("G"))
            h = addVertex(BaseLabeledVertex("H"))
            s = addVertex(BaseLabeledVertex("S"))

            addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a)
            addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b)

            addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c)
            addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d)

            addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e)
            addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f)

            addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h)
            addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g)

            expected.extend([s, b, f, e, g, h, a, d, c])

        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.visit(input_graph)

    def testVerifyDepthFirstSearch_test0_decomposed(self) -> None:
        expected = []

        def connect0():
            a = addVertex(BaseLabeledVertex("A"))
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            g = addVertex(BaseLabeledVertex("G"))
            h = addVertex(BaseLabeledVertex("H"))
            s = addVertex(BaseLabeledVertex("S"))

            addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a)
            addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b)

            addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c)
            addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d)

            addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e)
            addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f)

            addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h)
            addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g)

            expected.extend([s, b, f, e, g, h, a, d, c])

        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

    def testVerifyBreadthFirstSearch_test4_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    r := BaseLabeledVertex("r"),
                    s := BaseLabeledVertex("s"),
                    t := BaseLabeledVertex("t"),
                    u := BaseLabeledVertex("u"),
                    v := BaseLabeledVertex("v"),
                    w := BaseLabeledVertex("w"),
                    x := BaseLabeledVertex("x"),
                    y := BaseLabeledVertex("y"),
                    addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    addEdge(BaseLabeledEdge("t <-> x")).from_(t).to(x),
                    addEdge(BaseLabeledEdge("y <-> u")).from_(y).to(u),
                    addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        expected_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    r := BaseLabeledVertex("r"),
                    s := BaseLabeledVertex("s"),
                    t := BaseLabeledVertex("t"),
                    u := BaseLabeledVertex("u"),
                    v := BaseLabeledVertex("v"),
                    w := BaseLabeledVertex("w"),
                    x := BaseLabeledVertex("x"),
                    y := BaseLabeledVertex("y"),
                    addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        actual_graph = (
            CommonsGraph.visit(input_graph)
            .from_(BaseLabeledVertex("s"))
            .applyingBreadthFirstSearch0()
        )

        self.assertEqual(expected_graph, actual_graph)

    def testVerifyBreadthFirstSearch_test3_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    r := self.addVertex(BaseLabeledVertex("r")),
                    s := self.addVertex(BaseLabeledVertex("s")),
                    t := self.addVertex(BaseLabeledVertex("t")),
                    u := self.addVertex(BaseLabeledVertex("u")),
                    v := self.addVertex(BaseLabeledVertex("v")),
                    w := self.addVertex(BaseLabeledVertex("w")),
                    x := self.addVertex(BaseLabeledVertex("x")),
                    y := self.addVertex(BaseLabeledVertex("y")),
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    self.addEdge(BaseLabeledEdge("t <-> x")).from_(t).to(x),
                    self.addEdge(BaseLabeledEdge("y <-> u")).from_(y).to(u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        expected_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    r := self.addVertex(BaseLabeledVertex("r")),
                    s := self.addVertex(BaseLabeledVertex("s")),
                    t := self.addVertex(BaseLabeledVertex("t")),
                    u := self.addVertex(BaseLabeledVertex("u")),
                    v := self.addVertex(BaseLabeledVertex("v")),
                    w := self.addVertex(BaseLabeledVertex("w")),
                    x := self.addVertex(BaseLabeledVertex("x")),
                    y := self.addVertex(BaseLabeledVertex("y")),
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        CommonsGraph.visit(input_graph)
        CommonsGraph.visit(input_graph).from_(BaseLabeledVertex("s"))
        actual_graph = (
            CommonsGraph.visit(input_graph)
            .from_(BaseLabeledVertex("s"))
            .applyingBreadthFirstSearch0()
        )

        # Assertions or further processing can be added here as needed

    def testVerifyBreadthFirstSearch_test2_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    # Add vertices
                    r := BaseLabeledVertex("r"),
                    s := BaseLabeledVertex("s"),
                    t := BaseLabeledVertex("t"),
                    u := BaseLabeledVertex("u"),
                    v := BaseLabeledVertex("v"),
                    w := BaseLabeledVertex("w"),
                    x := BaseLabeledVertex("x"),
                    y := BaseLabeledVertex("y"),
                    # Add edges
                    addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    addEdge(BaseLabeledEdge("t <-> x")).from_(t).to(x),
                    addEdge(BaseLabeledEdge("y <-> u")).from_(y).to(u),
                    addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        expected_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    # Add vertices
                    r := BaseLabeledVertex("r"),
                    s := BaseLabeledVertex("s"),
                    t := BaseLabeledVertex("t"),
                    u := BaseLabeledVertex("u"),
                    v := BaseLabeledVertex("v"),
                    w := BaseLabeledVertex("w"),
                    x := BaseLabeledVertex("x"),
                    y := BaseLabeledVertex("y"),
                    # Add edges
                    addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        # Perform the visit
        CommonsGraph.visit(input_graph)
        CommonsGraph.visit(input_graph).from_(BaseLabeledVertex("s"))

    def testVerifyBreadthFirstSearch_test1_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    # Add vertices
                    r := self.addVertex(BaseLabeledVertex("r")),
                    s := self.addVertex(BaseLabeledVertex("s")),
                    t := self.addVertex(BaseLabeledVertex("t")),
                    u := self.addVertex(BaseLabeledVertex("u")),
                    v := self.addVertex(BaseLabeledVertex("v")),
                    w := self.addVertex(BaseLabeledVertex("w")),
                    x := self.addVertex(BaseLabeledVertex("x")),
                    y := self.addVertex(BaseLabeledVertex("y")),
                    # Add edges
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    self.addEdge(BaseLabeledEdge("t <-> x")).from_(t).to(x),
                    self.addEdge(BaseLabeledEdge("y <-> u")).from_(y).to(u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        expected_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    # Add vertices
                    r := self.addVertex(BaseLabeledVertex("r")),
                    s := self.addVertex(BaseLabeledVertex("s")),
                    t := self.addVertex(BaseLabeledVertex("t")),
                    u := self.addVertex(BaseLabeledVertex("u")),
                    v := self.addVertex(BaseLabeledVertex("v")),
                    w := self.addVertex(BaseLabeledVertex("w")),
                    x := self.addVertex(BaseLabeledVertex("x")),
                    y := self.addVertex(BaseLabeledVertex("y")),
                    # Add edges
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y),
                ]
            )
        )

        CommonsGraph.visit(input_graph)

    def testVerifyBreadthFirstSearch_test0_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    self.addVertex(BaseLabeledVertex("r")),
                    self.addVertex(BaseLabeledVertex("s")),
                    self.addVertex(BaseLabeledVertex("t")),
                    self.addVertex(BaseLabeledVertex("u")),
                    self.addVertex(BaseLabeledVertex("v")),
                    self.addVertex(BaseLabeledVertex("w")),
                    self.addVertex(BaseLabeledVertex("x")),
                    self.addVertex(BaseLabeledVertex("y")),
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(self.s).to(self.r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(self.s).to(self.w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(self.r).to(self.v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(self.w).to(self.t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(self.w).to(self.x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(self.t).to(self.u),
                    self.addEdge(BaseLabeledEdge("t <-> x")).from_(self.t).to(self.x),
                    self.addEdge(BaseLabeledEdge("y <-> u")).from_(self.y).to(self.u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(self.x).to(self.y),
                ]
            )
        )

        expected_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    self.addVertex(BaseLabeledVertex("r")),
                    self.addVertex(BaseLabeledVertex("s")),
                    self.addVertex(BaseLabeledVertex("t")),
                    self.addVertex(BaseLabeledVertex("u")),
                    self.addVertex(BaseLabeledVertex("v")),
                    self.addVertex(BaseLabeledVertex("w")),
                    self.addVertex(BaseLabeledVertex("x")),
                    self.addVertex(BaseLabeledVertex("y")),
                    self.addEdge(BaseLabeledEdge("s <-> r")).from_(self.s).to(self.r),
                    self.addEdge(BaseLabeledEdge("s <-> w")).from_(self.s).to(self.w),
                    self.addEdge(BaseLabeledEdge("r <-> v")).from_(self.r).to(self.v),
                    self.addEdge(BaseLabeledEdge("w <-> t")).from_(self.w).to(self.t),
                    self.addEdge(BaseLabeledEdge("w <-> x")).from_(self.w).to(self.x),
                    self.addEdge(BaseLabeledEdge("t <-> u")).from_(self.t).to(self.u),
                    self.addEdge(BaseLabeledEdge("x <-> y")).from_(self.x).to(self.y),
                ]
            )
        )

    def testNotExistVertex_test2_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]()
        )
        with self.assertRaises(RuntimeError):
            CommonsGraph.visit(input_graph).from_(BaseLabeledVertex("NOT EXIST"))

    def testNotExistVertex_test1_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: None
            )
        )
        CommonsGraph.visit(input_graph)

    def testNotExistVertex_test0_decomposed(self) -> None:
        input_graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: None
            )
        )
