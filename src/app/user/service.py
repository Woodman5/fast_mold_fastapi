from typing import Optional

from tortoise.query_utils import Q

from src.app.auth.security import verify_password, get_password_hash

from . import schemas, models
from ..base.service_base import BaseService


class UserService(BaseService):
    model = models.UserModel
    create_schema = schemas.User_Create_Pydantic
    update_schema = schemas.UserUpdate
    get_schema = schemas.User_Pydantic

    async def create_user(self, schema: schemas.User_Create_Pydantic, **kwargs):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.User_Create_Pydantic(
                **schema.dict(exclude={"password"}), password=hash_password, **kwargs
            )
        )

    async def create_user_by_admin(self, schema: schemas.UserRegistrationByAdminPydantic, **kwargs):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.UserRegistrationByAdminPydantic(
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

    async def create_superuser(self, schema: schemas.User_Admin_Create_Pydantic):
        hash_password = get_password_hash(schema.dict().pop("password"))
        return await self.create(
            schemas.User_Create_Pydantic(
                **schema.dict(exclude={"password"}),
                password=hash_password,
                is_active=True,
                is_superuser=True,
                is_staff=True,
                is_verified=False,
                role=4,
            )
        )


class PersonTypeService(BaseService):
    model = models.PersonType
    create_schema = schemas.Person_Create_Pydantic
    update_schema = schemas.Role
    get_schema = schemas.Person_Get_Pydantic


user_service = UserService()
person_type_service = PersonTypeService()
