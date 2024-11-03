#to setup test env. for things that'll get called before every test

import pytest
from src.flask_app.models import db
from src.flask_app.__init__ import create_app
#fixture : something that is available to every test

@pytest.fixture()
def app():
    app= create_app("sqlite://") #temp database fot test ,destroyed after test is completed
    with app.app_context():
        db.create_all()  #put models in databse

    yield app  #anythin before the yield is setup for the test

    #teardown for above fixture
    #pytest will run the code after yield , once the test is finished running : nothing in this case


