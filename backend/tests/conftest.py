import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
import mongomock

# Fixture for test DB
@pytest.fixture(scope="session", autouse=True)
def test_db():
    settings.db = mongomock.MongoClient().db
    yield settings.db
    settings.db = None

# Fixture for TestClient
@pytest.fixture()
def client():
    return TestClient(app)
