from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_friendship_request_request():
    request_body = {"sender_id": 1, "receiver_id": 2}
    return Predicate(
        method="POST",
        path="/friendships/requests",
        body=request_body,
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def create_friendship_request_response():
    response_body = {
        "id": 1,
        "created_at": "2024-02-28T17:25:38.795Z",
        "receiver_id": 2,
        "sender_id": 1,
        "status": "PENDING",
    }
    return Response(body=response_body, status_code=201, headers={"content-type": "application/json"})
