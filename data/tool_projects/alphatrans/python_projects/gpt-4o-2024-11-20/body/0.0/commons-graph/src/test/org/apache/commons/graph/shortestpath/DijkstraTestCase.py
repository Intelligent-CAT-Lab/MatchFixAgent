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
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class DijkstraTestCase(unittest.TestCase):

    def testNullVertices_test4_decomposed(self) -> None:
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
            ).from_(None).to(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None).applyingDijkstra(DoubleWeightBaseOperations())

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
            ).from_(None).to(None)

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

    def testNullMonoid_test7_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingDijkstra(None)

    def testNullMonoid_test6_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a).to(b)

    def testNullMonoid_test5_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)

    def testNullMonoid_test4_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullMonoid_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)

    def testNullMonoid_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

    def testNullMonoid_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testNullMonoid_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testNullGraph_test4_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to(None).applyingDijkstra(DoubleWeightBaseOperations())

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
            ).from_(None).to(None)

    def testNullGraph_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )

        with self.assertRaises(RuntimeError):
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

    def testNotConnectGraph_test7_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        with self.assertRaises(PathNotFoundException):
            CommonsGraph.findShortestPath(graph)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingDijkstra(DoubleWeightBaseOperations())

    def testNotConnectGraph_test6_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a).to(b)

    def testNotConnectGraph_test5_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)

    def testNotConnectGraph_test4_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNotConnectGraph_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        CommonsGraph.findShortestPath(graph)

    def testNotConnectGraph_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

    def testNotConnectGraph_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testNotConnectGraph_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testFindShortestPathAndVerify_test15_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
        expected.addConnectionInTail(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
        expected.addConnectionInTail(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .to(five)
            .applyingDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testFindShortestPathAndVerify_test14_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .to(five)
            .applyingDijkstra(DoubleWeightBaseOperations())
        )

        # Add assertions to compare `expected` and `actual` if needed

    def testFindShortestPathAndVerify_test13_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

        findShortestPath(graph)
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]())
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            one
        )
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            one
        ).to(five)

    def testFindShortestPathAndVerify_test12_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one)

    def testFindShortestPathAndVerify_test11_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testFindShortestPathAndVerify_test10_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

        CommonsGraph.findShortestPath(graph)

    def testFindShortestPathAndVerify_test9_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)
        graph.add_vertex(six)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.add_edge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
        )
        expected.add_connection_in_tail(
            three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
        )
        expected.add_connection_in_tail(
            six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five
        )

    def testFindShortestPathAndVerify_test8_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)
        graph.add_vertex(six)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.add_edge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
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
        six = BaseLabeledVertex("6")

        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)
        graph.add_vertex(six)

        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        graph.add_edge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        graph.add_edge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)
        graph.add_edge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        graph.add_edge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

    def testFindShortestPathAndVerify_test6_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")
        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)
        graph.add_vertex(six)

    def testFindShortestPathAndVerify_test5_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

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
