from __future__ import annotations

from fastapi import APIRouter

import src.health.routes


router = APIRouter()


router.include_router(src.health.routes.router)
