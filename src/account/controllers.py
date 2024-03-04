from __future__ import annotations

from typing import TYPE_CHECKING

from api.account import dtos as api_dtos
from api.client import Api

from src.account.dtos import (
    CreateAccountResponse,
    GetAccountIdResponse,
)
from src.config import CONFIG


if TYPE_CHECKING:
    from fastapi.security import HTTPAuthorizationCredentials

    from src.account.dtos import CreateAccountRequest, MatchAccountEmailRequest, MatchAccountLoginRequest
    from src.account.fields import AccountLoginField


async def create_account(request_data: CreateAccountRequest) -> CreateAccountResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.CreateAccountRequest.from_(request_data)
    response = await api.account.create_account(api_request_data)
    return CreateAccountResponse.from_(response)


async def get_account_id(
    account_login: AccountLoginField,
    authorization: HTTPAuthorizationCredentials,
) -> GetAccountIdResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    response = await api.account.get_account_id(account_login, authorization.credentials)
    return GetAccountIdResponse.from_(response)


async def match_account_login(request_data: MatchAccountLoginRequest) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.MatchAccountLoginRequest.from_(request_data)
    await api.account.match_account_login(api_request_data)


async def match_account_email(request_data: MatchAccountEmailRequest) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.MatchAccountEmailRequest.from_(request_data)
    await api.account.match_account_email(api_request_data)
