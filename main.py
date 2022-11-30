from typing import List
import httpx

wwc2022_groups = {}

class Team:
    def __init__(self, name: str, country: str, group_letter: str, group_points: int = 0,
                 wins: int = 0, draws:int = 0, losses: int = 0, games_played: int = 0,
                 goals=None):
        if goals is None:
            goals = {"goals_for": 0, "goals_against": 0}
        self.name = name
        self.country = country
        self.group_leter = group_letter
        self.group_points = group_points
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.games_played = games_played
        self.goals = goals

    def get_goals_difference(self):
        return self.goals["goals_against"] - self.goals["goals_for"]

    def __str__(self):
        return self.name

class Group:
    def __init__(self, letter: str, teams: List[Team]):
        self.letter = letter
        self.teams = teams
    def __str__(self):
        return self.letter
    def get_n_place(self, n):
        sorted_team_list = sorted(self.teams, key=lambda t1: (t1.group_points, t1.get_goals_difference(), t1.goals["goals_for"]), reverse=True)
        return sorted_team_list[n-1]
    def get_first_place(self):
        return self.get_n_place(1)
    def get_second_place(self):
        return self.get_n_place(2)


def load_data():
    data = httpx.request("GET", "https://worldcupjson.net/teams")
    for group in data.json()["groups"]:
        wwc2022_teams = []
        for team in group["teams"]:
            t = Team(team["name"], team["group_letter"], team["country"], team["group_points"],
                     team["wins"], team["draws"], team["losses"], team["games_played"], {"goals_for": team["goals_for"], "goals_against": team["goals_against"]})
            wwc2022_teams.append(t)
        wwc2022_groups[group["letter"]] = Group(group["letter"], wwc2022_teams)

if __name__ == "__main__":
    load_data()
    group_a = wwc2022_groups["A"]
    print(group_a.get_first_place())

