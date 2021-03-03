from typing import Optional
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr, UUID4


class HardnessScalesUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    hs_max: Optional[int] = 100
    hs_min: Optional[int] = 0
    hs_units: Optional[str] = '-'
    description: Optional[str] = None

    class Config:
        orm_mode = True


class HardnessScalesCreate(HardnessScalesUpdate):
    name: str
    slug: str


class HardnessScalesGet(HardnessScalesUpdate):
    id: int


class CommonHardnessUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str] = None

    class Config:
        orm_mode = True


class CommonHardnessCreate(CommonHardnessUpdate):
    name: str
    slug: str


class CommonHardnessGet(CommonHardnessUpdate):
    id: int


class StatusUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str] = None

    class Config:
        orm_mode = True


class StatusCreate(StatusUpdate):
    name: str
    slug: str


class StatusGet(StatusUpdate):
    id: int


class TechnologyUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]

    class Config:
        orm_mode = True


class TechnologyCreate(TechnologyUpdate):
    name: str
    slug: str


class TechnologyGet(TechnologyUpdate):
    id: int


class ToolClassUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ToolClassCreate(ToolClassUpdate):
    name: str
    slug: str


class ToolClassGet(ToolClassUpdate):
    id: int


class MaterialTypeUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]

    class Config:
        orm_mode = True


class MaterialTypeCreate(MaterialTypeUpdate):
    name: str
    slug: str


class MaterialTypeGet(MaterialTypeUpdate):
    id: int


class ImitationMaterialUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]

    class Config:
        orm_mode = True


class ImitationMaterialCreate(ImitationMaterialUpdate):
    name: str
    slug: str


class ImitationMaterialGet(ImitationMaterialUpdate):
    id: int


class ChemicalResistanceUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]

    class Config:
        orm_mode = True


class ChemicalResistanceCreate(ChemicalResistanceUpdate):
    name: str
    slug: str


class ChemicalResistanceGet(ChemicalResistanceUpdate):
    id: int


class MeasuringStandardsUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    standard_type: Optional[str]
    application_type: Optional[str]
    description: Optional[str] = None

    class Config:
        orm_mode = True


class MeasuringStandardsCreate(MeasuringStandardsUpdate):
    name: str
    slug: str
    standard_type: str
    application_type: str


class MeasuringStandardsGet(MeasuringStandardsUpdate):
    id: int


class ColorsUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    color_type: Optional[str]
    hex_code: Optional[str]
    rgb_code: Optional[str]
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ColorsCreate(ColorsUpdate):
    name: str
    slug: str
    color_type: str
    hex_code: str
    rgb_code: str


class ColorsGet(ColorsUpdate):
    id: int
