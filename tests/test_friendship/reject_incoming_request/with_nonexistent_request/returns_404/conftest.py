from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_friendship_requests_request():
    return Predicate(method="GET", path="/accounts/1/friendships/requests", headers={"Authorization": "Bearer token"})


@pytest.fixture
def get_friendship_requests_response_without_incoming_requests():
    response_body = {
        "requests": [
            {
                "id": 2,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 2,
                "sender_id": 1,
                "status": "PENDING",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
