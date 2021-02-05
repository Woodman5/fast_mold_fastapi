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
    def get_multi(*, skip: int = 0, limit: int = 100, db_session: Session = Depends(get_db)) -> str:
        """ Get all items """
        return service.get_multi(db_session=db_session, skip=skip, limit=limit)

    @router.get('/{pk}', response_model=response_schema, summary=f'{name}, get single item')
    def get_single(pk: int, db_session: Session = Depends(get_db)):
        """ Get single item """
        return service.get(db_session=db_session, id=pk)

    @router.post('/', response_model=response_schema, summary=f'{name}, post item')
    def create(*, schema: create_schema, db_session: Session = Depends(get_db)):
        """ Create Item """
        return service.create(db_session=db_session, obj_in=schema)

    @router.put('/{pk}', response_model=response_schema, summary=f'{name}, change item')
    def update(*, pk: int, schema: update_schema, db_session: Session = Depends(get_db)):
        """ Update Item """
        return service.update(db_session=db_session, obj_in=schema, id=pk)

    @router.delete('/{pk}', status_code=204, summary=f'{name}, delete item')
    def delete(*, pk: int, db_session: Session = Depends(get_db)):
        """ Delete Item """
        service.remove(db_session=db_session, id=pk)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router

