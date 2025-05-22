from __future__ import annotations
import re
from io import BytesIO
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
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class GraphSerializationTestCase(unittest.TestCase):

    __FILE_NAME: str = "target/serialiazedGraph.dat"

    def testSerializeUndirectedWeightdGraph_test2_decomposed(self) -> None:
        graph_connections = self.__buildWeightedGraphConnections()
        g = CommonsGraph.newUndirectedMutableGraph(graph_connections)
        self.__checkSerialization(g)

    def testSerializeUndirectedWeightdGraph_test1_decomposed(self) -> None:
        graph_connection = self.__buildWeightedGraphConnections()
        g = CommonsGraph.newUndirectedMutableGraph(graph_connection)

    def testSerializeUndirectedWeightdGraph_test0_decomposed(self) -> None:
        self.__buildWeightedGraphConnections()

    def testSerializeUndirectedGraph_test2_decomposed(self) -> None:
        graph_connections = self.__buildGraphConnections()
        g = CommonsGraph.newUndirectedMutableGraph(graph_connections)
        self.__checkSerialization(g)

    def testSerializeUndirectedGraph_test1_decomposed(self) -> None:
        graph_connections = self.__buildGraphConnections()
        g = CommonsGraph.newUndirectedMutableGraph(graph_connections)

    def testSerializeUndirectedGraph_test0_decomposed(self) -> None:
        self.__buildGraphConnections()

    def testSerializeSyncronyzedDirectedWeightdGraph_test3_decomposed(self) -> None:
        # Build weighted graph connections
        graph_connections = self.__buildWeightedGraphConnections()

        # Create a directed mutable graph using the connections
        directed_graph = CommonsGraph.newDirectedMutableGraph(graph_connections)

        # Synchronize the directed mutable graph
        synchronized_graph = CommonsGraph.synchronize2(directed_graph)

        # Check serialization of the synchronized graph
        self.__checkSerialization(synchronized_graph)

    def testSerializeSyncronyzedDirectedWeightdGraph_test2_decomposed(self) -> None:
        graph_connections = self.__buildWeightedGraphConnections()
        directed_graph = CommonsGraph.newDirectedMutableGraph(graph_connections)
        synchronized_graph = CommonsGraph.synchronize2(directed_graph)

    def testSerializeSyncronyzedDirectedWeightdGraph_test1_decomposed(self) -> None:
        graph_connections = self.__buildWeightedGraphConnections()
        CommonsGraph.newDirectedMutableGraph(graph_connections)

    def testSerializeSyncronyzedDirectedWeightdGraph_test0_decomposed(self) -> None:
        self.__buildWeightedGraphConnections()

    def testSerializeSpanningTree_test3_decomposed(self) -> None:
        spanning_tree = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        self.__populate(spanning_tree)
        connections = self.__buildWeightedGraphConnections()
        self.__populate(spanning_tree).with_connections(connections)
        self.__checkSerialization(spanning_tree)

    def testSerializeSpanningTree_test2_decomposed(self) -> None:
        spanning_tree = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        self.populate(spanning_tree)
        self.buildWeightedGraphConnections()
        self.populate(spanning_tree).with_connections(
            self.buildWeightedGraphConnections()
        )

    def testSerializeSpanningTree_test1_decomposed(self) -> None:
        spanning_tree = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        self.populate(spanning_tree)
        self.__buildWeightedGraphConnections()

    def testSerializeSpanningTree_test0_decomposed(self) -> None:
        spanning_tree = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
        self.populate(spanning_tree)

    def testSerializePath_test7_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        g = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        g.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        g.addConnectionInTail(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        g.addConnectionInTail(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        g.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

        self.__checkSerialization(g)

    def testSerializePath_test6_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        g = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        g.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )
        g.addConnectionInTail(a, BaseLabeledWeightedEdge[float]("a <-> b", 2.0), b)
        g.addConnectionInTail(b, BaseLabeledWeightedEdge[float]("b <-> c", 3.0), c)
        g.addConnectionInTail(
            c, BaseLabeledWeightedEdge[float]("c <-> goal", 3.0), goal
        )

    def testSerializePath_test5_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        g = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        g.addConnectionInTail(
            start, BaseLabeledWeightedEdge[float]("start <-> a", 1.5), a
        )

    def testSerializePath_test4_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

    def testSerializePath_test3_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")

    def testSerializePath_test2_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")

    def testSerializePath_test1_decomposed(self) -> None:
        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")

    def testSerializePath_test0_decomposed(self) -> None:
        start = BaseLabeledVertex("start")

    def testSerializeDirectedWeightdGraph_test2_decomposed(self) -> None:
        # Build weighted graph connections
        graph_connection = self.__buildWeightedGraphConnections()

        # Create a directed mutable graph using the connections
        g = CommonsGraph.newDirectedMutableGraph(graph_connection)

        # Check serialization of the graph
        self.__checkSerialization(g)

    def testSerializeDirectedWeightdGraph_test1_decomposed(self) -> None:
        graph_connections = self.__buildWeightedGraphConnections()
        g = CommonsGraph.newDirectedMutableGraph(graph_connections)

    def testSerializeDirectedWeightdGraph_test0_decomposed(self) -> None:
        self.__buildWeightedGraphConnections()

    def testSerializeDirectedGraph_test2_decomposed(self) -> None:
        # Build graph connections
        graph_connections = self.__buildGraphConnections()

        # Create a directed mutable graph using the graph connections
        g = CommonsGraph.newDirectedMutableGraph(graph_connections)

        # Check serialization of the graph
        self.__checkSerialization(g)

    def testSerializeDirectedGraph_test1_decomposed(self) -> None:
        graph_connection = self.__buildGraphConnections()
        g = CommonsGraph.newDirectedMutableGraph(graph_connection)

    def testSerializeDirectedGraph_test0_decomposed(self) -> None:
        self.__buildGraphConnections()

    def cleanUp(self) -> None:
        f = pathlib.Path(self.__FILE_NAME)
        if f.exists():
            f.unlink()

    @staticmethod
    def __checkSerialization(g: Graph[BaseLabeledVertex, typing.Any]) -> None:
        # Write the graph object to a file
        with open(GraphSerializationTestCase.__FILE_NAME, "wb") as fout:
            oos = io.BytesIO()
            import pickle

            pickle.dump(g, fout)

        # Read the graph object back from the file
        with open(GraphSerializationTestCase.__FILE_NAME, "rb") as fin:
            cloned = pickle.load(fin)

        # Assert that the original graph and the deserialized graph are equal
        assert g == cloned

    @staticmethod
    def __buildWeightedGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ):
        class CustomGraphConnection(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        ):
            def connect0(self):
                a = self.add_vertex(BaseLabeledVertex("a"))
                b = self.add_vertex(BaseLabeledVertex("b"))
                c = self.add_vertex(BaseLabeledVertex("c"))
                d = self.add_vertex(BaseLabeledVertex("d"))

                self.add_edge(
                    BaseLabeledWeightedEdge[float]("a -> c", 1.0)
                ).from_vertex(a).to_vertex(c)
                self.add_edge(
                    BaseLabeledWeightedEdge[float]("c -> d", 1.0)
                ).from_vertex(c).to_vertex(d)
                self.add_edge(
                    BaseLabeledWeightedEdge[float]("d -> b", 1.0)
                ).from_vertex(d).to_vertex(b)

        return CustomGraphConnection()

    @staticmethod
    def __buildGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledEdge]
    ):
        class CustomGraphConnection(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]
        ):
            def connect0(self):
                a = self.addVertex(BaseLabeledVertex("a"))
                b = self.addVertex(BaseLabeledVertex("b"))
                c = self.addVertex(BaseLabeledVertex("c"))
                d = self.addVertex(BaseLabeledVertex("d"))

                self.addEdge(BaseLabeledEdge("a -> c")).from_(a).to(c)
                self.addEdge(BaseLabeledEdge("c -> d")).from_(c).to(d)
                self.addEdge(BaseLabeledEdge("d -> b")).from_(d).to(b)

        return CustomGraphConnection()
