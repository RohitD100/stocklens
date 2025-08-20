# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="StockLens API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  
API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE")
ALGORITHMS = ["RS256"]

security = HTTPBearer()

def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        resp = requests.get(
            f"{AUTH0_DOMAIN}/userinfo",
            headers={"Authorization": f"Bearer {token}"}
        )

        if resp.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token is invalid"
            )

        return resp.json()

    except requests.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token validation failed: {str(e)}"
        )


@app.get("/")
def read_root():
    return {"message": "Welcome to StockLens API 🚀"}

@app.get("/news")
def get_news(payload: dict = Depends(verify_jwt)):
    return {
        "message": "You are authorized 🎉",
        "user": payload,
        "articles": ["Stock A rose 5%", "Stock B fell 3%"]
    }
