from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, Not, HasAtLeast, Or, HasFewerThan, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
