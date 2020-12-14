from typing import List

from fastapi import HTTPException, APIRouter
from starlette.background import BackgroundTasks

from . import db_manager
from .models import SearchQueryIn, SearchQueryOut

queries = APIRouter()


@queries.get('/', response_model=List[SearchQueryOut])
async def index():
    return await db_manager.get_all_queries()


@queries.post('/', status_code=201)
async def add_query(payload: SearchQueryIn, background_tasks: BackgroundTasks):
    query_id = await db_manager.add_search_query(payload)
    response = {
        'id': query_id,
    }
    return response



@queries.delete('/{id}')
async def delete_movie(query_id: int):
    query = await db_manager.get_query(query_id)
    if not query:
        raise HTTPException(status_code=404, detail="Search query not found")
    return await db_manager.delete_query(query_id)