from main import API_VERSION
from Database.Models.roots import RootResponseModel
import pytest


@pytest.mark.asyncio
async def testRoot(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == RootResponseModel(API=API_VERSION)
