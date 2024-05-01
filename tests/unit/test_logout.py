from ..conftest import client
from server import logout


def test_logout(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check that the response is valid and contains the data from the index.html file
    """
    response = client.get("/logout", follow_redirects=True)
    page_data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in page_data
