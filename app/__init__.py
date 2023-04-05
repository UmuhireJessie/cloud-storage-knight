from fastapi import FastAPI
from app.api import api_router
from app.core.config import settings


app = FastAPI(title="Knight's Cloud Storage - File Service API")


app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
    responses={
        500: {"description": "Internal Server Error"},
    },
)