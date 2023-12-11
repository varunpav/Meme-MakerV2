# auth/__init__.py

from flask import Blueprint
from authlib.integrations.flask_client import OAuth
from . import routes  # Import routes

# Initialize Blueprint
auth_bp = Blueprint('auth', __name__)

# Initialize OAuth
oauth = OAuth()


# Configuration for Google OAuth
def init_app(app):
    oauth.init_app(app)

    # Register Google as an OAuth client
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid email profile'},
    )

