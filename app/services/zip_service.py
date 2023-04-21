import zipfile
from io import BytesIO

from fastapi.responses import StreamingResponse

from app.domain.models import SVGRow


def create_svg_zip_buffer(csv_rows: list) -> BytesIO:
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for i, row in enumerate(csv_rows):
            svg_data = SVGRow(row).svg_data
            svg_filename = f"svg_file_{i}.svg"
            zip_file.writestr(svg_filename, svg_data)

    zip_buffer.seek(0)
    return zip_buffer


def create_zip_streaming_response(zip_buffer: BytesIO) -> StreamingResponse:
    if zip_buffer is None:
        raise TypeError("Zip buffer cannot be None")

    def iter_stream():
        yield from zip_buffer

    return StreamingResponse(
        iter_stream(),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=svgs.zip"},
    )
