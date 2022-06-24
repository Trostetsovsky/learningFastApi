import datetime

from core.security import hash_password
from db.users import users
from models.users_validator import UserIn, User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, u: UserIn) -> User:
        current_time = datetime.datetime.utcnow()
        user = User(
            id=0,
            email=u.email,
            name=u.name,
            hashed_password=hash_password(u.password),
            is_active=True,
            created_at=current_time,
            updated_at=current_time
        )
        values = {**user.dict()}
        values.pop('id', None)
        values.update({'hashed_password': values['hashed_password'].get_secret_value()})
        query = users.insert().values(**values)
        user.id = await self.database.execute(query=query)
        return user

    async def get_all(self, limit: int = 100, skip: int = 0):
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass