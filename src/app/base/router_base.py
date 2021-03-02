from typing import List, Optional, Dict, Type

from fastapi import APIRouter, Response, status, Depends, HTTPException
from pydantic import BaseModel

from src.app.base.service_base import (
    CreateSchemaType,
    UpdateSchemaType,
    ResponseSchemaType,
    CRUDBase
)


def get_customized_router(url: str,
                          service: CRUDBase,
                          response_schema: Type[BaseModel],
                          create_schema: Type[BaseModel],
                          update_schema: Type[BaseModel] = None,
                          name: str = 'Item',
                          dependencies=None,
                          ):

    if dependencies is None:
        dependencies = []

    router = APIRouter(
        prefix=f"{url}",
        dependencies=dependencies,
    )

    if not update_schema:
        update_schema = create_schema

    @router.get('/', response_model=List[response_schema], summary=f'{name}, get limited items')
    async def get_multi(*, skip: int = 0, limit: int = 100):
        """ Get limited items """
        return await service.get_multi(skip=skip, limit=limit)

    @router.get('/all', response_model=List[response_schema], summary=f'{name}, get all items')
    async def get_all():
        """ Get all items """
        return await service.get_all()

    @router.get('/pages', response_model=List[response_schema], summary=f'{name}, get items with pagination')
    async def get_by_page(page: int = 1, page_size: int = None):
        """ Get items with pagination """
        page_size = 20 if not page_size else page_size
        return await service.get_page(page=page, page_size=page_size)

    @router.get('/{pk}', response_model=response_schema, summary=f'{name}, get single item by Id')
    async def get_single(pk: int):
        """ Get single item """
        return await service.get(pk=pk)

    @router.post('/', response_model=response_schema, summary=f'{name}, post item')
    async def create(item: create_schema):
        """ Create Item """
        try:
            return await service.create(obj_in=item)
        except Exception as e:
            raise HTTPException(status_code=400, detail=e.detail)

    @router.put('/{pk}', response_model=response_schema, summary=f'{name}, change item')
    async def update(pk: int, schema: update_schema):
        """ Update Item """
        return await service.update(obj_in=schema, pk=pk)

    @router.delete('/{pk}', status_code=204, summary=f'{name}, delete item')
    async def delete(pk: int):
        """ Delete Item """
        try:
            await service.remove(pk=pk)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f'Deletion failed. {e.detail}')

    return router
