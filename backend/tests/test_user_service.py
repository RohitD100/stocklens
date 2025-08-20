import pytest
from app.services.user_service import insert_user_service

def test_insert_user_success(test_db):
    user = insert_user_service("test@example.com", "Test User", "tester")
    assert user["email"] == "test@example.com"
    assert user["name"] == "Test User"
    assert user["username"] == "tester"
    assert "id" in user

def test_insert_user_duplicate_email(test_db):
    # First insert
    insert_user_service("duplicate@example.com", "User One")
    
    # Second insert should raise RuntimeError
    with pytest.raises(RuntimeError) as excinfo:
        insert_user_service("duplicate@example.com", "User Two")
    assert "already exists" in str(excinfo.value)
