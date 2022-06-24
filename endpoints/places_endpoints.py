from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from endpoints.depends import get_place_repository, not_found_exception
from models.places_validator import Place, PlaceIn
from repositories.places_repository import PlaceRepository

router = APIRouter()


@router.post('/', response_model=Place)
async def create_places(
        p: PlaceIn,
        places: PlaceRepository = Depends(get_place_repository)):
    return await places.create(p=p)


@router.get('/', response_model=list[Place])
async def read_places(
        places: PlaceRepository = Depends(get_place_repository),
        limit: int = 100,
        skip: int = 0):
    return await places.get_all(limit=limit, skip=skip)


@router.patch('/', response_model=Place)
async def update_places(
        id: int,
        p: PlaceIn,
        places: PlaceRepository = Depends(get_place_repository)):
    place = await places.get_by_id(id=id)
    if place is None:
        raise not_found_exception
    return await places.update(id=id, p=p)


@router.delete('/')
async def delete_places(
        id: int,
        places: PlaceRepository = Depends(get_place_repository)):
    place = await places.get_by_id(id=id)
    if place is None:
        raise not_found_exception
    await places.delete(id=id)
    return {'status': True}
