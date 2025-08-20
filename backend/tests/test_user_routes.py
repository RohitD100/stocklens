def test_create_user_success(client):
    response = client.post("/user", json={
        "email": "apiuser@example.com",
        "name": "API User",
        "username": "apiuser"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "apiuser@example.com"
    assert data["name"] == "API User"

def test_create_user_duplicate_email(client):
    client.post("/user", json={
        "email": "dupapi@example.com",
        "name": "First User",
        "username": "seconduser"
    })
    response = client.post("/user", json={
        "email": "dupapi@example.com",
        "name": "Second User",
        "username": "seconduser"
    })
    assert response.status_code == 500  
    assert "already exists" in response.json()["detail"]
