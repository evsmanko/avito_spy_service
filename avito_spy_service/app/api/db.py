import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, TIMESTAMP, func)
from databases import Database


DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

queries_stat = Table(
    'query_stat',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('queryId', Integer),
    Column('queryViews', Integer),
    Column('added', TIMESTAMP, nullable=False, server_default=func.now()),
)

database = Database(DATABASE_URI)
