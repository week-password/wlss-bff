from __future__ import annotations

import json

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def create_account_request():
    request_body = {
        "account": {
            "email": "john.doe@mail.com",
            "login": "john_doe",
            "password": "qwerty123",
        },
        "profile": {
            "name": "John Doe",
            "description": "I'm the best guy for your mocks.",
        },
    }
    return Predicate(method="POST", path="/accounts", body=request_body)


@pytest.fixture
def create_account_response():
    response_body = {
        "account": {
            "id": 42,
            "created_at": "2024-02-28T17:25:38.795Z",
            "email": "john.doe@mail.com",
            "login": "john_doe",
        },
        "profile": {
            "account_id": 42,
            "avatar_id": None,
            "description": "I'm the best guy for your mocks.",
            "name": "John Doe",
        },
    }
    return Response(body=json.dumps(response_body), status_code=201, headers={"content-type": "application/json"})
