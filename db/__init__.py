from .places import places
from .users import users
from .locations import locations
from .users_favorite_places import users_favorite_places
from .base import metadata, engine

metadata.create_all(bind=engine)