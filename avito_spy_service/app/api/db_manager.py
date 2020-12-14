from .db import queries_stat, database
from .models import QueryStatIn


async def add_query_stat(payload: QueryStatIn):
    query = queries_stat.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_queries_stat():
    query = queries_stat.select()
    return await database.fetch_all(query)


async def get_query_stats_by_id(query_id: int):
    query = queries_stat.select(queries_stat.c.queryId == query_id)
    return await database.fetch_all(query)
