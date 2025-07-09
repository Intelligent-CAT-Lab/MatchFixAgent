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
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class TarjanTestCase(unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def testverifyHasStronglyConnectedComponents_test18_decomposed(self) -> None:
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

        actual = CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

        self.assertFalse(not actual)
        self.assertEqual(expected, {frozenset(scc) for scc in actual})

    def testSparse_test3_decomposed(self) -> None:
        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("A")),
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                    addVertex(BaseLabeledVertex("D")),
                    addVertex(BaseLabeledVertex("E")),
                    addVertex(BaseLabeledVertex("F")),
                ]
            )
        )
        expected = 6
        actual = CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()
        self.assertEqual(len(actual), expected)

    def testSparse_test2_decomposed(self) -> None:
        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("A")),
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                    addVertex(BaseLabeledVertex("D")),
                    addVertex(BaseLabeledVertex("E")),
                    addVertex(BaseLabeledVertex("F")),
                ]
            )
        )
        expected = 6
        CommonsGraph.findStronglyConnectedComponent(graph)
        actual = CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

    def testSparse_test1_decomposed(self) -> None:
        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("A")),
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                    addVertex(BaseLabeledVertex("D")),
                    addVertex(BaseLabeledVertex("E")),
                    addVertex(BaseLabeledVertex("F")),
                ]
            )
        )
        expected = 6
        CommonsGraph.findStronglyConnectedComponent(graph)

    def testSparse_test0_decomposed(self) -> None:
        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[int]](
                connect0=lambda: [
                    graph.addVertex(BaseLabeledVertex("A")),
                    graph.addVertex(BaseLabeledVertex("B")),
                    graph.addVertex(BaseLabeledVertex("C")),
                    graph.addVertex(BaseLabeledVertex("D")),
                    graph.addVertex(BaseLabeledVertex("E")),
                    graph.addVertex(BaseLabeledVertex("F")),
                ]
            )
        )

    def testNullGraph_test1_decomposed(self) -> None:
        graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph)
            CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

    def testNullGraph_test0_decomposed(self) -> None:
        graph = None
        with self.assertRaises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph)

    def testEmptyGraph_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findStronglyConnectedComponent(graph)
        CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

    def testEmptyGraph_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findStronglyConnectedComponent(graph)
