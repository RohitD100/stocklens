import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "StockLens API"
    VERSION: str = "1.0"
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN", "")
    AUTH0_AUDIENCE: str = os.getenv("AUTH0_AUDIENCE", "")

settings = Settings()
