import datetime


class ClubNotFoundError(Exception):
    """
    Error raised if the requested club is not found
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CompetitionNotFoundError(Exception):
    """
    Error raised if the requested competition is not found
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PurchaseError(Exception):
    """
    Error raised if the requested purchase of places does not
    comply with all or on off the parameter
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_club_by_email(clubs: list, request_email: str):
    """
    Function used for retrieving a club from a list of clubs by email
    clubs : list[dict]
    request_email : str
    return a club (dict)
    """
    for club in clubs:
        if club["email"] == request_email:
            return club
    raise ClubNotFoundError


def get_club_by_name(clubs: list, request_name: str):
    """
    Function used for retrieving a club from a list of clubs by name
    clubs : list[dict]
    name : str
    return a club (dict)
    """
    for club in clubs:
        if club["name"] == request_name:
            return club
    raise ClubNotFoundError


def get_competition(competitions: list, request_competition_name: str):
    """
    Function used for retrieving a competition from a list of competitions by name
    competitions : list[dict]
    request_competition_name : str
    return a competition (dict)
    """
    for competition in competitions:
        if competition["name"] == request_competition_name:
            return competition
    raise CompetitionNotFoundError


def purchase_places(club, competition, quantity: int):
    """
    Calculation function for purchasing places from a competition
    club : dict
    competition : dict
    quantity : int
    """
    if (
        quantity <= 0
        or quantity > int(club["points"])
        or quantity >= 12
        or quantity > int(competition["numberOfPlaces"])
    ):
        raise PurchaseError
    else:
        competition["numberOfPlaces"] = int(competition["numberOfPlaces"]) - quantity
        club["points"] = int(club["points"]) - quantity


def maximum_purchasable_places(club, competition):
    """
    Calculation function in order to define the maximum purchasable places
    club : dict
    competition : dict
    return an integer
    """
    max_places = 12
    if int(competition["numberOfPlaces"]) < 12:
        max_places = int(competition["numberOfPlaces"])
    if int(club["points"]) < 12:
        max_places = int(club["points"])
    return max_places


def date_checker(competition):
    today = datetime.datetime.today()
    competition_date = datetime.datetime.strptime(
        competition["date"], "%Y-%m-%d %H:%M:%S"
    )
    if competition_date < today:
        update_data = {"is_over": True}
        competition.update(update_data)
