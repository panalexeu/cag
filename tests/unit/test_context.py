from cag.core.base import Context, ContextUnit


def test_context_merges():
    ctx1 = Context(
        ctx_units=[
            ContextUnit(
                content='hey!',
                page_n=0
            )
        ],
        name='root'
    )
    ctx2 = Context(
        ctx_units=[
            ContextUnit(
                content='hello, world!',
                page_n=2
            )
        ],
        name='test2'
    )

    ctx = ctx1.merge([ctx2])

    assert len(ctx.ctx_units) == 2
    assert ctx.ctx_units[0].content == 'hey!'
    assert ctx.ctx_units[0].metadata['page_n'] == 0
    assert ctx.ctx_units[0].metadata['name'] == 'root'

    assert ctx.ctx_units[1].content == 'hello, world!'
    assert ctx.ctx_units[1].metadata['page_n'] == 2
    assert ctx.ctx_units[1].metadata['name'] == 'test2'
