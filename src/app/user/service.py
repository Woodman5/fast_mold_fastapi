from typing import Optional, List, Sequence
from ormar import Model

from src.app.user.models import Role, User
import src.app.user.schemas_alchemy as schemas


from src.app.auth.security import verify_password, get_password_hash
from src.app.base.service_base import CRUDBase


class CRUDUser(CRUDBase):
    async def get(self, pk: int) -> Optional[Model]:
        user = await self.model.objects.select_related('role').get(id=pk)
        # user = await self.model.objects.get(id=pk)
        # await user.role.load()
        return user

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        return await self.model.objects.offset(skip).limit(limit).select_related('role').all()

    # def get_by_email(self, email: str, **kwargs) -> Optional[User]:
    #     return db_session.query(User).filter(User.email == email).first()
    #
    # def get_by_name(self, dname: str, **kwargs) -> Optional[User]:
    #     return db_session.query(User).filter(User.username == name).first()
    #
    # def get_by_uuid(self, db_session: Session, uuid: str, **kwargs) -> Optional[User]:
    #     return db_session.query(User).filter(User.user_uuid == uuid).first()
    #
    # def create(self, db_session: Session, obj_in: schemas.UserInDB, **kwargs) -> User:
    #     obj_in = obj_in.dict()
    #     hash_password = get_password_hash(obj_in.pop("password"))
    #     db_obj = User(**obj_in, password=hash_password, role_id=5)
    #     print(db_obj)
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj
    #
    # def authenticate(
    #     self, db_session: Session, name: str, password: str, **kwargs
    # ) -> Optional[User]:
    #     user = self.get_by_name(db_session, name=name)
    #     if not user:
    #         return None
    #     if not verify_password(password, user.hashed_password):
    #         return None
    #     return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


class RoleCRUD(CRUDBase):
    pass


user_service = CRUDUser(User)
user_role_service = RoleCRUD(Role)
