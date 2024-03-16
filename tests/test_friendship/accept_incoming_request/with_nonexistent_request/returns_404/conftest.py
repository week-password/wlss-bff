from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_friendship_requests_request():
    return Predicate(method="GET", path="/accounts/1/friendships/requests", headers={"Authorization": "Bearer token"})


@pytest.fixture
def get_friendship_requests_response():
    response_body = {
        "requests": [
            {
                "id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 1,
                "sender_id": 3,
                "status": "PENDING",
            },
            {
                "id": 2,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 2,
                "sender_id": 1,
                "status": "PENDING",
            },

            {
                "id": 3,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 4,
                "sender_id": 1,
                "status": "REJECTED",
            },
            {
                "id": 4,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 5,
                "sender_id": 1,
                "status": "PENDING",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def accept_friendship_request_request():
    return Predicate(method="PUT", path="/friendships/requests/1/accepted", headers={"Authorization": "Bearer token"})


@pytest.fixture
def accept_friendship_request_response():
    response_body = {
        "friendships": [
            {
                "account_id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 3,
            },
            {
                "account_id": 3,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 1,
            },
        ],
    }
    return Response(body=response_body, status_code=201, headers={"content-type": "application/json"})
