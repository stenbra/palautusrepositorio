import requests
import time
from player import Player

def sort_by_points(player):
    return player.goals + player.assists
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    ##print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],player_dict['team'],player_dict['nationality'],
            player_dict['goals'],player_dict['assists'],player_dict['penalties'],
            player_dict['games']
        )

        players.append(player)

    sorted_players = sorted(players,reverse=True,key=sort_by_points)
    print("Players from FIN")

    for player in sorted_players:
        if(player.get_nationality()=="FIN"):
            print(player)

if __name__ == "__main__":
    main()
