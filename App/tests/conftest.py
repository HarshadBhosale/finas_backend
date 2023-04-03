import pytest_asyncio
from main import api
from httpx import AsyncClient
from Database.Models.base_model import BaseModel


@pytest_asyncio.fixture()
async def client():
    for table in BaseModel.__subclasses__():
        table.create_table()

    async with AsyncClient(app=api, base_url="http://localhost:8000") as testClient:
        yield testClient

    for table in BaseModel.__subclasses__():
        table.drop_table()


@pytest_asyncio.fixture()
async def hona(client):
    user_data = {
        "name": "hona",
        "email": "hona@hona.com",
        "password": "12345678",
    }
    response = await client.post("/users/", json=user_data)
    assert response.status_code == 201
    user = response.json()
    user["password"] = user_data["password"]
    return user


@pytest_asyncio.fixture()
async def hb(client):
    user_data = {
        "name": "hb",
        "email": "hb@hb.com",
        "password": "12345678",
    }
    response = await client.post("/users/", json=user_data)
    assert response.status_code == 201
    user = response.json()
    user["password"] = user_data["password"]
    return user
