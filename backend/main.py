from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="StockLens API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def read_root():
    return {"message": "Welcome to StockLens API 🚀"}

@app.get("/news")
def get_news():
    return {"articles": ["Stock A rose 5%", "Stock B fell 3%"]}
