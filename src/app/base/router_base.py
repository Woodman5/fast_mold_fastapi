from typing import List

from fastapi import APIRouter, Response, status

from src.app.base.service_base import (
    CreateSchemaType,
    UpdateSchemaType,
    ResponseSchemaType
)


def get_customized_router(url: str,
                          service,
                          response_schema: ResponseSchemaType,
                          create_schema: CreateSchemaType,
                          update_schema: UpdateSchemaType = None,
                          name='Item',
                          ):

    router = APIRouter(prefix=f"{url}")

    if not update_schema:
        update_schema = create_schema

    @router.get('/', response_model=List[response_schema], summary=f'{name}, get all items')
    async def get_all() -> str:
        """ Get all items """
        return await service.all()

    @router.get('/{pk}', response_model=response_schema, summary=f'{name}, get single item')
    async def get_single(pk: int):
        """ Get single item """
        return await service.get(id=pk)

    @router.post('/', response_model=response_schema, summary=f'{name}, post item')
    async def create(schema: create_schema):
        """ Create Item """
        return await service.create(schema)

    @router.put('/{pk}', response_model=response_schema, summary=f'{name}, change item')
    async def update(pk: int, schema: update_schema):
        """ Update Item """
        return await service.update(schema, id=pk)

    @router.delete('/{pk}', status_code=204, summary=f'{name}, delete item')
    async def delete(pk: int):
        """ Delete Item """
        await service.delete(id=pk)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router

