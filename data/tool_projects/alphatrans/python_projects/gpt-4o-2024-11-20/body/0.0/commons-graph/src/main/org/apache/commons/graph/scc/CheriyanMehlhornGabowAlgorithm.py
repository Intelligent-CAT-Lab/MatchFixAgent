from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithm import *


class CheriyanMehlhornGabowAlgorithm(SccAlgorithm):

    __sscCounter: int = 0
    __preorderCounter: int = 0
    __p: typing.List[typing.Any] = []
    __s: typing.List[typing.Any] = []
    __sscId: typing.Dict[typing.Any, int] = {}

    __preorder: typing.Dict[typing.Any, int] = {}

    __marked: typing.Set[typing.Any] = set()
    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        # Perform DFS for each unmarked vertex
        for vertex in self.__graph.get_vertices0():
            if vertex not in self.__marked:
                self.__dfs(vertex)

        # Create a list of sets to store strongly connected components (SCCs) by index
        indexed_scc_components: typing.List[typing.Set[typing.Any]] = [
            set() for _ in range(self.__sscCounter)
        ]

        # Assign vertices to their respective SCCs based on sscId
        for w in self.__graph.get_vertices0():
            component = indexed_scc_components[self.__sscId[w]]
            component.add(w)

        # Convert the list of SCCs into a set of sets
        scc: typing.Set[typing.FrozenSet[typing.Any]] = {
            frozenset(component) for component in indexed_scc_components
        }
        return scc

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph

    def __dfs(self, vertex: typing.Any) -> None:
        self.__marked.add(vertex)
        self.__preorder[vertex] = self.__preorderCounter
        self.__preorderCounter += 1
        self.__s.append(vertex)
        self.__p.append(vertex)

        for w in self.__graph.get_connected_vertices(vertex):
            if w not in self.__marked:
                self.__dfs(w)
            elif self.__sscId.get(w) is None:
                while self.__p and self.__preorder[self.__p[-1]] > self.__preorder[w]:
                    self.__p.pop()

        if self.__p and self.__p[-1] == vertex:
            self.__p.pop()
            while True:
                w = self.__s.pop()
                self.__sscId[w] = self.__sscCounter
                if w == vertex:
                    break
            self.__sscCounter += 1
