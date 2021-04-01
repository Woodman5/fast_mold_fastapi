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

    type_technology: Optional[List[int]]  # must be for any material
    matcolor: Optional[List[int]]  # must be for any material
    matcomponent: Optional[List[int]]  # can be for any material

    manufacturer: Optional[ForeignGet]  # must be for any material
    mat_type: Optional[ForeignGet]  # must be for any material
    mat: Optional[ForeignGet]  # can be for any material
    mech: Optional[ForeignGet]  # can be for almost any material
    p3d: Optional[ForeignGet]  # can be only for 3D printing
    gfrp: Optional[ForeignGet]  # can be only for Composite (resins, prepregs, gfrp, gfip, cfrp etc.)
    filler: Optional[ForeignGet]  # can be only for PU materials
    tech_param: Optional[ForeignGet]  # can be for any material


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
















