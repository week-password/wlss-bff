from __future__ import annotations

import jwt
import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def access_token():
    return jwt.encode({"account_id": 1}, key="some-secret-key")


@pytest.fixture
def search_profiles_request(access_token):
    return Predicate(method="POST", path="/profiles/search", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def search_profiles_response():
    response_body = {
        "profiles": [
            {
                "account_id": 1,
                "avatar_id": None,
                "description": None,
                "name": "John Doe",
            },
            {
                "account_id": 2,
                "avatar_id": None,
                "description": None,
                "name": "John Smith",
            },
            {
                "account_id": 3,
                "avatar_id": None,
                "description": None,
                "name": "John Bloggs",
            },
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_accounts_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts",
        query={"account_id": ["1", "2", "3"]},
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_accounts_response():
    response_body = {
        "accounts": [
            {"id": 1, "login": "john_doe"},
            {"id": 2, "login": "john_smith"},
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts/1/friendships/requests",
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_friendship_requests_response():
    return Response(body={"requests": []}, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_friendships_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts/1/friendships",
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_account_friendships_response(access_token):
    return Response(body={"friendships": []}, status_code=200, headers={"content-type": "application/json"})
