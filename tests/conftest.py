#to setup test env. for things that'll get called before every test

import pytest
from src.flask_app.models import db
from src.flask_app.__init__ import create_app
#fixture : something that is available to every test

@pytest.fixture()
def app():
    app= create_app() #temp database fot test ,destroyed after test is completed
    FLASK_SQLALCHEMY_DATABASE_URI = 'sqlite://'
    with app.app_context():
        db.create_all()  #put models in databse

    yield app  #anythin before the yield is setup for the test

    #teardown for above fixture
    #pytest will run the code after yield , once the test is finished running : nothing in this case

@pytest.fixture()
def client(app):
#can pass fixtures as args/parameter to other fixtures or test
#we are just defining fixture as parameter, pitest will match the para name and pass the fixture

    return app.test_client() #allow us to simulate requests

