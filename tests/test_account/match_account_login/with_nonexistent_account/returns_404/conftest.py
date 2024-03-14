from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


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
