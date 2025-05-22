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
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class AStarTestCase(unittest.TestCase):

    def testNullVertices_test5_decomposed(self) -> None:
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
            ).from_(None).to(None).applyingAStar(DoubleWeightBaseOperations())

        with self.assertRaises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

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
            ).from_(None).to(None).applyingAStar(DoubleWeightBaseOperations())

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
        with pytest.raises(RuntimeError):
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

    def testNullMonoid_test8_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
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
            ).from_(a).to(b)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingAStar(None)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingAStar(None).withHeuristic(heuristic)

    def testNullMonoid_test7_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
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
            ).from_(a).to(b)
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingAStar(None)

    def testNullMonoid_test6_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

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
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

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
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
        except RuntimeError as e:
            pytest.fail(e.getMessage())

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
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            def apply_heuristic(
                current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current)

            heuristic = Heuristic(apply_heuristic)

        except RuntimeError as e:
            pytest.fail(e.args[0] if e.args else "RuntimeError occurred")

        CommonsGraph.findShortestPath(graph)

    def testNullMonoid_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        heuristics: dict[BaseLabeledVertex, float] = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic[BaseLabeledVertex, float](
                lambda current, goal: heuristics.get(current)
            )
        except RuntimeError as e:
            pytest.fail(e.getMessage())

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

    def testNullHeuristic_test5_decomposed(self) -> None:
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
            ).from_(BaseLabeledVertex("a"))
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b"))
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b")).applyingAStar(
                DoubleWeightBaseOperations()
            )
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b")).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

    def testNullHeuristic_test4_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a"))
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b"))
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b")).applyingAStar(
            DoubleWeightBaseOperations()
        )

    def testNullHeuristic_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a"))
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a")).to(BaseLabeledVertex("b"))

    def testNullHeuristic_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).from_(BaseLabeledVertex("a"))

    def testNullHeuristic_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)
        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )

    def testNullHeuristic_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        CommonsGraph.findShortestPath(graph)

    def testNullGraph_test5_decomposed(self) -> None:
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
            ).from_(None).to(None).applyingAStar(DoubleWeightBaseOperations())
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to(None).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

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
            ).from_(None).to(None).applyingAStar(DoubleWeightBaseOperations())

    def testNullGraph_test3_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
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

    def testNullGraph_test2_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            )

        with pytest.raises(RuntimeError):
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

    def testNotConnectGraph_test8_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)
        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

        with pytest.raises(PathNotFoundException):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingAStar(DoubleWeightBaseOperations()).withHeuristic(
                heuristic
            )

    def testNotConnectGraph_test7_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

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
        ).from_(a).to(b).applyingAStar(DoubleWeightBaseOperations())

    def testNotConnectGraph_test6_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

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

        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

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

        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

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

        heuristics: dict[BaseLabeledVertex, float] = {}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()
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

    def testFindShortestPathAndVerify_test17_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics.get(current, 0.0)

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        expected.addConnectionInTail(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(start)
            .to(goal)
            .applyingAStar(DoubleWeightBaseOperations())
            .withHeuristic(heuristic)
        )

        self.assertEqual(expected, actual)

    def testFindShortestPathAndVerify_test16_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c
        )
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(start)
            .to(goal)
            .applyingAStar(DoubleWeightBaseOperations())
            .withHeuristic(heuristic)
        )

        self.assertEqual(expected, actual)

    def testFindShortestPathAndVerify_test15_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c
        )
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        findShortestPath(graph)
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]())
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            start
        )
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            start
        ).to(goal)
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            start
        ).to(goal).applyingAStar(DoubleWeightBaseOperations())

    def testFindShortestPathAndVerify_test14_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c
        )
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        result = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(start)
            .to(goal)
        )

        self.assertEqual(expected, result)

    def testFindShortestPathAndVerify_test13_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c
        )
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        findShortestPath(graph)
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]())
        findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge[float]()).from_(
            start
        )

    def testFindShortestPathAndVerify_test12_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        expected.addConnectionInTail(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal
        )

        result = CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        )
        # Add assertions here to verify the result matches the expected path

    def testFindShortestPathAndVerify_test11_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c
        )
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        CommonsGraph.findShortestPath(graph)

    def testFindShortestPathAndVerify_test10_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge("start <-> a", 1.5), a
        )
        expected.addConnectionInTail(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        expected.addConnectionInTail(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addConnectionInTail(
            c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal
        )

    def testFindShortestPathAndVerify_test9_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a)
        graph.addEdge(start, BaseLabeledWeightedEdge[float]("start <-> d", 2.0), d)
        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        graph.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal)
        graph.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 3.0), e)
        graph.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> goal", 2.0), goal)

        heuristics = {a: 4.0, b: 2.0, c: 4.0, d: 4.5, e: 2.0, goal: 6.0}

        class CustomHeuristic(Heuristic[BaseLabeledVertex, float]):
            def applyHeuristic(
                self, current: BaseLabeledVertex, goal: BaseLabeledVertex
            ) -> float:
                return heuristics[current]

        heuristic = CustomHeuristic()

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        expected.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )

    def testFindShortestPathAndVerify_test8_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        graph.add_vertex(start)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_vertex(goal)

        graph.add_edge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        graph.add_edge(start, BaseLabeledWeightedEdge("start <-> d", 2.0), d)
        graph.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 2.0), b)
        graph.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        graph.add_edge(c, BaseLabeledWeightedEdge("c <-> goal", 3.0), goal)
        graph.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 3.0), e)
        graph.add_edge(e, BaseLabeledWeightedEdge("e <-> goal", 2.0), goal)

    def testFindShortestPathAndVerify_test7_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")
        graph.addVertex(start)
        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)
        graph.addVertex(d)
        graph.addVertex(e)
        graph.addVertex(goal)

    def testFindShortestPathAndVerify_test6_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

    def testFindShortestPathAndVerify_test5_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

    def testFindShortestPathAndVerify_test4_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")

    def testFindShortestPathAndVerify_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testFindShortestPathAndVerify_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testFindShortestPathAndVerify_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")

    def testFindShortestPathAndVerify_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        start = BaseLabeledVertex("start")
