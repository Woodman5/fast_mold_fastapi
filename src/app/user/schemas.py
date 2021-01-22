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

    user_uuid: UUID4
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


class UserInDB(User):
    """ Свойства для получения через API """

    username: str
    email: EmailStr
    first_name: str
    last_name: str
    address: Optional[str]
    is_staff: bool
    role: Role


class UserForAdminInDB(UserInDB):
    """ Properties to receive via API by admin """

    id: int


class UserLastLoginUpdate(BaseModel):
    """ Update last login time"""

    last_login: datetime


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


class UserVerifyEmail(BaseModel):
    """ Properties to verify Email via link """
    is_verified: bool


# Используется при создании пользователя при запросе данных у пользователя
User_Create_Pydantic = pydantic_model_creator(UserModel,
                                              name='create_user',
                                              exclude_readonly=True,
                                              exclude=('user_uuid',
                                                       'is_active',
                                                       'is_superuser',
                                                       'is_verified',
                                                       'is_staff',
                                                       'is_legal_person',
                                                       'last_login',
                                                       'date_joined',
                                                       'role',
                                                       ),
                                              )

# Используется при создании пользователя администратором
User_Admin_Create_Pydantic = pydantic_model_creator(UserModel,
                                                    name='create_user_by_admin',
                                                    exclude_readonly=True,
                                                    exclude=('user_uuid',
                                                             'last_login',
                                                             'date_joined',
                                                             ),
                                                    )

# Используется при создании пользователя при получении данных из базы
User_Pydantic = pydantic_model_creator(UserModel,
                                       name='user',
                                       )
Person_Pydantic = pydantic_model_creator(PersonType,
                                         name='role',
                                         )
