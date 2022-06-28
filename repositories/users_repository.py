import datetime
from typing import Optional

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

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_email(self, email: str):
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def update(self, id: int, u: UserIn):
        user = User(
            id=id,
            email=u.email,
            name=u.name,
            hashed_password=hash_password(u.password),
            is_active=True,
            created_at=0,
            updated_at=datetime.datetime.utcnow(),
        )
        values = {**user.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        values.update({'hashed_password': values['hashed_password'].get_secret_value()})
        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query=query)
        return user

    async def delete(self):
        pass