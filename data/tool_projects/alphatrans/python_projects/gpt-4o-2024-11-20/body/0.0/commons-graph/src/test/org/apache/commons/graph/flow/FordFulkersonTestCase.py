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


class FordFulkersonTestCase(unittest.TestCase):

    def testNullVertices_test4_decomposed(self) -> None:
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
            ).from_(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None).applyingFordFulkerson(IntegerWeightBaseOperations())

    def testNullVertices_test3_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph)
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None)
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None)

    def testNullVertices_test2_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(graph)
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None)

    def testNullVertices_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())

    def testNullVertices_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findMaxFlow(graph)

    def testNullGraphAndVertices_test4_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None).applyingFordFulkerson(IntegerWeightBaseOperations())

    def testNullGraphAndVertices_test3_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None).to(None)

    def testNullGraphAndVertices_test2_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            ).from_(None)

    def testNullGraphAndVertices_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

    def testNullGraphAndVertices_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

    def testNullGraph_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(BaseWeightedEdge())

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(d)

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(d).applyingFordFulkerson(IntegerWeightBaseOperations())

    def testNullGraph_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

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
            ).from_(a).to(d)

    def testNullGraph_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(BaseWeightedEdge())

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a)

    def testNullGraph_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge[int]()
            )

    def testNullGraph_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")
        with self.assertRaises(RuntimeError):
            CommonsGraph.findMaxFlow(None)

    def testNullGraph_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

    def testNullGraph_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testNotConnected_2_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(actual, expected)

    def testNotConnected_2_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNotConnected_2_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)

    def testNotConnected_2_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 0

        max_flow_builder = CommonsGraph.findMaxFlow(graph)
        max_flow_builder.whereEdgesHaveWeights(BaseWeightedEdge())
        max_flow_builder.whereEdgesHaveWeights(BaseWeightedEdge()).from_(a)

    def testNotConnected_2_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())

    def testNotConnected_2_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 0
        CommonsGraph.findMaxFlow(graph)

    def testNotConnected_2_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)

        graph_connection = AbstractGraphConnection(connect0)
        self.graph = CommonsGraph.newDirectedMutableGraph(graph_connection)

    def testNotConnected_2_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

    def testNotConnected_2_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testNotConnected_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(actual, expected)

    def testNotConnected_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[int]](
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(d),
                ]
            )
        )

        expected = 0

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[int]()
        ).from_(a)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[int]()
        ).from_(a).to(d)

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[int]())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNotConnected_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[int]()
        ).from_(a)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[int]()
        ).from_(a).to(d)

    def testNotConnected_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[int]()
        ).from_(a)

    def testNotConnected_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge[int]())

    def testNotConnected_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 0
        CommonsGraph.findMaxFlow(graph)

    def testNotConnected_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

    def testNotConnected_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

    def testNotConnected_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testFindMaxFlowAndVerify_test8_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 2000

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testFindMaxFlowAndVerify_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 2000

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)
        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testFindMaxFlowAndVerify_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

        expected = 2000
        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        ).to(d)

    def testFindMaxFlowAndVerify_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 2000

        CommonsGraph.findMaxFlow(graph)
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge())
        CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            a
        )

    def testFindMaxFlowAndVerify_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 2000

        # Perform the max flow calculation
        max_flow_builder = CommonsGraph.findMaxFlow(graph)
        max_flow_builder.whereEdgesHaveWeights(BaseWeightedEdge())

    def testFindMaxFlowAndVerify_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))
            self.graph.addVertex(d)

            self.graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            self.graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            self.graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            self.graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))
        expected = 2000
        CommonsGraph.findMaxFlow(graph)

    def testFindMaxFlowAndVerify_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        def connect0():
            graph.addVertex(a)
            b = graph.addVertex(BaseLabeledVertex("B"))
            c = graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(d)

            graph.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
            graph.addEdge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
            graph.addEdge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
            graph.addEdge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
            graph.addEdge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

        graph = CommonsGraph.newDirectedMutableGraph(AbstractGraphConnection(connect0))

    def testFindMaxFlowAndVerify_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

    def testFindMaxFlowAndVerify_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
