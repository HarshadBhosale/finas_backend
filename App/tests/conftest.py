import pytest
from fastapi.testclient import TestClient
from main import api
from Database.Models.base_model import BaseModel


@pytest.fixture()
def client():
    for table in BaseModel.__subclasses__():
        table.create_table()

    yield TestClient(api)

    for table in BaseModel.__subclasses__():
        table.drop_table()


@pytest.fixture()
def hona(client):
    user_data = {
        "name": "hona",
        "email": "hona@hona.com",
        "password": "12345678",
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    user = response.json()
    user["password"] = user_data["password"]
    return user


@pytest.fixture()
def hb(client):
    user_data = {
        "name": "hb",
        "email": "hb@hb.com",
        "password": "12345678",
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    user = response.json()
    user["password"] = user_data["password"]
    return user
