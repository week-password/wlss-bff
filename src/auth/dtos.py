from __future__ import annotations

from typing import Any, TypeVar

from api.shared.fields import IdField, UuidField
from pydantic import Field

from src.account.fields import AccountEmailField, AccountLoginField, AccountPasswordField
from src.shared.schemas import Schema


DictT = TypeVar("DictT", bound=dict[str, Any])


class CreateSessionRequest(Schema):
    email: AccountEmailField | None = Field(None, example="john.doe@mail.com")
    login: AccountLoginField | None = Field(None, example="john_doe")
    password: AccountPasswordField = Field(..., example="qwerty123")


class CreateSessionResponse(Schema):
    session: _Session
    class _Session(Schema):  # noqa: E301
        id: UuidField = Field(..., example="b9dd3a32-aee8-4a6b-a519-def9ca30c9ec")
        account_id: IdField = Field(..., example=42)

    tokens: _Tokens
    class _Tokens(Schema):  # noqa: E301
        access_token: str = Field(..., example=(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6N"
            "DJ9.YKVpm2zdxup0_ts81Ft4USo-AUMKXBCTfgXtNFbRLlg"
        ))
        refresh_token: str = Field(..., example=(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0MiwiZGV2aWNlX2lkIj"
            "oxOCwiZXhwIjoxNjg3MjU2MTMxfQ.GgXVGPV1aE2GjyRWN_IrHaEkZwY_x0gs25lJKtgspX0"
        ))


class RefreshTokensResponse(Schema):
    access_token: str = Field(..., example=(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6N"
        "DJ9.YKVpm2zdxup0_ts81Ft4USo-AUMKXBCTfgXtNFbRLlg"
    ))
    refresh_token: str = Field(..., example=(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0MiwiZGV2aWNlX2lkIj"
        "oxOCwiZXhwIjoxNjg3MjU2MTMxfQ.GgXVGPV1aE2GjyRWN_IrHaEkZwY_x0gs25lJKtgspX0"
    ))
