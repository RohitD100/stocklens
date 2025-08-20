import httpx
from app.config import settings

async def search_stocks(query: str):
    url = f"https://finnhub.io/api/v1/search?q={query}&token={settings.FINN_HUB_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return [
            {"symbol": item["symbol"], "name": item["description"]}
            for item in data.get("result", [])
        ]

async def get_all_stocks(exchange: str = "US"):
    url = f"https://finnhub.io/api/v1/stock/symbol?exchange={exchange}&token={settings.FINN_HUB_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
        return [
            {"symbol": item["symbol"], "name": item["description"]}
            for item in data
        ]
