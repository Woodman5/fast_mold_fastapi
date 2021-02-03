from typing import Optional

from tortoise.query_utils import Q

from .models import mat_properties
from . import schemas
from ..base.service_base_tortoise import BaseService


class HardnessScalesService(BaseService):
    model = mat_properties.HardnessScales
    create_schema = schemas.HardnessScales_Create_Pydantic
    update_schema = schemas.HardnessScales_Create_Pydantic
    get_schema = schemas.HardnessScales_Get_Pydantic


class CommonHardnessService(BaseService):
    model = mat_properties.CommonHardness
    create_schema = schemas.CommonHardness_Create_Pydantic
    update_schema = schemas.CommonHardness_Create_Pydantic
    get_schema = schemas.CommonHardness_Get_Pydantic


hardness_scales_service = HardnessScalesService()
common_hardness_service = CommonHardnessService()
