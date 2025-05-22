from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.export.DotExporter import *
from src.test.org.apache.commons.graph.export.EdgeLabelMapper import *
from src.test.org.apache.commons.graph.export.EdgeWeightMapper import *
from src.main.org.apache.commons.graph.export.ExportSelector import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.test.org.apache.commons.graph.export.VertexLabelMapper import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class ExportTestCase(unittest.TestCase):

    __actual: UndirectedMutableGraph[
        BaseLabeledVertex, BaseLabeledWeightedEdge[float]
    ] = None

    def testShouldPrintDotFormat_test6_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")
        CommonsGraph.export(self.__actual).withName("DotFormatGraph").usingDotNotation()
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper())
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        )
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        ).withEdgeLabels(
            EdgeLabelMapper()
        )
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        ).withEdgeLabels(
            EdgeLabelMapper()
        ).to1(
            sys.stdout
        )

    def testShouldPrintDotFormat_test5_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")
        CommonsGraph.export(self.__actual).withName("DotFormatGraph").usingDotNotation()
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper())
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        )
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        ).withEdgeLabels(
            EdgeLabelMapper()
        )

    def testShouldPrintDotFormat_test4_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")
        CommonsGraph.export(self.__actual).withName("DotFormatGraph").usingDotNotation()
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper())
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper()).withEdgeWeights(
            EdgeWeightMapper()
        )

    def testShouldPrintDotFormat_test3_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")
        CommonsGraph.export(self.__actual).withName("DotFormatGraph").usingDotNotation()
        CommonsGraph.export(self.__actual).withName(
            "DotFormatGraph"
        ).usingDotNotation().withVertexLabels(VertexLabelMapper())

    def testShouldPrintDotFormat_test2_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")
        CommonsGraph.export(self.__actual).withName("DotFormatGraph").usingDotNotation()

    def testShouldPrintDotFormat_test1_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)
        CommonsGraph.export(self.__actual).withName("DotFormatGraph")

    def testShouldPrintDotFormat_test0_decomposed(self) -> None:
        CommonsGraph.export(self.__actual)

    def tearDown(self) -> None:
        self.__actual = None

    def setUp(self) -> None:
        self.__actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]](
                connect0=lambda: self._connect_graph()
            )
        )

    def _connect_graph(self) -> None:
        start = self.__actual.addVertex(BaseLabeledVertex("start"))
        a = self.__actual.addVertex(BaseLabeledVertex("a"))
        b = self.__actual.addVertex(BaseLabeledVertex("b"))
        goal = self.__actual.addVertex(BaseLabeledVertex("goal"))

        self.__actual.addEdge(BaseLabeledWeightedEdge[float]("start <-> a", 1.5)).from_(
            start
        ).to(a)
        self.__actual.addEdge(BaseLabeledWeightedEdge[float]("a <-> b", 2.0)).from_(
            a
        ).to(b)
        self.__actual.addEdge(BaseLabeledWeightedEdge[float]("a <-> goal", 2.0)).from_(
            a
        ).to(goal)
        self.__actual.addEdge(BaseLabeledWeightedEdge[float]("b <-> goal", 2.0)).from_(
            b
        ).to(goal)
