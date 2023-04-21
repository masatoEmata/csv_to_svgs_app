import io
import zipfile

import pytest

from app.services import zip_service


def test_create_svg_zip_buffer():
    csv_rows = [["test1", "test2", "test3"]]
    zip_buffer = zip_service.create_svg_zip_buffer(csv_rows)
    assert isinstance(zip_buffer, io.BytesIO)


def test_create_zip_streaming_response():
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("test.txt", "test content")
    response = zip_service.create_zip_streaming_response(zip_buffer)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/zip"
    assert response.headers["Content-Disposition"] == "attachment; filename=svgs.zip"


def test_create_zip_streaming_response_invalid_buffer():
    with pytest.raises(TypeError):
        zip_service.create_zip_streaming_response(None)
