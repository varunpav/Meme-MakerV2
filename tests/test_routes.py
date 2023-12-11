# tests/test_routes.py
def test_index_route(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Meme Maker" in response.data  # Assuming this text is in your index.html
