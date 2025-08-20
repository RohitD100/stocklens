from fastapi import APIRouter, Query
from app.services import finnhub
import httpx

router = APIRouter()

@router.get("/stocks")
async def search_stocks(q: str = Query(..., min_length=1)):
    try:
        return await finnhub.search_stocks(q)
    except httpx.HTTPError as e:
        return {"error": "Failed to fetch stock data", "details": str(e)}

@router.get("/stocks/all")
async def get_all_stocks(exchange: str = "US"):
    try:
        return await finnhub.get_all_stocks(exchange)
    except httpx.HTTPError as e:
        return {"error": "Failed to fetch stock data", "details": str(e)}
