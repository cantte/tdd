from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_endpoint():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == "Hello FastAPI"


def test_is_prime_endpoint():
    response = client.get("/is_prime/1")
    assert response.status_code == 200

    result = response.json()
    assert result is False

    response = client.get("/is_prime/-14")
    assert response.status_code == 200

    result = response.json()
    assert result is False

    response = client.get("/is_prime/6")
    assert response.status_code == 200

    result = response.json()
    assert result is False

    response = client.get("/is_prime/5")
    assert response.status_code == 200

    result = response.json()
    assert result is True

    response = client.get("/is_prime/49")
    assert response.status_code == 200

    result = response.json()
    assert result is False

    response = client.get("/is_prime/567")
    assert response.status_code == 200

    result = response.json()
    assert result is False

    response = client.get("/is_prime/97")
    assert response.status_code == 200

    result = response.json()
    assert result is True

    response = client.get("/is_prime/asd")
    assert response.status_code == 422

    response = client.get("/is_prime/")
    assert response.status_code == 404


def test_fibonacci_endpoint():
    response = client.get("/fibonacci/1")
    assert response.status_code == 200
    assert response.json() == 1

    response = client.get("/fibonacci/2")
    assert response.status_code == 200
    assert response.json() == 1

    response = client.get("/fibonacci/3")
    assert response.status_code == 200
    assert response.json() == 2

    response = client.get("/fibonacci/15")
    assert response.status_code == 200
    assert response.json() == 610

    response = client.get("/fibonacci/17")
    assert response.status_code == 200
    assert response.json() == 1597

    response = client.get("/fibonacci/n")
    assert response.status_code == 422

    response = client.get("/fibonacci/")
    assert response.status_code == 404

