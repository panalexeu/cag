from pathlib import Path

from cag.data_source.pdf import PDFDataSource


def test_pdf_source():
    data_source = PDFDataSource()

    res = data_source(Path('./tests/integr/assets/doc.pdf'))

    assert len(res.ctx_units) == 2
    assert res.ctx_units[0].metadata['page_num'] == 1
    assert res.ctx_units[1].metadata['page_num'] == 2
