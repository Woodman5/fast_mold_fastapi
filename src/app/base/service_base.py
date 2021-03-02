from typing import List, Optional, Generic, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from src.config.sqlalchemy_conf import Base
from ormar import Model, QuerySet

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)
ResponseSchemaType = Type[BaseModel]


class CRUDBase:

    def __init__(self, model: Type[Model]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get(self, pk: int, response_model: ResponseSchemaType) -> Union[BaseModel, Dict]:
        item = await self.model.objects.get(id=pk)
        if not item.item_removed:
            return response_model(**item.dict())
        else:
            return {'msg': 'Item removed'}

    async def get_select(self, pk: int) -> Union[BaseModel, Dict]:
        return await self.get(pk=pk)

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        return await self.model.objects.offset(skip).limit(limit).exclude(item_removed=True).all()

    async def get_page(self, page, page_size) -> Sequence[Optional[Model]]:
        return await self.model.objects.paginate(page, page_size).exclude(item_removed=True).all()

    async def get_all(self) -> Sequence[Optional[Model]]:
        return await self.model.objects.exclude(item_removed=True).all()

    async def create(self, obj_in: CreateSchemaType) -> Model:
        item = obj_in.dict()
        if 'created' in self.model.__fields__.keys():
            item['created'] = datetime.now()
        try:
            return await self.model.objects.create(**item)
        except Exception as e:
            print(e)

    async def update(self, pk: int, obj_in: UpdateSchemaType) -> Model:
        item = await self.model.objects.get(id=pk)
        obj_in = obj_in.dict(exclude_unset=True)
        if 'updated' in self.model.__fields__.keys():
            obj_in['updated'] = datetime.now()
        await item.update(**obj_in)
        return item

    async def remove(self, pk: int) -> int:
        if 'item_removed' in self.model.__fields__.keys():
            item = await self.model.objects.get(id=pk)
            await item.update(item_removed=True)
        else:
            await self.model.objects.delete(id=pk)
        return 1

