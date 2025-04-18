FROM python:3.12-alpine

WORKDIR /bot

COPY pyproject.toml uv.lock .python-version ./

RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync --no-dev

COPY . .

EXPOSE 5050

CMD [ "uv", "run", "--no-dev", "main.py" ]