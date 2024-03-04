from __future__ import annotations

from typing import Annotated

from api.shared.fields import IdField
from fastapi import APIRouter, Body, Path, status

from src.auth.dependencies import Authorization
from src.shared import swagger as shared_swagger
from src.wish import controllers
from src.wish.dtos import CreateWishBookingRequest


router = APIRouter(tags=["wish"])


@router.delete(
    "/accounts/{account_id}/wishes/{wish_id}",
    description="Delete particular wish and related bookings.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Wish and related bookings are deleted."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete particular wish.",
)
async def delete_wish(
    account_id: Annotated[IdField, Path(example=42)],
    wish_id: Annotated[IdField, Path(example=17)],
    authorization: Authorization,
) -> None:
    return await controllers.delete_wish(account_id, wish_id, authorization)


@router.post(
    "/accounts/{account_id}/wishes/{wish_id}/bookings",
    description="Book particular wish for particular account.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Wish booking is created successfully."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Book particular wish.",
)
async def create_wish_booking(
    account_id: Annotated[IdField, Path(example=42)],
    wish_id: Annotated[IdField, Path(example=18)],
    request_data: Annotated[CreateWishBookingRequest, Body()],
    authorization: Authorization,
) -> None:
    return await controllers.create_wish_booking(account_id, wish_id, request_data, authorization)


@router.delete(
    "/accounts/{account_id}/wishes/{wish_id}/bookings/{booking_id}",
    description="Delete particular wish booking.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Wish Booking has been removed."},
        status.HTTP_401_UNAUTHORIZED: shared_swagger.responses[status.HTTP_401_UNAUTHORIZED],
        status.HTTP_403_FORBIDDEN: shared_swagger.responses[status.HTTP_403_FORBIDDEN],
        status.HTTP_404_NOT_FOUND: shared_swagger.responses[status.HTTP_404_NOT_FOUND],
    },
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete wish booking.",
)
async def delete_wish_booking(
    account_id: Annotated[IdField, Path(example=42)],
    wish_id: Annotated[IdField, Path(example=18)],
    booking_id: Annotated[IdField, Path(example=3)],
    authorization: Authorization,
) -> None:
    return await controllers.delete_wish_booking(account_id, wish_id, booking_id, authorization)
