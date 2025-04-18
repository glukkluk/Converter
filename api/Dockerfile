FROM python:3.12-alpine

WORKDIR /api

COPY pyproject.toml uv.lock .python-version ./


RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync --no-dev

COPY . .

EXPOSE 8000

CMD [ "uv", "run", "manage.py", "runserver", "0.0.0.0:8000" ]