#!/bin/bash

APP_PORT=${PORT:-8000}  # default port 8000
cd /app/
gunicorn -k uvicorn.workers.UvicornWorker -t 3600 app.main:app --bind "0.0.0.0:${APP_PORT}"
# /opt/venv/bin/gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind "0.0.0.0:${APP_PORT}"
