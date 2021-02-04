from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, UUID4, AnyUrl
from src.app.base.schemas_base import Schema


class UserBase(BaseModel):
    user_uuid: UUID4
    username: str
    email: str
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    address: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    is_legal_person: bool
    is_verified: bool
    avatar: AnyUrl


class UserInDB(UserBase):
    password: str


class RoleBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    updated: Optional[datetime] = None
    created: datetime
    item_removed: bool
    # users: List[User] = []

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    item_removed: bool
    updated: Optional[datetime] = None
    created: datetime
    role: Role
    # role_id: int

    class Config:
        orm_mode = True


# class RoleFreddie(Schema):
#     id: int
#     person_type: str
#     person_slug: str
#     person_desc: Optional[str] = None
#
#     class Config:
#         default_readable_fields = {'person_type'}
#         orm_mode = True
#
#
# class RoleFreddieWrite(RoleFreddie):
#     id: int = None
#
#
# class UserFreddie(Schema):
#     id: int
#
#     username: str
#     email: str
#     password: str
#
#     first_name: str
#     last_name: str
#     middle_name: Optional[str]
#     phone: str
#     address: Optional[str]
#     is_active: bool
#     is_staff: bool
#     is_superuser: bool
#     is_legal_person: bool
#
#     last_login: Optional[datetime] = None
#     date_joined: datetime
#     role: RoleFreddie
#
#     class Config:
#         default_readable_fields = {'email', 'username'}
#         orm_mode = True

