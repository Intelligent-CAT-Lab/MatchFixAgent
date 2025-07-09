from __future__ import annotations
import re
import threading
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from src.test.org.apache.commons.graph.utils.TestRunner import *


class BaseMutableGraphTestCase(unittest.TestCase):

    def testUndirectedGraphRemoveEdgeNotExists_test1_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        e: BaseLabeledEdge = None

        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            pytest.fail(ex.getMessage())

        with pytest.raises(GraphException):
            g.removeEdge(e)

    def testUndirectedGraphRemoveEdgeNotExists_test0_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        e: BaseLabeledEdge = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            pytest.fail(ex.getMessage())

    def testUndirectedGraphRemoveEdge_test6_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)
        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testUndirectedGraphRemoveEdge_test5_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)
        edge = g.getEdge(source, target)

    def testUndirectedGraphRemoveEdge_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)

    def testUndirectedGraphRemoveEdge_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)

    def testUndirectedGraphRemoveEdge_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)

    def testUndirectedGraphRemoveEdge_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

    def testUndirectedGraphRemoveEdge_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(valueOf(1))

    def testMultiThreadUndirectGraph_test7_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())
        self.assertEqual((30 * (30 - 1) // 2), g.getSize())

    def testMultiThreadUndirectGraph_test6_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())

    def testMultiThreadUndirectGraph_test5_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

    def testMultiThreadUndirectGraph_test4_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)

    def testMultiThreadUndirectGraph_test3_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

    def testMultiThreadUndirectGraph_test2_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)

    def testMultiThreadUndirectGraph_test1_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1: GraphInsert = GraphInsert(g, 0, 10)

    def testMultiThreadUndirectGraph_test0_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

    def testGetNotExistsEdge_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        source = BaseLabeledVertex("1")
        target = BaseLabeledVertex("2")
        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testGetNotExistsEdge_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
        source = BaseLabeledVertex("1")
        target = BaseLabeledVertex("2")
        edge = g.getEdge(source, target)

    def testGetNotExistsEdge_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
        source = BaseLabeledVertex("1")
        target = BaseLabeledVertex("2")

    def testGetNotExistsEdge_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
        source = BaseLabeledVertex(str(1))

    def testGetNotExistsEdge_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

    def testGetEgdeNotExistsVertex_2_test1_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None

        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex("1")
            target = BaseLabeledVertex("200")
        except GraphException as e:
            pytest.fail(e.getMessage())

        with pytest.raises(GraphException):
            g.getEdge(source, target)

    def testGetEgdeNotExistsVertex_2_test0_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex(str(1))
            target = BaseLabeledVertex(str(200))
        except GraphException as e:
            pytest.fail(e.getMessage())

    def testGetEgdeNotExistsVertex_test1_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None

        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex(str(100))
            target = BaseLabeledVertex(str(2))
        except GraphException as e:
            pytest.fail(e.getMessage())

        with pytest.raises(GraphException):
            g.getEdge(source, target)

    def testGetEgdeNotExistsVertex_test0_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex(str(100))
            target = BaseLabeledVertex(str(2))
        except GraphException as e:
            pytest.fail(e.getMessage())

    def testGetEdge_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        edge = g.getEdge(source, target)
        self.assertIsNotNone(edge)

    def testGetEdge_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        edge = g.getEdge(source, target)

    def testGetEdge_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

    def testGetEdge_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        source = BaseLabeledVertex(str(1))

    def testGetEdge_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)

    def testGetConnectedVerticesOnNotConnectedGraph_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        test_vertex = BaseLabeledVertex("1")
        connected_vertices = g.getConnectedVertices(test_vertex)
        self.assertIsNotNone(connected_vertices)

        v = []
        for base_labeled_vertex in connected_vertices:
            v.append(base_labeled_vertex)

        self.assertEqual(0, len(v))

    def testGetConnectedVerticesOnNotConnectedGraph_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        testVertex = BaseLabeledVertex("1")
        connectedVertices = g.getConnectedVertices(testVertex)
        self.assertIsNotNone(connectedVertices)

        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)

    def testGetConnectedVerticesOnNotConnectedGraph_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
        test_vertex = BaseLabeledVertex("1")
        connected_vertices = g.getConnectedVertices(test_vertex)

    def testGetConnectedVerticesOnNotConnectedGraph_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
        test_vertex = BaseLabeledVertex("1")

    def testGetConnectedVerticesOnNotConnectedGraph_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

    def testGetConnectedVerticesNPE_test1_decomposed(self) -> None:
        g = None
        not_exists_vertex = None

        try:
            # Create an instance of UndirectedMutableGraph
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            # Build a complete graph with 10 vertices
            GraphUtils.buildCompleteGraph(10, g)

            # Create a vertex that does not exist in the graph
            not_exists_vertex = BaseLabeledVertex(str(1000))
        except GraphException as e:
            pytest.fail(e.getMessage())

        # Attempt to get connected vertices for a non-existent vertex
        with pytest.raises(GraphException):
            g.getConnectedVertices(not_exists_vertex)

    def testGetConnectedVerticesNPE_test0_decomposed(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        not_exists_vertex: BaseLabeledVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            not_exists_vertex = BaseLabeledVertex(str(1000))
        except GraphException as e:
            pytest.fail(e.getMessage())

    def testGetConnectedVertices_test5_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        test_vertex = BaseLabeledVertex(str(1))
        connected_vertices = g.getConnectedVertices(test_vertex)
        self.assertIsNotNone(connected_vertices)

        v = []
        for base_labeled_vertex in connected_vertices:
            v.append(base_labeled_vertex)

        self.assertEqual(9, len(v))
        self.assertFalse(test_vertex in v)

    def testGetConnectedVertices_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        test_vertex = BaseLabeledVertex(str(1))
        connected_vertices = g.getConnectedVertices(test_vertex)
        self.assertIsNotNone(connected_vertices)

        v = []
        for base_labeled_vertex in connected_vertices:
            v.append(base_labeled_vertex)

        self.assertEqual(9, len(v))

    def testGetConnectedVertices_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        test_vertex = BaseLabeledVertex(str(1))
        connected_vertices = g.getConnectedVertices(test_vertex)
        self.assertIsNotNone(connected_vertices)
        v = []
        for base_labeled_vertex in connected_vertices:
            v.append(base_labeled_vertex)

    def testGetConnectedVertices_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        test_vertex = BaseLabeledVertex(str(1))
        connected_vertices = g.getConnectedVertices(test_vertex)

    def testGetConnectedVertices_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)
        test_vertex = BaseLabeledVertex(str(1))

    def testGetConnectedVertices_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)

    def testDirectedMultiTh_test7_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())
        self.assertEqual(30 * (30 - 1), g.getSize())

    def testDirectedMultiTh_test6_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())

    def testDirectedMultiTh_test5_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

    def testDirectedMultiTh_test4_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)

    def testDirectedMultiTh_test3_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

    def testDirectedMultiTh_test2_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)

    def testDirectedMultiTh_test1_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        tr1: GraphInsert = GraphInsert(g, 0, 10)

    def testDirectedMultiTh_test0_decomposed(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = CommonsGraph.synchronize2(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

    def testDirectedGraphRemoveEdgeNotExists_test1_decomposed(self) -> None:
        g: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] | None = None
        e: BaseLabeledEdge | None = None

        try:
            g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            pytest.fail(str(ex))

        with pytest.raises(GraphException):
            g.removeEdge(e)

    def testDirectedGraphRemoveEdgeNotExists_test0_decomposed(self) -> None:
        g: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        e: BaseLabeledEdge = None
        try:
            g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            pytest.fail(str(ex))

    def testDirectedGraphRemoveEdge_test6_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex("1")
        target = BaseLabeledVertex("2")
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)
        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testDirectedGraphRemoveEdge_test5_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)
        edge = g.getEdge(source, target)

    def testDirectedGraphRemoveEdge_test4_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)
        g.removeEdge(e)

    def testDirectedGraphRemoveEdge_test3_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)
        e = g.getEdge(source, target)

    def testDirectedGraphRemoveEdge_test2_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        GraphUtils.buildCompleteGraph(10, g)

    def testDirectedGraphRemoveEdge_test1_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(valueOf(1))
        target = BaseLabeledVertex(valueOf(2))

    def testDirectedGraphRemoveEdge_test0_decomposed(self) -> None:
        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(valueOf(1))

    def testAddVertexAndEdge_test18_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices and edges
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))
        self.assertEqual(1, gSimple.getOutDegree(one))
        self.assertEqual(0, gSimple.getOutDegree(two))
        self.assertFalse(gSimple.containsEdge(BaseLabeledEdge("Not Exist Edge")))
        self.assertFalse(gSimple.containsVertex(BaseLabeledVertex("Not exist vertex")))

    def testAddVertexAndEdge_test17_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices and edges
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))
        self.assertEqual(1, gSimple.getOutDegree(one))
        self.assertEqual(0, gSimple.getOutDegree(two))
        self.assertFalse(gSimple.containsEdge(BaseLabeledEdge("Not Exist Edge")))

    def testAddVertexAndEdge_test16_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices and edges
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))
        self.assertEqual(1, gSimple.getOutDegree(one))
        self.assertEqual(0, gSimple.getOutDegree(two))

    def testAddVertexAndEdge_test15_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed mutable graph
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))

    def testAddVertexAndEdge_test14_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed mutable graph
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))

    def testAddVertexAndEdge_test13_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed mutable graph
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())

    def testAddVertexAndEdge_test12_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)

        # Assert the order and size of the graph
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())

        # Assert the degree of each vertex in the undirected graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)

        # Assert the order and size of the directed graph
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())

        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices and edges
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)

        # Assert the order of the simple directed graph
        self.assertEqual(2, gSimple.getOrder())

    def testAddVertexAndEdge_test11_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)

        # Assert the order and size of the graph
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())

        # Assert the degree of each vertex in the undirected graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)

        # Assert the order and size of the directed graph
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())

        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices and an edge
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)

    def testAddVertexAndEdge_test10_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)

        # Assert the order and size of the graph
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())

        # Assert the degree of each vertex in the undirected graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)

        # Assert the order and size of the directed graph
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())

        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create a simple directed graph and add vertices
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)

    def testAddVertexAndEdge_test9_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)

        # Assert the order and size of the graph
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())

        # Assert the degree of each vertex in the undirected graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)

        # Assert the order and size of the directed graph
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())

        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create another directed mutable graph
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")

    def testAddVertexAndEdge_test8_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        # Build a complete graph with 50 vertices
        GraphUtils.buildCompleteGraph(50, g)
        # Assert the order (number of vertices) of the graph
        self.assertEqual(50, g.getOrder())
        # Assert the size (number of edges) of the graph
        self.assertEqual(1225, g.getSize())
        # Assert the degree of each vertex in the graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        # Build a complete graph with 50 vertices
        GraphUtils.buildCompleteGraph(50, gDirect)
        # Assert the order (number of vertices) of the graph
        self.assertEqual(50, gDirect.getOrder())
        # Assert the size (number of edges) of the graph
        self.assertEqual(2450, gDirect.getSize())
        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        # Create another directed mutable graph
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        # Create a labeled vertex with label "1"
        one = BaseLabeledVertex("1")

    def testAddVertexAndEdge_test7_decomposed(self) -> None:
        # Create an undirected mutable graph
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        # Build a complete graph with 50 vertices
        GraphUtils.buildCompleteGraph(50, g)
        # Assert the order (number of vertices) of the graph
        self.assertEqual(50, g.getOrder())
        # Assert the size (number of edges) of the graph
        self.assertEqual(1225, g.getSize())
        # Assert the degree of each vertex in the undirected graph
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        # Create a directed mutable graph
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        # Build a complete graph with 50 vertices
        GraphUtils.buildCompleteGraph(50, gDirect)
        # Assert the order (number of vertices) of the graph
        self.assertEqual(50, gDirect.getOrder())
        # Assert the size (number of edges) of the graph
        self.assertEqual(2450, gDirect.getSize())
        # Assert the degree of each vertex in the directed graph
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

    def testAddVertexAndEdge_test6_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        g_direct = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g_direct)
        self.assertEqual(50, g_direct.getOrder())
        self.assertEqual(2450, g_direct.getSize())

    def testAddVertexAndEdge_test5_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())

    def testAddVertexAndEdge_test4_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, gDirect)

    def testAddVertexAndEdge_test3_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

    def testAddVertexAndEdge_test2_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())

    def testAddVertexAndEdge_test1_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())

    def testAddVertexAndEdge_test0_decomposed(self) -> None:
        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(50, g)


class GraphInsert(TestRunner):

    __end: int = 0

    __start: int = 0

    __g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None

    def runTest(self) -> None:
        for i in range(self.__start, self.__end):
            v = BaseLabeledVertex(str(i))
            self.__g.addVertex(v)

        with threading.Lock():  # Using threading.Lock to mimic synchronized block
            vertices = self.__g.getVertices0()
            for v1 in vertices:
                for v2 in vertices:
                    if not v1.equals(v2):
                        try:
                            e = BaseLabeledEdge(f"{v1} -> {v2}")
                            self.__g.addEdge(v1, e, v2)
                        except GraphException:
                            pass

    def __init__(
        self, g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge], start: int, end: int
    ) -> None:
        self.__g = g
        self.__start = start
        self.__end = end
