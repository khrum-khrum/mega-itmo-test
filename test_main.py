from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == '"pong"'


def test_echo():
    message = "hello"
    response = client.get(f"/echo/{message}")
    assert response.status_code == 200
    assert response.json() == message


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_fibonacci():
    response = client.get("/fibonacci/0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/fibonacci/1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    response = client.get("/fibonacci/2")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    response = client.get("/fibonacci/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

    response = client.get("/fibonacci/-1")
    assert response.status_code == 200
    assert response.json() == {"error": "Input must be a non-negative integer"}
