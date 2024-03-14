from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def match_account_login_request():
    return Predicate(method="POST", path="/accounts/logins/match", body={"login": "john_doe"})


@pytest.fixture
def match_account_login_response():
    return Response(body=None, status_code=204)
