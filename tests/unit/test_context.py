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

    ctx1.merge([ctx2])

    assert len(ctx1.ctx_units) == 2
    assert ctx1.ctx_units[1].content == 'hello, world!'
    assert ctx1.ctx_units[1].metadata['page_n'] == 2
    assert ctx1.ctx_units[1].metadata['name'] == 'test2'
