from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Body, Path, status

from src.account import controllers
from src.account.dtos import (
    CreateAccountRequest,
    CreateAccountResponse,
    GetAccountIdResponse,
    MatchAccountEmailRequest,
    MatchAccountLoginRequest,
)
from src.account.fields import AccountLoginField
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
    "/accounts/logins/{account_login}/id",
    description="Get Account Id by login. Account Id is available for every logged in user.",
    responses={
        status.HTTP_200_OK: {"description": "Account Id returned"},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    status_code=status.HTTP_200_OK,
    summary="Get Account Id.",
)
async def get_account_id(
    account_login: Annotated[AccountLoginField, Path(example="john_doe")],
    authorization: Authorization,
) -> GetAccountIdResponse:
    return await controllers.get_account_id(account_login, authorization)


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
