import sys
from pathlib import Path

from fastapi import FastAPI

from app.routers import upload

sys.path.append(str(Path(__file__).resolve().parent.parent))

app = FastAPI()

app.include_router(upload.router)
