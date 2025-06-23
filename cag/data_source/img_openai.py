import os
from pathlib import Path
from base64 import b64encode

from magic import from_file
from openai import OpenAI

from .base import BaseDataSource
from .error import FileTypeError
from ..core.base import Context


class ImgOpenAIDataSource(BaseDataSource):
    """
    Describes and extracts image information by calling OpenAI API into ``Context``.

    Depends on ``openai`` and ``python-magic`` packages.
    """

    def __init__(
            self,
            model: str,
            api_key: str | None = None,
            **kwargs
    ):
        self.model = model
        self.api_key = api_key
        self.sync_client = OpenAI(
            api_key=api_key if api_key else os.environ.get('OPENAI_API_KEY'),
            **kwargs
        )

    def __call__(self, path: Path, **kwargs) -> Context:
        if not self._is_valid(path):
            raise FileTypeError(f'File: `{path}` is not a valid image file.')

        content = self._read(path)

        # request to openai
        res = self.sync_client.chat.completions.create(
            model=self.model,
            messages=[{
                'role': 'system',
                'content': [
                    {'type': 'text', 'text': self.sys_prompt},
                    {
                        'type': 'image_url',
                        'image_url': {
                            'url': self._form_img_url(path=path, b64=content)
                        }
                    }
                ]
            }]
        )

        return res.choices[0].message.content

    def _is_valid(self, path: Path, **kwargs) -> bool:
        file_type = from_file(path, mime=True)
        return file_type.startswith('image/')

    def _read(self, path: Path, **kwargs) -> str:
        with open(path, 'rb') as file:
            enc = b64encode(file.read())
            b64_str = enc.decode('utf-8')

            return b64_str

    @staticmethod
    def _form_img_url(path: Path, b64: str) -> str:
        return f'data:image/{path.suffix};base64,{b64}'

    @property
    def sys_prompt(self) -> str:
        return """You are a helpful AI assistant.
Provide a detailed, concise description of what is depicted in the image.
Additionally, include any quoted or visible text content in the image to extract the full context.
"""
