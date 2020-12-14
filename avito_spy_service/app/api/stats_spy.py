from typing import List

from fastapi import APIRouter, HTTPException
from . import db_manager
from .models import QueryStatIn, QueryStatOut

queries_stat = APIRouter()


@queries_stat.get('/', response_model=List[QueryStatOut])
async def index():
    return await db_manager.get_all_queries_stat()


@queries_stat.post('/', response_model=QueryStatIn, status_code=201)
async def create_query_stat(payload: QueryStatIn):
    query_stat_id = await db_manager.add_query_stat(payload)

    response = {
        'id': query_stat_id,
        **payload.dict()
    }
    return response


@queries_stat.get('/{id}/', response_model=List[QueryStatOut])
async def get_query_stats_by_id(id: int):
    queries = await db_manager.get_query_stats_by_id(id)
    if not queries:
        raise HTTPException(status_code=404, detail="Cast not found")
    return queries