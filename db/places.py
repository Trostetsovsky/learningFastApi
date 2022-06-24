import datetime
import sqlalchemy

from .base import metadata

places = sqlalchemy.Table(
    'places', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('location_id', sqlalchemy.ForeignKey('locations.id'), nullable=False)
)