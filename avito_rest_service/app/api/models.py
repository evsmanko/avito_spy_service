from datetime import datetime
from pydantic import BaseModel, Field


class SearchQueryIn(BaseModel):
    search_text: str
    region: str


class SearchQueryOut(SearchQueryIn):
    id: int
    added: datetime = Field(default_factory=datetime.utcnow)