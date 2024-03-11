from __future__ import annotations

from typing import Annotated

from api.account.fields import AccountLoginField
from api.shared.fields import IdField
from fastapi import APIRouter, Body, Query, status
from fastapi.params import Path

from src.account import controllers
from src.account.dtos import (
    CreateAccountRequest,
    CreateAccountResponse,
    GetAccountByLoginResponse,
    GetAccountsResponse,
    MatchAccountEmailRequest,
    MatchAccountLoginRequest,
)
from src.auth.dependencies import Authorization
from src.shared import swagger as shared_swagger


router = APIRouter(tags=["account"])


@router.post(
    "/accounts",
    description="Sign Up - create a new account with profile.",
    responses={
        status.HTTP_201_CREATED: {"description": "New account and profile are created."},
    },
    status_code=status.HTTP_201_CREATED,
    summary="Sign Up - create a new account.",
    tags=["auth"],
)
async def create_account(
    request_data: Annotated[CreateAccountRequest, Body()],
) -> CreateAccountResponse:
    return await controllers.create_account(request_data)


@router.get(
    "/accounts/logins/{account_login}",
    description="Get account. Account info is available for every logged in user.",
    responses={
        status.HTTP_200_OK: {"description": "Account info returned"},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get account.",
)
async def get_account_by_login(
    authorization: Authorization,
    account_login: Annotated[AccountLoginField, Path(example="john_doe")],
) -> GetAccountByLoginResponse:
    return await controllers.get_account_by_login(account_login, authorization)


@router.get(
    "/accounts",
    description="Get accounts. Account infos are available for every logged in user.",
    responses={
        status.HTTP_200_OK: {"description": "Accounts info returned"},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get accounts.",
)
async def get_accounts(
    authorization: Authorization,
    account_ids: Annotated[
        list[IdField],
        Query(alias="id", example=[42, 18, 5]),
    ] = [],  # noqa: B006
    account_logins: Annotated[
        list[AccountLoginField],
        Query(alias="login", example=["john_doe", "john_smith"]),
    ] = [],  # noqa: B006
) -> GetAccountsResponse:
    return await controllers.get_accounts(account_ids, account_logins, authorization)


@router.post(
    "/accounts/logins/match",
    description="Check if account with provided login exists.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Account with current login exists."},
        status.HTTP_404_NOT_FOUND: {"description": "Account with current login doesn't exist."},
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Check login uniqueness.",
)
async def match_account_login(
    request_data: Annotated[MatchAccountLoginRequest, Body()],
) -> None:
    return await controllers.match_account_login(request_data)

@router.post(
    "/accounts/emails/match",
    description="Check if account with provided email exists.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Account with current email exists."},
        status.HTTP_404_NOT_FOUND: {"description": "Account with current email doesn't exist."},
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Check email uniqueness.",
)
async def match_account_email(
    request_data: Annotated[MatchAccountEmailRequest, Body()],
) -> None:
    return await controllers.match_account_email(request_data)
