from typing import Optional
from datetime import datetime

from fastapi_users import models
from pydantic import BaseModel


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


class User(models.BaseUser):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    phone: Optional[str] = None
    address: str
    is_staff: bool
    is_legal_person: bool
    last_login: Optional[datetime] = None
    date_joined: datetime
    # role_id: int  # Role
    role: Role

    class Config:
        orm_mode = True


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass



