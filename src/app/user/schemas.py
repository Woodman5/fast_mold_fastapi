from typing import Optional
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr, UUID4
from pydantic.fields import ModelField, Field
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from .models import User, PersonType


Person_Create_Pydantic = pydantic_model_creator(PersonType,
                                                name='Create role',
                                                exclude_readonly=True,
                                                exclude=('usermodels',)
                                                )

Person_Get_Pydantic = pydantic_model_creator(PersonType,
                                             name='Get role',
                                             exclude=('usermodels',)
                                             )


class Role(PydanticModel):
    id: Optional[int]
    person_type: Optional[str]
    person_slug: Optional[str]
    person_desc: Optional[str]


class UserLastLoginUpdate(BaseModel):
    """ Update last login time"""
    last_login: datetime


class UserVerifyEmail(BaseModel):
    """ Properties to verify Email via link """
    is_verified: bool


class UserPydanticBase(PydanticModel):
    """ Properties to receive via API by user """

    user_uuid: Optional[UUID4]
    username: Optional[str]
    email: Optional[EmailStr]
    avatar: Optional[str]
    is_verified: Optional[bool]
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    date_joined: Optional[datetime]
    role: Optional[Role]


class UserPydantic(UserPydanticBase):
    """ Additional properties to receive via API by admin """

    id: Optional[int]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_staff: Optional[bool]
    is_legal_person: Optional[bool]
    last_login: Optional[datetime]


class UserUpdate(PydanticModel):
    """ Properties to receive via API on update """

    username: Optional[str]
    email: Optional[EmailStr]

    avatar: Optional[str]

    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]

    phone: Optional[str]
    address: Optional[str]

    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_staff: Optional[bool]
    is_legal_person: Optional[bool]

    role_id: Optional[int]


# Используется при создании пользователя при самостоятельной регистрации
User_Create_Pydantic = pydantic_model_creator(User,
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
                                                       'role_id',
                                                       ),
                                              )

# Используется при создании пользователя администратором
User_Admin_Create_Pydantic = pydantic_model_creator(User,
                                                    name='create_user_by_admin',
                                                    exclude_readonly=True,
                                                    exclude=('user_uuid',
                                                             'last_login',
                                                             'date_joined',
                                                             ),
                                                    )

# Используется при запросе всех данных пользователя из базы
User_Pydantic = pydantic_model_creator(User,
                                       name='user',
                                       )


# Изменение типа поля после использования генератора "pydantic_model_creator"
class UserRegistrationByAdminPydantic(User_Admin_Create_Pydantic):
    """ Properties to validate user data for registration by admin """
    email: EmailStr = Field(...)


# print(Person_Get_Pydantic.schema_json(indent=4))
# print(Person_Create_Pydantic.schema_json(indent=4))
# print(User_Pydantic.schema_json(indent=4))
