from typing import List

from fastapi import APIRouter, Depends, Response, status

from src.app.auth.permissions import get_superuser, get_user

from src.app.user import models
from src.app.handbook import schemas
from src.app.handbook import service
from src.app.base.router_base import get_customized_router

handbook_router = APIRouter()

hs_router = get_customized_router(url='/hs',
                                  service=service.hardness_scales_service,
                                  response_schema=schemas.HardnessScalesGet,
                                  create_schema=schemas.HardnessScalesBase,
                                  update_schema=schemas.HardnessScalesBase,
                                  name='Hardness Scale'
                                  )
ch_router = get_customized_router(url='/ch',
                                  service=service.common_hardness_service,
                                  response_schema=schemas.CommonHardnessGet,
                                  create_schema=schemas.CommonHardnessBase,
                                  update_schema=schemas.CommonHardnessBase,
                                  name='Common Hardness')

handbook_router.include_router(hs_router, tags=['Hardness Scales'])
handbook_router.include_router(ch_router, tags=['Common Hardness'])  # , dependencies=[Depends(get_user)])
