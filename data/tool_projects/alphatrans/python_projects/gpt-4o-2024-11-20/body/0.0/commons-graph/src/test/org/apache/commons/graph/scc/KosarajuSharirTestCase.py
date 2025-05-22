from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class KosarajuSharirTestCase(unittest.TestCase):

    def testVerifyHasStronglyConnectedComponents_test27_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = {
            {a, b, d},
            {e, f},
            {g, h, c},
        }

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, actual)

        actual_a = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actual_a)
        self.assertEqual({a, b, d}, actual_a)

        actual_e = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actual_e)
        self.assertEqual({e, f}, actual_e)

        actual_g = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actual_g)
        self.assertEqual({g, h, c}, actual_g)

    def testVerifyHasStronglyConnectedComponents_test26_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actualG)

    def testVerifyHasStronglyConnectedComponents_test25_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> F")).from_vertex(a).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("D -> G")).from_vertex(d).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actual_a = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actual_a)
        self.assertEqual(scc1, set(actual_a))

        actual_e = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actual_e)
        self.assertEqual(scc2, set(actual_e))

        actual_g = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actual_g)
        self.assertEqual(scc3, set(actual_g))

    def testVerifyHasStronglyConnectedComponents_test24_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(connect0)

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

    def testVerifyHasStronglyConnectedComponents_test23_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actual_a = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actual_a)
        self.assertEqual(scc1, set(actual_a))

        actual_e = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actual_e)

    def testVerifyHasStronglyConnectedComponents_test22_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    graph.addVertex(a),
                    graph.addVertex(b),
                    graph.addVertex(c),
                    graph.addVertex(d),
                    graph.addVertex(e),
                    graph.addVertex(f),
                    graph.addVertex(g),
                    graph.addVertex(h),
                    graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = {
            {a, b, d},
            {e, f},
            {g, h, c},
        }

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, actual)

        actual_a = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actual_a)
        self.assertEqual({a, b, d}, actual_a)

        actual_e = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actual_e)
        self.assertEqual({e, f}, actual_e)

    def testVerifyHasStronglyConnectedComponents_test21_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

    def testVerifyHasStronglyConnectedComponents_test20_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.add_edge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.add_edge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)

    def testVerifyHasStronglyConnectedComponents_test19_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)

    def testVerifyHasStronglyConnectedComponents_test18_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.add_edge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.add_edge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()

        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

    def testVerifyHasStronglyConnectedComponents_test17_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)

    def testVerifyHasStronglyConnectedComponents_test16_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()

        self.assertEqual(expected, actual)

    def testVerifyHasStronglyConnectedComponents_test15_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        CommonsGraph.findStronglyConnectedComponent(graph)

    def testVerifyHasStronglyConnectedComponents_test14_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        # Add assertions or further processing as needed

    def testVerifyHasStronglyConnectedComponents_test13_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        # Here you would add assertions to verify the strongly connected components
        # For example:
        # actual = some_function_to_get_scc(graph)
        # self.assertEqual(expected, actual)

    def testVerifyHasStronglyConnectedComponents_test12_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> F")).from_vertex(a).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("D -> G")).from_vertex(d).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

    def testVerifyHasStronglyConnectedComponents_test11_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))

    def testVerifyHasStronglyConnectedComponents_test10_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> F")).from_vertex(a).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("D -> G")).from_vertex(d).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

    def testVerifyHasStronglyConnectedComponents_test9_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

    def testVerifyHasStronglyConnectedComponents_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

    def testVerifyHasStronglyConnectedComponents_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

    def testVerifyHasStronglyConnectedComponents_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

    def testVerifyHasStronglyConnectedComponents_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")

    def testVerifyHasStronglyConnectedComponents_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")

    def testVerifyHasStronglyConnectedComponents_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testVerifyHasStronglyConnectedComponents_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testVerifyHasStronglyConnectedComponents_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testVerifyHasStronglyConnectedComponents_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testUnconnectedGraph_test27_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actualG)
        self.assertEqual(scc3, set(actualG))

    def testUnconnectedGraph_test26_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actualG)

    def testUnconnectedGraph_test25_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)
        self.assertFalse(not actualG)
        self.assertEqual(scc3, set(actualG))

    def testUnconnectedGraph_test24_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, set(actualE))

    def testUnconnectedGraph_test23_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)

    def testUnconnectedGraph_test22_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        scc2 = {e, f}
        scc3 = {g, h, c}
        expected.add(frozenset(scc1))
        expected.add(frozenset(scc2))
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, actualA)

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)
        self.assertFalse(not actualE)
        self.assertEqual(scc2, actualE)

    def testUnconnectedGraph_test21_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)
        self.assertEqual(scc1, set(actualA))

    def testUnconnectedGraph_test20_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(b),
                    self.addVertex(c),
                    self.addVertex(d),
                    self.addVertex(e),
                    self.addVertex(f),
                    self.addVertex(g),
                    self.addVertex(h),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)
        self.assertFalse(not actualA)

    def testUnconnectedGraph_test19_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)

    def testUnconnectedGraph_test18_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        scc2 = {e, f}
        scc3 = {g, h, c}
        expected.add(frozenset(scc1))
        expected.add(frozenset(scc2))
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()

        self.assertFalse(not actual)
        self.assertEqual(expected, set(frozenset(scc) for scc in actual))

    def testUnconnectedGraph_test17_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    graph.addVertex(a),
                    graph.addVertex(b),
                    graph.addVertex(c),
                    graph.addVertex(d),
                    graph.addVertex(e),
                    graph.addVertex(f),
                    graph.addVertex(g),
                    graph.addVertex(h),
                    graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()
        self.assertFalse(not actual)

    def testUnconnectedGraph_test16_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()

        self.assertEqual(expected, actual)

    def testUnconnectedGraph_test15_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(connect0)

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        CommonsGraph.findStronglyConnectedComponent(graph)

    def testUnconnectedGraph_test14_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        # Assertions or further testing logic would go here

    def testUnconnectedGraph_test13_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))
        scc3 = {g, h, c}
        expected.add(frozenset(scc3))

        # Assertions or further processing can be added here

    def testUnconnectedGraph_test12_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()

        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

        scc2 = {e, f}
        expected.add(frozenset(scc2))

        # Assertions or further processing can be added here

    def testUnconnectedGraph_test11_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))
        scc2 = {e, f}
        expected.add(frozenset(scc2))

    def testUnconnectedGraph_test10_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

    def testUnconnectedGraph_test9_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.add_vertex(a)
            graph.add_vertex(b)
            graph.add_vertex(c)
            graph.add_vertex(d)
            graph.add_vertex(e)
            graph.add_vertex(f)
            graph.add_vertex(g)
            graph.add_vertex(h)

            graph.add_edge(BaseLabeledEdge("A -> B")).from_vertex(a).to_vertex(b)
            graph.add_edge(BaseLabeledEdge("B -> D")).from_vertex(b).to_vertex(d)
            graph.add_edge(BaseLabeledEdge("C -> G")).from_vertex(c).to_vertex(g)
            graph.add_edge(BaseLabeledEdge("D -> A")).from_vertex(d).to_vertex(a)
            graph.add_edge(BaseLabeledEdge("E -> C")).from_vertex(e).to_vertex(c)
            graph.add_edge(BaseLabeledEdge("E -> F")).from_vertex(e).to_vertex(f)
            graph.add_edge(BaseLabeledEdge("F -> E")).from_vertex(f).to_vertex(e)
            graph.add_edge(BaseLabeledEdge("G -> H")).from_vertex(g).to_vertex(h)
            graph.add_edge(BaseLabeledEdge("H -> C")).from_vertex(h).to_vertex(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = set()
        scc1 = {a, b, d}
        expected.add(frozenset(scc1))

    def testUnconnectedGraph_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(b)
            graph.addVertex(c)
            graph.addVertex(d)
            graph.addVertex(e)
            graph.addVertex(f)
            graph.addVertex(g)
            graph.addVertex(h)

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
            graph.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
            graph.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

    def testUnconnectedGraph_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

    def testUnconnectedGraph_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

    def testUnconnectedGraph_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")

    def testUnconnectedGraph_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")

    def testUnconnectedGraph_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

    def testUnconnectedGraph_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")

    def testUnconnectedGraph_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")

    def testUnconnectedGraph_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testNullVertices_test1_decomposed(self) -> None:
        a = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(
                a
            )

    def testNullVertices_test0_decomposed(self) -> None:
        a = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findStronglyConnectedComponent(graph)

    def testNullGraph_test1_decomposed(self) -> None:
        graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph)
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir0()

    def testNullGraph_test0_decomposed(self) -> None:
        graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph)

    def testNotExistVertex_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(
                BaseLabeledVertex("NOT EXISTS")
            )

    def testNotExistVertex_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findStronglyConnectedComponent(graph)
