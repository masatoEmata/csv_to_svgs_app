import csv
import zipfile
from io import BytesIO, StringIO

from chardet.universaldetector import UniversalDetector
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def upload_form():
    return """
    <html>
        <head>
            <title>CSV to SVG converter</title>
        </head>
        <body>
            <h1>CSV to SVG converter</h1>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="csv_file" type="file" accept=".csv">
                <button type="submit">Upload</button>
            </form>
        </body>
    </html>
    """


@app.post("/upload")
async def upload_file(csv_file: UploadFile = File(...)):
    content = await csv_file.read()

    detector = UniversalDetector()
    detector.feed(content)
    detector.close()
    encoding = detector.result["encoding"]

    content_str = content.decode(encoding)
    reader = csv.reader(StringIO(content_str), delimiter=",", quotechar='"')

    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for i, row in enumerate(reader):
            svg_data = row[0]
            svg_filename = f"svg_file_{i}.svg"
            zip_file.writestr(svg_filename, svg_data)

    zip_buffer.seek(0)

    def iter_stream():
        yield from zip_buffer

    response = StreamingResponse(iter_stream(), media_type="application/zip")
    response.headers["Content-Disposition"] = "attachment; filename=svg_files.zip"
    return response
