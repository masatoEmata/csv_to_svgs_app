import pytest

from app.services import csv_service


def test_detect_encoding():
    content = b"Some test content"
    assert csv_service.detect_encoding(content) == "ascii"


def test_detect_encoding_invalid_content():
    with pytest.raises(TypeError):
        csv_service.detect_encoding(None)


def test_read_csv():
    content = b"col1,col2,col3\nvalue1,value2,value3"
    encoding = "ascii"
    expected = [["col1", "col2", "col3"], ["value1", "value2", "value3"]]
    assert csv_service.read_csv(content, encoding) == expected


def test_read_csv_invalid_content():
    with pytest.raises(TypeError):
        csv_service.read_csv(None, "ascii")
