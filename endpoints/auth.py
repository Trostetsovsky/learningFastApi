from fastapi import APIRouter, Depends, HTTPException, status

from core.security import create_access_token, verify_password
from endpoints.depends import get_user_repository
from models.token import Login, Token
from repositories.users_repository import UserRepository

router = APIRouter()


@router.post('/', response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password.get_secret_value()):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Incorrect email or password!')
    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type='Bearer'
    )
