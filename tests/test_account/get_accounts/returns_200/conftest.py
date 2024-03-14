from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


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
