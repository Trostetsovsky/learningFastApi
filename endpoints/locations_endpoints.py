from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from endpoints.depends import get_location_repository, not_found_exception
from models.locations_validator import Location, LocationIn
from repositories.locations_repository import LocationRepository

router = APIRouter()


@router.get('/', response_model=list[Location])
async def read_locations(
        locations: LocationRepository = Depends(get_location_repository),
        limit: int = 100,
        skip: int = 0):
    return await locations.get_all(limit=limit, skip=skip)


@router.post('/', response_model=Location)
async def create_locations(
        l: LocationIn,
        locations: LocationRepository = Depends(get_location_repository)):
    return await locations.create(l=l)


@router.patch('/', response_model=Location)
async def update_locations(
        id: int,
        l: LocationIn,
        locations: LocationRepository = Depends(get_location_repository)):
    location = await locations.get_by_id(id=id)
    if location is None:
        raise not_found_exception
    return await locations.update(id=id, l=l)


@router.delete('/')
async def delete_locations(
        id: int,
        locations: LocationRepository = Depends(get_location_repository)):
    location = await locations.get_by_id(id=id)
    if location is None:
        raise not_found_exception
    await locations.delete(id=id)
    return {'status': True}