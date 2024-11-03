from src.flask_app.models import User

def test_home(client):
    response=client.get("/")
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data #b ; to convert to bytes for data to analyse

def test_registration(client,app):
#  need to use with app,context so app
    response = client.post('/register', data={"hashed_password":"sfsfrgrg", "user": "srrfr"})

    with app.app_context():
        assert User.query.count() ==2