import datetime
from typing import Optional

from db.places import places
from models.places_validator import PlaceIn, Place
from repositories.base_repository import BaseRepository


class PlaceRepository(BaseRepository):
    async def create(self, p: PlaceIn) -> Place:
        place = Place(
            id=0,
            title=p.title,
            description=p.description,
            is_active=p.is_active,
            created_at=datetime.datetime.utcnow(),
            location_id=p.location_id,
        )
        values = {**place.dict()}
        values.pop('id', None)
        query = places.insert().values(**values)
        place.id = await self.database.execute(query)
        return place

    async def update(self, id: int, p: PlaceIn) -> Place:
        place = Place(
            id=id,
            title=p.title,
            description=p.description,
            is_active=p.is_active,
            created_at=datetime.datetime.utcnow(),
            location_id=p.location_id,
        )
        values = {**place.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        query = places.update().where(places.c.id == id).values(**values)
        await self.database.execute(query=query)
        return place

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Place]:
        query = places.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Place]:
        query = places.select().where(places.c.id == id)
        place = await self.database.fetch_one(query=query)
        if place is None:
            return None
        return Place.parse_obj(place)

    async def delete(self, id: int):
        query = places.delete().where(places.c.id == id)
        await self.database.execute(query=query)
