import datetime

from fastapi import HTTPException, status
from sqlalchemy import and_

from db.users_favorite_places import users_favorite_places
from models.users_favorite_places_validator import UserFavoritePlaceIn, UserFavoritePlace
from repositories.base_repository import BaseRepository


class UserFavoritePlaceRepository(BaseRepository):

    async def create(self, user_id: int, u_input: UserFavoritePlaceIn) -> UserFavoritePlace:
        u = UserFavoritePlace(
            id=0,
            user_id=user_id,
            place_id=u_input.place_id,
            added_at=datetime.datetime.utcnow()
        )
        values = {**u.dict()}
        values.pop('id', None)
        query = users_favorite_places.insert().values(**values)
        try:
            u.id = await self.database.execute(query=query)
            return u
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Place not found!')

    async def get_all(self, user_id: int, limit: int = 100, skip: int = 0):
        query = users_favorite_places.select().where(users_favorite_places.c.user_id == user_id).limit(limit).offset(
            skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, user_id: int, place_id):
        query = users_favorite_places.select().filter(
            and_((users_favorite_places.c.place_id == place_id), (users_favorite_places.c.user_id == user_id)))
        place = await self.database.fetch_all(query=query)
        if place is None:
            return None
        return UserFavoritePlace.parse_obj(place)

    async def delete(self, user_id: int, u_input: UserFavoritePlaceIn):
        query = users_favorite_places.delete().filter(
            and_((users_favorite_places.c.place_id == u_input.place_id), (users_favorite_places.c.user_id == user_id)))
        return await self.database.execute(query=query)

    async def update(self):  # The method isn't needed
        pass
