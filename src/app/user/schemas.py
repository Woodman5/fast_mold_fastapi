from typing import Optional
from datetime import datetime
import uuid

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr, UUID4
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import UserModel, PersonType


class RoleBase(BaseModel):
    person_type: Optional[str] = None
    person_slug: Optional[str] = None
    person_desc: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(BaseModel):
    """User model"""

    user_uuid: UUID4 = uuid.uuid4()
    username: str
    email: EmailStr
    avatar: str = None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    first_name: str
    last_name: str
    middle_name: str = None
    phone: str
    address: str = None
    is_staff: bool = False
    is_legal_person: bool = False
    last_login: datetime = None
    date_joined: datetime
    role: Role = 4

    class Config:
        orm_mode = True


class UserCreate(User):
    """ Свойства для получения через API при создании из админки """

    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    address: str
    is_staff: bool
    role: Role


class UserCreateInRegistration(User):
    """ Свойства для получения через API при регистрации """

    username: str
    email: EmailStr
    password: str = Form(...)
    first_name: str
    last_name: str
    phone: str

    class Config:
        orm_mode = True


class UserUpdate(User):
    """ Properties to receive via API on update """

    password: Optional[str] = Form(...)


class UserDBNotPublic(User):
    id: int


User_Create_Pydantic = pydantic_model_creator(UserModel,
                                              name='create_user',
                                              exclude_readonly=True,
                                              exclude=('user_uuid',
                                                       'avatar',
                                                       'is_active',
                                                       'is_superuser',
                                                       'is_verified',
                                                       'middle_name',
                                                       'address',
                                                       'is_staff',
                                                       'is_legal_person',
                                                       'last_login',
                                                       'role',
                                                       ),
                                              )
User_Pydantic = pydantic_model_creator(UserModel,
                                       name='user',
                                       )
Person_Pydantic = pydantic_model_creator(PersonType,
                                         name='role',
                                         )
