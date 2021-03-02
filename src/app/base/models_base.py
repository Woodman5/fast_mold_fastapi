import datetime

import ormar
from src.config.ormar_settings import database, metadata


class NameMixin:
    name: str = ormar.String(max_length=200, unique=True, index=True, nullable=False)
    slug: str = ormar.String(max_length=200, unique=True, index=True, nullable=False)


class DescriptionMixin:
    description: str = ormar.Text(index=True, nullable=True)


class SoftDeleteMixin:
    item_removed = ormar.Boolean(default=False)


class TimestampMixin:
    created: datetime.datetime = ormar.DateTime(nullable=False)
    updated: datetime.datetime = ormar.DateTime(nullable=True)


class AbstractBaseModel(ormar.Model):

    class Meta:
        abstract = True
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)

    def __str__(self):
        return f"{type(self).__name__}(id: {self.id}, name: {self.name})"

    def __repr__(self):
        return f"<{type(self).__name__}(id: {self.id})>"


class ModelMixin(ormar.Model, NameMixin, DescriptionMixin, SoftDeleteMixin, TimestampMixin):

    class Meta:
        abstract = True




