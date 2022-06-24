from fastapi import APIRouter, Depends

from endpoints.depends import get_user_repository
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