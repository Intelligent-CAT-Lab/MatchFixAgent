from __future__ import annotations
import re
import random
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class UniVsBiDijkstraBenchmarkTestCase:

    __weightOperations: OrderedMonoid[float] = None

    __vertices: typing.List[BaseLabeledVertex] = None

    __targetListBi: typing.List[BaseLabeledVertex] = None

    __targetListUni: typing.List[BaseLabeledVertex] = None

    __sourceListBi: typing.List[BaseLabeledVertex] = None

    __sourceListUni: typing.List[BaseLabeledVertex] = None

    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None

    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )

    __EDGES: int = 100000
    __NODES: int = 5000

    def testPerformUnidirectionalDijkstra(self) -> None:
        source = self.__sourceListUni.pop(
            0
        )  # Remove the first element from the source list
        target = self.__targetListUni.pop(
            0
        )  # Remove the first element from the target list

        try:
            path = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(source)
                .to(target)
                .applyingDijkstra(self.__weightOperations)
            )

            self.assertTrue(path.getSize() > 0)
            self.assertTrue(path.getWeight() > 0.0)
        except Exception as e:
            print(e)

    def testPerformBidirectionalDijkstra(self) -> None:
        source = self.__sourceListBi.pop(
            0
        )  # Remove the first element from the source list
        target = self.__targetListBi.pop(
            0
        )  # Remove the first element from the target list

        try:
            path = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(source)
                .to(target)
                .applyingBidirectionalDijkstra(self.__weightOperations)
            )

            self.assertTrue(path.getSize() > 0)
            self.assertTrue(path.getWeight() > 0.0)
        except Exception as e:
            print(e)

    @staticmethod
    def setUp() -> None:
        UniVsBiDijkstraBenchmarkTestCase.__weightOperations = (
            DoubleWeightBaseOperations()
        )

        UniVsBiDijkstraBenchmarkTestCase.__weightedEdges = (
            lambda input: input.getWeight()
        )

        class CustomGraphConnection(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        ):
            def __init__(self):
                super().__init__()
                self.r = Random()

            def addEdge(self, src: BaseLabeledVertex, dst: BaseLabeledVertex) -> bool:
                try:
                    self.addEdge(
                        BaseLabeledWeightedEdge(
                            f"{src} -> {dst}", 10.0 * self.r.random() + 1.0
                        )
                    ).from_(src).to(dst)
                    return True
                except GraphException:
                    return False

            def connect0(self) -> None:
                UniVsBiDijkstraBenchmarkTestCase.__vertices = []
                for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES):
                    v = BaseLabeledVertex(str(i))
                    self.addVertex(v)
                    UniVsBiDijkstraBenchmarkTestCase.__vertices.append(v)

                for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES - 1):
                    self.addEdge(
                        UniVsBiDijkstraBenchmarkTestCase.__vertices[i],
                        UniVsBiDijkstraBenchmarkTestCase.__vertices[i + 1],
                    )

                self.addEdge(
                    UniVsBiDijkstraBenchmarkTestCase.__vertices[
                        UniVsBiDijkstraBenchmarkTestCase.__NODES - 1
                    ],
                    UniVsBiDijkstraBenchmarkTestCase.__vertices[0],
                )

                maxEdges = max(
                    0,
                    UniVsBiDijkstraBenchmarkTestCase.__EDGES
                    - UniVsBiDijkstraBenchmarkTestCase.__NODES,
                )
                for _ in range(maxEdges):
                    while not self.addEdge(
                        UniVsBiDijkstraBenchmarkTestCase.__vertices[
                            self.r.randint(
                                0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1
                            )
                        ],
                        UniVsBiDijkstraBenchmarkTestCase.__vertices[
                            self.r.randint(
                                0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1
                            )
                        ],
                    ):
                        pass

        UniVsBiDijkstraBenchmarkTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            CustomGraphConnection()
        )

        UniVsBiDijkstraBenchmarkTestCase.__sourceListUni = []
        UniVsBiDijkstraBenchmarkTestCase.__targetListUni = []

        UniVsBiDijkstraBenchmarkTestCase.__sourceListBi = []
        UniVsBiDijkstraBenchmarkTestCase.__targetListBi = []

        r = Random()

        for _ in range(15):
            s = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                r.randint(0, len(UniVsBiDijkstraBenchmarkTestCase.__vertices) - 1)
            ]
            UniVsBiDijkstraBenchmarkTestCase.__sourceListUni.append(s)
            UniVsBiDijkstraBenchmarkTestCase.__sourceListBi.append(s)

            t = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                r.randint(0, len(UniVsBiDijkstraBenchmarkTestCase.__vertices) - 1)
            ]
            UniVsBiDijkstraBenchmarkTestCase.__targetListUni.append(t)
            UniVsBiDijkstraBenchmarkTestCase.__targetListBi.append(t)
