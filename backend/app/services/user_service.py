from datetime import datetime
from app.config import settings

def insert_user_service(email: str, name: str, username: str = None) -> dict:
    if settings.db is None:
        raise RuntimeError("Database not connected")

    existing_user = settings.db["users"].find_one({"email": email})
    if existing_user:
        raise RuntimeError("User with this email already exists")

    user_doc = {
        "email": email,
        "name": name,
        "username": username,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    result = settings.db["users"].insert_one(user_doc)
    created_user = settings.db["users"].find_one({"_id": result.inserted_id})

    created_user["id"] = str(created_user["_id"])
    created_user.pop("_id", None)

    return created_user
