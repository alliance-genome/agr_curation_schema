###############################################
# Base Image
###############################################
FROM python:3.12-slim AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_PROJECT_ENVIRONMENT="/src/.venv" \
    UV_LINK_MODE=copy

# prepend the project venv to path
ENV PATH="/src/.venv/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base AS builder-base
RUN apt-get update \
    && apt-get install -y make git curl less emacs \
    && apt-get install --no-install-recommends -y \
    build-essential

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy project requirement files here to ensure they will be cached.
WORKDIR /src
COPY Makefile pyproject.toml uv.lock README.md ./
COPY . .

CMD ["uv", "sync"]
