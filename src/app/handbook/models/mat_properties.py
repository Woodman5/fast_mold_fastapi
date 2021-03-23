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


class HardnessScales(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Hardness Scales Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_hd"

    hs_min = ormar.Integer(default=0)
    hs_max = ormar.Integer(default=100)
    hs_units = ormar.String(max_length=30, nullable=True)


class CommonHardness(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Human readable hardness Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_comhd"


class Status(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Statuses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_status"


class Tech(AbstractBaseModel, NameMixin):
    """ Technologies list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_tech"


class ToolClass(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ ToolClasses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_toolclasses"


class MaterialType(AbstractBaseModel, NameMixin):
    """ MaterialTypes list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_mattypes"


class ImitationMaterial(AbstractBaseModel, NameMixin):
    """ ImitationMaterials list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_imitmat"


class ChemicalResistance(AbstractBaseModel, NameMixin):
    """ ChemicalResistances list Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_chemres"


class MeasuringStandards(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ MeasuringStandards Model """

    standard_type = ormar.String(max_length=30, choices=common_data.standard_type_list)
    application_type = ormar.String(max_length=30, choices=common_data.application_type_list)

    class Meta(ormar.ModelMeta):
        tablename = "hb_measuring"


class Colors(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Colors Model """

    color_type = ormar.String(max_length=30, choices=common_data.color_type_list)
    hex_code = ormar.String(max_length=30)
    rgb_code = ormar.String(max_length=30)

    class Meta(ormar.ModelMeta):
        tablename = "hb_colors"


class TypeTech(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin):
    """ TypeTech Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_typetech"

    technology = ormar.ForeignKey(Tech)


class ToolType(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin):
    """ ToolType Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_tooltype"

    tool_class = ormar.ForeignKey(ToolClass)


class ToolMan(AbstractBaseModel, NameMixin, ShortDescriptionMixin, DescriptionMixin, UrlMixin):
    """ ToolMan Model """

    class Meta(ormar.ModelMeta):
        tablename = "hb_toolman"

    country = ormar.String(max_length=200)
    technology = ormar.ManyToMany(Tech, related_name='tm')







