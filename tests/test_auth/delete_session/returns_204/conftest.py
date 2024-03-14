from __future__ import annotations

import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def delete_session_request():
    return Predicate(method="DELETE", path="/accounts/1/sessions/f6d7ccf6-8c66-4a78-8ecc-d91cba589263")

@pytest.fixture
def delete_session_response():
    return Response(status_code=204, headers={"content-type": "application/json"})
