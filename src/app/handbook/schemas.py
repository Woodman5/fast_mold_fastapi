from typing import Optional
from datetime import datetime

from fastapi import Body, Form
from pydantic import BaseModel, EmailStr, UUID4
from pydantic.fields import ModelField, Field
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel
from .models.mat_properties import (
    HardnessScales,
    CommonHardness,
)


HardnessScales_Create_Pydantic = pydantic_model_creator(HardnessScales,
                                                        name='Create Hardness Scales',
                                                        exclude_readonly=True,
                                                        )


class HardnessScalesUpdatePydantic(HardnessScales_Create_Pydantic):
    hs_type: Optional[str]
    hs_slug: Optional[str]
    hs_units: Optional[str]


HardnessScales_Get_Pydantic = pydantic_model_creator(HardnessScales, name='Get Hardness Scales')

CommonHardness_Create_Pydantic = pydantic_model_creator(CommonHardness,
                                                        name='Create Common Hardness',
                                                        exclude_readonly=True,
                                                        )


class CommonHardnessUpdatePydanticPydantic(CommonHardness_Create_Pydantic):
    ch_type: Optional[str]
    ch_slug: Optional[str]


CommonHardness_Get_Pydantic = pydantic_model_creator(CommonHardness, name='Get Common Hardness')
