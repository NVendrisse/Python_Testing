import json
from utils import (
    ClubNotFoundError,
    CompetitionNotFoundError,
    get_club_by_email,
    get_club_by_name,
    get_competition,
)
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"


competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    try:
        club = get_club_by_email(clubs, str(request.form["email"]))
    except ClubNotFoundError:
        flash(
            "This account doesn't exist, please make sure that you enterred your email properly"
        )
        return redirect(url_for("index"))
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition: str, club: str):
    try:
        foundClub = get_club_by_name(clubs, club)
        foundCompetition = get_competition(competitions, competition)
    except ClubNotFoundError:
        flash("The requested club was not found, please connect again")
        return redirect(url_for("index"))
    except CompetitionNotFoundError:
        flash("The requested competition was not found, please connect and try again")
        return redirect(url_for("index"))
    return render_template("booking.html", club=foundClub, competition=foundCompetition)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - placesRequired
    flash("Great booking complete!")
    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
