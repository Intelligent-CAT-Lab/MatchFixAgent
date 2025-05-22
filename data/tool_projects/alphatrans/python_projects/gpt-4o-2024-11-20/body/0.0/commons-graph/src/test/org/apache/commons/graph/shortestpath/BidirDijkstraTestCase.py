from __future__ import annotations
import time
import re
import random
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
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
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class BidirDijkstraTestCase(unittest.TestCase):

    __weightOperations: OrderedMonoid[float] = None

    __vertices: typing.List[BaseLabeledVertex] = None

    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )

    __EPSILON: float = 1.0e-6
    __EDGES: int = 100000
    __NODES: int = 5000
    __TIMES: int = 10

    def testVerifyTwoNodePath_test10_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .to(two)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyTwoNodePath_test9_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .to(two)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

    def testVerifyTwoNodePath_test8_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one).to(two)

    def testVerifyTwoNodePath_test7_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one)

    def testVerifyTwoNodePath_test6_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyTwoNodePath_test5_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        CommonsGraph.findShortestPath(graph)

    def testVerifyTwoNodePath_test4_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

    def testVerifyTwoNodePath_test3_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

    def testVerifyTwoNodePath_test2_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        graph.addVertex(one)
        graph.addVertex(two)

    def testVerifyTwoNodePath_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")

    def testVerifyTwoNodePath_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        one = BaseLabeledVertex("1")

    def testVerifyThreeNodePath_test12_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(a)
            .to(c)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyThreeNodePath_test11_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(a)
            .to(c)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

    def testVerifyThreeNodePath_test10_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a).to(c)

    def testVerifyThreeNodePath_test9_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(a)

    def testVerifyThreeNodePath_test8_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testVerifyThreeNodePath_test7_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        CommonsGraph.findShortestPath(graph)

    def testVerifyThreeNodePath_test6_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

    def testVerifyThreeNodePath_test5_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)
        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )

    def testVerifyThreeNodePath_test4_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

    def testVerifyThreeNodePath_test3_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)

    def testVerifyThreeNodePath_test2_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testVerifyThreeNodePath_test1_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testVerifyThreeNodePath_test0_decomposed(self) -> None:
        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")

    def testNullVertices_test4_decomposed(self) -> None:
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
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None).applyingBidirectionalDijkstra(
                DoubleWeightBaseOperations()
            )

    def testNullVertices_test3_decomposed(self) -> None:
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
        ).from_(a).to(b).applyingBidirectionalDijkstra(None)

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
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None)
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None).applyingBidirectionalDijkstra(
                DoubleWeightBaseOperations()
            )

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
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            )
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
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
            ).from_(a).to(b).applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

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
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
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
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
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

        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(one).to(five)

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
        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

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

    def testCompareToUnidirectional_test0_decomposed(self) -> None:
        r = Random()
        for _ in range(self.__TIMES):
            s = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
            t = None

            while True:
                t = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
                if not s.equals(t):
                    break

            path_uni = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(s)
                .to(t)
                .applyingDijkstra(self.__weightOperations)
            )

            path_bi = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(s)
                .to(t)
                .applyingBidirectionalDijkstra(self.__weightOperations)
            )

            self.assertEqual(path_uni.getSize(), path_bi.getSize())
            self.assertAlmostEqual(
                path_uni.getWeight(), path_bi.getWeight(), delta=self.__EPSILON
            )

    @staticmethod
    def setUp() -> None:
        BidirDijkstraTestCase.__weightOperations = DoubleWeightBaseOperations()

        def add_edge(src: BaseLabeledVertex, dst: BaseLabeledVertex) -> bool:
            try:
                edge = BaseLabeledWeightedEdge(
                    f"{src} -> {dst}", 10.0 * r.random() + 1.0
                )
                BidirDijkstraTestCase.__graph.addEdge(edge).from_(src).to(dst)
                return True
            except GraphException:
                return False

        class CustomGraphConnection(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        ):
            r = random.Random()

            def connect0(self) -> None:
                BidirDijkstraTestCase.__vertices = []
                for i in range(BidirDijkstraTestCase.__NODES):
                    v = BaseLabeledVertex(str(i))
                    self.addVertex(v)
                    BidirDijkstraTestCase.__vertices.append(v)

                for i in range(BidirDijkstraTestCase.__NODES - 1):
                    add_edge(
                        BidirDijkstraTestCase.__vertices[i],
                        BidirDijkstraTestCase.__vertices[i + 1],
                    )

                add_edge(
                    BidirDijkstraTestCase.__vertices[BidirDijkstraTestCase.__NODES - 1],
                    BidirDijkstraTestCase.__vertices[0],
                )

                max_edges = max(
                    0, BidirDijkstraTestCase.__EDGES - BidirDijkstraTestCase.__NODES
                )
                for _ in range(max_edges):
                    while not add_edge(
                        BidirDijkstraTestCase.__vertices[
                            self.r.randint(0, BidirDijkstraTestCase.__NODES - 1)
                        ],
                        BidirDijkstraTestCase.__vertices[
                            self.r.randint(0, BidirDijkstraTestCase.__NODES - 1)
                        ],
                    ):
                        pass

        BidirDijkstraTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            CustomGraphConnection()
        )
