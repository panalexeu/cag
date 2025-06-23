from typing import Any
from pathlib import Path

from magic import from_file
import pymupdf
from pymupdf import Page
from pymupdf4llm import to_markdown

from .base import BaseDataSource
from ..core.base import Context, ContextUnit
from .error import FileTypeError


class PDFDataSource(BaseDataSource):
    """
    Loads PDFs into ``Context``.

    Depends on ``python-magic`` and ``PyMuPDF``.
    """

    def __call__(self, path: Path, **kwargs) -> Context:
        if not self._is_valid(path):
            raise FileTypeError(f'File: `{path}` is not a valid PDF.')

        ctx_units = self._read(path)

        return Context(
            ctx_units=ctx_units,
            name=path.name
        )

    def _is_valid(self, path: Path, **kwargs) -> bool:
        file_type = from_file(path, mime=True)
        return 'pdf' in file_type

    def _read(self, path: Path, **kwargs) -> list[ContextUnit]:
        ctx_units = []

        with pymupdf.open(path) as doc:
            for page_num, page in enumerate(doc, start=1):
                page_content = page.get_text()
                proc_content = self._page_content_proc(page_content)

                ctx_units.append(
                    ContextUnit(
                        content=proc_content,
                        page_num=page_num
                    )
                )

        return ctx_units

    @staticmethod
    def _page_content_proc(content: str) -> str:
        return content.strip()
