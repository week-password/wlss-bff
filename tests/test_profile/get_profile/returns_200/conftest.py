from __future__ import annotations

import jwt
import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def access_token():
    return jwt.encode({"account_id": 2}, key="some-secret-key")


@pytest.fixture
def get_account_request(access_token):
    return Predicate(method="GET", path="/accounts/1", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_account_response():
    response_body = {"id": 1, "login": "john_doe"}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_profile_request(access_token):
    return Predicate(method="GET", path="/accounts/1/profile", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_profile_response():
    response_body = {
        "account_id": 1,
        "avatar_id": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_friendships_request(access_token):
    return Predicate(method="GET", path="/accounts/2/friendships", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_account_friendships_response():
    return Response({"friendships": []}, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts/2/friendships/requests",
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_friendship_requests_response():
    return Response({"requests": []}, status_code=200, headers={"content-type": "application/json"})
