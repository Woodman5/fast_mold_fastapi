from typing import List

from fastapi import APIRouter, Depends, Response, status

from src.app.auth.permissions import get_superuser

from src.app.user import models, schemas_alchemy
from src.app.user.service_alchemy import user_role_service
from src.app.base.router_base import get_customized_router


role_router = get_customized_router('/role',
                                    user_role_service,
                                    schemas_alchemy.Role,
                                    create_schema=schemas_alchemy.Role,
                                    update_schema=schemas_alchemy.Role,
                                    name='Role'
                                    )


# CRUD for Person types

# @person_type_router.get('/', response_model=List[schemas.Role])
# async def get_all_persontypes(user: models.UserModel = Depends(get_superuser)):
#     """ Get all person types """
#     return await user_role_service.all()
#
#
# @person_type_router.get('/{pk}', response_model=schemas.Role)
# async def get_single_persontype(pk: int, user: models.UserModel = Depends(get_superuser)):
#     """ Get person type """
#     return await user_role_service.get(id=pk)
#
#
# @person_type_router.post('/', response_model=schemas.Role)
# async def create_persontype(schema: schemas.Person_Create_Pydantic, user: models.UserModel = Depends(get_superuser)):
#     """ Create person type """
#     return await user_role_service.create(schema)
#
#
# @person_type_router.put('/{pk}', response_model=schemas.Role)
# async def update_persontype(pk: int, schema: schemas.Role, user: models.UserModel = Depends(get_superuser)):
#     """ Update person type """
#     return await user_role_service.update(schema, id=pk)
#
#
# @person_type_router.delete('/{pk}', status_code=204)
# async def delete_persontype(pk: int, user: models.UserModel = Depends(get_superuser)):
#     """ Delete person type """
#     await user_role_service.delete(id=pk)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
