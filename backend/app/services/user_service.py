from datetime import datetime, timezone
from app.config import settings

def insert_user_service(email: str, name: str, username: str = None) -> dict:
    if settings.db is None:
        raise RuntimeError("Database not connected")

    existing_user = settings.db["users"].find_one({"email": email})
    if existing_user:
        raise RuntimeError("User with this email already exists")
    
    now = datetime.now(timezone.utc)
    user_doc = {
        "email": email,
        "name": name,
        "username": username,
        "created_at": now,
        "updated_at": now
    }

    result = settings.db["users"].insert_one(user_doc)
    created_user = settings.db["users"].find_one({"_id": result.inserted_id})

    created_user["id"] = str(created_user["_id"])
    created_user.pop("_id", None)

    return created_user
