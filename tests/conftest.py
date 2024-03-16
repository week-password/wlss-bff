from __future__ import annotations

from types import SimpleNamespace

import pytest
from httpx import AsyncClient
from mbtest.imposters.imposters import Imposter
from mbtest.imposters.responses import HttpResponse
from mbtest.imposters.stubs import Stub
from mbtest.server import MountebankServer

from src.app import app
from src.config import CONFIG


@pytest.fixture
def anyio_backend():
    """Choose anyio back-end runner as asyncio. Source https://anyio.readthedocs.io/en/1.4.0/testing.html."""
    return "asyncio"


@pytest.fixture
async def client():
    """Async client."""
    async with AsyncClient(app=app, base_url="http://") as async_client:
        yield async_client


@pytest.fixture
def f(request):
    """Load fixtures declared via 'fixtures' mark and put it into 'f' as its attributes."""
    fixtures = SimpleNamespace()
    marker = request.node.get_closest_marker("fixtures")
    if not marker:
        return fixtures
    for fixture_alias, fixture_name in marker.args[0].items():
        fixture = request.getfixturevalue(fixture_name)
        setattr(fixtures, fixture_alias, fixture)
    return fixtures

@pytest.fixture
def mountebank():
    mountebank = MountebankServer(host=CONFIG.MOUNTEBANK_SERVER_HOST, port=CONFIG.MOUNTEBANK_SERVER_PORT)
    for impostor in mountebank.query_all_imposters():
        mountebank.delete_impostor(impostor)
    imposters = mountebank.query_all_imposters()
    assert len(imposters) == 0
    return mountebank


@pytest.fixture
def api_configured_with_api_stubs(mountebank, request):
    stubs = []
    if marker := request.node.get_closest_marker("api_stubs"):
        for request_fixture_name, response_fixture_name in marker.args:
            predicate = request.getfixturevalue(request_fixture_name)
            response = request.getfixturevalue(response_fixture_name)
            stubs.append(Stub(predicates=predicate, responses=response))
    imposter = Imposter(
        stubs,
        port=CONFIG.MOUNTEBANK_IMPOSTOR_PORT,
        default_response=HttpResponse(
            body={"impostor_error": "Couldn't find response for the stub request."},
            status_code=500,
        ),
    )
    mountebank = request.getfixturevalue("mountebank")
    mountebank.add_impostor(imposter)
    return imposter
