# python version
FROM python:3.10-slim

#  copy code, pipfile
WORKDIR /app/
COPY . /app/

# init apt-get and default installs
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    gcc

#  create pipenv environment
RUN pip install pipenv
# RUN python3 -m venv /opt/venv \
#     && /opt/venv/bin/python -m pip install pip --upgrade \
#     && /opt/venv/bin/python -m pip install -r requirements.txt

# Install dependencies in pipenv
RUN pipenv install --system --ignore-pipfile

# Cleanup
RUN apt-get remove -y --purge build-essential python3-dev gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# entrypoint
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["bash", "entrypoint.sh"]
