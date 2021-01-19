from fastapi import APIRouter

from .auth_config import fastapi_users, jwt_authentication, cookie_authentication


auth_router = APIRouter()

auth_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"],
)
