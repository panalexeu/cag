from pathlib import Path

import pytest
from dotenv import load_dotenv

from cag.data_source.img_openai import ImgOpenAIDataSource


@pytest.fixture
def data_source():
    load_dotenv()
    yield ImgOpenAIDataSource(
        model='gpt-4.1-nano'
    )


def test_img_openai_datasource_extracts_content(data_source):
    res = data_source(path=Path('./tests/integr/assets/macintosh.png'), temperature=0)
    assert 'macintosh' in res.ctx_units[0].content.lower()
