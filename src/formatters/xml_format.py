from typing import Any
from xml.dom import minidom
import xml.etree.ElementTree as ET

from .base import BaseCtxFormatter
from ..core.base import Context


class XMLCtxFormatter(BaseCtxFormatter):
    def __call__(self, context: Context) -> str:
        root = ET.Element(
            'Context',
            attrib=context.metadata
        )

        for unit in context.ctx_units:
            elem = ET.SubElement(
                parent=root,
                tag='ContextUnit',
                attrib=unit.metadata
            )
            elem.text = unit.content

        xlm_str = ET.tostring(root)
        format_xml = minidom.parseString(xlm_str).toprettyxml()

        return format_xml
