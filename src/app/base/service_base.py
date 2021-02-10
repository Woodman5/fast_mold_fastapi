from typing import List, Optional, Generic, TypeVar, Type, Sequence

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from src.config.sqlalchemy_conf import Base
from ormar import Model, QuerySet

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=BaseModel)


class CRUDBase:

    def __init__(self, model: Type[Model]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    async def get(self, pk: int) -> Optional[Model]:
        return await self.model.objects.get(id=pk)

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        return await self.model.objects.offset(skip).limit(limit).all()

    async def get_page(self, page, page_size) -> Sequence[Optional[Model]]:
        return await self.model.objects.paginate(page, page_size).all()

    async def get_all(self) -> Sequence[Optional[Model]]:
        return await self.model.objects.all()

    async def create(self, obj_in: CreateSchemaType) -> Model:
        item = self.model(**obj_in.dict())
        return await item.save()

    async def update(self, pk: int, obj_in: UpdateSchemaType) -> Model:
        item = await self.model.objects.get(id=pk)
        await item.update(**obj_in.dict(exclude_unset=True))
        return item

    async def remove(self, pk: int) -> int:
        return await self.model.objects.delete(id=pk)

