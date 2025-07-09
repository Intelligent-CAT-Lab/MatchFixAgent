from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *
from src.main.org.apache.commons.graph.scc.TarjanVertexMetaInfo import *


class TarjanAlgorithm(SccAlgorithm):

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        vertices_meta_info: typing.Dict[typing.Any, TarjanVertexMetaInfo] = {}
        s: typing.List[typing.Any] = []
        strongly_connected_components: typing.Set[typing.Set[typing.Any]] = set()
        index = 0

        for vertex in self.__graph.getVertices0():
            vertex_meta_info = self.__getMetaInfo(vertex, vertices_meta_info)
            if vertex_meta_info.hasUndefinedIndex():
                strongly_connected_component: typing.Set[typing.Any] = set()
                self.__strongConnect(
                    self.__graph,
                    vertex,
                    vertices_meta_info,
                    s,
                    strongly_connected_component,
                    index,
                )
                strongly_connected_components.add(
                    frozenset(strongly_connected_component)
                )

        return strongly_connected_components

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph

    @staticmethod
    def __strongConnect(
        graph: DirectedGraph[typing.Any, typing.Any],
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
        s: typing.List[typing.Any],
        stronglyConnectedComponent: typing.Set[typing.Any],
        index: int,
    ) -> None:
        vertexMetaInfo = TarjanAlgorithm.__getMetaInfo(vertex, verticesMetaInfo)
        vertexMetaInfo.setIndex(index)
        vertexMetaInfo.setLowLink(index)
        index += 1
        s.append(vertex)

        for adjacent in graph.getOutbound(vertex):
            adjacentMetaInfo = TarjanAlgorithm.__getMetaInfo(adjacent, verticesMetaInfo)
            if adjacentMetaInfo.hasUndefinedIndex():
                TarjanAlgorithm.__strongConnect(
                    graph,
                    adjacent,
                    verticesMetaInfo,
                    s,
                    stronglyConnectedComponent,
                    index,
                )
                vertexMetaInfo.setLowLink(
                    min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getLowLink())
                )
            elif adjacent in s:
                vertexMetaInfo.setLowLink(
                    min(vertexMetaInfo.getLowLink(), adjacentMetaInfo.getIndex())
                )

        if vertexMetaInfo.getLowLink() == vertexMetaInfo.getIndex():
            component = set()
            while True:
                v = s.pop()
                component.add(v)
                if v == vertex:
                    break
            stronglyConnectedComponent.update(component)

    @staticmethod
    def __getMetaInfo(
        vertex: typing.Any,
        verticesMetaInfo: typing.Dict[typing.Any, TarjanVertexMetaInfo],
    ) -> TarjanVertexMetaInfo:
        vertexMetaInfo = verticesMetaInfo.get(vertex)
        if vertexMetaInfo is None:
            vertexMetaInfo = TarjanVertexMetaInfo()
            verticesMetaInfo[vertex] = vertexMetaInfo
        return vertexMetaInfo
