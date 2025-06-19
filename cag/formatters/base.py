from abc import ABC, abstractmethod
from typing import Any

from pathlib import Path

from cag.core.base import Context


class BaseCtxFormatter(ABC):
    """Interface, that defines methods to format ``Context``"""

    def __init__(
            self,
            ctx: Context,
    ):
        self.ctx = ctx

    @abstractmethod
    def __call__(self) -> Any:
        """Define formatting logic here."""
        pass

    @abstractmethod
    def save(self, path: Path, name: str | None = None) -> None:
        """Define storing logic here."""
        pass
