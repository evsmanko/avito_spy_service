from .db import queries, database
from .models import SearchQueryIn


async def add_search_query(payload: SearchQueryIn):
    query = queries.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_queries():
    query = queries.select()
    return await database.fetch_all(query)


async def get_query(query_id: int):
    query = queries.select(queries.c.id == query_id)
    return await database.fetch_one(query)


async def delete_query(query_id: int):
    query = queries.delete().where(queries.c.id == query_id)
    return await database.execute(query=query)