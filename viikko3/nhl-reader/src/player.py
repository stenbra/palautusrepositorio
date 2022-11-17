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
        return "{0} team {1} goals {2} assists {3}".format(self.name,self.team,self.goals,self.assists)
