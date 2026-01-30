from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "\"pong\""


def test_echo():
    message = "hello"
    response = client.get(f"/echo/{message}")
    assert response.status_code == 200
    assert response.json() == message


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}