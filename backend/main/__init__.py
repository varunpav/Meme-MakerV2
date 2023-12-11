from flask import Blueprint

main_bp = Blueprint('main', __name__)

from backend.main import routes  # Importing routes at the end to avoid circular dependencies
