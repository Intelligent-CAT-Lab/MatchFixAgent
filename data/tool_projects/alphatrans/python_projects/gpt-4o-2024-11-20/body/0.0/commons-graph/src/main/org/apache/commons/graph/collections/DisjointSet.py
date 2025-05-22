from __future__ import annotations
import re
import collections
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.collections.DisjointSetNode import *


class DisjointSet:

    __disjointSets: typing.Dict[typing.Any, DisjointSetNode[typing.Any]] = {}

    def union(self, e1: typing.Any, e2: typing.Any) -> None:
        e1_root = self.__find0(self.__getNode(e1))
        e2_root = self.__find0(self.__getNode(e2))

        if e1_root == e2_root:
            return

        comparison = e1_root.compare_to(e2_root)
        if comparison < 0:
            e2_root.set_parent(e1_root)
        elif comparison > 0:
            e1_root.set_parent(e2_root)
        else:
            e2_root.set_parent(e1_root)
            e1_root.increase_rank()

    def find1(self, e: typing.Any) -> typing.Any:
        node = self.__find0(self.__getNode(e))

        if node == node.get_parent():
            return node.get_element()

        node.set_parent(self.__find0(node.get_parent()))

        return node.get_parent().get_element()

    def __getNode(self, e: typing.Any) -> DisjointSetNode[typing.Any]:
        node = self.__disjointSets.get(e)

        if node is None:
            node = DisjointSetNode(e)
            self.__disjointSets[e] = node

        return node

    def __find0(self, node: DisjointSetNode[typing.Any]) -> DisjointSetNode[typing.Any]:
        if node == node.get_parent():
            return node
        return self.__find0(node.get_parent())
