from typing import List

from fastapi import APIRouter, Depends

from src.app.auth.permissions import get_superuser

from src.app.user import models, schemas, service


admin_router = APIRouter()


@admin_router.get('', response_model=List[schemas.UserForAdminInDB])
async def get_all_users(user: models.UserModel = Depends(get_superuser)):
    """ Get all users """
    return await service.user_s.all()


@admin_router.get('/{pk}', response_model=schemas.UserForAdminInDB)
async def get_single_user(pk: int, user: models.UserModel = Depends(get_superuser)):
    """ Get user """
    return await service.user_s.get(id=pk)
    # return await models.UserModel.get(id=pk).prefetch_related('role')


@admin_router.get('/pt/{pk}', response_model=schemas.Person_Pydantic)
async def get_single_persontype(pk: int):
    """ Get person type """
    return await service.pt_s.get(id=pk)


@admin_router.post('', response_model=schemas.UserForAdminInDB)
async def create_user(schema: schemas.User_Admin_Create_Pydantic, user: models.UserModel = Depends(get_superuser)):
    """ Create user """
    # TODO исправить создание юзера, параметры: is_active & is_superuser & role & so on
    return await service.user_s.create_user(schema)


@admin_router.put('/{pk}', response_model=schemas.UserForAdminInDB)
async def update_user(pk: int, schema: schemas.UserUpdate, user: models.UserModel = Depends(get_superuser)):
    """ Update user """
    return await service.user_s.update(schema, id=pk)


@admin_router.delete('/{pk}', status_code=204)
async def delete_user(pk: int, user: models.UserModel = Depends(get_superuser)):
    """ Delete user """
    return await service.user_s.delete(id=pk)
