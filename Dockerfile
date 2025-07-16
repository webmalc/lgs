FROM python:3.13

RUN pip install uv

WORKDIR /app

COPY . .

RUN uv sync --all-extras --dev