from typing import List

from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

from src.config.sqlalchemy_conf import get_db
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
    async def get_multi(*, skip: int = 0, limit: int = 100, db_session: Session = Depends(get_db)) -> str:
        """ Get all items """
        return await service.get_multi(db_session, skip, limit)

    @router.get('/{pk}', response_model=response_schema, summary=f'{name}, get single item')
    async def get_single(pk: int, db_session: Session = Depends(get_db)):
        """ Get single item """
        return await service.get(db_session, id=pk)

    @router.post('/', response_model=response_schema, summary=f'{name}, post item')
    async def create(*, schema: create_schema, db_session: Session = Depends(get_db)):
        """ Create Item """
        return await service.create(db_session, schema)

    @router.put('/{pk}', response_model=response_schema, summary=f'{name}, change item')
    async def update(*, pk: int, schema: update_schema, db_session: Session = Depends(get_db)):
        """ Update Item """
        return await service.update(db_session=db_session, obj_in=schema, id=pk)

    @router.delete('/{pk}', status_code=204, summary=f'{name}, delete item')
    async def delete(*, pk: int, db_session: Session = Depends(get_db)):
        """ Delete Item """
        await service.delete(db_session, id=pk)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router

