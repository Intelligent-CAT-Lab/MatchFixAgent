from __future__ import annotations
import re
import io
import typing
from typing import *


class UncoloredOrderedVertices:

    __orderedVertices: typing.Dict[int, typing.Set[typing.Any]] = {}

    def size(self) -> int:
        return len(self.__orderedVertices)

    def iterator(self) -> typing.Iterator[typing.Any]:
        class CustomIterator:
            def __init__(
                self, ordered_vertices: typing.Dict[int, typing.Set[typing.Any]]
            ):
                self.keys = iter(ordered_vertices.keys())
                self.ordered_vertices = ordered_vertices
                self.pending = None
                self.next_item = None

            def __iter__(self):
                return self

            def __next__(self):
                if not self.has_next():
                    raise StopIteration()
                returned = self.next_item
                self.next_item = None
                return returned

            def has_next(self) -> bool:
                if self.next_item is not None:
                    return True

                while self.pending is None or not any(True for _ in self.pending):
                    try:
                        key = next(self.keys)
                        self.pending = iter(self.ordered_vertices[key])
                    except StopIteration:
                        return False

                self.next_item = next(self.pending)
                return True

            def remove(self):
                if self.pending is None:
                    raise Exception("No element to remove")
                # Python sets do not have a direct `remove` method for iterators,
                # so we need to remove the element from the set directly.
                self.pending = (item for item in self.pending if item != self.next_item)

        return CustomIterator(self.__orderedVertices)

    def compare(self, o1: int, o2: int) -> int:
        return (o2 > o1) - (o2 < o1)

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:
        vertices = self.__orderedVertices.get(degree)

        if vertices is None:
            vertices = set()

        vertices.add(v)
        self.__orderedVertices[degree] = vertices
