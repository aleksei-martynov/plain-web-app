from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert "Привет!" in response.text


def test_goodbye():
    response = client.get("/goodbye")
    assert response.status_code == 200
    assert "Пока!" in response.text
