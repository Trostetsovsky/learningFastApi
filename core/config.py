from starlette.config import Config

config = Config('.env')
DATABASE_URL = config('DATABASE_URL', cast=str, default='')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = config('SECRET_KEY', cast=str, default='d8497de10b71a74fea4f5ad7b5cbb27655e686c54d2e81e479e5a2577196fa85')

