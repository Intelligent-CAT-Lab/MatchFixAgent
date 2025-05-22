from __future__ import annotations
import re
from abc import ABC
import io


class ProcessDestroyer(ABC):

    def size(self) -> int:
        return 0

    def remove(self, process: subprocess.Popen) -> bool:
        # Implement the logic to remove the process here
        # For now, returning False as a placeholder
        return False

    def add(self, process: subprocess.Popen) -> bool:
        return True  # Replace with actual implementation logic
