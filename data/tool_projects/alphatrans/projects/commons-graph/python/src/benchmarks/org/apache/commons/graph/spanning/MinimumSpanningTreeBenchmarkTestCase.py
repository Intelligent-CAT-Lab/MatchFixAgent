from __future__ import annotations
import re
import io
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class MinimumSpanningTreeBenchmarkTestCase:

    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None

    __graph: UndirectedMutableGraph[
        BaseLabeledVertex, BaseLabeledWeightedEdge[float]
    ] = None

    __EDGES: int = 6000
    __NODES: int = 1000

    def testPerformPrim(self) -> None:
        actual = (
            CommonsGraph.minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingPrimAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertTrue(actual.getSize() > 0)

    def testPerformKruskal(self) -> None:
        actual = (
            CommonsGraph.minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertTrue(actual.getSize() > 0)

    def testPerformBoruvka(self) -> None:
        actual = (
            minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertTrue(actual.getSize() > 0)

    @staticmethod
    def setUp() -> None:
        MinimumSpanningTreeBenchmarkTestCase.__weightedEdges = Mapper(
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
                            f"{src} -> {dst}", float(self.r.nextInt(10))
                        )
                    ).from_(src).to(dst)
                    return True
                except GraphException:
                    return False

            def connect0(self) -> None:
                vertices = []
                for i in range(MinimumSpanningTreeBenchmarkTestCase.__NODES):
                    v = BaseLabeledVertex(str(i))
                    self.addVertex(v)
                    vertices.append(v)

                for i in range(MinimumSpanningTreeBenchmarkTestCase.__NODES - 1):
                    self.addEdge(vertices[i], vertices[i + 1])

                self.addEdge(
                    vertices[MinimumSpanningTreeBenchmarkTestCase.__NODES - 1],
                    vertices[0],
                )

                maxEdges = max(
                    0,
                    MinimumSpanningTreeBenchmarkTestCase.__EDGES
                    - MinimumSpanningTreeBenchmarkTestCase.__NODES,
                )
                for _ in range(maxEdges):
                    while not self.addEdge(
                        vertices[
                            self.r.nextInt(MinimumSpanningTreeBenchmarkTestCase.__NODES)
                        ],
                        vertices[
                            self.r.nextInt(MinimumSpanningTreeBenchmarkTestCase.__NODES)
                        ],
                    ):
                        pass

        MinimumSpanningTreeBenchmarkTestCase.__graph = (
            CommonsGraph.newUndirectedMutableGraph(CustomGraphConnection())
        )
