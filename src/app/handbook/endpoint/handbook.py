from typing import List

from fastapi import APIRouter, Depends, Response, status

from src.app.auth.permissions import get_superuser

from src.app.user import models
from src.app.handbook import schemas
from src.app.handbook import service
from src.app.base.router_base import get_customized_router

handbook_router = APIRouter()

hs_router = get_customized_router('/hs',
                                  service.hardness_scales_service,
                                  schemas.HardnessScales_Get_Pydantic,
                                  create_schema=schemas.HardnessScales_Create_Pydantic,
                                  update_schema=schemas.HardnessScalesUpdatePydantic,
                                  name='Hardness Scale'
                                  )
ch_router = get_customized_router('/ch',
                                  service.common_hardness_service,
                                  schemas.CommonHardness_Get_Pydantic,
                                  create_schema=schemas.CommonHardness_Create_Pydantic,
                                  update_schema=schemas.CommonHardnessUpdatePydanticPydantic,
                                  name='Common Hardness')

handbook_router.include_router(hs_router, tags=['Hardness Scales'])
handbook_router.include_router(ch_router, dependencies=[Depends(get_superuser)])
