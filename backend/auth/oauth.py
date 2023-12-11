from flask import redirect, url_for, session, Blueprint
from . import oauth  # Import the OAuth instance

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login/google')
def google_login():
    google = oauth.create_client('google')  # Create a Google OAuth client
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route('/authorize/google')
def google_authorize():
    google = oauth.create_client('google')  # Create a Google OAuth client
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    # Implement logic to create/login user
    return redirect(url_for('main.index'))
