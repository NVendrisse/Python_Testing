from ..conftest import club_fixture, competition_fixture, client
from server import book
import server


def test_book_valid_club(client, monkeypatch, club_fixture, competition_fixture):
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Spring%20Festival/Iron%20Temple")
    assert response.status_code == 200


def test_book_invalid_club(client, monkeypatch, club_fixture, competition_fixture):
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Spring%20Festival/Pomme")
    page_data = response.data.decode()
    assert response.status_code == 302


def test_book_invalid_competiton(
    client, monkeypatch, club_fixture, competition_fixture
):
    monkeypatch.setattr(server, "clubs", club_fixture)
    monkeypatch.setattr(server, "competitions", competition_fixture)
    response = client.get("/book/Pomme/Iron%20Temple")
    page_data = response.data.decode()
    assert response.status_code == 302
