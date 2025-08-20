from fastapi import APIRouter
from models.news import NewsResponse
from services.news_service import fetch_news

router = APIRouter()

@router.get("/", response_model=NewsResponse)
def get_news():
    return {"articles": fetch_news()}
