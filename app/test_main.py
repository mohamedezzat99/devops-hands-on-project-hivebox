from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_get_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}


def test_get_temperature():
    response = client.get("/temperature")
    assert response.status_code == 200
    assert "temperature" in response.json()
    assert isinstance(response.json()["temperature"], (int, float))
