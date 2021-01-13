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


class RoleBase(BaseModel):
    person_type: str
    person_slug: str
    person_desc: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    # users: List[User] = []

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    last_login: Optional[datetime] = None
    date_joined: datetime
    role: Role
    # role_id: int

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


