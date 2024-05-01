from ..conftest import club_fixture, competition_fixture, client
from server import book
import server


def test_book_valid_club(client, monkeypatch, club_fixture, competition_fixture):
    """
    GIVEN a Flask application configured for testing with a club list and a competition list
    WHEN the '/book' page is requested (GET) with an existing club and an existing competition
    THEN check that the response is valid
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Spring%20Festival/Iron%20Temple")
    assert response.status_code == 200


def test_book_invalid_club(client, monkeypatch, club_fixture, competition_fixture):
    """
    GIVEN a Flask application configured for testing a club list and a competition list
    WHEN the '/book' page is requested (GET) with a wrong club and an existing competition
    THEN check that the response is a redirection
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Spring%20Festival/Pomme")
    assert response.status_code == 302


def test_book_invalid_competiton(
    client, monkeypatch, club_fixture, competition_fixture
):
    """
    GIVEN a Flask application configured for testing a club list and a competition list
    WHEN the '/book' page is requested (GET) with an existing club and a wrong competition
    THEN check that the response is a redirection and contains the error message
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Pomme/Iron%20Temple")
    page_data = response.data.decode()
    assert response.status_code == 200
    assert (
        "The requested competition was not found, please connect and try again"
        in page_data
    )
