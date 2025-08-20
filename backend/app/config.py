import os
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import certifi

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

class Settings:
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN")
    API_AUDIENCE: str = os.getenv("API_AUDIENCE")
    ALGORITHMS = ["RS256"]
    FINN_HUB_API_KEY: str = os.getenv("FINN_HUB_API_KEY")
    MONGO_URL: str = os.getenv("MONGO_URL")
    MONGO_DB_NAME = "stocklens"

    def __init__(self):
        self.mongo_client = None
        self.db = None
        self.connect_mongo()

    def connect_mongo(self):
        if not self.MONGO_URL:
            logger.error("❌ MONGO_URL not set in environment variables!")
            return

        try:
            self.mongo_client = MongoClient(self.MONGO_URL, serverSelectionTimeoutMS=5000, tls=True,
    tlsCAFile=certifi.where())
            self.mongo_client.admin.command('ping')  
            self.db = self.mongo_client["stocklens"]
            logger.info(f"✅ Successfully connected to MongoDB database: stocklens")
        except ConnectionFailure as e:
            logger.error(f"❌ MongoDB connection failed: {e}")

settings = Settings()
