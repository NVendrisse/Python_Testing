import json
from utils import (
    ClubNotFoundError,
    CompetitionNotFoundError,
    PurchaseError,
    get_club_by_email,
    get_club_by_name,
    get_competition,
    purchase_places,
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
    try:
        club = get_club_by_name(clubs, request.form["club"])
        competition = get_competition(competitions, request.form["competition"])
        purchase_places(club, competition, int(request.form["places"]))
        flash("Great booking complete!")
        return render_template("welcome.html", club=club, competitions=competitions)
    except ClubNotFoundError:
        flash("The requested club was not found, please connect again")
        return redirect(url_for("index"))
    except CompetitionNotFoundError:
        flash("The requested competition was not found, please try again")
        return render_template("welcome.html", club=club, competitions=competitions)
    except PurchaseError:
        flash(
            "Oops! Something wrong happened, maybe you don't have enought points, or ask for too much places (ttt), please try again"
        )
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/points-display")
def point_display():
    return render_template("pointdisplay.html", clubs=clubs)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
