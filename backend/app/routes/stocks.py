# app/routes/news.py
from fastapi import APIRouter, Depends
from app.auth.jwt_handler import verify_jwt
from fastapi import APIRouter, Query
import httpx
import os

router = APIRouter()
FINN_HUB_API_KEY = os.getenv("FINN_HUB_API_KEY")

@router.get("/stocks")
async def search_stocks(q: str = Query(..., min_length=1)):
    url = f"https://finnhub.io/api/v1/search?q={q}&token={FINN_HUB_API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = [
                {"symbol": item["symbol"], "name": item["description"]}
                for item in data.get("result", [])
            ]
            return results
        except httpx.HTTPError as e:
            return {"error": "Failed to fetch stock data", "details": str(e)}


          
@router.get("/stocks/all")
async def get_all_stocks(exchange: str = "US"):
    url = f"https://finnhub.io/api/v1/stock/symbol?exchange={exchange}&token={FINN_HUB_API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            results = [
                {"symbol": item["symbol"], "name": item["description"]}
                for item in data
            ]
            return results
        except httpx.HTTPError as e:
            return {"error": "Failed to fetch stock data", "details": str(e)}