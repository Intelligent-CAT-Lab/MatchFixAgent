from __future__ import annotations
import time
import re
import typing
from typing import *
import unittest
import pytest
import io
import numbers
import os
import unittest
import typing
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.coloring.AbstractColoringTest import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class GraphColoringTestCase(AbstractColoringTest, unittest.TestCase):

    __colors: typing.Set[int] = set(range(11))

    def testSudoku_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)
        col = self._createColorsList(9)
        coloring_builder = CommonsGraph.coloring(g1)
        coloring_builder.withColors(col)
        sudoku = coloring_builder.withColors(col).applyingBackTrackingAlgorithm0()
        self._checkColoring(g1, sudoku)

    def testSudoku_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)
        col = self._createColorsList(9)
        coloring_builder = CommonsGraph.coloring(g1)
        coloring_builder.withColors(col)
        sudoku = coloring_builder.withColors(col).applyingBackTrackingAlgorithm0()

    def testSudoku_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)
        col = self._createColorsList(9)
        CommonsGraph.coloring(g1)
        CommonsGraph.coloring(g1).withColors(col)

    def testSudoku_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)
        col = self._createColorsList(9)
        CommonsGraph.coloring(g1)

    def testSudoku_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)
        col = self._createColorsList(9)

    def testSudoku_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildSudokuGraph(g1)

    def testNullGraph_test2_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(None).applyingGreedyAlgorithm()

    def testNullGraph_test1_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None)
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(None)

    def testNullGraph_test0_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None)

    def testNullColorGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(g).withColors(None)
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNullColorGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(g).withColors(None)

    def testNullColorGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)

    def testNotEnoughtColorGreedyGraph_test5_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        with pytest.raises(NotEnoughColorsException):
            colors = self._createColorsList(1)
            CommonsGraph.coloring(g).withColors(colors).applyingGreedyAlgorithm()

    def testNotEnoughtColorGreedyGraph_test4_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(1)
        CommonsGraph.coloring(g).withColors(colors_list)

    def testNotEnoughtColorGreedyGraph_test3_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        CommonsGraph.coloring(g)
        self._createColorsList(1)

    def testNotEnoughtColorGreedyGraph_test2_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        CommonsGraph.coloring(g)

    def testNotEnoughtColorGreedyGraph_test1_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

    def testNotEnoughtColorGreedyGraph_test0_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

    def testEmptyGraph_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.coloring(g)
        colors_list = self._createColorsList(1)
        self.coloring(g).withColors(colors_list)
        colored_vertices = (
            self.coloring(g).withColors(colors_list).applyingGreedyAlgorithm()
        )
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(0, colored_vertices.getRequiredColors())

    def testEmptyGraph_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.coloring(g)
        colors_list = self._createColorsList(1)
        self.coloring(g).withColors(colors_list)
        colored_vertices = (
            self.coloring(g).withColors(colors_list).applyingGreedyAlgorithm()
        )

    def testEmptyGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.coloring(g)
        colors_list = self._createColorsList(1)
        self.coloring(g).withColors(colors_list)

    def testEmptyGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)
        self._createColorsList(1)

    def testEmptyGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)

    def testCromaticNumberSparseGraph_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)
        coloring_result.withColors(self.__colors)
        colored_vertices = coloring_result.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()

        # Assert that the required number of colors is 1
        self.assertEqual(1, colored_vertices.getRequiredColors())

        # Check the coloring validity
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberSparseGraph_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)
        coloring_result.withColors(self.__colors)

        # Apply the greedy algorithm for coloring
        colored_vertices = coloring_result.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()

        # Assert that the required number of colors is 1
        self.assertEqual(1, colored_vertices.getRequiredColors())

    def testCromaticNumberSparseGraph_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)
        CommonsGraph.coloring(g1).withColors(self.__colors)
        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self.__colors)
            .applyingGreedyAlgorithm()
        )

    def testCromaticNumberSparseGraph_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)
        CommonsGraph.coloring(g1).withColors(self.__colors)

    def testCromaticNumberSparseGraph_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)

    def testCromaticNumberSparseGraph_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

    def testCromaticNumberComplete_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(100)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        colored_vertices = coloring_result.applyingGreedyAlgorithm()
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberComplete_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(100)
        CommonsGraph.coloring(g1).withColors(colors_list)
        colored_vertices = (
            CommonsGraph.coloring(g1).withColors(colors_list).applyingGreedyAlgorithm()
        )

    def testCromaticNumberComplete_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(100)
        CommonsGraph.coloring(g1).withColors(colors_list)

    def testCromaticNumberComplete_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)
        self._createColorsList(100)

    def testCromaticNumberComplete_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)

    def testCromaticNumberComplete_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)

    def testCromaticNumberBiparted_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        coloring_builder = CommonsGraph.coloring(g1)
        coloring_builder.withColors(self.__colors)
        colored_vertices = coloring_builder.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberBiparted_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        coloring_result = CommonsGraph.coloring(g1)
        coloring_result.withColors(self.__colors)
        colored_vertices = coloring_result.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()

    def testCromaticNumberBiparted_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)
        CommonsGraph.coloring(g1).withColors(self.__colors)

    def testCromaticNumberBiparted_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)

    def testCromaticNumberBiparted_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)

    def testCromaticNumber_test4_decomposed(self) -> None:
        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_graph())
        )
        CommonsGraph.coloring(g)
        CommonsGraph.coloring(g).withColors(self.__colors)
        colored_vertices = (
            CommonsGraph.coloring(g).withColors(self.__colors).applyingGreedyAlgorithm()
        )
        self._checkColoring(g, colored_vertices)

    def _connect_graph(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        two = self.addVertex(BaseLabeledVertex("2"))
        three = self.addVertex(BaseLabeledVertex("3"))

        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

    def testCromaticNumber_test3_decomposed(self) -> None:
        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_graph())
        )
        CommonsGraph.coloring(g)
        CommonsGraph.coloring(g).withColors(self.__colors)
        colored_vertices = (
            CommonsGraph.coloring(g).withColors(self.__colors).applyingGreedyAlgorithm()
        )

    def _connect_graph(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        two = self.addVertex(BaseLabeledVertex("2"))
        three = self.addVertex(BaseLabeledVertex("3"))

        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

    def testCromaticNumber_test2_decomposed(self) -> None:
        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_graph())
        )
        CommonsGraph.coloring(g)
        CommonsGraph.coloring(g).withColors(self.__colors)

    def _connect_graph(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        two = self.addVertex(BaseLabeledVertex("2"))
        three = self.addVertex(BaseLabeledVertex("3"))

        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

    def testCromaticNumber_test1_decomposed(self) -> None:
        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0=lambda: self._connect_graph())
        )
        CommonsGraph.coloring(g)

    def _connect_graph(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        two = self.addVertex(BaseLabeledVertex("2"))
        three = self.addVertex(BaseLabeledVertex("3"))

        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

    def testCromaticNumber_test0_decomposed(self) -> None:
        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                connect0=lambda: (
                    [
                        addVertex(BaseLabeledVertex("1")),
                        addVertex(BaseLabeledVertex("2")),
                        addVertex(BaseLabeledVertex("3")),
                    ],
                    [
                        addEdge(BaseLabeledEdge("1 -> 2"))
                        .from_(BaseLabeledVertex("1"))
                        .to(BaseLabeledVertex("2")),
                        addEdge(BaseLabeledEdge("2 -> 3"))
                        .from_(BaseLabeledVertex("2"))
                        .to(BaseLabeledVertex("3")),
                        addEdge(BaseLabeledEdge("3 -> 1"))
                        .from_(BaseLabeledVertex("3"))
                        .to(BaseLabeledVertex("1")),
                    ],
                )
            )
        )

    def testCrawnGraph_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        coloring_builder = CommonsGraph.coloring(g)
        coloring_builder.withColors(self.__colors)
        colored_vertices = coloring_builder.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()
        self._checkColoring(g, colored_vertices)

    def testCrawnGraph_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        coloring_builder = CommonsGraph.coloring(g)
        coloring_builder.withColors(self.__colors)
        colored_vertices = coloring_builder.withColors(
            self.__colors
        ).applyingGreedyAlgorithm()

    def testCrawnGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g).withColors(self.__colors)

    def testCrawnGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g)

    def testCrawnGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
