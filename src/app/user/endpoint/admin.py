from typing import List

from fastapi import APIRouter, Depends, Response, status

from src.app.auth.permissions import get_superuser

from src.app.user import models, schemas
from src.app.user.service import user_service


admin_router = APIRouter()


# CRUD for Users

@admin_router.get('', response_model=List[schemas.UserPydantic])
async def get_all_users(user: models.UserModel = Depends(get_superuser)):
    """ Get all users """
    return await user_service.all()


@admin_router.get('/{pk}', response_model=schemas.UserPydantic)
async def get_single_user(pk: int, user: models.UserModel = Depends(get_superuser)):
    """ Get user """
    return await user_service.get(id=pk)


@admin_router.post('', response_model=schemas.UserPydantic)
async def create_user_by_admin(schema: schemas.UserRegistrationByAdminPydantic, user: models.UserModel = Depends(get_superuser)):
    """ Create user """
    # TODO исправить создание юзера, параметры: is_active & is_superuser & role & so on
    return await user_service.create_user_by_admin(schema)


@admin_router.put('/{pk}', response_model=schemas.UserPydantic)
async def update_user(pk: int, schema: schemas.UserUpdate, user: models.UserModel = Depends(get_superuser)):
    """ Update user """
    return await user_service.update(schema, id=pk)


@admin_router.delete('/{pk}', status_code=204)
async def delete_user(pk: int, user: models.UserModel = Depends(get_superuser)):
    """ Delete user """
    await user_service.delete(id=pk)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

