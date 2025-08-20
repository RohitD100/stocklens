# app/routes/news.py
from fastapi import APIRouter, Depends
from app.auth.jwt_handler import verify_jwt

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to StockLens API 🚀"}

@router.get("/news")
async def get_news(payload: dict = Depends(verify_jwt)):
    return {
        "message": "You are authorized 🎉",
        "user": payload,
        "articles": ["Stock A rose 10%", "Stock B fell 3%"]
    }
