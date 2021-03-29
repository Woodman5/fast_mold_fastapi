import datetime
import ormar
from src.app.base.models_base import (
    AbstractBaseModel,
    ModelMixin,
    SoftDeleteMixin,
    TimestampMixin,
    NameMixin,
    DescriptionMixin,
    ShortDescriptionMixin,
    UrlMixin,
)
from . import common_data
from .mat_properties import (
    MeasuringStandards,
)


class Characteristic(AbstractBaseModel, NameMixin, ShortDescriptionMixin):
    """ Custom Characteristics Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_cc"

    value_type = ormar.String(max_length=50, choices=common_data.value_type_list, nullable=True)
    characteristic_type = ormar.String(max_length=50, choices=common_data.characteristic_type_list, nullable=True)

    standard = ormar.ForeignKey(MeasuringStandards, related_name='char_st', nullable=True)


# todo material = ormar.ForeignKey(Material)
class CustomMatParam(AbstractBaseModel, ShortDescriptionMixin):
    """ Custom Material Parameters Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_cmp"

    standard = ormar.ForeignKey(Characteristic, related_name='char', nullable=True)

    value = ormar.String(max_length=5000)




