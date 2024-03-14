from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def get_account_by_login_request():
    return Predicate(
        method="GET",
        path="/accounts",
        query={"account_login": "john_doe"},
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def get_account_by_login_response_with_nonexistent_account():
    response_body = {"accounts": []}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
