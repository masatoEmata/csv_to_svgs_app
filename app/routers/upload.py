from fastapi import APIRouter, File, Request, UploadFile
from fastapi.templating import Jinja2Templates

from app.services import csv_service, zip_service
from app.services.svgs_to_csv import SvgsToCsvService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", include_in_schema=False)
@router.get("/csv_to_svgs/form", include_in_schema=False)
async def csv_to_svgs_form(request: Request):
    return templates.TemplateResponse("form_csv_to_svgs.html", {"request": request})


@router.get("/svgs_to_csv/form", include_in_schema=False)
async def svgs_to_csv_form(request: Request):
    return templates.TemplateResponse("form_svgs_to_csv.html", {"request": request})


@router.post("/upload/csv_to_svgs")
async def csv_to_svgs(csv_file: UploadFile = File(...)):
    content = await csv_file.read()
    encoding = csv_service.detect_encoding(content)
    csv_rows = csv_service.read_csv(content, encoding)
    svg_zip_buffer = zip_service.create_svg_zip_buffer(csv_rows)

    return zip_service.create_zip_streaming_response(svg_zip_buffer)


@router.post("/upload/svgs_to_csv")
async def svgs_to_csv(files: list[UploadFile] = File(...)):
    return await SvgsToCsvService(files).svgs_to_csv()
