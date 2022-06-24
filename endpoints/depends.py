from fastapi import HTTPException
from starlette import status

from db.base import database
from repositories.locations_repository import LocationRepository
from repositories.places_repository import PlaceRepository
from repositories.users_repository import UserRepository

not_found_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found")


def get_place_repository() -> PlaceRepository:
    return PlaceRepository(database)


def get_location_repository() -> LocationRepository:
    return LocationRepository(database)


def get_user_repository() -> UserRepository:
    return UserRepository(database)
