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
    CRUDRelationsM2M,
    check_name_slug)

from .models import common_data
from .models.material import (
    HardnessScales,
    CommonHardness,
    Status,
    Tech,
    ToolClass,
    MaterialType,
    Imitation,
    ChemicalRes,
    MeasuringStandards,
    Color,
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


class ToolManufacturerCRUD(CRUDRelationsM2M):

    async def create(self, obj_in: CreateSchemaType, response_model: ResponseSchemaType) -> Union[
        BaseModel, HTTPException]:
        created_model, relation_items = await self.create_item(obj_in)

        for item in relation_items:
            await created_model.technology.add(item)

        data = self.construct_data(created_model, response_model)
        return data

    async def update(self, pk: int, obj_in: UpdateSchemaType, response_model: ResponseSchemaType) -> BaseModel:
        item = await self.get_item(pk=pk)
        updated_item_dict = await self.update_item(pk,
                                                   obj_in,
                                                   item.technology,
                                                   )
        data = self.construct_data(updated_item_dict, response_model)
        return data


hardness_scales_service = HardnessScalesCRUD(HardnessScales)
common_hardness_service = CommonHardnessCRUD(CommonHardness)
status_service = StatusCRUD(Status)
technology_service = TechnologyCRUD(Tech)
toolclass_service = ToolClassCRUD(ToolClass)
materialtype_service = MaterialTypeCRUD(MaterialType)
imitationmaterial_service = ImitationMaterialCRUD(Imitation)
chemicalresistance_service = ChemicalResistanceCRUD(ChemicalRes)
measuringstandards_service = MeasuringStandardsCRUD(MeasuringStandards)
colors_service = ColorsCRUD(Color)
typetechnology_service = TypeTechnologyCRUD(TypeTech, rel=['technology'], exclude=None)
tooltype_service = ToolTypeCRUD(ToolType, rel=['tool_class'], exclude=None)
toolmanufacturer_service = ToolManufacturerCRUD(ToolMan,
                                                rel=['technology'],
                                                rel_name='toolmantech',
                                                rel_model=Tech,
                                                pl_name='Technology',
                                                exclude=None
                                                )
