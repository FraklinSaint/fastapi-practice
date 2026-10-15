
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


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
