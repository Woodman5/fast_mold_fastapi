from typing import Optional

from sqlalchemy.orm import Session

from src.app.user.models import User, Role
import src.app.user.schemas_alchemy as schemas


from src.app.auth.security import verify_password, get_password_hash
from src.app.base.service_base import CRUDBase


class CRUDUser(CRUDBase[User, schemas.User, schemas.User]):
    def get_by_email(self, db_session: Session, *, email: str) -> Optional[User]:
        return db_session.query(User).filter(User.email == email).first()

    def get_by_name(self, db_session: Session, *, name: str) -> Optional[User]:
        return db_session.query(User).filter(User.username == name).first()

    def create(self, db_session: Session, *, obj_in: schemas.User) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.first_name,
            is_superuser=obj_in.is_superuser,
        )
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def authenticate(
        self, db_session: Session, *, email: str, password: str
    ) -> Optional[User]:
        user = self.get_by_email(db_session, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


class RoleCRUD(CRUDBase[Role, schemas.Role, schemas.Role]):
    pass


crud_user = CRUDUser(User)
user_role_service = RoleCRUD(Role)
