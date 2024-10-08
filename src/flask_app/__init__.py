# Initializes the Flask app
from flask import Flask
from flask_migrate import Migrate
from .models import db

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app,db)
    with app.app_context():
        db.create_all()
    return app