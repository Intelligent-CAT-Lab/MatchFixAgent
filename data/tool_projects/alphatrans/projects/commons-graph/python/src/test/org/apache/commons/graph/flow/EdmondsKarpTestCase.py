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
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *


class EdmondsKarpTestCase(unittest.TestCase):

    def testSparse_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 0

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(g)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )
        self.assertEqual(actual, expected)

    def testSparse_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        graph_connection = AbstractGraphConnection(connect0)
        graph = CommonsGraph.newDirectedMutableGraph(graph_connection)

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(g)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )

    def testSparse_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        self.graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        expected = 0
        CommonsGraph.findMaxFlow(self.graph)
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).from_(a)
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).from_(a).to(g)

    def testSparse_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        self.graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        expected = 0
        CommonsGraph.findMaxFlow(self.graph)
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).from_(a)

    def testSparse_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        self.graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )
        expected = 0
        CommonsGraph.findMaxFlow(self.graph)
        CommonsGraph.findMaxFlow(self.graph).whereEdgesHaveWeights(BaseWeightedEdge())

    def testSparse_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        self.graph = CommonsGraph.newDirectedMutableGraph(connect0)
        expected = 0
        CommonsGraph.findMaxFlow(self.graph)

    def testSparse_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(BaseLabeledVertex("D"))
            self.graph.addVertex(BaseLabeledVertex("E"))
            self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)

        self.graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

    def testSparse_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

    def testSparse_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testNullVertices_test4_decomposed(self) -> None:
        a = None
        g = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a).to(g)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a).to(g).applyingEdmondsKarp(IntegerWeightBaseOperations())

    def testNullVertices_test3_decomposed(self) -> None:
        a = None
        g = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a).to(g)

    def testNullVertices_test2_decomposed(self) -> None:
        a = None
        g = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a)

    def testNullVertices_test1_decomposed(self) -> None:
        a = None
        g = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())

    def testNullVertices_test0_decomposed(self) -> None:
        a = None
        g = None
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findMaxFlow(graph)

    def testNullGraph_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(BaseWeightedEdge())

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(g)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(g).applyingEdmondsKarp(IntegerWeightBaseOperations())

    def testNullGraph_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(a).to(g)

    def testNullGraph_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(BaseWeightedEdge())

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a)

    def testNullGraph_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

    def testNullGraph_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

    def testNullGraph_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

    def testNullGraph_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testFindMaxFlowAndVerify_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            d = self.graph.addVertex(BaseLabeledVertex("D"))
            e = self.graph.addVertex(BaseLabeledVertex("E"))
            f = self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> D", 3)).from_(a).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> A", 3)).from_(c).to(a)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1)).from_(c).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> E", 2)).from_(c).to(e)
            self.graph.addEdge(BaseLabeledWeightedEdge("D -> E", 2)).from_(d).to(e)
            self.graph.addEdge(BaseLabeledWeightedEdge("D -> F", 6)).from_(d).to(f)
            self.graph.addEdge(BaseLabeledWeightedEdge("E -> B", 1)).from_(e).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("E -> G", 1)).from_(e).to(g)
            self.graph.addEdge(BaseLabeledWeightedEdge("F -> G", 9)).from_(f).to(g)

        self.graph = CommonsGraph.newDirectedMutableGraph(connect0)

        expected = 5
        actual = (
            CommonsGraph.findMaxFlow(self.graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testFindMaxFlowAndVerify_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            addVertex(a)
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            addVertex(g)

            addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            addEdge(BaseLabeledWeightedEdge("A -> D", 3)).from_(a).to(d)
            addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)
            addEdge(BaseLabeledWeightedEdge("C -> A", 3)).from_(c).to(a)
            addEdge(BaseLabeledWeightedEdge("C -> D", 1)).from_(c).to(d)
            addEdge(BaseLabeledWeightedEdge("C -> E", 2)).from_(c).to(e)
            addEdge(BaseLabeledWeightedEdge("D -> E", 2)).from_(d).to(e)
            addEdge(BaseLabeledWeightedEdge("D -> F", 6)).from_(d).to(f)
            addEdge(BaseLabeledWeightedEdge("E -> B", 1)).from_(e).to(b)
            addEdge(BaseLabeledWeightedEdge("E -> G", 1)).from_(e).to(g)
            addEdge(BaseLabeledWeightedEdge("F -> G", 9)).from_(f).to(g)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 5

        # Perform the max flow calculations
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(g)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )

        # Assert the expected and actual values
        self.assertEqual(expected, actual)

    def testFindMaxFlowAndVerify_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            addVertex(a)
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            addVertex(g)

            addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            addEdge(BaseLabeledWeightedEdge("A -> D", 3)).from_(a).to(d)
            addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)
            addEdge(BaseLabeledWeightedEdge("C -> A", 3)).from_(c).to(a)
            addEdge(BaseLabeledWeightedEdge("C -> D", 1)).from_(c).to(d)
            addEdge(BaseLabeledWeightedEdge("C -> E", 2)).from_(c).to(e)
            addEdge(BaseLabeledWeightedEdge("D -> E", 2)).from_(d).to(e)
            addEdge(BaseLabeledWeightedEdge("D -> F", 6)).from_(d).to(f)
            addEdge(BaseLabeledWeightedEdge("E -> B", 1)).from_(e).to(b)
            addEdge(BaseLabeledWeightedEdge("E -> G", 1)).from_(e).to(g)
            addEdge(BaseLabeledWeightedEdge("F -> G", 9)).from_(f).to(g)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 5

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(g)

    def testFindMaxFlowAndVerify_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            d = self.graph.addVertex(BaseLabeledVertex("D"))
            e = self.graph.addVertex(BaseLabeledVertex("E"))
            f = self.graph.addVertex(BaseLabeledVertex("F"))
            self.graph.addVertex(g)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 3)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> D", 3)).from_(a).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 4)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> A", 3)).from_(c).to(a)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1)).from_(c).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> E", 2)).from_(c).to(e)
            self.graph.addEdge(BaseLabeledWeightedEdge("D -> E", 2)).from_(d).to(e)
            self.graph.addEdge(BaseLabeledWeightedEdge("D -> F", 6)).from_(d).to(f)
            self.graph.addEdge(BaseLabeledWeightedEdge("E -> B", 1)).from_(e).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("E -> G", 1)).from_(e).to(g)
            self.graph.addEdge(BaseLabeledWeightedEdge("F -> G", 9)).from_(f).to(g)

        self.graph = CommonsGraph.newDirectedMutableGraph(connect0)
        expected = 5

        max_flow_builder = CommonsGraph.findMaxFlow(self.graph)
        max_flow_builder.whereEdgesHaveWeights(BaseWeightedEdge())
        max_flow_builder.whereEdgesHaveWeights(BaseWeightedEdge()).from_(a)

    def testFindMaxFlowAndVerify_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            graph.add_vertex(a)
            b = graph.add_vertex(BaseLabeledVertex("B"))
            c = graph.add_vertex(BaseLabeledVertex("C"))
            d = graph.add_vertex(BaseLabeledVertex("D"))
            e = graph.add_vertex(BaseLabeledVertex("E"))
            f = graph.add_vertex(BaseLabeledVertex("F"))
            graph.add_vertex(g)

            graph.add_edge(BaseLabeledWeightedEdge("A -> B", 3)).from_vertex(
                a
            ).to_vertex(b)
            graph.add_edge(BaseLabeledWeightedEdge("A -> D", 3)).from_vertex(
                a
            ).to_vertex(d)
            graph.add_edge(BaseLabeledWeightedEdge("B -> C", 4)).from_vertex(
                b
            ).to_vertex(c)
            graph.add_edge(BaseLabeledWeightedEdge("C -> A", 3)).from_vertex(
                c
            ).to_vertex(a)
            graph.add_edge(BaseLabeledWeightedEdge("C -> D", 1)).from_vertex(
                c
            ).to_vertex(d)
            graph.add_edge(BaseLabeledWeightedEdge("C -> E", 2)).from_vertex(
                c
            ).to_vertex(e)
            graph.add_edge(BaseLabeledWeightedEdge("D -> E", 2)).from_vertex(
                d
            ).to_vertex(e)
            graph.add_edge(BaseLabeledWeightedEdge("D -> F", 6)).from_vertex(
                d
            ).to_vertex(f)
            graph.add_edge(BaseLabeledWeightedEdge("E -> B", 1)).from_vertex(
                e
            ).to_vertex(b)
            graph.add_edge(BaseLabeledWeightedEdge("E -> G", 1)).from_vertex(
                e
            ).to_vertex(g)
            graph.add_edge(BaseLabeledWeightedEdge("F -> G", 9)).from_vertex(
                f
            ).to_vertex(g)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 5
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).where_edges_have_weights(BaseWeightedEdge())

    def testFindMaxFlowAndVerify_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0():
            self.graph.add_vertex(a)
            b = self.graph.add_vertex(BaseLabeledVertex("B"))
            c = self.graph.add_vertex(BaseLabeledVertex("C"))
            d = self.graph.add_vertex(BaseLabeledVertex("D"))
            e = self.graph.add_vertex(BaseLabeledVertex("E"))
            f = self.graph.add_vertex(BaseLabeledVertex("F"))
            self.graph.add_vertex(g)

            self.graph.add_edge(BaseLabeledWeightedEdge("A -> B", 3)).from_vertex(
                a
            ).to_vertex(b)
            self.graph.add_edge(BaseLabeledWeightedEdge("A -> D", 3)).from_vertex(
                a
            ).to_vertex(d)
            self.graph.add_edge(BaseLabeledWeightedEdge("B -> C", 4)).from_vertex(
                b
            ).to_vertex(c)
            self.graph.add_edge(BaseLabeledWeightedEdge("C -> A", 3)).from_vertex(
                c
            ).to_vertex(a)
            self.graph.add_edge(BaseLabeledWeightedEdge("C -> D", 1)).from_vertex(
                c
            ).to_vertex(d)
            self.graph.add_edge(BaseLabeledWeightedEdge("C -> E", 2)).from_vertex(
                c
            ).to_vertex(e)
            self.graph.add_edge(BaseLabeledWeightedEdge("D -> E", 2)).from_vertex(
                d
            ).to_vertex(e)
            self.graph.add_edge(BaseLabeledWeightedEdge("D -> F", 6)).from_vertex(
                d
            ).to_vertex(f)
            self.graph.add_edge(BaseLabeledWeightedEdge("E -> B", 1)).from_vertex(
                e
            ).to_vertex(b)
            self.graph.add_edge(BaseLabeledWeightedEdge("E -> G", 1)).from_vertex(
                e
            ).to_vertex(g)
            self.graph.add_edge(BaseLabeledWeightedEdge("F -> G", 9)).from_vertex(
                f
            ).to_vertex(g)

        graph = CommonsGraph.newDirectedMutableGraph(connect0)
        expected = 5
        CommonsGraph.findMaxFlow(graph)

    def testFindMaxFlowAndVerify_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        def connect0(
            graph: DirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[int]
            ],
        ) -> None:
            graph.add_vertex(a)
            b = graph.add_vertex(BaseLabeledVertex("B"))
            c = graph.add_vertex(BaseLabeledVertex("C"))
            d = graph.add_vertex(BaseLabeledVertex("D"))
            e = graph.add_vertex(BaseLabeledVertex("E"))
            f = graph.add_vertex(BaseLabeledVertex("F"))
            graph.add_vertex(g)

            graph.add_edge(BaseLabeledWeightedEdge[int]("A -> B", 3)).from_vertex(
                a
            ).to_vertex(b)
            graph.add_edge(BaseLabeledWeightedEdge[int]("A -> D", 3)).from_vertex(
                a
            ).to_vertex(d)
            graph.add_edge(BaseLabeledWeightedEdge[int]("B -> C", 4)).from_vertex(
                b
            ).to_vertex(c)
            graph.add_edge(BaseLabeledWeightedEdge[int]("C -> A", 3)).from_vertex(
                c
            ).to_vertex(a)
            graph.add_edge(BaseLabeledWeightedEdge[int]("C -> D", 1)).from_vertex(
                c
            ).to_vertex(d)
            graph.add_edge(BaseLabeledWeightedEdge[int]("C -> E", 2)).from_vertex(
                c
            ).to_vertex(e)
            graph.add_edge(BaseLabeledWeightedEdge[int]("D -> E", 2)).from_vertex(
                d
            ).to_vertex(e)
            graph.add_edge(BaseLabeledWeightedEdge[int]("D -> F", 6)).from_vertex(
                d
            ).to_vertex(f)
            graph.add_edge(BaseLabeledWeightedEdge[int]("E -> B", 1)).from_vertex(
                e
            ).to_vertex(b)
            graph.add_edge(BaseLabeledWeightedEdge[int]("E -> G", 1)).from_vertex(
                e
            ).to_vertex(g)
            graph.add_edge(BaseLabeledWeightedEdge[int]("F -> G", 9)).from_vertex(
                f
            ).to_vertex(g)

        graph = CommonsGraph.newDirectedMutableGraph(connect0)

    def testFindMaxFlowAndVerify_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

    def testFindMaxFlowAndVerify_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
