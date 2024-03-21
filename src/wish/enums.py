from __future__ import annotations

from src.shared.enum import Enum


class BookingStatus(Enum):
    NOT_BOOKED = "notBooked"
    BOOKED_BY_CURRENT_ACCOUNT = "bookedByCurrentAccount"
    BOOKED_BY_ANOTHER_ACCOUNT = "bookedByAnotherAccount"
