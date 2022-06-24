import datetime
from pydantic import BaseModel


class UserFavoritePlaces(BaseModel):
    id: int
    user_id: int
    place_id: int
    added_at: datetime.datetime
