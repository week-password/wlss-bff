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
