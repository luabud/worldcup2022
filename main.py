from typing import List


class Team:
    def __init__(self, name: str, players: List[str] = None, year: object = None):
        self.name = name
        self.players = players
        self.year = year

    def __str__(self):
        return self.name


class Match:
    def __init__(self, first_team: Team, second_team: Team):
        self.first_team = first_team
        self.second_team = second_team
        self.year = first_team.year
        self.has_ended = False
        self.result = [0, 0]

    def end_match(self, first_team_score: int, second_team_score: int):
        self.result = [first_team_score, second_team_score]
        self.has_ended = True

    def get_winner(self):
        if not self.has_ended:
            raise Exception("Match hasn't ended yet!")
        if self.result[0] == self.result[1]:
            return f"{self.first_team} tied with {self.second_team}"
        return str(self.first_team) if self.result[0] > self.result[1] else str(self.second_team)

br = Team("Brazil",
          players=["David Luiz", "Júlio César", "Maicon", "Marcelo", "Dante", "Fernandinho", "Dante", "Hulk", "Neymar Jr.",
           "Thiago Silva"], year=2014)

ge = Team("Germany", players=["Manuel Neuer", "Philipp Lahm", "Benedikt Höwedes", "Sami Khedira", "Thomas Müller", "Mesut Özil",
                      "Miroslav Klose"], year=2014)

match = Match(br, ge)
match.end_match(1, 7)
print(match.get_winner())

