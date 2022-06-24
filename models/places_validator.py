import datetime
from pydantic import BaseModel


class Place(BaseModel):
    id: int
    title: str
    description: str
    is_active: bool
    created_at: datetime.datetime
    location_id: int


class PlaceIn(BaseModel):
    title: str
    description: str
    is_active: bool
    location_id: int
