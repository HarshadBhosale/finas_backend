from main import API_VERSION
from Database.Models.roots import RootResponseModel


def testRoot(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == RootResponseModel(API=API_VERSION)
