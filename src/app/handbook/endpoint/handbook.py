from fastapi import APIRouter

from src.app.auth.permissions import get_superuser, get_user

from src.app.handbook import schemas
from src.app.handbook import service
from src.app.base.router_base import get_customized_router

handbook_router = APIRouter()

hs_router = get_customized_router(url='/hs',
                                  service=service.hardness_scales_service,
                                  response_schema=schemas.HardnessScalesGet,
                                  create_schema=schemas.HardnessScalesCreate,
                                  update_schema=schemas.HardnessScalesUpdate,
                                  name='Hardness Scale'
                                  )
ch_router = get_customized_router(url='/ch',
                                  service=service.common_hardness_service,
                                  response_schema=schemas.CommonHardnessGet,
                                  create_schema=schemas.CommonHardnessCreate,
                                  update_schema=schemas.CommonHardnessUpdate,
                                  name='Common Hardness')
status_router = get_customized_router(url='/status',
                                      service=service.status_service,
                                      response_schema=schemas.StatusGet,
                                      create_schema=schemas.StatusCreate,
                                      update_schema=schemas.StatusUpdate,
                                      name='Status'
                                      )
technology_router = get_customized_router(url='/technology',
                                          service=service.technology_service,
                                          response_schema=schemas.TechnologyGet,
                                          create_schema=schemas.TechnologyCreate,
                                          update_schema=schemas.TechnologyUpdate,
                                          name='Technology'
                                          )

toolclass_router = get_customized_router(url='/toolclass',
                                         service=service.toolclass_service,
                                         response_schema=schemas.ToolClassGet,
                                         create_schema=schemas.ToolClassCreate,
                                         update_schema=schemas.ToolClassUpdate,
                                         name='Tool Class'
                                         )

materialtype_router = get_customized_router(url='/mattype',
                                            service=service.materialtype_service,
                                            response_schema=schemas.MaterialTypeGet,
                                            create_schema=schemas.MaterialTypeCreate,
                                            update_schema=schemas.MaterialTypeUpdate,
                                            name='Material Type'
                                            )

imitationmaterial_router = get_customized_router(url='/imitmat',
                                                 service=service.imitationmaterial_service,
                                                 response_schema=schemas.ImitationMaterialGet,
                                                 create_schema=schemas.ImitationMaterialCreate,
                                                 update_schema=schemas.ImitationMaterialUpdate,
                                                 name='Imitation Material'
                                                 )

chemicalresistance_router = get_customized_router(url='/chemresist',
                                                  service=service.chemicalresistance_service,
                                                  response_schema=schemas.ChemicalResistanceGet,
                                                  create_schema=schemas.ChemicalResistanceCreate,
                                                  update_schema=schemas.ChemicalResistanceUpdate,
                                                  name='Chemical Resistance'
                                                  )

measuringstandards_router = get_customized_router(url='/measuring-standards',
                                                  service=service.measuringstandards_service,
                                                  response_schema=schemas.MeasuringStandardsGet,
                                                  create_schema=schemas.MeasuringStandardsCreate,
                                                  update_schema=schemas.MeasuringStandardsUpdate,
                                                  name='Measuring Standard'
                                                  )

colors_router = get_customized_router(url='/colors',
                                      service=service.colors_service,
                                      response_schema=schemas.ColorsGet,
                                      create_schema=schemas.ColorsCreate,
                                      update_schema=schemas.ColorsUpdate,
                                      name='Color'
                                      )


handbook_router.include_router(hs_router, tags=['Hardness Scales'])
handbook_router.include_router(ch_router, tags=['Common Hardness'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(status_router, tags=['Statuses'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(toolclass_router, tags=['Tool Classes'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(materialtype_router, tags=['Material Types'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(imitationmaterial_router, tags=['Imitation Materials'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(technology_router, tags=['Technologies'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(chemicalresistance_router, tags=['Chemical Resistances'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(measuringstandards_router, tags=['Measuring Standards'])  # , dependencies=[Depends(get_user)])
handbook_router.include_router(colors_router, tags=['Colors'])  # , dependencies=[Depends(get_user)])
