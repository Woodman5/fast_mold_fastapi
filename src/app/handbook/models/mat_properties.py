from tortoise import fields, models, Tortoise
from tortoise.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

from src.app.base.models import (
    TimestampMixin,
    NameMixin,
    AbstractBaseModel,
    MaxValueValidator,
    MinValueValidator
)


class HardnessScales(AbstractBaseModel):
    """ Hardness Scales Model """

    hs_type = fields.CharField(100, description='Hardness scale')
    hs_slug = fields.CharField(100, description='Slug')
    hs_desc = fields.TextField(description='Description', null=True, default='')
    hs_min = fields.IntField(description='Minimal value', default=0, validators=[MinValueValidator(0)])
    hs_max = fields.IntField(description='Maximum value', default=100, validators=[MaxValueValidator(2000)])
    hs_units = fields.CharField(15, description='Measurement unit')

    class Meta:
        table = "handbook_hardnessscales"
        table_description = "Hardness scales of materials"

    def __str__(self):
        return f'{self.hs_type}'


class CommonHardness(AbstractBaseModel):
    """ Human readable hardness Model """

    ch_type = fields.CharField(100, description='Hardness')
    ch_slug = fields.CharField(100, description='Slug')
    ch_desc = fields.TextField(description='Description', null=True, default='')

    class Meta:
        table = "handbook_commonhardness"
        table_description = "Human readable hardness"

    def __str__(self):
        return f'{self.ch_type}'


Tortoise.init_models(["src.app.handbook.models.mat_properties"], "models")
