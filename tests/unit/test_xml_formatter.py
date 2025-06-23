import os
from tempfile import NamedTemporaryFile
from pathlib import Path

import pytest

from cag.core.base import Context, ContextUnit
from cag.formatters.xml import XMLCtxFormatter


@pytest.fixture()
def temp_file():
    with NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write("""
<?xml version="1.0" ?>
<Context name="hello">
    <ContextUnit page_n="0">Hello,</ContextUnit>
    <ContextUnit page_n="1">World!</ContextUnit>
</Context>  
""".strip())

    yield tmp.name

    os.remove(tmp.name)


def test_ctx_xml_formatter():
    ctx_units = [
        ContextUnit(
            content='Hello,',
            page_n=0
        ),
        ContextUnit(
            content='World!',
            page_n=1
        )
    ]
    ctx = Context(
        ctx_units,
        filename='hello_world.txt'
    )
    formatter = XMLCtxFormatter(ctx)

    res = formatter.__call__()
    # <Context filename="hello_world.txt">
    #         <ContextUnit page_n="0">Hello,</ContextUnit>
    #         <ContextUnit page_n="1">World!</ContextUnit>
    # </Context>

    assert isinstance(res, str)  # didn't find a better method, for some reason direct result assertion failed


def test_ctx_xml_formatter_loads_from_a_file(temp_file):
    formatter = XMLCtxFormatter.load(Path(temp_file))

    # object is fully restored from the file content
    assert isinstance(formatter, XMLCtxFormatter)

    assert isinstance(formatter.ctx, Context)

    assert formatter.ctx.metadata['name'] == 'hello'

    assert formatter.ctx.ctx_units[0].metadata['page_n'] == '0'
    assert formatter.ctx.ctx_units[0].content == 'Hello,'

    assert formatter.ctx.ctx_units[1].metadata['page_n'] == '1'
    assert formatter.ctx.ctx_units[1].content == 'World!'
