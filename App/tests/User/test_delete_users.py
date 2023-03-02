def testHona(client, hona):
    hona["name"] = "King"
    response = client.delete(
        f"/users/{hona['id']}",
        headers={"Authorization": f"Bearer {hona['access_token']}"},
    )
    assert response.status_code == 204


def testHB(client, hb):
    hb["name"] = "boss"
    response = client.delete(
        f"/users/{hb['id']}",
        headers={"Authorization": f"Bearer {hb['access_token']}"},
    )
    assert response.status_code == 204
