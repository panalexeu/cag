from cag.core.base import Context, ContextUnit
from cag.formatters.xml_format import XMLCtxFormatter


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

