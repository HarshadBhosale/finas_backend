import pytest


@pytest.mark.asyncio
async def testHona(client, hona):
    response = await client.get(
        f"/users/{hona['id']}",
        headers={"Authorization": f"Bearer {hona['access_token']}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == hona["name"]
    assert response.json()["email"] == hona["email"]
    assert response.json().get("password", "") == ""


@pytest.mark.asyncio
async def testHB(client, hb):
    response = await client.get(
        f"/users/{hb['id']}",
        headers={"Authorization": f"Bearer {hb['access_token']}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == hb["name"]
    assert response.json()["email"] == hb["email"]
    assert response.json().get("password", "") == ""
