from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.me.lemire.longcompression.synth.LongUniformDataGenerator import *


class LongClusteredDataGenerator:

    unidg: LongUniformDataGenerator = LongUniformDataGenerator(1, 0)

    def __init__(self) -> None:
        pass
