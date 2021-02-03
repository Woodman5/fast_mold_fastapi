from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.app.base.models import Model, AbstractBaseModel, SoftDelete
from sqlalchemy_utils import Timestamp, generic_repr, URLType, PhoneNumberType, UUIDType, EmailType


class HardnessScales(Model):
    """ Hardness Scales Model """

    __tablename__ = "Handbook_hardnessscales"

    hs_min = Column(Integer, default=0)
    hs_max = Column(Integer, default=100)
    hs_units = Column(String(15))


class CommonHardness(Model):
    """ Human readable hardness Model """

    __tablename__ = "Handbook_commonhardness"


