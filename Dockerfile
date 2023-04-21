FROM python:3.10-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./
# httpxのインストール先をsys.pathに追加
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages/"

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile --dev

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]
