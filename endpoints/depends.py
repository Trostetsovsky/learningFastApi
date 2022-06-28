from fastapi import HTTPException, Depends, status
from starlette import status

from core.security import JWTBearer, decode_access_token
from db.base import database
from models.users_validator import User
from repositories.locations_repository import LocationRepository
from repositories.places_repository import PlaceRepository
from repositories.user_favorite_places_repository import UserFavoritePlaceRepository
from repositories.users_repository import UserRepository

not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found")


def get_place_repository() -> PlaceRepository:
    return PlaceRepository(database)


def get_location_repository() -> LocationRepository:
    return LocationRepository(database)


def get_user_favorite_place_repository() -> UserFavoritePlaceRepository:
    return UserFavoritePlaceRepository(database)


def get_user_repository() -> UserRepository:
    return UserRepository(database)


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer())
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials are not valid')
    email: str = payload.get('sub')
    if email is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials are not valid')
    user = await users.get_by_email(email=email)
    if user is None:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials are not valid')
    return user
