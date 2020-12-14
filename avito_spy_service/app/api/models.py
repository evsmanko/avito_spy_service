from datetime import datetime
from pydantic import BaseModel, Field


class QueryStatIn(BaseModel):
    queryId: int
    queryViews: int


class QueryStatOut(QueryStatIn):
    id: int
    added: datetime = Field(default_factory=datetime.utcnow)