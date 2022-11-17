from player import Player
from player_reader import PlayerReader


def sort_by_points(player):
    return player.points

class PlayerStats:
    def __init__(self, playerReader:PlayerReader):
        self.players = playerReader.get_players()

    def top_scorers_by_nationality(self,nationality):
        players=[]
        sorted_players = sorted(self.players,reverse=True,key=sort_by_points)
        for player in sorted_players:
            if(player.get_nationality()==nationality):
                players.append(player)
        return players
