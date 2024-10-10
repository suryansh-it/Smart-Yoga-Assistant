# Initializes the Flask app
from flask import Flask
from flask_migrate import Migrate
from .models import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirect to login if not authenticated

    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    migrate = Migrate(app,db)
    with app.app_context():
        db.create_all()
    return app