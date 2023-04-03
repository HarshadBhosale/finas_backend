import pytest


@pytest.mark.asyncio
async def testHona(client, hona):
    hona["name"] = "King"
    response = await client.put(
        f"/users/{hona['id']}",
        headers={"Authorization": f"Bearer {hona['access_token']}"},
        json={"name": hona["name"]},
    )
    assert response.status_code == 202
    assert response.json()["name"] == hona["name"]
    assert response.json()["email"] == hona["email"]
    assert response.json().get("password", "") == ""


@pytest.mark.asyncio
async def testHB(client, hb):
    hb["name"] = "boss"
    response = await client.put(
        f"/users/{hb['id']}",
        headers={"Authorization": f"Bearer {hb['access_token']}"},
        json={"name": hb["name"]},
    )
    assert response.status_code == 202
    assert response.json()["name"] == hb["name"]
    assert response.json()["email"] == hb["email"]
    assert response.json().get("password", "") == ""
