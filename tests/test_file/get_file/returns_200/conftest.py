from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_file_request():
    return Predicate(method="GET", path="/files/d3bb68db-052f-4851-b74d-d9c884fd43df")


@pytest.fixture
def get_file_response():
    response_body = "image binary data"
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
