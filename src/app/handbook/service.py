from typing import Union

from fastapi import HTTPException, status
from pydantic import BaseModel

from src.app.base.service_base import CRUDBase, ResponseSchemaType, CreateSchemaType, UpdateSchemaType

from .models import common_data
from .models.mat_properties import (
    HardnessScales,
    CommonHardness,
    Status,
    Technology,
    ToolClass,
    MaterialType,
    ImitationMaterial,
    ChemicalResistance,
    MeasuringStandards,
    Colors,
    TypeTechnology,
)


class HardnessScalesCRUD(CRUDBase):
    pass


class CommonHardnessCRUD(CRUDBase):
    pass


class StatusCRUD(CRUDBase):
    pass


class TechnologyCRUD(CRUDBase):
    pass


class ToolClassCRUD(CRUDBase):
    pass


class MaterialTypeCRUD(CRUDBase):
    pass


class ImitationMaterialCRUD(CRUDBase):
    pass


class ChemicalResistanceCRUD(CRUDBase):
    pass


class MeasuringStandardsCRUD(CRUDBase):
    pass


class ColorsCRUD(CRUDBase):
    pass


class TypeTechnologyCRUD(CRUDBase):
    pass


hardness_scales_service = HardnessScalesCRUD(HardnessScales)
common_hardness_service = CommonHardnessCRUD(CommonHardness)
status_service = StatusCRUD(Status)
technology_service = TechnologyCRUD(Technology)
toolclass_service = ToolClassCRUD(ToolClass)
materialtype_service = MaterialTypeCRUD(MaterialType)
imitationmaterial_service = ImitationMaterialCRUD(ImitationMaterial)
chemicalresistance_service = ChemicalResistanceCRUD(ChemicalResistance)
measuringstandards_service = MeasuringStandardsCRUD(MeasuringStandards)
colors_service = ColorsCRUD(Colors)
typetechnology_service = TypeTechnologyCRUD(TypeTechnology)
