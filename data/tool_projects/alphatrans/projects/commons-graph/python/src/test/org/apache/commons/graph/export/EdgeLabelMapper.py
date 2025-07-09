from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.graph.Mapper import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *


class EdgeLabelMapper(Mapper):

    __serialVersionUID: int = 20120728

    def map_(self, input_: BaseLabeledWeightedEdge[float]) -> str:
        return input_.getLabel()
