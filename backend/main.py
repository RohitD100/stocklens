from fastapi import FastAPI

app = FastAPI(title="StockLens API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to StockLens API 🚀"}

@app.get("/news")
def get_news():
    return {"articles": ["Stock A rose 5%", "Stock B fell 3%"]}
