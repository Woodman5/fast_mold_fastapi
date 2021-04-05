from typing import Optional, List
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, validator, ValidationError, Json

from .models import common_data
from .models.material import (
    MatParam,
    Printing3D,
    GFRParams,
    MechanicalChars,
    MineralFiller,
    TechnologyChars,
)
from .schemas import TypeTechnologyGet, MeasuringStandardsGet


def check_value_in_list(value, value_list):
    if value in value_list:
        return True
    return False


class ForeignGet(BaseModel):
    id: int


class MaterialParams(MatParam):
    id: Optional[int]


class GFRParamsUpdate(GFRParams):
    id: Optional[int]
    hardener: Optional[ForeignGet]


class MechanicalCharsUpdate(MechanicalChars):
    id: Optional[int]


class TechnologyCharsUpdate(TechnologyChars):
    id: Optional[int]


class MineralFillerUpdate(MineralFiller):
    id: Optional[int]
    covering: Optional[ForeignGet]


class Printing3DUpdate(Printing3D):
    id: Optional[int]


class MaterialUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    short_desc: Optional[str]
    country: Optional[str]
    application: Optional[Json]
    url: Optional[str]

    type_technology: Optional[List[int]]  # must be for any material
    matcolor: Optional[List[int]]  # must be for any material
    matcomponent: Optional[List[int]]  # can be for any material
    cust_param: Optional[List[int]]  # can be for any material

    manufacturer: Optional[ForeignGet]  # must be for any material
    mat_type: Optional[ForeignGet]  # must be for any material
    mat: Optional[MaterialParams]  # can be for any material
    mech: Optional[MechanicalCharsUpdate]  # can be for almost any material
    p3d: Optional[Printing3DUpdate]  # can be only for 3D printing
    gfrp: Optional[GFRParamsUpdate]  # can be only for Composite (resins, prepregs, gfrp, gfip, cfrp etc.)
    filler: Optional[MineralFillerUpdate]  # can be only for PU materials
    tech_param: Optional[TechnologyCharsUpdate]  # can be for any material


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
    type_technology: Optional[List[ForeignGet]]
    matcolor: Optional[List[ForeignGet]]
    matcomponent: Optional[List[ForeignGet]]
    cust_param: Optional[List[ForeignGet]]

    created: datetime
    updated: Optional[datetime]


# class TypeTechnologyCreate(TypeTechnologyUpdate):
#     name: str
#     slug: str
#     short_desc: str
#     technology: ForeignGet
















