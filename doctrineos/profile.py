from pathlib import Path
from typing import Any, Dict

from doctrine import Doctrine


class DoctrineOSProfile:
    def __init__(self, path: str):
        self.path = Path(path)
        self.doctrine = Doctrine.load(self.path)
        self.receipt: Dict[str, Any] = self.doctrine.mount()

    @property
    def name(self) -> str:
        return self.doctrine.name

    @property
    def context_sha256(self) -> str:
        return str(self.receipt.get("context_sha256", ""))
