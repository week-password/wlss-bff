from __future__ import annotations

from unittest.mock import patch

import pytest


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client", "api": "api_configured_with_api_stubs"})
@pytest.mark.api_stubs(["create_file_request", "create_file_response"])
async def test_create_file_returns_201_with_correct_response(f):
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"upload_file": ("image.png", b"image binary data", "image/png")},
    )

    assert result.status_code == 201
    assert result.json() == {
        "id": "d3bb68db-052f-4851-b74d-d9c884fd43df",
        "extension": "png",
        "mimeType": "image/png",
        "size": 17,
    }


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client"})
@patch("src.file.dependencies.MAX_SIZE", 10)  # lower max size to improve test's performance
async def test_create_file_with_too_large_file_returns_413_with_correct_response(f):
    large_image_data = b"x" * 11
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"upload_file": ("image.png", large_image_data, "image/png")},
    )

    assert result.status_code == 413
    assert result.json() == {
        "resource": "file",
        "description": "File size is too large.",
        "details": "File size is too large and it cannot be handled.",
    }


@pytest.mark.anyio
@pytest.mark.fixtures({"client": "client"})
async def test_create_file_with_filename_without_extension_returns_422_with_correct_response(f):
    result = await f.client.post(
        "/files",
        headers={"Authorization": "Bearer token"},
        files={"upload_file": ("image", b"image binary data", "image/png")},
    )

    assert result.status_code == 422
    assert result.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": ["extension"],
                "msg": "Input should be 'gif', 'jfif', 'jif', 'jpe', 'jpeg', 'jpg', 'png' or 'webp'",
                "input": "",
                "ctx": {"expected": "'gif', 'jfif', 'jif', 'jpe', 'jpeg', 'jpg', 'png' or 'webp'"},
            },
        ],
    }
