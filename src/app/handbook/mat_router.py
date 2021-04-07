from fastapi import APIRouter, Response, status, Depends, HTTPException

from src.app.auth.permissions import get_superuser, get_user

from src.app.handbook import schemas
from src.app.handbook import service
from src.app.handbook.mat_service import material_service
from src.app.handbook import mat_schema
from src.app.handbook.models import material

material_router = APIRouter()


@material_router.get('/all', summary='Materials, get limited items')
async def get_all():
    """ Get all items """
    return await material_service.get_all(response_model=mat_schema.MaterialGet)


@material_router.get('/{pk}', summary='Materials, get single item by Id')
async def get_single(pk: int):
    """ Get single item """
    return await material_service.get(pk=pk, response_model=mat_schema.MaterialGet)


@material_router.post('/', summary='Materials, create item')
async def create(item: mat_schema.MaterialCreate):
    """ Create Item """
    return await material_service.create(obj_in=item, response_model=mat_schema.MaterialGet)


@material_router.delete('/{pk}', status_code=204, summary='Materials, delete item')
async def delete(pk: int):
    """ Delete Item """
    await material_service.remove(pk=pk)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
