from tortoise import fields, models
from tortoise.validators import Validator
from tortoise.exceptions import ValidationError


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


class NameMixin:
    name = fields.CharField(200, unique=True)


class AbstractBaseModel(models.Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class MaxValueValidator(Validator):
    """
    A validator to validate whether the given value is less or equal than the required value.
    """
    def __init__(self, max_value: int):
        self.max_value = max_value

    def __call__(self, value: int):
        if value > self.max_value:
            raise ValidationError(f"Value '{value}' is greater than max value")


class MinValueValidator(Validator):
    """
    A validator to validate whether the given value is greater or equal than the required value.
    """
    def __init__(self, min_value: int):
        self.min_value = min_value

    def __call__(self, value: int):
        if value < self.min_value:
            raise ValidationError(f"Value '{value}' is less than max value")


