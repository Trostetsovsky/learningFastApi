from typing import Optional

from db.locations import locations
from models.locations_validator import LocationIn, Location
from repositories.base_repository import BaseRepository


class LocationRepository(BaseRepository):
    async def create(self, l: LocationIn) -> Location:
        location = Location(
            id=0,
            city=l.city
        )
        values = {**location.dict()}
        values.pop('id', None)
        query = locations.insert().values(**values)
        location.id = await self.database.execute(query=query)
        return location

    async def update(self, id: int, l: LocationIn) -> Location:
        location = Location(
            id=id,
            city=l.city
        )
        values = {**location.dict()}
        values.pop('id', None)
        query = locations.update().where(locations.c.id == id).values(**values)
        await self.database.execute(query=query)
        return location

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Location]:
        query = locations.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def delete(self, id: int):
        query = locations.delete().where(locations.c.id == id)
        return await self.database.execute(query=query)

    async def get_by_id(self, id: int) -> Optional[Location]:
        query = locations.select().where(locations.c.id == id)
        location = await self.database.fetch_one(query=query)
        if location is None:
            return None
        return Location.parse_obj(location)
