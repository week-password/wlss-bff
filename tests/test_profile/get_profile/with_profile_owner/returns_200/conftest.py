from __future__ import annotations

import jwt
import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def access_token_of_profile_owner():
    return jwt.encode({"account_id": 1}, key="some-secret-key")


@pytest.fixture
def get_account_request_from_account_owner(access_token_of_profile_owner):
    return Predicate(
        method="GET",
        path="/accounts/1",
        headers={"Authorization": f"Bearer {access_token_of_profile_owner}"},
    )


@pytest.fixture
def get_account_response_for_account_owner():
    response_body = {"id": 1, "login": "john_doe"}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_profile_request_from_profile_owner(access_token_of_profile_owner):
    return Predicate(
        method="GET",
        path="/accounts/1/profile",
        headers={"Authorization": f"Bearer {access_token_of_profile_owner}"},
    )


@pytest.fixture
def get_profile_response_for_profile_owner():
    response_body = {
        "account_id": 1,
        "avatar_id": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
