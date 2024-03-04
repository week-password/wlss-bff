from __future__ import annotations

from typing import TYPE_CHECKING

from api.client import Api
from api.wish import dtos as api_dtos

from src.config import CONFIG


if TYPE_CHECKING:
    from fastapi.security import HTTPAuthorizationCredentials
    from wlss.shared.types import Id

    from src.wish.dtos import CreateWishBookingRequest


async def delete_wish(account_id: Id, wish_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    await api.wish.delete_wish(account_id, wish_id, authorization.credentials)


async def create_wish_booking(
    account_id: Id,
    wish_id: Id,
    request_data: CreateWishBookingRequest,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    api_request_data = api_dtos.CreateWishBookingRequest.from_(request_data)
    await api.wish.create_wish_booking(account_id, wish_id, api_request_data, authorization.credentials)


async def delete_wish_booking(
    account_id: Id,
    wish_id: Id,
    booking_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    api = Api(base_url=CONFIG.BFF_URL)
    await api.wish.delete_wish_booking(account_id, wish_id, booking_id, authorization.credentials)
