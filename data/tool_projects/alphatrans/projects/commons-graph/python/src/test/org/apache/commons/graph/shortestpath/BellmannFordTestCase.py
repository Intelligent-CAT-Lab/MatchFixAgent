from __future__ import annotations
import time
import re
import unittest
import pytest
import pathlib
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class BellmannFordTestCase(unittest.TestCase):

    def testNullVertices_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).applyingBelmannFord(DoubleWeightBaseOperations())

    def testNullVertices_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None)

    def testNullVertices_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullVertices_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)

    def testNullMonoid_test4_decomposed(self) -> None:
        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(graph)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).applyingBelmannFord(None)

    def testNullMonoid_test3_decomposed(self) -> None:
        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)

    def testNullMonoid_test2_decomposed(self) -> None:
        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullMonoid_test1_decomposed(self) -> None:
        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.findShortestPath(graph)

    def testNullMonoid_test0_decomposed(self) -> None:
        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

    def testNullGraph_test3_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).applyingBelmannFord(DoubleWeightBaseOperations())

    def testNullGraph_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None)

    def testNullGraph_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )

    def testNullGraph_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)

    def testNotConnectGraph_test1_decomposed(self) -> None:
        a = None
        b = None
        all_vertex_pairs_shortest_path = None

        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)

            all_vertex_pairs_shortest_path = (
                CommonsGraph.findShortestPath(graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(a)
                .applyingBelmannFord(DoubleWeightBaseOperations())
            )
        except PathNotFoundException as e:
            pytest.fail(e.getMessage())

        all_vertex_pairs_shortest_path.findShortestPath(a, b)

    def testNotConnectGraph_test0_decomposed(self) -> None:
        a = None
        b = None
        all_vertex_pairs_shortest_path = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)

            all_vertex_pairs_shortest_path = (
                CommonsGraph.findShortestPath(graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(a)
                .applyingBelmannFord(DoubleWeightBaseOperations())
            )
        except PathNotFoundException as e:
            pytest.fail(e.getMessage())

    def testFindShortestPathAndVerify_test14_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four)
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three
        )

        all_vertex_pairs_shortest_path = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .applyingBelmannFord(DoubleWeightBaseOperations())
        )

        actual = all_vertex_pairs_shortest_path.findShortestPath(one, three)

        self.assertEqual(expected, actual)

    def testFindShortestPathAndVerify_test13_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

        allVertexPairsShortestPath = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .applyingBelmannFord(DoubleWeightBaseOperations())
        )

        actual = allVertexPairsShortestPath.findShortestPath(one, three)

    def testFindShortestPathAndVerify_test12_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

        shortest_path_builder = CommonsGraph.findShortestPath(graph)
        shortest_path_builder = shortest_path_builder.whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        shortest_path_builder = shortest_path_builder.from_(one)

        all_vertex_pairs_shortest_path = shortest_path_builder.applyingBelmannFord(
            DoubleWeightBaseOperations()
        )

    def testFindShortestPathAndVerify_test11_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one)

    def testFindShortestPathAndVerify_test10_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testFindShortestPathAndVerify_test9_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

        CommonsGraph.findShortestPath(graph)

    def testFindShortestPathAndVerify_test8_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )
        expected.add_connection_in_tail(
            four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three
        )

    def testFindShortestPathAndVerify_test7_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four
        )

    def testFindShortestPathAndVerify_test6_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 6.0), two)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 4", 7.0), four)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 5.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 5", -4.0), five)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 8.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 2", -2.0), two)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 3", -3.0), three)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 9.0), five)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 3", 7.0), three)
        graph.add_edge(five, BaseLabeledWeightedEdge[float]("5 -> 1", 2.0), one)

    def testFindShortestPathAndVerify_test5_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

    def testFindShortestPathAndVerify_test4_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

    def testFindShortestPathAndVerify_test3_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")

    def testFindShortestPathAndVerify_test2_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")

    def testFindShortestPathAndVerify_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")

    def testFindShortestPathAndVerify_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
