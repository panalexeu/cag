import os

from magic import from_buffer

from .base import BaseDataSource
from ..core.base import Context, ContextUnit
from .error import FileTypeError


class TextDataSource(BaseDataSource):
    """
    Loads simple, non-binary, text files into ``Context``.

    Depends on ``python-magic`` package (libmagic).
    """

    def __call__(self, path: str, **kwargs) -> Context:
        """
        :param path: Path to a file.
        :return: ``Context`` as metadata ``filename`` is provided.
        """

        filename = path.split('/')[-1]

        if not self._is_text_file(path):
            raise FileTypeError(f'File: `{path}` is not a text file.')

        content = self._read_file(path)
        ctx_unit = ContextUnit(content)

        return Context(
            ctx_units=[ctx_unit],
            filename=filename
        )

    @staticmethod
    def _is_text_file(path: str) -> bool:
        with open(path, 'rb') as file:
            file_type = from_buffer(file.read(2048))

        return 'text' in file_type

    @staticmethod
    def _read_file(path: str) -> str:
        with open(path, 'r') as file:
            return file.read()
