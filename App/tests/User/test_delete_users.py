import pytest


@pytest.mark.asyncio
async def testHona(client, hona):
    hona["name"] = "King"
    response = await client.delete(
        f"/users/{hona['id']}",
        headers={"Authorization": f"Bearer {hona['access_token']}"},
    )
    assert response.status_code == 204


@pytest.mark.asyncio
async def testHB(client, hb):
    hb["name"] = "boss"
    response = await client.delete(
        f"/users/{hb['id']}",
        headers={"Authorization": f"Bearer {hb['access_token']}"},
    )
    assert response.status_code == 204
