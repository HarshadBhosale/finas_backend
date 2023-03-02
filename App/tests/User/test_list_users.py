def testHona(client, hona):
    response = client.get(
        "/users", headers={"Authorization": f"Bearer {hona['access_token']}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == hona["name"]
    assert response.json()[0]["email"] == hona["email"]
    assert response.json()[0].get("password", "") == ""


def testHonaHB(client, hona, hb):
    response = client.get(
        "/users", headers={"Authorization": f"Bearer {hona['access_token']}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == hona["name"]
    assert response.json()[0]["email"] == hona["email"]
    assert response.json()[0].get("password", "") == ""
    assert response.json()[1]["name"] == hb["name"]
    assert response.json()[1]["email"] == hb["email"]
    assert response.json()[1].get("password", "") == ""
