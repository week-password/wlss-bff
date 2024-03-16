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
def get_accounts_request():
    return Predicate(
        method="GET",
        path="/accounts",
        query={"account_id": [2, 5]},
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_accounts_response():
    response_body = {
        "accounts": [
            {
                "id": 2,
                "login": "john_smith",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_profiles_request():
    return Predicate(
        method="GET",
        path="/profiles",
        query={"account_id": [2, 5]},
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_profiles_response():
    response_body = {
        "profiles": [
            {
                "account_id": 2,
                "avatar_id": None,
                "description": "One more 'John' in out testing?",
                "name": "John Smith",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
