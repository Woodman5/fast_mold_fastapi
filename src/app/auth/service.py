from fastapi import BackgroundTasks
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional
from tortoise.query_utils import Q

from src.config import settings

from src.app.user import schemas, service, models
from .models import Verification
from .send_email import send_new_account_email
from pydantic import UUID4


password_reset_jwt_subject = "preset"


async def registration_user(new_user: schemas.User_Pydantic, task: BackgroundTasks) -> bool:
    """Регистрация пользователя"""
    if await models.UserModel.filter(Q(username=new_user.username) | Q(email=new_user.email)).exists():
        return True
    else:
        user = await service.user_service.create_user(new_user)
        verify = await Verification.create(user_id=user.id)
        task.add_task(
            send_new_account_email, new_user.email, new_user.username, new_user.password, verify.link
        )
        return False


async def verify_registration_user(uuid: UUID4) -> bool:
    """ Подтверждение email пользователя """
    verify = await Verification.get(link=uuid).prefetch_related("user")
    if verify:
        await service.user_service.update(schema=schemas.UserVerifyEmail(is_verified=True), id=verify.user.id)
        await Verification.filter(link=uuid).delete()
        return True
    else:
        return False


def generate_password_reset_token(email: str):
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": password_reset_jwt_subject, "email": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        assert decoded_token["sub"] == password_reset_jwt_subject
        return decoded_token["email"]
    except InvalidTokenError:
        return None
