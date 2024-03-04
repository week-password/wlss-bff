from __future__ import annotations

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_account_request", "create_account_response"])
async def test_create_account_returns_201_with_correct_response(f):
    result = await f.client.post(
        "/accounts",
        json={
            "account": {
                "email": "john.doe@mail.com",
                "login": "john_doe",
                "password": "qwerty123",
            },
            "profile": {
                "name": "John Doe",
                "description": "I'm the best guy for your mocks.",
            },
        },
    )

    assert result.status_code == 201
    assert result.json() == {
        "account": {
            "id": 42,
            "createdAt": "2024-02-28T17:25:38.795000Z",
            "email": "john.doe@mail.com",
            "login": "john_doe",
        },
        "profile": {
            "accountId": 42,
            "avatarId": None,
            "description": "I'm the best guy for your mocks.",
            "name": "John Doe",
        },
    }
