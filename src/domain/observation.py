from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class Location(BaseModel):
    long: float
    lat: float


class Measurement(BaseModel):
    id: str
    type: str
    value: float


class Observation(BaseModel):
    time: datetime
    location: Location
    measurements: List[Measurement]
