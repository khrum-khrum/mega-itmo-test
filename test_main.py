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


def test_set_and_get_value():
    key = "testkey"
    value = "testvalue"

    # Test POST /value/{key}
    response = client.post(f"/value/{key}", json={"value": value})
    assert response.status_code == 200
    assert response.json() == {"message": f"Value for key '{key}' set successfully"}

    # Test GET /value/{key}
    response = client.get(f"/value/{key}")
    assert response.status_code == 200
    assert response.json() == {"key": key, "value": value}


def test_get_nonexistent_value():
    key = "nonexistentkey"
    response = client.get(f"/value/{key}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Key '{key}' not found"}
