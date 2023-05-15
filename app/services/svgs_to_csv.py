import csv
import io

from bs4 import BeautifulSoup
from fastapi import File, UploadFile
from fastapi.responses import StreamingResponse


class SvgsToCsvService:
    def __init__(self, files: list[UploadFile] = File(...)):
        self.__files = files

    async def make_base_rows(self):
        rows = []
        for file in self.__files:
            content = await file.read()
            soup = BeautifulSoup(content, "xml")

            svg_header = soup.svg.prettify()
            paths = soup.find_all("path")
            for path in paths:
                svg_header = svg_header.replace(str(path), "")

            paths = [str(path) for path in paths]

            rows.append(
                [svg_header.replace("\n", "")]
                + [path.replace("\n", "") for path in paths]
            )
        return rows

    def write_csv_with_end_tag(self, rows, writer):
        for row in rows:
            row.append("</svg>")
            writer.writerow(row)

    async def svgs_to_csv(self):
        output = io.StringIO()

        writer = csv.writer(output)
        rows = await self.make_base_rows()
        self.write_csv_with_end_tag(rows, writer)
        output.seek(0)  # go back to the start of the StringIO object
        return StreamingResponse(iter(output), media_type="text/csv")
