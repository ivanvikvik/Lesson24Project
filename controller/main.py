from model import *


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Cristiano", "Ronaldo", 840, 300)
    alex = FootballPlayer("Alessandro", "Del Piero", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    players = (cristiano, alex, ivan, leo, 10, [])

    for player in players:
        print(player)

    player = Manager.give_golden_ball(players)

    print(f"\nBest player is {player}")


if __name__ == "__main__":
    main()
