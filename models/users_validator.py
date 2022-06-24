import datetime
from pydantic import BaseModel, SecretStr, EmailStr, constr, validator


class User(BaseModel):
    id: int
    email: EmailStr
    name: str
    hashed_password: SecretStr
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    email: EmailStr
    name: str
    password: constr(min_length=8)
    password2: str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Password don\'t match!')
        return v