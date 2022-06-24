import sqlalchemy

from .base import metadata

locations = sqlalchemy.Table(
    'locations', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('city', sqlalchemy.String, unique=True),
)