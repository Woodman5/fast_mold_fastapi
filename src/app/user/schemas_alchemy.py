from typing import List, Optional
from datetime import datetime
import uuid

from pydantic import BaseModel, UUID4, AnyUrl
from sqlalchemy_utils import PhoneNumberType
# from src.app.base.schemas_base import Schema


class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    phone: str

    class Config:
        arbitrary_types_allowed = True


class UserDefaults(UserBase):
    user_uuid: UUID4 = uuid.uuid4()
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False
    is_legal_person: bool = False
    is_verified: bool = False
    item_removed: bool = False


class UserInDB(UserBase):
    password: str
    user_uuid: Optional[UUID4]


class UserLastLoginUpdate(BaseModel):
    """ Update last login time"""
    last_login: datetime


class UserVerifyEmail(BaseModel):
    """ Properties to verify Email via link """
    is_verified: bool


class RoleBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None


class RoleUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]


class Role(RoleBase):
    id: Optional[int]
    updated: Optional[datetime] = None
    created: Optional[datetime]
    item_removed: Optional[bool]
    # users: List[User] = []

    class Config:
        orm_mode = True


class UserFull(UserDefaults):
    id: int
    last_name: Optional[str]
    middle_name: Optional[str]
    address: Optional[str]
    avatar: Optional[AnyUrl]
    updated: Optional[datetime] = None
    created: datetime
    last_login: Optional[datetime] = None
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

