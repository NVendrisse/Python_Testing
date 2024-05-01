from ..conftest import club_fixture, competition_fixture, client
from server import purchasePlaces
import server


def test_purchase_all_valid(client, monkeypatch, competition_fixture, club_fixture):
    """
    GIVEN a Flask application configured for testing with a club list and a competition list
    WHEN the '/purchasePlaces' page is posted (POST) with a valid club, a valid competition, and a valid quantity of asked places
    THEN check that the response is valid
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    form_data = {
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "10",
    }
    response = client.post("/purchasePlaces", data=form_data)
    assert response.status_code == 200


def test_purchase_invalid_club(client, monkeypatch, competition_fixture, club_fixture):
    """
    GIVEN a Flask application configured for testing with a club list and a competition list
    WHEN the '/purchasePlaces' page is posted (POST) with a invalid club, a valid competition, and a valid quantity of asked places
    THEN check that the response is a redirection
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    form_data = {
        "club": "Poire",
        "competition": "Spring Festival",
        "places": "10",
    }
    response = client.post("/purchasePlaces", data=form_data)
    assert response.status_code == 302


def test_purchase_invalid_competition(
    client,
    monkeypatch,
    competition_fixture,
    club_fixture,
):
    """
    GIVEN a Flask application configured for testing with a club list and a competition list
    WHEN the '/purchasePlaces' page is posted (POST) with a valid club, a invalid competition, and a valid quantity of asked places
    THEN check that the response is valid a part of the error message
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    form_data = {
        "club": "Simply Lift",
        "competition": "Banana",
        "places": "10",
    }
    response = client.post("/purchasePlaces", data=form_data)
    page_data = response.data.decode()
    assert response.status_code == 200
    assert "The requested competition was not found" in page_data


def test_purchase_invalid_places_quantity(
    client, monkeypatch, competition_fixture, club_fixture
):
    """
    GIVEN a Flask application configured for testing with a club list and a competition list
    WHEN the '/purchasePlaces' page is posted (POST) with a valid club, a valid competition, and a invalid quantity of asked places
    THEN check that the response is valid and contains a part of the error message
    """
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    form_data = {
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "0",
    }
    response = client.post("/purchasePlaces", data=form_data)
    page_data = response.data.decode()
    assert response.status_code == 200
    assert "Oops!" in page_data
