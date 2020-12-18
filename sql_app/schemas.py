from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
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


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    last_login: Optional[datetime] = None
    date_joined: datetime
    role_id: int

    class Config:
        orm_mode = True


class RoleBase(BaseModel):
    person_type: str
    person_slug: str
    person_desc: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    users: List[User] = []

    class Config:
        orm_mode = True






