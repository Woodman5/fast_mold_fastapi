from src.config.sqlalchemy_conf import Base
from sqlalchemy import Column, Integer, String, Boolean, Text

from sqlalchemy_utils import Timestamp, generic_repr


class NameMixin:
    name = Column(String(200), unique=True, index=True, nullable=False)
    slug = Column(String(200), unique=True, index=True, nullable=False)


class DescriptionMixin:
    description = Column(Text, index=True)


class SoftDelete:
    item_removed = Column(Boolean, default=False)


class AbstractBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)


@generic_repr
class Model(AbstractBaseModel, NameMixin, Timestamp, SoftDelete, DescriptionMixin):

    def __str__(self):
        return f"{type(self).__name__}(id: {self.id}, name: {self.name}"


