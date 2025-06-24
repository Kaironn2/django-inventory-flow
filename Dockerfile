FROM python:3.13.3-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock /_lock/

RUN --mount=type=cache,target=/root/.cache/uv \
    cd /_lock && \
    uv sync --locked --no-install-project

COPY . /app
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

RUN uv run src/manage.py migrate

CMD ["uv", "run", "src/manage.py", "runserver", "0.0.0.0:8000"]
