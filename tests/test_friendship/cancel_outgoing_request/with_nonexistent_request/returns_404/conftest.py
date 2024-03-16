from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_friendship_requests_request():
    return Predicate(method="GET", path="/accounts/1/friendships/requests", headers={"Authorization": "Bearer token"})


@pytest.fixture
def get_friendship_requests_response_without_requests():
    return Response(body={"requests": []}, status_code=200, headers={"content-type": "application/json"})
