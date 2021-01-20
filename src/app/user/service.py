from typing import Optional

from tortoise.query_utils import Q

from src.app.auth.security import verify_password, get_password_hash

from . import schemas, models
from ..base.service_base import BaseService


class UserService(BaseService):
    model = models.UserModel
    create_schema = schemas.UserCreateInRegistration
    update_schema = schemas.UserUpdate
    get_schema = schemas.User_Pydantic

    async def create_user(self, schema: schemas.UserCreateInRegistration, **kwargs):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserCreateInRegistration(
                **schema.dict(exclude={"password"}), password=hash_password, **kwargs
            )
        )

    async def authenticate(self, username: str, password: str) -> Optional[models.UserModel]:
        user = await self.model.get(username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    async def change_password(self, obj: models.UserModel, new_password: str):
        hashed_password = get_password_hash(new_password)
        obj.password = hashed_password
        await obj.save()

    async def get_username_email(self, username: str, email: str):
        return await self.model.get_or_none(Q(username=username) | Q(email=email))

    async def create_superuser(self, schema: schemas.UserCreateInRegistration):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserCreate(
                **schema.dict(exclude={"password"}),
                password=hash_password,
                is_active=True,
                is_superuser=True,
                is_staff=True,
            )
        )


user_s = UserService()
