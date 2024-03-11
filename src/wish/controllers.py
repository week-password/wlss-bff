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
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        await api.wish.delete_wish(account_id, wish_id, authorization.credentials)


async def create_wish_booking(
    account_id: Id,
    wish_id: Id,
    request_data: CreateWishBookingRequest,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    api_request_data = api_dtos.CreateWishBookingRequest.from_(request_data)
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        await api.wish.create_wish_booking(account_id, wish_id, api_request_data, authorization.credentials)


async def delete_wish_booking(
    account_id: Id,
    wish_id: Id,
    booking_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        await api.wish.delete_wish_booking(account_id, wish_id, booking_id, authorization.credentials)
