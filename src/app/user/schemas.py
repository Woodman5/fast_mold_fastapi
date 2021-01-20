from typing import Optional
from datetime import datetime

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

    # id: int
    user_uuid: UUID4
    username: str
    email: EmailStr
    avatar: Optional[str] = None
    is_active: bool
    is_superuser: bool
    is_verified: bool
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    phone: Optional[str] = None
    address: str
    is_staff: bool
    is_legal_person: bool
    last_login: Optional[datetime] = None
    date_joined: datetime
    role: Role

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


class UserCreateInRegistration(BaseModel):
    """ Свойства для получения через API при регистрации """

    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    address: str
    is_staff: bool
    role: Role

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
                                              exclude=('is_active', 'is_staff', 'is_superuser'),
                                              )
User_Pydantic = pydantic_model_creator(UserModel,
                                       name='user',
                                       )
Person_Pydantic = pydantic_model_creator(PersonType,
                                         name='role',
                                         )
