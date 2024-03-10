from __future__ import annotations

from typing import TYPE_CHECKING

from api.auth import dtos as api_dtos
from api.client import Api

from src.auth.dtos import CreateSessionResponse, RefreshTokensResponse
from src.config import CONFIG


if TYPE_CHECKING:
    from api.shared.fields import IdField, UuidField
    from fastapi.security import HTTPAuthorizationCredentials

    from src.auth.dtos import CreateSessionRequest



async def create_session(request_data: CreateSessionRequest) -> CreateSessionResponse:
    api_request_data = api_dtos.CreateSessionRequest.from_(request_data)
    async with Api(base_url=CONFIG.BFF_URL) as api:
        response = await api.auth.create_session(api_request_data)
    return CreateSessionResponse.from_(response)


async def refresh_tokens(
    account_id: IdField,
    session_id: UuidField,
    authorization: HTTPAuthorizationCredentials,
) -> RefreshTokensResponse:
    async with Api(base_url=CONFIG.BFF_URL) as api:
        response = await api.auth.refresh_tokens(account_id, session_id, authorization.credentials)
    return RefreshTokensResponse.from_(response)


async def delete_session(
    account_id: IdField,
    session_id: UuidField,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    async with Api(base_url=CONFIG.BFF_URL) as api:
        await api.auth.delete_session(account_id, session_id, authorization.credentials)


async def delete_all_sessions(
    account_id: IdField,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    async with Api(base_url=CONFIG.BFF_URL) as api:
        await api.auth.delete_all_sessions(account_id, authorization.credentials)
