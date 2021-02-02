import re
import uuid

# from tortoise import fields, models, Tortoise

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.config.sqlalchemy_conf import Base


class User(Base):
    __tablename__ = "UserAccounts_user"

    id = Column(Integer, primary_key=True, index=True)
    user_uuid = Column(String(150), index=True, unique=True, nullable=False, default=uuid.uuid4())

    username = Column(String(30), unique=True, index=True, nullable=False)
    email = Column(String(254), unique=True, index=True, nullable=False)

    password = Column(String)

    first_name = Column(String(150), index=True, default='')
    last_name = Column(String(150), index=True, default='')
    middle_name = Column(String(150), index=True, default='')
    phone = Column(String(20), index=True, nullable=False)
    address = Column(String, index=True, default='')
    avatar = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_legal_person = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    last_login = Column(DateTime(timezone=False))
    date_joined = Column(DateTime(timezone=False))

    role_id = Column(Integer, ForeignKey('UserAccounts_persontype.id'))

    role = relationship("PersonType", back_populates="users")


class PersonType(Base):
    __tablename__ = "UserAccounts_persontype"

    id = Column(Integer, primary_key=True, index=True)
    person_type = Column(String(100), index=True, nullable=False)
    person_slug = Column(String(100), index=True, nullable=False)
    person_desc = Column(String, index=True)

    users = relationship("User", back_populates="role")


# class UserModel(models.Model):
#     """ User Model """
#
#     id = fields.IntField(pk=True)
#     user_uuid = fields.UUIDField(index=True, unique=True, null=False, default=uuid.uuid4())
#     username = fields.CharField(index=True, unique=True, null=False, max_length=30)
#     email = fields.CharField(index=True, unique=True, null=False, max_length=255)
#     password = fields.CharField(null=False, max_length=255)
#     is_active = fields.BooleanField(default=True, null=False)
#     is_superuser = fields.BooleanField(default=False, null=False)
#     is_verified = fields.BooleanField(default=False, null=False)
#     first_name = fields.CharField(null=False, max_length=100)
#     last_name = fields.CharField(null=False, max_length=150)
#     middle_name = fields.CharField(null=True, max_length=100)
#     phone = fields.CharField(null=False, max_length=15)
#     address = fields.TextField(null=True)
#     is_staff = fields.BooleanField(default=False, null=False)
#     is_legal_person = fields.BooleanField(default=False, null=False)
#     last_login = fields.DatetimeField(null=True)
#     date_joined = fields.DatetimeField(auto_now_add=True)
#     avatar = fields.CharField(max_length=255, null=True)
#
#     # модель надо указать так: ключ словаря (models) как в файле main при регистрации черепахи
#     # в пункте modules и далее после точки название модели которое есть в файлах,
#     # перечисленных в значении (это список) этого ключа
#     role: fields.ForeignKeyRelation["PersonType"] = fields.ForeignKeyField('models.PersonType',
#                                                                            on_delete='CASCADE',
#                                                                            default=4,
#                                                                            related_name='usermodels'
#                                                                            )
#
#     person_type = fields.ReverseRelation["PersonType"]
#
#     def __str__(self):
#         return self.username
#
#     async def to_dict(self):
#         d = {}
#         for field in self._meta.db_fields:
#             d[field] = getattr(self, field)
#         for field in self._meta.backward_fk_fields:
#             d[field] = await getattr(self, field).all().values()
#         return d
#
#     class Meta:
#         table = 'UserAccounts_user'
#         table_description = "User"
#
#     class PydanticMeta:
#         backward_relations = True,
#
#
# class PersonType(models.Model):
#     """Person role model"""
#
#     id = fields.IntField(pk=True)
#     person_type = fields.CharField(description='User type', max_length=100)
#     person_slug = fields.CharField(description='Identifier', max_length=100)
#     person_desc = fields.TextField(description='Description', default='', null=True)
#
#     usermodels: fields.ReverseRelation[UserModel]
#
#     class Meta:
#         table = 'UserAccounts_persontype'
#         table_description = "User type"
#
#     def __str__(self):
#         return self.person_type
#
#
# # Необходимо для получения связанных моделей через "pydantic_model_creator".
# # Команда должны быть перед "pydantic_model_creator".
# Tortoise.init_models(["src.app.user.models"], "models")

