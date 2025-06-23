class ContextUnit:
    """
    Represents one context unit in a ``CachedContext``.

    Could be a PDF document page, presentation slide, image, etc.

    Stores unit's content and metadata information.
    """

    def __init__(
            self,
            content: str,
            **kwargs
    ):
        self.content = content
        self.metadata = kwargs

    def __repr__(self):
        prefix = '<ContextUnit'

        for key, val in self.metadata.items():
            prefix += f' {key}="{val}",'

        format_content = self.content[:64].replace('\n', ' ')

        prefix += f' content="{format_content}...">'

        return prefix


class Context:
    """
    Represents context of a whole document.

    Consists of ``ContextUnit``'s. Also stores metadata.
    """

    def __init__(
            self,
            ctx_units: list[ContextUnit],
            **kwargs
    ):
        self.ctx_units = ctx_units
        self.metadata = kwargs

    def __repr__(self):
        prefix = '<Context'

        # metadata fields
        for key, val in self.metadata.items():
            prefix += f' {key}="{val}"'

        # ctx units
        prefix += ' ctx_units=['

        for i, unit in enumerate(self.ctx_units):
            if i == len(self.ctx_units) - 1:
                prefix += f'{str(unit)}]>'
                break

            prefix += f'{str(unit)}, '

        return prefix

