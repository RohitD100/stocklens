import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN")
    API_AUDIENCE: str = os.getenv("AUTH0_API_AUDIENCE")
    FINN_HUB_API_KEY:str = os.getenv("FINN_HUB_API_KEY")
    ALGORITHMS = ["RS256"]

settings = Settings()
