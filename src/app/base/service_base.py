from typing import List, Optional, Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

# from src.config.sqlalchemy_conf import Base
from ormar import Model

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)
ResponseSchemaType = TypeVar("ResponseSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    # @role_router.get("/role/", response_model=List[schemas_alchemy.RoleBase])
    # async def get_items():
    #     items = await models.Role.objects.all()
    #     return items

    async def get(self, id: int) -> Optional[ModelType]:
        return await self.model.objects.get(id=id)

    # async def get_by(self, kwargs) -> Optional[ModelType]:
    #     print(**kwargs)
    #     return await self.model.objects.get(**kwargs)

    async def get_multi(self, skip=0, limit=100) -> List[ModelType]:
        return await self.model.objects.offset(skip).limit(limit).all()

    # def create(self, *, db_session: Session, obj_in: CreateSchemaType) -> ModelType:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj
    #
    # def update(
    #     self, db_session: Session, *, id: int, obj_in: UpdateSchemaType
    # ) -> ModelType:
    #     db_obj = db_session.query(self.model).get(id)
    #     obj_data = jsonable_encoder(db_obj)
    #     update_data = obj_in.dict(skip_defaults=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db_session.add(db_obj)
    #     db_session.commit()
    #     db_session.refresh(db_obj)
    #     return db_obj
    #
    # def remove(self, db_session: Session, *, id: int) -> ModelType:
    #     obj = db_session.query(self.model).get(id)
    #     db_session.delete(obj)
    #     db_session.commit()
    #     return obj
