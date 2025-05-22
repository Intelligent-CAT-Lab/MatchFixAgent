from __future__ import annotations
import math
from math import *
import time
import re
import collections
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.collections.FibonacciHeapNode import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class FibonacciHeap:

    __minimumNode: FibonacciHeapNode[typing.Any] = None

    __markedNodes: int = 0
    __trees: int = 0
    __size: int = 0
    __comparator: typing.Callable[[typing.Any, typing.Any], int] = None

    __elementsIndex: typing.Set[typing.Any] = set()
    __LOG_PHI: float = math.log((1 + math.sqrt(5)) / 2)

    def toString(self) -> str:
        if self.__minimumNode is None:
            return "FibonacciHeap=[]"

        stack = [self.__minimumNode]
        buf = ["FibonacciHeap=["]

        while stack:
            curr = stack.pop()
            buf.append(str(curr))
            buf.append(", ")

            if curr.getChild() is not None:
                stack.append(curr.getChild())

            start = curr
            curr = curr.getRight()

            while curr != start:
                buf.append(str(curr))
                buf.append(", ")

                if curr.getChild() is not None:
                    stack.append(curr.getChild())

                curr = curr.getRight()

        buf.append("]")

        return "".join(buf)

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        raise NotImplementedError("Operation not supported")

    def toArray0(self) -> typing.List[typing.Any]:
        raise NotImplementedError("Unsupported operation")

    def size(self) -> int:
        return self.__size

    def retainAll(self, c: typing.Collection[typing.Any]) -> bool:
        raise NotImplementedError("Operation not supported")

    def removeAll(self, c: typing.Collection[typing.Any]) -> bool:
        raise NotImplementedError("Operation not supported")

    def remove1(self, o: typing.Any) -> bool:
        raise NotImplementedError("Operation not supported")

    def remove0(self) -> typing.Any:
        if self.isEmpty():
            raise RuntimeError()
        return self.poll()

    def potential(self) -> int:
        return self.__trees + 2 * self.__markedNodes

    def poll(self) -> typing.Any:
        if self.isEmpty():
            return None

        z = self.__minimumNode
        num_of_kids = z.get_degree()

        x = z.get_child()
        temp_right = None

        while num_of_kids > 0:
            temp_right = x.get_right()

            self.__moveToRoot(x)

            x.set_parent(None)

            x = temp_right
            num_of_kids -= 1

        z.get_left().set_right(z.get_right())
        z.get_right().set_left(z.get_left())

        if z == z.get_right():
            self.__minimumNode = None
        else:
            self.__minimumNode = z.get_right()
            self.__consolidate()

        self.__size -= 1

        minimum = z.get_element()
        self.__elementsIndex.remove(minimum)
        return minimum

    def peek(self) -> typing.Any:
        if self.isEmpty():
            return None

        return self.__minimumNode.getElement()

    def offer(self, e: typing.Any) -> bool:
        return self.add(e)

    def iterator(self) -> typing.Iterator[typing.Any]:
        raise NotImplementedError("Unsupported operation")

    def isEmpty(self) -> bool:
        return self._FibonacciHeap__minimumNode is None

    def element(self) -> typing.Any:
        if self.isEmpty():
            raise RuntimeError()
        return self.peek()

    def containsAll(self, c: typing.Collection[typing.Any]) -> bool:
        if c is None:
            return False

        for o in c:
            if not self.contains(o):
                return False

        return True

    def contains(self, o: typing.Any) -> bool:
        if o is None:
            return False
        return o in self.__elementsIndex

    def clear(self) -> None:
        self.__minimumNode = None
        self.__size = 0
        self.__trees = 0
        self.__markedNodes = 0
        self.__elementsIndex.clear()

    def addAll(self, c: typing.Collection[typing.Any]) -> bool:
        for element in c:
            self.add(element)
        return True

    def add(self, e: typing.Any) -> bool:
        Assertions.checkNotNull(
            e, "Null elements not allowed in this FibonacciHeap implementation.", []
        )

        node = FibonacciHeapNode(e)

        self.__moveToRoot(node)

        self.__size += 1

        self.__elementsIndex.add(e)

        return True

    @staticmethod
    def FibonacciHeap1() -> FibonacciHeap[typing.Any]:
        return FibonacciHeap(None)

    def __init__(
        self, comparator: typing.Callable[[typing.Any, typing.Any], int]
    ) -> None:
        self.__comparator = comparator

    def __moveToRoot(self, node: FibonacciHeapNode[typing.Any]) -> None:
        if self.isEmpty():
            self.__minimumNode = node
        else:
            # Remove node from its current position
            node.get_left().set_right(node.get_right())
            node.get_right().set_left(node.get_left())

            # Add node to the root list
            node.set_left(self.__minimumNode)
            node.set_right(self.__minimumNode.get_right())
            self.__minimumNode.get_right().set_left(node)
            self.__minimumNode.set_right(node)

            # Update the minimum node if necessary
            if self.__compare(node, self.__minimumNode) < 0:
                self.__minimumNode = node
        # Remove y from its sibling list
        y.get_left().set_right(y.get_right())
        y.get_right().set_left(y.get_left())

        # Make x the parent of y
        y.set_parent(x)

        # If x has no children, make y its child
        if x.get_child() is None:
            x.set_child(y)
            y.set_right(y)
            y.set_left(y)
        else:
            # Add y to the child list of x
            y.set_left(x.get_child())
            y.set_right(x.get_child().get_right())
            x.get_child().get_right().set_left(y)
            x.get_child().set_right(y)

        # Increase the degree of x
        x.increase_degree()

        # Mark y as unmarked
        y.set_marked(False)

        # Increment the count of marked nodes
        self._FibonacciHeap__markedNodes += 1

    def __cut(
        self, x: FibonacciHeapNode[typing.Any], y: FibonacciHeapNode[typing.Any]
    ) -> None:
        self.__moveToRoot(x)

        y.decrease_degree()
        x.set_parent(None)

        x.set_marked(False)
        self.__markedNodes -= 1

    def __consolidate(self) -> None:
        if self.isEmpty():
            return

        array_size = int(math.floor(math.log(self.__size) / self.__LOG_PHI)) + 1
        node_sequence: List[Optional[FibonacciHeapNode[Any]]] = [None] * array_size

        num_roots = 0
        x = self.__minimumNode

        if x is not None:
            num_roots += 1
            x = x.get_right()

            while x != self.__minimumNode:
                num_roots += 1
                x = x.get_right()

        while num_roots > 0:
            degree = x.get_degree()
            next_node = x.get_right()

            while node_sequence[degree] is not None:
                y = node_sequence[degree]

                if self.__compare(x, y) > 0:
                    x, y = y, x

                self.__link(y, x)
                node_sequence[degree] = None
                degree += 1

            node_sequence[degree] = x
            x = next_node
            num_roots -= 1

        self.__minimumNode = None

        for pointer in node_sequence:
            if pointer is None:
                continue
            if self.__minimumNode is None:
                self.__minimumNode = pointer
            else:
                self.__moveToRoot(pointer)
                if self.__compare(pointer, self.__minimumNode) < 0:
                    self.__minimumNode = pointer

    def __compare(
        self, o1: FibonacciHeapNode[typing.Any], o2: FibonacciHeapNode[typing.Any]
    ) -> int:
        if self.__comparator is not None:
            return self.__comparator(o1.get_element(), o2.get_element())

        o1_element = o1.get_element()
        o2_element = o2.get_element()

        if not isinstance(o1_element, typing.SupportsRichComparison):
            raise TypeError(f"Element {o1_element} does not support comparison")

        return (o1_element > o2_element) - (o1_element < o2_element)

    def __cascadingCut(self, y: FibonacciHeapNode[typing.Any]) -> None:
        z = y.get_parent()

        if z is not None:
            if not y.is_marked():
                y.set_marked(True)
                self.__markedNodes += 1
            else:
                self.__cut(y, z)
                self.__cascadingCut(z)
