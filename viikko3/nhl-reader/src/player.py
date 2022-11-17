class Player:
    def __init__(self, name,team,nationality,goals,assists,penalties,games):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
        self.games =games

    def get_nationality(self):
        return self.nationality

    def __str__(self):
        return f"{self.name:20}  {self.team:2}  {self.goals:2} + {self.assists:2} = {self.goals+self.assists:2}"
