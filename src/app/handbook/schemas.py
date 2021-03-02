from typing import Optional
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr, UUID4
from pydantic.fields import ModelField, Field

from .models.mat_properties import (
    HardnessScales,
    CommonHardness,
)


class HardnessScalesBase(BaseModel):
    name: str
    slug: str
    hs_max: Optional[int] = 100
    hs_min: Optional[int] = 0
    hs_units: Optional[str] = '-'
    description: Optional[str] = None

    class Config:
        orm_mode = True


class HardnessScalesGet(HardnessScalesBase):
    id: int


class HardnessScalesFull(HardnessScalesGet):
    item_removed: bool
    created: datetime
    updated: datetime


class CommonHardnessBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CommonHardnessGet(CommonHardnessBase):
    id: int


class CommonHardnessFull(CommonHardnessGet):
    item_removed: bool
    created: datetime
    updated: datetime
