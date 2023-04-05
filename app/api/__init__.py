from fastapi import APIRouter

from app.api.controller import router

api_router = APIRouter()
api_router.include_router(
    router, prefix="/upload", tags=["Files"]
)