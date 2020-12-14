from fastapi import FastAPI

from .api.db import metadata, engine, database
from .api.stats_spy import queries_stat

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(queries_stat, prefix='/api/v1/stat', tags=['stat'])