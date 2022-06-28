import datetime
from pydantic import BaseModel


class UserFavoritePlace(BaseModel):
    id: int
    user_id: int
    place_id: int
    added_at: datetime.datetime


class UserFavoritePlaceIn(BaseModel):
    place_id: int
