from abc import ABC, abstractmethod

from src.core.base import Context


class BaseDataSource(ABC):
    """
    Interface, that defines methods to load data sources into `Context`.
    """

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Context:
        pass
