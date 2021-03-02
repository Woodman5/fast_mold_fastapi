from src.app.base.service_base import CRUDBase

from . import schemas
from .models.mat_properties import (
    CommonHardness,
    HardnessScales,
)


# class HardnessScalesService(CRUDBase):
#     model = HardnessScales
#     create_schema = schemas.HardnessScalesBase
#     update_schema = schemas.HardnessScalesBase
#     get_schema = schemas.HardnessScalesGet
#
#
# class CommonHardnessService(CRUDBase):
#     model = CommonHardness
#     create_schema = schemas.CommonHardnessBase
#     update_schema = schemas.CommonHardnessBase
#     get_schema = schemas.CommonHardnessGet


class HardnessScalesCRUD(CRUDBase):
    pass


class CommonHardnessCRUD(CRUDBase):
    pass


hardness_scales_service = HardnessScalesCRUD(HardnessScales)
common_hardness_service = CommonHardnessCRUD(CommonHardness)
