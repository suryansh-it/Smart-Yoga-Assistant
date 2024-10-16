import sys
import os

# Add the project root to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src.flask_app import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port = 8009)
