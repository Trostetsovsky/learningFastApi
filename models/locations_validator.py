from pydantic import BaseModel


class Location(BaseModel):
    id: int
    city: str


class LocationIn(BaseModel):
    city: str
