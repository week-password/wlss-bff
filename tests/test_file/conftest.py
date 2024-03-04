from __future__ import annotations

import json

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_file_request():
    # mountebank doesn't have an ability to simulate uploading file request
    # so we just simulate only method, path and headers to match with actual request
    return Predicate(method="POST", path="/files", headers={"Authorization": "Bearer token"})


@pytest.fixture
def create_file_response():
    response_body = {
        "id": "d3bb68db-052f-4851-b74d-d9c884fd43df",
        "extension": "png",
        "mime_type": "image/png",
        "size": 17,
    }
    return Response(body=json.dumps(response_body), status_code=201, headers={"content-type": "application/json"})


@pytest.fixture
def get_file_request():
    return Predicate(
        method="GET",
        path="/files/d3bb68db-052f-4851-b74d-d9c884fd43df",
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_file_response():
    response_body = "image binary data"
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
