from typing import Optional, List
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, validator, ValidationError

from .models import common_data


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

    manufacturer: Optional[int]
    mat_type: Optional[int]
    mat: Optional[int]
    mech: Optional[int]
    p3d: Optional[int]
    gfrp: Optional[int]
    filler: Optional[int]
    technology: Optional[int]


# class TypeTechnologyCreate(TypeTechnologyUpdate):
#     name: str
#     slug: str
#     short_desc: str
#     technology: ForeignGet
















