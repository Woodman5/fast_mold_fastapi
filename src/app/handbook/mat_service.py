from pprint import pprint
from typing import List, Optional, Set, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime, timezone
import pytz

from decimal import Decimal

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ormar import Model, QuerySet
from ormar.exceptions import NoMatch, MultipleMatches

from .models.material import (
    Material,
    ToolMan,
    MaterialType,
    MatParam,
    MechanicalChars,
    Printing3D,
    GFRParams,
    MineralFiller,
    TechnologyChars,
    TypeTech,
    Color,
    Component,
    CustomMatParam,
)
from src.app.base.service_base import (
    CRUDRelationsM2M,
    check_name_slug)


CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)
ResponseSchemaType = Type[BaseModel]


# removing all empty (None, "", []) data from dictionaries. Zeros are keeping.
def clear_dict(data: Dict) -> Dict:
    temp_data = data.copy()
    for k, v in temp_data.items():
        if isinstance(v, dict):
            clear_dict(v)
        if k == 'item_removed' or not v and not isinstance(v, (int, float, Decimal)):
            data.pop(k)
    return data


class MaterialCRUD(CRUDRelationsM2M):

    rel = [
        # this models must exist in DB prior material creation
        'manufacturer',
        'mat_type',

        # this models need to create in DB prior material creation
        'mat',
        'mech',
        'p3d',
        'gfrp',
        'filler',
        'tech_param',

        # this M2M models must exist in DB prior material creation
        'type_technology',
        'matcolor',
        'matcomponent',
        'cust_param',
    ]

    m2m_rel = [
        ('type_technology', TypeTech, 'Technology types'),
        ('matcolor', Color, 'Colors'),
        ('matcomponent', Component, 'Components'),
        ('cust_param', CustomMatParam, 'Custom parameters'),
    ]

    fields_to_del = (
        'materialtypetech',
        'materialcolor',
        'materialcomponent',
        'materialcustommatparam',
    )

    rel_to_be_created = (
        MatParam,
        MechanicalChars,
        Printing3D,
        GFRParams,
        MineralFiller,
        TechnologyChars,
    )

    one_name = 'material'
    pl_name = 'materials'
    rel_name = ''

    def __init__(self):
        super().__init__(Material, Color, self.rel, self.rel_name, self.pl_name)

    async def get(self, pk: int, response_model: ResponseSchemaType) -> Union[BaseModel, HTTPException]:
        item = await self.get_item(pk=pk)
        print('Original GET ---', )
        # pprint(item.dict())
        item_dict = self.remove_field(item, self.rel[-4::], self.fields_to_del)
        data = self.construct_data(item_dict, response_model)
        return data

    async def create(self, obj_in: CreateSchemaType, response_model: ResponseSchemaType):
        if not await check_name_slug(self.model, obj_in.name, obj_in.slug):
            m2m_relations_list = []
            pprint(obj_in)
            data = obj_in.dict(exclude_unset=True, exclude_none=True, exclude_defaults=True)
            print('--1--')
            pprint(data)
            data = clear_dict(data)
            print('--2--')
            pprint(data)
            for key, rel in enumerate(self.rel[2:-4:]):
                print('--rel--', rel)
                model_data = data.pop(rel, None)
                if model_data:
                    pprint(model_data)
                    pprint(self.rel_to_be_created[key])
                    db_model = await self.rel_to_be_created[key].objects.create(**model_data)
                    data[rel] = {'id': db_model.id}
                    # print('--id--', data[rel])

            for m2m in self.m2m_rel:
                if m2m[0] not in data:
                    continue
                relation_list = data.pop(m2m[0])
                relation_items = await m2m[1].objects.filter(id__in=relation_list).all()
                if not relation_items:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{m2m[2]} not found')

                m2m_relations_list.append((m2m[0], relation_items))

            data['created'] = datetime.now(timezone.utc)
            print('Original POST ---', )
            pprint(data)
            try:
                created_model = await self.model.objects.create(**data)
            except Exception as e:
                print(e)
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Model creation failed, {e}')

            for item in m2m_relations_list:
                field = getattr(created_model, item[0])
                for model in item[1]:
                    await field.add(model)

            data = self.construct_data(created_model, response_model)
            return data

        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Such fields already exists')


material_service = MaterialCRUD()



