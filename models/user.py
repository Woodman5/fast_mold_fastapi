from tortoise import fields
from tortoise.models import Model

import uuid
from typing import List, Optional, TypeVar

from fastapi_users import models
from pydantic import UUID4, BaseModel, EmailStr, validator

class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=30, unique=True, index=True, nullable=False)
    # email = Column(String(254), unique=True, index=True, nullable=False)
    #
    # password = Column(String)
    #
    # first_name = Column(String(150), index=True, default='')
    # last_name = Column(String(150), index=True, default='')
    # middle_name = Column(String(150), index=True, default='')
    # phone = Column(String(20), index=True, nullable=False)
    # address = Column(String, index=True, default='')
    #
    # is_active = Column(Boolean, default=True)
    # is_staff = Column(Boolean, default=False)
    # is_superuser = Column(Boolean, default=False)
    # is_legal_person = Column(Boolean, default=False)
    # last_login = Column(DateTime(timezone=False))
    # date_joined = Column(DateTime(timezone=False))
    #
    # role_id = Column(Integer, ForeignKey('handbook_persontype.id'))
    #
    # role = relationship("PersonType", back_populates="users")

    class Meta:
        table = "UserAccounts_user"


# class User(models.BaseUser):
#     id: Optional[int] = None
#     user_uuid: Optional[UUID4] = None
#     username: Optional[str] = None
#
#     @validator("user_uuid", pre=True, always=True)
#     def default_id(cls, v):
#         return v or uuid.uuid4()
#
#
# class UserCreate(models.BaseUserCreate):
#     username: str
#     email: EmailStr
#     password: str
#     is_active: Optional[bool] = True
#     is_superuser: Optional[bool] = False
#     # is_verified: Optional[bool] = False
#
#
# class UserUpdate(User, models.BaseUserUpdate):
#     pass
#
#
# class UserDB(User, models.BaseUserDB):
#     id: int
#     user_uuid: UUID4
#     password: str


# class User(Base):
#     __tablename__ = "UserAccounts_user"
#
#     id = Column(Integer, primary_key=True, index=True)
#
#     username = Column(String(30), unique=True, index=True, nullable=False)
#     email = Column(String(254), unique=True, index=True, nullable=False)
#
#     password = Column(String)
#
#     first_name = Column(String(150), index=True, default='')
#     last_name = Column(String(150), index=True, default='')
#     middle_name = Column(String(150), index=True, default='')
#     phone = Column(String(20), index=True, nullable=False)
#     address = Column(String, index=True, default='')
#
#     is_active = Column(Boolean, default=True)
#     is_staff = Column(Boolean, default=False)
#     is_superuser = Column(Boolean, default=False)
#     is_legal_person = Column(Boolean, default=False)
#     last_login = Column(DateTime(timezone=False))
#     date_joined = Column(DateTime(timezone=False))
#
#     role_id = Column(Integer, ForeignKey('handbook_persontype.id'))
#
#     role = relationship("PersonType", back_populates="users")
