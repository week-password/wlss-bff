FROM python:3.11-slim

WORKDIR /wlss-bff

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install poetry==1.4.2

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install --with=app,test

COPY . ./
