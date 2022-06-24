import datetime
import sqlalchemy

from .base import metadata

users_favorite_places = sqlalchemy.Table(
    'users_favorite_places', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column('place_id', sqlalchemy.ForeignKey('places.id'), nullable=False),
    sqlalchemy.Column('added_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)
