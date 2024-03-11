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
def get_account_by_login_request():
    return Predicate(
        method="GET",
        path="/accounts",
        query={"account_login": "john_doe"},
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_account_by_login_response():
    response_body = {
        "accounts": [
            {"id": 1, "login": "john_doe"},
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_by_login_response_with_nonexistent_account():
    response_body = {"accounts": []}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_accounts_request_for_two_accounts():
    return Predicate(
        method="GET",
        path="/accounts",
        query={"account_id": "1", "account_login": "john_smith"},
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_accounts_response_for_two_accounts():
    response_body = {
        "accounts": [
            {"id": 1, "login": "john_doe"},
            {"id": 2, "login": "john_smith"},
        ],
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def match_account_login_request():
    return Predicate(method="POST", path="/accounts/logins/match", body={"login": "john_doe"})


@pytest.fixture
def match_account_login_response():
    return Response(body=None, status_code=204)


@pytest.fixture
def match_account_login_request_for_nonexistent_account():
    return Predicate(method="POST", path="/accounts/logins/match", body={"login": "john_smith"})


@pytest.fixture
def match_account_login_response_for_nonexistent_account():
    response_body = {
        "resource": "Account",
        "description": "Requested resource not found.",
        "details": "Requested resource doesn't exist or has been deleted.",
    }
    return Response(body=response_body, status_code=404)


@pytest.fixture
def match_account_email_request():
    return Predicate(method="POST", path="/accounts/emails/match", body={"email": "john.doe@mail.com"})


@pytest.fixture
def match_account_email_response():
    return Response(body=None, status_code=204)
