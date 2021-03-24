from typing import Union
import datetime

import pytz
from fastapi import HTTPException, status
from pydantic import BaseModel

from src.app.base.service_base import (
    CRUDBase,
    ResponseSchemaType,
    CreateSchemaType,
    UpdateSchemaType,
    CRUDRelations,
    check_name_slug)

from .models import common_data
from .models.mat_properties import (
    HardnessScales,
    CommonHardness,
    Status,
    Tech,
    ToolClass,
    MaterialType,
    ImitationMaterial,
    ChemicalResistance,
    MeasuringStandards,
    Colors,
    TypeTech,
    ToolType,
    ToolMan,
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


class TypeTechnologyCRUD(CRUDRelations):
    pass


class ToolTypeCRUD(CRUDRelations):
    pass


class ToolManufacturerCRUD(CRUDRelations):

    async def create(self, obj_in: CreateSchemaType, response_model: ResponseSchemaType) -> Union[
        BaseModel, HTTPException]:

        if not await check_name_slug(self.model, obj_in.name, obj_in.slug):

            tech = obj_in.dict().pop('technology')
            tech_items = await Tech.objects.filter(id__in=tech).all()
            if not tech_items:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Technologies not found')

            try:
                created_model = await self.model.objects.create(**obj_in.dict(exclude={'technology'}))
            except Exception as e:
                print(e)
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Model creation failed')

            for item in tech_items:
                await created_model.technology.add(item)

            data = self.construct_data(created_model, response_model)
            return data
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Such fields already exists')


hardness_scales_service = HardnessScalesCRUD(HardnessScales)
common_hardness_service = CommonHardnessCRUD(CommonHardness)
status_service = StatusCRUD(Status)
technology_service = TechnologyCRUD(Tech)
toolclass_service = ToolClassCRUD(ToolClass)
materialtype_service = MaterialTypeCRUD(MaterialType)
imitationmaterial_service = ImitationMaterialCRUD(ImitationMaterial)
chemicalresistance_service = ChemicalResistanceCRUD(ChemicalResistance)
measuringstandards_service = MeasuringStandardsCRUD(MeasuringStandards)
colors_service = ColorsCRUD(Colors)
typetechnology_service = TypeTechnologyCRUD(TypeTech, rel=['technology'])
tooltype_service = ToolTypeCRUD(ToolType, rel=['tool_class'])
toolmanufacturer_service = ToolManufacturerCRUD(ToolMan, rel=['technology'], exclude=['country'])
