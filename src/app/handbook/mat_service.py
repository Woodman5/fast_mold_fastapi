from typing import List, Optional, Set, TypeVar, Type, Sequence, Union, Dict
from datetime import datetime, timezone
import pytz

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ormar import Model, QuerySet
from ormar.exceptions import NoMatch, MultipleMatches

from .models.material import Material
from src.app.base.service_base import check_name_slug

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)
ResponseSchemaType = Type[BaseModel]


class MaterialCRUD:

    def __init__(self):
        self.model = Material
        self.f_relations = (
            'manufacturer',
            'mat_type',
            'mat',
            'mech',
            'p3d',
            'gfrp',
            'filler',
            'technology',
        )
        self.m2m_relations = (
            'type_technology',
            'color',
            'component',
        )
        self.one_name = 'material'
        self.pl_name = 'materials'


material_service = MaterialCRUD()



