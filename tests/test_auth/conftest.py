from __future__ import annotations

import json

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_session_request():
    return Predicate(method="POST", path="/sessions", body={"login": "john_doe", "password": "qwerty123"})


@pytest.fixture
def create_session_response():
    response_body = {
        "session": {
            "id": "f6d7ccf6-8c66-4a78-8ecc-d91cba589263",
            "account_id": 1,
        },
        "tokens": {
            "access_token": "access token got from backend",
            "refresh_token": "refresh token got from backend",
        },
    }
    return Response(body=json.dumps(response_body), status_code=201, headers={"content-type": "application/json"})


@pytest.fixture
def refresh_tokens_request():
    return Predicate(
        method="POST",
        path="/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263/tokens",
        headers={"Authorization": "Bearer refresh-token"},
    )

@pytest.fixture
def refresh_tokens_response():
    response_body = {
        "access_token": "fresh access token got from backend",
        "refresh_token": "fresh refresh token got from backend",
    }
    return Response(body=json.dumps(response_body), status_code=201, headers={"content-type": "application/json"})


@pytest.fixture
def delete_session_request():
    return Predicate(method="DELETE", path="/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263")

@pytest.fixture
def delete_session_response():
    return Response(status_code=204, headers={"content-type": "application/json"})


@pytest.fixture
def delete_all_sessions_request():
    return Predicate(method="DELETE", path="/accounts/1/sessions", headers={"Authorization": "Bearer token"})


@pytest.fixture
def delete_all_sessions_response():
    return Response(status_code=204, headers={"content-type": "application/json"})
