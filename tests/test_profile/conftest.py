from __future__ import annotations

import jwt
import pytest
from mbtest.imposters.predicates import Predicate
from mbtest.imposters.responses import Response


@pytest.fixture
def access_token():
    return jwt.encode({"account_id": 2}, key="some-secret-key")


@pytest.fixture
def access_token_of_profile_owner():
    return jwt.encode({"account_id": 1}, key="some-secret-key")


@pytest.fixture
def get_account_request(access_token):
    return Predicate(method="GET", path="/accounts/1", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_account_request_from_account_owner(access_token_of_profile_owner):
    return Predicate(
        method="GET",
        path="/accounts/1",
        headers={"Authorization": f"Bearer {access_token_of_profile_owner}"},
    )


@pytest.fixture
def get_account_response():
    response_body = {"id": 1, "login": "john_doe"}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_response_for_account_owner():
    response_body = {"id": 1, "login": "john_doe"}
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_profile_request(access_token):
    return Predicate(method="GET", path="/accounts/1/profile", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_profile_request_from_profile_owner(access_token_of_profile_owner):
    return Predicate(
        method="GET",
        path="/accounts/1/profile",
        headers={"Authorization": f"Bearer {access_token_of_profile_owner}"},
    )


@pytest.fixture
def get_profile_response():
    response_body = {
        "account_id": 1,
        "avatar_id": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_profile_response_for_profile_owner():
    response_body = {
        "account_id": 1,
        "avatar_id": "3d859b6b-b1ce-4a30-b6bc-c62fc8992630",
        "description": "Who da heck is John Doe?",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_friendships_request(access_token):
    return Predicate(method="GET", path="/accounts/2/friendships", headers={"Authorization": f"Bearer {access_token}"})


@pytest.fixture
def get_account_friendships_response():
    return Response({"friendships": []}, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_friendships_response_with_one_friendship():
    response_body = {
        "friendships": [
            {
                "account_id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 2,
            },
            {
                "account_id": 2,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 1,
            },
        ],
    }
    return Response(response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_account_friendships_response_with_friendship_to_another_account():
    response_body = {
        "friendships": [
            {
                "account_id": 3,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 2,
            },
            {
                "account_id": 2,
                "created_at": "2024-02-28T17:25:38.795Z",
                "friend_id": 3,
            },
        ],
    }
    return Response(response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_request(access_token):
    return Predicate(
        method="GET",
        path="/accounts/2/friendships/requests",
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture
def get_friendship_requests_response():
    return Response({"requests": []}, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_response_with_one_incoming_request():
    response_body = {
        "requests": [
            {
                "id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 2,
                "sender_id": 1,
                "status": "PENDING",
            },
        ],
    }
    return Response(response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_response_with_one_outgoing_request():
    response_body = {
        "requests": [
            {
                "id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 1,
                "sender_id": 2,
                "status": "PENDING",
            },
        ],
    }
    return Response(response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def get_friendship_requests_response_with_one_rejected_request():
    response_body = {
        "requests": [
            {
                "id": 1,
                "created_at": "2024-02-28T17:25:38.795Z",
                "receiver_id": 1,
                "sender_id": 2,
                "status": "REJECTED",
            },
        ],
    }
    return Response(response_body, status_code=200, headers={"content-type": "application/json"})


@pytest.fixture
def update_profile_request():
    request_body = {
        "avatar_id": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
        "description": "NEW John Doe's profile description",
        "name": "John Doe",
    }
    return Predicate(
        method="PUT",
        path="/accounts/1/profile",
        body=request_body,
        headers={"Authorization": "Bearer token"},
    )


@pytest.fixture
def update_profile_response():
    response_body = {
        "account_id": 1,
        "avatar_id": "f6bdfda7-0a5b-4ed5-800f-ac352656abec",
        "description": "NEW John Doe's profile description",
        "name": "John Doe",
    }
    return Response(body=response_body, status_code=200, headers={"content-type": "application/json"})
