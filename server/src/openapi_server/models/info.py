# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Info(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Info - a model defined in OpenAPI

        id: The id of this Info [Optional].
        name: The name of this Info.
    """

    id: Optional[int] = Field(alias="id", default=None)
    name: str = Field(alias="name")

Info.update_forward_refs()
