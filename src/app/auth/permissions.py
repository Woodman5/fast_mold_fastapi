from typing import Optional, Dict

import jwt
from jwt import PyJWTError
from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyCookie, OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED
from src.config import settings

from src.app.user.models import UserModel
from src.app.user import service

from .jwt import ALGORITHM
from .schemas import TokenPayload


class OAuth2PasswordBearerCookie(OAuth2):

    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        header_authorization: str = request.headers.get("Authorization")
        print(request.headers.get("Authorization"))
        print(request.cookies.get("Session"))
        cookie_authorization: str = request.cookies.get("Session")

        header_scheme, header_param = get_authorization_scheme_param(header_authorization)

        if header_scheme.lower() == "bearer":
            authorization = True
            param = header_param

        elif cookie_authorization:
            authorization = True
            param = cookie_authorization

        else:
            authorization = False
            param = None

        if not authorization and header_scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    # headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


reusable_oauth2 = OAuth2PasswordBearerCookie(tokenUrl="/api/v1/auth/login/access-token")


async def get_current_user(token: str = Security(reusable_oauth2)):
    """ Check auth user
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
        print(token_data)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = await service.user_service.get_obj(id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user(current_user: UserModel = Security(get_current_user)):
    """ Проверка активный юзер или нет """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_superuser(current_user: UserModel = Security(get_current_user)):
    """ Проверка суперюзер или нет """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
