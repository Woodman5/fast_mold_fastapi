import datetime
import ormar
from src.app.base.models_base import (
    AbstractBaseModel,
    ModelMixin,
    SoftDeleteMixin,
    TimestampMixin,
    NameMixin,
    DescriptionMixin,
)


class HardnessScales(AbstractBaseModel, ModelMixin):
    """ Hardness Scales Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_hardnessscales"

    hs_min = ormar.Integer(default=0)
    hs_max = ormar.Integer(default=100)
    hs_units = ormar.String(max_length=30, nullable=True)


class CommonHardness(AbstractBaseModel, ModelMixin):
    """ Human readable hardness Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_commonhardness"



