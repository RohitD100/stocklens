from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import news, stocks

app = FastAPI(title="StockLens API", version="1.0")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news.router)
app.include_router(stocks.router)
