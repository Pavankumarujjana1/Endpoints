from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
user_id = None  


def test_create_user():
    global user_id
    user_data = {"username": "testuser", "password": "testpass"}
    response = client.post("/create", json=user_data)
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "User created"
    user_id = result["id"]


def test_read_user():
    global user_id
    assert user_id is not None
    response = client.get(f"/read/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["username"] == "testuser"
    assert user["password"] == "testpass"
    assert user["id"] == user_id


def test_update_user():
    global user_id
    assert user_id is not None
    update_data = {"username": "updateduser"}
    response = client.put(f"/update/{user_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Username updated"


def test_list_users():
    global user_id
    assert user_id is not None
    response = client.post("/list", json={"ids": [user_id]})
    assert response.status_code == 200
    users = response.json()["users"]
    assert len(users) == 1
    assert users[0]["username"] == "updateduser"
    assert users[0]["id"] == user_id


def test_delete_user():
    global user_id
    assert user_id is not None
    response = client.delete(f"/delete/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"


    response = client.get(f"/read/{user_id}")
    assert response.status_code == 404
