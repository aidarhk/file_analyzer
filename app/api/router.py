from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import download


api_router = APIRouter()


api_router.include_router(
    health.router
)

api_router.include_router(
    download.router
)