from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def match_account_email_request():
    return Predicate(method="POST", path="/accounts/emails/match", body={"email": "john.doe@mail.com"})


@pytest.fixture
def match_account_email_response():
    return Response(body=None, status_code=204)
