from ..conftest import client
from server import logout


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    page_data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in page_data
