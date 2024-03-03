from __future__ import annotations

from types import SimpleNamespace

import pytest
from httpx import AsyncClient

from src.app import app


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
