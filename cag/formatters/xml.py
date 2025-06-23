import xml.etree.ElementTree as ET
from typing import Self
from xml.dom import minidom

from pathlib import Path

from .base import BaseCtxFormatter
from ..core.base import Context, ContextUnit


class XMLCtxFormatter(BaseCtxFormatter):
    """Formats ``Context`` into unified XML, text file."""

    def __init__(
            self,
            ctx: Context,
    ):
        super().__init__(ctx)

    @classmethod
    def load(cls, path: Path) -> Self:
        with open(path, 'r') as file:
            xml_str = file.read()

        root: ET.Element = ET.fromstring(xml_str)

        # instantiate ContextUnit's
        ctx_units = []
        for child in root:
            ctx_units.append(
                ContextUnit(
                    child.text,
                    **child.attrib
                )
            )

        # instantiate Context
        ctx = Context(
            ctx_units,
            **root.attrib
        )

        return XMLCtxFormatter(ctx=ctx)

    def __call__(self) -> str:
        root = ET.Element(
            'Context',
            attrib=self._serialize_metadata(self.ctx.metadata)
        )

        for unit in self.ctx.ctx_units:
            elem = ET.SubElement(
                root,
                'ContextUnit',
                attrib=self._serialize_metadata(unit.metadata)
            )
            elem.text = unit.content

        xlm_str = ET.tostring(root)
        self.format_ctx = minidom.parseString(xlm_str).toprettyxml()

        return self.format_ctx

    @staticmethod
    def _serialize_metadata(metadata: dict) -> dict:
        for key, val in metadata.items():
            metadata[key] = str(val)

        return metadata

    def save(self, path: Path, name: str | None = None) -> None:
        """
        :param name: Storing ``Context`` name without extension.
        :param path: Storing directory.
        """
        if not name:
            name = self.ctx.metadata.get('name')

        with open(path.joinpath(name + '.xml'), 'w') as file:
            file.write(self.format_ctx)
