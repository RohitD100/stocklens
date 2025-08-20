from pydantic import BaseModel
from typing import List

class NewsResponse(BaseModel):
    articles: List[str]
