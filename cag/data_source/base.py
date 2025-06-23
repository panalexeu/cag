from typing import Any
from abc import ABC, abstractmethod

from cag.core.base import Context


class BaseDataSource(ABC):
    """
    Interface, that defines methods to load data sources into ``Context``.
    """

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Context:
        """Defines data source ``Context`` extraction logic."""
        pass

    @staticmethod
    def _is_valid(self, *args, **kwargs) -> bool:
        """Defines data source validation logic."""
        pass

    @staticmethod
    def _read(self, *args, **kwargs) -> Any:
        """Defines data source reading logic."""
        pass
