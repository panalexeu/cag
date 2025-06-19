class ContextUnit:
    """
    Represents one context unit in a CachedContext.

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


class Contex:
    """
    Represents context of a whole document.

    Consists of ContextUnits. Also stores metadata.
    """

    def __init__(
            self,
            ctx_units: list[ContextUnit],
            **kwargs
    ):
        self.ctx_units = ctx_units
        self.metadata = kwargs
