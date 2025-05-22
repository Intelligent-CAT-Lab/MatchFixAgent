from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *


class VisitAlgorithmsSelector(ABC):

    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        return handler.depth_first_search()

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        # Implementation logic for applyingDepthFirstSearch0 goes here
        # Since the Java method is abstract, the Python method remains unimplemented
        pass

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:
        return handler.apply_breadth_first_search()

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:
        # Implementation of the breadth-first search algorithm would go here.
        # Since the Java method is abstract, we leave this as a placeholder.
        pass
