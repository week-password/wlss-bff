from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import jwt
from api.client import Api
from api.wish import dtos as api_dtos
from wlss.shared.types import Id

from src.config import CONFIG
from src.wish.dtos import CreateWishResponse, GetAccountWishesResponse, UpdateWishResponse
from src.wish.enums import BookingStatus


if TYPE_CHECKING:
    from fastapi.security import HTTPAuthorizationCredentials

    from src.wish.dtos import CreateWishRequest, UpdateWishRequest


async def create_wish(
    account_id: Id,
    request_data: CreateWishRequest,
    authorization: HTTPAuthorizationCredentials,
) -> CreateWishResponse:
    api_request_data = api_dtos.CreateWishRequest.from_(request_data)
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        wish_response = await api.wish.create_wish(account_id, api_request_data, authorization.credentials)
    return CreateWishResponse.from_(wish_response)


async def update_wish(
    account_id: Id,
    wish_id: Id,
    request_data: UpdateWishRequest,
    authorization: HTTPAuthorizationCredentials,
) -> UpdateWishResponse:
    api_request_data = api_dtos.UpdateWishRequest.from_(request_data)
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        wish_response = await api.wish.update_wish(account_id, wish_id, api_request_data, authorization.credentials)
    return UpdateWishResponse.from_(wish_response)



async def get_account_wishes(account_id: Id, authorization: HTTPAuthorizationCredentials) -> GetAccountWishesResponse:
    token_payload = jwt.decode(authorization.credentials, options={"verify_signature": False})
    current_account_id = Id(token_payload["account_id"])

    if account_id == current_account_id:
        async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
            wishes_response = await api.wish.get_account_wishes(account_id, authorization.credentials)
            return GetAccountWishesResponse.model_validate([
                {
                    "id": wish.id,
                    "avatar_id": wish.avatar_id,
                    "description": wish.description,
                    "title": wish.title,
                    "booking_id": None,
                    "booking_status": None,
                }
                for wish in wishes_response.wishes
            ])

    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        wishes_response, bookings_response = await asyncio.gather(
            api.wish.get_account_wishes(account_id, authorization.credentials),
            api.wish.get_wish_bookings(account_id, authorization.credentials),
        )

    bookings_index = {booking.wish_id: booking for booking in bookings_response.wish_bookings}

    response_body = []
    for wish in wishes_response.wishes:
        booking_id = None
        booking_status = BookingStatus.NOT_BOOKED

        booking = bookings_index.get(wish.id)
        if booking is not None:
            booking_id = booking.id

            booking_status = BookingStatus.BOOKED_BY_ANOTHER_ACCOUNT
            if booking.account_id == current_account_id:
                booking_status = BookingStatus.BOOKED_BY_CURRENT_ACCOUNT

        response_body.append({
            "id": wish.id,
            "avatar_id": wish.avatar_id,
            "description": wish.description,
            "title": wish.title,
            "booking_id": booking_id,
            "booking_status": booking_status,
        })
    return GetAccountWishesResponse.model_validate(response_body)


async def delete_wish(account_id: Id, wish_id: Id, authorization: HTTPAuthorizationCredentials) -> None:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        await api.wish.delete_wish(account_id, wish_id, authorization.credentials)


async def create_wish_booking(
    account_id: Id,
    wish_id: Id,
    authorization: HTTPAuthorizationCredentials,
) -> None:
    token_payload = jwt.decode(authorization.credentials, options={"verify_signature": False})
    current_account_id = Id(token_payload["account_id"])

    api_request_data = api_dtos.CreateWishBookingRequest(account_id=current_account_id)
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
