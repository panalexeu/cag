import os
from tempfile import NamedTemporaryFile
import pytest

from src.core.base import Context
from src.data_source.text_source import TextDataSource
from src.data_source.error import FileTypeError


@pytest.fixture()
def temp_file():
    with NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write('Hello, World!')

    yield tmp.name

    os.remove(tmp.name)


@pytest.fixture()
def temp_bin_file():
    with NamedTemporaryFile(mode='b+w', delete=False) as tmp:
        tmp.write(b'\x00\xff\x10BinaryData') # to make truly binary include non-ascii bytes (by ChatGPT)

    yield tmp.name

    os.remove(tmp.name)


def test_text_source_reads_text_file(temp_file):
    data_source = TextDataSource()

    res = data_source.__call__(path=temp_file)

    assert isinstance(res, Context)
    assert res.ctx_units[0].content == 'Hello, World!'


def test_text_source_raises_exc_bin_file(temp_bin_file):
    data_source = TextDataSource()

    with pytest.raises(FileTypeError) as e:
        res = data_source.__call__(path=temp_bin_file)
