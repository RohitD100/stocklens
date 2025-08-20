# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
import os
import requests

router = APIRouter()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  # e.g. https://dev-xxxx.us.auth0.com/
API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE")  # API Identifier from Auth0
ALGORITHMS = ["RS256"]

security = HTTPBearer()

# Fetch JWKS from Auth0
jwks_url = f"{AUTH0_DOMAIN}.well-known/jwks.json"
jwks = requests.get(jwks_url).json()
jwks_keys = {key["kid"]: key for key in jwks["keys"]}

def verify_jwt(token: str = Depends(security)):
    try:
        headers = jwt.get_unverified_header(token.credentials)
        kid = headers["kid"]
        key = jwks_keys.get(kid)
        if key is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        payload = jwt.decode(
            token.credentials,
            key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=AUTH0_DOMAIN
        )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/protected")
def protected_route(payload: dict = Depends(verify_jwt)):
    return {"message": "You are authorized 🎉", "user": payload}
