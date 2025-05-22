from __future__ import annotations
import re
import io


class LongUtil:

    @staticmethod
    def _longToBinaryWithLeading(l: int) -> str:
        return f"{l:064b}"
