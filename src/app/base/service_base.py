from typing import List, Optional, Generic, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from src.config.sqlalchemy_conf import Base
from ormar import Model, QuerySet
from ormar.exceptions import NoMatch, MultipleMatches

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
        try:
            item = await self.model.objects.get(id=pk)
        except NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
        except MultipleMatches:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Found more than one item')
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)

        if 'item_removed' in self.model.__fields__.keys() and item.item_removed:
            raise HTTPException(status_code=status.HTTP_410_GONE, detail='Item removed')
        return item

    @staticmethod
    def construct_data(item, schema):
        """
        Method removes unnecessary attributes from DB data to correspond to provided schema.
        :param item: Data from DB
        :param schema: Pydantic schema
        :return: Pydantic model based on provided scheme without validation
        """
        data = item.dict()
        fields_to_del = set(data.keys()) - set(schema.__fields__.keys())
        for key in fields_to_del:
            data.pop(key)
        return schema.construct(**data)

    async def get(self, pk: int, response_model: ResponseSchemaType) -> Union[BaseModel, HTTPException]:
        item = await self.get_item(pk=pk)
        data = self.construct_data(item, response_model)
        return data

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.offset(skip).limit(limit).exclude(item_removed=True).all()
        else:
            return await self.model.objects.offset(skip).limit(limit).all()

    async def get_page(self, page, page_size) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.paginate(page, page_size).exclude(item_removed=True).all()
        else:
            return await self.model.objects.paginate(page, page_size).all()

    async def get_all(self) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.exclude(item_removed=True).all()
        else:
            return await self.model.objects.all()

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
                data = self.construct_data(created_model, response_model)
                return data
            except Exception as e:
                print(e)
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Such fields already exists')

    async def update(self, pk: int, obj_in: UpdateSchemaType, response_model: ResponseSchemaType) -> BaseModel:
        item = await self.get_item(pk=pk)
        obj_in = obj_in.dict(exclude_unset=True)
        if 'updated' in self.model.__fields__.keys():
            obj_in['updated'] = datetime.now()
        await item.update(**obj_in)
        data = self.construct_data(item, response_model)
        return data

    async def remove(self, pk: int) -> int:
        if not await self.model.objects.filter(pk=pk).exists():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
        if 'item_removed' in self.model.__fields__.keys():
            item = await self.get_item(pk=pk)
            time_for_name = int(datetime.now().timestamp())
            new_name = f'deletedrow_{item.name}_{time_for_name}'
            new_slug = f'deletedrow_{item.slug}_{time_for_name}'
            await item.update(name=new_name, slug=new_slug, item_removed=True)
        else:
            await self.model.objects.delete(id=pk)
        return 1


class CRUDRelations(CRUDBase):

    def __init__(self, model: Type[Model], rel: str):
        super().__init__(model)
        self.rel = rel

    async def get_item(self, pk: int):
        try:
            item = await self.model.objects.select_related(self.rel).get(id=pk)
        except NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
        except MultipleMatches:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Found more than one item')
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)

        if 'item_removed' in self.model.__fields__.keys() and item.item_removed:
            raise HTTPException(status_code=status.HTTP_410_GONE, detail='Item removed')
        return item

    async def get_multi(self, skip=0, limit=100) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.offset(skip).limit(limit).exclude(item_removed=True).select_related(self.rel).all()
        else:
            return await self.model.objects.offset(skip).limit(limit).select_related(self.rel).all()

    async def get_page(self, page, page_size) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.paginate(page, page_size).exclude(item_removed=True).select_related(self.rel).all()
        else:
            return await self.model.objects.paginate(page, page_size).select_related(self.rel).all()

    async def get_all(self) -> Sequence[Optional[Model]]:
        if 'item_removed' in self.model.__fields__.keys():
            return await self.model.objects.exclude(item_removed=True).select_related(self.rel).all()
        else:
            return await self.model.objects.select_related(self.rel).all()
