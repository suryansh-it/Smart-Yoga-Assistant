# Initializes the Flask app
from flask import Flask
from flask_migrate import Migrate
from .models import db, User  # Ensure models are imported here
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# from src.flask_app.routes import main  # Use absolute import

# Initialize Flask extensions
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config.from_prefixed_env()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Initialize bcrypt and login manager
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirect to login page if not authenticated

    # Import and register the blueprints (routes)
    from .routes import main
    from .auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Migrate setup
    migrate = Migrate(app, db)
    
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    
    return app

# Define user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
