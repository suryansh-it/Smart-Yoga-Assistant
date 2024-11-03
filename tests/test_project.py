def test_home(client):
    response=client.get("/")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data #b ; to convert to bytes for data to analyse