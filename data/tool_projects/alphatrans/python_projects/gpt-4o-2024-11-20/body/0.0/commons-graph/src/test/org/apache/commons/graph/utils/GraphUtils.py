from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.GraphException import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *


class GraphUtils:

    @staticmethod
    def buildSudokuGraph(
        sudoku: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge],
    ) -> List[List[BaseLabeledVertex]]:
        grid: List[List[BaseLabeledVertex]] = [
            [None for _ in range(9)] for _ in range(9)
        ]

        for row in range(9):
            for col in range(9):
                grid[row][col] = BaseLabeledVertex(f"{row}, {col}")
                sudoku.addVertex(grid[row][col])

        rows_offsets = [0, 3, 6]
        cols_offsets = [0, 3, 6]

        for rof in range(3):
            for cof in range(3):
                boxes: List[BaseLabeledVertex] = []
                for row in range(rows_offsets[rof], rows_offsets[rof] + 3):
                    for col in range(cols_offsets[cof], cols_offsets[cof] + 3):
                        boxes.append(grid[row][col])

                for v1 in boxes:
                    for v2 in boxes:
                        if v1 != v2:
                            e = BaseLabeledEdge(f"{v1} -> {v2}")
                            try:
                                sudoku.addEdge(v1, e, v2)
                            except GraphException:
                                pass

        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1 = grid[j][i]
                    v2 = grid[j][h]
                    if v1 != v2:
                        e = BaseLabeledEdge(f"{v1} -> {v2}")
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass

        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1 = grid[i][j]
                    v2 = grid[h][j]
                    if v1 != v2:
                        e = BaseLabeledEdge(f"{v1} -> {v2}")
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass

        return grid

    @staticmethod
    def buildCrownGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        tmp: List[BaseLabeledVertex] = []

        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
            tmp.append(v)

        for i in range(nVertices):
            next = i + 1 if i != (nVertices - 1) else 0
            e = BaseLabeledEdge(f"{i} -> {next}")
            try:
                g.addEdge(tmp[i], e, tmp[next])
            except GraphException:
                pass

    @staticmethod
    def buildCompleteGraph(
        nVertices: int, g: BaseMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        for v1 in g.getVertices0():
            for v2 in g.getVertices0():
                if not v1.equals(v2):
                    try:
                        g.addEdge(v1, BaseLabeledEdge(f"{v1} -> {v2}"), v2)
                    except GraphException:
                        pass

    @staticmethod
    def buildBipartedGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        # Add vertices to the graph
        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        # Create two partitions
        firstPartition: List[BaseLabeledVertex] = []
        secondPartition: List[BaseLabeledVertex] = []

        count = 0
        for v1 in g.getVertices0():
            if count == nVertices // 2:
                break
            firstPartition.append(v1)
            count += 1

        count = 0
        for v2 in g.getVertices0():
            if count < nVertices // 2:
                count += 1
                continue
            secondPartition.append(v2)
            count += 1

        # Add edges between the two partitions
        for v1 in firstPartition:
            for v2 in secondPartition:
                if not v1.equals(v2):
                    try:
                        g.addEdge(v1, BaseLabeledEdge(f"{v1} -> {v2}"), v2)
                    except GraphException:
                        pass

    def __init__(self) -> None:
        raise NotImplementedError("This class is not meant to be instantiated.")
