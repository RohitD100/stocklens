import pytest
from app.services.user_service import insert_user_service, get_user_by_email, get_all_users_from_db
from datetime import datetime

def test_insert_user_success(test_db):
    user = insert_user_service("test@example.com", "Test User", "tester")
    assert user["email"] == "test@example.com"
    assert user["name"] == "Test User"
    assert user["username"] == "tester"
    assert "id" in user
    assert isinstance(user["created_at"], datetime)
    assert isinstance(user["updated_at"], datetime)

def test_insert_user_duplicate_email(test_db):
    insert_user_service("duplicate@example.com", "User One")
    with pytest.raises(RuntimeError) as excinfo:
        insert_user_service("duplicate@example.com", "User Two")
    assert "already exists" in str(excinfo.value)

def test_get_user_by_email_success(test_db):
    insert_user_service("getuser@example.com", "Get User", "getuser")
    user = get_user_by_email("getuser@example.com")
    assert user is not None
    assert user["email"] == "getuser@example.com"
    assert user["name"] == "Get User"

def test_get_user_by_email_not_found(test_db):
    user = get_user_by_email("nonexistent@example.com")
    assert user is None

def test_get_all_users_from_db(test_db):
    # Clear users collection first (optional, depends on fixture)
    test_db["users"].delete_many({})
    
    insert_user_service("user1@example.com", "User One")
    insert_user_service("user2@example.com", "User Two")
    
    users = get_all_users_from_db()
    assert len(users) == 2
    emails = [u["email"] for u in users]
    assert "user1@example.com" in emails
    assert "user2@example.com" in emails
