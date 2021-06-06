from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, validator


class UnitsEnum(str, Enum):
    standard = "standard"
    metric = "metric"
    imperial = "imperial"


class Location(BaseModel):
    city: str
    state: Optional[str] = Field(None, min_length=2, max_length=2)
    country: str = Field("US", min_length=2, max_length=2)
    units: UnitsEnum = UnitsEnum.metric
