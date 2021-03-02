from typing import List, Optional, Generic, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
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

    async def get_item(self, pk: int):
        return await self.model.objects.get(id=pk)

    async def get(self, pk: int, response_model: ResponseSchemaType) -> Union[BaseModel, HTTPException]:
        item = await self.get_item(pk=pk)
        if not item.item_removed:
            return response_model(**item.dict())
        else:
            return HTTPException(status_code=status.HTTP_410_GONE)

    async def get_select(self, pk: int) -> Union[BaseModel, Dict]:
        return await self.get(pk=pk)

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        return await self.model.objects.offset(skip).limit(limit).exclude(item_removed=True).all()

    async def get_page(self, page, page_size) -> Sequence[Optional[Model]]:
        return await self.model.objects.paginate(page, page_size).exclude(item_removed=True).all()

    async def get_all(self) -> Sequence[Optional[Model]]:
        return await self.model.objects.exclude(item_removed=True).all()

    async def create(self, obj_in: CreateSchemaType, response_model: ResponseSchemaType) -> Union[
                                                                                            BaseModel, HTTPException]:
        name_exists = await self.model.objects.filter(name=obj_in.name).exists()
        slug_exists = await self.model.objects.filter(slug=obj_in.slug).exists()
        if not name_exists and not slug_exists:
            item = obj_in.dict()
            if 'created' in self.model.__fields__.keys():
                item['created'] = datetime.now()
            try:
                created_model = await self.model.objects.create(**item)
                return response_model(**created_model.dict())
            except Exception as e:
                print(e)
        else:
            return HTTPException(status_code=status.HTTP_409_CONFLICT)

    async def update(self, pk: int, obj_in: UpdateSchemaType, response_model: ResponseSchemaType) -> BaseModel:
        item = await self.get_item(pk=pk)
        obj_in = obj_in.dict(exclude_unset=True)
        if 'updated' in self.model.__fields__.keys():
            obj_in['updated'] = datetime.now()
        await item.update(**obj_in)
        return response_model(**item.dict())

    async def remove(self, pk: int) -> int:
        if 'item_removed' in self.model.__fields__.keys():
            item = await self.get_item(pk=pk)
            time_for_name = int(datetime.now().timestamp())
            new_name = f'deletedrow_{item.name}_{time_for_name}'
            new_slug = f'deletedrow_{item.slug}_{time_for_name}'
            await item.update(name=new_name, slug=new_slug, item_removed=True)
        else:
            await self.model.objects.delete(id=pk)
        return 1
