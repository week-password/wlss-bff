FROM python:3.11-slim

WORKDIR /wlss-bff

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install poetry==1.4.2

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

# we also need to install 'test' dependencies here, because linters check tests code as well
# otherwise linters will report 'module not found' errors for tests code
RUN poetry install --with=app,lint,test

COPY . ./
