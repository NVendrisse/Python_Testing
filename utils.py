class ClubNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class CompetitionNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PurchaseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_club_by_email(clubs: list, request_email: str):
    for club in clubs:
        if club["email"] == request_email:
            return club
    raise ClubNotFoundError


def get_club_by_name(clubs: list, request_name: str):
    for club in clubs:
        if club["name"] == request_name:
            return club
    raise ClubNotFoundError


def get_competition(competitions: list, request_competition_name: str):
    for competition in competitions:
        if competition["name"] == request_competition_name:
            return competition
    raise CompetitionNotFoundError


def purchase_places(club, competition, quantity: int):
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
