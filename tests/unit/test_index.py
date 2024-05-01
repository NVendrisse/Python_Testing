from server import index
from ..conftest import client


def test_index(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and the page data contain "Welcome"
    """
    response = client.get()
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome" in data
