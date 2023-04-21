from fastapi import APIRouter, File, Request, UploadFile
from fastapi.templating import Jinja2Templates

from app.services import csv_service, zip_service

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", include_in_schema=False)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload_form.html", {"request": request})


@router.post("/upload")
async def upload_file(csv_file: UploadFile = File(...)):

    content = await csv_file.read()
    encoding = csv_service.detect_encoding(content)
    csv_rows = csv_service.read_csv(content, encoding)
    svg_zip_buffer = zip_service.create_svg_zip_buffer(csv_rows)

    return zip_service.create_zip_streaming_response(svg_zip_buffer)
