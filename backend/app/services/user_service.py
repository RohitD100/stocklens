from datetime import datetime, timezone
from app.config import settings
import uuid

def insert_user_service(email: str, name: str, username: str = None) -> dict:
    if settings.db is None:
        raise RuntimeError("Database not connected")

    existing_user = settings.db["users"].find_one({"email": email})
    if existing_user:
        raise RuntimeError("User with this email already exists")
    
    now = datetime.now(timezone.utc)
    user_id = str(uuid.uuid4()) 
    user_doc = {
        "_id": user_id,
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


def get_user_by_email(email: str):
    user = settings.db["users"].find_one({"email": email})
    if user:
        user_out = {
            "id": str(user.get("_id")), 
            "email": user.get("email"),
            "name": user.get("name"),
            "username": user.get("username"),
            "auth_provider_sub": user.get("auth_provider_sub"),
            "created_at": user.get("created_at"),  
            "updated_at": user.get("updated_at")
        }
        return user_out
    return None


def get_all_users_from_db():
    users_cursor = settings.db["users"].find()
    users = []
    for user in users_cursor:
        users.append({
            "id": str(user.get("_id")),
            "email": user.get("email"),
            "name": user.get("name"),
            "username": user.get("username"),
            "auth_provider_sub": user.get("auth_provider_sub"),
            "created_at": user.get("created_at"),
            "updated_at": user.get("updated_at")
        })
    return users