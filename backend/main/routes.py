from flask import render_template
from backend.main import main_bp

@main_bp.route('/')
def index():
    return render_template('index.html')  # Assuming you have an index.html template in your templates directory
