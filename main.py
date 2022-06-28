import uvicorn
from fastapi import FastAPI

from endpoints import places_endpoints, locations_endpoints, users_endpoints, auth
from db.base import database

app = FastAPI()
app.include_router(places_endpoints.router, prefix='/places', tags=['places', ])
app.include_router(locations_endpoints.router, prefix='/locations', tags=['locations', ])
app.include_router(users_endpoints.router, prefix='/users', tags=['users', ])
app.include_router(auth.router, prefix='/auth', tags=['auth', ])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
