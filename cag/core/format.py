from abc import ABC, abstractmethod
from typing import Any

from .base import Context


class BaseCtxFormatter(ABC):
    """Interface, that defines methods to format ``Context``"""

    @abstractmethod
    def __call__(self, context: Context) -> Any:
        pass
