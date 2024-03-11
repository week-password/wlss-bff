from __future__ import annotations

from api.client import Api

from src.config import CONFIG
from src.health import dtos


async def get_health() -> dtos.HealthResponse:
    async with Api(base_url=CONFIG.BACKEND_API_URL) as api:
        response = await api.health.get_health()
    return dtos.HealthResponse.model_validate(response.model_dump())
