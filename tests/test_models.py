# tests/test_models.py
import pytest
from backend.models import User, Meme

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and username fields are defined correctly
    """
    user = User(username='john_doe', email='john@example.com')
    user.set_password('FlaskIsAwesome')
    assert user.email == 'john@example.com'
    assert user.username == 'john_doe'
    assert user.check_password('FlaskIsAwesome')
    assert not user.check_password('NotThePassword')
