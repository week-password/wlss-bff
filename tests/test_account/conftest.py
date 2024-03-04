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


@pytest.fixture
def get_account_id_request():
    return Predicate(method="GET", path="/accounts/logins/john_doe/id", headers={"Authorization": "Bearer token"})


@pytest.fixture
def match_account_login_request():
    return Predicate(method="POST", path="/accounts/logins/match", body={"login": "john_doe"})


@pytest.fixture
def match_account_login_response():
    return Response(body=None, status_code=204)


@pytest.fixture
def match_account_email_request():
    return Predicate(method="POST", path="/accounts/emails/match", body={"email": "john.doe@mail.com"})


@pytest.fixture
def match_account_email_response():
    return Response(body=None, status_code=204)


@pytest.fixture
def get_account_id_response():
    response_body = {"id": 42}
    return Response(body=json.dumps(response_body), status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_id_404_response():
    response_body = {
        "resource": "Account",
        "description": "Requested resource not found.",
        "details": "Requested resource doesn't exist or has been deleted.",
    }
    return Response(body=json.dumps(response_body), status_code=404, headers={"content-type": "application/json"})
