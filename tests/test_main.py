
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock

client = TestClient(app)

def mock_db(monkeypatch, fetchone=None, fetchall=None):
    connection = MagicMock()
    connection.__enter__.return_value = connection

    cursor = MagicMock()
    connection.cursor.return_value.__enter__.return_value = cursor

    cursor.fetchone.return_value = fetchone
    cursor.fetchall.return_value = fetchall or []

    monkeypatch.setattr(
        "main.get_connection",
        lambda: connection,
    )

    return cursor


def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello Vlad"}


def test_products_default_limit():
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == {"limit": 10}


def test_products_custom_limit():
    response = client.get("/products?limit=5")

    assert response.status_code == 200
    assert response.json() == {"limit": 5}


def test_create_user_rejects_invalid_age():
    response = client.post(
        "/users",
        json={"name": "Al", "age": 17},
    )

    assert response.status_code == 422

def test_get_user(monkeypatch):
    mock_db(
        monkeypatch,
        fetchone=(1, "Vlad", 18),
    )

    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Vlad",
        "age": 18,
    }

    
def test_get_user_not_found(monkeypatch):
    mock_db(
        monkeypatch,
        fetchone=None,
    )

    response = client.get("/users/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_create_user(monkeypatch):
    mock_db(
        monkeypatch,
        fetchone=(2, "Anna", 20),
    )

    response = client.post(
        "/users",
        json={"name": "Anna", "age": 20},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Anna",
        "age": 20,
    }


def test_update_user(monkeypatch):
    mock_db(
        monkeypatch,
        fetchone=(2, "Anna", 25),
    )

    response = client.patch(
        "/users/2",
        json={"age": 25},
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Anna",
        "age": 25,
    }


def test_delete_user(monkeypatch):
    mock_db(
        monkeypatch,
        fetchone=(2, "Anna", 25),
    )

    response = client.delete("/users/2")

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "name": "Anna",
        "age": 25,
    }
