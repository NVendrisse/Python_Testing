from ..conftest import club_fixture, client
from server import point_display
import server


def test_display(monkeypatch, club_fixture, client):
    """
    GIVEN a Flask application configured for testing with a club list
    WHEN the '/points-display' page is requested (GET)
    THEN check that the response is valid and contains the data from the pointdisplay.html file
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    response = client.get("/points-display")
    page_data = response.data.decode()
    assert response.status_code == 200
    assert "Here you can find all the available points for each club" in page_data
