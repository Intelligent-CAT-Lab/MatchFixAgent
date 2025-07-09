from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class PlayersRank(ABC):

    def updateRanking(self, player: typing.Any, ranking: float) -> None:
        # Implementation of the method goes here
        pass

    def getRanking(self, player: typing.Any) -> float:
        return 0.0  # Replace with actual implementation
