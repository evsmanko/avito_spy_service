import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, TIMESTAMP, func)
from databases import Database


DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

queries = Table(
    'queries',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('search_text', String(300)),
    Column('region', String(150)),
    Column('added', TIMESTAMP, nullable=False, server_default=func.now()),
)

queries_stat = Table(
    'queries_stat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('search_text', String(300)),
    Column('region', String(150)),
    Column('added', TIMESTAMP, nullable=False, server_default=func.now()),
)

database = Database(DATABASE_URI)
