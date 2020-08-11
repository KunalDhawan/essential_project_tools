from starlette.testclient import TestClient
from ...server import app

client = TestClient(app)

def test_factorial_api():

    input_number = 5

    body = {"input_number": input_number}
    response = client.post("/compute/factorial", json=body)

    assert response.status_code == 200
    assert response.json().get("factorial") == 120

def test_factorial_negative():

    input_number = -5

    body = {"input_number": input_number}
    response = client.post("/compute/factorial", json=body)

    assert response.status_code == 200
    assert response.json().get("factorial") == -2