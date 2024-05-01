from ..conftest import client
import server

USER = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}


def test_global(client):
    """
    GIVEN a Flask application configured for testing with a valid user and premade valid form data
    WHEN the user is using the application
    THEN check that all the response are valid
    """
    user = {"email": USER["email"]}
    form_data = {
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "10",
    }

    response = client.get("/")
    page_data = response.data.decode()
    assert response.status_code == 200
    response = client.post("/showSummary", data=user)
    page_data = response.data.decode()
    assert response.status_code == 200
    response = client.get("/book/Spring%20Festival/Simply%20Lift")
    page_data = response.data.decode()
    assert response.status_code == 200
    response = client.post("/purchasePlaces", data=form_data)
    page_data = response.data.decode()
    assert response.status_code == 200
    response = client.get("/logout", follow_redirects=True)
    page_data = response.data.decode()
    assert response.status_code == 200
    response = client.get("/points-display")
    page_data = response.data.decode()
    assert response.status_code == 200
