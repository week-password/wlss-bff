from __future__ import annotations

from src.shared.enum import Enum


class FriendshipStatus(Enum):
    NOT_REQUESTED = "notRequested"
    ACCEPTED_REQUEST = "acceptedRequest"
    INCOMING_REQUEST = "incomingRequest"
    OUTGOING_REQUEST = "outgoingRequest"
