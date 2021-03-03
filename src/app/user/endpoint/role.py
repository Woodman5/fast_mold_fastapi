from typing import List

from fastapi import APIRouter, Depends, Response, status

from src.app.user import models, schemas
from src.app.user.service import user_role_service
from src.app.base.router_base import get_customized_router
from src.app.auth.permissions import get_superuser, get_user


role_router = get_customized_router(url='/role',
                                    service=user_role_service,
                                    response_schema=schemas.RoleGet,
                                    create_schema=schemas.RoleCreate,
                                    update_schema=schemas.RoleUpdate,
                                    name='Role',
                                    dependencies=[Depends(get_superuser)],
                                    )

# role_router = APIRouter()
#
#
# @role_router.get("/role/", response_model=List[schemas_alchemy.RoleCreate])
# async def get_items():
#     items = await models.Role.objects.all()
#     return items
#
#
# @role_router.get("/role/{item_id}", response_model=schemas_alchemy.RoleCreate)
# async def get_items(item_id: int):
#     item = await models.Role.objects.get(pk=item_id)
#     return item
#
#
# @role_router.post("/role/", response_model=schemas_alchemy.Role)
# async def create_item(role: schemas_alchemy.RoleCreate):
#     # await role.save()
#     role_item = await models.Role.objects.create(**role.dict())
#     return role_item


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
