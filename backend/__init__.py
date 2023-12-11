# backend/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config
from backend.extensions import db
from backend.models import User, Meme
from backend.main import main_bp
from backend.auth import auth_bp, init_app as auth_init_app


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Authentication
    auth_init_app(app)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Additional initializations or configurations...
    # Example: app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
