from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from endpoints.depends import get_user_repository, get_current_user
from models.users_validator import UserIn, User
from repositories.users_repository import UserRepository

router = APIRouter()


@router.post('/', response_model=User)
async def create_users(
        u: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=u)


@router.get('/', response_model=list[User])
async def read_users(
        limit: int = 100,
        skip: int = 0,
        users: UserRepository = Depends(get_user_repository)):
    return await users.get_all(limit=limit, skip=skip)


@router.patch('/', response_model=User)
async def update_user(
        id: int,
        u: UserIn,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return await users.update(id=id, u=u)