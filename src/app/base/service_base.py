from typing import List, Optional, Set, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime, timezone
import pytz

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


async def check_name_slug(model: Type[Model], name: str, slug: str) -> bool:
    name_exists = await model.objects.filter(name=name).exists()
    slug_exists = await model.objects.filter(slug=slug).exists()
    if name_exists or slug_exists:
        return True
    return False


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
        :param exclude: fields to exclude
        :param item: Data from DB
        :param schema: Pydantic schema
        :return: Pydantic model based on provided scheme without validation
        """
        if not isinstance(item, dict):
            item = item.dict()
        # print('-----', item, sep='\n')
        fields_to_del = set(item.keys()) - set(schema.__fields__.keys())
        # print('-----', fields_to_del, '-----', sep='\n')
        for key in fields_to_del:
            item.pop(key)
        return schema.construct(**item)

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
        if not await check_name_slug(self.model, obj_in.name, obj_in.slug):
            item = obj_in.dict()
            if 'created' in self.model.__fields__.keys():
                item['created'] = datetime.now(timezone.utc)
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
            time_for_name = int(datetime.now(timezone.utc).timestamp())
            new_name = f'deletedrow_{item.name}_{time_for_name}'
            new_slug = f'deletedrow_{item.slug}_{time_for_name}'
            await item.update(name=new_name, slug=new_slug, item_removed=True)
        else:
            await self.model.objects.delete(id=pk)
        return 1


class CRUDRelations(CRUDBase):

    def __init__(self, model: Type[Model], rel: List[str], exclude: Union[List[str], None] = None):
        super().__init__(model)
        if exclude is None:
            exclude = []
        self.rel = rel
        self.exclude = exclude

    async def get_item(self, pk: int):
        try:
            item = await self.model.objects.select_related(self.rel).exclude_fields(self.exclude).get(id=pk)
        except NoMatch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
        except MultipleMatches:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail='Found more than one item')
        except Exception as e:
            print(e)
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


class CRUDRelationsM2M(CRUDRelations):

    def __init__(self,
                 model: Type[Model],
                 rel_model: Type[Model],
                 rel: List[str],
                 rel_name: str,
                 pl_name: str,
                 exclude: Union[List[str], None] = None):
        super().__init__(model, rel, exclude)
        self.rel_name = rel_name
        self.pl_name = pl_name
        self.rel_model = rel_model

    async def set_m2m_relation(self,
                               data_in: List[int],
                               model: Type[Model],
                               name: str,
                               relation_field,
                               update: bool = False,
                               ):
        m2m_items = await model.objects.filter(id__in=data_in).all()
        if not m2m_items:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{name} not found')

        if update:
            await relation_field.clear()

        for item in m2m_items:
            await relation_field.add(item)

    def remove_field(self, item, key, field):
        item_dict = item.dict()
        for key in item_dict[key]:
            key.pop(field)
        # print('------', item_dict, sep='\n')
        return item_dict

    async def get(self, pk: int, response_model: ResponseSchemaType) -> Union[BaseModel, HTTPException]:
        item = await self.get_item(pk=pk)
        item_dict = self.remove_field(item, self.rel[0], self.rel_name)
        data = self.construct_data(item_dict, response_model)
        return data

    async def create_item(self, obj_in):
        if not await check_name_slug(self.model, obj_in.name, obj_in.slug):
            relation_list = obj_in.dict().pop(self.rel[0])
            relation_items = await self.rel_model.objects.filter(id__in=relation_list).all()
            if not relation_items:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{self.pl_name} not found')

            try:
                created_model = await self.model.objects.create(**obj_in.dict(exclude={self.rel[0]}))
                return created_model, relation_items
            except Exception as e:
                print(e)
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Model creation failed')
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Such fields already exists')

    async def update_item(self, pk: int, obj_in: UpdateSchemaType, rel_field):
        item = await self.get_item(pk=pk)
        obj_in = obj_in.dict(exclude_unset=True)
        if 'updated' in self.model.__fields__.keys():
            obj_in['updated'] = datetime.now(timezone.utc)

        new_rels = obj_in.pop(self.rel[0], None)

        if obj_in:
            await item.update(**obj_in)

        if new_rels:
            await self.set_m2m_relation(new_rels, self.rel_model, self.pl_name, rel_field, update=True)

        item = await self.get_item(pk=pk)
        item_dict = self.remove_field(item, self.rel[0], self.rel_name)
        return item_dict











