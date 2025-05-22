from __future__ import annotations
import time
import re
import typing
from typing import *
from io import StringIO
import unittest
import pytest
import io
import numbers
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.coloring.AbstractColoringTest import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class GraphColoringBackTrackingTestCase(AbstractColoringTest, unittest.TestCase):

    def testSudokuWithConstraints_test12_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())
        self.assertEqual(1, sudoku.getColor(grid[0][0]))
        self.assertEqual(8, sudoku.getColor(grid[5][5]))
        self.assertEqual(5, sudoku.getColor(grid[1][2]))

        sb = []
        nf = lambda x: f"{x:02}"  # Format numbers as two digits

        sb.append("\n")
        for i in range(9):
            for j in range(9):
                sb.append("| ")
                sb.append(nf(sudoku.getColor(grid[i][j])))
                sb.append(" | ")
            sb.append("\n")

        Logger.getAnonymousLogger().fine("".join(sb))

    def testSudokuWithConstraints_test11_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())
        self.assertEqual(1, sudoku.getColor(grid[0][0]))
        self.assertEqual(8, sudoku.getColor(grid[5][5]))
        self.assertEqual(5, sudoku.getColor(grid[1][2]))

        sb = io.StringIO()
        nf = "{:02}".format  # Format numbers as two digits

        sb.write("\n")
        for i in range(9):
            for j in range(9):
                sb.write("| ")
                sb.write(nf(sudoku.getColor(grid[i][j])))
                sb.write(" | ")
            sb.write("\n")

    def testSudokuWithConstraints_test10_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())
        self.assertEqual(1, sudoku.getColor(grid[0][0]))
        self.assertEqual(8, sudoku.getColor(grid[5][5]))
        self.assertEqual(5, sudoku.getColor(grid[1][2]))

        sb = []
        sb.append("\n")

    def testSudokuWithConstraints_test9_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())
        self.assertEqual(1, sudoku.getColor(grid[0][0]))
        self.assertEqual(8, sudoku.getColor(grid[5][5]))
        self.assertEqual(5, sudoku.getColor(grid[1][2]))

    def testSudokuWithConstraints_test8_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())

    def testSudokuWithConstraints_test7_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)

    def testSudokuWithConstraints_test6_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )

    def testSudokuWithConstraints_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

    def testSudokuWithConstraints_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)
        CommonsGraph.coloring(g1)
        self._createColorsList(9)

    def testSudokuWithConstraints_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)
        CommonsGraph.coloring(g1)

    def testSudokuWithConstraints_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

    def testSudokuWithConstraints_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)

    def testSudokuWithConstraints_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

    def testSudoku_test9_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        # Perform coloring on the graph
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = coloring_result.applyingBackTrackingAlgorithm0()

        # Assert that the coloring result is not None
        self.assertIsNotNone(sudoku)

        # Check the coloring validity
        self._checkColoring(g1, sudoku)

        # Assert that the required number of colors is 9
        self.assertEqual(9, sudoku.getRequiredColors())

        # Build the string representation of the Sudoku grid
        sb = []
        nf = "{:02d}".format  # Format numbers as two digits

        sb.append("\n")
        for i in range(9):
            for j in range(9):
                sb.append(f"| {nf(sudoku.getColor(grid[i][j]))} | ")
            sb.append("\n")

        # Log the Sudoku grid
        Logger.getAnonymousLogger().fine("".join(sb))

    def testSudoku_test8_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = coloring_result.applyingBackTrackingAlgorithm0()

        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())

        sb = []
        nf = lambda x: f"{x:02}"  # Format numbers as two digits

        sb.append("\n")
        for i in range(9):
            for j in range(9):
                sb.append(f"| {nf(sudoku.getColor(grid[i][j]))} | ")
            sb.append("\n")

        # If needed, you can print or log the result:
        # print("".join(sb))

    def testSudoku_test7_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = coloring_result.applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())
        sb = []
        nf = "{:02d}".format
        sb.append("\n")

    def testSudoku_test6_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = coloring_result.applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())

    def testSudoku_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = coloring_result.applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)

    def testSudoku_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)
        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm0()
        )

    def testSudoku_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(9)
        CommonsGraph.coloring(g1).withColors(colors_list)

    def testSudoku_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)
        self._createColorsList(9)

    def testSudoku_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)
        CommonsGraph.coloring(g1)

    def testSudoku_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

    def testNullGraph_test2_decomposed(self) -> None:
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(None)

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(
                None
            ).applyingBackTrackingAlgorithm0()

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
            CommonsGraph.coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNullColorGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(g).withColors(None)

    def testNullColorGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)

    def testNotEnoughtColorGraph_test5_decomposed(self) -> None:
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
            CommonsGraph.coloring(g).withColors(
                self._createColorsList(1)
            ).applyingBackTrackingAlgorithm0()

    def testNotEnoughtColorGraph_test4_decomposed(self) -> None:
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

    def testNotEnoughtColorGraph_test3_decomposed(self) -> None:
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

    def testNotEnoughtColorGraph_test2_decomposed(self) -> None:
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

    def testNotEnoughtColorGraph_test1_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

    def testNotEnoughtColorGraph_test0_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

    def testEmptyGraph_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.coloring(g)
        self._createColorsList(1)
        self.coloring(g).withColors(self._createColorsList(1))
        coloredVertices = (
            self.coloring(g)
            .withColors(self._createColorsList(1))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(0, coloredVertices.getRequiredColors())

    def testEmptyGraph_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.coloring(g)
        colors_list = self._createColorsList(1)
        self.coloring(g).withColors(colors_list)
        colored_vertices = (
            self.coloring(g).withColors(colors_list).applyingBackTrackingAlgorithm0()
        )

    def testEmptyGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(1)
        CommonsGraph.coloring(g).withColors(colors_list)

    def testEmptyGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)
        self._createColorsList(1)

    def testEmptyGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.coloring(g)

    def testCromaticNumberSparseGraph_test6_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)

        # Create a list of colors
        colors_list = self._createColorsList(1)

        # Apply coloring with the created colors
        coloring_result = coloring_result.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(1, colored_vertices.getRequiredColors())

        # Check the coloring
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberSparseGraph_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        self.coloring(g1)
        colors_list = self._createColorsList(1)
        self.coloring(g1).withColors(colors_list)

        colored_vertices = (
            self.coloring(g1).withColors(colors_list).applyingBackTrackingAlgorithm0()
        )

        self.assertIsNotNone(colored_vertices)
        self.assertEqual(1, colored_vertices.getRequiredColors())

    def testCromaticNumberSparseGraph_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        self.coloring(g1)
        colors_list = self._createColorsList(1)
        self.coloring(g1).withColors(colors_list)
        colored_vertices = (
            self.coloring(g1).withColors(colors_list).applyingBackTrackingAlgorithm0()
        )

    def testCromaticNumberSparseGraph_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(1)
        CommonsGraph.coloring(g1).withColors(colors_list)

    def testCromaticNumberSparseGraph_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)
        self._createColorsList(1)

    def testCromaticNumberSparseGraph_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        CommonsGraph.coloring(g1)

    def testCromaticNumberSparseGraph_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

    def testCromaticNumberComplete_test6_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)

        # Create a list of 100 colors
        colors_list = self._createColorsList(100)

        # Apply the coloring algorithm with the created colors
        colored_vertices = coloring_result.withColors(
            colors_list
        ).applyingBackTrackingAlgorithm0()

        # Assert that the result is not null
        self.assertIsNotNone(colored_vertices)

        # Assert that the required number of colors is 100
        self.assertEqual(100, colored_vertices.getRequiredColors())

        # Check the validity of the coloring
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberComplete_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)

        # Create a list of 100 colors
        colors_list = self._createColorsList(100)

        # Apply the coloring with the created colors
        coloring_result = coloring_result.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(100, colored_vertices.getRequiredColors())

    def testCromaticNumberComplete_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(100)
        CommonsGraph.coloring(g1).withColors(colors_list)
        colored_vertices = (
            CommonsGraph.coloring(g1)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm0()
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

    def testCromaticNumberBiparted_test6_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)

        # Create a list of 2 colors
        colors_list = self._createColorsList(2)

        # Apply coloring with the created colors
        coloring_result = coloring_result.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(2, colored_vertices.getRequiredColors())

        # Check the coloring validity
        self._checkColoring(g1, colored_vertices)

    def testCromaticNumberBiparted_test5_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g1)

        # Create a list of 2 colors
        colors_list = self._createColorsList(2)

        # Apply coloring with the created colors list
        coloring_result = coloring_result.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(2, colored_vertices.getRequiredColors())

    def testCromaticNumberBiparted_test4_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(2)
        coloring_result = CommonsGraph.coloring(g1).withColors(colors_list)
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

    def testCromaticNumberBiparted_test3_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)
        colors_list = self._createColorsList(2)
        CommonsGraph.coloring(g1).withColors(colors_list)

    def testCromaticNumberBiparted_test2_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)
        self._createColorsList(2)

    def testCromaticNumberBiparted_test1_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)
        CommonsGraph.coloring(g1)

    def testCromaticNumberBiparted_test0_decomposed(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)

    def testCromaticNumber_test9_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(3)
        CommonsGraph.coloring(g).withColors(colors_list)

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(coloredVertex)
        )

        self.assertIsNotNone(coloredVertices)
        self.assertEqual(3, coloredVertices.getRequiredColors())
        self.assertEqual(2, coloredVertices.getColor(two))
        self._checkColoring(g, coloredVertices)

    def testCromaticNumber_test8_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(3)
        CommonsGraph.coloring(g).withColors(colors_list)

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(coloredVertex)
        )

        self.assertIsNotNone(coloredVertices)
        self.assertEqual(3, coloredVertices.getRequiredColors())
        self.assertEqual(2, coloredVertices.getColor(two))

    def testCromaticNumber_test7_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(3)
        CommonsGraph.coloring(g).withColors(colors_list)

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm1(coloredVertex)
        )

        self.assertIsNotNone(coloredVertices)
        self.assertEqual(3, coloredVertices.getRequiredColors())

    def testCromaticNumber_test6_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        self.coloring(g)
        self._createColorsList(3)
        self.coloring(g).withColors(self._createColorsList(3))

        coloredVertices = (
            self.coloring(g)
            .withColors(self._createColorsList(3))
            .applyingBackTrackingAlgorithm1(coloredVertex)
        )

    def testCromaticNumber_test5_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices[BaseLabeledVertex, int]()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(3)
        CommonsGraph.coloring(g).withColors(colors_list)

    def testCromaticNumber_test4_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices[BaseLabeledVertex, int]()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)
        self._createColorsList(3)

    def testCromaticNumber_test3_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices[BaseLabeledVertex, int]()
        coloredVertex.addColor(two, 2)

        CommonsGraph.coloring(g)

    def testCromaticNumber_test2_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

        coloredVertex = ColoredVertices[BaseLabeledVertex, int]()
        coloredVertex.addColor(two, 2)

    def testCromaticNumber_test1_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

        def connect0():
            one = g.addVertex(BaseLabeledVertex("1"))
            g.addVertex(two)
            three = g.addVertex(BaseLabeledVertex("3"))

            g.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
            g.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
            g.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)

        g = CommonsGraph.newUndirectedMutableGraph(AbstractGraphConnection(connect0))

    def testCromaticNumber_test0_decomposed(self) -> None:
        two = BaseLabeledVertex("2")

    def testCrawnGraph_test6_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)

        # Perform coloring on the graph
        coloring_instance = CommonsGraph.coloring(g)

        # Create a list of 2 colors
        colors_list = self._createColorsList(2)

        # Apply coloring with the created colors
        coloring_instance = coloring_instance.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_instance.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(2, colored_vertices.getRequiredColors())

        # Check the coloring validity
        self._checkColoring(g, colored_vertices)

    def testCrawnGraph_test5_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)

        # Perform coloring on the graph
        coloring_result = CommonsGraph.coloring(g)

        # Create a list of 2 colors
        colors_list = self._createColorsList(2)

        # Apply coloring with the created colors
        coloring_result = coloring_result.withColors(colors_list)

        # Apply the backtracking algorithm
        colored_vertices = coloring_result.applyingBackTrackingAlgorithm0()

        # Assertions
        self.assertIsNotNone(colored_vertices)
        self.assertEqual(2, colored_vertices.getRequiredColors())

    def testCrawnGraph_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(2)
        CommonsGraph.coloring(g).withColors(colors_list)
        colored_vertices = (
            CommonsGraph.coloring(g)
            .withColors(colors_list)
            .applyingBackTrackingAlgorithm0()
        )

    def testCrawnGraph_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g)
        colors_list = self._createColorsList(2)
        CommonsGraph.coloring(g).withColors(colors_list)

    def testCrawnGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g)
        self._createColorsList(2)

    def testCrawnGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
        CommonsGraph.coloring(g)

    def testCrawnGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)
