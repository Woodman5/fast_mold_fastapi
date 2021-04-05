from typing import Optional, List
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, validator, ValidationError

from .models import common_data
from src.app.base.helpers import check_value_in_list


class ForeignGet(BaseModel):
    id: int


class HardnessScalesUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    hs_max: Optional[int] = 100
    hs_min: Optional[int] = 0
    hs_units: Optional[str] = '-'
    description: Optional[str]

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
    description: Optional[str]

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
    description: Optional[str]

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
    description: Optional[str]

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
    description: Optional[str]

    class Config:
        orm_mode = True

    @validator('standard_type', 'application_type', pre=True)
    def make_lower(cls, v):
        return v.lower()

    @validator('standard_type', allow_reuse=True)
    def check_type_in_list(cls, v):
        if not check_value_in_list(v, common_data.standard_type_list):
            raise ValueError(f'must be in list: {common_data.standard_type_list}')
        return v

    @validator('application_type', allow_reuse=True)
    def check_app_in_list(cls, v):
        if not check_value_in_list(v, common_data.application_type_list):
            raise ValueError(f'must be in list: {common_data.application_type_list}')
        return v


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
    description: Optional[str]

    class Config:
        orm_mode = True

    @validator('color_type', pre=True)
    def make_lower(cls, v):
        return v.lower()

    @validator('color_type')
    def check_v_in_list(cls, v):
        if not check_value_in_list(v, common_data.color_type_list):
            raise ValueError(f'must be in list: {common_data.color_type_list}')
        return v


class ColorsCreate(ColorsUpdate):
    name: str
    slug: str
    color_type: str
    hex_code: str
    rgb_code: str


class ColorsGet(ColorsUpdate):
    id: int


class TypeTechnologyUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    short_desc: Optional[str]
    technology: Optional[TechnologyGet]

    class Config:
        orm_mode = True


class TypeTechnologyCreate(TypeTechnologyUpdate):
    name: str
    slug: str
    short_desc: str
    technology: ForeignGet


class TypeTechnologyGet(TypeTechnologyUpdate):
    id: int


class ToolTypeUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    short_desc: Optional[str]
    technology: Optional[TechnologyGet]

    class Config:
        orm_mode = True


class ToolTypeCreate(ToolTypeUpdate):
    name: str
    slug: str
    short_desc: str
    technology: ForeignGet


class ToolTypeGet(ToolTypeUpdate):
    id: int


class ToolManufacturerUpdate(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    short_desc: Optional[str]
    country: Optional[str]
    url: Optional[str]
    technology: Optional[List[int]]

    class Config:
        orm_mode = True


class ToolManufacturerCreate(ToolManufacturerUpdate):
    name: str
    slug: str
    short_desc: str
    country: str
    technology: List[int]


class ToolManufacturerGet(ToolManufacturerUpdate):
    id: int
    technology: List[TechnologyGet]


