from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_health_request():
    return Predicate(method="GET", path="/health")


@pytest.fixture
def get_health_response():
    response_body = {"status": "OK"}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
