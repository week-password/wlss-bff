# WLSS BFF

Backend For Frontend application for [Wish List Sharing Service](https://github.com/week-password/wisher).


## Table of Contents

[System requirements](#system-requirements)

[First time setup](#first-time-setup)

[Run app](#run-app)

[Run linters](#run-linters)

[Run tests](#run-tests)


***


## [System requirements](#table-of-contents)

To develop this project you need to have the following software installed.

- [Poetry 1.4.2](https://python-poetry.org/docs/)
- [Python](https://www.python.org/) (see version in `pyproject.toml` file)


## [First time setup](#table-of-contents)

Before start to setup project you have to meet [System requirements](#system-requirements).

Go to the project root directory.

1. Set up local environment:
```bash
# Set up git user for this repository
# change values below to your name and email
git config user.name "John Doe"
git config user.email "john.doe@mail.com"

# Create virtual environment and install dependencies.
poetry install --with app,lint,test

# Activate virtual environment.
poetry shell
```

2. Upgrade pip within virtual environment:
```bash
pip install --upgrade pip
```


## [Run app](#table-of-contents)

To run application you need to do all steps from [First time setup](#first-time-setup) section.

1. Run app:
```bash
# Run development server.
WLSS_ENV=local/dev uvicorn src.app:app --reload
```

2. Check application health status:
```bash
curl --request GET http://localhost:8000/health
```


## [Run linters](#table-of-contents)

To run linters you need to do all steps from [First time setup](#first-time-setup) section.

Linters order below is a preferred way to run and fix them one by one.

Run any linter you need or all of them at once:
```bash
# Run mypy.
mypy

# Run ruff.
ruff check src tests

# Run flake8.
flake8
```


## [Run tests](#table-of-contents)

To run tests you need to do all steps from [First time setup](#first-time-setup) section.

1. Run services and tests:
```bash
# Run pytest.
pytest --cov=src
```

Also you can choose one of the following ways of running tests:

- Tests with html coverage report:
```bash
pytest --cov=src ; coverage html
```

- Tests with execution contexts in report:
```bash
pytest --cov=src --cov-context=test ; coverage html --show-contexts --no-skip-covered
```
