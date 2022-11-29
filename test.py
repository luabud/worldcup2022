from models.team import Team
from models.match import Match


def test_match_year():
    match = Match(Team("Brazil", year=2014), Team("Germany", year=2014))
    match.end_match(1, 7)
    assert match.year == match.first_team.year == match.second_team.year


def test_0_score():
    match = Match(Team("Cameroon", year=2022), Team("Brazil", year=2022))
    assert not (sum(match.result) or match.has_ended)

