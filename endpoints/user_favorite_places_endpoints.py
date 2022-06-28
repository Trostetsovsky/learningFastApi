from fastapi import APIRouter, Depends, HTTPException, status

from endpoints.depends import get_user_favorite_place_repository, get_current_user
from models.users_favorite_places_validator import UserFavoritePlace, UserFavoritePlaceIn
from models.users_validator import User
from repositories.user_favorite_places_repository import UserFavoritePlaceRepository

router = APIRouter()


@router.get('/', response_model=list[UserFavoritePlace])
async def read_favorite_places(
        favorite_places: UserFavoritePlaceRepository = Depends(get_user_favorite_place_repository),
        current_user: User = Depends(get_current_user),
        limit: int = 100,
        skip: int = 0):
    return await favorite_places.get_all(user_id=current_user.id, limit=limit, skip=skip)


@router.post('/', response_model=UserFavoritePlace)
async def add_favorite_place(
        u: UserFavoritePlaceIn,
        favorite_places: UserFavoritePlaceRepository = Depends(get_user_favorite_place_repository),
        current_user: User = Depends(get_current_user)):
    return await favorite_places.create(user_id=current_user.id, u_input=u)


@router.delete('/')
async def delete_favorite_places(
        u: UserFavoritePlaceIn,
        favorite_places: UserFavoritePlaceRepository = Depends(get_user_favorite_place_repository),
        current_user: User = Depends(get_current_user)):
    favorite_place = await favorite_places.get_by_id(current_user.id, u.place_id)
    if favorite_place is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Place not found!')
    await favorite_places.delete(user_id=current_user.id, u_input=u)
    return {'status': True}