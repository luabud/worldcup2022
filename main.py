import string
import sys

import httpx

wwc2022_groups = {}


class Team:
    """A soccer/football team that has been qualified to play in the World Cup."""

    def __init__(
        self,
        name: str,
        country: str,
        group_letter: str,
        group_points: int = 0,
        wins: int = 0,
        draws: int = 0,
        losses: int = 0,
        games_played: int = 0,
        goals: dict[str, int] | None = None,
    ) -> None:
        self.name = name
        self.country = country
        self.group_leter = group_letter
        self.group_points = group_points
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.games_played = games_played
        self.goals = goals or {"goals_for": 0, "goals_against": 0}

    def __str__(self) -> str:
        return self.name

    @property
    def goals_difference(self) -> int:
        return self.goals["goals_against"] - self.goals["goals_for"]


class Group:
    """ A set of teams that play against each other in the World Cup."""

    def __init__(self, letter: str, teams: list[Team]) -> None:
        self.letter = letter
        self.teams = teams

    def __str__(self) -> str:
        return self.letter

    def get_n_place(self, n: int) -> Team:
        sorted_team_list = sorted(
            self.teams,
            key=lambda t1: (
                t1.group_points,
                t1.goals_difference,
                t1.goals["goals_for"],
            ),
            reverse=True,
        )
        return sorted_team_list[n - 1]

    def get_first_place(self):
        return self.get_n_place(1)

    def get_second_place(self):
        return self.get_n_place(2)


def load_data():
    data = httpx.request("GET", "https://worldcupjson.net/teams")
    for group in data.json()["groups"]:
        wwc2022_teams = []
        for team in group["teams"]:
            del team["goal_differential"]
            goals = {key: team.pop(key) for key in ["goals_for", "goals_against"]}
            t = Team(**team, goals=goals)
            wwc2022_teams.append(t)
        wwc2022_groups[group["letter"]] = Group(group["letter"], wwc2022_teams)


if __name__ == "__main__":
    load_data()
    if len(sys.argv) > 2 and sys.argv[1] in string.ascii_uppercase[:8]:
        group = wwc2022_groups[sys.argv[1]]
    else:
        group = wwc2022_groups["A"]
    print(group.get_first_place())
