from pathlib import Path

from magic import from_buffer

from .base import BaseDataSource
from ..core.base import Context, ContextUnit
from .error import FileTypeError


class TextDataSource(BaseDataSource):
    """
    Loads simple, non-binary, text files into ``Context``.

    Depends on ``python-magic`` package (libmagic).
    """

    def __call__(
            self,
            path: Path,
            **kwargs
    ) -> Context:
        """
        :param path: Path to a file.
        :return: ``Context`` as metadata ``filename`` is provided.
        """
        if not self._is_valid(path):
            raise FileTypeError(f'File: `{path}` is not a text file.')

        content = self._read(path)
        ctx_unit = ContextUnit(content)

        return Context(
            ctx_units=[ctx_unit],
            name=path.name
        )

    def _is_valid(self, path: Path, **kwargs) -> bool:
        with open(path, 'rb') as file:
            file_type = from_buffer(file.read(2048), mime=True)

        return 'text' in file_type

    def _read(self, path: Path, **kwargs) -> str:
        with open(path, 'r') as file:
            return file.read()
