from typing import Optional, List
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, validator, ValidationError

from .models import common_data
from .schemas import TypeTechnologyGet


def check_value_in_list(value, value_list):
    if value in value_list:
        return True
    return False


class ForeignGet(BaseModel):
    id: int


class MaterialUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    short_desc: Optional[str]
    country: Optional[str]
    application: Optional[str]
    url: Optional[str]

    type_technology: Optional[List[int]]
    matcolor: Optional[List[int]]
    matcomponent: Optional[List[int]]

    manufacturer: Optional[ForeignGet]
    mat_type: Optional[ForeignGet]
    mat: Optional[ForeignGet]
    mech: Optional[ForeignGet]
    p3d: Optional[ForeignGet]
    gfrp: Optional[ForeignGet]
    filler: Optional[ForeignGet]
    tech_param: Optional[ForeignGet]


class MaterialCreate(MaterialUpdate):
    name: str
    slug: str
    country: str

    type_technology: List[int]
    matcolor: List[int]

    manufacturer: ForeignGet
    mat_type: ForeignGet


class MaterialGet(MaterialUpdate):
    id: int
    type_technology: List[ForeignGet]
    matcolor: List[ForeignGet]
    matcomponent: List[ForeignGet]

# class TypeTechnologyCreate(TypeTechnologyUpdate):
#     name: str
#     slug: str
#     short_desc: str
#     technology: ForeignGet
















