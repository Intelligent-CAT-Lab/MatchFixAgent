from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class FindConnectedComponetTestCase(unittest.TestCase):

    def testverifyNullGraph_test2_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(None)

        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(None).includingAllVertices()

        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(
                None
            ).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()

    def testverifyNullGraph_test1_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(None)
            CommonsGraph.findConnectedComponent(None).includingAllVertices()

    def testverifyNullGraph_test0_decomposed(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(None)

    def testVerifyNullVerticesGraph_test4_decomposed(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertEqual(0, len(c))

    def testVerifyNullVerticesGraph_test3_decomposed(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

    def testVerifyNullVerticesGraph_test2_decomposed(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingVertices()

    def testVerifyNullVerticesGraph_test1_decomposed(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)

    def testVerifyNullVerticesGraph_test0_decomposed(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                connect0=lambda: [
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                ]
            )
        )

    def testVerifyEmptyGraph_test3_decomposed(self) -> None:
        graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertEqual(0, len(c))

    def testVerifyEmptyGraph_test2_decomposed(self) -> None:
        graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

    def testVerifyEmptyGraph_test1_decomposed(self) -> None:
        graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()

    def testVerifyEmptyGraph_test0_decomposed(self) -> None:
        graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponentsIncludingVertices2_test7_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        # Create the graph and add vertices
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(e),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        # Find connected components
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component_with_vertices = connected_component.includingVertices(a, e)
        coll = connected_component_with_vertices.applyingMinimumSpanningTreeAlgorithm()

        # Assertions
        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)
        self.assertEqual(2, len(coll))

    def testVerifyConnectedComponentsIncludingVertices2_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(e),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a, e)

        coll = connected_component.includingVertices(
            a, e
        ).applyingMinimumSpanningTreeAlgorithm()

        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)

    def testVerifyConnectedComponentsIncludingVertices2_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(e),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a, e)
        coll = connected_component.includingVertices(
            a, e
        ).applyingMinimumSpanningTreeAlgorithm()

    def testVerifyConnectedComponentsIncludingVertices2_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(BaseLabeledVertex("D"))
            graph.addVertex(e)
            graph.addVertex(BaseLabeledVertex("F"))
            graph.addVertex(BaseLabeledVertex("G"))
            graph.addVertex(BaseLabeledVertex("H"))

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a, e)

    def testVerifyConnectedComponentsIncludingVertices2_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(BaseLabeledVertex("D"))
            graph.addVertex(e)
            graph.addVertex(BaseLabeledVertex("F"))
            graph.addVertex(BaseLabeledVertex("G"))
            graph.addVertex(BaseLabeledVertex("H"))

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponentsIncludingVertices2_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(BaseLabeledVertex("D"))
            graph.addVertex(e)
            graph.addVertex(BaseLabeledVertex("F"))
            graph.addVertex(BaseLabeledVertex("G"))
            graph.addVertex(BaseLabeledVertex("H"))

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

    def testVerifyConnectedComponentsIncludingVertices2_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

    def testVerifyConnectedComponentsIncludingVertices2_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testVerifyConnectedComponentsIncludingVertices_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(BaseLabeledVertex("E")),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F"))
                    .from_(a)
                    .to(BaseLabeledVertex("F")),
                    self.addEdge(BaseLabeledEdge("A -> B"))
                    .from_(a)
                    .to(BaseLabeledVertex("B")),
                    self.addEdge(BaseLabeledEdge("B -> F"))
                    .from_(BaseLabeledVertex("B"))
                    .to(BaseLabeledVertex("F")),
                    self.addEdge(BaseLabeledEdge("C -> G"))
                    .from_(BaseLabeledVertex("C"))
                    .to(BaseLabeledVertex("G")),
                    self.addEdge(BaseLabeledEdge("D -> G"))
                    .from_(BaseLabeledVertex("D"))
                    .to(BaseLabeledVertex("G")),
                    self.addEdge(BaseLabeledEdge("E -> F"))
                    .from_(BaseLabeledVertex("E"))
                    .to(BaseLabeledVertex("F")),
                    self.addEdge(BaseLabeledEdge("H -> C"))
                    .from_(BaseLabeledVertex("H"))
                    .to(BaseLabeledVertex("C")),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a)
        coll = connected_component.includingVertices(
            a
        ).applyingMinimumSpanningTreeAlgorithm()
        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)
        self.assertEqual(1, len(coll))

    def testVerifyConnectedComponentsIncludingVertices_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a)
        coll = connected_component.includingVertices(
            a
        ).applyingMinimumSpanningTreeAlgorithm()
        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)

    def testVerifyConnectedComponentsIncludingVertices_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingVertices(a)
        coll = connected_component.includingVertices(
            a
        ).applyingMinimumSpanningTreeAlgorithm()

    def testVerifyConnectedComponentsIncludingVertices_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingVertices(a)

    def testVerifyConnectedComponentsIncludingVertices_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponentsIncludingVertices_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

    def testVerifyConnectedComponentsIncludingVertices_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testVerifyConnectedComponents3_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))

            self.graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            self.graph.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
            self.graph.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )

        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)
        self.assertEqual(1, len(c))

    def testVerifyConnectedComponents3_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))

            self.graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            self.graph.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
            self.graph.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )

        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)

    def testVerifyConnectedComponents3_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: (
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c),
                    self.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a),
                )
            )
        )

        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

    def testVerifyConnectedComponents3_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            self.graph.addVertex(a)
            b = self.graph.addVertex(BaseLabeledVertex("B"))
            c = self.graph.addVertex(BaseLabeledVertex("C"))

            self.graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            self.graph.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
            self.graph.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()

    def testVerifyConnectedComponents3_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            addVertex(a)
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))

            addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
            addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponents3_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            graph.addVertex(a)
            b = graph.addVertex(BaseLabeledVertex("B"))
            c = graph.addVertex(BaseLabeledVertex("C"))

            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
            graph.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(a)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

    def testVerifyConnectedComponents3_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testVerifyConnectedComponents2_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        connected_components = CommonsGraph.findConnectedComponent(graph)
        connected_components.includingAllVertices()
        c = (
            connected_components.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)
        self.assertEqual(2, len(c))

    def testVerifyConnectedComponents2_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)

    def testVerifyConnectedComponents2_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )

    def testVerifyConnectedComponents2_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()

    def testVerifyConnectedComponents2_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            addVertex(a)
            b = addVertex(BaseLabeledVertex("B"))
            c = addVertex(BaseLabeledVertex("C"))
            d = addVertex(BaseLabeledVertex("D"))
            e = addVertex(BaseLabeledVertex("E"))
            f = addVertex(BaseLabeledVertex("F"))
            g = addVertex(BaseLabeledVertex("G"))
            h = addVertex(BaseLabeledVertex("H"))

            addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
            addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponents2_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: (
                    self.addVertex(a),
                    b := self.addVertex(BaseLabeledVertex("B")),
                    c := self.addVertex(BaseLabeledVertex("C")),
                    d := self.addVertex(BaseLabeledVertex("D")),
                    e := self.addVertex(BaseLabeledVertex("E")),
                    f := self.addVertex(BaseLabeledVertex("F")),
                    g := self.addVertex(BaseLabeledVertex("G")),
                    h := self.addVertex(BaseLabeledVertex("H")),
                    self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f),
                    self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                )
            )
        )

    def testVerifyConnectedComponents2_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

    def testVerifyConnectedComponents_test6_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        # Create the graph using the AbstractGraphConnection
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(BaseLabeledVertex("E")),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        # Perform connectivity operations
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )

        # Assertions
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)  # Equivalent to assertFalse(c.isEmpty())
        self.assertEqual(8, len(c))

    def testVerifyConnectedComponents_test5_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(BaseLabeledVertex("E")),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()
        c = (
            connected_component.includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)

    def testVerifyConnectedComponents_test4_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(BaseLabeledVertex("E")),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )
        CommonsGraph.findConnectedComponent(graph)
        CommonsGraph.findConnectedComponent(graph).includingAllVertices()
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

    def testVerifyConnectedComponents_test3_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        # Define the graph connection logic
        class CustomGraphConnection(AbstractGraphConnection):
            def connect0(self):
                self.addVertex(a)
                self.addVertex(BaseLabeledVertex("B"))
                self.addVertex(BaseLabeledVertex("C"))
                self.addVertex(BaseLabeledVertex("D"))
                self.addVertex(BaseLabeledVertex("E"))
                self.addVertex(BaseLabeledVertex("F"))
                self.addVertex(BaseLabeledVertex("G"))
                self.addVertex(BaseLabeledVertex("H"))

        # Create the graph using the custom connection logic
        graph = CommonsGraph.newUndirectedMutableGraph(CustomGraphConnection())

        # Perform the connected components analysis
        connected_component = CommonsGraph.findConnectedComponent(graph)
        connected_component.includingAllVertices()

    def testVerifyConnectedComponents_test2_decomposed(self) -> None:
        a = BaseLabeledVertex("A")

        def connect0():
            graph.addVertex(a)
            graph.addVertex(BaseLabeledVertex("B"))
            graph.addVertex(BaseLabeledVertex("C"))
            graph.addVertex(BaseLabeledVertex("D"))
            graph.addVertex(BaseLabeledVertex("E"))
            graph.addVertex(BaseLabeledVertex("F"))
            graph.addVertex(BaseLabeledVertex("G"))
            graph.addVertex(BaseLabeledVertex("H"))

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(connect0)
        )

        CommonsGraph.findConnectedComponent(graph)

    def testVerifyConnectedComponents_test1_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge](
                lambda: [
                    self.addVertex(a),
                    self.addVertex(BaseLabeledVertex("B")),
                    self.addVertex(BaseLabeledVertex("C")),
                    self.addVertex(BaseLabeledVertex("D")),
                    self.addVertex(BaseLabeledVertex("E")),
                    self.addVertex(BaseLabeledVertex("F")),
                    self.addVertex(BaseLabeledVertex("G")),
                    self.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

    def testVerifyConnectedComponents_test0_decomposed(self) -> None:
        a = BaseLabeledVertex("A")
