from __future__ import annotations

from typing import TYPE_CHECKING

from api.account import dtos as api_dtos
from api.client import Api
from wlss.account.types import AccountLogin
from wlss.shared.types import Id

from src.account.dtos import (
    CreateAccountResponse,
    GetAccountsResponse,
)
from src.config import CONFIG


if TYPE_CHECKING:
    from fastapi.security import HTTPAuthorizationCredentials

    from src.account.dtos import CreateAccountRequest, MatchAccountEmailRequest, MatchAccountLoginRequest


async def create_account(request_data: CreateAccountRequest) -> CreateAccountResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.CreateAccountRequest.from_(request_data)
    response = await api.account.create_account(api_request_data)
    return CreateAccountResponse.from_(response)


async def get_accounts(
    account_ids: list[Id],
    account_logins: list[AccountLogin],
    authorization: HTTPAuthorizationCredentials,
) -> GetAccountsResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    response = await api.account.get_accounts(
        account_ids=[Id(id_) for id_ in account_ids],
        account_logins=[AccountLogin(login) for login in account_logins],
        token=authorization.credentials,
    )
    return GetAccountsResponse.model_validate(response.accounts, from_attributes=True)


async def match_account_login(request_data: MatchAccountLoginRequest) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.MatchAccountLoginRequest.from_(request_data)
    await api.account.match_account_login(api_request_data)


async def match_account_email(request_data: MatchAccountEmailRequest) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.MatchAccountEmailRequest.from_(request_data)
    await api.account.match_account_email(api_request_data)
