import datetime
import uuid

from typing import Optional, List, Sequence
from ormar import Model
from ormar.exceptions import NoMatch

from src.app.user.models import Role, User
import src.app.user.schemas_alchemy as schemas


from src.app.auth.security import verify_password, get_password_hash
from src.app.base.service_base import CRUDBase


class CRUDUser(CRUDBase):
    async def get_by(self, **kwargs):
        try:
            return await self.model.objects.select_related('role').get(**kwargs)
        except NoMatch:
            return None

    async def get(self, pk: int) -> Optional[Model]:
        return await self.get_by(id=pk)

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        return await self.model.objects.offset(skip).limit(limit).select_related('role').all()

    async def get_by_email(self, email: str) -> Optional[Model]:
        return await self.get_by(email=email)

    async def get_by_name(self, name: str) -> Optional[Model]:
        return await self.get_by(username=name)

    async def get_by_uuid(self, user_uuid: str) -> Optional[Model]:
        return await self.get_by(user_uuid=user_uuid)

    async def create(self, obj_in) -> Model:
        obj_in = obj_in.dict()
        hash_password = get_password_hash(obj_in.pop("password"))
        customer = await Role.objects.filter(slug='customer').get()
        created = datetime.datetime.now()
        user_uuid = uuid.uuid4()
        user = await self.model.objects.create(**obj_in,
                                               password=hash_password,
                                               role=customer,
                                               created=created,
                                               user_uuid=user_uuid,
                                               )
        return user

    async def authenticate(self, name: str, password: str) -> Optional[Model]:
        user = await self.get_by_name(name=name)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


class RoleCRUD(CRUDBase):
    pass


user_service = CRUDUser(User)
user_role_service = RoleCRUD(Role)