from __future__ import annotations

from api.client import Api

from src.config import CONFIG
from src.health import dtos


async def get_health() -> dtos.HealthResponse:
    api = Api(base_url=CONFIG.BFF_URL)
    response = await api.health.get_health()
    return dtos.HealthResponse.model_validate(response.model_dump())
