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

from . import common_data


class HardnessScales(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Hardness Scales Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_hardnessscales"

    hs_min = ormar.Integer(default=0)
    hs_max = ormar.Integer(default=100)
    hs_units = ormar.String(max_length=30, nullable=True)


class CommonHardness(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Human readable hardness Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_commonhardness"


class Status(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Statuses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_statuses"


class Technology(AbstractBaseModel, NameMixin):
    """ Technologies list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_technologies"


class ToolClass(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ ToolClasses list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_toolclasses"


class MaterialType(AbstractBaseModel, NameMixin):
    """ MaterialTypes list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_materialtypes"


class ImitationMaterial(AbstractBaseModel, NameMixin):
    """ ImitationMaterials list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_imitationmaterial"


class ChemicalResistance(AbstractBaseModel, NameMixin):
    """ ChemicalResistances list Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_chemicalresistance"


class MeasuringStandards(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ MeasuringStandards Model """

    standard_type = ormar.String(max_length=30, choices=common_data.standard_type_list)
    application_type = ormar.String(max_length=30, choices=common_data.application_type_list)

    class Meta(ormar.ModelMeta):
        tablename = "handbook_measuringstandards"


class Colors(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ Colors Model """

    color_type = ormar.String(max_length=30, choices=common_data.color_type_list)
    hex_code = ormar.String(max_length=30)
    rgb_code = ormar.String(max_length=30)

    class Meta(ormar.ModelMeta):
        tablename = "handbook_colors"


class TypeTechnology(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ TypeTechnology Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_typetechnology"

    short_desc = ormar.String(max_length=400)
    technology = ormar.ForeignKey(Technology)


class ToolType(AbstractBaseModel, NameMixin, DescriptionMixin):
    """ ToolType Model """

    class Meta(ormar.ModelMeta):
        tablename = "handbook_tooltype"

    short_desc = ormar.String(max_length=400)
    tool_class = ormar.ForeignKey(ToolClass)









